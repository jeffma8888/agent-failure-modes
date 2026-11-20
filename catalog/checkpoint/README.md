# checkpoint

[Catalog](../README.md) / checkpoint

An all-or-nothing step loses everything when it is interrupted, because it writes its output only at the end instead of writing a minimal-but-complete artifact first and refining in place.

**Ask:** If this step is killed at minute 8 of 10, does a usable artifact already exist on disk?

**You are probably here if:** An interruption or later edit loses usable output or evidence, or completed work remains blocked, unrecorded, or unpublished.

17 incidents filed here (17 occurrences); 15 more filed elsewhere are also tagged checkpoint.

## Incidents

This class has no topics, so this node is the leaf. Ordered by occurrences, then severity, then id.

### [INC-0006](../../incidents/INC-0006-checkpoint-first-a-killed-step-that-already-wrote-its-output.md) - Checkpoint-first: a killed step that already wrote its output still counts
- occurrences 1, severity medium, status fixed
- **Signature:** An attempt log is 48 bytes ('timed out after 600s') and the loop treats the iteration as a success anyway - because the OUTPUT FILE exists.
- **Rule:** Success is an ARTIFACT, not an exit code. Under a hard timeout, an agent that writes its minimal complete output first and refines in place still succeeds if killed. Correspondingly: never call a timeout a failure without checking whether the output file exists.

### [INC-0160](../../incidents/INC-0160-an-activation-was-tied-to-an-unreviewed-successor-and-had-to.md) - An activation was tied to an unreviewed successor and had to be re-ruled
- occurrences 1, severity medium, status fixed
- **Signature:** A shipped revision waited on a later revision that had not been reviewed.
- **Rule:** Do not tie the activation of a reviewed revision to an unreviewed successor.

### [INC-0258](../../incidents/INC-0258-a-failed-closing-run-could-leave-a-signed-record-public.md) - A failed closing run could leave a signed record public
- occurrences 1, severity medium, status fixed
- **Signature:** Publishing came before the closing check.
- **Rule:** Run the exact-closing checks on a local closing record before merging and uploading it

### [INC-0268](../../incidents/INC-0268-keep-a-canary-and-a-mid-stage-stop-rehearsal-in-separate-win.md) - Keep a canary and a mid-stage STOP rehearsal in separate windows
- occurrences 1, severity medium, status fixed
- **Signature:** A rehearsal planned inside a canary could have destroyed the canary evidence.
- **Rule:** Do not host a destructive rehearsal inside the run that produces the evidence

### [INC-0293](../../incidents/INC-0293-the-before-state-was-not-preserved-before-an-operator-edit.md) - The before-state was not preserved before an operator edit
- occurrences 1, severity medium, status fixed
- **Signature:** A later snapshot could not recreate the state from before an operator edit.
- **Rule:** Preserve before-state bytes before an operator edit; a later snapshot cannot recreate them

### [INC-0349](../../incidents/INC-0349-a-revision-was-overwritten-in-place-and-its-recorded-digest.md) - A revision was overwritten in place and its recorded digest named bytes that no longer existed
- occurrences 1, severity medium, status fixed
- **Signature:** A rechecker could not run the new tests against the prior revision because only its size and digest survived.
- **Rule:** A digest proves which bytes you meant, not that you can still run them; keep every reviewed revision's bytes until the fix lands

### [INC-0605](../../incidents/INC-0605-corpus-commits-sat-unpushed-after-the-gate-and-a-push-was-an.md) - Corpus commits sat unpushed after the gate, and a push was answered with a server error, so the remote head must be read back after every push
- occurrences 1, severity medium, status mitigated
- **Signature:** Local commits exist after a passed gate and the remote head is older.
- **Rule:** After every push, read the remote head back with ls-remote and compare it with the local head; do not call a gate-passed commit published until they match.

### [INC-0375](../../incidents/INC-0375-an-engineer-overwrote-its-own-unit-ledger-with-a-later-run.md) - An engineer overwrote its own unit ledger with a later run
- occurrences 1, severity low, status fixed
- **Signature:** A ledger file held only the latest run after an engineer wrote a new run over it.
- **Rule:** Keep a ledger append-only with a dated section per run; never overwrite it with a later run

### [INC-0377](../../incidents/INC-0377-a-draft-test-root-was-revised-in-place-after-review-marker-o.md) - A draft test root was revised in place after review, marker or activation
- occurrences 1, severity low, status fixed
- **Signature:** A root that others had reviewed or marked could be edited in place.
- **Rule:** Revise a draft test root in place only while it has no review, marker or activation; after that only a successor

### [INC-0402](../../incidents/INC-0402-an-author-who-received-a-ruling-mid-run-superseded-its-own-e.md) - An author who received a ruling mid-run superseded its own earlier status with a dated addendum without rewriting the historical bytes
- occurrences 1, severity low, status fixed
- **Signature:** A status written before a ruling needed to change after it.
- **Rule:** When a ruling changes a status, append a dated addendum that supersedes it; never rewrite the historical bytes

### [INC-0432](../../incidents/INC-0432-hand-delivery-under-a-hold-with-one-reconciliation-after-the.md) - Hand delivery under a hold, with one reconciliation after the load, replaced blocking on a state flip
- occurrences 1, severity low, status fixed
- **Signature:** Three rows waited on a backlog state flip that was held on purpose.
- **Rule:** Under a held state flip, deliver by hand on the established precedent and reconcile once after the hold; keep every freeze rule

### [INC-0443](../../incidents/INC-0443-a-self-imposed-freeze-outlived-its-reason-and-was-blocking-t.md) - A self-imposed freeze outlived its reason and was blocking three rows' activations
- occurrences 1, severity low, status fixed
- **Signature:** A STOP kept blocking work after the run it protected could no longer be affected.
- **Rule:** Re-derive a freeze's mechanism before honoring it; withdraw it when the guarded run cannot read what it protects

### [INC-0468](../../incidents/INC-0468-a-helper-finished-its-work-but-hung-in-the-framework-shutdow.md) - A helper finished its work but hung in the framework shutdown call, and its pass line came after the shutdown, so no evidence printed
- occurrences 1, severity low, status fixed
- **Signature:** A step did its work and then sat idle with no output.
- **Rule:** Write the evidence line before any shutdown call, bound the shutdown with a timeout, and exit explicitly

### [INC-0516](../../incidents/INC-0516-backlog-rows-stayed-open-after-their-fixes-merged-so-the-bac.md) - Backlog rows stayed open after their fixes merged, so the backlog no longer showed what was done
- occurrences 1, severity low, status mitigated
- **Signature:** The backlog lists as open rows whose fixes are already on the main line.
- **Rule:** Update a backlog row status with the merge commit at the time its fix merges, so the backlog stays the record of what is done.

### [INC-0531](../../incidents/INC-0531-a-graceful-pause-worked-because-each-in-flight-teammate-fini.md) - A graceful pause worked because each in-flight teammate finished one step, wrote a checkpoint and left its workspace as it was
- occurrences 1, severity low, status mitigated
- **Signature:** A team stops on request and resumes later, and every member continues from its own recorded state.
- **Rule:** To pause a team safely, tell each in-flight teammate to finish only the current step, write a resume checkpoint, and leave its worktree and processes as they are; resume from those checkpoints and never redo finished work.

### [INC-0592](../../incidents/INC-0592-a-static-triage-found-four-open-rows-already-done-by-named-m.md) - A static triage found four open rows already done by named merges, and the freeze rule kept them open with the merge commit in the status text
- occurrences 1, severity low, status mitigated
- **Signature:** Plan rows read as open although merged work already delivered them.
- **Rule:** When a freeze keeps a finished row open, record the delivering merge commit in its status text.

### [INC-0598](../../incidents/INC-0598-a-go-decision-was-tied-to-a-stale-commit-that-later-rulings.md) - A go decision was tied to a stale commit that later rulings had overtaken, and the ruling moved it to a named condition
- occurrences 1, severity low, status mitigated
- **Signature:** A go packet names a fixed commit that predates later rulings.
- **Rule:** Name a GO baseline by its condition, and recheck it against rulings made since the packet was written.

## Also tagged checkpoint

15 incidents filed under another home class also carry this class. Listed by the node where they live:

- [identity-and-keying/approval-names-wrong-commit](../identity-and-keying/approval-names-wrong-commit.md): INC-0164, INC-0175, INC-0261
- [stage-timeout/work-outgrows-enforced-timeouts](../stage-timeout/work-outgrows-enforced-timeouts.md): INC-0002, INC-0025
- [tooling-paths/chain-ran-on-after-failure](../tooling-paths/chain-ran-on-after-failure.md): INC-0050, INC-0294
- [delegation/stalled-behind-one-owner-or-decision](../delegation/stalled-behind-one-owner-or-decision.md): INC-0277
- [detector-fail-closed](../detector-fail-closed/README.md): INC-0034
- [false-green/verified-a-different-target](../false-green/verified-a-different-target.md): INC-0284
- [identity-and-keying](../identity-and-keying/README.md): INC-0341
- [identity-and-keying/replacement-record-malformed](../identity-and-keying/replacement-record-malformed.md): INC-0279
- [observability/missing-or-unverifiable-receipts](../observability/missing-or-unverifiable-receipts.md): INC-0254
- [spec-and-scope/records-drift-or-lose-provenance](../spec-and-scope/records-drift-or-lose-provenance.md): INC-0338
- [vcs-destruction](../vcs-destruction/README.md): INC-0281
