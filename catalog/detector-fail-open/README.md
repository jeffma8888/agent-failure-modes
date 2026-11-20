# detector-fail-open

[Catalog](../README.md) / detector-fail-open

A monitor or safety check silently never fires: a wrong regex flavor, the wrong parsed field, a case mismatch. A negative result is mistaken for health.

**Ask:** Have you fed this detector a known-bad sample and watched it fire, AND a known-good sample and watched it stay silent?

**You are probably here if:** A check stays silent on known-bad input, matches the wrong evidence, skips part of its scope or treats missing data as permission.

31 incidents filed here (31 occurrences); 20 more filed elsewhere are also tagged detector-fail-open.

## Topics

n = occurrences: incidents filed in the topic plus their recorded repeats.

| Topic | Go here if | n | Link |
|---|---|---|---|
| The checker ran but its target coverage is unproven | A successful checker or recorder misses its target, scans the wrong baseline, includes excluded files or ignores required history. | 9 | [coverage-and-controls-not-proven](coverage-and-controls-not-proven.md) |
| Syntax matching accepts decoys or rejects valid forms | A static rule recognizes one syntax shape, misses aliases or accepts a benign substring beside an invalid target. | 7 | [syntax-shapes-and-benign-decoys](syntax-shapes-and-benign-decoys.md) |
| A parser or pattern reads the wrong evidence | A detector sees nothing, matches injected text or classifies the wrong substring despite visible evidence. | 7 | [wrong-parser-or-pattern](wrong-parser-or-pattern.md) |
| A broken guard implementation still appears valid | The guard appears to satisfy its contract even though a faulty implementation can produce the same passing result. | 6 | [guard-defaults-and-negative-controls](guard-defaults-and-negative-controls.md) |

## Class-level incidents

Filed in this class but in none of its topics.

### [INC-0150](../../incidents/INC-0150-a-missing-independently-callable-guard-lacked-protocol-cases.md) - A missing independently callable guard lacked protocol cases, and macOS path aliases looked like regressions
- occurrences 1, severity medium, status fixed
- **Signature:** A guard without its own tests and cwd assertions failing on path aliases.
- **Rule:** Resolve paths before comparing, and compare to the active bytes first.

### [INC-0458](../../incidents/INC-0458-a-generated-down-migration-defect-fixed-once-came-back-in-th.md) - A generated down migration defect fixed once came back in the next row because the fix was never turned into a check
- occurrences 1, severity low, status fixed
- **Signature:** A defect already fixed once appeared again with no check to catch it.
- **Rule:** Turn a fixed generator defect into a check on the list that every later generated migration runs

## Also tagged detector-fail-open

20 incidents filed under another home class also carry this class. Listed by the node where they live:

- [false-green/check-satisfied-by-unrelated-cause](../false-green/check-satisfied-by-unrelated-cause.md): INC-0082, INC-0095, INC-0318
- [false-green](../false-green/README.md): INC-0028, INC-0040
- [false-green/red-for-the-wrong-reason](../false-green/red-for-the-wrong-reason.md): INC-0213, INC-0314
- [false-green/step-failed-but-gate-passed](../false-green/step-failed-but-gate-passed.md): INC-0120, INC-0347
- [false-green/mutation-witness-proves-less](../false-green/mutation-witness-proves-less.md): INC-0343
- [false-green/real-page-or-response-wrong-behind-green](../false-green/real-page-or-response-wrong-behind-green.md): INC-0250
- [false-green/test-cannot-see-the-defect](../false-green/test-cannot-see-the-defect.md): INC-0221
- [identity-and-keying/key-is-a-proxy](../identity-and-keying/key-is-a-proxy.md): INC-0122
- [identity-and-keying/replacement-record-malformed](../identity-and-keying/replacement-record-malformed.md): INC-0161
- [ipc-and-env](../ipc-and-env/README.md): INC-0009
- [observability/missing-or-unverifiable-receipts](../observability/missing-or-unverifiable-receipts.md): INC-0227
- [reward-hacking](../reward-hacking/README.md): INC-0199
- [spec-and-scope/tests-do-not-prove-the-contract](../spec-and-scope/tests-do-not-prove-the-contract.md): INC-0191
- [test-isolation/assertion-wider-than-contract](../test-isolation/assertion-wider-than-contract.md): INC-0126
- [verdict-token](../verdict-token/README.md): INC-0152

## Practices touching this class

- [PRA-0001](../CORE.md#practices) - The enforcement ladder: pick the cheapest rung that makes the failure impossible
- [PRA-0003](../CORE.md#practices) - Six conditions for a gate that cannot be skipped
- [PRA-0004](../CORE.md#practices) - Choose the constraint surface before choosing the enforcement strength
