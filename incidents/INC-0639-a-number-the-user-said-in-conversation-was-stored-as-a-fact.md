---
id: INC-0639
title: A number the user said in conversation was stored as a fact in long-term memory and scripts, though the user's own canonical document said otherwise
date: 2026-11-12
classes: [spec-and-scope]
severity: medium
status: mitigated
topic: spec-and-scope/records-drift-or-lose-provenance
occurrences: 1
---

# INC-0639 - A number the user said in conversation was stored as a fact in long-term memory and scripts, though the user's own canonical document said otherwise

**Catalog:** [root](../catalog/README.md) / [spec-and-scope](../catalog/spec-and-scope/README.md) / [A cited baseline, count, line, or digest no longer matches its source](../catalog/spec-and-scope/records-drift-or-lose-provenance.md)

**Cost:** The wrong number was fed back into later conversations by the stored profile and reusable scripts until a cross-check caught it; how many outputs carried it was not counted.

## Signature - how you recognise it

A figure in the agent's memory or scripts traces back to one thing the user said, and the user's canonical document gives a different figure.

## What happened

In a recorded conversation the user stated a number about their own situation. The agent wrote it into its long-term profile of the user and into reusable scripts as a settled fact, without comparing it with the user's canonical document, which gave a different value. The scripts then put the stored number back into later conversations, so each reuse reinforced the error. It was caught when the canonical number came up once in a later session and the agent cross-checked its records against it.

## Root cause

A self-report was promoted to a stored fact at write time, with no source attached and no comparison with the document the user keeps as authoritative.

## Why it was hard to see

The value came from the user, so it felt authoritative; once stored, every later reuse looked like confirmation, and the scripts hid where the number had come from.

## Fix

A stated number is stored as a quote with its source and date, and becomes a fact only after it matches the canonical document; a conflict between the two is surfaced to the user rather than resolved by the agent. The profile and the scripts were corrected from the canonical document.

## Verification

Checked: the stored value was compared with the canonical document and the conflict confirmed. Not checked: an audit of every other value written to memory from conversation, or whether the rule prevents recurrence.

## Transferable rule

> Store a number someone states as a quote with its source, never as a fact; promote it only after it matches the canonical document, and surface any conflict to the person instead of resolving it yourself.
