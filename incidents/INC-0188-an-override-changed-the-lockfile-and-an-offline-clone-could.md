---
id: INC-0188
title: An override changed the lockfile and an offline clone could not install it
date: 2026-10-30
classes: [tooling-paths, ipc-and-env]
severity: medium
status: fixed
---

# INC-0188 - An override changed the lockfile and an offline clone could not install it

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

An offline install failed for lack of supply-chain metadata.

## What happened

An override changed the lockfile, and its supply-chain metadata had never been fetched online, so an offline clone could not install it.

## Root cause

An override changed the lockfile, and its supply-chain metadata had never been fetched online, so an offline clone could not install it.

## Why it was hard to see

The metadata was assumed to be cached.

## Fix

Warm it with a frozen install in a scratch clone, not with a fetch in a populated checkout

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Warm override metadata with a frozen install in a scratch clone before any offline install

## Related

[INC-0178](./INC-0178-a-production-build-dirtied-the-tree-and-an-example-role-was.md)
