---
id: INC-0025
title: Retrying a killed verification step without resumable evidence is one failure, not four chances
date: 2026-08-15
classes: [stage-timeout, verdict-token, checkpoint]
severity: high
status: open
---

# INC-0025 - Retrying a killed verification step without resumable evidence is one failure, not four chances

**Cost:** No new loss to report: this is the measured residual of INC-0005, whose abort path has converted a finished, reviewed iteration into a total loss nine times.

## Signature - how you recognise it

Every attempt of the same step fails identically, at the same duration, with the same short timeout log. The retry count in the logs looks like resilience, while the outcome is exactly the outcome of one attempt.

## What happened

A verification/ship step runs under a hard per-step cap and is retried up to four times. Each retry restarts verification from zero, because the retry instruction deliberately does not read the previous attempt - a sound default, since the dominant failure leaves a log containing nothing but a timeout line. For most roles that is correct. For the verification step it is not: its artifact is EVIDENCE, and evidence about an unchanged tree is reusable. So the same full suite, the same audits and the same clean-clone re-run are recomputed on every attempt, against the same budget, with the same result.

## Root cause

Retries are independent trials only when the failure is random. A deterministic over-budget step fails the same way every time, so N retries of one plan is a single experiment repeated N times. The framework had nowhere to record PARTIAL verification: the only state shared between attempts was the working tree, so no attempt could tell what an earlier one had already proved.

## Why it was hard to see

A retry count reads as safety. The logs show four attempts rather than one, so the mechanism looks like it is working, and the wasted wall clock is charged to the cap rather than to the retry design. The natural fix is also a trap: letting the step write a 'partially verified' token re-creates the placeholder that INC-0005's ban existed to stop, because a progress marker living in the channel a parser reads as the verdict IS a placeholder verdict. The progress channel and the verdict channel have to be physically different things.

## Fix

Three parts, in the order that pays. (1) SHRINK THE CRITICAL PATH FIRST - resumption raises the ceiling, deleting work lowers the floor. Keep pre-ship only what is decisive or irreversible: the suite result, a status showing only intended changes, and any secret-leak scan, since a pushed secret cannot be unpushed. Move doc-accuracy checks, spec audits and clean-clone re-runs to the post-release check that already re-runs them, and demote nits to follow-ups. (2) GIVE THE STEP A RESUMABLE EVIDENCE LEDGER, outside the verdict channel: prose lines above the sentinel, each naming the check, its result, and a KEY identifying the exact input state it was computed against - the head commit plus a hash over the pending diff and every untracked file. On a retry, carry forward only the lines whose key still matches the tree and skip those checks; any mismatch voids the entire ledger. Unkeyed, a cached result is a false-green vector: it lets a retry ship on evidence gathered against a different tree. (3) MAKE 'KILLED' AND 'REFUSED' DIFFERENT ANSWERS. The runner already knows the attempt was killed, and that fact is discarded before the verdict is read. Treat a killed attempt holding no verdict as evidence about the MACHINE - retry, resume, do not destroy - and only an explicit refusal as evidence about the TREE.

## Verification

Not verified in production. Status is open, and the design is recorded before it ships rather than after. What IS measured, by reading the running system instead of its documentation: about 19,000 lines of framework code and 21 role cards contain no resumable-verification mechanism, no partial-verdict vocabulary and no evidence ledger of any kind; the retry instruction's own docstring states that it deliberately does not read the previous attempt; and the asymmetry part (3) asks for is ALREADY implemented one layer down, for a single sub-check whose 'could not complete' exit is explicitly treated as evidence about the machine rather than about the tree, on the stated grounds that a false revert destroys a whole green iteration. The principle was accepted in the small and never lifted to the layer that does the destroying. Acceptance test when it lands: force a kill mid-verification, assert the retry runs strictly fewer checks than the first attempt, and assert that a ledger whose key does not match the tree is discarded rather than trusted.

## Transferable rule

> A retry is a second chance only if something carried forward. Under a hard cap, N retries of a deterministic over-budget step is one failure repeated N times. Give the step a place to record partial results, key that record to the exact input state so a stale one is discarded, and keep it OUT of the channel a parser reads as the verdict.

## Provenance

Where this was observed, so the claim is checkable rather than anecdotal:

- https://github.com/jeffma8888/agent-foundry - `MAX_ATTEMPTS` and `retry_directive` in `foundry.py` (the retry text states in its own docstring that it deliberately does not read the previous attempt), the verify-first exception in `roles/final.md`, and the pre-ship clone gate whose 'could not complete' exit code is already treated as evidence about the machine rather than the tree - the asymmetry part (3) asks to be generalized.

## Related

[INC-0002](./INC-0002-the-hard-per-step-wall-clock-cap-is-the-number-one-cause-of.md) [INC-0005](./INC-0005-a-killed-step-with-no-verdict-token-is-read-as-reverted.md) [INC-0006](./INC-0006-checkpoint-first-a-killed-step-that-already-wrote-its-output.md)
