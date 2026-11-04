---
id: INC-0568
title: A feature branch merged on static gates only, and a unit test elsewhere that encoded the old seed order then went red on main
date: 2026-11-04
classes: [spec-and-scope]
severity: medium
status: mitigated
---

# INC-0568 - A feature branch merged on static gates only, and a unit test elsewhere that encoded the old seed order then went red on main

**Cost:** Main was red at the unit tier until a successor root landed, and the following tiers did not run.

## Signature - how you recognise it

A branch that changes product code passes type, lint, identity and backlog checks, but no whole-unit comparison ran.

## What happened

A feature branch that added an episode phase to the seed merged after its activation job ran type, lint, identity and backlog checks only. In the next full run a unit test of another root, which encodes the old phase order and uses a recording fake that returns no records, failed with a missing-column error. The run stopped at the unit tier, so integration, smoke and the browser tier did not run. It was not a product defect, because seeding after the earlier phase is the design. The lead ruled that a branch that changes product code merges only after a whole-unit comparison equal to the frozen baseline, cited in the merge message, and test-only branches keep the current gates.

## Root cause

The static gates do not run the unit tier, where another root encoded the old order.

## Why it was hard to see

The failure shows up only in the next full run, away from the branch.

## Fix

Run a whole-unit comparison on a product-changing branch before the merge.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A branch that changes product code merges only after a whole-unit comparison equal to the frozen baseline.

## Related

[INC-0553](./INC-0553-a-proposal-found-that-the-product-itself-writes-the-state-a.md)
