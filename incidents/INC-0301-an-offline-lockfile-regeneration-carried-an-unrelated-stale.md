---
id: INC-0301
title: An offline lockfile regeneration carried an unrelated stale resolution
date: 2026-11-01
classes: [tooling-paths, stale-module]
severity: medium
status: fixed
---

# INC-0301 - An offline lockfile regeneration carried an unrelated stale resolution

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A regenerated lockfile changed entries the ruling did not cover.

## What happened

regenerating offline also rewrote a test runner resolution because a committed override was not yet reflected in the lockfile; the change was unrelated to the ruled dependency

## Root cause

regenerating offline also rewrote a test runner resolution because a committed override was not yet reflected in the lockfile; the change was unrelated to the ruled dependency

## Why it was hard to see

The regenerated file looks complete, and the extra change is easy to commit with it.

## Fix

Discard the regeneration, add only the ruled lines by hand, and prove them with a frozen offline install

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Keep a dependency change to the ruled lines and prove it with a frozen install

## Related

[INC-0188](./INC-0188-an-override-changed-the-lockfile-and-an-offline-clone-could.md)
