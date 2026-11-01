---
id: INC-0257
title: Moving the home directory broke a launch that found its cache through it
date: 2026-11-01
classes: [ipc-and-env, test-isolation]
severity: medium
status: fixed
---

# INC-0257 - Moving the home directory broke a launch that found its cache through it

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

The cache location was implicit.

## What happened

Moving HOME for isolation broke a launch because the package-manager runtime cache was found through HOME.

## Root cause

Moving HOME for isolation broke a launch because the package-manager runtime cache was found through HOME.

## Why it was hard to see

The dependency on HOME was not written anywhere.

## Fix

Name every home-resolved cache explicitly

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Name every home-resolved cache explicitly when moving HOME for isolation

## Related

[INC-0188](./INC-0188-an-override-changed-the-lockfile-and-an-offline-clone-could.md)
