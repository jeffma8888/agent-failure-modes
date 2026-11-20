# A mutant or red-first witness does not prove what it is named for

[Catalog](../README.md) / [false-green](README.md) / mutation-witness-proves-less

**Go here if:** A named mutation stays green, goes red at setup or on a missing symbol, is masked by a guard, or kills only the first item; survivors appear while named tests pass; a config change has no red witness.

**Rule:** A witness counts only when it fails at the case's own assertion for the stated reason: trace every guard between the mutated line and the assertion, defeat each layer that enforces the rule, test redundant layers separately, state which items were witnessed, and measure mutants instead of reasoning about them. A config change that moves tests needs a red-first witness too.

14 incidents, 14 occurrences. Ordered by occurrences, then severity, then id.

## Incidents

### [INC-0524](../../incidents/INC-0524-a-root-named-a-mutation-its-assertions-could-not-see-because.md) - A root named a mutation its assertions could not see, because the next line returned the same status
- occurrences 2, severity low, status mitigated
- **Signature:** The named mutation is removed, and the case still passes because a later line refuses the same way.
- **Rule:** A mutation named as a case witness must be one the assertions can see; trace what the next line returns before naming it, and state the expected red line.
- **Recurrences:**
  - [INC-0533](../../incidents/INC-0533-a-named-mutant-was-masked-by-an-independent-guard-upstream-s.md) - 2026-11-02 - A named mutant was masked by an independent guard upstream, so the case could never turn red for the stated reason

### [INC-0116](../../incidents/INC-0116-two-validators-enforcing-the-same-rule-masked-single-file-mu.md) - Two validators enforcing the same rule masked single-file mutations
- occurrences 1, severity medium, status fixed
- **Signature:** Removing one of two redundant checks leaves the suite green.
- **Rule:** Test every layer of a redundant check independently.

### [INC-0133](../../incidents/INC-0133-a-local-guard-behind-a-shared-environment-pin-was-masked-and.md) - A local guard behind a shared environment pin was masked, and a mutation claim was reasoned instead of measured
- occurrences 1, severity medium, status fixed
- **Signature:** Removing a guard changes nothing because an outer pin already covers it.
- **Rule:** Measure mutations and protect files first.

### [INC-0336](../../incidents/INC-0336-a-tier-exclusion-was-added-only-after-a-witness-failed-witho.md) - A tier exclusion was added only after a witness failed without it
- occurrences 1, severity medium, status fixed
- **Signature:** A configuration change had a witness that was red before and green after.
- **Rule:** A config change that moves tests between tiers needs a red witness first, the same as a code change

### [INC-0339](../../incidents/INC-0339-a-mutant-of-a-shared-helper-proved-sensitivity-but-not-the-r.md) - A mutant of a shared helper proved sensitivity but not the real resource's end state
- occurrences 1, severity medium, status fixed
- **Signature:** Cheap fake-client controls went red, yet nothing showed the real pool ended in the right state after a failure.
- **Rule:** A helper mutant proves the test can see the bug; a real-resource witness proves the resource ends in the right state; when both are claimed, require both

### [INC-0343](../../incidents/INC-0343-a-weakened-final-check-survived-a-contract-suite-that-lacked.md) - A weakened final check survived a contract suite that lacked the right-signal, wrong-detail case
- occurrences 1, severity medium, status fixed
- **Signature:** Weakening a final title check survived an offline response-contract suite because no case left the title wrong while the status looked right.
- **Rule:** When a mutant survives, add the cell where the coarse signal is right and the checked detail is wrong, and rerun the mutant to prove the cell kills it

### [INC-0534](../../incidents/INC-0534-a-configuration-mutation-failed-a-setup-assertion-before-any.md) - A configuration mutation failed a setup assertion before any case oracle ran, so the red proved nothing about the cases
- occurrences 1, severity medium, status mitigated
- **Signature:** A mutation breaks the configuration, and the shared setup asserts the same configuration and fails first.
- **Rule:** A mutation counts for a case only when it fails at that case own assertion; check that the setup and fixture assertions do not fail first.

### [INC-0476](../../incidents/INC-0476-unit-mutation-testing-on-a-merged-change-found-two-survivors.md) - Unit mutation testing on a merged change found two survivors while every named test passed
- occurrences 1, severity low, status fixed
- **Signature:** Mutated code passed the whole suite.
- **Rule:** A passing suite is not a discriminating suite; run cheap mutations before merge, count only runs that executed the tests, and open a follow-up change for survivors instead of reopening the merge.

### [INC-0541](../../incidents/INC-0541-a-reviewer-accepted-an-initial-red-that-only-proved-a-new-fu.md) - A reviewer accepted an initial red that only proved a new function was missing, and said so
- occurrences 1, severity low, status mitigated
- **Signature:** A test-first red fails on an assertion that the new function exists.
- **Rule:** An initial red that only shows a new function is missing is not behavioral evidence; say so, and ask for a mutation or old-code run that reaches the behavioral assertions.

### [INC-0542](../../incidents/INC-0542-a-mutation-that-flipped-a-field-level-unique-flag-was-masked.md) - A mutation that flipped a field-level unique flag was masked by a unique index the migration had already created
- occurrences 1, severity low, status mitigated
- **Signature:** The mutated product setting is not the only thing enforcing the rule, because a database index enforces it too.
- **Rule:** When a rule is enforced in the schema as well as in code, a right-reason mutation must defeat both layers, in a disposable database with an exact recorded name.

### [INC-0560](../../incidents/INC-0560-a-mutant-made-the-product-raise-its-own-domain-error-inside.md) - A mutant made the product raise its own domain error inside the awaited expectation, before the matcher ran, and the agent disclosed that it was not an assertion error
- occurrences 1, severity low, status mitigated
- **Signature:** A red whose error type is not an assertion error, raised by the mutated product path.
- **Rule:** Classify a non-assertion red by where it was raised: a domain error from the mutated path inside the expectation is a right-reason kill; setup, timeout, harness or outside-path errors are not.

### [INC-0588](../../incidents/INC-0588-a-reviewer-s-original-race-script-could-not-run-unmodified-a.md) - A reviewer's original race script could not run unmodified against the revision because the step it interrupted no longer exists, and the reviewer reported it as stale test semantics
- occurrences 1, severity low, status mitigated
- **Signature:** An old reproducer asserts a step that the revision removed.
- **Rule:** When an old reproducer cannot run against a revision, report it as stale test semantics, not a kill, and report the adapted run separately.

### [INC-0608](../../incidents/INC-0608-a-mutant-was-witnessed-red-only-on-the-first-item-of-a-loop.md) - A mutant was witnessed red only on the first item of a loop, so the second row was not witnessed under the mutant
- occurrences 1, severity low, status mitigated
- **Signature:** A loop assertion goes red at its first item, so later items never run under the mutant.
- **Rule:** When a mutant turns a looped assertion red, state which items were witnessed; items after the first failure are not witnessed unless each has its own case.
