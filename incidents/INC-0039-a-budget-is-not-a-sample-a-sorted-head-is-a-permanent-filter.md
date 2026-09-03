---
id: INC-0039
title: A budget is not a sample: a sorted head is a permanent filter, disguised as a performance knob
date: 2026-08-29
classes: [observability, spec-and-scope, false-green]
severity: high
status: fixed
---

# INC-0039 - A budget is not a sample: a sorted head is a permanent filter, disguised as a performance knob

**Cost:** Eight of eleven research dimensions were STRUCTURALLY unreachable for as long as the backlog stayed large. Every downstream artifact reported them as under-researched instead of unreached, and the resulting register was about 40% one dimension with nothing explaining why.

## Signature - how you recognise it

A bounded pass reports steady healthy throughput, but its OUTPUT is concentrated in one region of the input space - and that region is the one that sorts first.

## What happened

A verification pass capped its per-tick network cost by taking the first N of a sorted file listing. Candidate filenames began with the research topic, so alphabetical order correlated exactly with the dimension being sampled. With 861 queued candidates spanning all 11 dimensions and a 120-per-tick budget, the verified pool contained exactly 3 of the 11 - and the other 8 could never be reached while the queue stayed longer than the budget.

## Root cause

A truncation whose ORDER correlates with the PROPERTY being measured is not a sample, it is a filter - and it is applied on every tick, forever. It survives review because it reads as a resource limit: the code says 'cap the cost', and the bias is a property of the input's naming, which lives somewhere else entirely.

## Why it was hard to see

The pass is genuinely bounded, genuinely fast, and its own logs are honest about how many records it looked at. Nothing reports what it never looked at. The bias only appears if you compare the DISTRIBUTION of the output against the distribution of the input, which no health check did.

## Fix

Round-robin across the dimension you actually care about, best-first WITHIN each bucket, cycling until the budget is spent. A thin bucket contributes everything it has and drops out, so no budget is reserved and then wasted. Give unclassifiable items their OWN bucket rather than dropping them - an item whose category cannot be read is exactly the one a human needs to see, and filtering it before the gate leaves it queued forever.

## Verification

The replacement selection function is committed with the measurement in its own docstring, so the reasoning cannot drift from the code: 861 queued across 11 dimensions, a verified queue of 99 containing exactly three, and the note that the eight missing dimensions were unreachable rather than under-researched.

## Transferable rule

> For ANY truncated pass, ask whether the ORDER is independent of the PROPERTY being measured. Filename, insertion, directory and id order almost never are - so a sorted head is a permanent filter wearing a performance knob's clothes. Round-robin across the dimension you care about, best-first inside each bucket, and give unclassifiable items their own bucket.

## Provenance

Where this was observed, so the claim is checkable rather than anecdotal:

- https://github.com/jeffma8888/agent-gap-radar - tools/verify_quotes.py, function select_bounded, whose docstring records the measured distribution and why the previous sorted-head selection was a bias rather than a sample.

## Related

[INC-0026](./INC-0026-a-whole-batch-verification-veto-turns-one-bad-item-into-a-pe.md) [INC-0028](./INC-0028-when-two-distributions-overlap-there-is-no-threshold-change.md)
