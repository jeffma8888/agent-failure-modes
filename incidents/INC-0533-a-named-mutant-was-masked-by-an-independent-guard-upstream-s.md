---
id: INC-0533
title: A named mutant was masked by an independent guard upstream, so the case could never turn red for the stated reason
date: 2026-11-02
classes: [false-green]
severity: medium
status: mitigated
---

# INC-0533 - A named mutant was masked by an independent guard upstream, so the case could never turn red for the stated reason

**Cost:** A case was credited with a witness mutation that could not turn it red; caught in static review.

## Signature - how you recognise it

A mutation weakens one access setting, and a separate guard on the same path still refuses.

## What happened

A root coverage proposed making a collection publicly readable as the witness mutation for a case that visits an admin route. Installed source shows the admin route is first guarded by an access check that sends an unauthenticated visitor to the login route, independently of the collection read setting. The mutation leaves that guard intact and the case stays green. The reviewer required a witness that reaches the route guard without weakening the case, and noted that a wait timeout on the redirect is not by itself the requested assertion red.

## Root cause

The witness was chosen from the setting that sounds related, without tracing the other guards on the path.

## Why it was hard to see

Defence in depth means several guards refuse the same request, and each one hides the others from a single mutation.

## Fix

Trace the guards between the mutated line and the assertion in installed source, and name a mutation that reaches the assertion.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Before naming a mutation as a case witness, trace every independent guard on the path from the mutated line to the assertion; a second guard masks the mutant.

## Related

[INC-0524](./INC-0524-a-root-named-a-mutation-its-assertions-could-not-see-because.md) [INC-0476](./INC-0476-unit-mutation-testing-on-a-merged-change-found-two-survivors.md)
