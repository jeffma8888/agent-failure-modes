# The checker ran but its target coverage is unproven

[Catalog](../README.md) / [detector-fail-open](README.md) / coverage-and-controls-not-proven

**Go here if:** A successful checker or recorder misses its target, scans the wrong baseline, includes excluded files or ignores required history.

**Rule:** Prove intended checker scope with explicit baseline, collected-target and per-observation evidence plus known-bad and known-good controls; require known events to be observed, distinguish empty results from failed collection and scan the full publishable range before accepting silence.

9 incidents, 9 occurrences. Ordered by occurrences, then severity, then id.

## Incidents

### [INC-0596](../../incidents/INC-0596-an-observer-recorded-zero-denied-connects-while-it-also-miss.md) - An observer recorded zero denied connects while it also missed the server's database connect, so zero denied proved nothing
- occurrences 1, severity high, status mitigated
- **Signature:** A monitor reports zero violations and zero of an event that must occur.
- **Rule:** Before trusting a zero-violations monitor, require a positive control: a known event it must record in the process that makes it.

### [INC-0037](../../incidents/INC-0037-a-liveness-check-built-on-a-process-table-grep-counts-itself.md) - A liveness check built on a process-table grep counts itself
- occurrences 1, severity medium, status fixed
- **Signature:** A 'something is running' check is never false. The measured count is exactly one more than the truth, and it reads one at moments when you know for certain that nothing is running.
- **Rule:** A process-table grep counts itself - the measuring command's arguments contain the search term, so a 'something is running' check is never false. Use a matcher that excludes its own process, and prove any busy/idle check TWO-SIDED: zero when nothing runs, non-zero with one known worker. A check never seen returning false has not been tested.

### [INC-0069](../../incidents/INC-0069-a-gate-compared-the-candidate-commit-with-itself-because-a-l.md) - A gate compared the candidate commit with itself because a local clone redefines the remote-tracking ref
- occurrences 1, severity medium, status mitigated
- **Signature:** A check diffs against the main branch of the remote, and it runs in a fresh clone of a local checkout rather than of the real remote.
- **Rule:** A check that runs inside a clone must not rely on remote-tracking refs. State the baseline commit explicitly, and reproduce the ref topology in a scratch repo before trusting the check.

### [INC-0140](../../incidents/INC-0140-a-known-red-was-listed-before-checking-the-scan-roots-of-the.md) - A known red was listed before checking the scan roots of the hygiene rule that raised it
- occurrences 1, severity medium, status fixed
- **Signature:** A finding is recorded as a known failure without confirming the rule scans that file.
- **Rule:** Confirm a rule scope before reporting its finding.

### [INC-0186](../../incidents/INC-0186-a-per-root-checker-summary-undercounted-edges.md) - A per-root checker summary undercounted edges
- occurrences 1, severity medium, status fixed
- **Signature:** The summary showed fewer edges than the manifests hold.
- **Rule:** Derive the marker set from the manifests, not from a per-root summary.

### [INC-0215](../../incidents/INC-0215-a-commit-skipped-the-machine-wide-pre-commit-scanner.md) - A commit skipped the machine-wide pre-commit scanner
- occurrences 1, severity medium, status fixed
- **Signature:** The scanner never ran.
- **Rule:** Never override the hook path; if it happens, amend with hooks on right away

### [INC-0292](../../incidents/INC-0292-a-snapshot-recorder-that-finished-was-taken-as-proof-it-had.md) - A snapshot recorder that finished was taken as proof it had collected
- occurrences 1, severity medium, status fixed
- **Signature:** A recorder reached its completion message while observations were missing.
- **Rule:** Completion is not collection; require per-observation status and distinguish empty from failed

### [INC-0372](../../incidents/INC-0372-a-test-run-s-command-line-exclusion-flag-did-not-take-effect.md) - A test run's command-line exclusion flag did not take effect, so excluded cases ran and called the package manager
- occurrences 1, severity medium, status fixed
- **Signature:** Cases that were meant to be excluded from a run executed anyway.
- **Rule:** List the collected files before a filtered run and stop if any excluded file is still collected

### [INC-0504](../../incidents/INC-0504-a-branch-scrubbed-a-local-path-in-a-later-commit-and-a-range.md) - A branch scrubbed a local path in a later commit, and a range scan found it still in history
- occurrences 1, severity low, status mitigated
- **Signature:** The final tree passes a leak scan, and a scan of every commit of the range does not.
- **Rule:** Scan every commit of a range, not only the final tree, before merging anything that will be pushed; a scrub in a later commit does not clean history.
