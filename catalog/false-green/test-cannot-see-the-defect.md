# A test stays green with the behavior removed or broken

[Catalog](../README.md) / [false-green](README.md) / test-cannot-see-the-defect

**Go here if:** Deleting or breaking the mechanism leaves the test green: no forced overlap, no descendant, no failing fixture, a grader that skips new rows, or assertions that hold with or without the feature.

**Rule:** Show each test can fail: make it establish its own precondition (the interleaving, the descendant, the dirty state), include the fixture where the two behaviors differ, and assert an observable effect that differs with and without the feature, through the real entry point, not how the code was invoked.

8 incidents, 8 occurrences. Ordered by occurrences, then severity, then id.

## Incidents

### [INC-0031](../../incidents/INC-0031-a-concurrency-test-with-no-forced-interleaving-passes-loudes.md) - A concurrency test with no forced interleaving passes loudest when the feature is absent
- occurrences 1, severity high, status fixed
- **Signature:** A test for an emergent property - locking, coalescing, deduplication, cache hits, backpressure - is green, and stays green when you delete the mechanism it exists to test.
- **Rule:** A test of an emergent property (locking, coalescing, dedup, cache hits, backpressure) must assert its own PRECONDITION - that the interleaving really happened - or it is greenest when the mechanism is absent. Force the window, assert on the field that races, mutation-verify each defect against a NAMED test, and run the checker from two working directories.

### [INC-0104](../../incidents/INC-0104-a-process-group-kill-test-used-single-process-stubs-so-signa.md) - A process-group kill test used single-process stubs, so signalling the leader and the group looked the same
- occurrences 1, severity medium, status fixed
- **Signature:** A group-kill test passes with stubs that have no descendants.
- **Rule:** A group-kill test needs a descendant, or it cannot tell group from leader.

### [INC-0153](../../incidents/INC-0153-a-test-checked-only-the-dispatch-argv-of-a-child-stage-not-i.md) - A test checked only the dispatch argv of a child stage, not its semantics
- occurrences 1, severity medium, status fixed
- **Signature:** A stage is proven by what it was called with, not by what it did.
- **Rule:** Test what a stage does, not how it was started.

### [INC-0155](../../incidents/INC-0155-a-kill-rehearsal-met-its-timeout-but-nobody-checked-what-the.md) - A kill rehearsal met its timeout but nobody checked what the killed process left behind
- occurrences 1, severity medium, status fixed
- **Signature:** A rehearsal passed on elapsed time while the leftovers of the killed run were unexamined.
- **Rule:** In a kill rehearsal, inspect the leftovers, and state the temporary directory setting the sweep depends on.

### [INC-0221](../../incidents/INC-0221-a-performance-refactor-was-checked-only-on-the-real-tree.md) - A performance refactor was checked only on the real tree
- occurrences 1, severity medium, status fixed
- **Signature:** Equal output on the real tree hid changed failure behavior.
- **Rule:** Prove a performance refactor with old and new on the same failure fixtures

### [INC-0222](../../incidents/INC-0222-a-clean-tree-positive-did-not-exercise-the-working-file-cont.md) - A clean-tree positive did not exercise the working-file context
- occurrences 1, severity medium, status fixed
- **Signature:** The clean tree matched the baseline, so the refusal path never ran.
- **Rule:** Plant a harmless byte difference before proving a refusal when the baseline is chosen by byte equality

### [INC-0388](../../incidents/INC-0388-a-baseline-comparison-graded-only-rows-present-in-the-baseli.md) - A baseline comparison graded only rows present in the baseline, so a new failing row passed
- occurrences 1, severity medium, status fixed
- **Signature:** A run with a new failing row compared equal to its baseline.
- **Rule:** A baseline comparison must grade a row new in the run on its own outcome

### [INC-0505](../../incidents/INC-0505-a-run-command-silently-dropped-a-named-option-and-three-test.md) - A run command silently dropped a named option, and three tests that ran it asserted only things that are true for the full data set too
- occurrences 1, severity medium, status mitigated
- **Signature:** A test runs a command with an option and asserts exit status, timing and a side marker, all of which hold with or without the option.
- **Rule:** A test that exercises an option goes through the real entry point and asserts an observable effect that differs with and without the option; exit 0 and side markers are not evidence the option took effect.
