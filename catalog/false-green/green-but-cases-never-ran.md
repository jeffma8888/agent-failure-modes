# The gate was green but the cases it vouches for never executed

[Catalog](../README.md) / [false-green](README.md) / green-but-cases-never-ran

**Go here if:** A pass, hold or acceptance is cited, but the new tests, selected projects, real commands or eligible population were empty, skipped, stubbed, or first ran after the merge.

**Rule:** Before citing a green, count what actually executed: cases per project, each new test file by its own marker, real commands rather than stubs, a non-empty population. A skipped, refused, setup-only or empty run is missing evidence, never a pass; a no-op outcome needs before/after proof.

14 incidents, 14 occurrences. Ordered by occurrences, then severity, then id.

## Incidents

### [INC-0447](../../incidents/INC-0447-tests-authored-but-never-executed-passed-acceptance-and-the.md) - Tests authored but never executed passed acceptance, and the first run of the heavy tier found a failing case
- occurrences 2, severity low, status fixed
- **Signature:** A row was signed off with part of its tests never run.
- **Rule:** Accept a production merge only after the heavy test tier passes on the merged tree; authored but unexecuted cases are missing evidence, not a pass
- **Recurrences:**
  - [INC-0482](../../incidents/INC-0482-tests-added-by-a-branch-were-never-run-before-the-merge-and.md) - 2026-11-02 - Tests added by a branch were never run before the merge, and the full suite failed on them afterwards

### [INC-0196](../../incidents/INC-0196-an-allowlist-fix-turned-gate-tests-green-while-the-runner-sk.md) - An allowlist fix turned gate tests green while the runner skipped the new project
- occurrences 1, severity medium, status fixed
- **Signature:** The gate tests passed and the new project never ran.
- **Rule:** Prove a new project ran by its own marker, not only by the shared stage record

### [INC-0203](../../incidents/INC-0203-a-setup-failure-was-at-risk-of-counting-as-a-test-run.md) - A setup failure was at risk of counting as a test run
- occurrences 1, severity medium, status fixed
- **Signature:** The run failed before any test started.
- **Rule:** Do not count a setup-only failure as a run

### [INC-0239](../../incidents/INC-0239-a-hold-outcome-had-no-proof-that-nothing-changed.md) - A hold outcome had no proof that nothing changed
- occurrences 1, severity medium, status fixed
- **Signature:** No change looks the same as no run.
- **Rule:** Prove a hold by the remote main SHA unchanged before and after and an empty porcelain on the build clone

### [INC-0253](../../incidents/INC-0253-two-of-four-selected-projects-executed-no-case.md) - Two of four selected projects executed no case
- occurrences 1, severity medium, status fixed
- **Signature:** The selection looked like coverage.
- **Rule:** Record executed cases per project; a selected project is not coverage

### [INC-0266](../../incidents/INC-0266-a-planned-round-with-stop-in-place-proves-nothing.md) - A planned round with STOP in place proves nothing
- occurrences 1, severity medium, status fixed
- **Signature:** A planned round would have been skipped silently by a stop gate.
- **Rule:** Never count a round as proof while a silent skip gate is in place; verify it actually ran

### [INC-0283](../../incidents/INC-0283-a-hold-gate-is-proven-only-while-eligible-work-exists.md) - A hold gate is proven only while eligible work exists
- occurrences 1, severity medium, status fixed
- **Signature:** A hold looked proven when the queue had nothing to select.
- **Rule:** Prove a hold gate only with eligible work present; an empty queue proves nothing

### [INC-0290](../../incidents/INC-0290-a-setup-hook-was-sized-from-file-time-or-from-a-refused-atte.md) - A setup hook was sized from file time, or from a refused attempt
- occurrences 1, severity medium, status fixed
- **Signature:** A hook timeout was chosen without measuring the hook itself.
- **Rule:** Measure the hook itself, count only runs that executed, and mark owed measurements as owed

### [INC-0321](../../incidents/INC-0321-a-green-parallel-run-was-cited-although-the-parallel-group-h.md) - A green parallel run was cited although the parallel group held no files
- occurrences 1, severity medium, status fixed
- **Signature:** The parallel pass was green over zero files.
- **Rule:** Count the population a mode actually runs before citing its green; while it is empty, proof comes from forced-overlap probes

### [INC-0356](../../incidents/INC-0356-a-reviewed-recipe-never-ran-its-real-tool-queries-because-ev.md) - A reviewed recipe never ran its real tool queries because every control stubbed them
- occurrences 1, severity medium, status fixed
- **Signature:** A recipe passed its dry run, control run and copy cases, then its first real run stopped in preparation on an unsupported option.
- **Rule:** A stubbed control proves the recipe's logic, not its commands; before an authorized run, execute every real read-only command once against the pinned tool versions

### [INC-0461](../../incidents/INC-0461-a-hook-ran-a-query-on-create-with-an-undefined-id-once-a-reg.md) - A hook ran a query on create with an undefined id once a registry became non empty: a latent defect exposed by data, not code
- occurrences 1, severity low, status fixed
- **Signature:** A seed failed with a database type error after a data change.
- **Rule:** Guard a hook query on the operation and a valid id; a check over an empty population proves nothing about the non empty case

### [INC-0477](../../incidents/INC-0477-a-browser-test-failed-at-its-first-request-and-after-that-wa.md) - A browser test failed at its first request, and after that was fixed the next run failed at a step that had never run
- occurrences 1, severity low, status fixed
- **Signature:** Fixing an early test failure exposed a later step that had never run.
- **Rule:** When a fix moves a failure later in a test, treat every newly reached step as never verified; a green earlier step proves only that step.

### [INC-0485](../../incidents/INC-0485-a-merge-checklist-drafted-early-found-a-test-change-the-merg.md) - A merge checklist drafted early found a test change the merge would have broken
- occurrences 1, severity low, status mitigated
- **Signature:** A source change altered a seed record, while a unit test still asserted the old shape.
- **Rule:** Draft the merge acceptance checklist while the row is still open, and for each source change read the tests that assert on it, so owed test changes are found before the merge turns the full run red.
