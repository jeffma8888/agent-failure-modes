---
id: INC-0027
title: A cache keyed on a recycled id judged each record on its predecessor's evidence
date: 2026-08-28
classes: [identity-and-keying, observability, false-green]
severity: critical
status: fixed
---

# INC-0027 - A cache keyed on a recycled id judged each record on its predecessor's evidence

**Cost:** A newly-built gate refused 849 of 859 real candidates. Hand-labelled validation on 24 records had measured ZERO false positives, so the gate was about to be trusted on real data.

## Signature - how you recognise it

A mass verdict whose stated reason is IDENTICAL across hundreds of distinct inputs. Runtime is also far higher than it should be, because the cache is not actually caching anything.

## What happened

A duplicate-detection gate compares a candidate against already-held records by running each one's detector against the other's fixtures. Those fixtures were cached by record id. Ids are handed out as 'next free', so a REFUSED candidate never claims its number and the next candidate is handed the same one - and the id-keyed cache then served the refused predecessor's fixtures to its successor. Every one of the 849 refusals named the same twin.

## Root cause

The cache key was an identifier that is unique only among ACCEPTED records, used to key evidence for candidates that had not been accepted yet. A cache key is normally a performance concern; here it silently decided WHICH EVIDENCE each record was judged on, which makes it a correctness surface.

## Why it was hard to see

The hand-labelled sample could only reveal false positives it happened to contain, and the collision requires a REFUSAL to have already occurred - which a curated all-valid sample never produces. Both tells were present and easy to read past: one identical reason across hundreds of distinct inputs, and a runtime that fell from 1m40s to 4.6s once the cache actually cached.

## Fix

Key derived evidence by CONTENT, or by an identity that is unique across everything the system will ever be asked about - never by a slot number a rejection can recycle. Then re-run the gate on the FULL population before trusting it, and before believing any mass verdict, count how many DISTINCT reasons it produced.

## Verification

After re-keying, the same population produced 6 refusals instead of 849 - each a genuine behavioural twin of a record accepted in the same pass - 24 promotions, a register of 40 records, and a green suite. Runtime fell from 1m40s to 4.6s, which is the second, independent tell that the cache had been mis-keyed rather than the data being duplicative.

## Transferable rule

> Never key derived evidence on an identifier a rejection can recycle: 'next free' ids are unique only among ACCEPTED records. Before believing a mass verdict, count its DISTINCT reasons - one identical reason across hundreds of inputs indicts the judge, not the data. Always re-run a gate on the full population; a hand-labelled sample finds only the false positives it contains.

## Provenance

Where this was observed, so the claim is checkable rather than anecdotal:

- https://github.com/jeffma8888/agent-gap-radar - commit 315bc6e adds the interchangeable-detector refusal this gate implements; tools/promote.py holds the fixture comparison and the ranking helper.

## Related

[INC-0019](./INC-0019-fail-open-detector-parsing-the-wrong-column-reports-healthy.md) [INC-0026](./INC-0026-a-whole-batch-verification-veto-turns-one-bad-item-into-a-pe.md)
