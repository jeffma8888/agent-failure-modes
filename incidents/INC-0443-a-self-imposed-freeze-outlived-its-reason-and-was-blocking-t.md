---
id: INC-0443
title: A self-imposed freeze outlived its reason and was blocking three rows' activations
date: 2026-11-02
classes: [checkpoint]
severity: low
status: fixed
---

# INC-0443 - A self-imposed freeze outlived its reason and was blocking three rows' activations

**Cost:** Three rows' activations waited on a freeze that protected nothing.

## Signature - how you recognise it

A STOP kept blocking work after the run it protected could no longer be affected.

## What happened

a self-imposed freeze (a main-side STOP on registry and marker changes) was kept after its reason was gone: the guarded run read only its own detached clone with its own registry and markers, so a change on main could not affect it, yet the freeze was blocking the activations of three rows; the lead re-derived the mechanism, withdrew the STOP and lifted the marker deferral

## Root cause

the freeze was honored as a rule after the reason for it had changed

## Why it was hard to see

A rule written down once is rarely re-checked against its mechanism.

## Fix

re-derive the mechanism of a freeze before honoring it again, and withdraw it when the guarded run cannot read what the freeze protects

## Verification

Checked by the lead. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Re-derive a freeze's mechanism before honoring it; withdraw it when the guarded run cannot read what it protects

## Related

[INC-0421](./INC-0421-a-closure-packet-freeze-test-turned-positive-on-a-control-on.md) [INC-0428](./INC-0428-a-supersession-marker-was-deferred-to-each-row-s-activation.md)
