---
id: INC-0359
title: A stored admission record left out the tool versions it was produced under
date: 2026-11-01
classes: [identity-and-keying, spec-and-scope]
severity: medium
status: fixed
---

# INC-0359 - A stored admission record left out the tool versions it was produced under

**Cost:** Minor: caught in spec review before it shipped.

## Signature - how you recognise it

A per-file audit that admits concurrent test runs recorded no tool versions, so a proof from one toolchain would unlock the fast route under another.

## What happened

a test harness kept an audit register that decided, per test file, whether files could safely run concurrently. The register recorded no interpreter or package manager version. An entry proven under one toolchain would still admit concurrency under another, and a missing or malformed version had no defined outcome

## Root cause

the register was keyed on the file and its content but not on the toolchain whose behavior the proof depended on

## Why it was hard to see

The audit looked complete because it covered every file and helper, and tool versions are environment rather than input, so nobody listed them as part of the proof's identity.

## Fix

Add runtime fields (interpreter version and package manager version) to the register and compare them with the running toolchain; any missing, malformed, unreadable or unequal value counts as malformed input and takes the serial route with a named reason, covered by a witness and the reason table

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A stored proof that unlocks a faster or riskier route must carry the tool versions it was produced under and compare them at use; a mismatch or a missing field takes the safe route with a named reason, never the fast one

## Related

[INC-0354](./INC-0354-gating-by-an-environment-variable-leaked-into-nested-runners.md) [INC-0256](./INC-0256-evidence-commands-ran-on-a-shimmed-runtime-instead-of-the-pi.md) [INC-0356](./INC-0356-a-reviewed-recipe-never-ran-its-real-tool-queries-because-ev.md)
