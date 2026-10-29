---
id: INC-0055
title: A scope cut was mapped against the previous version of its baseline document
date: 2026-10-28
classes: [spec-and-scope, identity-and-keying]
severity: medium
status: fixed
---

# INC-0055 - A scope cut was mapped against the previous version of its baseline document

**Cost:** A draft classified every row of a plan's previous version while a newer version with 18 additional rows was already committed, so every surviving-row count and effort total was wrong. All three independent reviewers found it; a revision was needed.

## Signature - how you recognise it

A derived document cites a baseline by version label only, and the baseline has changed since the author last read it.

## What happened

An author classified the rows of version 1.4 of a plan while version 1.5, with 18 new rows, was already committed. The derived scope cut therefore omitted the new rows and its counts and sums were off.

## Root cause

The author worked from a remembered copy of the baseline and named it by label, not by commit. A label does not say whether it is still current.

## Why it was hard to see

The previous version is internally consistent, so the draft looks coherent. Only a reader who opens the current version sees the gap.

## Fix

Rebase on the plan commit named in the header and classify the missing rows. Every derived document now states the exact baseline commit it was computed from.

## Verification

Three reviewers independently flagged the discrepancy; the revision's counts were recomputed from the named commit.

## Transferable rule

> Before mapping against a baseline document, read its current version and commit from disk and write that commit into the header of the derived document.

## Related

[INC-0042](./INC-0042-self-review-does-not-catch-recurrences-of-your-own-documente.md) [INC-0021](./INC-0021-stale-module-import-shipped-is-not-live.md)
