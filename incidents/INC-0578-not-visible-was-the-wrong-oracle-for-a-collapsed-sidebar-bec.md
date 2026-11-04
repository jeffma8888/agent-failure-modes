---
id: INC-0578
title: Not visible was the wrong oracle for a collapsed sidebar, because the closed navigation stays in the page with opacity zero and inert
date: 2026-11-04
classes: [false-green]
severity: low
status: mitigated
---

# INC-0578 - Not visible was the wrong oracle for a collapsed sidebar, because the closed navigation stays in the page with opacity zero and inert

**Cost:** None. The run before approval caught it, and the unlanded root was revised in place.

## Signature - how you recognise it

A closed menu is still in the DOM, and the visibility matcher ignores inert and off-screen position.

## What happened

A new root run before approval failed in the open-menu case because the media link stayed visible after the toggle read open menu. The case had never run before. In the installed admin framework the open class is added only when the navigation is open, and the closed navigation sets inert, but keeps its links in the DOM, and the visibility matcher ignores inert and off-screen position. The lead ruled that the closed check be inert present and the open class absent, the open check the open class, no inert and the link in the viewport, bound to the quoted source.

## Root cause

The oracle was chosen from how the menu looks, not from how the framework closes it.

## Why it was hard to see

Visible and in the DOM are different things for an inert element.

## Fix

Bind the closed and open states to the framework attributes quoted from the installed source.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Bind a collapsed or open state to the attributes the framework sets, not to a visibility matcher.

## Related

[INC-0571](./INC-0571-a-pre-action-zero-count-check-in-a-browser-test-showed-the-e.md)
