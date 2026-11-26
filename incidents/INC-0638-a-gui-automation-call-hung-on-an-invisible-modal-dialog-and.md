---
id: INC-0638
title: A GUI automation call hung on an invisible modal dialog, and the control tests were confounded because the relaunched app reopened the hung document
date: 2026-11-12
classes: [test-isolation, observability]
severity: medium
status: mitigated
topic: test-isolation/the-test-itself-is-the-defect
occurrences: 1
---

# INC-0638 - A GUI automation call hung on an invisible modal dialog, and the control tests were confounded because the relaunched app reopened the hung document

**Catalog:** [root](../catalog/README.md) / [test-isolation](../catalog/test-isolation/README.md) / [The red comes from the test's own fixture, tool option or control](../catalog/test-isolation/the-test-itself-is-the-defect.md)

**Cost:** Three control tests gave no usable signal and an input bisect ran on a wrong premise; the time lost was not measured.

## Signature - how you recognise it

An automation call into a desktop app never returns while the app spins at full CPU with nothing on screen, and known-good control inputs hang the same way after a forced restart.

## What happened

An agent drove a sandboxed desktop app through its scripting interface to export a document as PDF. The call never returned and the app's process sat at 100% CPU. The agent treated the document as the suspect and began bisecting the input. The call was in fact blocked by a modal dialog that never became visible, waiting for an answer no script would give. Each forced kill and relaunch let the app's window state restoration reopen the suspect document, so the three control tests that followed ran with that document loaded again and hung for the same reason, which made the controls read as evidence about the inputs under test.

## Root cause

The hang was diagnosed from the input side (what was fed in) instead of the process side (what the target was waiting on), and the retest procedure assumed a forced kill returns the app to a clean state, while the app restores its previous documents on relaunch.

## Why it was hard to see

The dialog was invisible, full CPU looked like work rather than a wait, and the reopened document arrived without any action by the agent, so each control looked like a fresh run with a different input.

## Fix

Sample the hung process first and read the main thread's stack for a modal or nested run loop. Before a retest after a forced kill, move or rename the input that hung (or turn off state restoration for that app) so the relaunch cannot reopen it, and confirm the app starts with no document open.

## Verification

Checked by the person who reported it: the hang was attributed to the modal dialog and the confounded controls to state restoration. Not checked: whether the rule prevents recurrence, or how many other sandboxed apps restore state this way.

## Transferable rule

> When an automation call hangs, sample the target process and look for a modal run loop before bisecting the input; before any retest after a forced kill, put the input that hung out of reach of the app's auto-reopen and confirm the app relaunched with nothing open.

## Related

[INC-0207](./INC-0207-three-sends-failed-because-a-packed-string-went-out-as-one-a.md)
