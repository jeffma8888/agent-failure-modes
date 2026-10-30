---
id: INC-0085
title: A helper owned by one test root was imported by later roots, creating an undeclared dependency
date: 2026-10-30
classes: [spec-and-scope, identity-and-keying]
severity: medium
status: fixed
---

# INC-0085 - A helper owned by one test root was imported by later roots, creating an undeclared dependency

**Cost:** Minor: caught in review or by a stop rule before it shipped.

## Signature - how you recognise it

A shared helper lives under one row or root and other rows import it without declaring the dependency.

## What happened

An audit found that a helper in one root was imported by later roots, so those rows depended on a row they did not list.

## Root cause

Ownership of shared helpers was not recorded, so a route-level check passed while the import graph had a hidden edge.

## Why it was hard to see

Each row looks self-contained until the import graph is read.

## Fix

Check who owns each shared helper before checking routes, and declare or move the helper.

## Verification

Checked by the reviewer or engineer who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Record the owner of every shared helper, and treat an import from another root as a declared dependency.
