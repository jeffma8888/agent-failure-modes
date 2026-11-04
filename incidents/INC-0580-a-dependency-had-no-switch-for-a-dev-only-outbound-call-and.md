---
id: INC-0580
title: A dependency had no switch for a dev-only outbound call, and the implementer stopped instead of guessing
date: 2026-11-04
classes: [spec-and-scope]
severity: low
status: mitigated
---

# INC-0580 - A dependency had no switch for a dev-only outbound call, and the implementer stopped instead of guessing

**Cost:** None. The work paused for a ruling, and no dependency was patched.

## Signature - how you recognise it

A requirement to disable an outbound call has no switch in the installed dependency.

## What happened

The installed framework version has no switch for its registry version check. The implementer stopped. The lead read the same source and found that the version check is called only from the development hot reloader bundles, and that the router server loads the development bundler only in development mode, with a comment that production startup does not query advisories. The lead ruled to observe the production server, not a patched launch option, because patching a dependency on every upgrade or masking fetch hides the call instead of removing it, and the shipped app runs the production server. The row was narrowed to telemetry only, with red first and a runtime green with the same unedited observer under the development server, where registry attempts remain expected and are reported, not hidden.

## Root cause

The requirement assumed every outbound call can be switched off in every mode.

## Why it was hard to see

The call exists only in development mode, which the first design did not separate from production.

## Fix

Check which mode reaches the call, and put the zero-outbound check on the production server.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Do not patch a dependency or mask fetch to silence a dev-only call; find which mode reaches it, and place the zero-outbound check where the shipped app runs.

## Related

[INC-0562](./INC-0562-the-first-real-run-of-a-new-egress-observer-on-unchanged-mai.md) [INC-0569](./INC-0569-denying-unexplained-loopback-connects-in-an-egress-observer.md)
