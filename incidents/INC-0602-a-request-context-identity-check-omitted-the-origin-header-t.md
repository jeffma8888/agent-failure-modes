---
id: INC-0602
title: A request-context identity check omitted the Origin header the repo helper sends and read user null, an author defect that looked like a product failure
date: 2026-11-04
classes: [test-isolation]
severity: low
status: mitigated
---

# INC-0602 - A request-context identity check omitted the Origin header the repo helper sends and read user null, an author defect that looked like a product failure

**Cost:** One failed baseline kept as evidence and one rerun.

## Signature - how you recognise it

A login returns success but the following identity request reports no user.

## What happened

A new root passed setup, migrate, seed, build and the server start, and the login POST returned 200 with a redirect. It then failed at the first identity assertion with user null instead of the expected account. The cause, checked by the lead, was that the identity GET sent no Origin header, while the repo's REST helper sends one. This was an author defect in the root, not a product or oracle result. The accepted fix changes only the identity GET to send the owned origin, keeps the exact positive user assertion, preserves the failed baseline and reruns once.

## Root cause

The author wrote the request by hand and did not reuse the helper that every other test uses.

## Why it was hard to see

A null user reads as a failed login or a product bug, and the earlier steps were all green.

## Fix

Send the owned origin on the identity request like the repo helper, keep the exact positive assertion, preserve the failed baseline and rerun.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> When a hand-written request context reads user null after a good login, compare its headers with the repo helper before blaming the product.

## Related

[INC-0599](./INC-0599-a-checklist-expected-a-slug-first-link-and-excused-absent-he.md) [INC-0595](./INC-0595-an-approval-header-named-the-review-commit-whose-tree-did-no.md)
