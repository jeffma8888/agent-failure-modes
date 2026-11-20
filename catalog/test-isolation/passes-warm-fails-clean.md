# Passes in a warm checkout, fails in a fresh clone, CI or other runner

[Catalog](../README.md) / [test-isolation](README.md) / passes-warm-fails-clean

**Go here if:** Green locally or in one run, red in a fresh clone, CI or a different runner: missing gitignored files, git history, an env var, a seed account, a helper, or a server (connection refused).

**Rule:** A test establishes every precondition itself (fixture in tmp_path, seed records, server, env var, full git history) and the runner owns the scratch paths its tests write to. Before calling it green, run it once in a fresh clone with nothing exported; before reading a red as a regression, run the same files under the same runner on main.

8 incidents, 8 occurrences. Ordered by occurrences, then severity, then id.

## Incidents

### [INC-0022](../../incidents/INC-0022-test-precondition-on-gitignored-local-state-passes-only-on-t.md) - Test precondition on gitignored local state passes only on this machine
- occurrences 1, severity high, status fixed
- **Signature:** A test passes locally on every developer machine, then fails immediately in a fresh CI clone. The diff between environments is directories or files gitignored by policy.
- **Rule:** A test that reads ambient filesystem state depends on gitignored files a fresh clone does not have. Before asserting on a path, ask whether git tracks it; if not, build the fixture yourself in `tmp_path` instead of asserting on the ambient tree. A test that passes only on this machine is not a test.

### [INC-0023](../../incidents/INC-0023-ci-shallow-clone-breaks-tests-that-read-git-history.md) - CI shallow clone breaks tests that read git history
- occurrences 1, severity medium, status fixed
- **Signature:** Tests pass locally, fail in CI, and none of them are testing the code under review. The failures reference git-history-shaped values.
- **Rule:** CI defaults to a depth-1 clone; any test that reads git history sees a different world there. Set `fetch-depth: 0`. Before blaming the commit under test, ask what CI's environment does NOT have: git history, tags, submodules, a TTY, network, timezone, locale. A synthetic depth-1 clone locally reproduces the failure in one step.

### [INC-0110](../../incidents/INC-0110-a-cross-row-test-needed-setup-absent-from-its-own-lifecycle.md) - A cross-row test needed setup absent from its own lifecycle, and green was claimed without a fresh-clone setup or a canonical temp directory
- occurrences 1, severity medium, status fixed
- **Signature:** A test passes in a warm checkout and needs a database or path that the fresh lifecycle never creates.
- **Rule:** Run from a clean state and compare resolved paths before reporting a pass.

### [INC-0297](../../incidents/INC-0297-a-test-needed-a-second-account-that-the-minimal-seed-did-not.md) - A test needed a second account that the minimal seed did not create
- occurrences 1, severity medium, status fixed
- **Signature:** Cases looked up a second admin account that the seed lacked.
- **Rule:** Check each test's seed needs against the seed its declared dependencies provide

### [INC-0299](../../incidents/INC-0299-a-row-only-overlay-left-out-the-helpers-of-a-dependency-row.md) - A row-only overlay left out the helpers of a dependency row, so consumers looked blocked
- occurrences 1, severity medium, status fixed
- **Signature:** Consumer files failed to import helpers that a declared dependency owns.
- **Rule:** Confirm the helpers owned by dependency rows are active in the base before judging a consumer blocked or red

### [INC-0495](../../incidents/INC-0495-the-acceptance-run-lacked-an-environment-variable-that-the-b.md) - The acceptance run lacked an environment variable that the branch run and the full suite set
- occurrences 1, severity low, status mitigated
- **Signature:** The only new failure in the acceptance run was a test that throws when one environment variable is absent.
- **Rule:** Record the environment of every run you compare, and give the acceptance run the same environment the full suite gives.

### [INC-0550](../../incidents/INC-0550-integration-files-that-need-a-live-server-failed-with-connec.md) - Integration files that need a live server failed with connection refused under a runner that starts none, first read as a branch regression
- occurrences 1, severity low, status mitigated
- **Signature:** Tests fail with connection refused on a branch, and the cause is a missing precondition of the runner.
- **Rule:** Before reading a red as a regression, run the same files with the same runner on the main branch; a connection refused under a runner that starts no server is a precondition, not a regression.

### [INC-0583](../../incidents/INC-0583-a-unit-row-passed-only-because-the-caller-exported-a-scratch.md) - A unit row passed only because the caller exported a scratch media directory, and the runner did not own one
- occurrences 1, severity low, status mitigated
- **Signature:** A row passes only when the caller environment supplies a path the runner should own.
- **Rule:** A runner must own the scratch directories its tests write to and ignore caller values for that tier; a row that passes only with an exported path is not green.
