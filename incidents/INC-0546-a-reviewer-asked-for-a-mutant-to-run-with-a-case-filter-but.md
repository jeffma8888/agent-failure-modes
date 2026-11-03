---
id: INC-0546
title: A reviewer asked for a mutant to run with a case filter, but the row runner takes one row and no filter
date: 2026-11-02
classes: [tooling-paths]
severity: low
status: mitigated
---

# INC-0546 - A reviewer asked for a mutant to run with a case filter, but the row runner takes one row and no filter

**Cost:** None. The activator ran the whole row and attributed each red to its own case line.

## Signature - how you recognise it

A review note names a run option that the runner does not have.

## What happened

A reviewer note asked to run a mutant with a case filter, because another case baseline would fail first in an unfiltered run. The row runner accepts exactly one row and no case filter. The activator ran the whole row, attributed each red to the line of its own case, and did not count the other case baseline red as a kill of any mutant.

## Root cause

The note assumed a runner feature that does not exist.

## Why it was hard to see

In a whole-row run, a red from another case looks like a kill of the mutant.

## Fix

Run the whole row, attribute each failure to its own case line, and do not count another case baseline red.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> When a runner cannot filter cases, run the whole row and attribute each red to its own case line; never credit another case baseline red as a kill.

## Related

[INC-0534](./INC-0534-a-configuration-mutation-failed-a-setup-assertion-before-any.md) [INC-0524](./INC-0524-a-root-named-a-mutation-its-assertions-could-not-see-because.md)
