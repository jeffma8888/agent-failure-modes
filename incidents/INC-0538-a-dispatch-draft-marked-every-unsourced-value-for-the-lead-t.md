---
id: INC-0538
title: A dispatch draft marked every unsourced value for the lead to bind instead of guessing
date: 2026-11-02
classes: [spec-and-scope]
severity: low
status: mitigated
---

# INC-0538 - A dispatch draft marked every unsourced value for the lead to bind instead of guessing

**Cost:** None; this is the intended behavior. The lead bound the open values in one ruling and the draft needed no corrections.

## Signature - how you recognise it

A packet contains values with no source in any record, such as a credential location, a clock setting or a build mode.

## What happened

The author of a walk dispatch packet cited each value to a file line, a commit or a ruling, and marked every value it could not source as bound by the lead. The report listed the open findings, such as the credential location, whether the walk server forces a clock, and the build mode, with the gap for each. The lead bound them together with the target tree, database, ports and permissions in a single ruling.

## Root cause

The records covered precedents, not the specific walk, so any value written without a source would have been a guess.

## Why it was hard to see

Filling a gap with a plausible precedent is quicker, and a wrong value surfaces only at run time.

## Fix

Mark each unsourced value, state the gap, and let the owner bind all of them at once.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> When a value is missing, mark it for the owner to bind and list the gap; never fill it with a precedent or a guess.

## Related

[INC-0535](./INC-0535-a-standing-promise-to-guard-every-proven-behavior-had-no-inv.md)
