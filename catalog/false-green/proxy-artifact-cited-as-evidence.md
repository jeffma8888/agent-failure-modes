# An artifact that looks like evidence was cited but proves no fact

[Catalog](../README.md) / [false-green](README.md) / proxy-artifact-cited-as-evidence

**Go here if:** A record cites a manifest, render, approval, ancestry, rename display or static PASS as proof, or names a commit id or value that was never copied from tool output.

**Rule:** Cite only evidence that directly establishes the claimed fact: open the artifact and check it holds what it claims (digests, bodies, byte equality, a runtime result), retain it, and copy every id or value verbatim from the output of the call that produced it, after that call has returned.

9 incidents, 9 occurrences. Ordered by occurrences, then severity, then id.

## Incidents

### [INC-0228](../../incidents/INC-0228-a-digest-manifest-without-digests-was-cited-as-evidence.md) - A digest manifest without digests was cited as evidence
- occurrences 1, severity medium, status fixed
- **Signature:** The manifest looked complete and held no digests.
- **Rule:** Check that a manifest has one digest per line before citing it

### [INC-0232](../../incidents/INC-0232-a-prompt-render-succeeded-without-reading-the-card-bodies.md) - A prompt render succeeded without reading the card bodies
- occurrences 1, severity medium, status fixed
- **Signature:** The render referenced the cards by path only.
- **Rule:** Verify external card bytes separately from a successful prompt render

### [INC-0233](../../incidents/INC-0233-approval-of-role-cards-in-prose-was-at-risk-of-standing-in-f.md) - Approval of role cards in prose was at risk of standing in for a runtime check
- occurrences 1, severity medium, status fixed
- **Signature:** No run backed the approval.
- **Rule:** Run the planted-dispute rehearsal and the incomplete-verdict dry run at the exit commit; prose approval is not runtime evidence

### [INC-0247](../../incidents/INC-0247-ancestry-was-at-risk-of-standing-in-for-a-clean-tree-or-a-ch.md) - Ancestry was at risk of standing in for a clean tree or a checker run
- occurrences 1, severity medium, status fixed
- **Signature:** The commit was there and the facts were not proved.
- **Rule:** Do not use ancestry as evidence of a clean tree, a checker run or bracketing observations

### [INC-0295](../../incidents/INC-0295-a-pure-move-onto-an-existing-path-was-read-from-the-diff-s-r.md) - A pure move onto an existing path was read from the diff's rename display
- occurrences 1, severity medium, status fixed
- **Signature:** A move showed as modify plus delete, so the diff could not confirm it.
- **Rule:** Prove a move by byte equality and digests, not by the rename display

### [INC-0315](../../incidents/INC-0315-a-static-checker-s-pass-was-read-as-acceptance-without-an-an.md) - A static checker's PASS was read as acceptance without an anchored baseline
- occurrences 1, severity medium, status fixed
- **Signature:** An identity PASS appeared with no recorded hash behind the supplied baseline.
- **Rule:** A static tool's PASS is labeled as static and anchored to recorded hashes; it never stands in for runtime or acceptance

### [INC-0408](../../incidents/INC-0408-an-evidence-gap-a-temporary-config-not-retained-was-closed-b.md) - An evidence gap, a temporary config not retained, was closed by a lead re-run that kept it, not by asking the author to reconstruct it
- occurrences 1, severity low, status fixed
- **Signature:** A run's evidence omitted a temporary config that had been deleted.
- **Rule:** Close an evidence gap by a re-run that keeps and records the artifact, not by a reconstruction

### [INC-0634](../../incidents/INC-0634-a-record-naming-a-commit-id-was-written-in-the-same-parallel.md) - A record naming a commit id was written in the same parallel batch as the call that creates the commit, so a plausible id was written instead of the real one
- occurrences 1, severity low, status mitigated
- **Signature:** A recorded commit id does not exist in the repository.
- **Rule:** Never record a value produced by a call in the same parallel batch as that call; write the record after the call returns and copy the value from its output. A record that must name an output waits one turn.

### [INC-0637](../../incidents/INC-0637-a-ledger-named-a-nonexistent-commit-after-a-short-sha-was-le.md) - A ledger named a nonexistent commit after a short SHA was lengthened by hand
- occurrences 1, severity low, status mitigated
- **Signature:** A recorded SHA has the tool-produced prefix but a hand-added suffix that does not match the real commit.
- **Rule:** Never lengthen, shorten or retype a SHA by hand; every SHA in a record is a verbatim copy of tool output at the length shown. For a different length, obtain that form from git before writing the record.
