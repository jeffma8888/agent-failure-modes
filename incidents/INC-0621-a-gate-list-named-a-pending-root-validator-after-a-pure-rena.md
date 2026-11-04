---
id: INC-0621
title: A gate list named a pending-root validator after a pure-rename activation that removes the very payload the validator requires, and the engineer stopped
date: 2026-11-04
classes: [spec-and-scope]
severity: low
status: mitigated
---

# INC-0621 - A gate list named a pending-root validator after a pure-rename activation that removes the very payload the validator requires, and the engineer stopped

**Cost:** One engineer stop; the check was satisfied by a run on main before the activation instead.

## Signature - how you recognise it

A named gate cannot pass on the tree the preceding step produces.

## What happened

The activation ruling listed a pending-root validator as a gate after a step that activates the root by a pure rename, which removes the physical payload under the pending path. The validator requires every manifest entry to exist there with a matching digest, so it could not pass afterwards. The engineer read the tool source and stopped. Earlier activations had never run it. The lead satisfied the check by running it on main where the root was still pending (exit 0, one payload file passed), and the activated bytes have the same digest. This is the fourth recurrence of ruling on a tool's behaviour without reading its source.

## Root cause

The check was named from its purpose, not from what it requires of the tree.

## Why it was hard to see

The name suggests a check on any root, and earlier activations had skipped it, so no prior run exposed the mismatch.

## Fix

Run the check where its precondition holds (before the activation) and cite that run, and drop it from the post-step gate list.

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> Before naming a check in a gate list, read what the check requires and confirm it can pass on the post-step tree.

## Related

[INC-0612](./INC-0612-a-ruling-set-a-lock-wait-the-installed-lock-could-not-honour.md) [INC-0616](./INC-0616-a-signed-packet-required-a-tail-only-migration-rollback-but.md) [INC-0618](./INC-0618-three-successive-oracle-changes-were-ruled-for-one-test-with.md)
