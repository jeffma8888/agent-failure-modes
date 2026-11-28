---
id: INC-0667
title: A requirements document's option set settled a question the governing plan assigns to the design document
date: 2026-11-26
classes: [spec-and-scope]
severity: low
status: fixed
topic: spec-and-scope/wrong-owner-path-or-scope
occurrences: 1
---

# INC-0667 - A requirements document's option set settled a question the governing plan assigns to the design document

**Catalog:** [root](../catalog/README.md) / [spec-and-scope](../catalog/spec-and-scope/README.md) / [Work lands under the wrong owner, path, or write boundary](../catalog/spec-and-scope/wrong-owner-path-or-scope.md)

**Cost:** One review finding and part of a revision round on the requirements document.

## Signature - how you recognise it

A document for one stage lists options and picks one for a question that the project's governing plan names as belonging to a later stage's document.

## What happened

A project's governing plan assigned each open question to a stage: requirements first, design after. The first version of the requirements document included an option set that weighed alternatives for one of the questions assigned to the design stage and chose among them. A second-model reviewer, reading the document against the plan's assignments, reported that the decision was not this document's to make. The rule adopted from the finding is that the requirements document states the need and leaves the choice to the design stage.

## Root cause

The author had the whole project context in view and answered an open question it could see, without checking which stage the governing plan names as the owner of that decision.

## Why it was hard to see

The option set was relevant and argued, so it read as diligence. The ownership of each question is written in a different document from the one being drafted, and a requirements template does not ask who owns a decision.

## Fix

Before writing an option set, look the question up in the governing plan's stage assignments; if a later stage owns it, record the need and the constraints the answer must satisfy and hand the question forward undecided.

## Verification

A second-model reviewer compared the document with the governing plan's assignments and reported the overreach. Not checked in the input: the revised text, or whether the design stage later treated the question as open.

## Transferable rule

> Before a stage document decides a question, check which stage the governing plan assigns it to; a requirements document states the need and the constraints and leaves a design-assigned question open for the design document.
