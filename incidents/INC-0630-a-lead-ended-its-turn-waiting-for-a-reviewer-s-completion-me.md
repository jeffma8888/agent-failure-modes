---
id: INC-0630
title: A lead ended its turn waiting for a reviewer's completion message while the reviewer's finished files were already on disk, and nothing moved for days
date: 2026-11-07
classes: [delegation]
severity: high
status: mitigated
---

# INC-0630 - A lead ended its turn waiting for a reviewer's completion message while the reviewer's finished files were already on disk, and nothing moved for days

**Cost:** Nothing moved from about 06:31 on 11/04 to 23:43 on 11/07, about three and a half days, while every output sat finished on disk.

## Signature - how you recognise it

A team is idle while the work it waits for is already on disk.

## What happened

A reviewer's two files were on disk, and the lead ended its turn waiting for the reviewer's completion message instead of acting on the files. The teammates then went to paused and no message came. Every output sat finished on disk the whole time, and only the long-lived test servers and the cluster stayed up. The lead called it a recurrence of the finished-work-unnoticed pattern.

## Root cause

The lead treated the message as the only signal that work was done.

## Why it was hard to see

A paused teammate sends no message, so waiting on a message alone cannot end by itself.

## Fix

Check the expected output files on disk, verify them, and act on them when the author is silent.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Act on verified on-disk outputs when the author is silent, and never end a turn waiting on a message alone.

## Related

[INC-0589](./INC-0589-the-only-copies-of-eight-reviewed-drafts-sat-untracked-in-on.md) [INC-0510](./INC-0510-mutation-restore-receipts-were-kept-only-in-tool-output-so-t.md)
