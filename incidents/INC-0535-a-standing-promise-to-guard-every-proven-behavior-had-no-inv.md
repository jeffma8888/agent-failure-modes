---
id: INC-0535
title: A standing promise to guard every proven behavior had no inventory, so partial protection could pass as coverage
date: 2026-11-02
classes: [spec-and-scope]
severity: low
status: mitigated
---

# INC-0535 - A standing promise to guard every proven behavior had no inventory, so partial protection could pass as coverage

**Cost:** No loss. Without the inventory the share of walked behaviors with an automated guard was unknown, and gaps had no owner.

## Signature - how you recognise it

A broad request such as never break what already works is acknowledged but never turned into a per-item count of what is guarded.

## What happened

The standing request was that every behavior a manual walk proves gets an automated guard. A reviewer turned it into a static map with one line per checklist row. Each line recorded whether the guard was active in a collected test path, approved but pending, under review, blocked on a reviewed defect, or missing. Of 46 lines, 9 were active, 1 approved, 4 under review, 8 blocked and 24 had none. Each gap got a proposed root, grouped into 20 proposals. Active meant a matching assertion existed, not that a mutation had been shown to kill it, and a row with an essential uncovered behavior counted as missing even if partial protection existed.

## Root cause

The request was a principle with no measure, so each new test looked like progress while the uncovered share stayed invisible.

## Why it was hard to see

Partial guards make a row look protected, and without a count nobody can say how much of the walk is unguarded.

## Fix

Build the inventory with strict status definitions, count each status, and attach a proposed owner and root to every gap.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Turn a broad protection promise into a per-item inventory with strict status definitions, a count, and a proposed guard for every gap; partial protection of a row is a gap.

## Related

[INC-0524](./INC-0524-a-root-named-a-mutation-its-assertions-could-not-see-because.md)
