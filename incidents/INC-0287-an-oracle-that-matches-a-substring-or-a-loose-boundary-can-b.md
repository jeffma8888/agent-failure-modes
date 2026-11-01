---
id: INC-0287
title: An oracle that matches a substring or a loose boundary can be satisfied by a decoy
date: 2026-11-01
classes: [false-green, spec-and-scope]
severity: medium
status: fixed
---

# INC-0287 - An oracle that matches a substring or a loose boundary can be satisfied by a decoy

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

An assertion passed on a decoy that merely contained the expected text.

## What happened

a markup pattern with a word boundary also matched a similarly named attribute, and a count of label characters in flattened text passed when a heading and a separate element supplied them; neither proved the intended attribute or element

## Root cause

a markup pattern with a word boundary also matched a similarly named attribute, and a count of label characters in flattened text passed when a heading and a separate element supplied them; neither proved the intended attribute or element

## Why it was hard to see

The real case and the decoy produce the same match, so the assertion looks correct.

## Fix

Anchor on the exact boundary, observe the exact element or attribute that carries the claim, and add negative controls that must make the assertion fail

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Prove a claim on the exact element or attribute, and show the oracle rejects a decoy

## Related

[INC-0176](./INC-0176-a-shape-regex-was-used-as-ownership-evidence-for-a-sweep.md)
