---
id: INC-0081
title: Reviewers and QA wrote absolute home paths and notes paths into repository docs, and only the push guard caught them
date: 2026-10-30
classes: [tooling-paths, observability]
severity: low
status: fixed
---

# INC-0081 - Reviewers and QA wrote absolute home paths and notes paths into repository docs, and only the push guard caught them

**Cost:** Minor: four push attempts in one hour were blocked and reworded; nothing leaked because the guard ran before each push.

## Signature - how you recognise it

Documents authored by several agents cite local files by absolute path or by the location of private lead notes.

## What happened

Reviews and coverage records included absolute home paths and paths of private notes. A leak guard rejected the pushes four times in one hour across two reviews and three coverage files.

## Root cause

Task templates did not say how to cite private notes, and agents copy the paths they were shown.

## Why it was hard to see

The text is correct and useful locally, so authors see no problem until a pattern scan runs at the last step.

## Fix

Task templates now say to cite lead notes by file name only and use repository-relative paths; the guard runs before each push.

## Verification

Checked: the guard blocked each occurrence before push. Not checked: whether the new template wording stops recurrence.

## Transferable rule

> Tell authors how to cite private material in the brief, and keep the leak scan as a pre-push gate rather than the only control.

## Related

[INC-0074](./INC-0074-a-brief-named-a-source-directory-the-repository-does-not-hav.md)
