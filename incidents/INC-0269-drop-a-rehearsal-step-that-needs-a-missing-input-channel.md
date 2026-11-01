---
id: INC-0269
title: Drop a rehearsal step that needs a missing input channel
date: 2026-11-01
classes: [spec-and-scope, false-green]
severity: medium
status: fixed
---

# INC-0269 - Drop a rehearsal step that needs a missing input channel

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A rehearsal step could only pass if its input was faked.

## What happened

a rehearsal step needed an input channel the engine does not have, so it was dropped by ruling rather than faked (G5, R-EA)

## Root cause

a rehearsal step needed an input channel the engine does not have, so it was dropped by ruling rather than faked (G5, R-EA)

## Why it was hard to see

A faked input yields a green that proves nothing.

## Fix

Drop the step and say why in the ruling

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Drop a step that needs a missing channel rather than faking it

## Related

[INC-0252](./INC-0252-a-word-grep-reported-a-failure-in-a-passing-log.md)
