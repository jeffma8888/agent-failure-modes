# stage-timeout

[Catalog](../README.md) / stage-timeout

A hard per-step wall-clock cap (beneath any outer timeout you set) silently kills work that runs too long. The narration drops and the step looks like it produced nothing.

**Ask:** What is the hardest time cap actually enforced on one step, and how close is the real work to it?

40 incidents filed here (40 occurrences); 9 more filed elsewhere are also tagged stage-timeout.

## Incidents

This class has no topics, so this node is the leaf. Ordered by occurrences, then severity, then id.

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

The 37 entries below are listed by title only so this node stays under 12 KB. Open the page, or run `python3 tools/afm.py show INC-XXXX`, for its signature and rule.

- [INC-0025](../../incidents/INC-0025-retrying-a-killed-verification-step-without-resumable-eviden.md) - Retrying a killed verification step without resumable evidence is one failure, not four chances (n=1, high)
- [INC-0092](../../incidents/INC-0092-a-whole-group-termination-grace-period-was-shorter-than-the.md) - A whole-group termination grace period was shorter than the wrapper process, so the wrapper exit ended the wait early (n=1, medium)
- [INC-0093](../../incidents/INC-0093-a-smoke-run-deadline-shared-the-normal-step-budget-policy.md) - A smoke-run deadline shared the normal step budget policy (n=1, medium)
- [INC-0107](../../incidents/INC-0107-a-timeout-override-was-not-re-checked-against-the-newest-rul.md) - A timeout override was not re-checked against the newest ruling, and fixes were verified from the coverage note (n=1, medium)
- [INC-0111](../../incidents/INC-0111-http-only-timeouts-were-copied-from-a-process-hang-pattern-w.md) - HTTP-only timeouts were copied from a process-hang pattern without the reason (n=1, medium)
- [INC-0124](../../incidents/INC-0124-a-poll-timeout-placed-in-assertion-options-was-still-a-propa.md) - A poll timeout placed in assertion options was still a propagation override, and shared helpers were left out of the dependent root verdict (n=1, medium)
- [INC-0131](../../incidents/INC-0131-a-stage-hang-deadline-copied-from-a-planning-estimate-killed.md) - A stage hang deadline copied from a planning estimate killed a correct run once heavier tests joined (n=1, medium)
- [INC-0139](../../incidents/INC-0139-a-readiness-deadline-tested-only-inside-a-step-was-untested.md) - A readiness deadline tested only inside a step was untested outside it (n=1, medium)
- [INC-0143](../../incidents/INC-0143-two-branches-implementing-the-same-stage-split-were-merged-w.md) - Two branches implementing the same stage split were merged without re-measuring, although merged tests can change a project time several times over (n=1, medium)
- [INC-0187](../../incidents/INC-0187-a-slow-stage-was-trimmed-by-cases-instead-of-cut-by-grouping.md) - A slow stage was trimmed by cases instead of cut by grouping files (n=1, medium)
- [INC-0195](../../incidents/INC-0195-a-single-stage-time-on-a-loaded-host-was-read-as-a-measureme.md) - A single stage time on a loaded host was read as a measurement (n=1, medium)
- [INC-0209](../../incidents/INC-0209-a-full-step-deadline-was-shorter-than-the-measured-stage-tim.md) - A FULL step deadline was shorter than the measured stage time (n=1, medium)
- [INC-0210](../../incidents/INC-0210-a-slow-suite-was-a-candidate-for-cutting-before-it-was-profi.md) - A slow suite was a candidate for cutting before it was profiled (n=1, medium)
- [INC-0218](../../incidents/INC-0218-two-loaded-host-reds-shared-one-cause-and-were-at-risk-of-a.md) - Two loaded-host reds shared one cause and were at risk of a timeout bump (n=1, medium)
- [INC-0230](../../incidents/INC-0230-a-split-of-the-dominant-test-file-saved-about-zero.md) - A split of the dominant test file saved about zero (n=1, medium)
- [INC-0271](../../incidents/INC-0271-a-load-induced-harness-red-is-not-headroom.md) - A load-induced harness red is not headroom (n=1, medium)
- [INC-0308](../../incidents/INC-0308-a-fixed-stage-deadline-met-planned-case-growth-that-nobody-h.md) - A fixed stage deadline met planned case growth that nobody had projected (n=1, medium)
- [INC-0312](../../incidents/INC-0312-a-whole-stage-was-divided-by-a-parallel-speedup-although-par.md) - A whole stage was divided by a parallel speedup although part of it had to stay serial (n=1, medium)
- [INC-0333](../../incidents/INC-0333-a-per-commit-stage-cost-more-than-doubled-before-anyone-samp.md) - A per-commit stage cost more than doubled before anyone sampled it (n=1, medium)
- [INC-0345](../../incidents/INC-0345-a-timing-anchor-derived-by-subtraction-was-used-as-if-it-wer.md) - A timing anchor derived by subtraction was used as if it were a measurement (n=1, medium)
- [INC-0348](../../incidents/INC-0348-a-deadline-set-at-twice-the-slowest-sample-was-budgeted-agai.md) - A deadline set at twice the slowest sample was budgeted against the whole deadline (n=1, medium)
- [INC-0355](../../incidents/INC-0355-per-item-sequential-timeouts-could-not-meet-a-global-deadlin.md) - Per-item sequential timeouts could not meet a global deadline stated in the spec (n=1, medium)
- [INC-0500](../../incidents/INC-0500-one-load-gate-sized-for-full-runs-was-applied-to-every-run-a.md) - One load gate sized for full runs was applied to every run, and scoped runs were refused while the real load producer went unexamined (n=1, medium)
- [INC-0512](../../incidents/INC-0512-read-once-and-refuse-load-admission-stopped-whole-teammate-c.md) - Read-once-and-refuse load admission stopped whole teammate cycles while load spiked and fell within a minute (n=1, medium)
- [INC-0529](../../incidents/INC-0529-a-full-run-stopped-at-the-unit-step-because-one-test-hit-the.md) - A full run stopped at the unit step because one test hit the runner's default five-second bound while host load rose sevenfold (n=1, medium)
- [INC-0590](../../incidents/INC-0590-a-full-acceptance-run-stopped-at-a-step-hang-limit-with-ever.md) - A full acceptance run stopped at a step hang limit with every reported case passing, and the budget was raised from measured times (n=1, medium)
- [INC-0393](../../incidents/INC-0393-a-load-reading-taken-minutes-before-a-launch-was-stale-and-t.md) - A load reading taken minutes before a launch was stale, and the launch read much higher (n=1, low)
- [INC-0417](../../incidents/INC-0417-a-load-gate-read-and-a-launch-chained-in-one-command-let-a-u.md) - A load gate read and a launch chained in one command let a unit probe start at a load above the gate (n=1, low)
- [INC-0427](../../incidents/INC-0427-a-host-load-spike-came-from-operating-system-daemons-not-the.md) - A host load spike came from operating system daemons, not the team, and the load wait held (n=1, low)
- [INC-0444](../../incidents/INC-0444-a-static-closure-packet-that-did-not-converge-in-three-round.md) - A static closure packet that did not converge in three rounds was replaced by running the thing and diagnosing the receipts (n=1, low)
- [INC-0450](../../incidents/INC-0450-a-load-gate-stop-was-the-right-call-and-cost-nothing-because.md) - A load gate stop was the right call and cost nothing because the runner created nothing before the check (n=1, low)
- [INC-0465](../../incidents/INC-0465-an-admission-sent-at-a-low-load-reading-reached-the-runner-a.md) - An admission sent at a low load reading reached the runner after the load rose again, and the runner fresh reading then refused it (n=1, low)
- [INC-0501](../../incidents/INC-0501-an-error-named-only-the-leaf-of-an-import-chain-and-a-rule-t.md) - An error named only the leaf of an import chain, and a rule to add a link only when the next run named it spent a run per link (n=1, low)
- [INC-0508](../../incidents/INC-0508-a-build-step-was-given-the-load-threshold-meant-for-timing-s.md) - A build step was given the load threshold meant for timing-sensitive runs and was refused twice while the host was busy (n=1, low)
- [INC-0521](../../incidents/INC-0521-three-unit-tests-timed-out-at-a-short-child-process-bound-un.md) - Three unit tests timed out at a short child-process bound under parallel load and passed in isolation (n=1, low)
- [INC-0551](../../incidents/INC-0551-a-test-that-passed-alone-at-about-63-percent-of-its-timeout.md) - A test that passed alone at about 63 percent of its timeout budget timed out in a loaded whole-suite run (n=1, low)
- [INC-0591](../../incidents/INC-0591-a-triage-showed-a-neighbouring-step-already-at-69-percent-of.md) - A triage showed a neighbouring step already at 69 percent of its limit at lower load, so the budget ruling covered it before it failed (n=1, low)

## Also tagged stage-timeout

9 incidents filed under another home class also carry this class. Listed by the node where they live:

- [false-green](../false-green/README.md): INC-0168, INC-0236, INC-0290, INC-0291
- [checkpoint](../checkpoint/README.md): INC-0006
- [concurrency](../concurrency/README.md): INC-0219
- [observability](../observability/README.md): INC-0007
- [spec-and-scope](../spec-and-scope/README.md): INC-0071
- [verdict-token](../verdict-token/README.md): INC-0005

## Practices touching this class

- [PRA-0001](../CORE.md#practices) - The enforcement ladder: pick the cheapest rung that makes the failure impossible
- [PRA-0003](../CORE.md#practices) - Six conditions for a gate that cannot be skipped
- [PRA-0005](../CORE.md#practices) - Admission control for an agent team on a shared host
