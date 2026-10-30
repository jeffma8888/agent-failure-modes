---
id: INC-0122
title: A digest present anywhere in a manifest was taken as proof it belonged to its file
date: 2026-10-30
classes: [identity-and-keying, detector-fail-open]
severity: medium
status: fixed
---

# INC-0122 - A digest present anywhere in a manifest was taken as proof it belonged to its file

**Cost:** Minor: caught by a re-check, an audit or review before it shipped.

## Signature - how you recognise it

A check finds the digest somewhere in the manifest and passes.

## What happened

A digest present anywhere in a manifest did not prove it belonged to its file, so swapped or misplaced digests could pass.

## Root cause

The check tested membership, not the path-to-digest pairing.

## Why it was hard to see

Every digest is valid and present, only misassigned.

## Fix

Bind each path to its own digest.

## Verification

Checked by the reviewer or lead who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Verify pairs, not membership.

## Related

[INC-0080](./INC-0080-two-writers-used-the-same-short-question-id-for-different-ga.md)
