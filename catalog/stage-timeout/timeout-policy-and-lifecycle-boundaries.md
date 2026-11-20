# Timeout policy ignores purpose, call path or lifecycle

[Catalog](../README.md) / [stage-timeout](README.md) / timeout-policy-and-lifecycle-boundaries

**Go here if:** The same timeout contract is enforced differently from what its current policy promises when the work reaches the actual execution path.

**Rule:** Define each timeout purpose, scope and rationale in the current policy, then verify it in active code on every dependent path; use group-wide lifetime and global elapsed time for global shutdown contracts.

7 incidents, 7 occurrences. Ordered by occurrences, then severity, then id.

## Incidents

### [INC-0092](../../incidents/INC-0092-a-whole-group-termination-grace-period-was-shorter-than-the.md) - A whole-group termination grace period was shorter than the wrapper process, so the wrapper exit ended the wait early
- occurrences 1, severity medium, status fixed
- **Signature:** A shutdown waits for a process group, but the wait ends when the wrapper process exits.
- **Rule:** Bind a group shutdown wait to the group, not to a wrapper that can exit first.

### [INC-0093](../../incidents/INC-0093-a-smoke-run-deadline-shared-the-normal-step-budget-policy.md) - A smoke-run deadline shared the normal step budget policy
- occurrences 1, severity medium, status fixed
- **Signature:** One timeout policy covers both quick steps and a long smoke run.
- **Rule:** Give runs with different deadline purposes their own policy.

### [INC-0107](../../incidents/INC-0107-a-timeout-override-was-not-re-checked-against-the-newest-rul.md) - A timeout override was not re-checked against the newest ruling, and fixes were verified from the coverage note
- occurrences 1, severity medium, status fixed
- **Signature:** A revision lands after a ruling and keeps an override that the ruling changed.
- **Rule:** Verify from the code line, not from the note that describes it.

### [INC-0111](../../incidents/INC-0111-http-only-timeouts-were-copied-from-a-process-hang-pattern-w.md) - HTTP-only timeouts were copied from a process-hang pattern without the reason
- occurrences 1, severity medium, status fixed
- **Signature:** A timeout override appears in a test where its original cause does not apply.
- **Rule:** An override without a stated reason is not reviewable.

### [INC-0124](../../incidents/INC-0124-a-poll-timeout-placed-in-assertion-options-was-still-a-propa.md) - A poll timeout placed in assertion options was still a propagation override, and shared helpers were left out of the dependent root verdict
- occurrences 1, severity medium, status fixed
- **Signature:** A timeout override hides in assertion options or a shared helper that a root depends on.
- **Rule:** Only an oracle-valued deadline is exempt from the override rule; include shared helpers in each dependent verdict.

### [INC-0139](../../incidents/INC-0139-a-readiness-deadline-tested-only-inside-a-step-was-untested.md) - A readiness deadline tested only inside a step was untested outside it
- occurrences 1, severity medium, status fixed
- **Signature:** A deadline is proven on one code path and ships on another.
- **Rule:** Test the deadline on every path that can reach it.

### [INC-0355](../../incidents/INC-0355-per-item-sequential-timeouts-could-not-meet-a-global-deadlin.md) - Per-item sequential timeouts could not meet a global deadline stated in the spec
- occurrences 1, severity medium, status fixed
- **Signature:** A spec required every process group to be reaped within 10 s, while the shutdown code waited on the groups one after another at about 10 s each.
- **Rule:** When a spec sets a global bound, check the existing per-item loop arithmetic; sequential waits add up
