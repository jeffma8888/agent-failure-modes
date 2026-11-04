---
id: INC-0623
title: A helper piped to tail and followed by && ran the next step although the helper failed, because a pipeline's status is its last command's
date: 2026-11-04
classes: [false-green]
severity: medium
status: mitigated
---

# INC-0623 - A helper piped to tail and followed by && ran the next step although the helper failed, because a pipeline's status is its last command's

**Cost:** A next step ran after a failed helper, caught on reading the output.

## Signature - how you recognise it

A chain continues after a step that printed a failure, because a pipe hid its status.

## What happened

A command of the form helper piped to tail, then &&, then the next step, ran the next step although the helper failed. A pipeline's exit status is that of its last command, so the status of tail, which succeeded, decided the chain. This recurred within the hour of the earlier gate-chain slip.

## Root cause

A pipe replaces the helper's status with the status of the last command.

## Why it was hard to see

Adding tail to shorten the output looks harmless and does not look like a gate.

## Fix

Check the helper's status with pipefail or in a separate call, and do not place && after a pipe to tail.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Never put && after a pipe to tail; check the helper's own status with pipefail or a separate call.

## Related

[INC-0620](./INC-0620-a-publish-gate-chain-ran-a-build-script-at-a-path-that-does.md)
