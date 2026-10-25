#include "cln_flow_experiment.h"
#include <assert.h>
#include <inttypes.h>
#include <stdio.h>
#include <string.h>

typedef struct {uint16_t prev[32];uint32_t count;uint64_t rank,sequence;} oracle;
static void oracle_reset(oracle*o){memset(o->prev,0,sizeof o->prev);o->count=0;o->rank=0;++o->sequence;}
static uint32_t oracle_accept(oracle*o,uint32_t v){
    uint32_t e=v*v;
    for(unsigned i=0;i<31u;++i)e+=(uint32_t)o->prev[i]*o->prev[i];
    for(unsigned i=31u;i>0u;--i)o->prev[i]=o->prev[i-1u];
    o->prev[0]=(uint16_t)v;++o->count;++o->rank;return e;
}
static uint32_t seed=UINT32_C(0x81700901);
static uint32_t next_rand(void){seed^=seed<<13;seed^=seed>>17;seed^=seed<<5;return seed;}

static uint64_t exercise(cln_algorithm alg){
    cln_flow_experiment f;cln_flow_init(&f,alg);oracle o={0};
    uint64_t accepted=0;
    assert(cln_flow_commit(&f)==CLN_FLOW_EMPTY);
    assert(cln_flow_receive(&f,&(cln_observation){0})==CLN_FLOW_EMPTY);
    for(unsigned i=0;i<55000u;++i){
        if(i%247u==0u){
            assert(cln_flow_request_reset(&f)==CLN_FLOW_OK);
            assert(cln_flow_complete_reset(&f)==CLN_FLOW_OK);
            oracle_reset(&o);
        }
        uint32_t v=next_rand()&4095u;
        if(i%193u==0u)v=4095u;
        if(i%199u==0u)v=0u;
        if(i%151u==0u){
            cln_flow_experiment before=f;
            assert(cln_flow_offer(&f,UINT32_MAX)==CLN_FLOW_REJECT);
            assert(memcmp(&before,&f,sizeof f)==0);
        }
        assert(cln_flow_offer(&f,v)==CLN_FLOW_OK);
        cln_flow_experiment old=f;
        assert(cln_flow_offer(&f,2u)==CLN_FLOW_BUSY);
        assert(memcmp(&old,&f,sizeof f)==0);
        assert(cln_flow_commit(&f)==CLN_FLOW_OK);
        uint32_t expected=oracle_accept(&o,v);
        ++accepted;
        assert(f.has_debt && !f.has_offer);
        assert(cln_flow_commit(&f)==CLN_FLOW_BUSY);
        if(i%71u==0u){
            assert(cln_flow_request_reset(&f)==CLN_FLOW_OK);
            old=f;
            assert(cln_flow_complete_reset(&f)==CLN_FLOW_BUSY);
            assert(memcmp(&old,&f,sizeof f)==0);
            assert(cln_flow_offer(&f,1u)==CLN_FLOW_OK); /* pending producer slot */
            assert(cln_flow_commit(&f)==CLN_FLOW_RESET_REQUIRED);
        }
        cln_observation obs={0};
        assert(cln_flow_receive(&f,&obs)==CLN_FLOW_OK);
        assert(obs.sequence==o.sequence && obs.ordinal==o.rank && obs.energy==expected);
        assert(!f.has_debt);
        assert(cln_flow_receive(&f,&obs)==CLN_FLOW_EMPTY); /* no double receipt */
        if(f.wants_reset){
            assert(f.has_offer);
            assert(cln_flow_complete_reset(&f)==CLN_FLOW_OK);
            oracle_reset(&o);
            assert(cln_flow_commit(&f)==CLN_FLOW_OK); /* offered sample accepted after marker */
            expected=oracle_accept(&o,1u);
            ++accepted;
            assert(cln_flow_receive(&f,&obs)==CLN_FLOW_OK);
            assert(obs.sequence==o.sequence && obs.ordinal==o.rank && obs.energy==expected);
        }
    }
    /* A finite rank exhausts: an offered valid event is not silently accepted. */
    f.detector.ordinal=UINT64_MAX;
    assert(cln_flow_offer(&f,1u)==CLN_FLOW_OK);
    cln_flow_experiment snapshot=f;
    assert(cln_flow_commit(&f)==CLN_FLOW_EXHAUSTED);
    assert(memcmp(&snapshot,&f,sizeof f)==0);
    /* Lost consumer context while detector continues: the energy-only interface
     * fails exact index association, rather than secretly using detector rank. */
    cln_flow_init(&f,alg);o=(oracle){0};
    cln_observation first={0},second={0};
    assert(cln_flow_offer(&f,0u)==CLN_FLOW_OK);
    assert(cln_flow_commit(&f)==CLN_FLOW_OK);
    assert(cln_flow_receive(&f,&first)==CLN_FLOW_OK);
    f.consumer.ordinal=0; /* unsupported restart with lost persistent state */
    assert(cln_flow_offer(&f,0u)==CLN_FLOW_OK);
    assert(cln_flow_commit(&f)==CLN_FLOW_OK);
    assert(cln_flow_receive(&f,&second)==CLN_FLOW_OK);
    assert(first.ordinal==1u && second.ordinal==1u && f.detector.ordinal==2u);
    return accepted;
}
int main(void){
    uint64_t a=exercise(CLN_A_RAW),b=exercise(CLN_B_SQUARE);
    assert(a==b);
    printf("{\"study\":\"CLN001-FLOW-001\",\"accepted_per_algorithm\":%" PRIu64 ",\"algorithms\":2,\"assertions_complete\":true,\"model_scope_only\":true,\"full_AS_pass\":false,\"actual_publisher_verified\":false}\n",a);
    return 0;
}
