---
id: INC-0489
title: A rule written in teammate briefs was broken by the lead in its own shell
date: 2026-11-02
classes: [delegation]
severity: low
status: mitigated
---

# INC-0489 - A rule written in teammate briefs was broken by the lead in its own shell

**Cost:** None incurred: the slip was seen in the next command and undone before any run.

## Signature - how you recognise it

The author of a standing rule broke it by reflex while setting up a new work tree.

## What happened

While preparing a new work tree, the lead linked the dependency directory from another tree by reflex. The standing tool rule, which the lead had pasted into every teammate brief, forbids linking dependency directories between work trees. The lead noticed the link in the next command, before any install, build or test ran, and removed it by its exact recorded name.

## Root cause

The rule lived in the briefs written for others, and the lead's own habit ran ahead of it, with no step that checked the lead's own commands against the rules.

## Why it was hard to see

The command was routine and looked like ordinary setup, and the rule is one the lead believes it follows.

## Fix

Read each of the lead's own commands against the standing rules before running it, and remove any slip by its exact recorded name before any run.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A rule written in teammate briefs binds the lead's own shell too; read your own command against the standing rules before running it, and undo any slip by its exact recorded name before any run.

## Related

[INC-0384](./INC-0384-the-lead-stamped-a-brief-four-minutes-ahead-of-the-clock-aga.md) [INC-0452](./INC-0452-a-ruling-cannot-override-a-teammate-tool-rules-so-the-lead-s.md)
