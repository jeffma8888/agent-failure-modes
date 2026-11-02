---
id: INC-0527
title: An absence check for a hidden field matched the hidden input the library renders, so a regression root was red on unchanged code
date: 2026-11-02
classes: [false-green]
severity: medium
status: mitigated
---

# INC-0527 - An absence check for a hidden field matched the hidden input the library renders, so a regression root was red on unchanged code

**Cost:** An activation run stopped on a baseline red, and a successor root was needed; no product change.

## Signature - how you recognise it

A test asserts that a selector for a hidden field matches nothing, and the library renders a hidden input with the field id.

## What happened

The activation run of a regression root on unchanged code failed both cases at an assertion that a selector for a hidden field, a JSON field or an editor widget matches zero elements, receiving one. The runner stopped before any mutation and weakened nothing. Installed source shows the library renders a hidden field as a hidden input with an id built from the field path, so the single match was the product working as intended. The selector arm for the field id was a root defect. The earlier static review could not see this, since it needs the rendered markup.

## Root cause

The absence check was written from what a hidden field should mean, not from what the library renders.

## Why it was hard to see

Static review cannot see rendered markup, so only a run on unchanged code shows the root is wrong.

## Fix

Write the absence check against what the library renders for a hidden field, and revise the root by a successor.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A regression root must be green on unchanged code before any mutation; an absence selector for a hidden field must account for the hidden input the library still renders.

## Related

[INC-0523](./INC-0523-three-test-roots-by-three-authors-used-the-same-guessed-loca.md) [INC-0524](./INC-0524-a-root-named-a-mutation-its-assertions-could-not-see-because.md)
