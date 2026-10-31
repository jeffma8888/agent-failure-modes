---
id: INC-0144
title: Expected lifecycle refusals were mixed with static findings in a sweep
date: 2026-10-30
classes: [observability, detector-fail-closed]
severity: medium
status: fixed
---

# INC-0144 - Expected lifecycle refusals were mixed with static findings in a sweep

**Cost:** Minor: caught by an engineer, reviewer or the lead before it shipped.

## Signature - how you recognise it

A sweep report cannot tell an intended refusal from a real finding.

## What happened

An N-02b sweep mixed expected lifecycle refusals with static findings.

## Root cause

Both kinds of output went to one list.

## Why it was hard to see

A refusal looks like a failure.

## Fix

Keep expected lifecycle refusals separate from static findings.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Report expected refusals apart from real findings.
