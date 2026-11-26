---
id: INC-0655
title: A delegation brief contained examples forbidden by its own rule
date: 2026-11-23
classes: [spec-and-scope, delegation]
severity: low
status: mitigated
topic: spec-and-scope/requirements-and-limits-collide
occurrences: 1
---

# INC-0655 - A delegation brief contained examples forbidden by its own rule

**Catalog:** [root](../catalog/README.md) / [spec-and-scope](../catalog/spec-and-scope/README.md) / [Requirements, units, or hard limits cannot hold together](../catalog/spec-and-scope/requirements-and-limits-collide.md)

**Cost:** One contradictory brief section required correction after the author flagged it; further propagation or rework was not reported.

## Signature - how you recognise it

A teammate brief bans personal names while its own background section includes personal names.

## What happened

The lead drafted a teammate brief with a rule forbidding personal names, then included names of third-party founders in its own context section. The assigned author noticed the conflict and flagged it in the handoff.

## Root cause

The brief's constraint was treated as a requirement for the teammate's output rather than a requirement on the instruction artifact itself; the lead did not run the brief's checks against the complete brief before dispatch.

## Why it was hard to see

Rules and context often occupy separate sections, and a writer can treat background as exempt. The teammate then receives both a prohibition and a violating example in the same authority-bearing document.

## Fix

Run all constraints in the brief over its full text before issuing it, remove prohibited examples, and check that context and output rules agree.

## Verification

The assigned author identified the named examples and reported the contradiction. Not checked in the input: whether the lead corrected the issued brief or whether later briefs consistently pass their own checks.

## Transferable rule

> Before issuing a delegation brief, apply every prohibition and formatting check in it to the entire brief itself, including context and examples; remove contradictions before a teammate receives them.

## Related

[INC-0076](./INC-0076-a-teammate-s-write-boundary-contradicted-the-charter-s-file.md) [INC-0489](./INC-0489-a-rule-written-in-teammate-briefs-was-broken-by-the-lead-in.md)
