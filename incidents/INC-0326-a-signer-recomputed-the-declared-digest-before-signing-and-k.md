---
id: INC-0326
title: A signer recomputed the declared digest before signing and kept the signature outside the hashed range
date: 2026-11-01
classes: [spec-and-scope, identity-and-keying]
severity: medium
status: fixed
---

# INC-0326 - A signer recomputed the declared digest before signing and kept the signature outside the hashed range

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A declared digest was about to be signed without the signer having hashed the bytes.

## What happened

an amendment declared a contract digest, and signing it without recomputing the digest from the stated recipe, or appending the signature inside the hashed range, would have bound the signature to unverified or changed bytes

## Root cause

an amendment declared a contract digest, and signing it without recomputing the digest from the stated recipe, or appending the signature inside the hashed range, would have bound the signature to unverified or changed bytes

## Why it was hard to see

The declared digest looks authoritative, and a signature added to the file changes the bytes it was meant to bind.

## Fix

Recompute the digest from the stated recipe before signing, and append the signature after the hashed range so the digest stays valid

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A signature binds to bytes the signer has hashed himself, and appending the signature must not change the hashed range

## Related

[INC-0122](./INC-0122-a-digest-present-anywhere-in-a-manifest-was-taken-as-proof-i.md) [INC-0228](./INC-0228-a-digest-manifest-without-digests-was-cited-as-evidence.md) [INC-0277](./INC-0277-sign-the-stable-re-checked-part-of-a-design-addendum-instead.md) [INC-0335](./INC-0335-a-pinned-base-digest-froze-a-file-that-a-later-row-split-nee.md)
