#include "cln_sync_experiment.h"
#include <stdint.h>

void cln_sync_init(cln_sync_experiment *s, cln_algorithm algorithm) {
    if (!s) return;
    s->algorithm = algorithm;
    s->sequence = 0;
    s->ordinal = 0;
    if (algorithm == CLN_A_RAW) cln_raw_reset(&s->num.a);
    else if (algorithm == CLN_B_SQUARE) cln_square_reset(&s->num.b);
}

cln_sync_status cln_sync_input(cln_sync_experiment *s, uint32_t value, cln_observation *out) {
    if (!s || !out || (s->algorithm != CLN_A_RAW && s->algorithm != CLN_B_SQUARE))
        return CLN_SYNC_INVALID;
    if (value > CLN_MAX_SAMPLE) return CLN_SYNC_REJECT;
    /* Refuse beyond model's representable rank, do not silently wrap.
     * This reveals an unclosed full-AS requirement, NOT an approved epoch cap. */
    if (s->ordinal == UINT64_MAX) return CLN_SYNC_EXHAUSTED;
    uint32_t energy = 0;
    cln_status result = s->algorithm == CLN_A_RAW
        ? cln_raw_accept(&s->num.a, value, &energy)
        : cln_square_accept(&s->num.b, value, &energy);
    if (result != CLN_ACCEPTED) return CLN_SYNC_INVALID;
    ++s->ordinal;
    *out = (cln_observation){s->sequence, s->ordinal, energy};
    return CLN_SYNC_OK;
}

cln_sync_status cln_sync_reset(cln_sync_experiment *s) {
    if (!s || (s->algorithm != CLN_A_RAW && s->algorithm != CLN_B_SQUARE))
        return CLN_SYNC_INVALID;
    if (s->sequence == UINT64_MAX) return CLN_SYNC_EXHAUSTED;
    /* All output is synchronous here: no in-flight debt in this narrow model.
     * Does not license an actual distributed drain/ACK assumption. */
    if (s->algorithm == CLN_A_RAW) cln_raw_reset(&s->num.a);
    else cln_square_reset(&s->num.b);
    ++s->sequence;
    s->ordinal = 0;
    return CLN_SYNC_OK;
}
