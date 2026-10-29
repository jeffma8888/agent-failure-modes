---
id: INC-0047
title: In an ordered replacement list, a general rule placed before a specific one consumes its match
date: 2026-10-28
classes: [tooling-paths]
severity: low
status: fixed
---

# INC-0047 - In an ordered replacement list, a general rule placed before a specific one consumes its match

**Cost:** Near miss, caught before the run. The rewrite would have left a mangled fragment of a path in place of a clean replacement, in a text-rewrite whose purpose was removing sensitive tokens.

## Signature - how you recognise it

A replacement list gains a broad pattern at the top, above a narrower pattern for a case the broad one also matches.

## What happened

A general rule (replace any local tool path) was prepended to a replacement list that already held a specific rule for one such path containing spaces. Applied in order, the general rule would have rewritten only the prefix of that path and left the remainder behind, so the specific rule no longer matched.

## Root cause

Ordered rewrite lists apply first-match or sequentially, so an earlier broad rule consumes text that a later narrow rule was written for. The new rule was reasoned about alone, not against the rules it overlaps.

## Why it was hard to see

Each rule is correct in isolation, the list looks like a set rather than a sequence, and the broken output is only wrong at the one overlapping case.

## Fix

Put specific rules first and general rules last. Rescan the rewritten output for the original tokens.

## Verification

Read the rule file after editing it, and checked the rewritten output for leftover original tokens rather than trusting the rule order.

## Transferable rule

> In ordered rewrite lists (sed scripts, replacement files, routing tables) put specific rules before general ones, and verify on the OUTPUT, not on the rules.

## Related

[INC-0030](./INC-0030-rewriting-a-region-by-slicing-between-two-markers-deletes-wh.md) [INC-0043](./INC-0043-an-anchored-replace-that-matches-a-prefix-of-a-line-is-still.md)
