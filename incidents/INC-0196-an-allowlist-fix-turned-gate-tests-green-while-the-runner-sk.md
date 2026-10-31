---
id: INC-0196
title: An allowlist fix turned gate tests green while the runner skipped the new project
date: 2026-10-30
classes: [false-green, tooling-paths]
severity: medium
status: fixed
---

# INC-0196 - An allowlist fix turned gate tests green while the runner skipped the new project

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

The gate tests passed and the new project never ran.

## What happened

An adapter allowlist fix made the gate tests green while the delegated runner silently skipped the new project; only the shared stage record was checked.

## Root cause

An adapter allowlist fix made the gate tests green while the delegated runner silently skipped the new project; only the shared stage record was checked.

## Why it was hard to see

The shared record looks like proof of every project.

## Fix

Prove the project own marker as well as the shared stage record, and carry the newest helper revision when its config writer must change

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Prove a new project ran by its own marker, not only by the shared stage record

## Related

[INC-0190](./INC-0190-fast-stayed-green-while-a-command-adapter-fixture-missed-a-n.md)
