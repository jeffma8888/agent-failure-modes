---
id: INC-0002
title: The hard per-step wall-clock cap is the number-one cause of lost work
date: 2026-08-04
classes: [stage-timeout, observability, checkpoint]
severity: critical
status: mitigated
---

# INC-0002 - The hard per-step wall-clock cap is the number-one cause of lost work

**Cost:** About 9 hours across 2 full iterations produced zero shipped commits: 8 attempts, 8 timeouts, 0 output.

## Signature - how you recognise it

Every attempt log for a specific step is exactly the same tiny size and reads only 'timed out after 600s'. Two full iterations produce nothing while sibling teams on the same infrastructure ship normally.

## What happened

A multi-team build loop lost 9 hours of wall clock across 8 attempts on a single team's planning step. Every attempt log was 48 bytes - the timeout message and nothing else, meaning the agent produced no output before being killed. Sibling teams on the same box in the same window shipped normally.

## Root cause

The agent CLI enforced a hard 600-second cap per invocation, beneath any outer timeout the loop set. The step had grown to require reading and rewriting a large input file that exceeded the time budget, so every attempt was killed mid-work. The loop's success predicate ('output file exists') hid this: on the rare occasion the work landed before 600s, the step's median was reported as healthy instead of AT the cap.

## Why it was hard to see

The outer timeout on the loop was set to 1800s and looked fine; the real cap is two layers below. And the loop's own telemetry showed the step passing sometimes, not dying at exactly 600 every time.

## Fix

Three changes in priority order. (a) Put a write-early rule in every role prompt: a step counts as SUCCESS the moment it writes a minimal-but-complete output file, then refines in place. (b) Add per-step duration metrics to the dispatcher so a median at the cap is visible. (c) Give the largest inputs a character budget and enforce it (see INC-0004).

## Verification

After the write-early rule shipped, the same team's next iteration produced output on attempt 1 even though the attempt still hit 600s - because the agent had checkpointed its minimal artifact within the first 8 minutes.

## Transferable rule

> A per-step timeout you did not set is often the real timeout. If a step's attempt logs are all the same tiny size, its median is AT the cap, not near it. Fix: write-early checkpoint (minimal complete output first, then refine in place), and always report the duration DISTRIBUTION, never a single-shot healthy flag.

## Provenance

Where this was observed, so the claim is checkable rather than anecdotal:

- https://github.com/jeffma8888/agent-foundry - the orchestrator whose hard per-stage cap this describes; the cap is enforced by the agent CLI beneath the timeout the loop sets itself.
- https://github.com/jeffma8888/proactive-loop-agent - the product loop whose planning stage burned two consecutive iterations this way: 8 attempts, 8 timeouts, ~9 hours, no output, every attempt log 48 bytes.

## Related

[INC-0006](./INC-0006-checkpoint-first-a-killed-step-that-already-wrote-its-output.md) [INC-0007](./INC-0007-diagnose-stalled-work-from-the-duration-distribution-not-the.md)
