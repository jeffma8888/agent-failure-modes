# Timing models or optimizations are not measured

[Catalog](../README.md) / [stage-timeout](README.md) / timing-models-and-critical-path

**Go here if:** A split saves nothing, a speedup ignores serial work or an incomplete or loaded run is treated as calibrated headroom.

**Rule:** Base timing models and optimizations on repeated, complete measurements of the exact tree with load recorded; profile the real critical path, retain protected cases, include serial work and cold starts, and apply the required margin rather than the full deadline.

8 incidents, 8 occurrences. Ordered by occurrences, then severity, then id.

## Incidents

### [INC-0187](../../incidents/INC-0187-a-slow-stage-was-trimmed-by-cases-instead-of-cut-by-grouping.md) - A slow stage was trimmed by cases instead of cut by grouping files
- occurrences 1, severity medium, status fixed
- **Signature:** A stage kept growing while case trimming saved little.
- **Rule:** Group files that parallelize cleanly; do not trim cases whose timeouts are fixed.

### [INC-0195](../../incidents/INC-0195-a-single-stage-time-on-a-loaded-host-was-read-as-a-measureme.md) - A single stage time on a loaded host was read as a measurement
- occurrences 1, severity medium, status fixed
- **Signature:** The same tree read 30.5 s and then 14.9 s.
- **Rule:** Decide timing rules on repeated runs with the load recorded, never on one stage time

### [INC-0210](../../incidents/INC-0210-a-slow-suite-was-a-candidate-for-cutting-before-it-was-profi.md) - A slow suite was a candidate for cutting before it was profiled
- occurrences 1, severity medium, status fixed
- **Signature:** The slow part was not where cuts would land.
- **Rule:** Profile before cutting tests

### [INC-0230](../../incidents/INC-0230-a-split-of-the-dominant-test-file-saved-about-zero.md) - A split of the dominant test file saved about zero
- occurrences 1, severity medium, status fixed
- **Signature:** The split was on the shorter branch of the critical path.
- **Rule:** Profile a dominant file and check shared inventory assertions and the critical path before splitting it

### [INC-0271](../../incidents/INC-0271-a-load-induced-harness-red-is-not-headroom.md) - A load-induced harness red is not headroom
- occurrences 1, severity medium, status fixed
- **Signature:** A run stopped early under load and its remaining time looked like spare budget.
- **Rule:** Do not count the arithmetic distance to a budget as headroom when later stages never ran

### [INC-0312](../../incidents/INC-0312-a-whole-stage-was-divided-by-a-parallel-speedup-although-par.md) - A whole stage was divided by a parallel speedup although part of it had to stay serial
- occurrences 1, severity medium, status fixed
- **Signature:** A projected stage time divided the serial files by the speedup too.
- **Rule:** Model a parallelised stage as serial work plus parallel makespan plus new cold starts, never as total time over N

### [INC-0345](../../incidents/INC-0345-a-timing-anchor-derived-by-subtraction-was-used-as-if-it-wer.md) - A timing anchor derived by subtraction was used as if it were a measurement
- occurrences 1, severity medium, status fixed
- **Signature:** A budget model anchored on a stage time obtained by subtraction, while quiet measured samples were higher.
- **Rule:** Replace a derived timing anchor with a measured one as soon as the thing exists, and recompute every threshold it feeds

### [INC-0348](../../incidents/INC-0348-a-deadline-set-at-twice-the-slowest-sample-was-budgeted-agai.md) - A deadline set at twice the slowest sample was budgeted against the whole deadline
- occurrences 1, severity medium, status fixed
- **Signature:** A stage was projected safe until it reached its deadline, while one sample already broke the real binding line.
- **Rule:** When a rule demands margin k, the budget is the deadline divided by k; track the slowest sample against that, not the deadline
