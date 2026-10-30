---
id: INC-0082
title: An absence check passed vacuously because the forbidden text never matched the real title and the document may never have been read
date: 2026-10-30
classes: [false-green, detector-fail-open]
severity: medium
status: fixed
---

# INC-0082 - An absence check passed vacuously because the forbidden text never matched the real title and the document may never have been read

**Cost:** Caught in review before activation; the check would have stayed green while the forbidden text was present.

## Signature - how you recognise it

A test asserts a string occurs zero times in a page, and the count is zero for reasons unrelated to the page content.

## What happened

An exact-text count-zero check never failed because the seeded title carried an extra suffix, so the exact string was never present. A whole-document variant would also pass on an empty or error page.

## Root cause

The check had no positive control: nothing proved the same read could find any text at all, and exact matching ignored the real title shape.

## Why it was hard to see

Zero occurrences looks like success, and a missing or error document gives the same result as a clean one.

## Fix

Use substring checks on both the served bytes and the parsed DOM plus the title, each paired with a same-document positive control, a string the same read must find.

## Verification

Checked in review by reading the seeded title and the assertion. Not checked: runtime behavior, the suite was still pending.

## Transferable rule

> Every absence assertion needs a positive control from the same read, and matching must be substring-tolerant of the real data shape.
