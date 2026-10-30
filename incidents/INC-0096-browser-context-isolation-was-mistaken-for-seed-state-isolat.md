---
id: INC-0096
title: Browser-context isolation was mistaken for seed-state isolation
date: 2026-10-30
classes: [test-isolation]
severity: medium
status: fixed
---

# INC-0096 - Browser-context isolation was mistaken for seed-state isolation

**Cost:** Minor: caught in review, a re-check or acceptance before it shipped.

## Signature - how you recognise it

A spec reads seed data while relying on a fresh browser context.

## What happened

A spec read seed data and assumed isolation because each test had a fresh browser context, but database seed state is shared across contexts.

## Root cause

Two different kinds of isolation were treated as one.

## Why it was hard to see

Fresh context cleanly isolates cookies and storage, which looks like full isolation.

## Fix

A spec that reads seed data must reset and seed itself.

## Verification

Checked by the engineer, reviewer or lead who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Isolate each kind of state separately: browser state by context, data by reset and seed.
