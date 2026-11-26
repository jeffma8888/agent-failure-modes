---
id: INC-0649
title: Repository metadata checks missed live naming collisions hidden in repository documentation
date: 2026-11-23
classes: [false-green]
severity: medium
status: mitigated
topic: false-green/test-cannot-see-the-defect
occurrences: 1
---

# INC-0649 - Repository metadata checks missed live naming collisions hidden in repository documentation

**Catalog:** [root](../catalog/README.md) / [false-green](../catalog/false-green/README.md) / [A test stays green with the behavior removed or broken](../catalog/false-green/test-cannot-see-the-defect.md)

**Cost:** Two naming candidates had to be rejected after passing initial clearance checks; the time spent on rework was not recorded.

## Signature - how you recognise it

A candidate name passes registry, handle and repository-description checks, but a same-category product using that name is described in a search-hit README.

## What happened

Two proposed names passed metadata-based checks. A second-model reviewer read the repositories behind the search hits and found existing same-category products: one documented chiefly in a non-English README, and another distributed through a release repository whose description was blank.

## Root cause

The negative claim that no collision exists was based on searchable descriptions and summaries that did not cover the content and language of every relevant repository hit.

## Why it was hard to see

A missing description looks like missing evidence, not counterevidence; a non-English README or a release-only repository can look unrelated in a brief search result. Several independent-looking metadata checks still shared the same blind spot.

## Fix

Inspect the README of repository-name hits with empty descriptions, non-English documentation or release/landing-only layouts before clearing the name; record the source evidence for the category comparison.

## Verification

The second-model reviewer found two concrete collisions by opening the README content. Not checked in the input: that the amended clearance method catches every future category collision.

## Transferable rule

> Before declaring a proposed name free of same-category collisions, read the README of every repository-name hit with an empty description, non-English content or a release/landing-only layout; document what establishes its category.

## Related

[INC-0505](./INC-0505-a-run-command-silently-dropped-a-named-option-and-three-test.md) [INC-0042](./INC-0042-self-review-does-not-catch-recurrences-of-your-own-documente.md)
