---
id: INC-0361
title: A test's teardown emptied a shared server database, and a gate that never completed hid the red
date: 2026-11-01
classes: [test-isolation, observability]
severity: medium
status: fixed
---

# INC-0361 - A test's teardown emptied a shared server database, and a gate that never completed hid the red

**Cost:** Minor: a merge was blocked until a full run passed; nothing shipped.

## Signature - how you recognise it

A late end-to-end step could not log in because an earlier test's teardown had deleted the seeded accounts from the shared server database.

## What happened

a full acceptance run passed every step through the server integration step and then failed two end-to-end tests with a login refusal. An earlier integration test shared the same server database and its teardown reset the content, deleting every collection except the framework's own, including the staff accounts. The end-to-end step then found no seeded account. Both tests were already on the main line; the records show no completed full run since they landed (that is the recorded history checked, not every historical run), so the red was latent there and was not caused by the change under review

## Root cause

a test mutated shared state and restored an empty state instead of the baseline its successors expect, and the slow gate that would have run the two tests together had not completed since they were added

## Why it was hard to see

Each test passed alone, the fast gates never run the two together, and the full gate's absence of completed runs looked like unrelated slowness rather than hidden accumulated reds.

## Fix

A revision of the integration test whose teardown leaves the shared database in the state the run created (accounts seeded), written red first; a census of other tests in the shared-server steps that change shared state; and the merge stays blocked until a new full run passes on the merge result

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A test that mutates shared state must restore the baseline its successors expect (reset then reseed, never reset only), and the harness should re-establish and check that baseline when each shared step starts; a slow gate with no recorded completion since two tests landed has not tested them together, so treat the main line as unproven until it runs

## Related

[INC-0097](./INC-0097-url-guards-did-not-prove-a-test-owned-the-disposable-cluster.md) [INC-0088](./INC-0088-qa-helpers-assumed-rest-field-shapes-that-differ-from-the-de.md) [INC-0297](./INC-0297-a-test-needed-a-second-account-that-the-minimal-seed-did-not.md)
