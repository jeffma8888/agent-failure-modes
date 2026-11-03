---
id: INC-0530
title: An icon-only button had no accessible name, so a role-name locator could never match and the test timed out
date: 2026-11-02
classes: [false-green]
severity: low
status: mitigated
---

# INC-0530 - An icon-only button had no accessible name, so a role-name locator could never match and the test timed out

**Cost:** A browser test timed out at one line and needed a successor root; no product change.

## Signature - how you recognise it

A test waits for a button by role and name, and the button has no name to match.

## What happened

A browser root located the remove control of an upload field by its role and a name pattern, and the run timed out at that line. Installed source shows the control is an icon-only button with no children, no aria-label and no tooltip, and the button component sets an aria-label only from its prop. A role-name pattern cannot match it. The successor binds it by class inside the field scope and also handles the empty field, where no remove control exists.

## Root cause

The locator assumed every button has an accessible name.

## Why it was hard to see

A timeout at a locator looks like a slow page, and the missing name is visible only in the source or the accessibility snapshot.

## Fix

Bind the locator to the class the installed source renders inside the field scope, and handle the empty-field case.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Before writing a role-name locator for a control, read the installed source for its accessible name; an icon-only control with no label has none, and a test that waits for one can only time out.

## Related

[INC-0523](./INC-0523-three-test-roots-by-three-authors-used-the-same-guessed-loca.md) [INC-0527](./INC-0527-an-absence-check-for-a-hidden-field-matched-the-hidden-input.md)
