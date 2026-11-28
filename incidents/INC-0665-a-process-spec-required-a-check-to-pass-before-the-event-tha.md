---
id: INC-0665
title: A process spec required a check to pass before the event that triggers the check
date: 2026-11-26
classes: [spec-and-scope]
severity: low
status: fixed
topic: spec-and-scope/instructions-tools-cannot-follow
occurrences: 1
---

# INC-0665 - A process spec required a check to pass before the event that triggers the check

**Catalog:** [root](../catalog/README.md) / [spec-and-scope](../catalog/spec-and-scope/README.md) / [Instructions fail a gate or omit the required operation](../catalog/spec-and-scope/instructions-tools-cannot-follow.md)

**Cost:** One section of a first draft rewritten by its author in the same drafting pass, before review.

## Signature - how you recognise it

A phase list places a gate before an event, and the check behind that gate only starts when the event happens.

## What happened

The first draft of a requirements document for a delivery workflow listed its approval phases in order and required the continuous-integration run to be green before a pull request could be opened. In the same draft that run was triggered by opening the pull request, so the gate waited on a result that could not exist until the gated step had happened. The author found the cycle in a consistency pass before review and split the checks: local checks and the human approval come before the pull request, and the checks the pull request triggers come before the merge.

## Root cause

The phases were ordered by intent (quality before exposure) without writing down which event starts each check, so a dependency on a later event went unnoticed.

## Why it was hard to see

Each sentence is reasonable alone: checks should pass before review, and checks run on pull requests. The cycle appears only when the trigger of the check and the position of its gate are read together.

## Fix

Write beside every gate the event that starts its check, then walk the sequence once from the first phase and confirm each trigger has already happened when its gate is reached. Split a check that has a local form and an event-triggered form into two gates.

## Verification

The author's own consistency pass found the cycle and the draft was corrected before review. Not checked: whether the corrected sequence has been executed end to end, or whether the rule prevents recurrence.

## Transferable rule

> When specifying approval phases, name the event that triggers each check and walk the sequence to confirm it can run in that order; a gate must never wait on a result that exists only after the step it gates.

## Related

[INC-0621](./INC-0621-a-gate-list-named-a-pending-root-validator-after-a-pure-rena.md) [INC-0615](./INC-0615-a-gate-order-put-the-typecheck-right-after-type-generation-w.md) [INC-0353](./INC-0353-an-authorization-point-was-placed-after-the-first-event-that.md)
