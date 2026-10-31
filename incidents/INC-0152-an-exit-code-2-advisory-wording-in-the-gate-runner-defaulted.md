---
id: INC-0152
title: An exit code 2 advisory wording in the gate runner defaulted to proceed
date: 2026-10-30
classes: [verdict-token, detector-fail-open]
severity: medium
status: fixed
---

# INC-0152 - An exit code 2 advisory wording in the gate runner defaulted to proceed

**Cost:** Minor: caught by a reviewer, an auditor or the lead before it shipped.

## Signature - how you recognise it

A gate returns an advisory status that a caller treats as pass.

## What happened

The Foundry exit 2 advisory, proceed wording is the default that the final release card had to override.

## Root cause

The runner default was proceed on an incomplete verdict.

## Why it was hard to see

The default is hidden until a release is attempted.

## Fix

The final card must override the default so incomplete never ships.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Override permissive defaults on the release path.
