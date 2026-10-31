---
id: INC-0156
title: A test fixture name collided with a framework built-in and only collection revealed it
date: 2026-10-30
classes: [tooling-paths, false-green]
severity: medium
status: fixed
---

# INC-0156 - A test fixture name collided with a framework built-in and only collection revealed it

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A helper looked fine in review and failed to load in every spec that imported it.

## What happened

A QA browser helper registered an auto fixture named offline, which the Playwright version in use already registers as a built-in option, so every importing spec failed at collection.

## Root cause

The name was valid in isolation and nothing before collection compares it with the framework built-ins.

## Why it was hard to see

Hard to see by reading: the file is syntactically correct and the clash appears only when the framework loads it.

## Fix

Rename the fixture (outboundGuard) in a QA revision with no assertion change, and prove it with a list run at the destination.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Run the framework list command on each new helper before its activation review.

## Related

[INC-0153](./INC-0153-a-test-checked-only-the-dispatch-argv-of-a-child-stage-not-i.md)
