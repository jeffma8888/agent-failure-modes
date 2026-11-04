---
id: INC-0599
title: A checklist expected a slug first link and excused absent headers, and installed UI source and a reviewer disproved both
date: 2026-11-04
classes: [spec-and-scope]
severity: medium
status: mitigated
---

# INC-0599 - A checklist expected a slug first link and excused absent headers, and installed UI source and a reviewer disproved both

**Cost:** The checklist was blocked and rewritten before a walk used it.

## Signature - how you recognise it

A manual checklist states what the UI will show without reading the installed UI code.

## What happened

The review blocked the checklist for two reasons. One check excused absent headers and inferred a multipart request from its size. The other expected a slug as the first link in the episode list and create steps, which the installed UI source disproves. A second version is written for both blocks and six notes, and the reviewer rechecks it.

## Root cause

Expectations were written from memory of the product instead of from the installed source.

## Why it was hard to see

A guessed expectation fails only when a person walks it, and may be ruled a product bug.

## Fix

Check each checklist expectation against the installed UI source, and require the headers and the request type to be observed.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Before a checklist states what a screen shows, verify it against installed UI source; do not infer request type or excuse missing headers.

## Related

[INC-0538](./INC-0538-a-dispatch-draft-marked-every-unsourced-value-for-the-lead-t.md)
