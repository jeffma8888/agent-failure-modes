---
id: INC-0448
title: Two fields mapping to one database enum made the generated migration narrow a five-state status to two states
date: 2026-11-02
classes: [identity-and-keying]
severity: low
status: fixed
---

# INC-0448 - Two fields mapping to one database enum made the generated migration narrow a five-state status to two states

**Cost:** No bad migration landed; the engineer stopped and regenerated.

## Signature - how you recognise it

A generated migration silently narrowed a status to fewer states than the field allows.

## What happened

the framework's own draft status field and the persistent five-state status field collided on one generated enum name, so the generated migration gave both the two draft states and would have rejected the other three; the engineer caught it by reading the generated SQL before type generation and stopped; the lead sourced a per-field enum-name option in the installed packages and ruled a distinct enum name per table for the persistent field, with the generated files removed by exact name and regenerated, and a check before type generation that all five states are present on both persistent enums

## Root cause

two fields mapped to the same default enum name, so the first definition won

## Why it was hard to see

The generated file looked valid and only a reading of the SQL showed the narrowing.

## Fix

give the persistent field its own enum name per table, regenerate, and check the generated SQL for all states before generating types

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Give each field that persists a state set its own enum name per table, and check the generated SQL for every state before generating types

## Related

[INC-0173](./INC-0173-a-ruling-widened-a-shared-valid-state-and-only-some-payloads.md) [INC-0426](./INC-0426-a-generated-migration-needed-a-lint-only-edit-so-the-evidenc.md) [INC-0439](./INC-0439-a-generated-down-migration-dropped-a-table-with-cascade-and.md) [INC-0455](./INC-0455-a-provenance-check-that-the-generator-can-never-satisfy-the.md) [INC-0458](./INC-0458-a-generated-down-migration-defect-fixed-once-came-back-in-th.md)
