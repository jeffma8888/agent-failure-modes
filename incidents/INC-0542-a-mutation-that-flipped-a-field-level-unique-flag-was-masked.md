---
id: INC-0542
title: A mutation that flipped a field-level unique flag was masked by a unique index the migration had already created
date: 2026-11-02
classes: [false-green]
severity: low
status: mitigated
---

# INC-0542 - A mutation that flipped a field-level unique flag was masked by a unique index the migration had already created

**Cost:** No loss. The reviewer blocked the root until a sanctioned route for right-reason evidence existed.

## Signature - how you recognise it

The mutated product setting is not the only thing enforcing the rule, because a database index enforces it too.

## What happened

A reviewer blocked a root because its named mutation, turning off the unique flag on a field, could not turn the duplicate-rejection assertions red: the migrated unique index still rejected the duplicate. The block was a missing sanction, not a payload defect. The lead sanctioned a route: on the activator own cluster, a disposable database with an exact recorded name, migrated, then drop that one index in that database only (recording the statement and the index list before and after) together with the field flip, observe both cases red on their rejection assertions, drop the database by its exact name, restore the product bytes by hash, and show green again on a fresh migrated database.

## Root cause

The rule was enforced at two layers, and the mutation reached only the upper one.

## Why it was hard to see

The run stays green or red for the wrong reason unless the lower layer is traced.

## Fix

Mutate the schema layer in a disposable database as well as the field flag, and record the statements.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> When a rule is enforced in the schema as well as in code, a right-reason mutation must defeat both layers, in a disposable database with an exact recorded name.

## Related

[INC-0534](./INC-0534-a-configuration-mutation-failed-a-setup-assertion-before-any.md) [INC-0524](./INC-0524-a-root-named-a-mutation-its-assertions-could-not-see-because.md)
