---
id: INC-0037
title: A liveness check built on a process-table grep counts itself
date: 2026-08-28
classes: [detector-fail-open, tooling-paths, observability]
severity: medium
status: fixed
---

# INC-0037 - A liveness check built on a process-table grep counts itself

**Cost:** A scheduled pipeline concluded on every tick that a worker was still running, and stood down, because the command asking the question matched the pattern it was asking about.

## Signature - how you recognise it

A 'something is running' check is never false. The measured count is exactly one more than the truth, and it reads one at moments when you know for certain that nothing is running.

## What happened

A driver decided whether to do work by listing the process table and matching a pattern that names its own workers. Because the shell wraps the whole pipeline in a login shell, the argument vector of the matching command itself contains the pattern - so the check always found at least one match and always reported busy.

## Root cause

A process-table scan is not an outside observer. The measuring command is a member of the population it measures, and its arguments contain the search term by construction, so the detector's blind spot is the detector.

## Why it was hard to see

It is a fail-open detector for a safety property - do not consume files a producer is still writing - so its wrong answer is the cautious one, and caution produces no error anywhere. The count is off by exactly one, which is the least suspicious possible wrong answer, and it is only wrong when the truth is ZERO, which is precisely when the check is supposed to unblock work.

## Fix

Use a matcher that excludes its own process by design rather than a text scan of the process table, or match on something the query itself cannot contain. Then prove it two-sided: assert the count is ZERO with nothing running, and non-zero with one known worker alive. A busy check that has never been observed returning false has not been tested.

## Verification

Replaced with a matcher that excludes its own process id. The count then read zero with no workers alive and the pipeline harvested on the following tick instead of standing down; both states were observed rather than inferred.

## Transferable rule

> A process-table grep counts itself - the measuring command's arguments contain the search term, so a 'something is running' check is never false. Use a matcher that excludes its own process, and prove any busy/idle check TWO-SIDED: zero when nothing runs, non-zero with one known worker. A check never seen returning false has not been tested.

## Related

[INC-0011](./INC-0011-concurrent-agent-brains-silently-starve-and-kill-each-other.md) [INC-0018](./INC-0018-fail-open-detector-pipe-alternation-matches-nothing-under-on.md) [INC-0019](./INC-0019-fail-open-detector-parsing-the-wrong-column-reports-healthy.md)
