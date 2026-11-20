# A shell chain ran on after a failed step, or a refusal sank safe steps

[Catalog](../README.md) / [tooling-paths](README.md) / chain-ran-on-after-failure

**Go here if:** A commit, push or cleanup ran although an earlier edit or check failed; the chain saw the formatter's status; a script died in an unrehearsed step; an approval refusal discarded bundled edits.

**Rule:** Validate every precondition before the first write, join dependent steps with && (never ; or a pipe into a formatter), print each step's exit status, put external and destructive writes last, split the chain at every approval boundary, and dry-run the WHOLE script on scratch copies.

6 incidents, 6 occurrences. Ordered by occurrences, then severity, then id.

## Incidents

### [INC-0294](../../incidents/INC-0294-activating-a-replacement-over-the-only-file-in-a-directory-r.md) - Activating a replacement over the only file in a directory removed the directory
- occurrences 1, severity medium, status fixed
- **Signature:** A move failed halfway because removing the sole file removed its parent.
- **Rule:** Before a remove-and-move, check whether the file is alone in its directory, and run pending checks first

### [INC-0364](../../incidents/INC-0364-a-hand-written-landing-chain-swallowed-a-failed-post-commit.md) - A hand-written landing chain swallowed a failed post-commit leak scan and three commits landed on top
- occurrences 1, severity medium, status fixed
- **Signature:** A landing step printed nothing and the chain moved on, although the script it ran had exited non-zero.
- **Rule:** Print the exit status of every commit and check step explicitly (never only on success), run the range leak scan before landing anything on top of a new commit, and use the guarded landing helper, not an ad-hoc chain

### [INC-0046](../../incidents/INC-0046-a-script-with-external-writes-was-only-dry-run-for-its-first.md) - A script with external writes was only dry-run for its first step, and only write-last ordering made its failure harmless
- occurrences 1, severity low, status fixed
- **Signature:** A multi-step script that pushes or resets exits non-zero partway through its first real run, having only been rehearsed on its hardest step.
- **Rule:** In any script that writes externally, order every fallible local step first and every external write last, and dry-run the WHOLE script end to end against scratch copies before the real run, not just its hardest step.

### [INC-0050](../../incidents/INC-0050-bundling-safe-local-steps-with-an-approval-gated-step-loses.md) - Bundling safe local steps with an approval-gated step loses the local steps when the gate refuses
- occurrences 1, severity low, status fixed
- **Signature:** A single shell command performs an edit, a commit and a push, and the push is subject to a per-call human approval rule.
- **Rule:** Never bundle unattended-safe steps with a step that needs a human's approval. Split the chain at the approval boundary so a refusal costs only the gated step.

### [INC-0051](../../incidents/INC-0051-a-fallible-edit-script-followed-by-a-semicolon-let-the-commi.md) - A fallible edit script followed by a semicolon let the commit run on a partial result
- occurrences 1, severity low, status fixed
- **Signature:** A script that writes several files is followed by a commit joined with a semicolon, and the script's output contains a traceback.
- **Rule:** Validate all preconditions before the first write, and never let a later step run after an earlier one failed: join dependent steps with a short-circuit and, not a semicolon.

### [INC-0357](../../incidents/INC-0357-a-landing-helper-piped-a-guarded-commit-into-a-formatter-so.md) - A landing helper piped a guarded commit into a formatter, so the guard's failure did not stop the cleanup
- occurrences 1, severity low, status fixed
- **Signature:** A scrub guard failed, yet the helper went on to delete the source file because the pipeline reported the formatter's zero status.
- **Rule:** Never pipe a gating command into a formatter in a chain whose later steps destroy the input; check the gate's own exit status
