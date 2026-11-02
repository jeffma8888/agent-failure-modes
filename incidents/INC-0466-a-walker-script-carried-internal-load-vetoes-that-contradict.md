---
id: INC-0466
title: A walker script carried internal load vetoes that contradicted a later ruling, and the runner rightly refused to edit the immutable bytes
date: 2026-11-02
classes: [spec-and-scope]
severity: low
status: fixed
---

# INC-0466 - A walker script carried internal load vetoes that contradicted a later ruling, and the runner rightly refused to edit the immutable bytes

**Cost:** A successor script and a rerun of one step.

## Signature - how you recognise it

A script stopped a run on a gate that a ruling had removed.

## What happened

a walker script held two internal load vetoes, a start gate and a browser start gate, that contradicted a later ruling to record load and not stop; they would have blocked the walker right after a build; the runner refused to edit bytes that were pinned as immutable, and the lead issued a successor script that prints a recorded only marker at both places and changes nothing else

## Root cause

the ruling changed the gate in text, and the gate also lived in script bytes

## Why it was hard to see

Nobody listed the places that encode a gate when the ruling was written.

## Fix

issue a successor with only the two lines changed, check it by a diff against the original and a syntax check, and keep the original unchanged

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> When a ruling changes a gate, list every script that encodes the old gate before the ruling is relied on

## Related

[INC-0390](./INC-0390-a-dispatch-packet-written-for-a-future-branch-went-stale-whe.md) [INC-0401](./INC-0401-a-dispatch-packet-called-a-root-absent-an-hour-after-it-had.md) [INC-0358](./INC-0358-a-restated-rule-gained-a-qualifier-the-original-ruling-never.md)
