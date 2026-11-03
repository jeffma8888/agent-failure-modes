---
id: INC-0534
title: A configuration mutation failed a setup assertion before any case oracle ran, so the red proved nothing about the cases
date: 2026-11-02
classes: [false-green]
severity: medium
status: mitigated
---

# INC-0534 - A configuration mutation failed a setup assertion before any case oracle ran, so the red proved nothing about the cases

**Cost:** Two cases were credited with mutations whose red would have come from setup; caught in static review.

## Signature - how you recognise it

A mutation breaks the configuration, and the shared setup asserts the same configuration and fails first.

## What happened

A root coverage named removing or reordering collections in the configuration as the mutations for two cases. The setup step of the root asserts exactly the same list of collections, so those mutations fail in setup before the dashboard cards or the navigation are checked. A setup assertion is not evidence that each case detects broken rendered links. The reviewer required mutations that survive setup and reach the case assertions, and ruled that discovery, import or setup failure is not mutation evidence.

## Root cause

The mutation target overlapped the fixture assertion, so the earliest failure was the setup one.

## Why it was hard to see

The run is red, which looks like success for the mutation, and only the failing line shows it was the wrong one.

## Fix

Choose mutations that pass the setup assertions and fail at the case own assertion line.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A mutation counts for a case only when it fails at that case own assertion; check that the setup and fixture assertions do not fail first.

## Related

[INC-0524](./INC-0524-a-root-named-a-mutation-its-assertions-could-not-see-because.md) [INC-0533](./INC-0533-a-named-mutant-was-masked-by-an-independent-guard-upstream-s.md)
