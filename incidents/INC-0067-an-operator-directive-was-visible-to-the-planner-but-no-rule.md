---
id: INC-0067
title: An operator directive was visible to the planner but no rule ranked it, so it was deferred while the loop shipped its own picks
date: 2026-10-27
classes: [steering-channel, spec-and-scope]
severity: medium
status: fixed
---

# INC-0067 - An operator directive was visible to the planner but no rule ranked it, so it was deferred while the loop shipped its own picks

**Cost:** Two precise operator directives were acknowledged and deferred for an iteration while the loop shipped lower-priority picks of its own. Found by grading the planner's own triage, which labelled both 'not in the current slate'.

## Signature - how you recognise it

A directive is placed in the file every role reads first, and the planning role's output acknowledges it and then does something else.

## What happened

An operator of a self-improving loop wrote two defect pins at the head of the learnings file that every role reads first. The planner role's prompt limited its candidate pool to the scouts' slates and contained no rule for ranking an operator pin. The pins were read, and deferred.

## Root cause

Visibility was mistaken for a route. Delivery into the prompt (which INC-0020 covers) was working; what was missing was a rule in the decision step that says which input wins. A picker with a closed candidate pool cannot select an item that was never put into the pool.

## Why it was hard to see

The directive was read and quoted back, which looks like compliance. The failure shows only as a deferral that sounds reasonable.

## Fix

One routing rule added at the same head: an un-retired operator pin is candidate 1 of every slate and the planner's pick, and lens scope does not apply. The rule was later written into the planner's prompt with a test.

## Verification

After the rule was added the loop executed six pins in seven consecutive iterations. Not checked here: behaviour of the prompt-level version beyond the test that was added with it.

## Transferable rule

> A directive to an agent system needs a route into the decision, not only visibility. Before queuing one, read the picker's prompt and confirm which rule will select it; if none does, write that rule first.

## Related

[INC-0020](./INC-0020-a-steering-channel-counts-only-when-the-consumer-s-own-parse.md) [INC-0004](./INC-0004-a-monotonically-growing-required-reading-file-silently-kills.md)
