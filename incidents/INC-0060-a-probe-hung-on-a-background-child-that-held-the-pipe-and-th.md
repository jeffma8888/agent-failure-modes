---
id: INC-0060
title: A probe hung on a background child that held the pipe, and the timeout wrapper it relied on did not exist
date: 2026-10-29
classes: [tooling-paths, observability]
severity: low
status: fixed
---

# INC-0060 - A probe hung on a background child that held the pipe, and the timeout wrapper it relied on did not exist

**Cost:** A hung diagnostic session. The 'command not found' error that explained it had been written to a log nobody read until the hang.

## Signature - how you recognise it

A shell one-liner starts a long-lived server with a trailing background marker inside a captured pipeline, and wraps the client in a timeout command.

## What happened

A one-liner started a stub server in the background inside a pipeline, so the pipeline waited forever on the server's inherited standard output. Separately, the client under test never ran, because the timeout command is not installed by default on this operating system, and the shell printed 'command not found' into a log.

## Root cause

Two shell-level assumptions: that backgrounding detaches a child from the pipeline's pipe, and that a common wrapper exists on the target OS. Neither was checked, and the one error that was emitted went somewhere unread.

## Why it was hard to see

The first failure looks like the client hanging, so attention goes to the client, which never actually ran.

## Fix

Drive multi-process probes from one script in a language with explicit process control: the server started with its streams sent to the null device, the client run with a timeout argument, and the server killed in a finally block.

## Verification

The scripted probe terminated on its own and reported the client's real outcome.

## Transferable rule

> Never background a long-lived process inside a captured pipeline, and confirm every wrapper command exists on the target OS before relying on it. Read the error stream before theorising about the hang.

## Related

[INC-0037](./INC-0037-a-liveness-check-built-on-a-process-table-grep-counts-itself.md) [INC-0024](./INC-0024-backtick-command-substitution-in-a-heredoc-corrupts-and-exec.md)
