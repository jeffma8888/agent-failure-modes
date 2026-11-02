---
id: INC-0376
title: A signed design heading outranked a plan census parenthetical when two reviews disagreed on a file location
date: 2026-11-01
classes: [spec-and-scope]
severity: low
status: fixed
---

# INC-0376 - A signed design heading outranked a plan census parenthetical when two reviews disagreed on a file location

**Cost:** Two reviews pulled the same file to different directories until the signed text was read.

## Signature - how you recognise it

Two reviews gave different locations for the same file.

## What happened

two reviews disagreed on where a hook file lives: a signed low-level design heading (src/payload/hooks/) named one directory while a parenthetical in the plan census implied another; the lead ruled for the signed heading

## Root cause

a secondary summary was weighed equally with the signed design text

## Why it was hard to see

Both sources looked authoritative, and the parenthetical was easy to quote.

## Fix

Read the signed design text before choosing between conflicting reviews

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> When reviews disagree on a file location, read the signed design text first; it outranks a plan parenthetical

## Related

[INC-0369](./INC-0369-a-bare-syntax-check-resolved-to-a-different-runtime-that-ign.md) [INC-0390](./INC-0390-a-dispatch-packet-written-for-a-future-branch-went-stale-whe.md) [INC-0391](./INC-0391-an-implementer-s-evidence-admitted-one-case-that-contradicte.md) [INC-0401](./INC-0401-a-dispatch-packet-called-a-root-absent-an-hour-after-it-had.md) [INC-0413](./INC-0413-an-acceptance-document-cited-a-ruling-that-did-not-yet-exist.md)
