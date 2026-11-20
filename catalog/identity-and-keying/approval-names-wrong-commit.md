# An approval or activation names the wrong commit or line of history

[Catalog](../README.md) / [identity-and-keying](README.md) / approval-names-wrong-commit

**Go here if:** A gate tying a revision to its approval refuses or wrongly passes: the named commit is not an ancestor, predates what it approves, is HEAD mid-merge, precedes review; a merge leaves activation due.

**Rule:** Name the commit that actually holds what you assert, the first main commit holding both the review and the reviewed bytes, and judge ancestry on current main: merge main into the branch first, land bytes before the record approving them, write a marker only after its review, carry every activation a merge makes due, and run the identity check on the exact merged tree after each landing and merge.

9 incidents, 9 occurrences. Ordered by occurrences, then severity, then id.

## Incidents

### [INC-0261](../../incidents/INC-0261-a-landed-root-revision-cannot-carry-its-supersession-file-in.md) - A landed root revision cannot carry its supersession file in the same commit
- occurrences 2, severity medium, status fixed
- **Signature:** A supersession file was planned in the same commit as the root it approves.
- **Rule:** Land a root revision first and add its supersession file after the non-author re-check
- **Recurrences:**
  - [INC-0595](../../incidents/INC-0595-an-approval-header-named-the-review-commit-whose-tree-did-no.md) - 2026-11-04 - An approval header named the review commit, whose tree did not yet hold the reviewed root, and the identity checker refused it

### [INC-0164](../../incidents/INC-0164-a-reverted-and-re-landed-qa-revision-got-its-marker-approved.md) - A reverted and re-landed QA revision got its marker approved at the wrong commit
- occurrences 1, severity medium, status fixed
- **Signature:** The identity checker compared old active bytes at the approved commit.
- **Rule:** When a reverted revision is re-landed after an older copy became active, approve its marker at the re-land commit.

### [INC-0175](../../incidents/INC-0175-a-merge-of-main-left-an-activation-due-and-went-red.md) - A merge of main left an activation due and went red
- occurrences 1, severity medium, status fixed
- **Signature:** The merge commit was red on its own.
- **Rule:** A merge of main carries every activation its new markers make due.

### [INC-0204](../../incidents/INC-0204-a-precommit-check-reported-a-merge-brought-approval-as-unrea.md) - A precommit check reported a merge-brought approval as unreachable
- occurrences 1, severity medium, status fixed
- **Signature:** The check read the wrong commit.
- **Rule:** Judge reachability on the committed merge, not on the precommit state

### [INC-0240](../../incidents/INC-0240-an-auto-merge-of-a-helper-could-lose-an-activation-or-covera.md) - An auto-merge of a helper could lose an activation or coverage unnoticed
- occurrences 1, severity medium, status fixed
- **Signature:** The bytes were right and a project could still drop out.
- **Rule:** Prove an auto-merge by an ordered two-parent history check and an exact-run project inventory

### [INC-0513](../../incidents/INC-0513-an-activation-moved-a-superseded-root-s-spec-while-main-carr.md) - An activation moved a superseded root's spec while main carried the approved successor edge, and identity failed only after the merge
- occurrences 1, severity medium, status mitigated
- **Signature:** An identity check reports a missing deletion of a pending copy after a branch merges a main that supersedes the activated revision.
- **Rule:** Before activating a root, confirm on current main that it is still the terminal of its supersession chain; run the identity check after merging main into the branch, not only before.

### [INC-0397](../../incidents/INC-0397-a-pending-root-whose-supersession-line-said-review-pending-f.md) - A pending root whose supersession line said review pending failed the identity checker at landing
- occurrences 1, severity low, status fixed
- **Signature:** The identity checker rejected a landing whose marker line said approval was pending.
- **Rule:** Land a pending successor without its marker; write the marker only after the review

### [INC-0486](../../incidents/INC-0486-an-approval-on-main-was-not-an-ancestor-of-the-branch-that-n.md) - An approval on main was not an ancestor of the branch that needed it
- occurrences 1, severity low, status mitigated
- **Signature:** A checker required the approval commit to be an ancestor of the branch head, and the branch had forked before the approval landed.
- **Rule:** An approval that landed on main after a branch forked is not an ancestor of that branch; merge main into the branch before any activation commit that a checker ties to that approval.
