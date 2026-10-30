---
id: INC-0124
title: A poll timeout placed in assertion options was still a propagation override, and shared helpers were left out of the dependent root verdict
date: 2026-10-30
classes: [stage-timeout, spec-and-scope]
severity: medium
status: fixed
---

# INC-0124 - A poll timeout placed in assertion options was still a propagation override, and shared helpers were left out of the dependent root verdict

**Cost:** Minor: caught in review, an audit or an engineer check before it shipped.

## Signature - how you recognise it

A timeout override hides in assertion options or a shared helper that a root depends on.

## What happened

A poll timeout in assertion options carried an override across a revision just like a test-level timeout. Shared helpers were not checked as part of each dependent root verdict.

## Root cause

Only test-level timeouts were treated as overrides, and verdicts stopped at the root files.

## Why it was hard to see

The value sits inside an options object, and the helper is owned by another root.

## Fix

Treat any timeout as an override unless its value comes from an oracle deadline, and check shared helpers in every dependent root verdict.

## Verification

Checked by the reviewer, engineer or lead who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Only an oracle-valued deadline is exempt from the override rule; include shared helpers in each dependent verdict.

## Related

[INC-0107](./INC-0107-a-timeout-override-was-not-re-checked-against-the-newest-rul.md) [INC-0111](./INC-0111-http-only-timeouts-were-copied-from-a-process-hang-pattern-w.md)
