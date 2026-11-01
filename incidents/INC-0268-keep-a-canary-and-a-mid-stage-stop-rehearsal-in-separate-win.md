---
id: INC-0268
title: Keep a canary and a mid-stage STOP rehearsal in separate windows
date: 2026-11-01
classes: [checkpoint, spec-and-scope]
severity: medium
status: fixed
---

# INC-0268 - Keep a canary and a mid-stage STOP rehearsal in separate windows

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A rehearsal planned inside a canary could have destroyed the canary evidence.

## What happened

a canary that also hosts a mid-stage STOP rehearsal can destroy the evidence it was meant to produce

## Root cause

a canary that also hosts a mid-stage STOP rehearsal can destroy the evidence it was meant to produce

## Why it was hard to see

Combining them saves a window.

## Fix

Run the canary to its terminal record and record the verdict first; move the rehearsal to its own window

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Do not host a destructive rehearsal inside the run that produces the evidence

## Related

[INC-0266](./INC-0266-a-planned-round-with-stop-in-place-proves-nothing.md)
