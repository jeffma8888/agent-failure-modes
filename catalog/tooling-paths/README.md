# tooling-paths

[Catalog](../README.md) / tooling-paths

The shell or tool layer betrays you: command substitution runs inside a string you meant as data, a built-in resolves paths from an unexpected root, an interpreter shim mutates the wrong environment.

**Ask:** Will any character in this string be interpreted rather than stored, and from what directory does this tool actually resolve paths?

**You are probably here if:** A command did other than you typed: a value truncated, a path refused or resolved elsewhere, a chain ran on after a failure, the wrong binary or tree answered.

68 incidents filed here (68 occurrences); 30 more filed elsewhere are also tagged tooling-paths.

## Topics

n = occurrences: incidents filed in the topic plus their recorded repeats.

| Topic | Go here if | n | Link |
|---|---|---|---|
| A helper or runner reads your argument as a different kind or name | A bare file name taken as a root name, an item named twice acted on twice, a revision id refused where the runner wants the base row, an option the runner lacks is requested, a missing db gets created | 10 | [argument-read-as-other-kind](argument-read-as-other-kind.md) |
| An edit anchor or text match hit different bytes than you meant | Empty () or control characters in a file you just wrote; a symbol vanished or doubled after a 'confined' edit; a rewrite changed only a prefix; zero matches in visible text; a guard matched itself | 8 | [edit-or-match-hit-wrong-bytes](edit-or-match-hit-wrong-bytes.md) |
| The tool's own resolution or defaults, not the target, caused it | 'command not found' in a log, a syntax check ran the script, a launch with no process or output, a wrapper ran zero tests, a scoped-config error the real build never raises, a fetch called 'blocked' | 8 | [tool-defaults-not-target](tool-defaults-not-target.md) |
| Code valid alone fails in the host runtime, module form or generator | A spec or helper fails at collection or load (fixture name clash, import.meta under CommonJS, non-erasable syntax); a generated file dirties the tree, fails type-check or lint, or cannot round-trip | 8 | [valid-alone-fails-in-host](valid-alone-fails-in-host.md) |
| zsh reads your variable differently: colon modifier, word split, array | A value is silently truncated, 'bad object name' on sha:path, a hash equals the hash of empty input, a loop sends one argument or none, one of two files committed, a checker ran without its env. | 7 | [zsh-expansion-surprises](zsh-expansion-surprises.md) |
| A shell chain ran on after a failed step, or a refusal sank safe steps | A commit, push or cleanup ran although an earlier edit or check failed; the chain saw the formatter's status; a script died in an unrehearsed step; an approval refusal discarded bundled edits. | 6 | [chain-ran-on-after-failure](chain-ran-on-after-failure.md) |
| A relative path or link resolves from a different root than assumed | Imports or links break after a file moves, is copied or activates at another depth; a relative path lands outside the workspace; a compare follows symlinks into the host; a link dangles from one tree | 6 | [path-resolves-from-wrong-root](path-resolves-from-wrong-root.md) |
| Sandbox cannot resolve or authorize the target you actually meant | Refused as outside the workspace though the path is allowed, a regex literal blocked as a path, cd to a variable refused, a search refused as a home-directory scan, a setuid tool denied by a profile. | 6 | [sandbox-refuses-allowed-target](sandbox-refuses-allowed-target.md) |
| The checkout or dependency tree you ran in lacks what the job needs | Module not found from a worktree on an older base, a tracked file 'missing' in a sparse checkout, every check exits early, an install hits the network or fails offline, a lockfile regen changes more | 6 | [tree-lacks-what-job-needs](tree-lacks-what-job-needs.md) |

## Class-level incidents

Filed in this class but in none of its topics.

### [INC-0081](../../incidents/INC-0081-reviewers-and-qa-wrote-absolute-home-paths-and-notes-paths-i.md) - Reviewers and QA wrote absolute home paths and notes paths into repository docs, and only the push guard caught them
- occurrences 1, severity low, status fixed
- **Signature:** Documents authored by several agents cite local files by absolute path or by the location of private lead notes.
- **Rule:** Tell authors how to cite private material in the brief, and keep the leak scan as a pre-push gate rather than the only control.

### [INC-0407](../../incidents/INC-0407-a-lead-signature-line-containing-the-assistant-s-product-nam.md) - A lead signature line containing the assistant's product name failed the scrub
- occurrences 1, severity low, status fixed
- **Signature:** A signature line failed the scrub.
- **Rule:** Sign with a role name; a product name in a signature line fails the scrub

### [INC-0437](../../incidents/INC-0437-evidence-receipts-leaked-absolute-paths-into-branch-history.md) - Evidence receipts leaked absolute paths into branch history, and the lead landed by squash instead of rewriting history
- occurrences 1, severity low, status fixed
- **Signature:** The leak guard reported absolute paths and a tool name inside evidence files.
- **Rule:** Write evidence commands with placeholders for paths and tools; handle leaked history by a squash landing that keeps the original branch as the local audit trail

## Also tagged tooling-paths

30 incidents filed under another home class also carry this class. Listed by the node where they live:

- [false-green/green-but-cases-never-ran](../false-green/green-but-cases-never-ran.md): INC-0196, INC-0203, INC-0356
- [vcs-destruction](../vcs-destruction/README.md): INC-0114, INC-0162, INC-0309
- [concurrency](../concurrency/README.md): INC-0117, INC-0368
- [detector-fail-closed](../detector-fail-closed/README.md): INC-0238, INC-0327
- [false-green/step-failed-but-gate-passed](../false-green/step-failed-but-gate-passed.md): INC-0280, INC-0322
- [false-green/verified-a-different-target](../false-green/verified-a-different-target.md): INC-0163, INC-0344
- [delegation/order-collides-with-rule-or-guard](../delegation/order-collides-with-rule-or-guard.md): INC-0179
- [detector-fail-open/coverage-and-controls-not-proven](../detector-fail-open/coverage-and-controls-not-proven.md): INC-0037
- [detector-fail-open/wrong-parser-or-pattern](../detector-fail-open/wrong-parser-or-pattern.md): INC-0029
- [false-green](../false-green/README.md): INC-0205
- [false-green/check-satisfied-by-unrelated-cause](../false-green/check-satisfied-by-unrelated-cause.md): INC-0058
- [false-green/count-or-total-computed-wrong](../false-green/count-or-total-computed-wrong.md): INC-0070
- [false-green/oracle-or-claim-written-from-memory](../false-green/oracle-or-claim-written-from-memory.md): INC-0056
- [false-green/red-for-the-wrong-reason](../false-green/red-for-the-wrong-reason.md): INC-0200
- [observability/misleading-metrics-and-status](../observability/misleading-metrics-and-status.md): INC-0073
- [spec-and-scope/instructions-tools-cannot-follow](../spec-and-scope/instructions-tools-cannot-follow.md): INC-0267
- [spec-and-scope/requirements-and-limits-collide](../spec-and-scope/requirements-and-limits-collide.md): INC-0189
- [spec-and-scope/tests-do-not-prove-the-contract](../spec-and-scope/tests-do-not-prove-the-contract.md): INC-0332
- [stale-module](../stale-module/README.md): INC-0123
- [test-isolation](../test-isolation/README.md): INC-0286
- [test-isolation/assertion-wider-than-contract](../test-isolation/assertion-wider-than-contract.md): INC-0351
- [test-isolation/the-test-itself-is-the-defect](../test-isolation/the-test-itself-is-the-defect.md): INC-0340

## Practices touching this class

- [PRA-0004](../CORE.md#practices) - Choose the constraint surface before choosing the enforcement strength
