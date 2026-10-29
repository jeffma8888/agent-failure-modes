---
id: INC-0059
title: A 'client too old' error was assumed to be client-side; the gate was on the server and keyed on the request body
date: 2026-10-29
classes: [ipc-and-env, observability]
severity: medium
status: mitigated
---

# INC-0059 - A 'client too old' error was assumed to be client-side; the gate was on the server and keyed on the request body

**Cost:** Time spent on a wrong local theory while trying to move a build engine to a newer model. No damage; the finding changed the plan from patching the existing client to building an honest one.

## Signature - how you recognise it

A vendor coding CLI says a newer version is required for a feature, and the working theory is a local version check.

## What happened

A vendor coding CLI reported that a newer version was required for a newer model. The assumption was a local check. A logging stub standing in for the model API showed the CLI did send the request. Replaying the request, changing one variable at a time, showed two layers: a request-shape incompatibility (a deprecated reasoning parameter), then a server-side version check that reads markers inside the request body, so changing the user-agent header changed nothing.

## Root cause

The error text described a symptom ('too old') and the location was inferred from it. Without locating the check, every workaround targeted the wrong layer.

## Why it was hard to see

The message reads like a local complaint. A server gate keyed on body content is invisible from the client's side, and a header change that does nothing looks like a failed experiment, not a finding.

## Fix

Locate the gate first: stand up a stub endpoint to see what is actually sent, then replay with one variable changed at a time. Then build an honest client of your own rather than patching or impersonating the old one.

## Verification

The stub showed the request leaving the client; the replays separated the shape error from the server-side check.

## Transferable rule

> Before working around a version or access error, find where the check lives. A server-side gate on client identity is a decision for the human who owns the access, never something to strip or fake.

## Related

[INC-0053](./INC-0053-a-command-line-agent-silently-ran-an-older-model-than-assume.md) [INC-0036](./INC-0036-a-relaunch-that-bypasses-the-canonical-launcher-runs-healthy.md)
