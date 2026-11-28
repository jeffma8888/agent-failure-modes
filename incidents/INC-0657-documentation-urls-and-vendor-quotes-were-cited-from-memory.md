---
id: INC-0657
title: Documentation URLs and vendor quotes were cited from memory: five links returned 404 and two quotes were no longer on the live pages
date: 2026-11-25
classes: [false-green, delegation]
severity: medium
status: mitigated
topic: false-green/oracle-or-claim-written-from-memory
occurrences: 1
---

# INC-0657 - Documentation URLs and vendor quotes were cited from memory: five links returned 404 and two quotes were no longer on the live pages

**Catalog:** [root](../catalog/README.md) / [false-green](../catalog/false-green/README.md) / [A test oracle, locator or review claim came from memory, not source](../catalog/false-green/oracle-or-claim-written-from-memory.md)

**Cost:** Five dead links and two stale quotes sat in research drafts and one revision brief; all were caught before publication by a citation audit or by an author who fetched before citing. Roughly one revision round of rework, not timed.

## Signature - how you recognise it

A cited URL or a quoted phrase has no fetch behind it in the current revision: the link returns 404, or the words are not on the page as it reads today.

## What happened

Three rows from one research effort. An author cited four documentation URLs from memory, and a citation audit found that all four returned 404. A reviewer reconstructed a documentation URL from memory instead of copying one it had fetched, and the lead passed it to the author in a revision brief without fetching it; it returned 404, and the author found the live page through the documentation site's search. A reviewer quoted two vendor phrases that were no longer on the live pages; the author re-fetched both pages and found different wording.

## Root cause

URLs and quotes were produced from recall of how a documentation site is usually laid out, or of what a page said on an earlier visit, instead of being copied from a fetch made for this revision. Documentation sites reorganise paths and rewrite copy, so recall drifts from the live site without any signal.

## Why it was hard to see

A reconstructed URL has the right host and a plausible path, and a remembered quote sounds like the vendor. Each hand-off from reviewer to lead to author added apparent confirmation without anyone loading the page, and a 404 appears only when someone follows the link.

## Fix

Every URL is fetched before it is cited or handed to a teammate, and the citation is copied from the page that loaded; quotes are copied from a fetch made in the revision that cites them. The citation audit fetches every cited link.

## Verification

Checked: the author's citation audit covered all 73 cited sources, the corrected links load, and the two quotes were replaced with the wording on the re-fetched pages. Not checked: whether quotes in earlier, already-closed documents still match their pages.

## Transferable rule

> Fetch every URL before you cite it or hand it to anyone, and copy it from the page that loaded; quote only text from a fetch made in the revision that cites it. A remembered or reconstructed route is a guess, and so is wording from an earlier visit.

## Related

[INC-0206](./INC-0206-a-guessed-commit-id-was-sent-to-two-teammates.md) [INC-0642](./INC-0642-a-quote-check-passed-on-the-collector-s-own-annotations-beca.md)
