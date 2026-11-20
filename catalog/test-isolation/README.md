# test-isolation

[Catalog](../README.md) / test-isolation

A test passes only in the environment where it was written: it depends on untracked local state, ambient file counts, a directory name, or git history a clean checkout does not have.

**Ask:** Would this test pass in a throwaway fresh clone on a different machine? What ambient state is it silently reading?

36 incidents filed here (36 occurrences); 33 more filed elsewhere are also tagged test-isolation.

## Incidents

This class has no topics, so this node is the leaf. Ordered by occurrences, then severity, then id.

### [INC-0022](../../incidents/INC-0022-test-precondition-on-gitignored-local-state-passes-only-on-t.md) - Test precondition on gitignored local state passes only on this machine
- occurrences 1, severity high, status fixed
- **Signature:** A test passes locally on every developer machine, then fails immediately in a fresh CI clone. The diff between environments is directories or files gitignored by policy.
- **Rule:** A test that reads ambient filesystem state depends on gitignored files a fresh clone does not have. Before asserting on a path, ask whether git tracks it; if not, build the fixture yourself in `tmp_path` instead of asserting on the ambient tree. A test that passes only on this machine is not a test.

### [INC-0600](../../incidents/INC-0600-two-branches-each-green-alone-with-a-clean-merge-tree-went-r.md) - Two branches each green alone with a clean merge-tree went red together, because one sanctioned product change altered the label the other test selected by
- occurrences 1, severity high, status mitigated
- **Signature:** A test passes on its own branch and the merged tree is red with no textual conflict.
- **Rule:** A clean merge-tree and two green branches do not show the merge is green; before merging a test that selects by a visible label, run it on a base that holds every sanctioned label change, and audit other specs for the old label.

### [INC-0627](../../incidents/INC-0627-a-new-end-to-end-case-passed-alone-in-its-row-gate-the-merge.md) - A new end-to-end case passed alone in its row gate, the merge went ahead with no full end-to-end tier on the branch tip, and the first full run after the merge failed it
- occurrences 1, severity high, status mitigated
- **Signature:** A case green in its own row fails in the full tier with a module-format load error.
- **Rule:** A branch that adds or changes end-to-end files runs the full end-to-end step before merge; a row gate alone does not show load-order errors.

### [INC-0023](../../incidents/INC-0023-ci-shallow-clone-breaks-tests-that-read-git-history.md) - CI shallow clone breaks tests that read git history
- occurrences 1, severity medium, status fixed
- **Signature:** Tests pass locally, fail in CI, and none of them are testing the code under review. The failures reference git-history-shaped values.
- **Rule:** CI defaults to a depth-1 clone; any test that reads git history sees a different world there. Set `fetch-depth: 0`. Before blaming the commit under test, ask what CI's environment does NOT have: git history, tags, submodules, a TTY, network, timezone, locale. A synthetic depth-1 clone locally reproduces the failure in one step.

### [INC-0038](../../incidents/INC-0038-a-determinism-test-that-scans-the-live-working-tree-cannot-p.md) - A determinism test that scans the live working tree cannot pass while another writer edits it
- occurrences 1, severity medium, status open
- **Signature:** A test asserting that two consecutive runs produce identical output fails in the full suite and passes in isolation. The failure moves between runs and correlates with another session's file timestamps rather than with anything that changed under test.
- **Rule:** Determinism is a property of a function over a FIXED input. A test that scans the live working tree twice and compares is really asserting that no other writer touched the tree, so it tests the writers, not the code - and it passes in isolation, which reads as flakiness. Give the test a fixture it owns, or snapshot the input once and assert the snapshot is unchanged.

### [INC-0088](../../incidents/INC-0088-qa-helpers-assumed-rest-field-shapes-that-differ-from-the-de.md) - QA helpers assumed REST field shapes that differ from the design, and integration files mutated shared state without restoring it
- occurrences 1, severity medium, status fixed
- **Signature:** Helpers read fields in a shape the design does not use; a spec passes alone and fails after a file that left state changed.
- **Rule:** Every file that mutates shared state restores it or reseeds, and helpers match the documented field shapes.

The 30 entries below are listed by title only so this node stays under 12 KB. Open the page, or run `python3 tools/afm.py show INC-XXXX`, for its signature and rule.

- [INC-0096](../../incidents/INC-0096-browser-context-isolation-was-mistaken-for-seed-state-isolat.md) - Browser-context isolation was mistaken for seed-state isolation (n=1, medium)
- [INC-0097](../../incidents/INC-0097-url-guards-did-not-prove-a-test-owned-the-disposable-cluster.md) - URL guards did not prove a test owned the disposable cluster, and shared state was not restored on failure (n=1, medium)
- [INC-0110](../../incidents/INC-0110-a-cross-row-test-needed-setup-absent-from-its-own-lifecycle.md) - A cross-row test needed setup absent from its own lifecycle, and green was claimed without a fresh-clone setup or a canonical temp directory (n=1, medium)
- [INC-0126](../../incidents/INC-0126-test-discovery-was-compared-with-an-absolute-scratch-prefix.md) - Test discovery was compared with an absolute scratch prefix that matched by accident, and guard omission mutants were not each killed (n=1, medium)
- [INC-0132](../../incidents/INC-0132-vitest-4-ran-projects-in-parallel-and-file-serialization-ins.md) - Vitest 4 ran projects in parallel and file serialization inside a project did not order whole-cluster checks (n=1, medium)
- [INC-0136](../../incidents/INC-0136-a-cross-agent-inventory-flake-came-from-sharing-one-harness.md) - A cross-agent inventory flake came from sharing one harness cluster between runtime agents (n=1, medium)
- [INC-0138](../../incidents/INC-0138-a-stage-that-kept-a-database-alive-collided-with-later-inven.md) - A stage that kept a database alive collided with later inventory and frozen-clock gc cases (n=1, medium)
- [INC-0169](../../incidents/INC-0169-a-garbage-collection-test-with-a-moved-clock-reaped-the-oute.md) - A garbage collection test with a moved clock reaped the outer tier own live database (n=1, medium)
- [INC-0172](../../incidents/INC-0172-a-clean-tree-gate-failed-on-a-fixture-synthetic-repo-before.md) - A clean-tree gate failed on a fixture synthetic repo before the behavior under test (n=1, medium)
- [INC-0183](../../incidents/INC-0183-sibling-fixture-factories-lacked-the-metadata-that-makes-a-c.md) - Sibling fixture factories lacked the metadata that makes a checker required (n=1, medium)
- [INC-0286](../../incidents/INC-0286-fix-module-resolution-once-at-the-root-not-per-test.md) - Fix module resolution once at the root, not per test (n=1, medium)
- [INC-0297](../../incidents/INC-0297-a-test-needed-a-second-account-that-the-minimal-seed-did-not.md) - A test needed a second account that the minimal seed did not create (n=1, medium)
- [INC-0299](../../incidents/INC-0299-a-row-only-overlay-left-out-the-helpers-of-a-dependency-row.md) - A row-only overlay left out the helpers of a dependency row, so consumers looked blocked (n=1, medium)
- [INC-0303](../../incidents/INC-0303-a-guard-added-to-a-test-tool-broke-the-check-under-test.md) - A guard added to a test tool broke the check under test (n=1, medium)
- [INC-0320](../../incidents/INC-0320-a-positive-control-s-first-red-was-the-control-s-own-defect.md) - A positive control's first red was the control's own defect (n=1, medium)
- [INC-0340](../../incidents/INC-0340-a-fixture-that-linked-the-host-dependency-tree-let-the-packa.md) - A fixture that linked the host dependency tree let the package manager rewrite it (n=1, medium)
- [INC-0360](../../incidents/INC-0360-ownership-registered-before-a-create-made-a-definite-duplica.md) - Ownership registered before a create made a definite duplicate error drop a foreign database (n=1, medium)
- [INC-0361](../../incidents/INC-0361-a-test-s-teardown-emptied-a-shared-server-database-and-a-gat.md) - A test's teardown emptied a shared server database, and a gate that never completed hid the red (n=1, medium)
- [INC-0084](../../incidents/INC-0084-test-summary-assertions-broke-on-ansi-color-codes-and-compil.md) - Test-summary assertions broke on ANSI color codes, and compile caches were mistaken for resource leaks (n=1, low)
- [INC-0351](../../incidents/INC-0351-a-physical-copy-of-a-shared-package-store-carried-its-regist.md) - A physical copy of a shared package store carried its registry of outside links (n=1, low)
- [INC-0398](../../incidents/INC-0398-a-content-inventory-that-hashed-every-file-under-the-depende.md) - A content inventory that hashed every file under the dependency tree stopped a clean run because the test runner rewrote its result cache there (n=1, low)
- [INC-0460](../../incidents/INC-0460-an-order-sensitive-comparison-of-two-tool-listings-failed-on.md) - An order sensitive comparison of two tool listings failed only when new files were added, though the contract was set membership (n=1, low)
- [INC-0472](../../incidents/INC-0472-the-first-browser-test-to-load-the-app-config-failed-to-link.md) - The first browser test to load the app config failed to link because one module was reached by two loaders (n=1, low)
- [INC-0483](../../incidents/INC-0483-a-test-counted-a-whole-shared-directory-and-the-reset-reseed.md) - A test counted a whole shared directory, and the reset reseeded into it (n=1, low)
- [INC-0495](../../incidents/INC-0495-the-acceptance-run-lacked-an-environment-variable-that-the-b.md) - The acceptance run lacked an environment variable that the branch run and the full suite set (n=1, low)
- [INC-0511](../../incidents/INC-0511-a-harness-test-failed-because-another-run-s-orphan-database.md) - A harness test failed because another run's orphan database vanished mid-test, so the test depended on state it did not own (n=1, low)
- [INC-0537](../../incidents/INC-0537-a-protection-root-pinned-an-exact-seed-inventory-and-a-featu.md) - A protection root pinned an exact seed inventory, and a feature row that grew the seed turned it red (n=1, low)
- [INC-0550](../../incidents/INC-0550-integration-files-that-need-a-live-server-failed-with-connec.md) - Integration files that need a live server failed with connection refused under a runner that starts none, first read as a branch regression (n=1, low)
- [INC-0583](../../incidents/INC-0583-a-unit-row-passed-only-because-the-caller-exported-a-scratch.md) - A unit row passed only because the caller exported a scratch media directory, and the runner did not own one (n=1, low)
- [INC-0602](../../incidents/INC-0602-a-request-context-identity-check-omitted-the-origin-header-t.md) - A request-context identity check omitted the Origin header the repo helper sends and read user null, an author defect that looked like a product failure (n=1, low)

## Also tagged test-isolation

33 incidents filed under another home class also carry this class. Listed by the node where they live:

- [false-green](../false-green/README.md): INC-0031, INC-0040, INC-0112, INC-0116, INC-0133, INC-0153, INC-0190, INC-0192, INC-0208, INC-0214, INC-0222, INC-0246, INC-0282, INC-0321, INC-0339, INC-0363
- [tooling-paths](../tooling-paths/README.md): INC-0137, INC-0178, INC-0288, INC-0316, INC-0342
- [ipc-and-env](../ipc-and-env/README.md): INC-0106, INC-0119, INC-0257, INC-0354
- [detector-fail-open](../detector-fail-open/README.md): INC-0150, INC-0166, INC-0372
- [spec-and-scope](../spec-and-scope/README.md): INC-0243, INC-0255
- [stage-timeout](../stage-timeout/README.md): INC-0003, INC-0230
- [concurrency](../concurrency/README.md): INC-0313
