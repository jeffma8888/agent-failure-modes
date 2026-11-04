---
id: INC-0573
title: Teammate replies stopped reaching the lead for about 25 minutes while their files landed on disk
date: 2026-11-04
classes: [delegation]
severity: medium
status: mitigated
---

# INC-0573 - Teammate replies stopped reaching the lead for about 25 minutes while their files landed on disk

**Cost:** Finished work sat unread for up to 25 minutes, including the fix for a red main.

## Signature - how you recognise it

A teammate is finished and its files exist, but no reply message arrives.

## What happened

Between about 00:43 and 01:05 the replies of eight teammates never reached the lead. Their files were on disk, including the main red fix, which sat unread. The lead then ruled that when the state list shows a teammate finished with no reply, the lead reads that teammate report path on disk at once. Two more replies were lost later and their files again arrived.

## Root cause

The reply channel failed silently while the file channel worked.

## Why it was hard to see

No error shows; the lead waits for a message that is not coming.

## Fix

Read the report path on disk whenever the state shows a finished teammate with no reply.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> When a teammate shows finished with no reply, read its report file at once; do not wait for the message.

## Related

[INC-0449](./INC-0449-the-lead-missed-six-teammate-replies-across-a-context-compac.md)
