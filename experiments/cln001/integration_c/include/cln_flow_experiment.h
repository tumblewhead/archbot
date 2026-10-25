#ifndef CLN_FLOW_EXPERIMENT_H
#define CLN_FLOW_EXPERIMENT_H
/* Exploratory S rendezvous with one publisher slot and one owed result.
 * Busy means NOT accepted. The caller must retain and retry that input.
 * Consumer rank is inferred from ordered receipts, not from a transmitted n.
 * No crash atomicity, arbitrary index, or real ADC buffering is guaranteed.
 */
#include "cln_sync_experiment.h"
#include <stdint.h>
typedef enum {
    CLN_FLOW_OK=0, CLN_FLOW_BUSY, CLN_FLOW_EMPTY, CLN_FLOW_INVALID,
    CLN_FLOW_REJECT, CLN_FLOW_EXHAUSTED, CLN_FLOW_RESET_REQUIRED
} cln_flow_status;
typedef struct {
    uint64_t sequence, ordinal; /* consumer-owned, hypothetical retained */
} cln_flow_consumer;
typedef struct {
    cln_sync_experiment detector;
    cln_flow_consumer consumer;
    uint32_t offered_value;  /* publisher-owned in the hypothetical contract */
    uint32_t owed_energy;     /* one detector-owned, unpublished result */
    uint8_t has_offer, has_debt, wants_reset;
} cln_flow_experiment;
void cln_flow_init(cln_flow_experiment *s, cln_algorithm algorithm);
cln_flow_status cln_flow_offer(cln_flow_experiment *s, uint32_t value);
cln_flow_status cln_flow_commit(cln_flow_experiment *s);
cln_flow_status cln_flow_receive(cln_flow_experiment *s, cln_observation *out);
cln_flow_status cln_flow_request_reset(cln_flow_experiment *s);
cln_flow_status cln_flow_complete_reset(cln_flow_experiment *s);
#endif
