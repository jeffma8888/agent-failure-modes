---
id: INC-0042
title: Self-review does not catch recurrences of your own documented rules
date: 2026-09-01
classes: [false-green, observability, delegation]
severity: high
status: mitigated
---

# INC-0042 - Self-review does not catch recurrences of your own documented rules

**Cost:** Three defects survived a deliberate self-review of a decision document and were found by an independent verifier minutes later. All three were recurrences of failure families already written down in the reviewer's OWN standing rules.

## Signature - how you recognise it

An artifact passes its author's careful self-review, and an independent pass immediately finds defects that match rules the author can quote from memory.

## What happened

A document was self-reviewed against a written checklist and then handed to an independent verifier, which found three defects. Each was a known family: an unqualified superlative computed over the wrong population (a maximum taken over one subset, stated as if over the whole), and an aggregator restatement of a primary source treated as independent corroboration.

## Root cause

The context that produced the defect is the context grading it. Self-review re-reads the artifact with the same framing, the same assumptions and the same blind spots that generated it, so a rule can be perfectly known and still not APPLIED - knowing and executing are different capabilities, and only the second one is being tested at review time.

## Why it was hard to see

It is invisible from the inside, by construction: the author's confidence is highest exactly where the shared assumption sits. Writing the rule down does not help, because the failure is not ignorance of the rule. And each individual defect is small enough to look like polish rather than a defect class.

## Fix

Add an INDEPENDENT verifier slot with no access to the author's reasoning - only the artifact and the primary sources - and give it a bounded, enumerable brief (check these N claims, one row per claim). Do NOT respond to a recurrence by rewriting the rule: record it as a receipt that the rule keeps recurring, which is evidence about the ENFORCEMENT POINT, not about the wording.

## Verification

The verifier slot found three defects in an artifact that had just passed self-review, and every one mapped to an existing documented family - which is the measurement that argues for the slot rather than for another rule. Conclusions survived in all three cases; the SENTENCES did not, which is why a reader-facing artifact needs a reader-independent check.

## Transferable rule

> Self-review is graded by the context that produced the defect, so a rule can be perfectly known and still not applied - knowing and executing are different capabilities. Use an independent verifier with access to the artifact and primary sources but NOT your reasoning, and treat a recurrence as evidence about the enforcement point, never as a reason to reword the rule.

## Related

[INC-0041](./INC-0041-a-verifier-that-lived-and-answered-can-still-deliver-an-unus.md) [INC-0001](./INC-0001-reward-hacking-twelve-near-identical-features-shipped-as-dif.md)
