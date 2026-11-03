---
id: INC-0531
title: A graceful pause worked because each in-flight teammate finished one step, wrote a checkpoint and left its workspace as it was
date: 2026-11-02
classes: [checkpoint]
severity: low
status: mitigated
---

# INC-0531 - A graceful pause worked because each in-flight teammate finished one step, wrote a checkpoint and left its workspace as it was

**Cost:** None incurred; no finished work was redone on resume.

## Signature - how you recognise it

A team stops on request and resumes later, and every member continues from its own recorded state.

## What happened

When the owner asked for a graceful pause, no new job, run, merge or review started. In-flight teammates were told to finish the current step only, append a pause checkpoint to their report, keep their worktree and database cluster as they were, and stop. Idle teammates got no new work, and shared services were not touched. On the resume message every teammate continued from its own checkpoint and an in-flight slice was continued, with no finished work restarted.

## Root cause

Not a failure: a pause that is bounded to one step per member and records the state needed to continue.

## Why it was hard to see

A pause is easy to ask for and easy to get wrong by killing work mid-step or by leaving no record of where each member stopped.

## Fix

Repeat the pattern: finish the current step, write a resume checkpoint, leave workspace and processes as they are.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> To pause a team safely, tell each in-flight teammate to finish only the current step, write a resume checkpoint, and leave its worktree and processes as they are; resume from those checkpoints and never redo finished work.

## Related

[INC-0449](./INC-0449-the-lead-missed-six-teammate-replies-across-a-context-compac.md)
