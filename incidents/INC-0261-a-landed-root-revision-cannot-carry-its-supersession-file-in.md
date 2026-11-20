---
id: INC-0261
title: A landed root revision cannot carry its supersession file in the same commit
date: 2026-11-01
classes: [identity-and-keying, checkpoint]
severity: medium
status: fixed
topic: identity-and-keying/approval-names-wrong-commit
occurrences: 2
---

# INC-0261 - A landed root revision cannot carry its supersession file in the same commit

**Catalog:** [root](../catalog/README.md) / [identity-and-keying](../catalog/identity-and-keying/README.md) / [An approval or activation names the wrong commit or line of history](../catalog/identity-and-keying/approval-names-wrong-commit.md)

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A supersession file was planned in the same commit as the root it approves.

## What happened

an approved line must name the commit that already contains the bytes, so a root revision cannot carry its SUPERSEDES file in the same commit

## Root cause

an approved line must name the commit that already contains the bytes, so a root revision cannot carry its SUPERSEDES file in the same commit

## Why it was hard to see

An approval that names a commit cannot ship inside that commit.

## Fix

Land the root without it, then add the file after the non-author re-check

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Land a root revision first and add its supersession file after the non-author re-check

## Recurrences

Occurrences: 2. Repeats of this failure are recorded here instead of as new incidents.

- [INC-0595](./INC-0595-an-approval-header-named-the-review-commit-whose-tree-did-no.md) - 2026-11-04 - An approval header named the review commit, whose tree did not yet hold the reviewed root, and the identity checker refused it

## Related

[INC-0182](./INC-0182-a-marker-generator-covered-every-payload-of-a-root-when-only.md)
