---
id: INC-0520
title: A manifest listed its lines unsorted and the landing gate refused it
date: 2026-11-02
classes: [identity-and-keying]
severity: low
status: mitigated
---

# INC-0520 - A manifest listed its lines unsorted and the landing gate refused it

**Cost:** One root was held out of a landing batch until the manifest was sorted.

## Signature - how you recognise it

The identity check requires sorted manifest lines, and a manifest lists one group before another.

## What happened

The manifest of one root listed its unit lines before its end-to-end lines. The identity check requires sorted lines, so the root was not landed with the rest of its batch, and the author was assigned to sort it.

## Root cause

The ordering rule was checked only at the landing and not by the author before handing the root over.

## Why it was hard to see

The content is correct and complete, and only a mechanical ordering rule is broken.

## Fix

Sort the lines as the check requires, and run the identity check on the root before handing it over.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Run the landing gate own identity check on a root before handing it over, so a mechanical ordering rule is met by the author and not found at the landing.

## Related

[INC-0513](./INC-0513-an-activation-moved-a-superseded-root-s-spec-while-main-carr.md)
