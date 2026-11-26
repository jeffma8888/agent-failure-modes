---
id: INC-0648
title: A current project thesis relied on a shutdown report that had already been reversed
date: 2026-11-23
classes: [spec-and-scope]
severity: medium
status: mitigated
topic: spec-and-scope/claims-outrun-available-evidence
occurrences: 1
---

# INC-0648 - A current project thesis relied on a shutdown report that had already been reversed

**Catalog:** [root](../catalog/README.md) / [spec-and-scope](../catalog/spec-and-scope/README.md) / [Claims or instructions say more than the evidence supports](../catalog/spec-and-scope/claims-outrun-available-evidence.md)

**Cost:** An outdated premise reached the project vision, overview and teammate brief; correction effort was not timed.

## Signature - how you recognise it

A dated secondary report supports a present-tense market premise, while the primary status source records a later reversal.

## What happened

The lead based the project thesis on a single news report that a competitor product had shut down. The report was accurate when published, but the primary changelog showed that the shutdown had been reversed nine days later. An author following a primary-sources-only requirement found the reversal after the premise had spread into three planning artifacts.

## Root cause

Evidence that an event occurred was treated as evidence that its resulting state still held; no write-time check of the primary status source bounded the present-tense claim.

## Why it was hard to see

The secondary report was not fabricated or initially wrong. Its clear historical statement became misleading only when reused as a current premise, and copying it between documents added apparent agreement without new evidence.

## Fix

Require a fresh primary-source status check for each current-event premise before publishing it, record the check date, and revise the artifacts that inherited the outdated premise.

## Verification

The author checked the primary changelog and found the later reversal. Not checked in the input: a complete re-audit of the affected artifacts or whether the new write-time check prevents recurrence.

## Transferable rule

> Check every current-event premise against the primary status source at write time and record the check date; use secondary reporting to establish historical events, not present state.

## Related

[INC-0593](./INC-0593-a-packet-author-who-could-not-read-the-rulings-file-marked-e.md) [INC-0577](./INC-0577-an-exact-list-in-a-test-was-authored-on-an-older-base-and-re.md)
