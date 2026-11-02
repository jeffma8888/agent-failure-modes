---
id: INC-0363
title: A module-presence guard went through the test's own file-system mock, so a missing-API label was never proven
date: 2026-11-01
classes: [false-green, test-isolation]
severity: low
status: fixed
---

# INC-0363 - A module-presence guard went through the test's own file-system mock, so a missing-API label was never proven

**Cost:** Minor: six red cells carried an unproven label until the first green run; nothing shipped.

## Signature - how you recognise it

Tests labelled as missing-API reds still failed at the same guard after the module existed.

## What happened

six tests were labelled missing-API reds at the first red stage. At the first green run they still failed at the same guard although the module existed. The guard checked module presence with a file-existence call, and the same test file replaced the file-system module with a mock that answered true only for one configuration string and false for the module's location. The guard therefore fired whether or not the module existed, and the missing-API label was never evidence. The green run showed four real behavioural gaps and six guard failures, with no genuine missing-API failure

## Root cause

a presence check was routed through a mock installed by the same test, and the red classification was accepted without observing the guard in both states (module present, module absent)

## Why it was hard to see

A red at the guard looks exactly like the expected missing-API red, and a guard that always fires can never contradict the label.

## Fix

The earlier label was withdrawn as unproven. A test-only change makes the mock pass every other argument through to the real implementation, or the guard uses a presence check that does not use the mock; both observations are recorded (module present: the guard is silent; module hidden in a controlled way: the guard fires)

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Before counting a red as missing-API, prove the guard both ways (module present: silent; module absent: fires), and never route a presence check through a mock the same test installs

## Related

[INC-0083](./INC-0083-controls-that-fail-in-only-one-direction-a-drop-guard-keyed.md) [INC-0318](./INC-0318-a-path-guard-probed-only-with-nonexistent-paths-could-never.md) [INC-0320](./INC-0320-a-positive-control-s-first-red-was-the-control-s-own-defect.md)
