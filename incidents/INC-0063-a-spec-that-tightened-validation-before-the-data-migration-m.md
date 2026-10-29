---
id: INC-0063
title: A spec that tightened validation before the data migration made every real-data test fail
date: 2026-10-29
classes: [spec-and-scope, false-green]
severity: low
status: fixed
---

# INC-0063 - A spec that tightened validation before the data migration made every real-data test fail

**Cost:** The implementer could not reach a green suite on the real data table, so code defects and missing data were indistinguishable. The implementer had to prove the code on a patched scratch copy instead.

## Signature - how you recognise it

A new spec makes a field required, while the step that adds that field to the existing data is scheduled after the code.

## What happened

A spec revision made the validator reject measured rows lacking a list of measurements, but scheduled adding those lists as the spec author's step after the implementation. Every test against the real table therefore failed until the data landed.

## Root cause

The spec ordered work by who owned it instead of by dependency. Tightened validation turns missing data into a failure of the code's tests, mixing two kinds of defect in one red signal.

## Why it was hard to see

Each step is reasonable alone, and the red tests look like implementation bugs. Only the dependency between the validator and the data explains why no implementation could pass.

## Fix

The spec author added the data and regenerated the derived policy block, after which the full suite went green (131 tests). Meanwhile the implementer verified the code on a patched scratch copy of the data.

## Verification

The full suite passed against the real table once the data landed.

## Transferable rule

> When a spec tightens validation, order the data migration before the code, or give the implementer an explicit scratch-copy check, so code defects and missing data are tested separately.

## Related

[INC-0022](./INC-0022-test-precondition-on-gitignored-local-state-passes-only-on-t.md) [INC-0035](./INC-0035-two-individually-safe-options-are-unsafe-together-when-their.md)
