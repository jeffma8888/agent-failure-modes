---
id: INC-0407
title: A lead signature line containing the assistant's product name failed the scrub
date: 2026-11-02
classes: [tooling-paths]
severity: low
status: fixed
---

# INC-0407 - A lead signature line containing the assistant's product name failed the scrub

**Cost:** A commit would have been blocked or a banned name published.

## Signature - how you recognise it

A signature line failed the scrub.

## What happened

a lead signature line containing the assistant's product name failed the leak scrub

## Root cause

the signature used the product name instead of the role name

## Why it was hard to see

The signature is habit text, outside the text people check for names.

## Fix

Sign with a role name, never a product name

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Sign with a role name; a product name in a signature line fails the scrub

## Related

[INC-0238](./INC-0238-a-leak-scanner-matched-part-of-a-generated-name-and-blocked.md) [INC-0370](./INC-0370-a-scrub-command-was-refused-as-a-broad-home-directory-scan-b.md)
