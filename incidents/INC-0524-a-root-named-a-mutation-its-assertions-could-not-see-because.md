---
id: INC-0524
title: A root named a mutation its assertions could not see, because the next line returned the same status
date: 2026-11-02
classes: [false-green]
severity: low
status: mitigated
---

# INC-0524 - A root named a mutation its assertions could not see, because the next line returned the same status

**Cost:** A case would have been credited with a witness mutation that could not turn it red.

## Signature - how you recognise it

The named mutation is removed, and the case still passes because a later line refuses the same way.

## What happened

A root coverage named as its witness a mutation that removes an early return for a missing sniffed type. With no sniffed type, the next line, which compares the declared type with the sniffed one, is true, so the code still refuses with the same status and the case stays green. The witness was ruled to be a mutation the case can see, such as disabling the whole refusal so the bad bytes are stored, stated with its expected red line.

## Root cause

The witness was chosen from the line mutated, not from what the following lines return.

## Why it was hard to see

Each line looks like the guard of the case, and redundant guards hide each other.

## Fix

Trace the code after the mutated line before naming it, and state its expected red line.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A mutation named as a case witness must be one the assertions can see; trace what the next line returns before naming it, and state the expected red line.

## Related

[INC-0476](./INC-0476-unit-mutation-testing-on-a-merged-change-found-two-survivors.md) [INC-0510](./INC-0510-mutation-restore-receipts-were-kept-only-in-tool-output-so-t.md)
