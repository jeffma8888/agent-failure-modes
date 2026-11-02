---
id: INC-0421
title: A closure packet freeze test turned positive on a control-only landing and the lead admitted it narrowly
date: 2026-11-02
classes: [false-green]
severity: low
status: fixed
---

# INC-0421 - A closure packet freeze test turned positive on a control-only landing and the lead admitted it narrowly

**Cost:** No run was lost; the run waited for a written admission instead of proceeding or being blocked.

## Signature - how you recognise it

A freeze test reported a change that the guarded run could not read.

## What happened

the closure packet's freeze test turned positive on a control-only landing that changed checker metadata on main and nothing the run reads; the lead admitted it narrowly for the diagnostic-only run because the run executes in a detached clone with its own registry and markers, any further change to a registry or marker file before launch is a new STOP, and the identity step is not waived

## Root cause

the freeze test checks main, while the run reads its own detached copy of the registry and markers

## Why it was hard to see

The test was right that something changed and wrong about whether the run could see it.

## Fix

when a freeze test fires on a landing the run cannot read, record the admission with its reason, its exact scope and the condition that reopens it, and keep every identity step

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Admit a freeze-test hit only narrowly: name the landing, why the run cannot read it, and the change that makes it a new STOP; never waive the identity step

## Related

[INC-0335](./INC-0335-a-pinned-base-digest-froze-a-file-that-a-later-row-split-nee.md) [INC-0359](./INC-0359-a-stored-admission-record-left-out-the-tool-versions-it-was.md) [INC-0443](./INC-0443-a-self-imposed-freeze-outlived-its-reason-and-was-blocking-t.md)
