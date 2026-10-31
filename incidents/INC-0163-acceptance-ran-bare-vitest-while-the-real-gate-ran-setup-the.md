---
id: INC-0163
title: Acceptance ran bare vitest while the real gate ran setup then the FAST runner
date: 2026-10-30
classes: [false-green, tooling-paths]
severity: medium
status: fixed
---

# INC-0163 - Acceptance ran bare vitest while the real gate ran setup then the FAST runner

**Cost:** Minor: a green row merge looked red.

## Signature - how you recognise it

A row merge looked red under the acceptance script and green under preship, or the reverse.

## What happened

The lead acceptance script ran bare vitest, which stopped being valid once the server project gained a global setup that needs the per-stage database the FAST runner provides.

## Root cause

The acceptance command was a shortcut that differed from the commands preship runs.

## Why it was hard to see

The shortcut was valid until a project gained a setup dependency, and nothing flagged the drift.

## Fix

Run the same commands preship runs: setup, then the FAST runner.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Acceptance must run the same commands preship runs, otherwise a green merge looks red or a red one looks green.

## Related

[INC-0145](./INC-0145-a-readiness-check-measured-the-lead-checkout-while-preship-m.md)
