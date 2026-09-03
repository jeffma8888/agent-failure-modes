---
id: INC-0043
title: An anchored replace that matches a PREFIX of a line is still 'exactly once'
date: 2026-09-02
classes: [tooling-paths, concurrency, identity-and-keying]
severity: high
status: fixed
---

# INC-0043 - An anchored replace that matches a PREFIX of a line is still 'exactly once'

**Cost:** A concurrent writer's entire batch of seven records silently disappeared from the generated output while the edit reported success. Nothing in the writing script noticed; only the build's own invariant tests caught it, after the damage was on disk.

## Signature - how you recognise it

An edit asserted to match exactly once succeeds, and afterwards the file contains a duplicated fragment of the line you replaced - or one symbol defined twice, the later definition shadowing the earlier.

## What happened

Two independent sessions appended batches to one shared list. The second anchored on the composition line as it had existed BEFORE the first session's change ('X = A + B + C'), but the line now read 'X = A + B + C + D'. The anchor matched as a PREFIX, the uniqueness assertion passed, and the replacement produced 'X = A + B + C + D_new + D' while also defining a second 'D' that shadowed the first - so the first session's seven records vanished from the built artifact.

## Root cause

Two individually-plausible errors compounding. First, an anchor that is a PREFIX of the real line still occurs exactly once, so a count assertion answers 'is this string ambiguous?' and never 'is this string the WHOLE thing I mean to replace?'. Second, both writers independently reached for the next sequential symbol name for their batch, so the later definition silently shadowed the earlier one instead of colliding loudly.

## Why it was hard to see

The edit reports success, the file still parses, and the module still imports. The uniqueness assertion is the very mechanism that was supposed to prevent this, which converts a caught error into false confidence. And the assertion that WOULD have caught it - unique sequential ids - lives in the test suite rather than in the writing script, so it fires only after the file has been overwritten.

## Fix

Anchor on the WHOLE line, or on a content span that includes its terminator, never a prefix. Assert the POST-write state as well as the pre-write count: that each expected symbol is defined exactly once and that the composition names each exactly once. In a shared appended structure, do not assume the next sequential symbol name is free - read the live file first and derive the name from what is actually there.

## Verification

The repair used the broken state itself as its anchor ('... + D + D', asserted to occur exactly once) and asserted afterwards that BOTH batch symbols are defined exactly once. The rebuild reports 42 unique ids with no gap in the sequence, all 27 invariant tests pass, and the other writer's seven records are present again.

## Transferable rule

> An anchor that is a PREFIX of the real line still matches 'exactly once', so a uniqueness assertion certifies ambiguity and never completeness - anchor on the whole line or include its terminator. In a shared appended structure never assume the next sequential symbol name is free: read the live file, and assert AFTER writing that each symbol is defined exactly once.

## Provenance

Where this was observed, so the claim is checkable rather than anecdotal:

- https://github.com/jeffma8888/agent-failure-modes - this repository is where the collision happened: tools/corpus.py now carries the repaired composition line, and commit bccb9d1 is the concurrent writer's batch that was briefly shadowed.

## Related

[INC-0030](./INC-0030-rewriting-a-region-by-slicing-between-two-markers-deletes-wh.md) [INC-0027](./INC-0027-a-cache-keyed-on-a-recycled-id-judged-each-record-on-its-pre.md) [INC-0038](./INC-0038-a-determinism-test-that-scans-the-live-working-tree-cannot-p.md)
