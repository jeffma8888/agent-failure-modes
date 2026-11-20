# vcs-destruction

[Catalog](../README.md) / vcs-destruction

Version control is used as a weapon against the working tree: a blanket stage sweeps in unrelated edits, a revert-to-remote discards uncommitted work, or identity leaks into history.

**Ask:** Whose uncommitted work is in this tree, and what does a failure-path reset or a blanket 'add all' do to it?

21 incidents filed here (21 occurrences); 9 more filed elsewhere are also tagged vcs-destruction.

## Incidents

This class has no topics, so this node is the leaf. Ordered by occurrences, then severity, then id.

### [INC-0014](../../incidents/INC-0014-a-revert-on-failure-loop-destroys-uncommitted-human-work-in.md) - A revert-on-failure loop destroys uncommitted human work in a shared tree
- occurrences 1, severity critical, status mitigated
- **Signature:** A loop is enabled that commits from a working directory where another writer has uncommitted changes. The loop's failure path is a full reset to the remote head.
- **Rule:** A loop's revert-to-remote cannot distinguish loop dirt from human work-in-progress. Guard shared trees with a per-team STOP sentinel that names owner, files at risk, lift condition and whether restart is needed. Sentinels are polled every round; the enabled flag needs a restart. Verify the lift condition in the SAME command that removes it.

### [INC-0015](../../incidents/INC-0015-git-identity-leak-real-name-via-ambient-global-config.md) - Git identity leak: real name via ambient global config
- occurrences 1, severity critical, status fixed
- **Signature:** `git log --all --format='%an <%ae>'` on any repo shows an identity string you did not consciously set for THAT repo.
- **Rule:** For any repo destined to be public, set BOTH repo-local `user.name` AND `user.email` (to a public handle and id-anchored noreply) BEFORE the first commit. Verify with `git log --all --format='%an <%ae>'`. A noreply email alone does not stop the ambient global name from leaking. An `includeIf` gitdir must be the REAL path, not a symlink.

### [INC-0012](../../incidents/INC-0012-a-loop-s-git-add-a-sweeps-a-human-s-uncommitted-edits-into-a.md) - A loop's `git add -A` sweeps a human's uncommitted edits into a loop commit
- occurrences 1, severity high, status mitigated
- **Signature:** `git log --oneline -S "<a phrase you typed>" -- <file>` shows your text landed in a commit whose SUBJECT is the loop's story.
- **Rule:** In a multi-writer tree, never use `git add -A` or `git commit -a`; name paths on the commit itself and check its stat before moving on. A path-limited commit cannot protect your edits from another writer's blanket stage, so quiesce live loops before editing their tree. Undo an over-broad commit only while it is still HEAD and without changing working-tree bytes.

### [INC-0013](../../incidents/INC-0013-add-then-commit-is-a-shared-index-race-use-a-path-limited-co.md) - add-then-commit is a shared-index race; use a path-limited commit
- occurrences 1, severity high, status fixed
- **Signature:** You ran `git add <paths>` followed by a separate `git commit` and the resulting commit contains files you never touched. Diff against your parent shows the loop's whole iteration.
- **Rule:** The git index is process-shared: a pathless commit takes whatever is staged at that instant, not what you staged. For any out-of-band write to a repo another writer touches: name the paths on the commit itself (`git commit -m 'msg' -- <paths>`) rather than doing add-then-commit. Do not force-push while the loop is live.

### [INC-0044](../../incidents/INC-0044-pushing-a-local-repository-to-a-new-remote-publishes-its-who.md) - Pushing a local repository to a new remote publishes its whole history, not its current tree
- occurrences 1, severity high, status fixed
- **Signature:** A repository is about to be pushed for the first time, the plan is stated in terms of which files to exclude, and nobody has listed the paths that were EVER tracked.
- **Rule:** Pushing an existing repository publishes its HISTORY. Before the first push audit every path ever tracked, every blob version and every commit message, never only the tree, and install a pre-push guard that scans the pushed range. Excluding a file from the tree does not remove it from history.

### [INC-0045](../../incidents/INC-0045-disabling-a-loop-s-push-while-its-failure-path-resets-to-the.md) - Disabling a loop's push while its failure path resets to the remote erases shipped work
- occurrences 1, severity high, status fixed
- **Signature:** A proposal simplifies a pipeline by turning off its publish step, while the rollback path of the same pipeline hard-resets to the published state and never fetches.
- **Rule:** Before turning off a pipeline's publish or push step, find what its rollback resets TO. If rollback targets the published state, publishing is part of the durability contract, not an optional gate.

### [INC-0065](../../incidents/INC-0065-a-graceful-stop-flag-checked-before-every-stage-would-have-d.md) - A 'graceful' stop flag checked before every stage would have discarded the in-flight iteration's finished work
- occurrences 1, severity high, status fixed
- **Signature:** A stop sentinel is meant to drain a loop between iterations, but nobody has checked where in the loop it is read.
- **Rule:** Before using a stop flag to drain a loop, read every place it is checked, and set it only after the last check that would discard work.

### [INC-0101](../../incidents/INC-0101-a-later-row-overwrote-a-file-that-was-already-active.md) - A later row overwrote a file that was already active
- occurrences 1, severity medium, status fixed
- **Signature:** Part of a file must activate later, and activating it replaces the active file.
- **Rule:** Active files are append-only; later parts get new destinations.

### [INC-0103](../../incidents/INC-0103-a-teammate-could-not-run-a-destructive-git-command-even-when.md) - A teammate could not run a destructive git command even when the lead instructed it
- occurrences 1, severity medium, status fixed
- **Signature:** A lead instructs a teammate to run a reset or similar, and the permission ceiling refuses it.
- **Rule:** Plan destructive operations for the context that holds the permission.

### [INC-0114](../../incidents/INC-0114-a-second-clone-named-after-the-remote-held-a-stale-tip-and-w.md) - A second clone named after the remote held a stale tip and was mistaken for the working checkout
- occurrences 1, severity medium, status fixed
- **Signature:** Two checkouts exist, and the folder name suggests the wrong one is current.
- **Rule:** Never identify a checkout by its folder name.

### [INC-0162](../../incidents/INC-0162-a-chained-amend-reworded-the-previous-commit-after-a-failed.md) - A chained amend reworded the previous commit after a failed revert
- occurrences 1, severity medium, status fixed
- **Signature:** A revert failed on an invalid flag and the next chained step changed the wrong commit.
- **Rule:** Chain an amend only with && after a step whose success is checked, and confirm the HEAD subject before amending.

### [INC-0185](../../incidents/INC-0185-rename-detection-reported-a-false-rename-in-a-merge.md) - Rename detection reported a false rename in a merge
- occurrences 1, severity medium, status fixed
- **Signature:** A merge showed a rename and delete that did not happen.
- **Rule:** Do not accept either side of a reported rename; confirm the blob against main.

### [INC-0226](../../incidents/INC-0226-a-hand-made-merge-could-differ-from-the-mechanical-merge-unn.md) - A hand-made merge could differ from the mechanical merge unnoticed
- occurrences 1, severity medium, status fixed
- **Signature:** The extra changes sat inside a large merge.
- **Rule:** Verify a hand-made merge against a mechanical merge of the same parents

### [INC-0229](../../incidents/INC-0229-a-commit-swept-another-session-uncommitted-entries.md) - A commit swept another session uncommitted entries
- occurrences 1, severity medium, status fixed
- **Signature:** Entries landed under a message about a different lesson.
- **Rule:** In a shared checkout, stage only your own paths and check the log for foreign commits before writing

### [INC-0281](../../incidents/INC-0281-confirm-the-landing-commit-contains-every-file-before-cleani.md) - Confirm the landing commit contains every file before cleaning the source
- occurrences 1, severity medium, status fixed
- **Signature:** A source was cleaned against a failed commit and its change was reverted.
- **Rule:** Confirm the landing commit contains every file before cleaning the source

### [INC-0309](../../incidents/INC-0309-a-helper-tool-s-argument-meaning-was-misread-by-its-own-auth.md) - A helper tool's argument meaning was misread by its own author
- occurrences 1, severity medium, status fixed
- **Signature:** A digest was passed where the clean step expected a commit, and a tracked file was deleted.
- **Rule:** Read a tool's usage line before a destructive mode, even your own tool; keep destructive steps in tools that verify the kind of each argument

### [INC-0380](../../incidents/INC-0380-a-landing-helper-s-clean-step-deleted-a-pending-root-directo.md) - A landing helper's clean step deleted a pending root directory and left an unchanged tracked file deleted after the fast-forward
- occurrences 1, severity medium, status fixed
- **Signature:** A tracked file that had not changed was gone after a landing.
- **Rule:** A clean step must not leave a tracked unchanged file deleted; restore tracked files after a fast-forward and check tree status

### [INC-0409](../../incidents/INC-0409-a-landing-helper-s-clean-step-fast-forwarded-a-merged-featur.md) - A landing helper's clean step fast-forwarded a merged feature branch's ref, which would have moved a live branch
- occurrences 1, severity medium, status fixed
- **Signature:** A clean step changed the ref of a branch that had already been merged, and it could have been one still in use.
- **Rule:** A clean step must never move a branch ref that is still under work

### [INC-0632](../../incidents/INC-0632-a-read-only-audit-ran-git-merge-tree-write-tree-in-a-protect.md) - A read-only audit ran git merge-tree --write-tree in a protected checkout; refs, index and worktree stayed clean while loose objects were written
- occurrences 1, severity medium, status mitigated
- **Signature:** A read-only task includes git merge-tree --write-tree (or another command that writes objects), and the only post-check is a clean status and an unchanged HEAD.
- **Rule:** Classify Git commands by all state they write, not clean status. Run object-writing analysis only in a newly isolated scratch clone. Protected-repository writes need separate explicit authorization; an inventory grants no permission and does not prove reversibility.

The 2 entries below are listed by title only so this node stays under 12 KB. Open the page, or run `python3 tools/afm.py show INC-XXXX`, for its signature and rule.

- [INC-0400](../../incidents/INC-0400-an-activation-instruction-to-delete-superseded-pending-copie.md) - An activation instruction to delete superseded pending copies had nothing to delete because an earlier pure rename had already moved them (n=1, low)
- [INC-0436](../../incidents/INC-0436-a-squash-recipe-equated-the-landing-tree-with-a-stale-branch.md) - A squash recipe equated the landing tree with a stale branch tree and would have dropped later main work (n=1, low)

## Also tagged vcs-destruction

9 incidents filed under another home class also carry this class. Listed by the node where they live:

- [tooling-paths](../tooling-paths/README.md): INC-0024, INC-0030, INC-0046, INC-0357, INC-0362
- [checkpoint](../checkpoint/README.md): INC-0293
- [concurrency](../concurrency/README.md): INC-0324
- [detector-fail-open](../detector-fail-open/README.md): INC-0215
- [false-green](../false-green/README.md): INC-0295

## Practices touching this class

- [PRA-0001](../CORE.md#practices) - The enforcement ladder: pick the cheapest rung that makes the failure impossible
- [PRA-0004](../CORE.md#practices) - Choose the constraint surface before choosing the enforcement strength
