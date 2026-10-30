---
id: INC-0102
title: A success control that forbade every connection pinned an implementation from before a later startup step that must connect
date: 2026-10-30
classes: [spec-and-scope, false-green]
severity: medium
status: fixed
---

# INC-0102 - A success control that forbade every connection pinned an implementation from before a later startup step that must connect

**Cost:** Minor: caught by a stop rule, a re-check or review before it shipped.

## Signature - how you recognise it

A control test forbids all connections while a later row adds a startup step that connects.

## What happened

A success control forbade every connection, which fixed the implementation as it was before a later startup step, such as a cleanup sweep, that has to connect. An engineer stopped on it.

## Root cause

The prohibition was written for the current startup and not for the contract that later rows add.

## Why it was hard to see

The control passes on the early implementation, so the conflict shows only when the later step lands.

## Fix

Forbid only the connections the contract forbids, and allow the later step explicitly.

## Verification

Checked by the engineer, reviewer or lead who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Write prohibitions against the full startup contract, not the current implementation.

## Related

[INC-0087](./INC-0087-an-import-level-audit-missed-helper-calls-that-needed-a-late.md)
