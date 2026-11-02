---
id: INC-0499
title: The first defect of a kind prompted an audit of the whole kind, which found a second
date: 2026-11-02
classes: [spec-and-scope]
severity: medium
status: mitigated
---

# INC-0499 - The first defect of a kind prompted an audit of the whole kind, which found a second

**Cost:** None incurred beyond one extra fix row: the second defect was found by a static audit before any release.

## Signature - how you recognise it

One hard-coded external host was found in a page that must work offline, and a second, silent one existed on the server.

## What happened

A browser run found an admin editor fetching a public content delivery host, which the admin must not depend on. Instead of fixing only that field, the team ordered a static audit of every hard-coded non-local URL that an admin page or the server can reach at runtime. The audit found a second external origin: server-side telemetry that is on by default and posts to a public host at server start and on admin access, because the configuration omitted the switch that turns it off. A third origin, an avatar service, was already disabled by the configuration. The audit was a source reading, not a network observation, and said so. A unit test on the built configuration now pins the switch.

## Root cause

The first fix would have covered one instance of a class, and the class was defined by what the product may reach, not by the field that happened to be seen first.

## Why it was hard to see

The second instance made no visible request in the browser, was on by default, and the configuration was correct on its face except for a missing line.

## Fix

Audit the whole class from installed source, fix every instance found, pin each with a test on the built configuration or a browser run, and state that the audit is source reachability and not an observed guarantee.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> When one instance of a defect class appears, audit for the whole class before fixing only the instance.

## Related

[INC-0498](./INC-0498-the-first-browser-run-of-new-end-to-end-cases-found-two-prod.md) [INC-0494](./INC-0494-the-first-real-click-around-found-product-defects-that-many.md)
