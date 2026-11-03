---
id: INC-0536
title: A one-line comment conflict hid a type break from the automatic part of the merge
date: 2026-11-02
classes: [spec-and-scope]
severity: low
status: mitigated
---

# INC-0536 - A one-line comment conflict hid a type break from the automatic part of the merge

**Cost:** No loss. The tester stopped at the conflict, and the merged tree was never committed with the break.

## Signature - how you recognise it

A merge conflict looks like one stale comment, while the automatically merged lines of the same file are inconsistent with each other.

## What happened

A branch merge stopped on a conflict in a seed file that was a single stale comment. The side that merged automatically had also switched an import to a new helper, while a call further down still used the old one, so the merged tree would not have passed the type check. The tester stopped instead of resolving it and reported to the lead, who assigned the resolution to the engineer who owned the code, with no test edits and a stated rule for how the new data is counted.

## Root cause

The conflict markers showed only the textual overlap, not the semantic interaction between the two sides.

## Why it was hard to see

A small conflict invites a quick fix, and the type break appears only after the merge is complete.

## Fix

Stop at the conflict, report both sides, and let the code owner resolve it, then run the type check on the merged tree.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> After any merge conflict, inspect the whole merged file for changes the tool resolved automatically and run the type check before accepting; a tester does not resolve product conflicts.

## Related

[INC-0535](./INC-0535-a-standing-promise-to-guard-every-proven-behavior-had-no-inv.md)
