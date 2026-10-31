---
id: INC-0203
title: A setup failure was at risk of counting as a test run
date: 2026-10-30
classes: [false-green, tooling-paths]
severity: medium
status: fixed
---

# INC-0203 - A setup failure was at risk of counting as a test run

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

The run failed before any test started.

## What happened

Setup-only failures of a clean-clone run, such as a missing package-manager cache or a missing metadata cache in a moved private environment, are not test executions but could be counted as runs.

## Root cause

Setup-only failures of a clean-clone run, such as a missing package-manager cache or a missing metadata cache in a moved private environment, are not test executions but could be counted as runs.

## Why it was hard to see

The run exits red like any other.

## Fix

Report them, fix the invocation, and do not count them as runs

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Do not count a setup-only failure as a run

## Related

[INC-0188](./INC-0188-an-override-changed-the-lockfile-and-an-offline-clone-could.md)
