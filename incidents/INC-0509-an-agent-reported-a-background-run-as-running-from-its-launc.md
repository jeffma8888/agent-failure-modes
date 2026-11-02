---
id: INC-0509
title: An agent reported a background run as running from its launch, but the task had only echoed a prompt and no test process existed
date: 2026-11-02
classes: [observability]
severity: low
status: mitigated
---

# INC-0509 - An agent reported a background run as running from its launch, but the task had only echoed a prompt and no test process existed

**Cost:** A false running report until the agent rechecked and corrected it; no result was recorded from the missing run.

## Signature - how you recognise it

A background task exists and a launch was acknowledged, but no process of the run exists.

## What happened

An agent reported a background run as admitted and running from its launch. The task had only echoed an interactive prompt, and no test process existed. The agent found this on its own recheck and corrected the report. A started task had been taken for a started run.

## Root cause

The report was based on the launch of the wrapper task, not on output of the run itself.

## Why it was hard to see

The task handle is real and shows as started, so nothing looks wrong until someone looks for the process.

## Fix

Report a run as running only from its own output, such as a launch line or a process id that exists.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Report a run as running only from its own output (a launch line, a PID that exists); a started task is not a started run.

## Related

[INC-0490](./INC-0490-a-wrapper-exited-zero-while-a-step-record-said-the-step-fail.md)
