---
id: INC-0596
title: An observer recorded zero denied connects while it also missed the server's database connect, so zero denied proved nothing
date: 2026-11-04
classes: [detector-fail-open]
severity: high
status: mitigated
---

# INC-0596 - An observer recorded zero denied connects while it also missed the server's database connect, so zero denied proved nothing

**Cost:** A run that looked clean could not be credited; the criteria were rewritten around a positive control.

## Signature - how you recognise it

A monitor reports zero violations and zero of an event that must occur.

## What happened

Under the production serving mode the unchanged observer recorded registry 0, telemetry 0, loopback connects 0 and denied 0, but it also recorded no database TCP connect although the app reads the database. So the run did not show that the observer sees every transport in the serving processes. The ruling made a positive control a done criterion: the observer must record the server's database connect with its allow decision, in the process that makes it. The coverage fix was accepted when four allowed connects were recorded through the socket connect method, with both observer mutants red.

## Root cause

The observer's preload did not cover a transport the serving process uses, so silence was not evidence of absence.

## Why it was hard to see

Zero denied reads as a pass; only an event that must occur and is missing reveals the blind spot.

## Fix

Add a positive control that makes the observer record a known allowed event, and fix coverage before trusting a zero count.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Before trusting a zero-violations monitor, require a positive control: a known event it must record in the process that makes it.

## Related

[INC-0575](./INC-0575-a-lock-design-passed-its-own-14-tests-and-a-reviewer-s-four.md)
