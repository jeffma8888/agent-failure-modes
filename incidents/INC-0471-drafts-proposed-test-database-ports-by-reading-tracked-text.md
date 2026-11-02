---
id: INC-0471
title: Drafts proposed test database ports by reading tracked text, and two clashed with each other and two with live listeners
date: 2026-11-02
classes: [concurrency]
severity: low
status: fixed
---

# INC-0471 - Drafts proposed test database ports by reading tracked text, and two clashed with each other and two with live listeners

**Cost:** None: found before any cluster was created.

## Signature - how you recognise it

Proposed numbers collided with each other and with live listeners.

## What happened

several drafts proposed test database ports by reading tracked text only; two drafts chose the same number and two chose ports that a live server was already listening on; the lead read only listener listing found it, voided every proposal and allocated the numbers centrally, each a placeholder until a read only probe at that row start shows no listener

## Root cause

free numbers were chosen by searching text, which says nothing about what is listening now

## Why it was hard to see

Each draft looked correct on its own, and only a view of the live system shows the clash.

## Fix

allocate shared numbered resources centrally, and probe the live system read only at the time of use; if occupied, stop and report, and the lead picks the next free number

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Allocate shared numbered resources centrally and probe the live system at use time; a text search for free numbers is not a probe

## Related

[INC-0136](./INC-0136-a-cross-agent-inventory-flake-came-from-sharing-one-harness.md) [INC-0305](./INC-0305-a-process-the-sandbox-could-not-see-was-judged-dead-and-its.md) [INC-0393](./INC-0393-a-load-reading-taken-minutes-before-a-launch-was-stale-and-t.md)
