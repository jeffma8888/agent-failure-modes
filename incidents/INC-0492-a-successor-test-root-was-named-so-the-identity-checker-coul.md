---
id: INC-0492
title: A successor test root was named so the identity checker could never accept it as a successor
date: 2026-11-02
classes: [identity-and-keying]
severity: low
status: mitigated
---

# INC-0492 - A successor test root was named so the identity checker could never accept it as a successor

**Cost:** None incurred: found by reading the checker before activation, at the price of a rename and a recheck.

## Signature - how you recognise it

The successor carried a name from a different family than the root it replaced.

## What happened

A successor test root was named after its backlog row. The identity checker accepts a supersession only inside one family and only with a higher revision, so a root with the row name could never replace the root it was written to replace. A reviewer found this by reading the checker source before activation. The checker was left unchanged, because a gate is never loosened to fit an artifact. The root and its coverage note were renamed into the old family with a higher revision, payload bytes unchanged, the manifest and the planned supersession lines updated, and the backlog row kept as owner.

## Root cause

The name was taken from the backlog row, and the checker rule that ties a successor to a family and a higher revision had not been read before the mapping was written.

## Why it was hard to see

The root looked correct on its own, and the refusal would have come only at activation.

## Fix

Rename the successor into the family it supersedes with a higher revision, keep the row as owner, update the manifest and supersession lines, and run the identity check on the result.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Name a successor after the family it supersedes, and read the checker's acceptance rule before writing the mapping; never loosen the gate to fit the artifact.

## Related

[INC-0403](./INC-0403-the-identity-checker-allowed-a-successor-root-s-new-path-wit.md) [INC-0397](./INC-0397-a-pending-root-whose-supersession-line-said-review-pending-f.md)
