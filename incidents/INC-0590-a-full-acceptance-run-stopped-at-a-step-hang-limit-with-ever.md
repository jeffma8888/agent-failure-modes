---
id: INC-0590
title: A full acceptance run stopped at a step hang limit with every reported case passing, and the budget was raised from measured times
date: 2026-11-04
classes: [stage-timeout]
severity: medium
status: mitigated
---

# INC-0590 - A full acceptance run stopped at a step hang limit with every reported case passing, and the budget was raised from measured times

**Cost:** One full run produced no verdict for its later steps (integration, build, server, smoke and e2e did not complete), and a rerun at the same load would have hit the same limit.

## Signature - how you recognise it

A step stops at its hang limit after a partial report in which every case passed, and the wrapper exits 0.

## What happened

The integration step stopped at its hang limit (60 s budget times 3, 180002 ms) with 10 of about 42 files reported, all passing. Earlier steps were green. The step runs its files one at a time, two new files had been added, and under heavier load (load1 12.5 at admission, 17.9 at step start) the same files ran 1.5 to 2 times slower than in an earlier run: 83.4 s against 46.4 s, 9.4 s against 6.5 s, 8.9 s against 4.8 s. The lead called the run neither red nor green and did not rerun it. The step budget was raised from 60 to 120 s (hang limit 360 s) with a comment citing the measurements, and the run waits for the merge.

## Root cause

The step budget was set at lighter load and fewer files, and the work grew while the budget stayed.

## Why it was hard to see

The report showed only passing cases and a zero exit from the wrapper, which looks green. Rerunning at the same load would have repeated the stop.

## Fix

Judge the run from step records, call it neither red nor green, raise the budget from measured per-file times with the measurements in a comment, and rerun only after the budget changes.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> When a step stops at its hang limit with all reported cases passing, do not call it green or red and do not rerun into the same limit; raise the budget from measured times, cite them, then rerun.

## Related

[INC-0348](./INC-0348-a-deadline-set-at-twice-the-slowest-sample-was-budgeted-agai.md) [INC-0551](./INC-0551-a-test-that-passed-alone-at-about-63-percent-of-its-timeout.md)
