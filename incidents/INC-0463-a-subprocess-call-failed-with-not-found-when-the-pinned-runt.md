---
id: INC-0463
title: A subprocess call failed with not found when the pinned runtime directory was missing from the search path, and the first run showed five extra failures
date: 2026-11-02
classes: [ipc-and-env]
severity: low
status: fixed
---

# INC-0463 - A subprocess call failed with not found when the pinned runtime directory was missing from the search path, and the first run showed five extra failures

**Cost:** A rerun with the search path set.

## Signature - how you recognise it

Extra failures appeared in the first run.

## What happened

a test spawned the package manager and failed with a not found error because the directory of the pinned runtime was not on the search path; the first run showed five extra failures that were not product defects

## Root cause

the test shell did not carry the runtime search path

## Why it was hard to see

Five failures looked like regressions until the first error name was read.

## Fix

put the pinned runtime directory first on the search path in the command that runs the test, and read the first failure name before counting reds

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Put the pinned runtime directory on the search path in the same command that runs the tests; a not found error from a spawned tool is an environment fault, not a product failure

## Related

[INC-0106](./INC-0106-deleting-postgresql-environment-variables-left-client-tools.md) [INC-0256](./INC-0256-evidence-commands-ran-on-a-shimmed-runtime-instead-of-the-pi.md) [INC-0369](./INC-0369-a-bare-syntax-check-resolved-to-a-different-runtime-that-ign.md)
