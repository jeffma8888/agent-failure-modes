---
id: INC-0162
title: A chained amend reworded the previous commit after a failed revert
date: 2026-10-30
classes: [vcs-destruction, tooling-paths]
severity: medium
status: fixed
---

# INC-0162 - A chained amend reworded the previous commit after a failed revert

**Cost:** Minor: a previous commit was reworded by mistake.

## Signature - how you recognise it

A revert failed on an invalid flag and the next chained step changed the wrong commit.

## What happened

A revert used an invalid flag and failed, and the chained amend then reworded the previous commit instead of the revert.

## Root cause

The amend was chained without checking that the revert succeeded.

## Why it was hard to see

The chain continued silently after the failure, and HEAD still looked plausible.

## Fix

Repair the reworded commit and redo the revert with a valid flag.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Chain an amend only with && after a step whose success is checked, and confirm the HEAD subject before amending.

## Related

[INC-0147](./INC-0147-a-moved-history-row-was-silently-modernized-instead-of-stayi.md)
