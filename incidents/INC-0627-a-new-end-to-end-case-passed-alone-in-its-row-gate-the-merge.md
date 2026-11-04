---
id: INC-0627
title: A new end-to-end case passed alone in its row gate, the merge went ahead with no full end-to-end tier on the branch tip, and the first full run after the merge failed it
date: 2026-11-04
classes: [test-isolation]
severity: high
status: mitigated
---

# INC-0627 - A new end-to-end case passed alone in its row gate, the merge went ahead with no full end-to-end tier on the branch tip, and the first full run after the merge failed it

**Cost:** The main branch went red at the full run, and nothing downstream of it could proceed until a diagnosis.

## Signature - how you recognise it

A case green in its own row fails in the full tier with a module-format load error.

## What happened

A new end-to-end case passed alone in its row. The gate list ran it only there, and no full end-to-end tier ran on the branch tip before the merge. The first full run after the merge failed it in 15 ms in a setup hook with a module-format error (exports is not defined in ES module scope). The case reaches a shared module through a dynamic import, while other specs in the full tier import the same module statically, so the working hypothesis is one module loaded in two formats in the same worker. The code did not change at merge, so the case was green alone and red together.

## Root cause

The gate list ran the new case only in its own row, which cannot show interaction with the other specs in a worker.

## Why it was hard to see

A module loaded in two formats fails only when another spec loads it first in the same worker, which a single-case run never does.

## Fix

Run the full end-to-end step on the branch tip before the merge, and audit other specs and helpers that import the same module in either form.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A branch that adds or changes end-to-end files runs the full end-to-end step before merge; a row gate alone does not show load-order errors.

## Related

[INC-0600](./INC-0600-two-branches-each-green-alone-with-a-clean-merge-tree-went-r.md) [INC-0208](./INC-0208-two-rows-were-green-alone-and-red-together.md)
