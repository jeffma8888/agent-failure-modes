---
id: INC-0335
title: A pinned base digest froze a file that a later row split needed to change
date: 2026-11-01
classes: [spec-and-scope, identity-and-keying]
severity: medium
status: fixed
---

# INC-0335 - A pinned base digest froze a file that a later row split needed to change

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A needed edit to a file would have invalidated the digest that prepared patches pin.

## What happened

prepared patches pinned the digest of one file, so a planned change to that file could not land before the patches, and had to become a later patch drafted on the modelled result

## Root cause

prepared patches pinned the digest of one file, so a planned change to that file could not land before the patches, and had to become a later patch drafted on the modelled result

## Why it was hard to see

The edit is small and correct, and its only cost is invalidating every patch bound to the old digest.

## Fix

Treat the pinned file as frozen and route every change through a later patch with the same regenerate caveat

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> When prepared patches pin a file's digest, treat that file as frozen and route every change through a later patch with the same regenerate caveat

## Related

[INC-0326](./INC-0326-a-signer-recomputed-the-declared-digest-before-signing-and-k.md) [INC-0122](./INC-0122-a-digest-present-anywhere-in-a-manifest-was-taken-as-proof-i.md) [INC-0421](./INC-0421-a-closure-packet-freeze-test-turned-positive-on-a-control-on.md) [INC-0436](./INC-0436-a-squash-recipe-equated-the-landing-tree-with-a-stale-branch.md)
