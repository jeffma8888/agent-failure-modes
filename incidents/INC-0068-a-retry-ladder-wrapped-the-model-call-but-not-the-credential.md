---
id: INC-0068
title: A retry ladder wrapped the model call but not the credential helper on the same path, so one helper blip became a long hold
date: 2026-10-29
classes: [ipc-and-env, observability]
severity: high
status: mitigated
---

# INC-0068 - A retry ladder wrapped the model call but not the credential helper on the same path, so one helper blip became a long hold

**Cost:** In one afternoon: five stage deaths, five 30-minute holds (about 2.5 hours idle), and a launcher preflight that refused a relaunch on the same transient failure.

## Signature - how you recognise it

A credential helper that passes every manual probe exits non-zero about once an hour inside the loop, and the loop reports an expired session.

## What happened

A stage engine retried authentication errors from the model API with a backoff ladder, but treated one non-zero exit of its credential helper as fatal. Each blip killed a stage, the dispatcher classified it as an expired session and held for 30 minutes, and the launcher's single-attempt preflight refused to relaunch on the same blip. The helper itself worked in eight consecutive clean manual runs.

## Root cause

The retry ladder covered one external call and not the others on the path to a model turn. A transient failure of a helper was also labelled with a permanent-failure name, so the scheduler waited for a human who was not needed. The helper's real cause was a hard 2-second connect timeout to its credential backend that trips about once an hour.

## Why it was hard to see

Manual probes of the helper were clean, so the helper was 'known good'. The log carried a classification ('auth failed'), not the failing attempt's stderr.

## Fix

A retry wrapper (3 attempts, delays of 0, 2 and 5 seconds, output emitted only on success, failed attempts' stderr logged with secrets redacted) was substituted as the configured credential command and activated by a clean-point restart. The proper fix, retry inside the engine's own credential provider, was filed for the engine's owner.

## Verification

The wrapper's log captured the cause on its first trigger, two minutes after it went live: a connect timeout in the helper, and the retry 4 seconds later succeeded, so that iteration shipped instead of taking a hold. The engine-side fix is not verified here.

## Transferable rule

> A retry ladder must cover every external call on the path to a model turn, including helpers that fetch credentials. When a dependency that passes manual probes fails in the loop, log the failing attempt's stderr instead of a classification, and never let a one-shot preflight decide whether an unattended system restarts.

## Related

[INC-0009](./INC-0009-interactive-only-credential-expiry-silently-stalls-unattende.md) [INC-0049](./INC-0049-a-cached-credential-made-a-dependency-look-optional-and-the.md) [INC-0005](./INC-0005-a-killed-step-with-no-verdict-token-is-read-as-reverted.md)
