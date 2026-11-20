# The red comes from the test's own fixture, tool option or control

[Catalog](../README.md) / [test-isolation](README.md) / the-test-itself-is-the-defect

**Go here if:** A page that works by hand fails under the test tool; a new positive control fails first; a fixture breaks its own gate or lets a package manager rewrite the host tree; a module lacks an export it has.

**Rule:** When a new test, control, fixture or tool option goes red, or never reaches its negative, suspect the test first: reproduce with a minimal variant or a known-good page, bisect the tool's options, compare a hand-written request with the repo helper, keep fixtures from writing outside themselves, and fix it as a tests-only change that keeps the right-reason red.

7 incidents, 7 occurrences. Ordered by occurrences, then severity, then id.

## Incidents

### [INC-0172](../../incidents/INC-0172-a-clean-tree-gate-failed-on-a-fixture-synthetic-repo-before.md) - A clean-tree gate failed on a fixture synthetic repo before the behavior under test
- occurrences 1, severity medium, status fixed
- **Signature:** A test failed at the gate, not at the behavior it meant to exercise.
- **Rule:** A clean-tree gate applies to a fixture synthetic repo too.

### [INC-0183](../../incidents/INC-0183-sibling-fixture-factories-lacked-the-metadata-that-makes-a-c.md) - Sibling fixture factories lacked the metadata that makes a checker required
- occurrences 1, severity medium, status fixed
- **Signature:** A positive control passed without reaching its negative.
- **Rule:** Sibling fixture factories carry the same required metadata.

### [INC-0303](../../incidents/INC-0303-a-guard-added-to-a-test-tool-broke-the-check-under-test.md) - A guard added to a test tool broke the check under test
- occurrences 1, severity medium, status fixed
- **Signature:** A page that works by hand rendered empty under the test tool.
- **Rule:** Test a guard added to a test tool against a known good page, and bisect the tool's options when a page that works by hand fails

### [INC-0320](../../incidents/INC-0320-a-positive-control-s-first-red-was-the-control-s-own-defect.md) - A positive control's first red was the control's own defect
- occurrences 1, severity medium, status fixed
- **Signature:** The control failed because its captured environment overwrote a value the nested runner set.
- **Rule:** When a new positive control fails, suspect the control first, fix it as a tests-only commit and keep the red

### [INC-0340](../../incidents/INC-0340-a-fixture-that-linked-the-host-dependency-tree-let-the-packa.md) - A fixture that linked the host dependency tree let the package manager rewrite it
- occurrences 1, severity medium, status fixed
- **Signature:** A fixture's package manager run pruned the linked host dependency tree and turned 11 failures into 51.
- **Rule:** Never link a writable host dependency tree into a fixture that runs the package manager; if unavoidable, turn auto-install off explicitly in the fixture environment and add a guard that fails when the host tree's listing changes

### [INC-0472](../../incidents/INC-0472-the-first-browser-test-to-load-the-app-config-failed-to-link.md) - The first browser test to load the app config failed to link because one module was reached by two loaders
- occurrences 1, severity low, status fixed
- **Signature:** A module that exports a name was reported as lacking it.
- **Rule:** Reproduce a loader failure with minimal variants before editing product code, and keep modules shared with the app config graph out of static import chains that a test runner compiles differently

### [INC-0602](../../incidents/INC-0602-a-request-context-identity-check-omitted-the-origin-header-t.md) - A request-context identity check omitted the Origin header the repo helper sends and read user null, an author defect that looked like a product failure
- occurrences 1, severity low, status mitigated
- **Signature:** A login returns success but the following identity request reports no user.
- **Rule:** When a hand-written request context reads user null after a good login, compare its headers with the repo helper before blaming the product.
