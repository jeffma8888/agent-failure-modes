---
id: INC-0634
title: A record naming a commit id was written in the same parallel batch as the call that creates the commit, so a plausible id was written instead of the real one
date: 2026-11-08
classes: [false-green]
severity: low
status: mitigated
topic: false-green/proxy-artifact-cited-as-evidence
occurrences: 1
---

# INC-0634 - A record naming a commit id was written in the same parallel batch as the call that creates the commit, so a plausible id was written instead of the real one

**Catalog:** [root](../catalog/README.md) / [false-green](../catalog/false-green/README.md) / [An artifact that looks like evidence was cited but proves no fact](../catalog/false-green/proxy-artifact-cited-as-evidence.md)

**Cost:** One record carried a wrong commit id for about a minute, until the landing output was read and the line fixed.

## Signature - how you recognise it

A recorded commit id does not exist in the repository.

## What happened

A lead ran two tool calls in one parallel batch: the landing of a review, which creates a commit, and the ledger write that records that landing. The ledger line had to name the new commit, which did not exist when the line was composed, so a plausible id was written instead of the real one. The slip was caught from the landing output a minute later and fixed with an anchored replace that asserted the old text appeared once and the new text once.

## Root cause

A record was composed in the same batch as the call that produces the value it names.

## Why it was hard to see

A plausible id reads as correct, and the batch gave no point at which the real value was available.

## Fix

Write the record after the producing call returns and copy the value from its output; fix a wrong line with a replace that asserts the old text once and the new text once.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Never record a value produced by a call in the same parallel batch as that call; write the record after the call returns and copy the value from its output. A record that must name an output waits one turn.

## Related

[INC-0611](./INC-0611-a-time-label-was-written-in-the-same-script-that-read-the-cl.md) [INC-0623](./INC-0623-a-helper-piped-to-tail-and-followed-by-ran-the-next-step-alt.md)
