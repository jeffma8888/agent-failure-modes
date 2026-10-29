---
id: INC-0058
title: A broad exception handler hid the difference between 'not found' and 'unknown name'
date: 2026-10-29
classes: [false-green, tooling-paths]
severity: low
status: fixed
---

# INC-0058 - A broad exception handler hid the difference between 'not found' and 'unknown name'

**Cost:** Caught while writing tests, before release. A command-line tool would have reported an unknown name as 'no eligible candidate', with the wrong exit code, and a test would have passed on the bug.

## Signature - how you recognise it

A handler catches a parent exception type first, and a sibling error with a different meaning is a subclass of it.

## What happened

In Python, a missing-key error is a subclass of the broader lookup error. A command-line tool that caught the broad type first mapped unknown-name errors to the exit code for 'no eligible candidate'. A test asserting that the broad type is raised also passed when the real defect was a missing key.

## Root cause

Handler order and assertion width. The broad handler absorbed an error with a different meaning, and the broad assertion could not distinguish the two.

## Why it was hard to see

Both paths produce a plausible error exit, and the broad test is green for either cause.

## Fix

Catch the narrower exception first, and assert the exact exception type in tests where the distinction matters.

## Verification

Found by the engineer writing the tests; the exact-type assertion fails on the wrong error.

## Transferable rule

> When one error type subclasses another, order handlers narrow to broad and test the exact type. A broad assertion is green for every cause beneath it.

## Related

[INC-0031](./INC-0031-a-concurrency-test-with-no-forced-interleaving-passes-loudes.md) [INC-0034](./INC-0034-a-malformed-item-aborts-the-per-item-pass-and-the-crash-rein.md)
