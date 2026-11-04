---
id: INC-0629
title: A ruling said a test helper needed no revision route because one search seemed to show it was in no identity manifest, and the full gate then failed that check on exactly that entry
date: 2026-11-04
classes: [spec-and-scope]
severity: medium
status: mitigated
---

# INC-0629 - A ruling said a test helper needed no revision route because one search seemed to show it was in no identity manifest, and the full gate then failed that check on exactly that entry

**Cost:** A full gate run of about three minutes ended in an identity-check failure on the manifest entry the search had missed.

## Signature - how you recognise it

A repo checker that runs in under a second fails late in a long gate on a point already ruled.

## What happened

The lead ruled that a test helper needed no revision route because one search seemed to show it was in no identity manifest. The full gate then failed the repo's own identity check on exactly that manifest entry, after a run of about three minutes. The repo checker itself runs in about 0.4 seconds on the candidate tip.

## Root cause

A route was ruled from an inference drawn from one search, not from the repo's own checker.

## Why it was hard to see

The search result looked decisive, and the checker's verdict only appeared late in the long gate.

## Fix

Run the repo's own checker on the candidate tip before ruling a route.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Before ruling a route, run the repo's own checker on the candidate tip instead of inferring from a search.

## Related

[INC-0621](./INC-0621-a-gate-list-named-a-pending-root-validator-after-a-pure-rena.md) [INC-0618](./INC-0618-three-successive-oracle-changes-were-ruled-for-one-test-with.md)
