# A planned step cannot run because its prerequisite is missing

[Catalog](../README.md) / [spec-and-scope](README.md) / missing-or-late-prerequisites

**Go here if:** A row needs data, types, a callable seam, a component, or approval that arrives later; pressure grows to invent a stub or weaken the contract.

**Rule:** Trace each step to its actual inputs, declared callable seams, owners, and approvals, then order required prerequisites before consumers without inventing dependencies or stubs.

11 incidents, 11 occurrences. Ordered by occurrences, then severity, then id.

## Incidents

### [INC-0075](../../incidents/INC-0075-tests-and-code-were-written-against-a-spec-before-its-indepe.md) - Tests and code were written against a spec before its independent review returned, and the rulings then changed
- occurrences 1, severity medium, status mitigated
- **Signature:** Downstream roles start in parallel with the independent review of the document they depend on, to keep everyone busy.
- **Rule:** An independent spec review is a gate, not a parallel track. Keep idle teammates busy with work that does not depend on the spec's open rulings.

### [INC-0100](../../incidents/INC-0100-a-new-test-file-was-placed-in-a-row-whose-activation-order-d.md) - A new test file was placed in a row whose activation order did not include a collection the file creates, and an oracle was asserted without its spec sentence
- occurrences 1, severity medium, status fixed
- **Signature:** A test creates a collection or relies on a rule that the row order or spec does not support.
- **Rule:** Place tests by activation order and quote the spec before asserting.

### [INC-0109](../../incidents/INC-0109-a-ui-test-was-accepted-although-no-plan-row-owned-a-custom-u.md) - A UI test was accepted although no plan row owned a custom UI component it needed
- occurrences 1, severity medium, status fixed
- **Signature:** A test drives a component that no row builds, so the last row meets a missing UI.
- **Rule:** Every component a test needs has an owning row.

### [INC-0115](../../incidents/INC-0115-rows-that-point-at-a-relationship-target-were-ordered-before.md) - Rows that point at a relationship target were ordered before the target was registered, tempting stubs or optional fields
- occurrences 1, severity medium, status fixed
- **Signature:** A row needs a related record that a later row creates.
- **Rule:** Fix the order, not the contract.

### [INC-0242](../../incidents/INC-0242-four-of-five-test-authors-stopped-at-the-same-undeclared-sea.md) - Four of five test authors stopped at the same undeclared seam
- occurrences 1, severity medium, status fixed
- **Signature:** Authors stopped at the same boundary.
- **Rule:** Audit a proposed test by the seam it declares, and checkpoint per root rather than per batch

### [INC-0243](../../incidents/INC-0243-a-proposed-subject-was-treated-as-if-its-seam-were-declared.md) - A proposed subject was treated as if its seam were declared
- occurrences 1, severity medium, status fixed
- **Signature:** The missing binding was not declared anywhere.
- **Rule:** Declare the import seam; ownership or authorization of a subject does not declare a callable boundary

### [INC-0269](../../incidents/INC-0269-drop-a-rehearsal-step-that-needs-a-missing-input-channel.md) - Drop a rehearsal step that needs a missing input channel
- occurrences 1, severity medium, status fixed
- **Signature:** A rehearsal step could only pass if its input was faked.
- **Rule:** Drop a step that needs a missing channel rather than faking it

### [INC-0304](../../incidents/INC-0304-a-test-was-about-to-move-to-satisfy-a-dependency-without-rea.md) - A test was about to move to satisfy a dependency without reading what it asserts
- occurrences 1, severity medium, status fixed
- **Signature:** A proposed move would have removed the only browser acceptance for two rows.
- **Rule:** A dependency edge does not justify moving a test; check what it asserts and what acceptance the move would remove

### [INC-0353](../../incidents/INC-0353-an-authorization-point-was-placed-after-the-first-event-that.md) - An authorization point was placed after the first event that needs the identity
- occurrences 1, severity medium, status fixed
- **Signature:** A spec required records emitted early in a run to carry an identifier that was not created until later in the run.
- **Rule:** Put the authorization point before the first event that must carry the identity, and test the forged-object negative

### [INC-0063](../../incidents/INC-0063-a-spec-that-tightened-validation-before-the-data-migration-m.md) - A spec that tightened validation before the data migration made every real-data test fail
- occurrences 1, severity low, status fixed
- **Signature:** A new spec makes a field required, while the step that adds that field to the existing data is scheduled after the code.
- **Rule:** When a spec tightens validation, order the data migration before the code, or give the implementer an explicit scratch-copy check, so code defects and missing data are tested separately.

### [INC-0429](../../incidents/INC-0429-a-dependency-question-was-answered-by-the-backlog-itself-a-r.md) - A dependency question was answered by the backlog itself, a relation owned by a later row, so no wait was needed
- occurrences 1, severity low, status fixed
- **Signature:** A spec raised a wait on something a later row was already scheduled to add.
- **Rule:** Before waiting on a dependency, read the backlog for the row that owns it; if a later row owns it, ship without it and add no stub
