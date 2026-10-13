# AS-001 corrected-scope authority request v1

**Status:** PROPOSED / NOT APPROVED
**Authority required:** Human engineering authority
**Trigger:** `reviews/gates/TOY1-SCOPE-AUDIT-002-receipt.json`
**Supporting scope review:** `reviews/gates/TOY1-SCOPE-AUDIT-002.md`
**Change request:** `process/change_requests/CR-001-SYNTHETIC-REQUIREMENT-AUTHORITY.md`

## Decision requested

Authorize creation and independent review of a versioned AS-001 corrected
baseline with the following *replacement for R-001*:

> For each legal sample accepted at the detector interface, update the
> detector exactly once. The numerical rolling result is determined by
> the order of accepted samples and shall not depend on the elapsed time
> between invocations. Any throughput limit, overload behavior or
> real-time processing deadline belongs to a separately approved
> integration requirement.

Authorize the interpretation of `R-002` as **the newest 32 accepted
interface samples, in acceptance order**, zero-padded on startup.
This is not a requirement to infer or detect all physical acquisitions
that a producer might fail to deliver. The toy mathematical fixture
still uses 32 elements of unsigned 12-bit domain 0..4095 unless
separately authorized to change.

Under this corrected scope, **no AS-mandated obligation** requires:
- one sample every 1 ms;
- detection of every upstream dropped physical acquisition;
- loss-epoch or sequence counter;
- recovery from 2^32 counter wrapping;
- task-independent acquisition watchdog;
- atomic publication to an *unspecified* concurrent external reader.

These mechanisms may be considered only where an approved integration
contract genuinely requires them. The detector must still preserve
its own numerical invariant and publish complete results under any
explicitly approved reader interface.

## Scope deliberately unchanged

- C-001: 12-bit unsigned legal sample range of the synthetic toy.
- C-002: separately approved 2048-byte detector-attributable SRAM
  budget and its unique-byte peak attribution rules.
- C-003: no reliance on floating-point hardware.
- R-002: 32-sample exact squared sum with zero-padded startup.
- R-003: no overflow for legal input sequences.
- F-001 objectives, PR-002 abstract theorem and accepted proof limits.
- AP-002 provisional selection and accepted AD-003 remain **historical
  decisions**; they require impact review and a new superseding
  authority receipt if a protected condition changes.
- VO-001 acceptance remains only within the synthetic ADC domain.
- VO-002, VO-003, VO-005 and VO-006 remain open; no acceptance/discharge
  follows solely from this scope request.

## Controlled consequences upon explicit approval

1. Create *versioned proposed* BKP provenance correction and AS
   candidate. Do not overwrite the original AS or accepted decisions.
2. Re-scope VO-004 and VP-001. An original 1-ms target timing obligation
   cannot be deleted or marked discharged by editorial change; it must
   be formally superseded in an accepted verification revision.
3. Assess implications for AP-002 provisional authority conditions,
   accepted AD-003 and F-based evaluation, without automatically
   revoking an unaffected mathematical architecture.
4. Generate a new minimal CON candidate from the accepted corrected
   AS, and obtain independent review. Retain CON v1-v4 and review
   history as evidence of prior decisions and process defects.
5. Change the process source-ingestion policy so synthetic examples
   cannot silently become binding stakeholder requirements again.

## Alternatives and boundaries

- **Approve minimal accepted-input semantics (recommended):** Keep
  the rolling algorithm sample-indexed and optional physical-loss
  behavior outside the algorithm's AS.
- **Require last 32 physical ADC acquisitions:** Specify an acquisition
  domain, dropped-sample handling and authority for loss detection
  before designing such an interface. This is a different requirement,
  not implied by the current synthetic BKP.

Neither option promises infinite throughput. Sample-rate independence
is a property of numerical semantics, not a guarantee that an MCU can
execute an unbounded number of calls per second.

## Approval rule

An explicit human approval must identify this request and the
accepted-input semantics above. An audit `PASS`, agent recommendation
or a casual ambiguous acknowledgement is not authority. Until an
accepted superseding record is created, the original AS and all
dependent accepted receipts remain historical authority and no new
CON/DE/firmware gate advances from this proposal.
