---
id: INC-0276
title: Do not hand-match paths a framework matches with a richer syntax
date: 2026-11-01
classes: [spec-and-scope, false-green]
severity: medium
status: fixed
---

# INC-0276 - Do not hand-match paths a framework matches with a richer syntax

**Cost:** Minor: caught before it shipped.

## Signature - how you recognise it

A hand matcher understood fewer path forms than the framework it mirrored.

## What happened

the known-path rule matched custom view paths with a hand matcher that only understands a plain parameter, while the framework uses a richer path syntax (optional, wildcard), a latent false 404 for the first row that adds such a view

## Root cause

the known-path rule matched custom view paths with a hand matcher that only understands a plain parameter, while the framework uses a richer path syntax (optional, wildcard), a latent false 404 for the first row that adds such a view

## Why it was hard to see

Every route that exists today matches, so the gap shows only later.

## Fix

Use the framework matcher, or add unit cases for optional and wildcard forms

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Reuse the framework path matcher instead of a hand matcher, or test every syntax form it supports

## Related

[INC-0272](./INC-0272-not-found-under-a-streaming-root-layout-answers-200-whatever.md)
