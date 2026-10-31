---
id: INC-0179
title: A chat pre-approval did not lift an explicit approval rule
date: 2026-10-30
classes: [delegation, tooling-paths]
severity: medium
status: fixed
---

# INC-0179 - A chat pre-approval did not lift an explicit approval rule

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

An upload stalled on an approval prompt that expired.

## What happened

An explicit tool approval rule still prompted after a chat pre-approval, and the prompt expired while the operator was away.

## Root cause

The pre-approval was assumed to carry over.

## Why it was hard to see

The failure shows up away from the cause and looks plausible.

## Fix

Queue the uploads and report them instead of retrying or rephrasing the command.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> When an approval prompt expires, queue and report; never rephrase around the rule.

## Related

[INC-0153](./INC-0153-a-test-checked-only-the-dispatch-argv-of-a-child-stage-not-i.md)
