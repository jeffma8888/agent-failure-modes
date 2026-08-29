---
id: INC-0035
title: Two individually safe options are unsafe together when their combination leaves a consumer unable to distinguish two states
date: 2026-08-28
classes: [false-green, spec-and-scope]
severity: high
status: fixed
---

# INC-0035 - Two individually safe options are unsafe together when their combination leaves a consumer unable to distinguish two states

**Cost:** Nothing shipped - a second reviewer found the hole before the combined path ran. Had it run, the downstream publisher would have consumed unverified evidence, which is the single guarantee the whole verification stage exists to provide.

## Signature - how you recognise it

Two changes, each reviewed and each safe. Nothing in either diff is wrong. The defect exists only in the state the pair produces, and it shows up as a consumer reading a collection whose members no longer all mean the same thing.

## What happened

A verification stage was given a per-run bound so it could not spend unbounded network time, and separately it left verified items in place rather than moving them. Each choice was defensible alone. Together they meant the queue held verified items and never-examined items with no marker separating them - so the downstream publisher, told to consume 'the queue', could no longer tell which was which and would have published unverified evidence.

## Root cause

Both options changed the MEANING of a shared collection rather than its contents. The bound makes 'everything here has been checked' false; leaving items in place removes the only signal of which ones were. Neither is visible in a single-change review, because the invariant they jointly break is not stated in either diff.

## Why it was hard to see

Review is per-change and each change is correct in isolation. No test fails, because a test for either feature exercises the other's absent half. And the resulting state is silently plausible: the collection is well-formed, the counts look right, and the consumer's own code is untouched.

## Fix

Give the verified set its own destination, so 'verified' is a LOCATION rather than a claim, and point the consumer at that location only. Wherever a stage is bounded, make the bound visible in the artifact it produces - state how many items were examined out of how many exist - so a consumer can never mistake a bounded pass for a complete one.

## Verification

The staged destination shipped as its own change with its own tests, and the driver was repointed at it. A dry run then confirmed the publisher considers only network-verified items: four accepted out of 129 staged, with the 861 unexamined items untouched.

## Transferable rule

> Ask of any two individually safe options whether their COMBINATION leaves a consumer unable to distinguish two states. A per-run bound plus an in-place 'done' marker is the canonical pair: the bound makes 'all of these were checked' false, and the in-place marker deletes the evidence of which ones were. Make the checked set a separate LOCATION, and make any bound visible in the artifact.

## Provenance

Where this was observed, so the claim is checkable rather than anecdotal:

- https://github.com/jeffma8888/agent-gap-radar - the `--verified` staging destination (a747cc8), added so that bounding a verification pass and promoting from it stay honest at the same time.

## Related

[INC-0026](./INC-0026-a-whole-batch-verification-veto-turns-one-bad-item-into-a-pe.md) [INC-0034](./INC-0034-a-malformed-item-aborts-the-per-item-pass-and-the-crash-rein.md)
