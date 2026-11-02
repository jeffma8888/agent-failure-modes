---
id: INC-0503
title: A brief stated a baseline environment from a compacted summary, and the baseline script showed the opposite
date: 2026-11-02
classes: [spec-and-scope]
severity: low
status: mitigated
---

# INC-0503 - A brief stated a baseline environment from a compacted summary, and the baseline script showed the opposite

**Cost:** One round trip and a withdrawn brief; no wrong result was recorded because the implementer checked the script.

## Signature - how you recognise it

A brief says a baseline ran with a variable unset, and the script that produced the baseline sets it.

## What happened

A brief said a whole-suite baseline had been run with a storage variable unset and that this gave exactly the known failures. The premise came from a compacted summary. The implementer read the script that produced the baseline, found the variable was set to a fresh directory, and saw that the failure names did not involve that variable. It followed the artifact and reported the contradiction. The wording was withdrawn, and every comparison was ruled to set the variable to a fresh directory the runner creates and records.

## Root cause

An environment fact was carried from a summary into an instruction instead of being read from the script or log that produced the baseline.

## Why it was hard to see

A summary states the premise with the same confidence as the artifact, and the premise sounds plausible, so only reading the producing script exposes it.

## Fix

State a baseline environment from the script or log that produced it. Withdraw the earlier wording, and record the variable the runner sets for each comparison.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> State a baseline environment from the script or log that produced it, never from memory; an implementer who sees a premise contradict the artifact follows the artifact and reports it.

## Related

[INC-0457](./INC-0457-a-ruling-wrote-a-media-directory-binding-from-memory-that-co.md) [INC-0456](./INC-0456-the-lead-wrote-ruling-timestamps-from-memory-three-times-and.md)
