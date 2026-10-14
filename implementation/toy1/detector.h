#ifndef TOY1_DETECTOR_H
#define TOY1_DETECTOR_H

#include <stdint.h>

enum { DETECTOR_WINDOW = 32, DETECTOR_MAX_SAMPLE = 4095 };

typedef struct {
    uint16_t samples[DETECTOR_WINDOW];
    uint8_t oldest;
    uint32_t sum_squares;
} detector_t;

/* Initialize before accepting input. Reset requires the caller to quiesce
 * acceptance and ensure no operation is in progress through completion. */
void detector_init(detector_t *detector);
void detector_reset(detector_t *detector);

/* Precondition: sample is in [0, 4095], and the detector is initialized.
 * Exactly one update is performed; the returned value is the coherent
 * post-update sum for this call. Out-of-domain behavior is unspecified. */
uint32_t detector_accept(detector_t *detector, uint16_t sample);

#endif
