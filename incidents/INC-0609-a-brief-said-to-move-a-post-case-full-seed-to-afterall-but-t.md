---
id: INC-0609
title: A brief said to move a post-case full seed to afterAll, but the seed is find-or-create, so a seed without a reset first does not restore the baseline
date: 2026-11-04
classes: [spec-and-scope]
severity: medium
status: mitigated
---

# INC-0609 - A brief said to move a post-case full seed to afterAll, but the seed is find-or-create, so a seed without a reset first does not restore the baseline

**Cost:** One author's matrix was admitted on the old bytes and could be credited for those bytes only; the candidate needed a revision and a fresh matrix.

## Signature - how you recognise it

A cleanup hook that only seeds leaves earlier rows in place.

## What happened

A successor brief said to move the post-case full seed to a once-per-file hook. The seed is find-or-create, so seeding without a reset first does not restore the baseline. The review requirement, that the file-level hook body equal the per-case hook body exactly (reset, then full seed, under the same guard), was newer than the brief's move-only wording, so this was a brief change, not an author defect. The matrix already running on the old bytes was not stopped and counts as evidence for those bytes only. Two other authors applied the requirement before admission.

## Root cause

The brief described the move in words and did not state the exact hook body.

## Why it was hard to see

A find-or-create seed on a dirty database looks like a restore, and the old bytes passed their own pairs.

## Fix

State the exact body in the brief (reset, then seed, under the same guard), keep any run on old bytes credited to those bytes only, and test first with a check that fails on the old bytes.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> When a brief moves a cleanup, state the exact body to run; a seed that is find-or-create without a reset first does not restore a baseline.

## Related

[INC-0594](./INC-0594-a-successor-draft-named-as-its-old-bytes-a-revision-that-was.md) [INC-0538](./INC-0538-a-dispatch-draft-marked-every-unsourced-value-for-the-lead-t.md)
