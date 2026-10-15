# Independent resource evidence review: TOY1-VO002-HOST-20261015T035845Z

**Task:** `REVIEW_RESOURCE_EVIDENCE-TOY1-VR001`  
**Review mode:** Direct independent review after registered Codex runner launch failure  
**Checkout HEAD:** `3d479d06b2828b3feddbfa90ac735f41491abbce`  
**Evidence source revision:** `4b080f79fb066daf28b859f3f92ad2647abdc74b`

## Finding

The host-only observation is internally consistent and accurately describes the pinned `detector_t` declaration: `samples` occupies 64 bytes at offset 0, `oldest` occupies one byte at offset 64, and `sum_squares` occupies four bytes at offset 68. Their 69 field bytes plus three bytes of host ABI padding give the reported 72-byte object. The recorded host output and compiler-version logs are available and their SHA-256 values match the submitted summary. The submitted compiler and execution exit codes are zero. This reviewer inspected the logs and source; the checksummed evidence reports the compilation and execution. This review did not reproduce the compile or execution.

The evidence source commit exists in the local object database. The checked-out HEAD differs from that pinned source revision, but the current source pins and evidence blob match the manifest, and `tools/task.py inspect` validated the pinned inputs. Record the HEAD/revision discrepancy for traceability; this does not change what source revision the evidence claims to describe.

This is strictly a host ABI object-layout observation. The C-002 charged-SRAM contract has seven conditional ceilings totaling 1,792 bytes and a 256-byte reserve under its 2,048-byte limit. These are commitments, not measured usage or proof of feasibility. All seven target peaks are correctly `null`; target ABI, stack and interrupt nesting, shared/dynamic allocation attribution, target map/image, and integration evidence remain absent. The observation is not F-001 state-SRAM evidence.

The registered `task.py run` failed before a reviewer turn started: Codex session unavailable, completed turns 0, and stderr reports failure to initialize its in-process app-server client because the filesystem is read-only. This direct review is separately identified and must not be treated as a successful registered runner execution.

## Checks and scope

- **Reviewer-inspected:** evidence summary schema and bounds; submitted evidence blob SHA-1; all seven source SHA-256 pins; `detector_t` declaration and actual layout probe; host raw log SHA-256 values and layout output; approved C-002 scope and CON-AP2-003-v6 ceilings; VO ledger.
- **Reviewer-reproduced:** none of the host compilation or layout execution.
- **Producer-reported:** successful host compiler invocation and execution, pinned source revision, stable sources during collection.
- **Deterministic task checks:** resource-evidence unit tests passed (3 tests); task manifest inspection passed. Registered review runner failed before review; no gate decision was emitted by it.

## Disposition

**ACCEPT_WITH_CLARIFICATIONS**, scoped only to recording the reported host layout observation. The checkout/pinned-revision difference and registered runner launch failure remain explicit process/traceability issues. No target resource conclusion follows. VO-002, VO-003, VO-004, VO-005, and VO-006 remain OPEN; AD-003 and F-001 remain unchanged. No product verification or VO discharge is claimed.

**Next eligible action:** preserve this scoped review receipt and address the registered runner launch defect through the applicable process/genericity work. Do not route automatically to target qualification; no target configuration is authorized by this evidence.
