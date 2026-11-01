---
id: INC-0270
title: Restarting a shared dispatcher is the shared owner decision
date: 2026-11-01
classes: [delegation, ipc-and-env]
severity: medium
status: fixed
---

# INC-0270 - Restarting a shared dispatcher is the shared owner decision

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A team lead could have restarted a shared dispatcher that affects all teams.

## What happened

restarting a shared dispatcher loads new engine code for every team, so it is the shared owner decision, not a team lead

## Root cause

restarting a shared dispatcher loads new engine code for every team, so it is the shared owner decision, not a team lead

## Why it was hard to see

The restart looks local to the team.

## Fix

Leave stop, restart and config edits to the shared owner

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Leave a shared service restart to its shared owner

## Related

[INC-0237](./INC-0237-a-team-runtime-cap-blocked-new-teammates-behind-retained-idl.md)
