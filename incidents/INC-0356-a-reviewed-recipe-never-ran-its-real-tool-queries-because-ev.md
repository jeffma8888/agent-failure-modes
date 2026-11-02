---
id: INC-0356
title: A reviewed recipe never ran its real tool queries because every control stubbed them
date: 2026-11-01
classes: [false-green, tooling-paths]
severity: medium
status: fixed
---

# INC-0356 - A reviewed recipe never ran its real tool queries because every control stubbed them

**Cost:** One scheduled authorized run was lost before setup.

## Signature - how you recognise it

A recipe passed its dry run, control run and copy cases, then its first real run stopped in preparation on an unsupported option.

## What happened

an acceptance recipe passed its dry run, its control run, six exit controls and 26 copy cases, all with stubbed package manager calls; the first real authorized run stopped in preparation because one query passed an option the pinned manager version does not support ("Unknown option"), so a scheduled run was lost before setup

## Root cause

every control replaced the real tool calls with stubs, so the commands themselves were never executed against the pinned tool version before the authorized run

## Why it was hard to see

Many green controls and two reviews made the recipe look proven, but they all tested its logic and none tested its commands.

## Fix

A real-binary preflight mode that executes every read-only query the preparation step uses, in the real environment, and a real run that refuses to start without a passing preflight at the same recipe digest

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A stubbed control proves the recipe's logic, not its commands; before an authorized run, execute every real read-only command once against the pinned tool versions

## Related

[INC-0104](./INC-0104-a-process-group-kill-test-used-single-process-stubs-so-signa.md) [INC-0046](./INC-0046-a-script-with-external-writes-was-only-dry-run-for-its-first.md) [INC-0256](./INC-0256-evidence-commands-ran-on-a-shimmed-runtime-instead-of-the-pi.md) [INC-0351](./INC-0351-a-physical-copy-of-a-shared-package-store-carried-its-regist.md)
