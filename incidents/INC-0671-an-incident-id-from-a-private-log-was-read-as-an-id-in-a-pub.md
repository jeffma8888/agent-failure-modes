---
id: INC-0671
title: An incident id from a private log was read as an id in a public corpus that numbers its records separately
date: 2026-11-25
classes: [identity-and-keying, delegation]
severity: low
status: mitigated
topic: identity-and-keying/new-id-already-taken
occurrences: 1
---

# INC-0671 - An incident id from a private log was read as an id in a public corpus that numbers its records separately

**Catalog:** [root](../catalog/README.md) / [identity-and-keying](../catalog/identity-and-keying/README.md) / [A newly minted id or name collides with one already in use](../catalog/identity-and-keying/new-id-already-taken.md)

**Cost:** One lookup; a recurrence filed against an unrelated record was avoided before anything was written.

## Signature - how you recognise it

A note or brief says a failure is already recorded under an id, and the id has the target corpus's format but comes from a different log.

## What happened

A private learning log stated that a mechanism was already recorded under a given incident id, and a delegation brief for curating a public incident corpus repeated the pointer. The private log numbers its incidents on its own scale but writes ids in the same format as the public corpus. A curator about to file a recurrence against that id first ran the corpus's own show command and found that the id named an unrelated record. The pointer was dropped and the duplicate check was redone with the corpus's search.

## Root cause

Two registries use one id format with independent numbering, and an id was carried from one into the other as if it were global.

## Why it was hard to see

The id resolved to a real record, so nothing failed; the mismatch shows only when the record's title is read against the mechanism it is supposed to cover. The pointer arrived in a brief, which lent it authority.

## Fix

Resolve every cross-reference in the target corpus with its own lookup before using it, and compare the record's title and rule with the claim; write the registry's name beside any id that crosses a repository boundary.

## Verification

The curator's lookup showed the mismatch before any record was written. Not checked: whether other pointers in the same log carry the same confusion.

## Transferable rule

> Resolve every cross-reference into a corpus with that corpus's own lookup (check, search or show) and read the record before using the id; never carry an id from one repository's numbering into another unresolved.

## Related

[INC-0080](./INC-0080-two-writers-used-the-same-short-question-id-for-different-ga.md)
