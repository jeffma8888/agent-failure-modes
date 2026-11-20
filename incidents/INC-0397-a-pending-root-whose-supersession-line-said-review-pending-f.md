---
id: INC-0397
title: A pending root whose supersession line said review pending failed the identity checker at landing
date: 2026-11-02
classes: [identity-and-keying]
severity: low
status: fixed
topic: identity-and-keying/approval-names-wrong-commit
occurrences: 1
---

# INC-0397 - A pending root whose supersession line said review pending failed the identity checker at landing

**Catalog:** [root](../catalog/README.md) / [identity-and-keying](../catalog/identity-and-keying/README.md) / [An approval or activation names the wrong commit or line of history](../catalog/identity-and-keying/approval-names-wrong-commit.md)

**Cost:** A pending root could not land with a marker that claimed an approval it did not yet have.

## Signature - how you recognise it

The identity checker rejected a landing whose marker line said approval was pending.

## What happened

a pending root whose supersession approval line said review pending failed the identity checker at landing; the pending successor was landed without its marker, and the marker is to be written only after the review

## Root cause

the marker was written before the review, so it asserted a state that did not exist

## Why it was hard to see

Writing the marker early looks like preparing for the review, but the checker reads it as a claim.

## Fix

Land a pending successor without its marker and write the marker only after the review

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Land a pending successor without its marker; write the marker only after the review

## Related

[INC-0161](./INC-0161-landing-a-revision-beside-a-supersession-edge-broke-identity.md) [INC-0377](./INC-0377-a-draft-test-root-was-revised-in-place-after-review-marker-o.md) [INC-0403](./INC-0403-the-identity-checker-allowed-a-successor-root-s-new-path-wit.md)
