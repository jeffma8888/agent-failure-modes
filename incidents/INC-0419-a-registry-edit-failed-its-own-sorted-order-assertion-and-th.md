---
id: INC-0419
title: A registry edit failed its own sorted-order assertion, and the identity checker refuses a supersession whose old path the registry still names
date: 2026-11-02
classes: [identity-and-keying]
severity: low
status: fixed
---

# INC-0419 - A registry edit failed its own sorted-order assertion, and the identity checker refuses a supersession whose old path the registry still names

**Cost:** One registry edit was rejected by its own assertion before landing.

## Signature - how you recognise it

A registry edit and a supersession record conflicted when landed separately.

## What happened

the lead's registry edit first failed its own sorted-order assertion, and the identity checker refuses a SUPERSEDES whose old path is still named by the registry; both files change in one control commit

## Root cause

the registry and the supersession record each constrain the other, so neither can land first

## Why it was hard to see

Each file was valid alone and invalid next to the other.

## Fix

edit the registry line and the supersession record together in one control commit, and assert sorted order before landing

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Change the registry line and the supersession record whose old path it names in one control commit, and assert the sorted order first

## Related

[INC-0279](./INC-0279-replacing-an-active-test-file-moves-the-replacement-its-supe.md) [INC-0123](./INC-0123-after-activation-a-registry-line-named-a-pending-path-that-n.md) [INC-0157](./INC-0157-a-split-ownership-root-could-not-activate-because-identity-h.md) [INC-0428](./INC-0428-a-supersession-marker-was-deferred-to-each-row-s-activation.md) [INC-0445](./INC-0445-a-migration-lock-covered-the-whole-branch-when-it-needed-to.md)
