---
id: INC-0495
title: The acceptance run lacked an environment variable that the branch run and the full suite set
date: 2026-11-02
classes: [test-isolation]
severity: low
status: mitigated
---

# INC-0495 - The acceptance run lacked an environment variable that the branch run and the full suite set

**Cost:** Minor: one extra failing test in the first acceptance run and a re-run.

## Signature - how you recognise it

The only new failure in the acceptance run was a test that throws when one environment variable is absent.

## What happened

After a merge, the acceptance run showed a sixth unit failure beyond the five baseline names. The new test failed only because the acceptance script gave the unit tier no media directory variable, and the code under test throws without it. The branch run and the full suite both set it. With the variable set, the unit tier showed the same five baseline failures and no new one. The script now gives the unit tier a scratch value, as the full suite does.

## Root cause

The acceptance run and the runs it was compared with differed in environment, and the difference was not recorded.

## Why it was hard to see

A new failing test in a freshly merged change looks like a defect of the merge, and the missing variable was set by default in the other runs.

## Fix

Give the acceptance run the same environment the full suite gives, and record the environment of every run that is compared.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Record the environment of every run you compare, and give the acceptance run the same environment the full suite gives.

## Related

[INC-0412](./INC-0412-a-whole-unit-re-run-showed-five-failures-in-unrelated-files.md)
