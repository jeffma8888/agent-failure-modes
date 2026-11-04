---
id: INC-0564
title: A merge check rejected a generated migration for whitespace that every earlier generated migration also had
date: 2026-11-04
classes: [detector-fail-closed]
severity: low
status: mitigated
---

# INC-0564 - A merge check rejected a generated migration for whitespace that every earlier generated migration also had

**Cost:** The first merge attempt stopped; the merge helper was changed to exclude generated migrations from the whitespace check.

## Signature - how you recognise it

A whitespace check rejects the output of a code generator.

## What happened

The first merge attempt stopped at the whitespace diff check on a new generated migration file, which has a space before a tab and trailing spaces. That is the generator own output, and every migration already on the main branch has the same pattern. The lead ruled that generated files stay byte for byte as generated, that the merge helper excludes the generated migration files from that check while still checking the index file and every other file, and that hand edits to a generated migration remain forbidden.

## Root cause

The check was written for hand-written files.

## Why it was hard to see

The failure looks like a style defect to fix by editing.

## Fix

Exempt generated files from the check by exact pattern, and keep checking everything else.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Do not hand-edit generated files to satisfy a whitespace check; exempt them by an exact pattern and keep checking all other files.

## Related

[INC-0545](./INC-0545-a-landing-helper-guessed-the-kind-of-each-argument-from-its.md)
