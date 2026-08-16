---
id: INC-0005
title: A killed step with no verdict token is read as REVERTED
date: 2026-08-10
classes: [verdict-token, stage-timeout]
severity: critical
status: mitigated
---

# INC-0005 - A killed step with no verdict token is read as REVERTED

**Cost:** Two of three iterations reverted with every gate green, destroying verified work.

## Signature - how you recognise it

An iteration passes every gate, tests are green, git status is clean - and the loop reverts anyway with no error message. The final step's log ends mid-verification.

## What happened

A ship step was expected to write one of two verdict tokens: PUSHED or REVERTED. A parser downstream read that token to decide whether to keep the iteration's work or reset to origin. On several consecutive iterations the step was killed by the per-stage cap before it wrote a token. The parser saw no token and defaulted to REVERTED. All-green work was destroyed.

## Root cause

A parser that accepted only two literal tokens and defaulted to the pessimistic one on absence. Combined with a step instructed to verify thoroughly (suite pass, spec audit, doc audit, fresh-clone check) under a hard 600s cap, it predictably ran out of time before writing its verdict.

## Why it was hard to see

The step is doing exactly what it was told to do: being careful. The parser's pessimistic default is a reasonable safety choice in isolation. The failure is that 'thoroughness' and 'cap' together produce 'no token' more often than the parser designer expected. And the obvious fix had already been applied once, in the opposite direction. An earlier version had the step write its verdict token EARLY as a placeholder it intended to overwrite; four iterations of already-green work were lost that way, each killed after its own gates had passed while the artifact still held the placeholder. So placeholders were banned - and that ban is what produced the no-token revert, which then destroyed two of three consecutive iterations. The failure mode inverted under its own fix, which is why the surviving rule has to be narrow: write the REAL verdict early. Not 'write something early', and not 'never write early'.

## Fix

Two changes. (a) Never write a placeholder token - only the real verdict, but write it EARLY. Budget verification to the cap: decide on decisive evidence only (full suite result + git status showing intended changes), and write the token by minute 8. Reviewer nits, prose fixes, doc-wording edits are NOT ship blockers; record them as follow-ups. (b) On the parser side, distinguish 'no token due to timeout' (retry-safe) from 'REVERTED' (destructive) whenever the token stream carries any indication of the underlying cause.

## Verification

The next four iterations wrote their token by minute 6-8 of a ~12-minute step and all shipped correctly. Status stays MITIGATED rather than fixed, for three reasons that are all still live. The parser still collapses 'killed before deciding' and 'decided not to ship' into one destructive outcome. The ship step is the one role FORBIDDEN from checkpoint-first, because its verdict has to be the artifact's last line, so the mechanism that protects every other role structurally cannot protect the verdict itself. And retries re-run the whole verification from scratch, so four attempts are one correlated failure rather than four independent chances. What actually shipped is a behavioural budget written into a prompt, which is the weakest kind of guarantee: it holds only while the agent obeys it under time pressure. See INC-0025.

## Transferable rule

> A machine-parsed verdict token that defaults to the destructive answer on absence is a critical safety hazard when its writer runs under a hard timeout. Write the verdict EARLY on decisive evidence only, budget verification to the cap, and treat lower-priority audits as follow-ups.

## Provenance

Where this was observed, so the claim is checkable rather than anecdotal:

- https://github.com/jeffma8888/agent-foundry - the verdict parser and the release-gate role card that this incident is about: `parse_ship_action` in `foundry.py` accepts only PUSHED/REVERTED and returns None otherwise, and `roles/final.md` carries the verify-first exception that forbids this one role from checkpointing its verdict.

## Related

[INC-0002](./INC-0002-the-hard-per-step-wall-clock-cap-is-the-number-one-cause-of.md) [INC-0006](./INC-0006-checkpoint-first-a-killed-step-that-already-wrote-its-output.md) [INC-0025](./INC-0025-retrying-a-killed-verification-step-without-resumable-eviden.md)
