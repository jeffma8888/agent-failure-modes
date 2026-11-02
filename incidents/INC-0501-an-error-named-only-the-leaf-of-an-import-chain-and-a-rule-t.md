---
id: INC-0501
title: An error named only the leaf of an import chain, and a rule to add a link only when the next run named it spent a run per link
date: 2026-11-02
classes: [stage-timeout]
severity: low
status: mitigated
---

# INC-0501 - An error named only the leaf of an import chain, and a rule to add a link only when the next run named it spent a run per link

**Cost:** One unit run was spent before a source search showed the whole import chain at once.

## Signature - how you recognise it

A load error names one package, but that package is reached through others that fail the same way.

## What happened

The unit tier failed before any test because the runtime refused a stylesheet file shipped by a leaf package, reached through a framework export that a generated map had begun to import. The first ruling allowed only the packages in the failing chain to be added to the runner inline list, and another only if the next run named it. The error named only the leaf, so each further link would have cost one run. A search of installed source showed that the export re-exports a UI package whose client index also imports the stylesheet.

## Root cause

The rule let the error message decide what was on the path, and an error names the point of failure, not the chain that leads to it.

## Why it was hard to see

Adding only what the last error named looks careful and minimal, and each run looks like progress, so the cost of serial discovery is easy to mistake for diligence.

## Fix

Trace the chain in installed source from the leaf to the entry, add every package that source shows on the path in one change, and record the file and line for each. Keep the other evidence requirements unchanged.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> When an error names only the leaf of a dependency chain, trace the chain in source and act on all of it, rather than letting each run name the next link.

## Related

[INC-0477](./INC-0477-a-browser-test-failed-at-its-first-request-and-after-that-wa.md) [INC-0472](./INC-0472-the-first-browser-test-to-load-the-app-config-failed-to-link.md)
