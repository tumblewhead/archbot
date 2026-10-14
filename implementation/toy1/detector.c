#include "detector.h"

void detector_init(detector_t *detector)
{
    unsigned i;
    for (i = 0; i < DETECTOR_WINDOW; ++i) {
        detector->samples[i] = 0u;
    }
    detector->oldest = 0u;
    detector->sum_squares = 0u;
}

void detector_reset(detector_t *detector)
{
    detector_init(detector);
}

uint32_t detector_accept(detector_t *detector, uint16_t sample)
{
    const uint16_t old = detector->samples[detector->oldest];
    /* Cast before multiplication so the product is evaluated in uint32_t. */
    const uint32_t incoming_square = (uint32_t)sample * (uint32_t)sample;
    const uint32_t outgoing_square = (uint32_t)old * (uint32_t)old;
    const uint32_t next_sum = detector->sum_squares + incoming_square
                            - outgoing_square;

    detector->samples[detector->oldest] = sample;
    detector->oldest = (uint8_t)((detector->oldest + 1u) & 31u);
    detector->sum_squares = next_sum;
    return next_sum;
}
