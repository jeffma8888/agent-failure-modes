---
id: INC-0668
title: An options analysis eliminated alternatives on blocking cons that the cited sources did not support
date: 2026-11-26
classes: [spec-and-scope]
severity: medium
status: fixed
topic: spec-and-scope/claims-outrun-available-evidence
occurrences: 1
---

# INC-0668 - An options analysis eliminated alternatives on blocking cons that the cited sources did not support

**Catalog:** [root](../catalog/README.md) / [spec-and-scope](../catalog/spec-and-scope/README.md) / [Claims or instructions say more than the evidence supports](../catalog/spec-and-scope/claims-outrun-available-evidence.md)

**Cost:** Several options wrongly eliminated in the first version of a design document; 58 source checks by a second-model reviewer, then 15 reopened checks and two further revision rounds.

## Signature - how you recognise it

A con tagged blocking carries a citation, and the cited passage says only that the option is harder or needs more parts, or names a different constraint from the one the option breaks.

## What happened

The first version of a design document compared implementation options and eliminated several on cons tagged blocking, each with a citation. A second-model reviewer opened the source behind every blocking con, 58 checks, and found several did not hold: a hosted free tier said to be absent existed, a database role said to be unrestrictable could be scoped, two workflow engines said to lack a self-hosted container path documented one, and a protocol said to forbid a behaviour did not forbid it. One option the upstream research had kept viable was missing from the comparison altogether. In the next version one elimination cited a self-approval invariant although the option kept a separate human gate; its real defect was a different one. A stage earlier the same pattern had appeared in the requirements document, where a requirement cited a section that in fact sequenced the feature last.

## Root cause

The cons were written from the author's impression of each alternative, and the citation was attached as a pointer to the topic without re-opening the passage to confirm it states infeasibility. Harder was rounded up to impossible, and the nearest-sounding invariant stood in for the one at stake.

## Why it was hard to see

Every con carried a citation, so the comparison looked sourced. Each claim was plausible for its technology, and the error is visible only to someone who opens the cited page and looks for the sentence.

## Fix

Give every blocking con the quoted source line or the exact invariant that makes the option infeasible; downgrade to advisory any con whose source says only harder or more parts; diff the option list against the options the upstream document kept viable; have a different-model reviewer open each cited source.

## Verification

A second-model reviewer opened the source of all 58 blocking cons in the first version and re-ran 15 reopened checks on the second, which surfaced the wrong-invariant citation. Not checked in the input: whether advisory cons received the same source check, or a full re-check of the final version.

## Transferable rule

> Tag a con blocking only if you can quote the source line or name the exact invariant that makes the option infeasible; if the source says only harder or needs more parts, tag it advisory; and list every option the upstream document kept viable so none is eliminated by omission.

## Related

[INC-0650](./INC-0650-an-options-comparison-applied-the-same-hard-constraint-at-di.md)
