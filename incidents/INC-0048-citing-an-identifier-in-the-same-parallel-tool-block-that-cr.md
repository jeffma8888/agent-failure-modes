---
id: INC-0048
title: Citing an identifier in the same parallel tool block that creates it makes the citation a guess
date: 2026-10-28
classes: [concurrency, observability]
severity: low
status: fixed
---

# INC-0048 - Citing an identifier in the same parallel tool block that creates it makes the citation a guess

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

## Related

[INC-0041](./INC-0041-a-verifier-that-lived-and-answered-can-still-deliver-an-unus.md)
