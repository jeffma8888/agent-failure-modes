---
id: INC-0616
title: A signed packet required a tail-only migration rollback, but the named command rolls back a whole batch, so on a fresh database it would undo every migration
date: 2026-11-04
classes: [spec-and-scope]
severity: medium
status: mitigated
---

# INC-0616 - A signed packet required a tail-only migration rollback, but the named command rolls back a whole batch, so on a fresh database it would undo every migration

**Cost:** The engineer's fourth stop; no database was allocated, and the proof step was replaced by a driver script.

## Signature - how you recognise it

A signed proof step names a command whose installed semantics are broader than the claim it must prove.

## What happened

The packet required proof that only the newest migration rolls back. The installed migration code gives every pending file one batch number and rolls back every row of the latest batch. On a fresh database the named migrate, down, migrate sequence would therefore roll back all six migrations and could not prove a tail-only rollback. The engineer stopped before allocating anything. The ruling replaced it with a driver script that first migrates an explicit list without the newest file, then migrates the rest so the newest sits alone in its batch, rolls back one batch, and checks the result.

## Root cause

The packet named a command by its name, not by what the installed code does to a fresh database.

## Why it was hard to see

The command is the usual round trip and works as named for a single migration; the batch semantics only matter when many are pending.

## Fix

Read the installed tool against each requirement it must prove, and where the semantics differ, use a driver that sets up the batch boundary explicitly.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Before signing, read the tool's installed semantics against each requirement it must prove; a command name is not evidence it proves the claim.

## Related

[INC-0612](./INC-0612-a-ruling-set-a-lock-wait-the-installed-lock-could-not-honour.md) [INC-0615](./INC-0615-a-gate-order-put-the-typecheck-right-after-type-generation-w.md)
