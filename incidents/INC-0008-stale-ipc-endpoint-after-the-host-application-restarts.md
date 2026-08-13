---
id: INC-0008
title: Stale IPC endpoint after the host application restarts
date: 2026-08-03
classes: [ipc-and-env]
severity: high
status: mitigated
---

# INC-0008 - Stale IPC endpoint after the host application restarts

**Cost:** Every step instant-failed with a ~500-byte CLI help-text log; the dispatcher sat alive-but-broken for hours before the failure mode was recognized.

## Signature - how you recognise it

Every step instantly fails (same-second timing, not a timeout). Attempt logs are ~500 bytes containing CLI help text ('did not match ... check syntax'), not the timeout string. The process looks alive.

## What happened

The agent CLI was served by a running host application over a Unix socket at a path derived from the host's PID. When the host app restarted the PID changed and the socket rotated. Any long-running loop that had inherited the old socket path in its environment continued running - and every one of its child invocations failed instantly with the CLI's built-in 'endpoint not reachable' help text.

## Root cause

The dispatcher spawned children via `subprocess.run(cmd, ...)` with NO `env=` argument, so every child inherited the environment captured at launch. That endpoint pointed at a socket that no longer existed.

## Why it was hard to see

The process was alive. A naive is-it-running check returned yes. Only the specific log-content signature revealed the failure: ~500 bytes, CLI help text, same-second timing.

## Fix

Resolve the endpoint at each child spawn instead of capturing it once. On spawn, glob candidate sockets by mtime, and for the newest do a 0.5s `connect()` probe to confirm a live listener. If it answers, pass that path in the child's env; if none answer, leave the inherited value and warn (never make a working setup worse). Do NOT rely on `os.kill(pid, 0)` against a PID embedded in the socket filename - PID reuse silently returns 'alive' on an unrelated live process.

## Verification

After the fix, a synthetic app restart in the same session left the dispatcher's next spawn healthy. Regression test: bind a real listener and a non-listening socket side by side in a tmp dir and confirm the probe selects the listener.

## Transferable rule

> A subprocess spawned with no explicit env inherits every environmental identifier the parent captured at launch - including socket paths tied to a PID that can change. When the parent long outlives its environmental assumptions, resolve identifiers at spawn time with an ACTIVE probe (connect, not exists). Never trust a PID from a filename against PID reuse.

## Related

[INC-0009](./INC-0009-interactive-only-credential-expiry-silently-stalls-unattende.md)
