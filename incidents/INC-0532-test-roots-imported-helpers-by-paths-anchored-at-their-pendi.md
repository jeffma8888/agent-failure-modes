---
id: INC-0532
title: Test roots imported helpers by paths anchored at their pending depth, so every import would break at the active destination
date: 2026-11-02
classes: [tooling-paths]
severity: medium
status: mitigated
---

# INC-0532 - Test roots imported helpers by paths anchored at their pending depth, so every import would break at the active destination

**Cost:** Two roots were blocked in review and needed successors; found statically before activation.

## Signature - how you recognise it

A spec imports by relative paths that resolve from its pending folder and climb outside the repository from its active folder.

## What happened

The specs of two roots imported helpers and a testing module with relative paths written for the pending folder. At the active destination those paths climb outside the repository and every import target is absent. Activation must copy a pending file byte for byte, so an activator may not rewrite the imports, and a valid manifest does not prove that imports resolve. Both roots were blocked and successors were assigned.

## Root cause

The paths were written for where the file sits while it is a draft, not for where it will run.

## Why it was hard to see

The manifest and the file are internally consistent, and the failure appears only at a location the file has not yet reached.

## Fix

Write imports for the active destination, or resolve every import from the destination path before a root is landed.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Check that every import of a root resolves from the path where the file will run, not only from where it is written; a pending copy that must move byte-identical cannot be repaired at activation.

## Related

[INC-0513](./INC-0513-an-activation-moved-a-superseded-root-s-spec-while-main-carr.md) [INC-0473](./INC-0473-a-test-file-was-edited-on-order-although-its-digest-was-pinn.md)
