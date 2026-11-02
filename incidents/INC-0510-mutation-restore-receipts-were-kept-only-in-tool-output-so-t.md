---
id: INC-0510
title: Mutation restore receipts were kept only in tool output, so two independent reviewers could not verify restoration
date: 2026-11-02
classes: [observability]
severity: low
status: mitigated
---

# INC-0510 - Mutation restore receipts were kept only in tool output, so two independent reviewers could not verify restoration

**Cost:** Two reviews held on the same gap until a ruling accepted the shipped-bytes evidence instead; no mutation rerun.

## Signature - how you recognise it

A reviewer asks for proof that a mutated file was restored, and the only record is output that was not saved.

## What happened

For two slices the restore receipts of the mutation runs existed only as tool output, with no file kept, and two reviewers held on the same gap. The gap was accepted because the retained logs showed distinct assertion failures, and each reviewer had matched the shipped file to the committed blob and seen a passing run on it. From then on every mutant writes a file with its diff and the hash after restore before the scratch copy is deleted.

## Root cause

Restoration was treated as a step to perform, not as a fact to leave evidence of.

## Why it was hard to see

The mutation itself leaves logs, so the work looks documented, and the missing piece is the proof of the undo.

## Fix

Persist one receipt per mutant, the diff and the hash after restore, as a file before the scratch copy is deleted.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A mutation run keeps a receipt per mutant, the diff and the hash after restore, as a file before the scratch copy is deleted; tool output is not evidence a second reviewer can check.

## Related

[INC-0476](./INC-0476-unit-mutation-testing-on-a-merged-change-found-two-survivors.md) [INC-0126](./INC-0126-test-discovery-was-compared-with-an-absolute-scratch-prefix.md)
