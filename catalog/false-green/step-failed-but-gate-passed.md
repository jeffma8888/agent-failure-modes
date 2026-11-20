# A gate verdict came from a wrapper, pipe, chain or last line

[Catalog](../README.md) / [false-green](README.md) / step-failed-but-gate-passed

**Go here if:** A gate passed or a script carried on although a step failed: a wrapper exited 0, a pipe hid the status, a chain kept going, or the verdict came from the last line or exit code alone.

**Rule:** Take each step's verdict from its own status and output: set pipefail or capture status on the next line, stop a chain at the first failure, gate on step records not a wrapper's exit, fail a clean-pass control on error text, never chain a required write after a diagnostic and check the file exists, re-read a dependent write's precondition before it, and prove a failing child turns the gate red.

13 incidents, 13 occurrences. Ordered by occurrences, then severity, then id.

## Incidents

### [INC-0490](../../incidents/INC-0490-a-wrapper-exited-zero-while-a-step-record-said-the-step-fail.md) - A wrapper exited zero while a step record said the step failed
- occurrences 2, severity medium, status mitigated
- **Signature:** The wrapper exit status was zero and one step record said failed by timeout.
- **Rule:** Gate on the step records, never on the wrapper exit status; a wrapper can exit zero while a step record says failed.
- **Recurrences:**
  - [INC-0566](../../incidents/INC-0566-a-run-wrapper-exited-zero-although-one-of-its-steps-exited-o.md) - 2026-11-04 - A run wrapper exited zero although one of its steps exited one

### [INC-0480](../../incidents/INC-0480-a-push-gate-that-piped-the-test-run-into-a-trimming-command.md) - A push gate that piped the test run into a trimming command would have pushed even if the tests had failed
- occurrences 2, severity low, status fixed
- **Signature:** A gating command was piped, so the gate read the last command status.
- **Rule:** Never pipe a gating command; capture its exit status first, by pipefail or by writing to a file and checking the status before reading the file.
- **Recurrences:**
  - [INC-0623](../../incidents/INC-0623-a-helper-piped-to-tail-and-followed-by-ran-the-next-step-alt.md) - 2026-11-04 - A helper piped to tail and followed by && ran the next step although the helper failed, because a pipeline's status is its last command's

### [INC-0120](../../incidents/INC-0120-a-guard-control-asserted-only-exit-0-so-a-warn-and-pass-guar.md) - A guard control asserted only exit 0, so a warn-and-pass guard looked like a clean pass
- occurrences 1, severity medium, status fixed
- **Signature:** A guard that prints an error but exits 0 passes a control that checks the exit code.
- **Rule:** Check output as well as exit status in a clean-pass control.

### [INC-0280](../../incidents/INC-0280-never-chain-a-write-after-a-diagnostic.md) - Never chain a write after a diagnostic
- occurrences 1, severity medium, status fixed
- **Signature:** A write skipped by a failed diagnostic left every later check green.
- **Rule:** Never chain a write after a diagnostic with &&; assert the written file exists before trusting later checks

### [INC-0322](../../incidents/INC-0322-a-search-helper-ended-a-gather-loop-at-the-first-file-withou.md) - A search helper ended a gather loop at the first file without a match
- occurrences 1, severity medium, status fixed
- **Signature:** A loop printed results for some inputs and silently skipped the rest.
- **Rule:** In loops, use a tool whose no-match status you control (append a guard) and check that every iteration printed

### [INC-0347](../../incidents/INC-0347-a-final-print-in-a-wrapper-replaced-the-command-s-failure-wi.md) - A final print in a wrapper replaced the command's failure with success
- occurrences 1, severity medium, status fixed
- **Signature:** A generated run script ended with a print statement and no explicit exit, so a red gate returned zero.
- **Rule:** In a wrapper, save the exit status on the very next line and end with an explicit exit of it; prove a nonzero child makes the wrapper nonzero

### [INC-0396](../../incidents/INC-0396-a-multi-step-command-reported-success-for-its-later-steps-wh.md) - A multi-step command reported success for its later steps while its middle step had not happened
- occurrences 1, severity medium, status fixed
- **Signature:** A command's final output said done while one step had never run.
- **Rule:** Verify each landing by the commit log, never by the last line of the command

### [INC-0620](../../incidents/INC-0620-a-publish-gate-chain-ran-a-build-script-at-a-path-that-does.md) - A publish gate chain ran a build script at a path that does not exist, printed the failing exit status and carried on to the export and the leak scan
- occurrences 1, severity medium, status mitigated
- **Signature:** A chained gate prints a non-zero status for one step and still runs the steps after it.
- **Rule:** A gate chain stops at the first failed step; a printed status is not a check.

### [INC-0625](../../incidents/INC-0625-a-walk-script-ran-a-signed-write-whose-precondition-was-abse.md) - A walk script ran a signed write whose precondition was absent because the step before it had been refused, and the write succeeded on a record that never met the condition
- occurrences 1, severity medium, status mitigated
- **Signature:** A dependent step succeeds on a record that never reached the state the step requires.
- **Rule:** A script asserts each dependent step's precondition with a fresh read right before the write and exits before any later step on failure.

### [INC-0382](../../incidents/INC-0382-a-click-around-walk-that-always-exits-1-from-a-known-gap-can.md) - A click-around walk that always exits 1 from a known gap cannot gate regressions
- occurrences 1, severity low, status fixed
- **Signature:** A walk reported failure on every run, so a new failure was indistinguishable.
- **Rule:** Compare a walk with a known gap against a named baseline result; an exit code that is always failing cannot gate

### [INC-0389](../../incidents/INC-0389-two-plan-checks-ran-at-a-wrong-script-path-and-the-last-line.md) - Two plan checks ran at a wrong script path and the last line of their output looked like a result
- occurrences 1, severity low, status fixed
- **Signature:** A crashed check ended with a line that resembled a result.
- **Rule:** Match the explicit pass line of a check, never its last line
