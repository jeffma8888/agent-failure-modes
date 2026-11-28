# false-green

[Catalog](../README.md) / false-green

A quality gate reports success while the work is not actually good: vacuous tests, tautological assertions, skipped cases, or a grader that cannot fail.

**Ask:** Could this gate be green on broken code? What is the smallest wrong change that still passes it?

**You are probably here if:** A gate, test or check is green (or red) while the work it vouches for is broken, never ran, or was judged by a signal that cannot tell the difference.

131 incidents filed here (135 occurrences); 64 more filed elsewhere are also tagged false-green.

## Topics

n = occurrences: incidents filed in the topic plus their repeats.

| Topic | Go here if | n | Link |
|---|---|---|---|
| A test oracle, locator or review claim came from memory, not source | A locator never matches, an absence check matches a hidden input the library renders, an assertion expects what the design never defined, an identifier is slightly wrong, or a behavior claim is false. | 15 | [oracle-or-claim-written-from-memory](oracle-or-claim-written-from-memory.md) |
| The gate was green but the cases it vouches for never executed | A pass, hold or acceptance is cited, but the new tests, selected projects, real commands or eligible population were empty, skipped, stubbed, or first ran after the merge. | 14 | [green-but-cases-never-ran](green-but-cases-never-ran.md) |
| A mutant or red-first witness does not prove what it is named for | A named mutation stays green, goes red at setup or on a missing symbol, is masked by a guard, or kills only the first item; survivors appear while named tests pass; a config change has no red witness. | 14 | [mutation-witness-proves-less](mutation-witness-proves-less.md) |
| A red, blocked or failing result came from setup or environment | A failure, BLOCKED or audit hit appears, but the cause is a sandbox or network denial, an unset variable, host load, a fixture tripping an earlier guard, or probe machinery that never ran. | 13 | [red-for-the-wrong-reason](red-for-the-wrong-reason.md) |
| A gate verdict came from a wrapper, pipe, chain or last line | A gate passed or a script carried on although a step failed: a wrapper exited 0, a pipe hid the status, a chain kept going, or the verdict came from the last line or exit code alone. | 13 | [step-failed-but-gate-passed](step-failed-but-gate-passed.md) |
| A negative, absence or presence check passed for an unrelated reason | A refusal, zero-count, absence or 'error shown' assertion passed, but it would also pass on an unrelated error, a nonexistent target, an unread page, a decoy or a stale element. | 12 | [check-satisfied-by-unrelated-cause](check-satisfied-by-unrelated-cause.md) |
| An artifact that looks like evidence was cited but proves no fact | A record cites a manifest, render, approval, ancestry, rename display or static PASS as proof, or names a commit id or value that was never copied from tool output. | 12 | [proxy-artifact-cited-as-evidence](proxy-artifact-cited-as-evidence.md) |
| Tests pass but the real page, status or session is wrong | Every tier is green, yet the real site shows a blank page, a not-found with status 200, raw markup or a guest instead of staff, a probe used up one-time state, or a flow needing a hidden token fails. | 12 | [real-page-or-response-wrong-behind-green](real-page-or-response-wrong-behind-green.md) |
| A test stays green with the behavior removed or broken | Deleting or breaking the mechanism leaves the test green: no forced overlap, no descendant, no failing fixture, a grader that skips new rows, or assertions that hold with or without the feature. | 10 | [test-cannot-see-the-defect](test-cannot-see-the-defect.md) |
| Verified a shortcut, a part or an old revision instead of what ships | Results differ between a focused run and the canonical gate, branches alone and merged, tree and branch range; the gate ran without the fix; merged options blur checked vs unchecked; cases ran twice. | 10 | [verified-a-different-target](verified-a-different-target.md) |
| A reported count, total or ledger does not match what ran | A row count, failure count, test total or coverage ledger is off: escaped delimiters, a header row, a missing runner, a word match, renamed checks, or totals that hide which items moved. | 7 | [count-or-total-computed-wrong](count-or-total-computed-wrong.md) |

## Class-level incidents

Filed in this class but in none of its topics.

### [INC-0028](../../incidents/INC-0028-when-two-distributions-overlap-there-is-no-threshold-change.md) - When two distributions overlap there is no threshold - change the signal, not the number
- occurrences 1, severity medium, status fixed
- **Signature:** Every candidate cutoff either misses real positives or refuses real work, and moving it just trades one error for the other. Each individual measurement looks reasonable.
- **Rule:** Before choosing a threshold, measure the MINIMUM of one population against the MAXIMUM of the other. If they overlap, no cutoff exists and tuning only picks which error you make - find an EXECUTABLE consequence of the two things being the same instead. Require mutual agreement (one-way is subsumption) and test the silent half, or any broad check counts as a twin.

### [INC-0040](../../incidents/INC-0040-a-guard-that-asserts-a-lifecycle-stage-fails-at-exactly-the.md) - A guard that asserts a lifecycle stage fails at exactly the moment it was written to protect
- occurrences 1, severity medium, status fixed
- **Signature:** A safety test has never once failed, and the state it forbids is a state on the project's own roadmap. It fails for the first time immediately after a milestone.
- **Rule:** Write down the state your guard FORBIDS, then ask whether the project intends to REACH that state. If it does, the guard is asserting a schedule, not a safety property, and it will fail precisely when the guarded event happens. The invariant worth protecting sits one level down: not 'no remote' but 'no credential in a remote'.

### [INC-0205](../../incidents/INC-0205-a-runtime-value-was-at-risk-of-being-invented-to-quiet-the-c.md) - A runtime value was at risk of being invented to quiet the compiler
- occurrences 1, severity medium, status fixed
- **Signature:** The compiler asked for a value the code should not have.
- **Rule:** Copy the typed input and delete from the copy; never fabricate a runtime value to quiet the compiler

## Also tagged false-green

64 incidents filed under another home class also carry this class. Listed by the node where they live:

- [detector-fail-open/syntax-shapes-and-benign-decoys](../detector-fail-open/syntax-shapes-and-benign-decoys.md): INC-0129, INC-0141, INC-0142, INC-0151
- [spec-and-scope/claims-outrun-available-evidence](../spec-and-scope/claims-outrun-available-evidence.md): INC-0300, INC-0656, INC-0660, INC-0662
- [spec-and-scope/records-drift-or-lose-provenance](../spec-and-scope/records-drift-or-lose-provenance.md): INC-0194, INC-0198, INC-0217, INC-0302
- [spec-and-scope/tests-do-not-prove-the-contract](../spec-and-scope/tests-do-not-prove-the-contract.md): INC-0105, INC-0285, INC-0311, INC-0328
- [test-isolation/the-test-itself-is-the-defect](../test-isolation/the-test-itself-is-the-defect.md): INC-0172, INC-0183, INC-0303, INC-0320
- [detector-fail-open/wrong-parser-or-pattern](../detector-fail-open/wrong-parser-or-pattern.md): INC-0078, INC-0118, INC-0224
- [identity-and-keying/replacement-record-malformed](../identity-and-keying/replacement-record-malformed.md): INC-0154, INC-0167, INC-0216
- [ipc-and-env](../ipc-and-env/README.md): INC-0180, INC-0223, INC-0256
- [observability/misleading-metrics-and-status](../observability/misleading-metrics-and-status.md): INC-0039, INC-0146, INC-0231
- [spec-and-scope/missing-or-late-prerequisites](../spec-and-scope/missing-or-late-prerequisites.md): INC-0063, INC-0075, INC-0269
- [checkpoint](../checkpoint/README.md): INC-0258, INC-0349
- [detector-fail-open/guard-defaults-and-negative-controls](../detector-fail-open/guard-defaults-and-negative-controls.md): INC-0113, INC-0148
- [identity-and-keying/approval-names-wrong-commit](../identity-and-keying/approval-names-wrong-commit.md): INC-0204, INC-0240
- [spec-and-scope/fix-misses-related-consumers](../spec-and-scope/fix-misses-related-consumers.md): INC-0086, INC-0173
- [spec-and-scope/framework-contract-assumptions](../spec-and-scope/framework-contract-assumptions.md): INC-0134, INC-0276
- [tooling-paths/chain-ran-on-after-failure](../tooling-paths/chain-ran-on-after-failure.md): INC-0051, INC-0364
- [tooling-paths/valid-alone-fails-in-host](../tooling-paths/valid-alone-fails-in-host.md): INC-0156, INC-0170
- [delegation/brief-or-plan-left-a-gap](../delegation/brief-or-plan-left-a-gap.md): INC-0298
- [detector-fail-open/coverage-and-controls-not-proven](../detector-fail-open/coverage-and-controls-not-proven.md): INC-0069
- [identity-and-keying/new-id-already-taken](../identity-and-keying/new-id-already-taken.md): INC-0027
- [observability/missing-or-unverifiable-receipts](../observability/missing-or-unverifiable-receipts.md): INC-0666
- [reward-hacking](../reward-hacking/README.md): INC-0001
- [spec-and-scope](../spec-and-scope/README.md): INC-0026
- [spec-and-scope/instructions-tools-cannot-follow](../spec-and-scope/instructions-tools-cannot-follow.md): INC-0330
- [spec-and-scope/requirements-and-limits-collide](../spec-and-scope/requirements-and-limits-collide.md): INC-0102
- [spec-and-scope/wrong-owner-path-or-scope](../spec-and-scope/wrong-owner-path-or-scope.md): INC-0289
- [stage-timeout/timeout-policy-and-lifecycle-boundaries](../stage-timeout/timeout-policy-and-lifecycle-boundaries.md): INC-0139
- [stage-timeout/timing-models-and-critical-path](../stage-timeout/timing-models-and-critical-path.md): INC-0271
- [stage-timeout/work-outgrows-enforced-timeouts](../stage-timeout/work-outgrows-enforced-timeouts.md): INC-0209
- [test-isolation/assertion-wider-than-contract](../test-isolation/assertion-wider-than-contract.md): INC-0084
- [tooling-paths/sandbox-refuses-allowed-target](../tooling-paths/sandbox-refuses-allowed-target.md): INC-0260
- [vcs-destruction](../vcs-destruction/README.md): INC-0632
