---
id: INC-0515
title: A rulings file grew past what a reader's tool returns, and a read of a named range was clipped, so compliance could not be certified
date: 2026-11-02
classes: [observability]
severity: low
status: mitigated
---

# INC-0515 - A rulings file grew past what a reader's tool returns, and a read of a named range was clipped, so compliance could not be certified

**Cost:** A required read could not be certified as done; the rule was changed to name sections instead of a range.

## Signature - how you recognise it

An instruction requires reading a range of a file whose size exceeds what the reader tool returns.

## What happened

The file of lead rulings grew past 660 KB, and a teammate reported that its read of a named range of rulings was clipped. An instruction to read the whole range could not be certified as followed. From then on a brief names the rulings to read, they are read by heading together with the standing rules quoted in the brief, and missing an unnamed old ruling is not a compliance failure.

## Root cause

A read requirement was written for a file that kept growing, with no bound on what the reader could actually receive.

## Why it was hard to see

Output that is clipped looks complete to the reader, and the instruction looked reasonable when the file was small.

## Fix

Name the sections to read by heading and quote the standing rules in the brief.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Do not require a read whose size exceeds what the reader tool returns; name the exact sections to read, and treat an unnamed old section as outside the compliance check.

## Related

[INC-0507](./INC-0507-an-independence-rule-did-not-say-what-counts-as-an-agent-or.md)
