#ifndef CLN_NUMERIC_H
#define CLN_NUMERIC_H
/* CLN-001 experimental finite C numeric kernels. NOT AP/CON/DE/product source.
 * Invalid input has no effects on numeric state; rejected before conversion.
 * Window energy fits 29 unsigned bits: 32 * 4095^2 = 536608800.
 * Index, publication debt, reset identity and producer availability are OUTSIDE
 * this numeric-kernel API and must not be inferred from its success.
 */
#include <stdint.h>

#define CLN_TAIL 31u
#define CLN_MAX_SAMPLE 4095u
#define CLN_MAX_ENERGY UINT32_C(536608800)

typedef enum {
    CLN_ACCEPTED = 0,
    CLN_REJECTED_RANGE = 1,
    CLN_BAD_ARGUMENT = 2
} cln_status;

typedef struct {
    uint16_t raw[CLN_TAIL];
    uint8_t oldest;
} cln_raw31;

typedef struct {
    uint32_t square[CLN_TAIL];
    uint32_t sum31;
    uint8_t oldest;
} cln_square31;

void cln_raw_reset(cln_raw31 *s);
void cln_square_reset(cln_square31 *s);
cln_status cln_raw_accept(cln_raw31 *s, uint32_t value, uint32_t *energy);
cln_status cln_square_accept(cln_square31 *s, uint32_t value, uint32_t *energy);

#endif
