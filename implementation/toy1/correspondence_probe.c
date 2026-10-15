/* Independent host-only correspondence probe, not part of detector firmware.
 * Explicit checks remain active with NDEBUG defined. All inputs are legal.
 * TOY1_KNOWN_BAD_CONTROL mutates only the reference, never detector.c.
 */
#include "detector.h"
#include <stdint.h>
#include <limits.h>
#include <stdio.h>

#if UINT16_MAX < 4095u
#error "This probe needs a uint16_t capable of legal detector samples"
#endif
#if UINT32_MAX < 553377825u
#error "This probe needs a uint32_t capable of the accepted arithmetic envelope"
#endif

enum { CASES = 8192 };

static void clear_history(uint16_t history[DETECTOR_WINDOW])
{
    unsigned j;
    for (j = 0u; j < DETECTOR_WINDOW; ++j) {
        history[j] = 0u;
    }
}

/* Deliberately different representation: shift oldest out; rescan every
 * sample on each step instead of using an oldest index or rolling subtraction.
 */
static uint32_t reference_accept(uint16_t history[DETECTOR_WINDOW], uint16_t value)
{
    uint32_t sum = 0u;
    unsigned j;
    for (j = 1u; j < DETECTOR_WINDOW; ++j) {
        history[j - 1u] = history[j];
    }
    history[DETECTOR_WINDOW - 1u] = value;
    for (j = 0u; j < DETECTOR_WINDOW; ++j) {
        const uint32_t v = (uint32_t)history[j];
        sum += v * v;
    }
#ifdef TOY1_KNOWN_BAD_CONTROL
    /* Negative control must be detected even when assertions are disabled. */
    sum += 1u;
#endif
    return sum;
}

static int check_step(detector_t *detector,
                      uint16_t history[DETECTOR_WINDOW],
                      uint16_t sample, unsigned case_index)
{
    const uint32_t actual = detector_accept(detector, sample);
    const uint32_t expected = reference_accept(history, sample);
    if (actual != expected) {
        (void)fprintf(stderr,
                      "MISMATCH case=%u sample=%u expected=%lu actual=%lu\n",
                      case_index, (unsigned)sample,
                      (unsigned long)expected, (unsigned long)actual);
        return 1;
    }
    if (detector->sum_squares != actual) {
        (void)fprintf(stderr, "INCONSISTENT_STATE case=%u\n", case_index);
        return 2;
    }
    return 0;
}

int main(void)
{
    detector_t detector;
    uint16_t history[DETECTOR_WINDOW];
    uint32_t state = UINT32_C(0x243F6A88);
    unsigned i;
    unsigned checked = 0u;

    detector_init(&detector);
    clear_history(history);
    if (detector.sum_squares != 0u || detector.oldest != 0u) {
        (void)fputs("INIT_FAILED\n", stderr);
        return 3;
    }
    for (i = 0u; i < DETECTOR_WINDOW; ++i) {
        if (detector.samples[i] != 0u) {
            (void)fputs("INIT_HISTORY_FAILED\n", stderr);
            return 4;
        }
    }

    for (i = 0u; i < (unsigned)CASES; ++i) {
        uint16_t sample;
        int status;
        /* Reset only between completed accepted calls, matching CON-v6. */
        if (i != 0u && i % 257u == 0u) {
            detector_reset(&detector);
            clear_history(history);
            if (detector.sum_squares != 0u || detector.oldest != 0u) {
                return 5;
            }
        }

        state = state * UINT32_C(1664525) + UINT32_C(1013904223);
        if (i % 97u == 0u) {
            sample = UINT16_C(4095);
        } else if (i % 89u == 0u) {
            sample = 0u;
        } else if (i % 61u == 0u) {
            sample = 1u;
        } else {
            sample = (uint16_t)(state & UINT32_C(4095));
        }
        status = check_step(&detector, history, sample, i);
        if (status != 0) {
            return status;
        }
        ++checked;
    }
    (void)printf("HOST_PROBE_OK checks=%u sizeof_detector=%lu CHAR_BIT=%u "
                 "UINT16_MAX=%lu UINT32_MAX=%lu\n",
                 checked, (unsigned long)sizeof detector, (unsigned)CHAR_BIT,
                 (unsigned long)UINT16_MAX, (unsigned long)UINT32_MAX);
    return 0;
}
