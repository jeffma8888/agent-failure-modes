---
id: INC-0017
title: A killed detached loop resurrects with a new PPID
date: 2026-08-05
classes: [delegation, ipc-and-env]
severity: medium
status: fixed
---

# INC-0017 - A killed detached loop resurrects with a new PPID

**Cost:** About 90 minutes of confusion after a kill; the loop came back detached and continued producing unauthorized output.

## Signature - how you recognise it

You kill the loop's pid. Later, `ps` shows a fresh pid with ppid 1, running the same loop script, on a new sleep-backoff cycle.

## What happened

A detached loop was killed via SIGTERM against its pid. Around 90 minutes later a new pid appeared for the same script, reparented to init (ppid 1), alive and in a sleep-backoff cycle. It had been restarted by a scheduled task or a supervisor script the operator did not know about.

## Root cause

The loop was reachable from more than one launcher. The kill removed the running process but not the source that spawned it. Reparenting to init is a healthy pattern for a well-behaved daemon, so nothing was 'wrong' - the operator simply hunted the wrong controller.

## Why it was hard to see

There is often no visible link between the killed pid and its next incarnation. Watching `ps -ef | grep <script>` misses the launcher.

## Fix

The durable off switch is removing the REQUIRED INPUT the loop reads at the top of every iteration - a STOP file the script honors, or the story queue it consumes. This forces a graceful exit rather than trying to out-kill a re-spawner. Look for the launcher: (a) same argv on the restarted process = something is auto-resurrecting it (search cron, launchd/systemd, supervisor scripts); (b) different argv = a human or another session deliberately relaunched with new parameters. THAT diff is the tell.

## Verification

After the STOP file was in place, the next restart honored it and exited cleanly on its own.

## Transferable rule

> To stop a well-behaved detached loop, remove the input it polls (a STOP file it honors), not just its pid - a supervisor or scheduler can re-launch a killed pid. Same argv on a new pid = auto-resurrection; different argv = a fresh authorized launch. Hunt the launcher accordingly, and leave a documented STOP so you and the other session do not fight over the process.

## Related

[INC-0016](./INC-0016-anti-delegation-clause-must-forbid-scaffold-a-loop-too.md)
