---
id: INC-0561
title: A verifier matched plain text in colored logs and stopped
date: 2026-11-04
classes: [tooling-paths]
severity: low
status: mitigated
---

# INC-0561 - A verifier matched plain text in colored logs and stopped

**Cost:** The index generation stopped before writing; no test ran and no product file changed.

## Signature - how you recognise it

A text match over raw logs that contain terminal color escape codes.

## What happened

A verifier looked for plain test-count text in raw logs that carried terminal color escapes, matched nothing, and stopped before writing its index. Stripping the escapes for matching only, with the raw evidence bytes unchanged, made the check succeed for all nine receipts, and the index hashed the original raw bytes.

## Root cause

The match assumed plain text in logs that were colored.

## Why it was hard to see

A stopped check looks like a missing result, not a formatting problem.

## Fix

Strip escapes for matching only and hash the raw bytes.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Strip color escapes for matching only; never alter the raw evidence bytes or the hash of them.

## Related

[INC-0545](./INC-0545-a-landing-helper-guessed-the-kind-of-each-argument-from-its.md)
