---
id: INC-0526
title: A reviewer was named after checking commit authorship only, and the reviewer had judged the root's cases in an earlier review file
date: 2026-11-02
classes: [delegation]
severity: low
status: mitigated
---

# INC-0526 - A reviewer was named after checking commit authorship only, and the reviewer had judged the root's cases in an earlier review file

**Cost:** One review was delayed and reassigned.

## Signature - how you recognise it

An author-conflict check covers commits, and the conflict is in a review file.

## What happened

A reviewer was named for a slice after checking commit authorship but not review files. The reviewer had written an earlier review file that judged the cases of the slice root, so it stopped at its own author check, which was correct. The assigner now searches the review folder for the root identifier and reads the author of each hit for every candidate before naming a reviewer.

## Root cause

The author check was defined over commits, and a review is authorship of a judgement that lives in a different file.

## Why it was hard to see

A reviewer who never committed to the root looks independent in the log.

## Fix

Search commits and review files for the root identifier and read each hit author, for every candidate.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> An author-conflict check covers review files as well as commits: search both for the root identifier and read the author of every hit before the reviewer is named.

## Related

[INC-0517](./INC-0517-two-reviewers-were-named-who-had-written-or-judged-the-roots.md) [INC-0507](./INC-0507-an-independence-rule-did-not-say-what-counts-as-an-agent-or.md)
