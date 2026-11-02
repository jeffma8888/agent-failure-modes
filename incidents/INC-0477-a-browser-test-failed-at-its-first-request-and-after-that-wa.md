---
id: INC-0477
title: A browser test failed at its first request, and after that was fixed the next run failed at a step that had never run
date: 2026-11-02
classes: [false-green]
severity: low
status: fixed
---

# INC-0477 - A browser test failed at its first request, and after that was fixed the next run failed at a step that had never run

**Cost:** Minor: one extra run to reach the step; found before merge.

## Signature - how you recognise it

Fixing an early test failure exposed a later step that had never run.

## What happened

A browser test failed at its first API read with a 403, which hid every later step. After the fix for that cause, the next run passed login and the new identity assertion and failed where a locator for a form field was not found on the edit view, a step that had never run. The fix moved the failure later and did not finish the test.

## Root cause

The early failure stopped the test, so the later steps had never been executed and carried no evidence.

## Why it was hard to see

A fixed first failure looks like progress toward green, and the later steps look verified because they exist in the file.

## Fix

After a fix moves a failure later, treat each newly reached step as never verified, read it against the framework source before the next run, and keep the evidence of the earlier steps separate.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> When a fix moves a failure later in a test, treat every newly reached step as never verified; a green earlier step proves only that step.

## Related

[INC-0447](./INC-0447-tests-authored-but-never-executed-passed-acceptance-and-the.md) [INC-0472](./INC-0472-the-first-browser-test-to-load-the-app-config-failed-to-link.md)
