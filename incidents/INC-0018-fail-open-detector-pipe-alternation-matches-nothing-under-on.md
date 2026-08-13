---
id: INC-0018
title: Fail-open detector: pipe alternation matches nothing under one regex flavor
date: 2026-08-05
classes: [detector-fail-open]
severity: high
status: fixed
---

# INC-0018 - Fail-open detector: pipe alternation matches nothing under one regex flavor

**Cost:** The credential-expiry branch of a watchdog could never have fired for the several days it was live - so a real credential outage would not have been caught.

## Signature - how you recognise it

A monitor built on `grep -E 'A\|B'` or `grep 'A\|B'` prints nothing while the eye clearly sees both patterns in the log. A negative result is being read as health.

## What happened

A watchdog used shell grep with escaped-pipe alternation (`\|`) as its match pattern. In this shell, `grep` was aliased to ripgrep. Ripgrep is regex-by-default and reads `\|` as an escaped LITERAL pipe - not as alternation. The pattern returned zero hits on inputs that clearly contained both alternatives.

## Root cause

Two shell-tool assumptions differed. BSD grep (macOS default) uses BRE, where `\|` is alternation only with `-E`. Ripgrep uses ERE-shaped regex by default and treats `\|` as a literal. The single-backslash form is a footgun that reads correctly to a human familiar with only one of the two flavors.

## Why it was hard to see

A negative result from a matcher is indistinguishable from health. Nothing errors, nothing warns.

## Fix

Use plain `|` for alternation, never `\|`. Do not rely on `-E` to mean 'extended regex' - in some tools it means something else entirely (e.g. `--encoding` in ripgrep). Match case correctly or pass `-i`. And the durable practice: for any detector or alarm, feed it a known-bad sample and assert it fires BEFORE trusting it. Fail-open monitoring is worse than none.

## Verification

A synthetic 'credential refresh failed' line in a tmp file caused the fixed matcher to fire; the same line under the old pattern was silent. Two-sided self-test now runs before every alarm cycle.

## Transferable rule

> A negative result from a detector is NOT evidence of health. Every alarm must be proven against a KNOWN-BAD sample before it is trusted (fires) and against a known-good sample (does not fire). Fail-open monitoring is worse than none. And know your regex flavor: `\|` is alternation in BRE but a LITERAL pipe in ripgrep - use plain `|`.

## Related

[INC-0019](./INC-0019-fail-open-detector-parsing-the-wrong-column-reports-healthy.md)
