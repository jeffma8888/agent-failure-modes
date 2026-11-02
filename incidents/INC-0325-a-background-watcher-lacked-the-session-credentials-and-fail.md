---
id: INC-0325
title: A background watcher lacked the session credentials and failed every poll
date: 2026-11-01
classes: [ipc-and-env, observability]
severity: medium
status: fixed
---

# INC-0325 - A background watcher lacked the session credentials and failed every poll

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A watcher reported nothing because every poll was refused.

## What happened

a background watcher meant to report worker run states ran without the session's credentials, so it could not reach the coordinator and failed every poll

## Root cause

a background watcher meant to report worker run states ran without the session's credentials, so it could not reach the coordinator and failed every poll

## Why it was hard to see

A watcher that fails quietly looks the same as nothing to report.

## Fix

Check what a background watcher can authenticate to before relying on it, keep authenticated checks in live turns, and never write a session secret to disk to make it work

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Check what a background watcher can authenticate to before relying on it; keep authenticated checks in live turns and never write a session secret to disk

## Related

[INC-0009](./INC-0009-interactive-only-credential-expiry-silently-stalls-unattende.md) [INC-0068](./INC-0068-a-retry-ladder-wrapped-the-model-call-but-not-the-credential.md)
