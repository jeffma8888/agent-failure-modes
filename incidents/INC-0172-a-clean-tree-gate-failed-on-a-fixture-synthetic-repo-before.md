---
id: INC-0172
title: A clean-tree gate failed on a fixture synthetic repo before the behavior under test
date: 2026-10-30
classes: [test-isolation, false-green]
severity: medium
status: fixed
---

# INC-0172 - A clean-tree gate failed on a fixture synthetic repo before the behavior under test

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A test failed at the gate, not at the behavior it meant to exercise.

## What happened

Generated launcher files in a fixture synthetic repo were not ignored before the fixture commit, so the clean-tree gate failed first.

## Root cause

The fixture was written as if the gate did not apply to it.

## Why it was hard to see

The failure shows up away from the cause and looks plausible.

## Fix

Ignore generated files before the fixture commit, and print the child output with a one-off probe.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A clean-tree gate applies to a fixture synthetic repo too.

## Related

[INC-0153](./INC-0153-a-test-checked-only-the-dispatch-argv-of-a-child-stage-not-i.md)
