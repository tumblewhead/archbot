#include "cln_flow_experiment.h"
#include <stdint.h>

static int valid(const cln_flow_experiment *s) {
    return s && (s->detector.algorithm == CLN_A_RAW || s->detector.algorithm == CLN_B_SQUARE);
}
void cln_flow_init(cln_flow_experiment *s, cln_algorithm a) {
    if (!s) return;
    cln_sync_init(&s->detector, a);
    s->consumer=(cln_flow_consumer){0,0};
    s->offered_value=0;s->owed_energy=0;
    s->has_offer=0;s->has_debt=0;s->wants_reset=0;
}
cln_flow_status cln_flow_offer(cln_flow_experiment *s, uint32_t value) {
    if (!valid(s)) return CLN_FLOW_INVALID;
    if (value > CLN_MAX_SAMPLE) return CLN_FLOW_REJECT;
    if (s->has_offer) return CLN_FLOW_BUSY;
    s->offered_value=value;s->has_offer=1;
    return CLN_FLOW_OK;
}
cln_flow_status cln_flow_commit(cln_flow_experiment *s) {
    if (!valid(s)) return CLN_FLOW_INVALID;
    if (s->wants_reset) return CLN_FLOW_RESET_REQUIRED;
    if (s->has_debt) return CLN_FLOW_BUSY;
    if (!s->has_offer) return CLN_FLOW_EMPTY;
    cln_observation internal={0};
    const cln_sync_status status=cln_sync_input(&s->detector,s->offered_value,&internal);
    if (status==CLN_SYNC_EXHAUSTED) return CLN_FLOW_EXHAUSTED;
    if (status!=CLN_SYNC_OK) return CLN_FLOW_INVALID;
    s->owed_energy=internal.energy;
    s->has_offer=0;s->has_debt=1;
    return CLN_FLOW_OK;
}
cln_flow_status cln_flow_receive(cln_flow_experiment *s, cln_observation *out) {
    if (!valid(s) || !out) return CLN_FLOW_INVALID;
    if (!s->has_debt) return CLN_FLOW_EMPTY;
    if (s->consumer.ordinal == UINT64_MAX) return CLN_FLOW_EXHAUSTED;
    /* Atomic receipt plus debt discharge in this model only.
     * Consumer sees ONLY the ordered energy, not detector ordinal. */
    ++s->consumer.ordinal;
    *out=(cln_observation){s->consumer.sequence,s->consumer.ordinal,s->owed_energy};
    s->has_debt=0;
    return CLN_FLOW_OK;
}
cln_flow_status cln_flow_request_reset(cln_flow_experiment *s) {
    if (!valid(s)) return CLN_FLOW_INVALID;
    s->wants_reset=1;
    return CLN_FLOW_OK;
}
cln_flow_status cln_flow_complete_reset(cln_flow_experiment *s) {
    if (!valid(s)) return CLN_FLOW_INVALID;
    if (!s->wants_reset) return CLN_FLOW_RESET_REQUIRED;
    if (s->has_debt) return CLN_FLOW_BUSY;
    if (s->consumer.sequence==UINT64_MAX) return CLN_FLOW_EXHAUSTED;
    const cln_sync_status result=cln_sync_reset(&s->detector);
    if (result==CLN_SYNC_EXHAUSTED) return CLN_FLOW_EXHAUSTED;
    if (result!=CLN_SYNC_OK) return CLN_FLOW_INVALID;
    /* S orders successful old receipts before this reset marker.
     * A previously offered (not accepted) sample remains staged. */
    ++s->consumer.sequence;s->consumer.ordinal=0;
    s->wants_reset=0;
    return CLN_FLOW_OK;
}
