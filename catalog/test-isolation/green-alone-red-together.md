# Green alone, red in the full suite, with another run, or after a merge

[Catalog](../README.md) / [test-isolation](README.md) / green-alone-red-together

**Go here if:** Passes alone but fails in the full suite, beside another agent, run or parallel project, or in the first full run after a merge; a database vanishes mid-test; cleanup claims a database it never made.

**Rule:** Own the state you assert on: count only what the test created, by name; give each run, stage and agent its own database or cluster, lifetime tied to its creator; when state cannot be private, serialize every project or group sharing it, not only files within one; teardown restores the baseline successors expect (reset then reseed), on failure too; run the full tier on the merged tip before merge.

12 incidents, 12 occurrences. Ordered by occurrences, then severity, then id.

## Incidents

### [INC-0600](../../incidents/INC-0600-two-branches-each-green-alone-with-a-clean-merge-tree-went-r.md) - Two branches each green alone with a clean merge-tree went red together, because one sanctioned product change altered the label the other test selected by
- occurrences 1, severity high, status mitigated
- **Signature:** A test passes on its own branch and the merged tree is red with no textual conflict.
- **Rule:** A clean merge-tree and two green branches do not show the merge is green; before merging a test that selects by a visible label, run it on a base that holds every sanctioned label change, and audit other specs for the old label.

### [INC-0627](../../incidents/INC-0627-a-new-end-to-end-case-passed-alone-in-its-row-gate-the-merge.md) - A new end-to-end case passed alone in its row gate, the merge went ahead with no full end-to-end tier on the branch tip, and the first full run after the merge failed it
- occurrences 1, severity high, status mitigated
- **Signature:** A case green in its own row fails in the full tier with a module-format load error.
- **Rule:** A branch that adds or changes end-to-end files runs the full end-to-end step before merge; a row gate alone does not show load-order errors.

### [INC-0038](../../incidents/INC-0038-a-determinism-test-that-scans-the-live-working-tree-cannot-p.md) - A determinism test that scans the live working tree cannot pass while another writer edits it
- occurrences 1, severity medium, status open
- **Signature:** A test asserting that two consecutive runs produce identical output fails in the full suite and passes in isolation. The failure moves between runs and correlates with another session's file timestamps rather than with anything that changed under test.
- **Rule:** Determinism is a property of a function over a FIXED input. A test that scans the live working tree twice and compares is really asserting that no other writer touched the tree, so it tests the writers, not the code - and it passes in isolation, which reads as flakiness. Give the test a fixture it owns, or snapshot the input once and assert the snapshot is unchanged.

### [INC-0088](../../incidents/INC-0088-qa-helpers-assumed-rest-field-shapes-that-differ-from-the-de.md) - QA helpers assumed REST field shapes that differ from the design, and integration files mutated shared state without restoring it
- occurrences 1, severity medium, status fixed
- **Signature:** Helpers read fields in a shape the design does not use; a spec passes alone and fails after a file that left state changed.
- **Rule:** Every file that mutates shared state restores it or reseeds, and helpers match the documented field shapes.

### [INC-0096](../../incidents/INC-0096-browser-context-isolation-was-mistaken-for-seed-state-isolat.md) - Browser-context isolation was mistaken for seed-state isolation
- occurrences 1, severity medium, status fixed
- **Signature:** A spec reads seed data while relying on a fresh browser context.
- **Rule:** Isolate each kind of state separately: browser state by context, data by reset and seed.

### [INC-0097](../../incidents/INC-0097-url-guards-did-not-prove-a-test-owned-the-disposable-cluster.md) - URL guards did not prove a test owned the disposable cluster, and shared state was not restored on failure
- occurrences 1, severity medium, status fixed
- **Signature:** A test destroys or mutates state after checking only that the URL looks safe.
- **Rule:** Ownership comes from what the test created; restoration belongs in teardown that runs on failure.

### [INC-0132](../../incidents/INC-0132-vitest-4-ran-projects-in-parallel-and-file-serialization-ins.md) - Vitest 4 ran projects in parallel and file serialization inside a project did not order whole-cluster checks
- occurrences 1, severity medium, status fixed
- **Signature:** Inventory checks across a shared cluster race between projects.
- **Rule:** Serialize across projects explicitly when they share state.

### [INC-0136](../../incidents/INC-0136-a-cross-agent-inventory-flake-came-from-sharing-one-harness.md) - A cross-agent inventory flake came from sharing one harness cluster between runtime agents
- occurrences 1, severity medium, status fixed
- **Signature:** Inventory checks fail when two agents use one cluster.
- **Rule:** Give each agent its own cluster.

### [INC-0138](../../incidents/INC-0138-a-stage-that-kept-a-database-alive-collided-with-later-inven.md) - A stage that kept a database alive collided with later inventory and frozen-clock gc cases
- occurrences 1, severity medium, status fixed
- **Signature:** A leftover database from one stage changes the result of a later stage.
- **Rule:** Tie resource lifetime to its creating stage.

### [INC-0169](../../incidents/INC-0169-a-garbage-collection-test-with-a-moved-clock-reaped-the-oute.md) - A garbage collection test with a moved clock reaped the outer tier own live database
- occurrences 1, severity medium, status fixed
- **Signature:** A test removed a database that belonged to the run that was executing it.
- **Rule:** A test that reaps shared resources must run before the outer run owns any.

### [INC-0360](../../incidents/INC-0360-ownership-registered-before-a-create-made-a-definite-duplica.md) - Ownership registered before a create made a definite duplicate error drop a foreign database
- occurrences 1, severity medium, status fixed
- **Signature:** A harness queued a drop of its test database before creating it, so a create that failed because the name existed would drop a database it never made.
- **Rule:** Ownership recorded before a create covers an uncertain outcome only; on a definite already-exists error release the claim before rethrowing, and test with a pre-existing object under the exact name

### [INC-0361](../../incidents/INC-0361-a-test-s-teardown-emptied-a-shared-server-database-and-a-gat.md) - A test's teardown emptied a shared server database, and a gate that never completed hid the red
- occurrences 1, severity medium, status fixed
- **Signature:** A late end-to-end step could not log in because an earlier test's teardown had deleted the seeded accounts from the shared server database.
- **Rule:** A test that mutates shared state must restore the baseline its successors expect (reset then reseed, never reset only), and the harness should re-establish and check that baseline when each shared step starts; a slow gate with no recorded completion since two tests landed has not tested them together, so treat the main line as unproven until it runs
