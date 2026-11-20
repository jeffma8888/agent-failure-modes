# Assertion measures more than its contract: caches, order, whole totals

[Catalog](../README.md) / [test-isolation](README.md) / assertion-wider-than-contract

**Go here if:** Code unchanged: a leak or inventory check flags tool caches or link files; a count over a shared directory or server takes in seed or foreign records, even alone; order on a set; ANSI or raw paths.

**Rule:** Match the assertion to the contract: count only the identities the case created, never an unfiltered shared total or its delta; compare sorted copies for set membership; strip terminal codes, compare relative or resolved paths; derive expected inventories from source declarations, fail closed on a shape change; name explicitly, never by directory or pattern, the tool-owned paths a check skips.

8 incidents, 8 occurrences. Ordered by occurrences, then severity, then id.

## Incidents

### [INC-0483](../../incidents/INC-0483-a-test-counted-a-whole-shared-directory-and-the-reset-reseed.md) - A test counted a whole shared directory, and the reset reseeded into it
- occurrences 2, severity low, status mitigated
- **Signature:** A total taken over a shared directory included files the case did not create.
- **Rule:** A test that counts a shared directory or table must count only what the case creates, by baseline delta or by name, because the per-test reset and seed change the total.
- **Recurrences:**
  - [INC-0511](../../incidents/INC-0511-a-harness-test-failed-because-another-run-s-orphan-database.md) - 2026-11-02 - A harness test failed because another run's orphan database vanished mid-test, so the test depended on state it did not own

### [INC-0126](../../incidents/INC-0126-test-discovery-was-compared-with-an-absolute-scratch-prefix.md) - Test discovery was compared with an absolute scratch prefix that matched by accident, and guard omission mutants were not each killed
- occurrences 1, severity medium, status fixed
- **Signature:** A discovery comparison passes because an absolute prefix coincidentally lines up.
- **Rule:** Compare relative names and kill every mutant on its own.

### [INC-0084](../../incidents/INC-0084-test-summary-assertions-broke-on-ansi-color-codes-and-compil.md) - Test-summary assertions broke on ANSI color codes, and compile caches were mistaken for resource leaks
- occurrences 1, severity low, status fixed
- **Signature:** A test asserts on tool summary text that contains color escape codes, or a leak check counts cache files.
- **Rule:** Normalize terminal output before matching it, and define what counts as an owned resource before counting leaks.

### [INC-0351](../../incidents/INC-0351-a-physical-copy-of-a-shared-package-store-carried-its-regist.md) - A physical copy of a shared package store carried its registry of outside links
- occurrences 1, severity low, status fixed
- **Signature:** A preparation check that no copied link resolves outside the copy stopped the first authorized run before setup.
- **Rule:** Before copying a shared tool cache into an isolated run, list its links; a registry of outside links is metadata to exclude, while any other outside link is a containment failure

### [INC-0398](../../incidents/INC-0398-a-content-inventory-that-hashed-every-file-under-the-depende.md) - A content inventory that hashed every file under the dependency tree stopped a clean run because the test runner rewrote its result cache there
- occurrences 1, severity low, status fixed
- **Signature:** An inventory guard failed a clean run because one cache file changed.
- **Rule:** Exempt exactly one named path from a content inventory, with its digests recorded; never a directory or pattern

### [INC-0460](../../incidents/INC-0460-an-order-sensitive-comparison-of-two-tool-listings-failed-on.md) - An order sensitive comparison of two tool listings failed only when new files were added, though the contract was set membership
- occurrences 1, severity low, status fixed
- **Signature:** A test failed after unrelated files were added.
- **Rule:** Compare sorted copies when the contract is set membership, and keep order sensitive equality for contracts that define order

### [INC-0537](../../incidents/INC-0537-a-protection-root-pinned-an-exact-seed-inventory-and-a-featu.md) - A protection root pinned an exact seed inventory, and a feature row that grew the seed turned it red
- occurrences 1, severity low, status mitigated
- **Signature:** An active root asserts an exact count of seeded records, and a feature branch adds more records.
- **Rule:** A root that pins an exact inventory should derive it from the source declarations and fail closed on a shape change; a right-reason red from legitimate growth is fixed by a reviewed successor, never by the implementer editing the test.
