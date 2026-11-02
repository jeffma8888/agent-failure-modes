---
id: INC-0365
title: A delegated test run needed login and logout, which delegates may not do, so the lead ran the pinned script
date: 2026-11-01
classes: [ipc-and-env, delegation]
severity: low
status: fixed
---

# INC-0365 - A delegated test run needed login and logout, which delegates may not do, so the lead ran the pinned script

**Cost:** Minor: the run waited for the lead; nothing was weakened or lost.

## Signature - how you recognise it

A delegate prepared a browser walk that logs in and out but the runtime refused it for delegated agents.

## What happened

a delegated QA agent prepared a browser click-around script that logs in as a test account, walks pages and logs out. The runtime classifies login and logout as externally visible writes and refuses them for delegated agents, so the delegate could not run its own script. The lead ran the exact script, pinned by its hash, under lead authority and handed the artifacts back for the report

## Root cause

the test needed an action above the delegate's permission ceiling, and the delegate had no sanctioned route to the result other than the lead

## Why it was hard to see

The script itself was fine and validated statically, so the only blocker was who may run it, and the easy ways out (skip the login steps, or report the result unobserved) would have weakened or faked the test.

## Fix

The delegate writes and statically validates the script and pins its hash and exact command; the lead runs it unchanged and returns the artifacts; the report separates what was validated statically from what the lead observed

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> When a test needs an action above a delegate's permission ceiling, the delegate writes and statically validates the script and pins its hash and exact command; the lead runs it unchanged and returns the artifacts; never weaken the test to fit the ceiling, and never let the delegate claim a result it did not observe

## Related

[INC-0103](./INC-0103-a-teammate-could-not-run-a-destructive-git-command-even-when.md) [INC-0200](./INC-0200-a-sandbox-permission-failure-was-at-risk-of-reading-as-a-cod.md) [INC-0050](./INC-0050-bundling-safe-local-steps-with-an-approval-gated-step-loses.md) [INC-0367](./INC-0367-a-brief-for-a-database-backed-run-omitted-the-test-database.md)
