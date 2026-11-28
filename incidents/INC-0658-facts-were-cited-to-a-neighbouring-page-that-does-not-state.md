---
id: INC-0658
title: Facts were cited to a neighbouring page that does not state them: a general product page, the newest release, a paginated index
date: 2026-11-25
classes: [false-green, spec-and-scope]
severity: low
status: mitigated
topic: false-green/proxy-artifact-cited-as-evidence
occurrences: 3
---

# INC-0658 - Facts were cited to a neighbouring page that does not state them: a general product page, the newest release, a paginated index

**Catalog:** [root](../catalog/README.md) / [false-green](../catalog/false-green/README.md) / [An artifact that looks like evidence was cited but proves no fact](../catalog/false-green/proxy-artifact-cited-as-evidence.md)

**Cost:** Three citations pointed at pages that did not contain their claims; one wrong release attribution reached a revision brief and the lead's long-term memory before the author corrected it. A few fetches each to correct.

## Signature - how you recognise it

A cited page loads and is about the right subject, but searching it for the claim finds nothing; the statement lives on a sibling page such as an older release note or a per-item page.

## What happened

Three rows from one research effort. An availability claim was cited to a provider's general product page instead of the page that states it. A reviewer attributed a changelog fact (a settings screen moved into the app) to the newest release; that release's page had no such note, and a search of the full feed showed it shipped several releases earlier. A first draft cited a paginated index page for facts that each live on a per-item page, so the support would move as the index paged on.

## Root cause

The citation was chosen by topic (the page about this product, the latest release, the list that includes the item) instead of by content (the page whose text states the fact). Nobody searched the cited page for the claim before citing it.

## Why it was hard to see

The cited page loads, is on the right site and is about the right thing, so a link check or a glance passes. The newest release is the natural default for a recent change, and an index page does contain the item's title.

## Fix

Each fact is cited to the page whose text states it: the release note that contains the entry, the per-item URL, the specific product page. Before citing, the author confirms the claim's wording appears on the cited page.

## Verification

Checked: the author fetched the newest release page, found no matching note, searched the full feed and re-cited the release that contains it; the other two citations were re-pointed. Not checked: whether the wrong attribution was removed from every place it had been copied to.

## Transferable rule

> Cite each fact to the page whose text states it (the release note that contains it, the per-item page, the specific doc), and search that page for the claim before citing; a page merely about the subject, the newest release or an index page is not support.

## Recurrences

Occurrences: 3. Repeats of this failure are recorded here instead of as new incidents.

- 2026-11-25 - A research author stated that a workflow engine deploys as a single node and cited its deployment guide; the guide covers installation mechanisms only and states no topology. Caught by the author's own page check during revision.
- 2026-11-26 - An author cited audience confidence ratings to a section that discusses those audiences but assigns no ratings; one rating came from another document. The reviewer nearly accepted them because the section covered the topic, then read the cited lines.

## Related

[INC-0062](./INC-0062-a-reviewer-s-claim-about-framework-behaviour-was-wrong-and-a.md) [INC-0194](./INC-0194-a-citation-check-by-search-alone-could-miss-a-changed-fact.md)
