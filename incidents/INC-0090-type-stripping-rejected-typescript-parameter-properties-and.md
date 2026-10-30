---
id: INC-0090
title: Type-stripping rejected TypeScript parameter properties, and admin selectors were undefined
date: 2026-10-30
classes: [tooling-paths, spec-and-scope]
severity: low
status: fixed
---

# INC-0090 - Type-stripping rejected TypeScript parameter properties, and admin selectors were undefined

**Cost:** Minor: caught in review or by a stop rule before it shipped.

## Signature - how you recognise it

A page object fails to load under a type-stripping runtime, or a test needs UI selectors that do not exist.

## What happened

Strip-types rejects TypeScript parameter properties, so page objects needed explicit fields. Where admin selectors were undefined, editor steps went through the staff REST API.

## Root cause

The runtime supports only erasable TypeScript syntax, and the UI contract did not define selectors.

## Why it was hard to see

The code compiles in an editor but fails at load.

## Fix

Use explicit fields in page objects; when selectors are undefined, drive editor steps through the staff REST API and assert the viewer result.

## Verification

Checked by the reviewer or engineer who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Write test code in erasable TypeScript only, and assert through contracts that exist.
