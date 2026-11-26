---
id: INC-0640
title: A fact was recorded as unverified because the web-search tool errored, while the page-fetch tool and other retrieval routes still worked
date: 2026-11-12
classes: [tooling-paths, spec-and-scope]
severity: medium
status: mitigated
topic: tooling-paths/tool-defaults-not-target
occurrences: 2
---

# INC-0640 - A fact was recorded as unverified because the web-search tool errored, while the page-fetch tool and other retrieval routes still worked

**Catalog:** [root](../catalog/README.md) / [tooling-paths](../catalog/tooling-paths/README.md) / [The tool's own resolution or defaults, not the target, caused it](../catalog/tooling-paths/tool-defaults-not-target.md)

**Cost:** A scored triage note carried a false evidence gap that two fetches could close, and the user had to push back; in the second occurrence the settled fact moved a score.

## Signature - how you recognise it

A research note writes unverified or unchecked beside a fact right after one retrieval tool errored, and no other route is listed as tried.

## What happened

An agent writing a scored triage note needed a company's latest funding round and valuation. Its web-search tool returned an error, and it recorded the fact as unverified, although its plain page-fetch tool still worked. After the user pushed back, the agent fetched a news search feed (RSS) with the page-fetch tool and then the article it pointed to, and verified the fact in two calls. A later triage repeated the pattern although the fallback chain was by then written into the agent's research procedure.

## Root cause

The failure of one endpoint was recorded as a property of the evidence: the gap word described the state of a tool, not what retrieval could establish.

## Why it was hard to see

Unverified reads as cautious and honest, so writing it after a tool error feels like the safe choice, and nothing in the note shows how few routes were tried. Once the fallbacks are documented, skipping them is a skipped procedure that still looks like a coverage gap.

## Fix

Before writing any gap word, run the alternate retrieval routes: news search feeds through the page fetcher, a direct fetch of the likely source article, reference and filing searches, public APIs. Write unverified only when every route failed, and list the routes tried beside it.

## Verification

Checked: the first fact was verified in two calls after the pushback, and the second was settled by the documented fallback chain in about ten calls. Not checked: whether older notes carry gap words written after a single tool failure.

## Transferable rule

> Write unverified only after every retrieval route has failed, not one endpoint: when a search tool errors, run the documented fallbacks (news feeds through the page fetcher, a direct fetch of the likely source, reference and filing searches) and list the routes tried beside the gap word.

## Recurrences

Occurrences: 2. Repeats of this failure are recorded here instead of as new incidents.

- 2026-11-16 - A triage written ten days earlier marked a company's funding stage unchecked after the search tool errored; the fallback chain already in the research procedure (news feeds, metasearch, forum and filing searches, a job-board API, direct fetches) settled it in about ten calls and moved a score.

## Related

[INC-0072](./INC-0072-four-different-fetch-failures-were-all-reported-as-the-site.md) [INC-0593](./INC-0593-a-packet-author-who-could-not-read-the-rulings-file-marked-e.md)
