/* Toy 1 HOST-ONLY C99 object-layout probe.
 * Not part of detector firmware. sizeof and offsetof are ABI-specific.
 * Compiles the actual reviewed detector.h, not a duplicate struct.
 */
#include "detector.h"
#include <stddef.h>
#include <stdio.h>

int main(void)
{
    detector_t detector;
    (void)printf(
        "{\"schema\":\"pc-toy1-layout-observation/v1\","
        "\"sizeof_detector\":%zu,"
        "\"sizeof_samples\":%zu,"
        "\"sizeof_oldest\":%zu,"
        "\"sizeof_sum_squares\":%zu,"
        "\"offset_samples\":%zu,"
        "\"offset_oldest\":%zu,"
        "\"offset_sum_squares\":%zu,"
        "\"window\":%u}\n",
        sizeof detector,
        sizeof detector.samples,
        sizeof detector.oldest,
        sizeof detector.sum_squares,
        offsetof(detector_t, samples),
        offsetof(detector_t, oldest),
        offsetof(detector_t, sum_squares),
        (unsigned)DETECTOR_WINDOW
    );
    return 0;
}
