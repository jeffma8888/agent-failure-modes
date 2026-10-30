---
id: INC-0099
title: A test reassignment written only in prose was not enforced by any tool
date: 2026-10-30
classes: [spec-and-scope, identity-and-keying]
severity: medium
status: fixed
---

# INC-0099 - A test reassignment written only in prose was not enforced by any tool

**Cost:** Minor: caught in review, a re-check or acceptance before it shipped.

## Signature - how you recognise it

A rule about which row owns a test exists in text, and tools disagree or ignore it.

## What happened

A test reassignment was recorded only in prose, so the row selector, the activation diff check and the identity check could each read it differently or not at all.

## Root cause

There was no single machine-readable source for the assignment.

## Why it was hard to see

The prose is clear to a reader, so the missing enforcement is invisible.

## Fix

Keep one registry file that the row selector, the activation diff check and the identity check all read.

## Verification

Checked by the engineer, reviewer or lead who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Put a reassignment in one registry that every enforcing tool reads.
