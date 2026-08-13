---
id: INC-0003
title: A slow test suite makes a product unbuildable by the loop
date: 2026-08-04
classes: [stage-timeout, spec-and-scope, test-isolation]
severity: high
status: fixed
---

# INC-0003 - A slow test suite makes a product unbuildable by the loop

**Cost:** About 7 hours across 3 iterations shipped 0 commits for one product; the correct fix touched a config the loop was not authorized to change.

## Signature - how you recognise it

One team consistently fails while sibling teams on the same infrastructure ship normally. Every failed engineer and tester attempt log is a 48-byte 'timed out' stub. Shrinking the spec does not help.

## What happened

A build loop had four products. Three shipped normally; the fourth went 3 iterations / 7 hours / 0 ships. Attempt logs were all identical 48-byte timeout messages. The natural hypothesis was rate-limiting by the model provider. Wrong.

## Root cause

The product's own test suite took 504 seconds. The agent CLI's per-invocation cap was 600 seconds. That left about 96 seconds for the engineer or tester agent to read, edit, verify and write its output file - so every attempt died right after the suite finished. The spec-size hypothesis was falsifiable and falsified: specs shrank from 13KB to 6KB and a two-line change still failed.

## Why it was hard to see

The failure looked like provider throttling (concurrent teams, some green some red is throttle-shaped), and the local test suite was in fact all green. Only a wall-clock measurement of the suite against the CLI cap made the shape visible.

## Fix

Make the suite fast. The product's own planner had proposed pytest parallelism in prior iterations; the loop could not act on it because that required relaxing a 'dev-dep: pytest only' quality bar - an OPERATOR decision, not an agent one. Adding pytest-xdist as a locked dev dep and setting `addopts = "-q -n auto"` cut the suite from 504s to 89s (5.7x). Put the parallelism in `addopts`, not in one call site, so every call site inherits it.

## Verification

Suite: 504s to 89s across three consecutive runs. The next iteration shipped in 46 minutes, every step producing output on attempt 1.

## Transferable rule

> A loop CAN correctly diagnose its own blocker and still be structurally unable to fix it if the fix touches a policy only the operator owns - so when a team stalls, READ ITS PLANNER'S NOTES FIRST. If a suite approaches the per-step timeout, the product is unbuildable by the loop; fix the SUITE, and put the fix in a config all call sites inherit.

## Related

[INC-0002](./INC-0002-the-hard-per-step-wall-clock-cap-is-the-number-one-cause-of.md) [INC-0004](./INC-0004-a-monotonically-growing-required-reading-file-silently-kills.md)
