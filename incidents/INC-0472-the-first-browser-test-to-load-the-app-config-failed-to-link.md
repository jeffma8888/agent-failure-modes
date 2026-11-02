---
id: INC-0472
title: The first browser test to load the app config failed to link because one module was reached by two loaders, and minimal variants proved it before any product edit
date: 2026-11-02
classes: [test-isolation]
severity: low
status: fixed
---

# INC-0472 - The first browser test to load the app config failed to link because one module was reached by two loaders, and minimal variants proved it before any product edit

**Cost:** One failed test step, no product harm.

## Signature - how you recognise it

A module that exports a name was reported as lacking it.

## What happened

the first browser test that loaded the app config inside the test worker failed with a missing named export error, though the module did export it; the module was reached twice, once by a static import chain that the test runner compiled as CommonJS (testing module to seed to hook) and once by the ES module graph of a dynamic config import; two minimal scratch variants with no database and no connection attempts proved it before any product edit: static seed import then dynamic config failed to link, and dynamic config alone linked and reached a later environment check; the fix moved the one value import inside the function that needs it, and a third run of the first variant after the fix linked

## Root cause

one module was loaded by two loaders in one worker, a static chain compiled one way and a dynamic graph loaded another way

## Why it was hard to see

The error blamed the export, which was present, and the failure showed only in the first test that loaded the config.

## Fix

reproduce a loader failure with minimal variants before editing product code, then move the single value import inside the function that needs it, so the module loads only through the ES module graph

## Verification

Checked by the engineer with scratch variants and recorded hashes. Not checked: the full browser step, which stays held for a later run.

## Transferable rule

> Reproduce a loader failure with minimal variants before editing product code, and keep modules shared with the app config graph out of static import chains that a test runner compiles differently

## Related

[INC-0158](./INC-0158-a-spec-used-import-meta-under-a-package-that-loads-specs-as.md) [INC-0286](./INC-0286-fix-module-resolution-once-at-the-root-not-per-test.md) [INC-0422](./INC-0422-a-scoped-compiler-config-flagged-an-import-style-that-the-ca.md)
