---
id: INC-0500
title: One load gate sized for full runs was applied to every run, and scoped runs were refused while the real load producer went unexamined
date: 2026-11-02
classes: [stage-timeout]
severity: medium
status: mitigated
---

# INC-0500 - One load gate sized for full runs was applied to every run, and scoped runs were refused while the real load producer went unexamined

**Cost:** Scoped single-row runs were refused repeatedly (one engineer three times, another twice) and the reds that gate every fix stalled; one admitted red was a timeout, a wasted run.

## Signature - how you recognise it

A single load threshold chosen for full-suite runs refuses small scoped runs once several teammates work in parallel.

## What happened

One load limit, sized for full-suite runs, was applied to every database and browser run. With more teammates in parallel, scoped single-row runs were refused again and again at readings only moderately above the limit, and the reds that gate each fix waited. The first admitted red was a timeout, which counts as a wasted run and not as a red. The load was then examined and found to come mostly from the system file indexer working through the installed packages of each new worktree, with several setups overlapping, not from the tests.

## Root cause

The gate was sized for the heaviest class of run and applied to the lightest, and the team tightened or waited on the load without first finding what produced it.

## Why it was hard to see

A load average does not say who produced it, and a refusal looks like a correct safety stop, so the cost of a gate sized too tightly shows up only as stalled work, not as a failure.

## Fix

Gate by run class: scoped runs under a higher threshold, full runs and comparison walks under the lower one. Keep the evidence rules unchanged: a timeout, setup failure or harness error at any load is a wasted run, not a red and not a pass. Create new worktrees in a folder the system file indexer skips, and ask the owner to turn indexing off for project folders.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Size an admission gate to the class of run it protects, and find what is actually producing the load before tightening or waiting on it.

## Related

[INC-0427](./INC-0427-a-host-load-spike-came-from-operating-system-daemons-not-the.md) [INC-0393](./INC-0393-a-load-reading-taken-minutes-before-a-launch-was-stale-and-t.md)
