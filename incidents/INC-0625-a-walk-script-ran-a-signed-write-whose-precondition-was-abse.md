---
id: INC-0625
title: A walk script ran a signed write whose precondition was absent because the step before it had been refused, and the write succeeded on a record that never met the condition
date: 2026-11-04
classes: [false-green]
severity: medium
status: mitigated
---

# INC-0625 - A walk script ran a signed write whose precondition was absent because the step before it had been refused, and the write succeeded on a record that never met the condition

**Cost:** One step's result is void, neither a pass nor a defect, and the walk item stays blocked.

## Signature - how you recognise it

A dependent step succeeds on a record that never reached the state the step requires.

## What happened

A manual walk script saved two edits, then tried to publish, which was refused because a required value had not been supplied. The same script still ran the next step, a slug change signed for after a real published version. It saved on a record that had never been published, so it ran outside its signed condition. The walker caught the breach and reported it. The ruling voided that step, classified the refused publish as a walker input error and not a product finding, and kept the item blocked. The independent steps in the same script stand.

## Root cause

The script did not stop when a step failed and did not check the precondition of the dependent step.

## Why it was hard to see

The dependent write succeeded, so its output looked like a pass.

## Fix

Assert each dependent step's precondition with a fresh read right before the write, and exit before any later step on failure.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A script asserts each dependent step's precondition with a fresh read right before the write and exits before any later step on failure.

## Related

[INC-0623](./INC-0623-a-helper-piped-to-tail-and-followed-by-ran-the-next-step-alt.md) [INC-0620](./INC-0620-a-publish-gate-chain-ran-a-build-script-at-a-path-that-does.md)
