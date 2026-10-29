---
id: INC-0046
title: A script with external writes was only dry-run for its first step, and only write-last ordering made its failure harmless
date: 2026-10-28
classes: [tooling-paths, vcs-destruction]
severity: low
status: fixed
---

# INC-0046 - A script with external writes was only dry-run for its first step, and only write-last ordering made its failure harmless

**Cost:** None incurred. A history-swap script aborted on an invalid command flag. Because every external write came after every fallible local step, nothing external had happened; with the order reversed, the remote and the working copy would have diverged.

## Signature - how you recognise it

A multi-step script that pushes or resets exits non-zero partway through its first real run, having only been rehearsed on its hardest step.

## What happened

A script rewrote history, pushed it, and reset a working copy onto it. A cherry-pick step used a flag that does not exist, and under errexit the script aborted. Only the first step, the rewrite, had been dry-run; the rest had never executed end to end.

## Root cause

The rehearsal covered the step judged riskiest rather than the whole script, so a trivial typo in an unrehearsed step was the first thing the real run met.

## Why it was hard to see

The hard part was tested, which feels like having tested the script. A simple invocation error in a later step looks too trivial to rehearse.

## Fix

Corrected the invocation and reran. The script already checked a deterministic base commit before acting and ordered all fallible local steps before any external write, which is why the abort was harmless.

## Verification

The rerun completed with the expected base-commit check passing and the external writes happening only after every local step had succeeded.

## Transferable rule

> In any script that writes externally, order every fallible local step first and every external write last, and dry-run the WHOLE script end to end against scratch copies before the real run, not just its hardest step.

## Related

[INC-0044](./INC-0044-pushing-a-local-repository-to-a-new-remote-publishes-its-who.md) [INC-0014](./INC-0014-a-revert-on-failure-loop-destroys-uncommitted-human-work-in.md)
