---
id: INC-0057
title: A revision that closed every finding introduced new defects in the seams it added
date: 2026-10-29
classes: [false-green, spec-and-scope]
severity: medium
status: mitigated
---

# INC-0057 - A revision that closed every finding introduced new defects in the seams it added

**Cost:** A revision accepted all 12 blocking review findings and the blocking count rose to 15 on the next round. One more full revision and review cycle was needed.

## Signature - how you recognise it

Each review round's fix adds new concrete claims (types, hooks, signatures), and the next round's findings are mostly about those additions.

## What happened

A scope document accepted all 12 blocking findings by adding concrete seams: types, setup hooks, seed calls. Several of the additions were wrong: a data type that does not exist, a test-runner setup object that cannot cross into forked workers, a seed call with the wrong signature, a schema field the design never had. Independent reviewers found 15 blocking issues in round two.

## Root cause

Accepting a finding was treated as closing it. A fix that names new things makes new claims, and those claims were written from memory instead of checked against their source of truth, which is the same failure the fix was responding to.

## Why it was hard to see

The fix addresses the reviewer's exact words, so it looks responsive. The new claims are specific and plausible, and only a reader who looks each one up in the design or the framework source sees that it is false.

## Fix

The next revision's brief requires the author to search for every newly relied-on name, signature and framework behaviour in the design and the pinned framework source before writing it down.

## Verification

Reviewers checked each newly named type and signature against the design and the framework source, which is how the wrong ones were found.

## Transferable rule

> An accepted finding is not a closed finding. Re-verify every new concrete claim a fix introduces against its source of truth before declaring the finding closed.

## Related

[INC-0042](./INC-0042-self-review-does-not-catch-recurrences-of-your-own-documente.md) [INC-0056](./INC-0056-test-seams-declared-from-memory-carried-wrong-field-names-an.md)
