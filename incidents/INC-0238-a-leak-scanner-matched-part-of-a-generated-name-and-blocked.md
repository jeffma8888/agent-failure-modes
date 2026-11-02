---
id: INC-0238
title: A leak scanner matched part of a generated name and blocked uploads
date: 2026-10-31
classes: [detector-fail-closed, tooling-paths]
severity: medium
status: fixed
---

# INC-0238 - A leak scanner matched part of a generated name and blocked uploads

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

The scan failed closed on a merge long after the files were added.

## What happened

A leak scanner word list matched part of a time zone name in generated framework types, and the push range scan never covered those files until a merge.

## Root cause

A leak scanner word list matched part of a time zone name in generated framework types, and the push range scan never covered those files until a merge.

## Why it was hard to see

The generated files were outside the push range.

## Fix

Fix it with an encoded safe prefix for that one word, prove it with planted cases against the old version, and scan the whole tree after every merge, not only the push range

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Scan the whole tree after every merge, and fix a scanner false match with an encoded safe prefix proved by planted cases

## Related

[INC-0215](./INC-0215-a-commit-skipped-the-machine-wide-pre-commit-scanner.md) [INC-0407](./INC-0407-a-lead-signature-line-containing-the-assistant-s-product-nam.md)
