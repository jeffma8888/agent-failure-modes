---
id: INC-0612
title: A ruling set a lock wait the installed lock could not honour, because the tool hard-codes the wait and reads no variable
date: 2026-11-04
classes: [spec-and-scope]
severity: low
status: mitigated
---

# INC-0612 - A ruling set a lock wait the installed lock could not honour, because the tool hard-codes the wait and reads no variable

**Cost:** One ruling could not be carried out as written, and the single readmission attempt waited for a signal instead of running.

## Signature - how you recognise it

A ruling names a tool parameter that the installed tool does not expose.

## What happened

After an invocation ended NOT-RUN on the lock wait limit of 2700 s, the lead granted one readmission with the wait raised to 5400 s. The installed lock hard-codes 2700 s and reads no environment variable, so the ruling could not be honoured without an altered copy. The author asked instead of improvising. The lead amended the ruling: the installed tool unchanged, and the one readmission submitted only when the lead signals that the queue holds at most one other job. The lead declined a copied wrapper because the lock has no queue order and the one-invocation rule is better served by timing.

## Root cause

The wait was ruled from what was wanted, not from what the installed tool exposes.

## Why it was hard to see

Raising a wait looks like a harmless parameter change; only reading the tool shows it is a constant.

## Fix

Amend the ruling to the unchanged tool plus a signal to submit when the queue is short, and have authors ask when a ruling cannot be carried out as written.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Before ruling a parameter, read the tool to confirm it exposes that parameter; if a ruling cannot be carried out as written, ask instead of improvising a copy.

## Related

[INC-0609](./INC-0609-a-brief-said-to-move-a-post-case-full-seed-to-afterall-but-t.md) [INC-0594](./INC-0594-a-successor-draft-named-as-its-old-bytes-a-revision-that-was.md)
