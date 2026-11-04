---
id: INC-0605
title: Corpus commits sat unpushed after the gate, and a push was answered with a server error, so the remote head must be read back after every push
date: 2026-11-04
classes: [checkpoint]
severity: medium
status: mitigated
---

# INC-0605 - Corpus commits sat unpushed after the gate, and a push was answered with a server error, so the remote head must be read back after every push

**Cost:** Eight incidents were missing from the remote until the lead found them.

## Signature - how you recognise it

Local commits exist after a passed gate and the remote head is older.

## What happened

Two corpus commits (eight incidents) passed their gate but were not on the remote. The lead found them unpushed and reran the gate, and the first push got a server error. The second landed, and the remote head was checked with ls-remote. An earlier push had also been answered with a server error and later went through on retry.

## Root cause

A passed gate was treated as publication, and a push failure was not read back.

## Why it was hard to see

A server error on push looks like a failure, and a quiet success on retry looks like a finished job until the remote is read.

## Fix

Read the remote head back with ls-remote after every push, and report any commit that is not on the remote.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> After every push, read the remote head back with ls-remote and compare it with the local head; do not call a gate-passed commit published until they match.

## Related

[INC-0592](./INC-0592-a-static-triage-found-four-open-rows-already-done-by-named-m.md)
