---
id: INC-0519
title: A root was passed to a landing helper by name and by path, and the cleanup removed a file twice and stopped
date: 2026-11-02
classes: [tooling-paths]
severity: low
status: mitigated
---

# INC-0519 - A root was passed to a landing helper by name and by path, and the cleanup removed a file twice and stopped

**Cost:** One landing was finished by hand.

## Signature - how you recognise it

The same item is given to a helper in two forms, and a later step acts on it twice.

## What happened

A pending root was passed to the landing helper both by its bare name and by its coverage path. The cleanup step removed the same file twice and stopped halfway, and the landing was finished by hand. The rule is to pass a pending root by its bare name only.

## Root cause

The helper did not de-duplicate an item that reached it in two forms.

## Why it was hard to see

Each form is valid alone, so only the combination fails, and it fails in the cleanup after the main work.

## Fix

Pass each item once, in the one documented form.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Give a landing helper each item once and in its one documented form; an item named twice is a cleanup that can fail halfway.

## Related

[INC-0490](./INC-0490-a-wrapper-exited-zero-while-a-step-record-said-the-step-fail.md)
