#include "detector.h"

#include <assert.h>
#include <stddef.h>
#include <stdio.h>

/* Independent newest-32 reference queue, shifted on each accepted sample. */
static uint32_t reference_accept(uint16_t history[DETECTOR_WINDOW], uint16_t x)
{
    uint32_t sum = 0u;
    size_t i;
    for (i = 0; i + 1u < DETECTOR_WINDOW; ++i) {
        history[i] = history[i + 1u];
    }
    history[DETECTOR_WINDOW - 1] = x;
    for (i = 0; i < DETECTOR_WINDOW; ++i) {
        const uint32_t value = history[i];
        sum += value * value;
    }
    return sum;
}

static void compare_sequence(const uint16_t *values, size_t count)
{
    detector_t d;
    uint16_t history[DETECTOR_WINDOW] = {0};
    size_t i;
    detector_init(&d);
    for (i = 0; i < count; ++i) {
        const uint32_t expected = reference_accept(history, values[i]);
        assert(detector_accept(&d, values[i]) == expected);
        assert(d.sum_squares == expected);
    }
}

int main(void)
{
    detector_t d;
    uint16_t max_run[96];
    uint16_t mixed[160];
    size_t i;

    detector_init(&d);
    assert(d.sum_squares == 0u);
    assert(detector_accept(&d, 0u) == 0u);
    assert(detector_accept(&d, DETECTOR_MAX_SAMPLE)
           == 16769025u);
    detector_reset(&d);
    assert(d.sum_squares == 0u);
    assert(d.oldest == 0u);
    for (i = 0; i < DETECTOR_WINDOW; ++i) {
        assert(d.samples[i] == 0u);
    }

    for (i = 0; i < sizeof max_run / sizeof max_run[0]; ++i) {
        max_run[i] = DETECTOR_MAX_SAMPLE;
    }
    compare_sequence(max_run, sizeof max_run / sizeof max_run[0]);

    for (i = 0; i < sizeof mixed / sizeof mixed[0]; ++i) {
        /* Legal-domain deterministic pattern; exercises many ring wraps. */
        mixed[i] = (uint16_t)((i * 977u + (i / 3u) * 131u) & 4095u);
    }
    compare_sequence(mixed, sizeof mixed / sizeof mixed[0]);

    detector_init(&d);
    for (i = 0; i < DETECTOR_WINDOW; ++i) {
        assert(detector_accept(&d, DETECTOR_MAX_SAMPLE)
               == (uint32_t)(i + 1u) * 16769025u);
    }
    assert(d.sum_squares == 536608800u);
    assert(detector_accept(&d, 0u) == 519839775u);

    printf("sizeof(detector_t)=%zu bytes; detector checks passed\n",
           sizeof d);
    return 0;
}
