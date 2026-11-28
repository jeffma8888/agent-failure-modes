---
id: INC-0048
title: Citing an identifier in the same parallel tool block that creates it makes the citation a guess
date: 2026-10-28
classes: [concurrency, observability]
severity: low
status: fixed
topic: null
occurrences: 4
---

# INC-0048 - Citing an identifier in the same parallel tool block that creates it makes the citation a guess

**Catalog:** [root](../catalog/README.md) / [concurrency](../catalog/concurrency/README.md)

**Cost:** A message cited a commit identifier that had not yet been produced, so the citation was a guess presented as a fact. Caught before it could mislead anyone, but a wrong identifier in a record is unfalsifiable by a reader who trusts it.

## Signature - how you recognise it

One batch of parallel tool calls contains both a step that creates an identifier (commit hash, ticket number, file path) and a step that quotes it.

## What happened

An agent issued a commit and a message citing that commit's hash in the same parallel block. Calls in one block are independent, so the message could not have read the result of the commit; the hash it carried was predicted or invented.

## Root cause

Treating parallel calls as if they were sequential. Dependence between two steps is the exact case parallelism is not for, and the dependency was hidden because the value looks like something one 'knows' once the action is requested.

## Why it was hard to see

The action succeeds and the text reads plausibly. Nothing fails; the wrong identifier is simply wrong.

## Fix

Run the creating step first, read the identifier from its result, then cite it in a later call.

## Verification

The corrected citation was read from the commit's own output.

## Transferable rule

> Never cite an identifier produced by a step that has not returned yet. If call B needs a value from call A, B goes in a later block and quotes what A actually returned.

## Recurrences

Occurrences: 4. Repeats of this failure are recorded here instead of as new incidents.

- 2026-11-19 - A lead issued a teammate spawn and the write of a tracking file in one parallel batch, so the file recorded a thread id the spawn had not yet returned; a later retain call on that id failed with thread not found.
- 2026-11-26 - A tracking log and a durable note recorded a guessed commit hash in the parallel batch that created the commit. The lead found the mismatch after reading the commit output.
- 2026-11-26 - Second time in one evening: a lead wrote a spawned thread's id into a retain call, a roster and a memory note in the batch after the spawn, from an id it had composed, not read; the retain failed with thread not found. The roster write must now quote the spawn output line.

## Related

[INC-0041](./INC-0041-a-verifier-that-lived-and-answered-can-still-deliver-an-unus.md)
