# Stale or overbroad load gates block or mis-admit work

[Catalog](../README.md) / [stage-timeout](README.md) / stale-or-overbroad-load-admission

**Go here if:** A launch ignores a denying read, uses stale approval or a blanket gate repeatedly refuses small or timing-insensitive work.

**Rule:** Apply the documented freshness window and workload-specific threshold before launch side effects, stop when the gate denies, and wait only within a bounded admission loop; inspect load producers without altering unrelated processes rather than applying a full-run gate to every task.

8 incidents, 8 occurrences. Ordered by occurrences, then severity, then id.

## Incidents

### [INC-0500](../../incidents/INC-0500-one-load-gate-sized-for-full-runs-was-applied-to-every-run-a.md) - One load gate sized for full runs was applied to every run, and scoped runs were refused while the real load producer went unexamined
- occurrences 1, severity medium, status mitigated
- **Signature:** A single load threshold chosen for full-suite runs refuses small scoped runs once several teammates work in parallel.
- **Rule:** Size an admission gate to the class of run it protects, and find what is actually producing the load before tightening or waiting on it.

### [INC-0512](../../incidents/INC-0512-read-once-and-refuse-load-admission-stopped-whole-teammate-c.md) - Read-once-and-refuse load admission stopped whole teammate cycles while load spiked and fell within a minute
- occurrences 1, severity medium, status mitigated
- **Signature:** A launch is refused on one load reading, and the next reading a minute later would have admitted it.
- **Rule:** When load is spiky, admit by waiting for the gate with a bounded timeout and a printed admitting reading, not by one reading at launch.

### [INC-0393](../../incidents/INC-0393-a-load-reading-taken-minutes-before-a-launch-was-stale-and-t.md) - A load reading taken minutes before a launch was stale, and the launch read much higher
- occurrences 1, severity low, status fixed
- **Signature:** A load gate passed from a reading that no longer described the host.
- **Rule:** Gate on load where you launch, immediately before; an earlier or second-hand reading is stale

### [INC-0417](../../incidents/INC-0417-a-load-gate-read-and-a-launch-chained-in-one-command-let-a-u.md) - A load gate read and a launch chained in one command let a unit probe start at a load above the gate
- occurrences 1, severity low, status fixed
- **Signature:** A probe started on a host whose load was far above the gate.
- **Rule:** Run the load read and the launch as two separate commands; a reading at or above the gate stops the launch

### [INC-0427](../../incidents/INC-0427-a-host-load-spike-came-from-operating-system-daemons-not-the.md) - A host load spike came from operating system daemons, not the team, and the load wait held
- occurrences 1, severity low, status fixed
- **Signature:** Host load was far above the gate while no team run was active.
- **Rule:** A load gate holds regardless of who causes the load; continue static work and do not touch system daemons

### [INC-0450](../../incidents/INC-0450-a-load-gate-stop-was-the-right-call-and-cost-nothing-because.md) - A load gate stop was the right call and cost nothing because the runner created nothing before the check
- occurrences 1, severity low, status fixed
- **Signature:** A run stopped at the gate while the host was overloaded.
- **Rule:** Put the load check before anything is created, so a gate stop costs nothing and leaves nothing to tear down

### [INC-0465](../../incidents/INC-0465-an-admission-sent-at-a-low-load-reading-reached-the-runner-a.md) - An admission sent at a low load reading reached the runner after the load rose again, and the runner fresh reading then refused it
- occurrences 1, severity low, status fixed
- **Signature:** A runner refused a step that had just been admitted.
- **Rule:** An admission admits the step: a reading within 60 seconds of the admission is a record, and a reading after that is a fresh gate

### [INC-0508](../../incidents/INC-0508-a-build-step-was-given-the-load-threshold-meant-for-timing-s.md) - A build step was given the load threshold meant for timing-sensitive runs and was refused twice while the host was busy
- occurrences 1, severity low, status mitigated
- **Signature:** A strict admission threshold designed for timing-sensitive runs is applied to a step whose result does not depend on timing.
- **Rule:** Pick each step load threshold by whether its result depends on timing; a build that only gets slower uses the looser class.
