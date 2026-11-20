# Verified a shortcut, a part or an old revision instead of what ships

[Catalog](../README.md) / [false-green](README.md) / verified-a-different-target

**Go here if:** Results differ between a focused run and the canonical gate, branches alone and merged, tree and branch range; the gate ran without the fix; merged options blur checked vs unchecked; cases ran twice.

**Rule:** Verify the exact thing that ships with the canonical gate's own commands: the merged stack, every caller of a changed helper, the full branch range, a revision that holds the fix. A focused run, one branch or one option alone proves only itself; ask what two safe changes combined let a consumer confuse. A test that launches a runner runs it on a probe file, never the whole suite.

10 incidents, 10 occurrences. Ordered by occurrences, then severity, then id.

## Incidents

### [INC-0035](../../incidents/INC-0035-two-individually-safe-options-are-unsafe-together-when-their.md) - Two individually safe options are unsafe together when their combination leaves a consumer unable to distinguish two states
- occurrences 1, severity high, status fixed
- **Signature:** Two changes, each reviewed and each safe. Nothing in either diff is wrong. The defect exists only in the state the pair produces, and it shows up as a consumer reading a collection whose members no longer all mean the same thing.
- **Rule:** Ask of any two individually safe options whether their COMBINATION leaves a consumer unable to distinguish two states. A per-run bound plus an in-place 'done' marker is the canonical pair: the bound makes 'all of these were checked' false, and the in-place marker deletes the evidence of which ones were. Make the checked set a separate LOCATION, and make any bound visible in the artifact.

### [INC-0163](../../incidents/INC-0163-acceptance-ran-bare-vitest-while-the-real-gate-ran-setup-the.md) - Acceptance ran bare vitest while the real gate ran setup then the FAST runner
- occurrences 1, severity medium, status fixed
- **Signature:** A row merge looked red under the acceptance script and green under preship, or the reverse.
- **Rule:** Acceptance must run the same commands preship runs, otherwise a green merge looks red or a red one looks green.

### [INC-0168](../../incidents/INC-0168-disjoint-project-discovery-did-not-stop-a-suite-from-running.md) - Disjoint project discovery did not stop a suite from running twice
- occurrences 1, severity medium, status fixed
- **Signature:** One stage doubled its cases and its time.
- **Rule:** A test that launches a runner must run it on a probe file, not the whole suite.

### [INC-0190](../../incidents/INC-0190-fast-stayed-green-while-a-command-adapter-fixture-missed-a-n.md) - FAST stayed green while a command-adapter fixture missed a new execution project
- occurrences 1, severity medium, status fixed
- **Signature:** Only the FULL path caught the missing project.
- **Rule:** Update every command-adapter fixture when an execution project is added, and do not trust FAST alone

### [INC-0208](../../incidents/INC-0208-two-rows-were-green-alone-and-red-together.md) - Two rows were green alone and red together
- occurrences 1, severity medium, status fixed
- **Signature:** The combination failed and neither branch did.
- **Rule:** Rehearse the merged stack, not the branches

### [INC-0214](../../incidents/INC-0214-a-helper-was-fixed-and-a-caller-still-passed-a-literal-empty.md) - A helper was fixed and a caller still passed a literal empty object
- occurrences 1, severity medium, status fixed
- **Signature:** The helper fix left a caller broken.
- **Rule:** Check every caller of a fixed helper with a strict destination compile

### [INC-0284](../../incidents/INC-0284-a-gate-result-counts-only-at-a-revision-the-gate-can-fetch-a.md) - A gate result counts only at a revision the gate can fetch and that holds its fix
- occurrences 1, severity medium, status fixed
- **Signature:** A gate passed at a revision that did not yet hold the fix it depended on.
- **Rule:** A gate run counts only at a revision the gate's clone can fetch and that already contains the fix the gate depends on

### [INC-0344](../../incidents/INC-0344-focused-runs-after-a-refactor-hid-static-check-residue-until.md) - Focused runs after a refactor hid static-check residue until the first canonical run
- occurrences 1, severity medium, status fixed
- **Signature:** Many commits were verified with focused runs, and the first canonical runs failed at lint and a hygiene check before any suite ran.
- **Rule:** After a refactor, run the canonical gate once, static steps included, before more focused work; focused runs skip lint, typecheck and hygiene checks

### [INC-0421](../../incidents/INC-0421-a-closure-packet-freeze-test-turned-positive-on-a-control-on.md) - A closure packet freeze test turned positive on a control-only landing and the lead admitted it narrowly
- occurrences 1, severity low, status fixed
- **Signature:** A freeze test reported a change that the guarded run could not read.
- **Rule:** Admit a freeze-test hit only narrowly: name the landing, why the run cannot read it, and the change that makes it a new STOP; never waive the identity step

### [INC-0474](../../incidents/INC-0474-a-whitespace-check-over-the-branch-range-failed-on-generated.md) - A whitespace check over the branch range failed on generated SQL, while the same check on the working tree alone had passed
- occurrences 1, severity low, status fixed
- **Signature:** A worktree only check passed where the branch range check failed.
- **Rule:** A worktree only whitespace check is not range proof; run the check over the branch range, exclude generator output by path, never reformat it, and keep every other path clean.
