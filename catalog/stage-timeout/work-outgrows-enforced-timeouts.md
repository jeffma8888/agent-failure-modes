# Work outgrows hidden caps or loses timeout headroom

[Catalog](../README.md) / [stage-timeout](README.md) / work-outgrows-enforced-timeouts

**Go here if:** Attempts die at an identical limit, a growing suite stops mid-report or a test passes alone but times out under parallel load.

**Rule:** Measure all work against the smallest enforced cap on the current tree under representative load, bound growing inputs and retain measured headroom as tests change; checkpoint state-keyed progress instead of retrying the same over-budget plan.

14 incidents, 14 occurrences. Ordered by occurrences, then severity, then id.

## Incidents

### [INC-0002](../../incidents/INC-0002-the-hard-per-step-wall-clock-cap-is-the-number-one-cause-of.md) - The hard per-step wall-clock cap is the number-one cause of lost work
- occurrences 1, severity critical, status mitigated
- **Signature:** Every attempt log for a specific step is exactly the same tiny size and reads only 'timed out after 600s'. Two full iterations produce nothing while sibling teams on the same infrastructure ship normally.
- **Rule:** A per-step timeout you did not set is often the real timeout. If a step's attempt logs are all the same tiny size, its median is AT the cap, not near it. Fix: write-early checkpoint (minimal complete output first, then refine in place), and always report the duration DISTRIBUTION, never a single-shot healthy flag.

### [INC-0003](../../incidents/INC-0003-a-slow-test-suite-makes-a-product-unbuildable-by-the-loop.md) - A slow test suite makes a product unbuildable by the loop
- occurrences 1, severity high, status fixed
- **Signature:** One team consistently fails while sibling teams on the same infrastructure ship normally. Every failed engineer and tester attempt log is a 48-byte 'timed out' stub. Shrinking the spec does not help.
- **Rule:** A loop CAN correctly diagnose its own blocker and still be structurally unable to fix it if the fix touches a policy only the operator owns - so when a team stalls, READ ITS PLANNER'S NOTES FIRST. If a suite approaches the per-step timeout, the product is unbuildable by the loop; fix the SUITE, and put the fix in a config all call sites inherit.

### [INC-0004](../../incidents/INC-0004-a-monotonically-growing-required-reading-file-silently-kills.md) - A monotonically growing required-reading file silently kills the loop
- occurrences 1, severity high, status fixed
- **Signature:** Same log signature as INC-0002, but the guilty artifact is a required-reading file (a roadmap, a design doc, a large context file) that grew organically over many iterations.
- **Rule:** Any file injected into EVERY iteration's prompt is a resource. Bound it by CHARACTERS, not item count, and cap it at write time. A monotonically growing steering artifact will silently kill the loop on the same timeout cap; when it does, the log looks exactly like a rate-limit stall - distinguish by content, not size.

### [INC-0025](../../incidents/INC-0025-retrying-a-killed-verification-step-without-resumable-eviden.md) - Retrying a killed verification step without resumable evidence is one failure, not four chances
- occurrences 1, severity high, status open
- **Signature:** Every attempt of the same step fails identically, at the same duration, with the same short timeout log. The retry count in the logs looks like resilience, while the outcome is exactly the outcome of one attempt.
- **Rule:** A retry is a second chance only if something carried forward. Under a hard cap, N retries of a deterministic over-budget step is one failure repeated N times. Give the step a place to record partial results, key that record to the exact input state so a stale one is discarded, and keep it OUT of the channel a parser reads as the verdict.

### [INC-0131](../../incidents/INC-0131-a-stage-hang-deadline-copied-from-a-planning-estimate-killed.md) - A stage hang deadline copied from a planning estimate killed a correct run once heavier tests joined
- occurrences 1, severity medium, status fixed
- **Signature:** A stage that passed earlier is killed after more tests are added.
- **Rule:** Measure, then set deadlines.

### [INC-0143](../../incidents/INC-0143-two-branches-implementing-the-same-stage-split-were-merged-w.md) - Two branches implementing the same stage split were merged without re-measuring, although merged tests can change a project time several times over
- occurrences 1, severity medium, status fixed
- **Signature:** A merged stage split keeps timings measured before the merge.
- **Rule:** Re-measure after a merge that changes the tests in a stage.

### [INC-0209](../../incidents/INC-0209-a-full-step-deadline-was-shorter-than-the-measured-stage-tim.md) - A FULL step deadline was shorter than the measured stage time
- occurrences 1, severity medium, status fixed
- **Signature:** The deadline sat below the measured time.
- **Rule:** Recheck FULL step budgets against measured FAST stage times whenever the suite grows

### [INC-0308](../../incidents/INC-0308-a-fixed-stage-deadline-met-planned-case-growth-that-nobody-h.md) - A fixed stage deadline met planned case growth that nobody had projected
- occurrences 1, severity medium, status fixed
- **Signature:** A stage deadline measured at 24 cases was about to carry 105.
- **Rule:** When an acceptance checklist adds cases to a bounded stage, project the stage time per rung and decide who re-measures before the load, not after the first timeout

### [INC-0333](../../incidents/INC-0333-a-per-commit-stage-cost-more-than-doubled-before-anyone-samp.md) - A per-commit stage cost more than doubled before anyone sampled it
- occurrences 1, severity medium, status fixed
- **Signature:** The first stage sample came after several review rounds and showed far more than the design assumed.
- **Rule:** When a row adds tests to a shared per-commit gate, sample the stage early and compare with the design assumption; move heavy proofs to the slower tier rather than raising the cap

### [INC-0529](../../incidents/INC-0529-a-full-run-stopped-at-the-unit-step-because-one-test-hit-the.md) - A full run stopped at the unit step because one test hit the runner's default five-second bound while host load rose sevenfold
- occurrences 1, severity medium, status mitigated
- **Signature:** A unit test fails with a timeout at the runner's default bound, and the host load at the end of the step is many times that at its start.
- **Rule:** A per-test bound left at the runner default is a decision nobody made; set it at the project level for the load class the step runs in, and treat a default-bound timeout under load as a wasted run, not a red.

### [INC-0590](../../incidents/INC-0590-a-full-acceptance-run-stopped-at-a-step-hang-limit-with-ever.md) - A full acceptance run stopped at a step hang limit with every reported case passing, and the budget was raised from measured times
- occurrences 1, severity medium, status mitigated
- **Signature:** A step stops at its hang limit after a partial report in which every case passed, and the wrapper exits 0.
- **Rule:** When a step stops at its hang limit with all reported cases passing, do not call it green or red and do not rerun into the same limit; raise the budget from measured times, cite them, then rerun.

### [INC-0521](../../incidents/INC-0521-three-unit-tests-timed-out-at-a-short-child-process-bound-un.md) - Three unit tests timed out at a short child-process bound under parallel load and passed in isolation
- occurrences 1, severity low, status mitigated
- **Signature:** Tests that spawn a child process fail with a spawn timeout at a five-second bound only while the host is loaded.
- **Rule:** A short child-process bound fails under parallel load while the test is correct; classify such a timeout by an isolated rerun, and give child-process tests a bound that tolerates the load class they run in.

### [INC-0551](../../incidents/INC-0551-a-test-that-passed-alone-at-about-63-percent-of-its-timeout.md) - A test that passed alone at about 63 percent of its timeout budget timed out in a loaded whole-suite run
- occurrences 1, severity low, status mitigated
- **Signature:** A test finishes at well over half of its budget alone, then times out under load.
- **Rule:** A test that needs over half its timeout budget alone will time out under load; raise the budget with the measured duration recorded, and do not touch the assertion.

### [INC-0591](../../incidents/INC-0591-a-triage-showed-a-neighbouring-step-already-at-69-percent-of.md) - A triage showed a neighbouring step already at 69 percent of its limit at lower load, so the budget ruling covered it before it failed
- occurrences 1, severity low, status mitigated
- **Signature:** A step that passed in an earlier run used most of its hang limit at lower load than the run that failed.
- **Rule:** When raising one step budget for load slowdown, check each sibling step's measured share of its limit and cover any that would fail at that slowdown in the same ruling.
