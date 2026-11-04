---
id: INC-0560
title: A mutant made the product raise its own domain error inside the awaited expectation, before the matcher ran, and the agent disclosed that it was not an assertion error
date: 2026-11-04
classes: [false-green]
severity: low
status: mitigated
---

# INC-0560 - A mutant made the product raise its own domain error inside the awaited expectation, before the matcher ran, and the agent disclosed that it was not an assertion error

**Cost:** None. The disclosure let the lead rule on the classification.

## Signature - how you recognise it

A red whose error type is not an assertion error, raised by the mutated product path.

## What happened

Of nine mutation receipts, eight failed with explicit assertion errors. One mutant made the product refuse an edit it should permit, by throwing its own domain error while the awaited expression inside the expectation was evaluated, before the matcher ran. The agent disclosed that this did not meet the strict assertion-error qualification instead of counting it silently. The lead ruled that a domain error raised by the mutated path inside the test expectation is a right-reason kill, while a setup error, a timeout, a harness error or an error from outside the mutated path is not.

## Root cause

The mutated behavior was enforced by an exception, which the test framework reports differently from a failed matcher.

## Why it was hard to see

The error type alone does not say whether the test failed on the protected behavior.

## Fix

Disclose the error type, and classify by whether the mutated path raised it inside the expectation.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Classify a non-assertion red by where it was raised: a domain error from the mutated path inside the expectation is a right-reason kill; setup, timeout, harness or outside-path errors are not.

## Related

[INC-0534](./INC-0534-a-configuration-mutation-failed-a-setup-assertion-before-any.md) [INC-0524](./INC-0524-a-root-named-a-mutation-its-assertions-could-not-see-because.md)
