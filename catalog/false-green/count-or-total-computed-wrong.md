# A reported count, total or ledger does not match what ran

[Catalog](../README.md) / [false-green](README.md) / count-or-total-computed-wrong

**Go here if:** A row count, failure count, test total or coverage ledger is off: escaped delimiters, a header row, a missing runner, a word match, renamed checks, or totals that hide which items moved.

**Rule:** Compute counts from structured sources (runner summary lines, parsed tables, the exact bytes executed) with the same formula as the earlier record, reconcile by item identity rather than totals, and cross-check any count by a second method before it reaches a verdict.

6 incidents, 6 occurrences. Ordered by occurrences, then severity, then id.

## Incidents

### [INC-0174](../../incidents/INC-0174-a-count-change-was-reconciled-by-totals-and-a-route-switch-l.md) - A count change was reconciled by totals and a route switch leaked into the default path
- occurrences 1, severity medium, status fixed
- **Signature:** Totals matched while the contents differed.
- **Rule:** Explain a count change by file identity, not by totals.

### [INC-0252](../../incidents/INC-0252-a-word-grep-reported-a-failure-in-a-passing-log.md) - A word grep reported a failure in a passing log
- occurrences 1, severity medium, status fixed
- **Signature:** A test title contained the word.
- **Rule:** Count failures from runner summary lines, never from a word match

### [INC-0259](../../incidents/INC-0259-sum-every-runner-the-earlier-record-summed.md) - Sum every runner the earlier record summed
- occurrences 1, severity medium, status fixed
- **Signature:** A reported total omitted one runner.
- **Rule:** Compute a total with the same formula as the earlier record, covering every runner

### [INC-0310](../../incidents/INC-0310-a-coverage-ledger-keyed-on-report-names-missed-a-scoped-run.md) - A coverage ledger keyed on report names missed a scoped run of the exact bytes
- occurrences 1, severity medium, status fixed
- **Signature:** The ledger called a red check stale while a reviewer had already executed the exact terminal file.
- **Rule:** Key coverage ledgers on the exact bytes executed, from any report, not on report names

### [INC-0323](../../incidents/INC-0323-a-red-run-that-also-renamed-its-checks-counted-name-drift-as.md) - A red run that also renamed its checks counted name drift as defects
- occurrences 1, severity medium, status fixed
- **Signature:** A large failure count included checks that failed only because they were renamed.
- **Rule:** A red-first run that also renames checks shows real behavioural reds per fix, paired with aggregate and exit evidence, never a bare failure count

### [INC-0070](../../incidents/INC-0070-two-reviewers-table-parsers-undercounted-rows-on-escaped-pip.md) - Two reviewers' table parsers undercounted rows on escaped pipes and a sum included a header
- occurrences 1, severity low, status fixed
- **Signature:** A count or sum of table rows comes from splitting lines on the column delimiter, and some cells contain the delimiter escaped.
- **Rule:** Parse table syntax properly before reporting a count, and cross-check any count or sum against a second method before it reaches a verdict.
