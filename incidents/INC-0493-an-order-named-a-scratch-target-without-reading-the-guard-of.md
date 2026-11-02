---
id: INC-0493
title: An order named a scratch target without reading the guard of the command that would fill it
date: 2026-11-02
classes: [delegation]
severity: low
status: mitigated
---

# INC-0493 - An order named a scratch target without reading the guard of the command that would fill it

**Cost:** None incurred: a reviewer found it while writing a checklist, before any run, and the executor stopped before creating anything; the cost was a new dedicated database cluster and a re-issued order.

## Signature - how you recognise it

The target named in the order was on the list of targets the named command refuses.

## What happened

A ruling named a scratch database on the shared database server and the test seed command to fill it. That command has a guard that refuses unless the environment is marked test, both connection strings use a dedicated loopback port other than the shared one, the admin string names the maintenance database on the same port, and the database name carries a test prefix. A reviewer found the conflict while writing the checklist. The executor stopped before creating anything. The target was moved to a new dedicated cluster, the guard was left unchanged, and the order was amended so the shared server is not used at all.

## Root cause

The order named a target and a command without reading the command guard against that target.

## Why it was hard to see

The target looked ordinary and the command looked routine, and the refusal would have shown only at the first run.

## Fix

Move the target to one the guard accepts, leave the guard unchanged, amend the order, and read the guard of every command named against the target before issuing an order.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Before naming a target in an order, read the guards of every command you name against that target.

## Related

[INC-0489](./INC-0489-a-rule-written-in-teammate-briefs-was-broken-by-the-lead-in.md)
