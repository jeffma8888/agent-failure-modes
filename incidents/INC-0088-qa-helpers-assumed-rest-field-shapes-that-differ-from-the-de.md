---
id: INC-0088
title: QA helpers assumed REST field shapes that differ from the design, and integration files mutated shared state without restoring it
date: 2026-10-30
classes: [test-isolation, spec-and-scope]
severity: medium
status: fixed
---

# INC-0088 - QA helpers assumed REST field shapes that differ from the design, and integration files mutated shared state without restoring it

**Cost:** Minor: caught in review or by a stop rule before it shipped.

## Signature - how you recognise it

Helpers read fields in a shape the design does not use; a spec passes alone and fails after a file that left state changed.

## What happened

Localized text groups in the design did not match the shapes QA helpers read from REST responses, and integration files that mutated shared state did not restore it, breaking later specs that do not reseed.

## Root cause

Helpers were written from memory of the shape, and restoration was assumed rather than required.

## Why it was hard to see

Each file passes in isolation; the break appears only in file order.

## Fix

Check design field shapes against every REST read in QA helpers, and restore or reseed after any shared-state mutation.

## Verification

Checked by the reviewer or engineer who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Every file that mutates shared state restores it or reseeds, and helpers match the documented field shapes.
