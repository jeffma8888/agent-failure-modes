---
id: INC-0595
title: An approval header named the review commit, whose tree did not yet hold the reviewed root, and the identity checker refused it
date: 2026-11-04
classes: [identity-and-keying]
severity: medium
status: mitigated
---

# INC-0595 - An approval header named the review commit, whose tree did not yet hold the reviewed root, and the identity checker refused it

**Cost:** One refused approval attempt (approval tree manifest mismatch) before the header was corrected.

## Signature - how you recognise it

An approval names a commit that predates the merge of the root it approves.

## What happened

The approval file for a pending root named the review commit. The identity checker requires the named commit's tree to hold the reviewed manifest, and the review commit predated the root merge, so the first attempt was refused. The header was rewritten to name the first main commit that holds both the review and the root.

## Root cause

The review commit was the natural name for the approval, but the review landed before the root did.

## Why it was hard to see

Both the review and the root were real and reviewed; only the commit order made the tree lack the manifest.

## Fix

Name, in the approval header, the first main commit that holds both the review and the root.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> An approval header must name a commit whose tree holds the reviewed manifest: the first main commit holding both the review and the root.

## Related

[INC-0403](./INC-0403-the-identity-checker-allowed-a-successor-root-s-new-path-wit.md) [INC-0594](./INC-0594-a-successor-draft-named-as-its-old-bytes-a-revision-that-was.md)
