---
id: INC-0645
title: The agent taught its own testability choice, a query function passed in as a parameter, as a property of the problem the source posed
date: 2026-11-21
classes: [spec-and-scope]
severity: medium
status: fixed
topic: spec-and-scope/claims-outrun-available-evidence
occurrences: 1
---

# INC-0645 - The agent taught its own testability choice, a query function passed in as a parameter, as a property of the problem the source posed

**Catalog:** [root](../catalog/README.md) / [spec-and-scope](../catalog/spec-and-scope/README.md) / [Claims or instructions say more than the evidence supports](../catalog/spec-and-scope/claims-outrun-available-evidence.md)

**Cost:** A primer gave the user a wrong picture of the problem's interface until the user asked for evidence; correcting it took one round of reading the primary reports.

## Signature - how you recognise it

An explanation of a problem describes an interface detail that appears only in the agent's own solution or a secondary practice page, and in none of the primary reports.

## What happened

An agent's solution to a practice problem took the provided query function as a parameter so its tests could pass in a fake. When the user asked for a primer, the agent framed the question as a functional-programming pattern in which the problem hands the candidate a function. The user asked for evidence. The firsthand reports showed a global function already defined in the editor and called by name; the only parameter-style signature came from a machine-generated practice page.

## Root cause

A choice the agent made for testability was remembered as part of the specification, and the teaching was drawn from the agent's own artifact instead of from the primary reports.

## Why it was hard to see

The artifact was the most recent and most detailed thing in context, and one secondary page appeared to agree with it, so the agent's own choice looked confirmed.

## Fix

The answer now says the parameter was the agent's testability choice and recommends calling the provided function by name, as the reports describe.

## Verification

Checked: the primary reports were read and compared with the primer. Not checked: other teaching notes drawn from the same solution.

## Transferable rule

> When teaching from an artifact you wrote, label each choice you made separately from what the source specifies, and check the primary reports before calling anything part of the problem.
