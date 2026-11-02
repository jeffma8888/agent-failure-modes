---
id: INC-0498
title: The first browser run of new end-to-end cases found two product defects that config reads and other tiers missed
date: 2026-11-02
classes: [false-green]
severity: medium
status: mitigated
---

# INC-0498 - The first browser run of new end-to-end cases found two product defects that config reads and other tiers missed

**Cost:** Two product defects sat behind green tiers until the first browser run, and two fix rows were added.

## Signature - how you recognise it

A config listed a column and a field, and the real page showed neither as intended.

## What happened

The first run of a set of browser cases on the real admin passed three cases and failed three. A list page silently dropped its name column, because the list view skips a group field that has no custom cell renderer, although the config listed it as a default column. An editor page requested a public content delivery host at runtime, because a read-only JSON field renders a code editor whose loader fetches from that host, although the admin must work offline. Both were product defects, not wrong oracles, so the assertions and the transport guard stayed as written.

## Root cause

Reading the config was taken as evidence of what the page shows and what it fetches, and no tier rendered the real page.

## Why it was hard to see

The config was correct on its face, the other tiers were green, and an unrendered column or a quiet third-party fetch gives no error.

## Fix

Commit the red cases first as the pre-fix evidence, fix the product, and keep the assertions and the transport guard unchanged.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A config that lists a column or a field is not evidence that the page shows it or works offline; only a browser run on the real page is.

## Related

[INC-0494](./INC-0494-the-first-real-click-around-found-product-defects-that-many.md) [INC-0496](./INC-0496-an-acceptance-record-was-ready-for-signature-with-every-test.md)
