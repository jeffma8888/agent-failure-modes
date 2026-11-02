---
id: INC-0389
title: Two plan checks ran at a wrong script path and the last line of their output looked like a result
date: 2026-11-01
classes: [false-green]
severity: low
status: fixed
---

# INC-0389 - Two plan checks ran at a wrong script path and the last line of their output looked like a result

**Cost:** A check that never ran looked like one that printed output.

## Signature - how you recognise it

A crashed check ended with a line that resembled a result.

## What happened

the lead ran two plan checks at a wrong script path and read them through the last output line only; after a crash stack, the last line was just the runtime version line, which looked like output

## Root cause

only the last line was read, and a crash stack can end in a harmless looking line

## Why it was hard to see

The last line is the cheapest thing to read, and it was not empty.

## Fix

Match the explicit pass line of the check; never trust the last line of a check

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Match the explicit pass line of a check, never its last line

## Related

[INC-0380](./INC-0380-a-landing-helper-s-clean-step-deleted-a-pending-root-directo.md) [INC-0371](./INC-0371-a-byte-count-compare-at-the-exact-old-length-reported-end-of.md) [INC-0396](./INC-0396-a-multi-step-command-reported-success-for-its-later-steps-wh.md)
