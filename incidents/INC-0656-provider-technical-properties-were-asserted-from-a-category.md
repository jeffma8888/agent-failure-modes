---
id: INC-0656
title: Provider technical properties were asserted from a category label, one consumer's configuration and a marketing page, not from the provider's technical documentation
date: 2026-11-25
classes: [spec-and-scope, false-green]
severity: medium
status: mitigated
topic: spec-and-scope/claims-outrun-available-evidence
occurrences: 1
---

# INC-0656 - Provider technical properties were asserted from a category label, one consumer's configuration and a marketing page, not from the provider's technical documentation

**Catalog:** [root](../catalog/README.md) / [spec-and-scope](../catalog/spec-and-scope/README.md) / [Claims or instructions say more than the evidence supports](../catalog/spec-and-scope/claims-outrun-available-evidence.md)

**Cost:** Four wrong technical claims about third-party providers reached first drafts of research documents; each was corrected by a primary-source pass or a review before publication, at the cost of extra revision work that was not timed.

## Signature - how you recognise it

A comparison groups or describes providers in the words of a marketing category, a landing page or one customer's setup, while the provider's own runtime or deployment documentation lists a different default or several options.

## What happened

Several defects from one research effort share this mechanism. An author grouped two sandbox providers under their shared marketing category (microVM isolation); their runtime documentation showed that one defaults to a container and the other also offers a user-space kernel sandbox, so the grouping was wrong at exactly the level an isolation decision needs. The same author described a provider's storage as ephemeral because one consuming application configured it that way; the provider documents default persistence. A reviewer read a vendor's marketing page ('deploy in your own cloud network') as confirming a deployment claim, while the page the document actually cited showed vendor-hosted deployment. Another document's first draft overstated a vendor's deployment model the same way. The author's own primary-source pass caught the first two; review caught the other two.

## Root cause

The source used for a provider's technical property described something else: the category the provider markets itself under, how one customer configured it, or what a sales page promises. Each is true about something, so none looked fabricated, but none states the provider's contract for the specific offering and runtime class being compared.

## Why it was hard to see

Category labels and landing-page phrases are written to be quoted and are often accurate for the flagship option, so they read as authoritative. A consumer's configuration is real behaviour observed in the wild. Providers that offer several runtime classes or deployment models are exactly the ones a label flattens, and the difference shows only on the technical page.

## Fix

Each provider property was re-sourced from the provider's own runtime, storage or deployment documentation, stated per runtime class or deployment option, and cited to that page. What a provider can do and how one consumer configured it are now cited separately, and a reviewer verifies a technical claim on the page the document cites.

## Verification

Checked: the author and the reviewer re-read the technical pages, and the corrected claims match them as of the correction date. Not checked: whether other providers in the same documents were classified from labels, or whether the rule prevents recurrence.

## Transferable rule

> Take a provider's technical property (isolation boundary, persistence, deployment model) only from its own technical documentation for the specific offering and runtime class, and check it on the page cited; a category label, a marketing page or one consumer's configuration is never the provider's contract.

## Related

[INC-0648](./INC-0648-a-current-project-thesis-relied-on-a-shutdown-report-that-ha.md)
