#include "cln_numeric.h"
#include <string.h>

_Static_assert(CLN_TAIL == 31u, "exactly 31 preceding accepted samples");
_Static_assert(CLN_MAX_ENERGY == UINT32_C(32) * UINT32_C(4095) * UINT32_C(4095),
               "sum of squares maximum must fit in uint32_t");

void cln_raw_reset(cln_raw31 *s) {
    if (s != 0) (void)memset(s, 0, sizeof *s);
}

void cln_square_reset(cln_square31 *s) {
    if (s != 0) (void)memset(s, 0, sizeof *s);
}

cln_status cln_raw_accept(cln_raw31 *s, uint32_t value, uint32_t *energy) {
    if (s == 0 || energy == 0) return CLN_BAD_ARGUMENT;
    if (value > CLN_MAX_SAMPLE) return CLN_REJECTED_RANGE;
    uint32_t total = value * value;
    for (unsigned i = 0; i < CLN_TAIL; ++i) {
        uint32_t v = s->raw[i];
        total += v * v;
    }
    /* Consume the old window BEFORE evicting its oldest member. */
    s->raw[s->oldest] = (uint16_t)value;
    s->oldest = (uint8_t)((s->oldest + 1u) % CLN_TAIL);
    *energy = total;
    return CLN_ACCEPTED;
}

cln_status cln_square_accept(cln_square31 *s, uint32_t value, uint32_t *energy) {
    if (s == 0 || energy == 0) return CLN_BAD_ARGUMENT;
    if (value > CLN_MAX_SAMPLE) return CLN_REJECTED_RANGE;
    const uint32_t q = value * value;
    const uint32_t result = s->sum31 + q;
    const uint32_t oldest_q = s->square[s->oldest];
    /* Current output includes previous 31. Next S excludes oldest previous. */
    s->sum31 = result - oldest_q;
    s->square[s->oldest] = q;
    s->oldest = (uint8_t)((s->oldest + 1u) % CLN_TAIL);
    *energy = result;
    return CLN_ACCEPTED;
}
