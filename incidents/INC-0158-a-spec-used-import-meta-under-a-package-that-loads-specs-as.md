---
id: INC-0158
title: A spec used import.meta under a package that loads specs as CommonJS
date: 2026-10-30
classes: [tooling-paths]
severity: medium
status: fixed
---

# INC-0158 - A spec used import.meta under a package that loads specs as CommonJS

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A module-form feature worked in the author mind and would fail when the spec first loaded.

## What happened

A pending spec computed its path with import.meta while the root package loads specs as CommonJS, so it would fail to load once activated.

## Root cause

The module form of the host package was not checked when the spec was written.

## Why it was hard to see

It stays dormant while the spec is pending and fails only at activation.

## Fix

Compute the module-relative path in a CommonJS-safe way with no assertion change.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Check the module form of the host package before using import.meta in a spec.

## Related

[INC-0156](./INC-0156-a-test-fixture-name-collided-with-a-framework-built-in-and-o.md)
