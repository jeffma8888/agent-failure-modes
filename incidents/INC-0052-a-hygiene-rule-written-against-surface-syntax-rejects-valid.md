---
id: INC-0052
title: A hygiene rule written against surface syntax rejects valid cases; enforce the property at the boundary where it happens
date: 2026-10-28
classes: [detector-fail-closed, spec-and-scope]
severity: low
status: fixed
---

# INC-0052 - A hygiene rule written against surface syntax rejects valid cases; enforce the property at the boundary where it happens

**Cost:** Near miss in a charter draft, caught before adoption. Adopted as written, the rules would have rejected legitimate tests of a URL normaliser and forbidden an intended reuse of one test file across several configurations.

## Signature - how you recognise it

A rule meant to guarantee a behaviour (no network calls) is phrased as a ban on a syntactic form (no URL literals), and the code under test legitimately handles that form.

## What happened

A charter for a test-writing agent said tests must make no network calls and enforced it by banning external URL literals in tests. A URL normaliser's tests need pasted links as inputs, so the rule would have rejected exactly the valid inputs. A second draft rule, one browser-test project per file, would have blocked the intended reuse of one spec across several viewport projects.

## Root cause

The rule targeted the text that usually precedes the unwanted behaviour instead of the behaviour. A literal is not a call, so the syntactic ban is over-inclusive (it rejects data) and also under-inclusive (a URL built at run time passes). The rules were written without checking them against the features they must test.

## Why it was hard to see

The ban reads as obviously safe and is trivially greppable, which makes it look like a strong guarantee. Its false rejections appear only against the specific features that legitimately contain the pattern.

## Fix

Enforce the real property at its boundary: block outbound transport in the test runner itself, so any network attempt fails regardless of how the address was written. Keep literals as a review flag rather than a hard failure. Restate the second rule as 'exactly once per assigned project'.

## Verification

The author re-read each rule against the features it must permit and found both conflicts before adoption. The transport-level block has the two-sided test any guard needs: a real outbound attempt fails, a literal used as plain data passes.

## Transferable rule

> Enforce a property where it happens (the network boundary), not by banning the syntax that usually precedes it. Before adopting a hygiene rule, run it against the features the project must test and ask what valid input it would reject.

## Related

[INC-0040](./INC-0040-a-guard-that-asserts-a-lifecycle-stage-fails-at-exactly-the.md) [INC-0029](./INC-0029-when-a-check-reports-missing-content-the-extractor-is-the-fi.md) [INC-0018](./INC-0018-fail-open-detector-pipe-alternation-matches-nothing-under-on.md)
