---
id: INC-0574
title: Two mutation drivers stopped before the restored green because they matched a log-tail string the harness does not print
date: 2026-11-04
classes: [tooling-paths]
severity: low
status: mitigated
---

# INC-0574 - Two mutation drivers stopped before the restored green because they matched a log-tail string the harness does not print

**Cost:** Two restored-green runs were missed and one extra sanctioned invocation was needed for each.

## Signature - how you recognise it

A driver waits for a text in a log tail, and the text is never printed or is colored.

## What happened

One driver stopped after its expected red and a correct restore, before the restored green, because a literal grep missed terminal color codes. A later driver stopped at the same point on a log-tail string that the harness does not print. Each needed one corrected same-scope invocation, with the first attempt kept as evidence. The rulings required judging exit codes and not log tails, with escapes stripped for matching only where text must be matched, and a check that the product file hash equals the head hash before the green run.

## Root cause

The stop condition read output text instead of the exit code.

## Why it was hard to see

Output text depends on formatting and on the harness, which the driver author does not control.

## Fix

Judge exit codes, strip escapes only for matching, and check the product hash before the restored green.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A mutation driver must judge exit codes, not log tails; if text must be matched, strip escapes for matching only.

## Related

[INC-0561](./INC-0561-a-verifier-matched-plain-text-in-colored-logs-and-stopped.md)
