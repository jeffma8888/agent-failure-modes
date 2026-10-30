---
id: INC-0076
title: A teammate's write boundary contradicted the charter's file layout, so a required record landed where activation would reject it
date: 2026-10-30
classes: [spec-and-scope, delegation]
severity: low
status: fixed
---

# INC-0076 - A teammate's write boundary contradicted the charter's file layout, so a required record landed where activation would reject it

**Cost:** Caught before commit. A required coverage record was left inside the boundary's directory, where the activation step would have rejected it as an unlisted payload.

## Signature - how you recognise it

A brief limits writes to one directory, and the governing charter requires an output in a different one.

## What happened

A brief allowed a test-writing agent to write only under a pending-tests directory. The charter places each task's coverage record in a separate coverage directory. The agent obeyed the boundary and left the record under a handoff file inside the pending root.

## Root cause

The boundary and the charter were written independently and never compared. A compliant agent resolves a conflict in favour of the explicit restriction, so the charter's requirement is the one that loses.

## Why it was hard to see

The agent did exactly what the brief said and reported it. The failure appears later, at a consumer that checks the layout.

## Fix

The coordinator moved the records to the charter's location before committing and widened the next batch's boundary to match the charter.

## Verification

Checked: the three misplaced records were found and moved before the commit. The widened boundary has not yet been exercised.

## Transferable rule

> Derive a teammate's write boundary from the governing charter's layout, and check the two agree before sending the brief.

## Related

[INC-0074](./INC-0074-a-brief-named-a-source-directory-the-repository-does-not-hav.md) [INC-0016](./INC-0016-anti-delegation-clause-must-forbid-scaffold-a-loop-too.md)
