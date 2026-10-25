#include "cln_numeric.h"
#include "cln_sync_experiment.h"
#include <assert.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <string.h>

typedef struct {
    uint16_t ring[32];
    unsigned cursor;
    uint64_t ordinal;
} oracle;
static uint32_t oracle_accept(oracle *o, uint32_t v) {
    uint32_t result = v*v;
    for (unsigned i=0;i<31u;++i) {
        uint32_t a=o->ring[(o->cursor+1u+i)%32u];
        result+=a*a;
    }
    o->ring[o->cursor]=(uint16_t)v;
    o->cursor=(o->cursor+1u)%32u;
    ++o->ordinal;
    return result;
}
static uint32_t prng(uint32_t *s) {
    *s ^= *s << 13;
    *s ^= *s >> 17;
    *s ^= *s << 5;
    return *s;
}
static void check_state(cln_raw31 *a,cln_square31 *b,oracle *o) {
    uint32_t sum=0;
    for(unsigned i=0;i<31u;++i) {
        uint16_t v=o->ring[(o->cursor+1u+i)%32u];
        assert(a->raw[(a->oldest+i)%31u]==v);
        assert(b->square[(b->oldest+i)%31u]==(uint32_t)v*v);
        sum+=(uint32_t)v*v;
    }
    assert(b->sum31==sum);
}
static uint64_t run_numeric(void) {
    cln_raw31 a;cln_square31 b; oracle o={0};
    cln_raw_reset(&a);cln_square_reset(&b);
    uint32_t seed=UINT32_C(0x19960909); uint64_t n=0;
    for(unsigned i=0;i<160000u;++i) {
        if (i%997u==0u) {
            memset(&o,0,sizeof o);cln_raw_reset(&a);cln_square_reset(&b);
        }
        uint32_t v = (i%31u==0u) ? 4095u : ((i%13u==0u) ? 0u : prng(&seed)&4095u);
        if(i%101u==0u) v=65536u;
        if(i%107u==0u) v=4096u;
        if(i%109u==0u) v=UINT32_MAX; /* -1 conversion, no truncation acceptance */
        cln_raw31 olda=a;cln_square31 oldb=b;
        uint32_t ea=UINT32_C(0xdec0de00), eb=UINT32_C(0xdec0de00);
        cln_status ra=cln_raw_accept(&a,v,&ea);
        cln_status rb=cln_square_accept(&b,v,&eb);
        if(v>4095u) {
            assert(ra==CLN_REJECTED_RANGE && rb==CLN_REJECTED_RANGE);
            assert(memcmp(&olda,&a,sizeof a)==0 && memcmp(&oldb,&b,sizeof b)==0);
            assert(ea==UINT32_C(0xdec0de00) && eb==UINT32_C(0xdec0de00));
            continue;
        }
        assert(ra==CLN_ACCEPTED && rb==CLN_ACCEPTED);
        uint32_t expected=oracle_accept(&o,v);
        assert(ea==expected && eb==expected && ea<=CLN_MAX_ENERGY);
        check_state(&a,&b,&o);
        ++n;
    }
    return n;
}
static uint64_t run_uninterrupted(void) {
    cln_raw31 a;cln_square31 b; oracle o={0};
    cln_raw_reset(&a);cln_square_reset(&b);
    for(unsigned k=0;k<32768u;++k) {
        uint32_t v=(k/8u)%4096u, ea=0,eb=0;
        assert(cln_raw_accept(&a,v,&ea)==CLN_ACCEPTED);
        assert(cln_square_accept(&b,v,&eb)==CLN_ACCEPTED);
        assert(ea==oracle_accept(&o,v) && eb==ea);
        check_state(&a,&b,&o);
    }
    return 32768u;
}
static uint64_t run_integration(void) {
    cln_sync_experiment a,b;cln_sync_init(&a,CLN_A_RAW);cln_sync_init(&b,CLN_B_SQUARE);
    oracle o={0};uint64_t accepted=0;
    for(unsigned i=0;i<12345u;++i) {
        if (i%443u==0u) {
            assert(cln_sync_reset(&a)==CLN_SYNC_OK);
            assert(cln_sync_reset(&b)==CLN_SYNC_OK);
            memset(&o,0,sizeof o);
        }
        uint32_t v=(i%53u==0u)?4096u:((i*214013u+2531011u)&4095u);
        cln_observation oa={0},ob={0};
        cln_sync_experiment pre_a=a,pre_b=b;
        cln_sync_status sa=cln_sync_input(&a,v,&oa);
        cln_sync_status sb=cln_sync_input(&b,v,&ob);
        if(v>4095u) {
            assert(sa==CLN_SYNC_REJECT && sb==CLN_SYNC_REJECT);
            assert(memcmp(&a,&pre_a,sizeof a)==0 && memcmp(&b,&pre_b,sizeof b)==0);
        } else {
            assert(sa==CLN_SYNC_OK && sb==CLN_SYNC_OK);
            uint32_t en=oracle_accept(&o,v);
            assert(oa.sequence==a.sequence && oa.ordinal==o.ordinal && oa.energy==en);
            assert(ob.sequence==oa.sequence && ob.ordinal==oa.ordinal && ob.energy==oa.energy);
            ++accepted;
        }
    }
    /* Reject instead of silently wrapping; this is MODEL failure of full AS. */
    a.ordinal=UINT64_MAX;
    cln_sync_experiment before=a;cln_observation o0={0};
    assert(cln_sync_input(&a,2u,&o0)==CLN_SYNC_EXHAUSTED);
    assert(memcmp(&a,&before,sizeof a)==0);
    a.sequence=UINT64_MAX;
    before=a;
    assert(cln_sync_reset(&a)==CLN_SYNC_EXHAUSTED);
    assert(memcmp(&a,&before,sizeof a)==0);
    return accepted;
}
int main(void) {
    assert(sizeof(cln_raw31) <= 2048 && sizeof(cln_square31) <=2048);
    assert(cln_raw_accept(NULL,1u,NULL)==CLN_BAD_ARGUMENT);
    assert(cln_square_accept(NULL,1u,NULL)==CLN_BAD_ARGUMENT);
    uint64_t a=run_numeric(),b=run_uninterrupted(),c=run_integration();
    printf("{\"study\":\"CLN001-C-PROTOTYPE\",\"numeric_accepted\":%llu,\"uninterrupted_accepted\":%llu,\"sync_accepted\":%llu,\"raw_state_bytes\":%zu,\"square_state_bytes\":%zu,\"sync_state_bytes\":%zu,\"full_AS_pass\":false,\"all_assertions_completed\":true}\n",(unsigned long long)a,(unsigned long long)b,(unsigned long long)c,sizeof(cln_raw31),sizeof(cln_square31),sizeof(cln_sync_experiment));
    return 0;
}
