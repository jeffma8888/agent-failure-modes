---
id: INC-0136
title: A cross-agent inventory flake came from sharing one harness cluster between runtime agents
date: 2026-10-30
classes: [test-isolation, concurrency]
severity: medium
status: fixed
---

# INC-0136 - A cross-agent inventory flake came from sharing one harness cluster between runtime agents

**Cost:** Minor: caught by an engineer, reviewer or the lead before it shipped, except item one which delayed finished work.

## Signature - how you recognise it

Inventory checks fail when two agents use one cluster.

## What happened

A cross-agent inventory flake showed that two runtime agents shared one harness cluster.

## Root cause

Cluster ownership was per environment, not per agent.

## Why it was hard to see

Each run is correct alone.

## Fix

Use one harness cluster per runtime agent.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Give each agent its own cluster.

## Related

[INC-0097](./INC-0097-url-guards-did-not-prove-a-test-owned-the-disposable-cluster.md)
