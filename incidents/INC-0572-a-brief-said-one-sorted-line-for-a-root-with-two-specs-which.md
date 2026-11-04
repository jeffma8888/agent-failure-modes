---
id: INC-0572
title: A brief said one sorted line for a root with two specs, which could be read two ways
date: 2026-11-04
classes: [spec-and-scope]
severity: low
status: mitigated
---

# INC-0572 - A brief said one sorted line for a root with two specs, which could be read two ways

**Cost:** None. The ambiguity was resolved by a ruling.

## Signature - how you recognise it

A count in a brief does not say what it counts.

## What happened

The brief for a root activation said one sorted line in the device map, but the root has two browser specs, and the map header says one line per browser spec. The lead ruled that the root gets two lines, one per spec, and that the brief meant one per destination.

## Root cause

The count was stated without its unit.

## Why it was hard to see

The literal reading and the map header disagree.

## Fix

State the unit of a count, and ask when the brief and the file header disagree.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> When a brief and a file header disagree on a count, ask for the unit before editing.

## Related

[INC-0540](./INC-0540-a-successor-root-needed-to-change-a-file-owned-by-another-ro.md)
