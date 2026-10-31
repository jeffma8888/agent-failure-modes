---
id: INC-0220
title: A reviewer proposed text was at risk of being applied by its own author
date: 2026-10-31
classes: [delegation, identity-and-keying]
severity: medium
status: fixed
---

# INC-0220 - A reviewer proposed text was at risk of being applied by its own author

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

The author could soften the reviewer text.

## What happened

A reviewer exact proposed text was applied by someone with no independent check, with no backup of the pre-edit set.

## Root cause

A reviewer exact proposed text was applied by someone with no independent check, with no backup of the pre-edit set.

## Why it was hard to see

Applying text looks mechanical.

## Fix

Apply it through a third party who is not the original author, back up the pre-edit set with digests, then have the proposer re-review and a separate QA re-check

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Apply a reviewer exact text through a third party, with digested backups, a proposer re-review and a separate re-check

## Related

[INC-0206](./INC-0206-a-guessed-commit-id-was-sent-to-two-teammates.md)
