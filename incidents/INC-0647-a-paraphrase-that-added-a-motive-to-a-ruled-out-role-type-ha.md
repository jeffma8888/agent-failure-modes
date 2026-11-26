---
id: INC-0647
title: A paraphrase that added a motive to a ruled-out role type hardened into an AI-only filter, and later sessions drafted declines the user's rubric did not support
date: 2026-11-23
classes: [spec-and-scope]
severity: medium
status: mitigated
topic: spec-and-scope/records-drift-or-lose-provenance
occurrences: 1
---

# INC-0647 - A paraphrase that added a motive to a ruled-out role type hardened into an AI-only filter, and later sessions drafted declines the user's rubric did not support

**Catalog:** [root](../catalog/README.md) / [spec-and-scope](../catalog/spec-and-scope/README.md) / [A cited baseline, count, line, or digest no longer matches its source](../catalog/spec-and-scope/records-drift-or-lose-provenance.md)

**Cost:** Decline drafts were written for roles the user was still open to; caught when the user read one. Whether any had been sent was not recorded.

## Signature - how you recognise it

A stored preference line states a motive or positive goal where the source stated only an exclusion, and a later decline cites that goal as its reason.

## What happened

A user ruled out one kind of role, operating infrastructure fleets. The agent's summary added a motive, that the user wants to build AI systems rather than operate fleets, and a later compact index line led with 'build AI systems'. Sessions that read the index took the line as AI-only and drafted declines for ordinary backend roles citing a focus on AI roles, although the user's scoring rubric scored backend work low but not zero and the search tool kept it as a tier. The user read a draft and said backend roles were open, only ranked lower.

## Root cause

Each compression changed the preference's polarity and scope: an exclusion became a positive goal, and the goal then read as a gate. Nothing compared the index line with the rubric that actually scored roles.

## Why it was hard to see

Each step was a plausible paraphrase of the one before, the motive clause sounded like the user, and the index line was short enough that its loss of scope was invisible.

## Fix

The index line now states the ranking explicitly (preferred, open, out) with dates; a decline reason must be one the user holds, and the rule was carried into the reply procedure and the rubric.

## Verification

Checked by the user: backend roles are open at a lower rank, and the index line was rewritten. Not checked: other compressed preference lines for the same drift.

## Transferable rule

> When compressing a preference, keep its polarity and scope (out versus merely ranked lower); never turn a motive clause into a gate, and use a stored preference as a reject reason only if it agrees with the rubric that scores it.
