---
id: INC-0036
title: A relaunch that bypasses the canonical launcher runs healthy but unobservable, and the diagnostic inverts
date: 2026-08-23
classes: [observability, ipc-and-env]
severity: medium
status: fixed
---

# INC-0036 - A relaunch that bypasses the canonical launcher runs healthy but unobservable, and the diagnostic inverts

**Cost:** One wasted drain-and-relaunch cycle, each drain costing its in-flight iteration, plus a false alarm: the freshness check reported that the restart had failed at the moment it had just succeeded - the reading most likely to trigger yet another destructive restart.

## Signature - how you recognise it

The process is alive with the right parent and the right arguments, but the log has no launch banner, and every freshness or liveness check that reads that log reports a problem. Restarting again reproduces the same silence.

## What happened

A long-running supervisor writes its log by duplicating its own standard output onto a file descriptor at launch, which the canonical launch script arranges. A hand-rolled relaunch started the same entry point directly, with output sent to a null device. The process ran correctly and did real work, but produced no log at all - so the verb that reads the log for a launch banner reported that no restart had happened, about a restart that had.

## Root cause

The launcher was not a convenience wrapper; it was part of the observability contract. Reproducing its command without reproducing the environment it establishes yields a process that is functionally correct and epistemically invisible.

## Why it was hard to see

Every direct check passes - the process exists, the parent is right, the arguments match - so the natural conclusion is that the diagnostic is broken and can be ignored. The failure is also self-erasing: with no log there is nothing to point at, and the most obvious remedy is another restart, which in a loop that reverts on failure is the operation with the highest destructive potential.

## Fix

Relaunch only through the canonical launcher, and make the restart procedure assert the ARTIFACT the diagnostic reads - that a launch banner naming the expected roster appears in the log after the restart timestamp - rather than asserting the process exists. If a hand-rolled start is unavoidable, reproduce the output plumbing first and verify the banner before believing anything else.

## Verification

After relaunching through the launcher, the log carried the banner with the expected roster, the freshness verb reported up to date with zero shipped-but-inert commits, and the process was confirmed detached under the expected parent. The earlier warning was then traced to the missing banner rather than to the restart.

## Transferable rule

> A launcher script is often part of the observability contract, not a convenience. Reproducing its command without its environment yields a process that works and cannot be seen, and every log-reading check then reports a failure that did not happen. Relaunch through the canonical entry point, and verify a restart by asserting the artifact your diagnostics read, not that the process exists.

## Provenance

Where this was observed, so the claim is checkable rather than anecdotal:

- https://github.com/jeffma8888/agent-foundry - `launch_dispatcher.sh`, the dispatcher's own stdout redirection, and the `live-lag` verb that reads the launch banner out of the log.

## Related

[INC-0008](./INC-0008-stale-ipc-endpoint-after-the-host-application-restarts.md) [INC-0017](./INC-0017-a-killed-detached-loop-resurrects-with-a-new-ppid.md) [INC-0021](./INC-0021-stale-module-import-shipped-is-not-live.md)
