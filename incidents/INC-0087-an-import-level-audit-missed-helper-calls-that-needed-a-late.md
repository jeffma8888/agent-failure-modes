---
id: INC-0087
title: An import-level audit missed helper calls that needed a later row, and only the engineer stop rule caught it
date: 2026-10-30
classes: [delegation, spec-and-scope]
severity: medium
status: fixed
---

# INC-0087 - An import-level audit missed helper calls that needed a later row, and only the engineer stop rule caught it

**Cost:** Minor: caught in review or by a stop rule before it shipped.

## Signature - how you recognise it

A helper call such as a registered-resource lookup needs a feature delivered by a later row.

## What happened

An import-level audit passed, but a helper call needed pidfiles from a later row. The engineer stopped under an explicit stop rule.

## Root cause

Imports show what is loaded, not which helper methods need later-row behavior.

## Why it was hard to see

The dependency is in a method call, so import analysis cannot see it.

## Fix

Give engineers an explicit stop rule for needs that belong to a later row.

## Verification

Checked by the reviewer or engineer who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Pair static audits with a stop rule so an engineer halts when a call needs later-row behavior.
