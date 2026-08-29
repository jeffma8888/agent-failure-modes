---
id: INC-0031
title: A concurrency test with no forced interleaving passes loudest when the feature is absent
date: 2026-08-28
classes: [false-green, test-isolation, observability]
severity: high
status: fixed
---

# INC-0031 - A concurrency test with no forced interleaving passes loudest when the feature is absent

**Cost:** A deliberately-broken build passed its own concurrency test, so the artifact would have taught its reader that a planted bug was absent.

## Signature - how you recognise it

A test for an emergent property - locking, coalescing, deduplication, cache hits, backpressure - is green, and stays green when you delete the mechanism it exists to test.

## What happened

A test asserted on a counter incremented in place, which the interpreter specializes into a sequence with no interleaving window, while the deliberately forced yield sat on a DIFFERENT field. The race the test existed to detect therefore never occurred, and the test passed against the variant with the locking removed.

## Root cause

The test never established its own PRECONDITION - that concurrent callers actually overlap on the field under test. An emergent-property test that does not force the interleaving measures nothing, and it is greenest exactly when the mechanism is missing, because the fast path finishes before any peer arrives.

## Why it was hard to see

Nothing about the run looks wrong: it is fast, deterministic and green. The absence of the race is indistinguishable from the presence of the fix, and a second occurrence of this exact failure was found six days after the first one was documented.

## Fix

Force the window deliberately (sleep inside the critical section) and assert on the field that really races. Then MUTATION-VERIFY: plant each defect one at a time and require a NAMED test to go red, restoring the file in a finally block and asserting each anchor occurs exactly once. Measure the loss rate rather than assuming it - a flaky discriminator is worse than none, because it teaches the reader to distrust a real failure.

## Verification

Candidate designs measured 33% loss (flaky) and 0% loss before a loop-inside-thread pattern made the failure deterministic: about 85% of 4,000 updates lost in 10 of 10 unlocked runs, exact in 10 of 10 locked runs. The verifier itself then needed a portability check - it passed from its own directory and reported EVERY class broken when invoked from the parent, because the subprocess could not import the test package, and a checker that reports false BROKEN points at repairing correct code.

## Transferable rule

> A test of an emergent property (locking, coalescing, dedup, cache hits, backpressure) must assert its own PRECONDITION - that the interleaving really happened - or it is greenest when the mechanism is absent. Force the window, assert on the field that races, mutation-verify each defect against a NAMED test, and run the checker from two working directories.

## Provenance

Where this was observed, so the claim is checkable rather than anecdotal:

- https://github.com/jeffma8888/agent-gap-radar - e37ef89 and tools/verify_mutations.py implement the plant-one-defect-at-a-time harness this fix prescribes, with restoration verified by content in a finally block.

## Related

[INC-0022](./INC-0022-test-precondition-on-gitignored-local-state-passes-only-on-t.md) [INC-0028](./INC-0028-when-two-distributions-overlap-there-is-no-threshold-change.md)
