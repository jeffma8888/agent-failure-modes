---
id: INC-0570
title: Two lead rulings narrated facts that git disagreed with, and the corrections were appended after checking git
date: 2026-11-04
classes: [observability]
severity: low
status: mitigated
---

# INC-0570 - Two lead rulings narrated facts that git disagreed with, and the corrections were appended after checking git

**Cost:** None. The corrections were appended and the conclusions were not affected.

## Signature - how you recognise it

A ruling states a branch base or a new file that the commit history contradicts.

## What happened

One ruling and an assignment said a branch was based on the main commit, while it was based on an earlier one named in an earlier assignment, and the merge-tree check still targeted main. Another ruling said a fix added a new unit file, while it extended an existing one by 18 lines, as the commit stat shows. Each correction was appended after checking git.

## Root cause

The facts were written from recollection of the plan, not read from git.

## Why it was hard to see

The narrative reads plausibly and is rarely checked.

## Fix

Check the base and the file list in git before stating them, and correct by an appended note.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Before stating a branch base or a new file in a ruling, read it from git; correct by an appended note.

## Related

[INC-0567](./INC-0567-heading-times-in-several-rulings-and-briefs-ran-thirty-to-se.md)
