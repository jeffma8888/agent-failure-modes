# observability

[Catalog](../README.md) / observability

The signal you trust hides the truth: an outcome flag masks a chronically over-budget step, a lifetime average hides a spike, a hardened process reports zero usage.

**Ask:** Are you reading a distribution or a single number, a delta or a lifetime average - and could the measurement itself be denied?

**You are probably here if:** Logs, timing, counts or status look reassuring, but the underlying run, evidence or reported chronology cannot be verified.

44 incidents filed here (48 occurrences); 58 more filed elsewhere are also tagged observability.

## Topics

n = occurrences: incidents filed in the topic plus their repeats.

| Topic | Go here if | n | Link |
|---|---|---|---|
| Timestamp labels disagree with the actual clock | A ruling, brief or receipt has a time ahead of the clock, a guessed label or a quoted clock value no call returned. | 16 | [clock-labels-without-clock-evidence](clock-labels-without-clock-evidence.md) |
| A reassuring signal contradicts the underlying evidence | The reported result looks settled, but inspecting the actual target does not support what the signal or summary claims. | 14 | [misleading-metrics-and-status](misleading-metrics-and-status.md) |
| Missing evidence keeps findings unverified | You cannot verify a finding from inspectable evidence of the actual run, and repeated inspection still leaves the same questions open. | 13 | [missing-or-unverifiable-receipts](missing-or-unverifiable-receipts.md) |

## Class-level incidents

Filed in this class but in none of its topics.

### [INC-0358](../../incidents/INC-0358-a-restated-rule-gained-a-qualifier-the-original-ruling-never.md) - A restated rule gained a qualifier the original ruling never had
- occurrences 3, severity medium, status fixed
- **Signature:** A ruling said to report every sample over a limit at once, but the spec that restated it said to report only eligible samples.
- **Rule:** When a ruling is restated in a spec, copy its population word for word; a qualifier borrowed from another purpose narrows an alarm, so diff every restated condition against the ruling's own words and fix each sibling copy
- **Recurrences:**
  - 2026-11-26 - A design document labelled one choice as the upstream requirements document's default, but the label contradicted that document's own option set; a second-model reviewer found it.
  - 2026-11-26 - In the next version of the same design document, upstream priorities and conditions were paraphrased under a default label, so the requirements document appeared to say something it did not; the reviewer required verbatim quotes of upstream priorities and conditions.

### [INC-0562](../../incidents/INC-0562-the-first-real-run-of-a-new-egress-observer-on-unchanged-mai.md) - The first real run of a new egress observer on unchanged main caught the dev server phoning home, and the agent stopped instead of widening the allowlist
- occurrences 1, severity medium, status mitigated
- **Signature:** A new network observer denies connects that the unchanged product already makes.
- **Rule:** When a new observer denies traffic on the unchanged base, stop and report; never widen the allowlist, and key any refinement to recorded listeners.

### [INC-0586](../../incidents/INC-0586-a-waiter-whose-helper-could-not-open-its-guard-spun-to-the-w.md) - A waiter whose helper could not open its guard spun to the wait limit with tracebacks, and a malformed owner record was skipped silently
- occurrences 1, severity medium, status mitigated
- **Signature:** A failure to open the guard and an unreadable owner record produce no report that names a manual step.
- **Rule:** When a guard or an owner identity cannot be proved, exit promptly with a manual step naming the exact path; never spin or skip silently.

## Also tagged observability

58 incidents filed under another home class also carry this class. Listed by the node where they live:

- [false-green/green-but-cases-never-ran](../false-green/green-but-cases-never-ran.md): INC-0239, INC-0253, INC-0266, INC-0283
- [ipc-and-env](../ipc-and-env/README.md): INC-0049, INC-0059, INC-0068, INC-0325
- [concurrency](../concurrency/README.md): INC-0048, INC-0554, INC-0558
- [delegation/finished-on-disk-no-reply](../delegation/finished-on-disk-no-reply.md): INC-0091, INC-0128, INC-0317
- [delegation/guessed-or-stale-id-name-path](../delegation/guessed-or-stale-id-name-path.md): INC-0201, INC-0206, INC-0263
- [detector-fail-open/coverage-and-controls-not-proven](../detector-fail-open/coverage-and-controls-not-proven.md): INC-0037, INC-0140, INC-0292
- [detector-fail-open/wrong-parser-or-pattern](../detector-fail-open/wrong-parser-or-pattern.md): INC-0019, INC-0029, INC-0077
- [false-green/count-or-total-computed-wrong](../false-green/count-or-total-computed-wrong.md): INC-0252, INC-0259, INC-0310
- [spec-and-scope/requirements-and-limits-collide](../spec-and-scope/requirements-and-limits-collide.md): INC-0127, INC-0334, INC-0352
- [detector-fail-closed](../detector-fail-closed/README.md): INC-0032, INC-0033
- [false-green/oracle-or-claim-written-from-memory](../false-green/oracle-or-claim-written-from-memory.md): INC-0042, INC-0062
- [false-green/proxy-artifact-cited-as-evidence](../false-green/proxy-artifact-cited-as-evidence.md): INC-0228, INC-0247
- [false-green/real-page-or-response-wrong-behind-green](../false-green/real-page-or-response-wrong-behind-green.md): INC-0244, INC-0273
- [spec-and-scope](../spec-and-scope/README.md): INC-0026, INC-0262
- [spec-and-scope/records-drift-or-lose-provenance](../spec-and-scope/records-drift-or-lose-provenance.md): INC-0235, INC-0346
- [stage-timeout/timing-models-and-critical-path](../stage-timeout/timing-models-and-critical-path.md): INC-0195, INC-0210
- [stale-module](../stale-module/README.md): INC-0021, INC-0145
- [delegation/order-collides-with-rule-or-guard](../delegation/order-collides-with-rule-or-guard.md): INC-0654
- [false-green](../false-green/README.md): INC-0028
- [false-green/red-for-the-wrong-reason](../false-green/red-for-the-wrong-reason.md): INC-0202
- [false-green/test-cannot-see-the-defect](../false-green/test-cannot-see-the-defect.md): INC-0031
- [identity-and-keying/key-is-a-proxy](../identity-and-keying/key-is-a-proxy.md): INC-0054
- [identity-and-keying/new-id-already-taken](../identity-and-keying/new-id-already-taken.md): INC-0027
- [spec-and-scope/claims-outrun-available-evidence](../spec-and-scope/claims-outrun-available-evidence.md): INC-0306
- [spec-and-scope/framework-contract-assumptions](../spec-and-scope/framework-contract-assumptions.md): INC-0245
- [stage-timeout/work-outgrows-enforced-timeouts](../stage-timeout/work-outgrows-enforced-timeouts.md): INC-0002
- [test-isolation/green-alone-red-together](../test-isolation/green-alone-red-together.md): INC-0361
- [test-isolation/the-test-itself-is-the-defect](../test-isolation/the-test-itself-is-the-defect.md): INC-0638
- [tooling-paths](../tooling-paths/README.md): INC-0081
- [tooling-paths/tool-defaults-not-target](../tooling-paths/tool-defaults-not-target.md): INC-0060

## Practices touching this class

- [PRA-0002](../CORE.md#practices) - Classify a control by its enforcement point, never by its medium
- [PRA-0003](../CORE.md#practices) - Six conditions for a gate that cannot be skipped
- [PRA-0005](../CORE.md#practices) - Admission control for an agent team on a shared host
