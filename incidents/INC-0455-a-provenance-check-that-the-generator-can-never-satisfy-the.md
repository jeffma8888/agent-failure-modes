---
id: INC-0455
title: A provenance check that the generator can never satisfy: the zero parent id on every snapshot
date: 2026-11-02
classes: [false-green]
severity: low
status: fixed
---

# INC-0455 - A provenance check that the generator can never satisfy: the zero parent id on every snapshot

**Cost:** None: the stop came before any harm.

## Signature - how you recognise it

A required check was impossible to pass whatever the code did.

## What happened

a parent id equality check for a snapshot could never pass, because the installed generator gives every snapshot the zero parent id, including the default one, the adapter default snapshot and the accepted prior migration; the check was withdrawn

## Root cause

the check was written from an assumption about the generator output

## Why it was hard to see

Nobody ran the generator to see what it writes into the field.

## Fix

accept parent provenance on three facts: the generated SQL adds only the new additions and re-emits nothing from the prior migration, so the diff base contained it; the new snapshot minus the additions equals the prior snapshot structurally; and the index order matches; later rows use the same three facts

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Prove a diff base from what the generated SQL does and does not emit, and never demand a check the generator can not satisfy

## Related

[INC-0448](./INC-0448-two-fields-mapping-to-one-database-enum-made-the-generated-m.md) [INC-0426](./INC-0426-a-generated-migration-needed-a-lint-only-edit-so-the-evidenc.md) [INC-0439](./INC-0439-a-generated-down-migration-dropped-a-table-with-cascade-and.md)
