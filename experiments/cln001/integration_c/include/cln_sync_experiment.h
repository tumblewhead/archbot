#ifndef CLN_SYNC_EXPERIMENT_H
#define CLN_SYNC_EXPERIMENT_H
/* BOUNDED experiment: prospective S interface, not a verified provider.
 * One call returns synchronously. No accepted-but-unpaid result may exist
 * in this API under its model. A real publisher's lossless coordination,
 * consumer restart persistence and arbitrary rank require separate contracts.
 * uint64_t rank/sequence limits are a MODEL LIMIT, not an AS modification.
 */
#include "cln_numeric.h"
#include <stdint.h>

typedef enum { CLN_A_RAW = 0, CLN_B_SQUARE = 1 } cln_algorithm;
typedef struct {
    uint64_t sequence;
    uint64_t ordinal;
    uint32_t energy;
} cln_observation;
typedef struct {
    cln_algorithm algorithm;
    union { cln_raw31 a; cln_square31 b; } num;
    uint64_t sequence;
    uint64_t ordinal;
} cln_sync_experiment;
typedef enum {
    CLN_SYNC_OK=0,
    CLN_SYNC_REJECT=1,
    CLN_SYNC_EXHAUSTED=2,
    CLN_SYNC_INVALID=3
} cln_sync_status;

void cln_sync_init(cln_sync_experiment *s, cln_algorithm algorithm);
cln_sync_status cln_sync_input(cln_sync_experiment *s, uint32_t value, cln_observation *out);
cln_sync_status cln_sync_reset(cln_sync_experiment *s);

#endif
