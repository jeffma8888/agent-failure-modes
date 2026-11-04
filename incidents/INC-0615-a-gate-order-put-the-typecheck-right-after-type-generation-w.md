---
id: INC-0615
title: A gate order put the typecheck right after type generation without walking the type dependency, and the engineer stopped again
date: 2026-11-04
classes: [spec-and-scope]
severity: low
status: mitigated
---

# INC-0615 - A gate order put the typecheck right after type generation without walking the type dependency, and the engineer stopped again

**Cost:** A third stop for the engineer, and a ruling that replaced the gate order and admitted one known typecheck error until a later step.

## Signature - how you recognise it

A gate required green immediately after a step that creates the error it checks.

## What happened

The ordering placed a green typecheck right after type generation. The generated type made a field required, and the only create call lacking it was the seed episode create, which a later step changes. The typecheck failed with exactly one error at that call. The engineer stopped. The ruling admitted that single error before the later step, treated every other error as a stop, and required exit 0 with an empty log after the later step.

## Root cause

The order was set without tracing the generated type to the callers it can break.

## Why it was hard to see

Regenerating types looks like a safe step, and the one failing caller sat in a later step's file.

## Fix

Trace each generated artifact to every caller it can break, and place the gate after the step that fixes the last caller; if a red is admitted earlier, name its exact error and require green later.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Before ordering gates, trace each generated artifact to every caller it can break, and place the typecheck after the step that fixes the last caller.

## Related

[INC-0614](./INC-0614-a-signed-command-allow-list-written-from-the-runtime-list-om.md) [INC-0609](./INC-0609-a-brief-said-to-move-a-post-case-full-seed-to-afterall-but-t.md)
