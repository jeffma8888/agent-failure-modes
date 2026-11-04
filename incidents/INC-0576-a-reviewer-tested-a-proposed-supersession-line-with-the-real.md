---
id: INC-0576
title: A reviewer tested a proposed supersession line with the real checker and found it in the wrong form for an already active predecessor
date: 2026-11-04
classes: [spec-and-scope]
severity: low
status: mitigated
---

# INC-0576 - A reviewer tested a proposed supersession line with the real checker and found it in the wrong form for an already active predecessor

**Cost:** None. The author used the form that matches the predecessor state before activation.

## Signature - how you recognise it

A replacement marker is written in the form for a pending predecessor when the predecessor is already active.

## What happened

A reviewer ran the identity checker on a proposed replacement marker and found that a successor over an active predecessor must use the active-path form: the old active path, the old hash and the same active path, because the predecessor pending payload is gone. The pending-to-pending form fails with a missing unlisted deletion. The lead confirmed it with the checker, and the rule is that authors propose the form that matches the predecessor state.

## Root cause

The form depends on the state of the predecessor, which the author did not check.

## Why it was hard to see

Both forms look valid until the checker runs.

## Fix

Run the real checker on the proposed line and pick the form that matches the predecessor state.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Test a proposed replacement marker with the real checker, and use the form that matches the predecessor state.

## Related

[INC-0540](./INC-0540-a-successor-root-needed-to-change-a-file-owned-by-another-ro.md)
