---
id: INC-0669
title: Sections of one design document contradicted each other on a terminal state, a durability promise and a component's access
date: 2026-11-26
classes: [spec-and-scope]
severity: medium
status: fixed
topic: spec-and-scope/requirements-and-limits-collide
occurrences: 1
---

# INC-0669 - Sections of one design document contradicted each other on a terminal state, a durability promise and a component's access

**Catalog:** [root](../catalog/README.md) / [spec-and-scope](../catalog/spec-and-scope/README.md) / [Requirements, units, or hard limits cannot hold together](../catalog/spec-and-scope/requirements-and-limits-collide.md)

**Cost:** Two contradictions reached a second-model reviewer in the second version and cost part of a revision round; a third was caught by the author during a trim pass.

## Signature - how you recognise it

One cause maps to different terminal states in a diagram and a table, or one section promises a property that a procedure in another section can break.

## What happened

A long design document was written section by section; this record covers two sets of findings from it. While the first version was being drafted, a sentence imported from the research notes said workers claim jobs with row locks, while another section had decided that workers never touch the database; the author caught it during a trim pass. In the second version a reviewer found that a timeout led to one terminal state in the state diagram and a different one in the step table, and that one section promised the audit trail is never deleted while the backup-restore procedure in another could delete it. After the fixes, a dedicated search for each state name across the document found no further conflict.

## Root cause

Each section was checked against its own sources and template when written, and no pass compared the names and promises that several sections share. An imported sentence carried the assumptions of the document it came from.

## Why it was hard to see

Every section reads correctly alone, and the conflicting statements sit far apart in different forms: a diagram, a table, a paragraph. A copied sentence is fluent and sourced, so it is not re-read as a design claim.

## Fix

Before submitting, list every state name and every durability, deletion or restore claim, search the whole document for each, and reconcile to one terminal state per cause; re-read every sentence imported from research against the decisions already recorded.

## Verification

After the fixes, a search pass per state name across all sections found no remaining conflict. Not checked: shared claims other than state names and durability promises, or an independent re-review of the final version.

## Transferable rule

> Before submitting a design document, search every state name and every durability, deletion or restore claim across all sections and reconcile them to one terminal state per cause; re-read each sentence copied from research against the decisions already made.

## Related

[INC-0302](./INC-0302-a-plan-revision-left-stale-operative-text-that-only-an-indep.md)
