# spec-and-scope

[Catalog](../README.md) / spec-and-scope

The loop does the wrong amount of work: it pursues the whole visible mission instead of its assigned slice, or picks tasks by lowest effort instead of highest value, or grows an artifact without bound.

**Ask:** Does the agent's visible context imply a bigger goal than its assigned task, and is any required-reading artifact growing every iteration?

**You are probably here if:** Work exceeds its assigned slice or size cap, favors easy tasks over value, or a plan contradicts files, tools, dependencies, permissions, or delivered work.

104 incidents filed here (104 occurrences); 58 more filed elsewhere are also tagged spec-and-scope.

## Topics

n = occurrences: incidents filed in the topic plus their recorded repeats.

| Topic | Go here if | n | Link |
|---|---|---|---|
| Framework behavior contradicts the design or test | The framework transforms input before a check, swallows a refusal, adds unexpected defaults, makes an undeclared request, or loses behavior when a component is replaced. | 14 | [framework-contract-assumptions](framework-contract-assumptions.md) |
| Green tests omit or misstate required behavior | A named parameter is untested, moved files vanish from a run, coverage summarizes a tier, an oracle pins the wrong detail, or static gates miss a unit regression. | 13 | [tests-do-not-prove-the-contract](tests-do-not-prove-the-contract.md) |
| Instructions fail a gate or omit the required operation | A gate cannot pass after its preceding step, a required command or parameter is unavailable, a tool exceeds promised effects, a runner cannot reach a check, or cleanup only seeds and leaves old rows. | 12 | [instructions-tools-cannot-follow](instructions-tools-cannot-follow.md) |
| A cited baseline, count, line, or digest no longer matches its source | A baseline, count, citation, finding, or ruling no longer matches its source; moved or signed bytes differ, or review re-reads unchanged ranges and misses the actual delta. | 12 | [records-drift-or-lose-provenance](records-drift-or-lose-provenance.md) |
| Work lands under the wrong owner, path, or write boundary | A task needs unowned files, a brief forbids a required output, a file is never collected, tools disagree on ownership, or a rule covers a whole commit instead of its affected files. | 12 | [wrong-owner-path-or-scope](wrong-owner-path-or-scope.md) |
| A planned step cannot run because its prerequisite is missing | A row needs data, types, a callable seam, a component, or approval that arrives later; pressure grows to invent a stub or weaken the contract. | 11 | [missing-or-late-prerequisites](missing-or-late-prerequisites.md) |
| Claims or instructions say more than the evidence supports | A question is already answered, a diagnosis is only conditional, a value has no source, or a landing summary claims more work than the author delivered. | 10 | [claims-outrun-available-evidence](claims-outrun-available-evidence.md) |
| Requirements, units, or hard limits cannot hold together | A duration exceeds its cap, a count has no unit, a complete identity cannot fit the transport, or a validator rejects a value its producer must emit. | 10 | [requirements-and-limits-collide](requirements-and-limits-collide.md) |
| A local fix leaves sibling cases or callers broken | A fix leaves sibling payloads or callers using old arguments, state, or commands; a second defect remains, or a tiny conflict hides inconsistent automatically merged code. | 8 | [fix-misses-related-consumers](fix-misses-related-consumers.md) |

## Class-level incidents

Filed in this class but in none of its topics.

### [INC-0026](../../incidents/INC-0026-a-whole-batch-verification-veto-turns-one-bad-item-into-a-pe.md) - A whole-batch verification veto turns one bad item into a permanent block
- occurrences 1, severity high, status fixed
- **Signature:** A gate that used to pass now refuses on every cycle, and it names a DIFFERENT offending item each time. The queue grows monotonically. Each individual refusal is correct and well-reported.
- **Rule:** A gate whose verdict covers the whole batch, and whose caller aborts on any failure, turns one bad item into a permanent block as soon as the queue keeps growing - a ratchet, not a filter. Judge each item on its own evidence, act per item, and never let the gate's exit code re-create the batch veto.

### [INC-0262](../../incidents/INC-0262-keep-local-evidence-paths-out-of-review-text.md) - Keep local evidence paths out of review text
- occurrences 1, severity medium, status fixed
- **Signature:** A review cited a private local folder in committed text.
- **Rule:** Keep local evidence paths out of committed review text

## Also tagged spec-and-scope

58 incidents filed under another home class also carry this class. Listed by the node where they live:

- [delegation/brief-or-plan-left-a-gap](../delegation/brief-or-plan-left-a-gap.md): INC-0087, INC-0098, INC-0135, INC-0331
- [false-green/real-page-or-response-wrong-behind-green](../false-green/real-page-or-response-wrong-behind-green.md): INC-0241, INC-0265, INC-0272, INC-0275
- [stage-timeout/timeout-policy-and-lifecycle-boundaries](../stage-timeout/timeout-policy-and-lifecycle-boundaries.md): INC-0107, INC-0111, INC-0124, INC-0355
- [stage-timeout/timing-models-and-critical-path](../stage-timeout/timing-models-and-critical-path.md): INC-0187, INC-0312, INC-0345, INC-0348
- [stage-timeout/work-outgrows-enforced-timeouts](../stage-timeout/work-outgrows-enforced-timeouts.md): INC-0003, INC-0004, INC-0308, INC-0333
- [vcs-destruction](../vcs-destruction/README.md): INC-0044, INC-0045, INC-0065, INC-0101
- [false-green/oracle-or-claim-written-from-memory](../false-green/oracle-or-claim-written-from-memory.md): INC-0057, INC-0061, INC-0234
- [identity-and-keying/replacement-record-malformed](../identity-and-keying/replacement-record-malformed.md): INC-0130, INC-0157, INC-0182
- [test-isolation/passes-warm-fails-clean](../test-isolation/passes-warm-fails-clean.md): INC-0110, INC-0297, INC-0299
- [checkpoint](../checkpoint/README.md): INC-0160, INC-0268
- [detector-fail-closed](../detector-fail-closed/README.md): INC-0052, INC-0366
- [false-green/check-satisfied-by-unrelated-cause](../false-green/check-satisfied-by-unrelated-cause.md): INC-0193, INC-0287
- [identity-and-keying/key-is-a-proxy](../identity-and-keying/key-is-a-proxy.md): INC-0149, INC-0359
- [observability/clock-labels-without-clock-evidence](../observability/clock-labels-without-clock-evidence.md): INC-0274, INC-0350
- [tooling-paths/valid-alone-fails-in-host](../tooling-paths/valid-alone-fails-in-host.md): INC-0090, INC-0171
- [concurrency](../concurrency/README.md): INC-0066
- [delegation/reviewer-not-independent-or-free](../delegation/reviewer-not-independent-or-free.md): INC-0337
- [false-green/count-or-total-computed-wrong](../false-green/count-or-total-computed-wrong.md): INC-0323
- [false-green/mutation-witness-proves-less](../false-green/mutation-witness-proves-less.md): INC-0336
- [false-green/proxy-artifact-cited-as-evidence](../false-green/proxy-artifact-cited-as-evidence.md): INC-0315
- [false-green/verified-a-different-target](../false-green/verified-a-different-target.md): INC-0035
- [identity-and-keying/new-id-already-taken](../identity-and-keying/new-id-already-taken.md): INC-0080
- [observability](../observability/README.md): INC-0358
- [observability/misleading-metrics-and-status](../observability/misleading-metrics-and-status.md): INC-0039
- [reward-hacking](../reward-hacking/README.md): INC-0001
- [stage-timeout](../stage-timeout/README.md): INC-0218
- [steering-channel](../steering-channel/README.md): INC-0067
- [test-isolation/green-alone-red-together](../test-isolation/green-alone-red-together.md): INC-0088
