---
id: INC-0614
title: A signed command allow-list written from the runtime list omitted the commands the packet's own test-first and static steps needed, and the engineer stopped
date: 2026-11-04
classes: [spec-and-scope]
severity: low
status: mitigated
---

# INC-0614 - A signed command allow-list written from the runtime list omitted the commands the packet's own test-first and static steps needed, and the engineer stopped

**Cost:** The engineer could not run two required steps and stopped, so work waited for an amended allow-list.

## Signature - how you recognise it

A packet requires a step whose command is not on its own signed allow-list.

## What happened

A go packet was signed with a command allow-list written from the runtime command list. The packet's own test-first steps, a scoped unit run and a typecheck, needed commands the list omitted. The engineer stopped correctly instead of improvising a command outside the signed list.

## Root cause

The allow-list was built from the runtime commands and not from the packet's required steps.

## Why it was hard to see

The list looked complete against the runtime, and the gap showed only when the engineer reached the early steps.

## Fix

Derive the allow-list by walking every required step of the packet, including test-first reds and static gates, and have the engineer stop and ask when a step needs an unlisted command.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Derive a signed command allow-list by walking every required step of the packet, including test-first reds and static gates, not from the runtime list alone.

## Related

[INC-0612](./INC-0612-a-ruling-set-a-lock-wait-the-installed-lock-could-not-honour.md) [INC-0609](./INC-0609-a-brief-said-to-move-a-post-case-full-seed-to-afterall-but-t.md)
