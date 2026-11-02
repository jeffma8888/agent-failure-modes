---
id: INC-0422
title: A scoped compiler config flagged an import style that the canonical build never compiles
date: 2026-11-02
classes: [tooling-paths]
severity: low
status: fixed
---

# INC-0422 - A scoped compiler config flagged an import style that the canonical build never compiles

**Cost:** Minor: an error that was not a defect could have forced a repository config or test edit.

## Signature - how you recognise it

A scoped compile failed on a file the canonical build does not compile.

## What happened

a scoped compiler config reported an error on an import style that six helpers on main already use, because the canonical build compiles only its referenced projects and never reaches that file; the lead allowed the option in the external retained config only, with no repository config change and no test change

## Root cause

the scoped config includes files the canonical build never reaches

## Why it was hard to see

The error was real under the scoped config and meaningless for the build.

## Fix

compare a scoped-config diagnostic with the canonical build before treating it as a code defect, and fix an artifact of the scoped config in the retained external config only

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Check a scoped compiler diagnostic against the canonical build before calling it a defect; fix a scoped-config artifact in the retained config, not the repository

## Related

[INC-0342](./INC-0342-a-shortcut-launcher-lacked-the-protection-the-canonical-entr.md) [INC-0344](./INC-0344-focused-runs-after-a-refactor-hid-static-check-residue-until.md) [INC-0110](./INC-0110-a-cross-row-test-needed-setup-absent-from-its-own-lifecycle.md)
