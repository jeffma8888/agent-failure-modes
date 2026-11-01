---
id: INC-0289
title: A passing identity check was taken as agreement with the signed plan
date: 2026-11-01
classes: [spec-and-scope, false-green]
severity: medium
status: fixed
---

# INC-0289 - A passing identity check was taken as agreement with the signed plan

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A file resolved to the wrong owner while its identity check passed.

## What happened

no registry line existed for a replacement file, so the resolver fell back to the source family while the signed plan named a different owner; the identity checker validated form, not plan agreement

## Root cause

no registry line existed for a replacement file, so the resolver fell back to the source family while the signed plan named a different owner; the identity checker validated form, not plan agreement

## Why it was hard to see

The checker passes, so nothing prompts anyone to compare the resolved owner with the plan.

## Fix

Add the registry line and compare the resolved owner with the plan for every replacement

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Identity validity is not plan agreement; compare the resolved owner with the signed plan

## Related

[INC-0157](./INC-0157-a-split-ownership-root-could-not-activate-because-identity-h.md) [INC-0279](./INC-0279-replacing-an-active-test-file-moves-the-replacement-its-supe.md)
