---
id: INC-0518
title: A landing tool read a bare file name as a test-root name, so a file was left out of a landing and the identifier check failed
date: 2026-11-02
classes: [tooling-paths]
severity: low
status: mitigated
---

# INC-0518 - A landing tool read a bare file name as a test-root name, so a file was left out of a landing and the identifier check failed

**Cost:** A landing was incomplete and an identifier check failed until the omission was found.

## Signature - how you recognise it

A tool accepts root names and file paths, and a bare file name is taken as a root name.

## What happened

A landing tool took a bare file name given for the backlog as the name of a test root. The backlog file was therefore not landed as a file, and the identifier check failed. The curator assignment records the cause as a bare file name read as a root name.

## Root cause

The tool guessed the kind of a bare token instead of requiring an explicit form.

## Why it was hard to see

The tool ran without an error of its own, so the omission showed only as a downstream check failing.

## Fix

Pass a non-root file in a form the tool cannot read as a root name, and compare the landing list with the intended files before it runs.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A tool that accepts both root names and file paths must not guess which one a bare token is; list what it will land and compare with what was intended before it runs.

## Related

[INC-0490](./INC-0490-a-wrapper-exited-zero-while-a-step-record-said-the-step-fail.md)
