# test-isolation

[Catalog](../README.md) / test-isolation

A test passes only in the environment where it was written: it depends on untracked local state, ambient file counts, a directory name, or git history a clean checkout does not have.

**Ask:** Would this test pass in a throwaway fresh clone on a different machine? What ambient state is it silently reading?

**You are probably here if:** A test green on your machine, alone, or on its branch goes red in a fresh clone, CI, the full suite, or next to another run or agent, with no product change.

36 incidents filed here (36 occurrences); 33 more filed elsewhere are also tagged test-isolation.

## Topics

n = occurrences: incidents filed in the topic plus their repeats.

| Topic | Go here if | n | Link |
|---|---|---|---|
| Green alone, red in the full suite, with another run, or after a merge | Passes alone but fails in the full suite, beside another agent, run or parallel project, or in the first full run after a merge; a database vanishes mid-test; cleanup claims a database it never made. | 12 | [green-alone-red-together](green-alone-red-together.md) |
| Assertion measures more than its contract: caches, order, whole totals | Code unchanged: a leak or inventory check flags tool caches or link files; a count over a shared directory or server takes in seed or foreign records, even alone; order on a set; ANSI or raw paths. | 8 | [assertion-wider-than-contract](assertion-wider-than-contract.md) |
| Passes in a warm checkout, fails in a fresh clone, CI or other runner | Green locally or in one run, red in a fresh clone, CI or a different runner: missing gitignored files, git history, an env var, a seed account, a helper, or a server (connection refused). | 8 | [passes-warm-fails-clean](passes-warm-fails-clean.md) |
| The red comes from the test's own fixture, tool option or control | A page that works by hand fails under the test tool; a new positive control fails first; a fixture breaks its own gate or lets a package manager rewrite the host tree; a module lacks an export it has. | 7 | [the-test-itself-is-the-defect](the-test-itself-is-the-defect.md) |

## Class-level incidents

Filed in this class but in none of its topics.

### [INC-0286](../../incidents/INC-0286-fix-module-resolution-once-at-the-root-not-per-test.md) - Fix module resolution once at the root, not per test
- occurrences 1, severity medium, status fixed
- **Signature:** Each test root worked around the same missing dependency in its own way.
- **Rule:** Resolve a shared dependency once at the root and keep test roots on plain imports

## Also tagged test-isolation

33 incidents filed under another home class also carry this class. Listed by the node where they live:

- [ipc-and-env](../ipc-and-env/README.md): INC-0106, INC-0119, INC-0257, INC-0354
- [false-green/mutation-witness-proves-less](../false-green/mutation-witness-proves-less.md): INC-0116, INC-0133, INC-0339
- [false-green/test-cannot-see-the-defect](../false-green/test-cannot-see-the-defect.md): INC-0031, INC-0153, INC-0222
- [false-green/verified-a-different-target](../false-green/verified-a-different-target.md): INC-0190, INC-0208, INC-0214
- [false-green/real-page-or-response-wrong-behind-green](../false-green/real-page-or-response-wrong-behind-green.md): INC-0246, INC-0282
- [false-green/red-for-the-wrong-reason](../false-green/red-for-the-wrong-reason.md): INC-0192, INC-0363
- [concurrency](../concurrency/README.md): INC-0313
- [detector-fail-open](../detector-fail-open/README.md): INC-0150
- [detector-fail-open/coverage-and-controls-not-proven](../detector-fail-open/coverage-and-controls-not-proven.md): INC-0372
- [detector-fail-open/syntax-shapes-and-benign-decoys](../detector-fail-open/syntax-shapes-and-benign-decoys.md): INC-0166
- [false-green](../false-green/README.md): INC-0040
- [false-green/check-satisfied-by-unrelated-cause](../false-green/check-satisfied-by-unrelated-cause.md): INC-0112
- [false-green/green-but-cases-never-ran](../false-green/green-but-cases-never-ran.md): INC-0321
- [spec-and-scope/fix-misses-related-consumers](../spec-and-scope/fix-misses-related-consumers.md): INC-0255
- [spec-and-scope/missing-or-late-prerequisites](../spec-and-scope/missing-or-late-prerequisites.md): INC-0243
- [stage-timeout/timing-models-and-critical-path](../stage-timeout/timing-models-and-critical-path.md): INC-0230
- [stage-timeout/work-outgrows-enforced-timeouts](../stage-timeout/work-outgrows-enforced-timeouts.md): INC-0003
- [tooling-paths/argument-read-as-other-kind](../tooling-paths/argument-read-as-other-kind.md): INC-0137
- [tooling-paths/path-resolves-from-wrong-root](../tooling-paths/path-resolves-from-wrong-root.md): INC-0316
- [tooling-paths/tool-defaults-not-target](../tooling-paths/tool-defaults-not-target.md): INC-0342
- [tooling-paths/tree-lacks-what-job-needs](../tooling-paths/tree-lacks-what-job-needs.md): INC-0288
- [tooling-paths/valid-alone-fails-in-host](../tooling-paths/valid-alone-fails-in-host.md): INC-0178
