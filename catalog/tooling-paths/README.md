# tooling-paths

[Catalog](../README.md) / tooling-paths

The shell or tool layer betrays you: command substitution runs inside a string you meant as data, a built-in resolves paths from an unexpected root, an interpreter shim mutates the wrong environment.

**Ask:** Will any character in this string be interpreted rather than stored, and from what directory does this tool actually resolve paths?

68 incidents filed here (68 occurrences); 30 more filed elsewhere are also tagged tooling-paths.

## Incidents

This class has no topics, so this node is the leaf. Ordered by occurrences, then severity, then id.

The 68 entries below are listed by title only so this node stays under 12 KB. Open the page, or run `python3 tools/afm.py show INC-XXXX`, for its signature and rule.

- [INC-0024](../../incidents/INC-0024-backtick-command-substitution-in-a-heredoc-corrupts-and-exec.md) - Backtick command substitution in a heredoc corrupts and executes (n=1, high)
- [INC-0030](../../incidents/INC-0030-rewriting-a-region-by-slicing-between-two-markers-deletes-wh.md) - Rewriting a region by slicing between two markers deletes whatever else lives there (n=1, high)
- [INC-0043](../../incidents/INC-0043-an-anchored-replace-that-matches-a-prefix-of-a-line-is-still.md) - An anchored replace that matches a PREFIX of a line is still 'exactly once' (n=1, high)
- [INC-0633](../../incidents/INC-0633-an-untracked-workspace-link-in-the-main-checkout-was-rewritt.md) - An untracked workspace link in the main checkout was rewritten during a sibling worktree's provisioning to a target that only worked from main by accident, and four days later a gate that copied dependencies failed in a way that looked like a product fault (n=1, high)
- [INC-0072](../../incidents/INC-0072-four-different-fetch-failures-were-all-reported-as-the-site.md) - Four different fetch failures were all reported as 'the site blocks automated access' (n=1, medium)
- [INC-0094](../../incidents/INC-0094-macos-sandbox-exec-refused-to-exec-a-setuid-binary-so-a-sand.md) - macOS sandbox-exec refused to exec a setuid binary, so a sandboxed acceptance profile failed on the process-introspection tool (n=1, medium)
- [INC-0137](../../incidents/INC-0137-a-database-adapter-created-an-absent-database-even-with-sche.md) - A database adapter created an absent database even with schema push disabled (n=1, medium)
- [INC-0156](../../incidents/INC-0156-a-test-fixture-name-collided-with-a-framework-built-in-and-o.md) - A test fixture name collided with a framework built-in and only collection revealed it (n=1, medium)
- [INC-0158](../../incidents/INC-0158-a-spec-used-import-meta-under-a-package-that-loads-specs-as.md) - A spec used import.meta under a package that loads specs as CommonJS (n=1, medium)
- [INC-0165](../../incidents/INC-0165-a-shell-variable-followed-by-a-colon-and-a-letter-became-a-h.md) - A shell variable followed by a colon and a letter became a history modifier (n=1, medium)
- [INC-0170](../../incidents/INC-0170-a-tracked-file-rewritten-per-tool-mode-could-not-stay-clean.md) - A tracked file rewritten per tool mode could not stay clean in both tiers (n=1, medium)
- [INC-0171](../../incidents/INC-0171-a-generator-default-module-augmentation-made-its-committed-o.md) - A generator default module augmentation made its committed output fail the type check (n=1, medium)
- [INC-0177](../../incidents/INC-0177-card-text-pointed-at-its-own-directory-as-the-checkout.md) - Card text pointed at its own directory as the checkout (n=1, medium)
- [INC-0178](../../incidents/INC-0178-a-production-build-dirtied-the-tree-and-an-example-role-was.md) - A production build dirtied the tree and an example role was missing locally (n=1, medium)
- [INC-0181](../../incidents/INC-0181-a-package-launcher-in-an-uninstalled-source-clone-reached-fo.md) - A package launcher in an uninstalled source clone reached for the registry (n=1, medium)
- [INC-0188](../../incidents/INC-0188-an-override-changed-the-lockfile-and-an-offline-clone-could.md) - An override changed the lockfile and an offline clone could not install it (n=1, medium)
- [INC-0207](../../incidents/INC-0207-three-sends-failed-because-a-packed-string-went-out-as-one-a.md) - Three sends failed because a packed string went out as one argument (n=1, medium)
- [INC-0211](../../incidents/INC-0211-a-regex-literal-was-read-as-a-file-path-by-the-permission-ch.md) - A regex literal was read as a file path by the permission checker (n=1, medium)
- [INC-0212](../../incidents/INC-0212-a-relative-path-was-resolved-against-the-wrong-root.md) - A relative path was resolved against the wrong root (n=1, medium)
- [INC-0248](../../incidents/INC-0248-the-env-script-could-not-be-sourced-in-zsh.md) - The env script could not be sourced in zsh (n=1, medium)
- [INC-0249](../../incidents/INC-0249-a-cd-to-a-path-in-a-variable-was-refused-by-the-sandbox.md) - A cd to a path in a variable was refused by the sandbox (n=1, medium)
- [INC-0260](../../incidents/INC-0260-prove-an-alias-fix-by-the-exact-sha-run-with-the-default-spe.md) - Prove an alias fix by the exact-SHA run with the default spelling (n=1, medium)
- [INC-0264](../../incidents/INC-0264-run-repo-checkers-from-a-tree-that-contains-them.md) - Run repo checkers from a tree that contains them (n=1, medium)
- [INC-0278](../../incidents/INC-0278-brace-a-shell-variable-that-is-followed-by-a-colon.md) - Brace a shell variable that is followed by a colon (n=1, medium)
- [INC-0288](../../incidents/INC-0288-verify-a-worktree-can-run-the-required-checks-before-assigni.md) - Verify a worktree can run the required checks before assigning work there (n=1, medium)
- [INC-0294](../../incidents/INC-0294-activating-a-replacement-over-the-only-file-in-a-directory-r.md) - Activating a replacement over the only file in a directory removed the directory (n=1, medium)
- [INC-0301](../../incidents/INC-0301-an-offline-lockfile-regeneration-carried-an-unrelated-stale.md) - An offline lockfile regeneration carried an unrelated stale resolution (n=1, medium)
- [INC-0307](../../incidents/INC-0307-a-measurement-wrapper-inherited-the-environment-the-tests-re.md) - A measurement wrapper inherited the environment the tests replace (n=1, medium)
- [INC-0316](../../incidents/INC-0316-a-recursive-diff-of-a-copied-tree-followed-fixture-symlinks.md) - A recursive diff of a copied tree followed fixture symlinks into the host (n=1, medium)
- [INC-0319](../../incidents/INC-0319-a-sparse-checkout-hid-a-tracked-file-that-every-brief-pointe.md) - A sparse checkout hid a tracked file that every brief pointed at (n=1, medium)
- [INC-0342](../../incidents/INC-0342-a-shortcut-launcher-lacked-the-protection-the-canonical-entr.md) - A shortcut launcher lacked the protection the canonical entry supplies implicitly (n=1, medium)
- [INC-0364](../../incidents/INC-0364-a-hand-written-landing-chain-swallowed-a-failed-post-commit.md) - A hand-written landing chain swallowed a failed post-commit leak scan and three commits landed on top (n=1, medium)
- [INC-0532](../../incidents/INC-0532-test-roots-imported-helpers-by-paths-anchored-at-their-pendi.md) - Test roots imported helpers by paths anchored at their pending depth, so every import would break at the active destination (n=1, medium)
- [INC-0597](../../incidents/INC-0597-a-run-before-approve-test-asked-for-a-runtime-route-that-kee.md) - A run-before-approve test asked for a runtime route that keeps the harness untouched instead of bypassing identity (n=1, medium)
- [INC-0046](../../incidents/INC-0046-a-script-with-external-writes-was-only-dry-run-for-its-first.md) - A script with external writes was only dry-run for its first step, and only write-last ordering made its failure harmless (n=1, low)
- [INC-0047](../../incidents/INC-0047-in-an-ordered-replacement-list-a-general-rule-placed-before.md) - In an ordered replacement list, a general rule placed before a specific one consumes its match (n=1, low)
- [INC-0050](../../incidents/INC-0050-bundling-safe-local-steps-with-an-approval-gated-step-loses.md) - Bundling safe local steps with an approval-gated step loses the local steps when the gate refuses (n=1, low)
- [INC-0051](../../incidents/INC-0051-a-fallible-edit-script-followed-by-a-semicolon-let-the-commi.md) - A fallible edit script followed by a semicolon let the commit run on a partial result (n=1, low)
- [INC-0060](../../incidents/INC-0060-a-probe-hung-on-a-background-child-that-held-the-pipe-and-th.md) - A probe hung on a background child that held the pipe, and the timeout wrapper it relied on did not exist (n=1, low)
- [INC-0081](../../incidents/INC-0081-reviewers-and-qa-wrote-absolute-home-paths-and-notes-paths-i.md) - Reviewers and QA wrote absolute home paths and notes paths into repository docs, and only the push guard caught them (n=1, low)
- [INC-0090](../../incidents/INC-0090-type-stripping-rejected-typescript-parameter-properties-and.md) - Type-stripping rejected TypeScript parameter properties, and admin selectors were undefined (n=1, low)
- [INC-0357](../../incidents/INC-0357-a-landing-helper-piped-a-guarded-commit-into-a-formatter-so.md) - A landing helper piped a guarded commit into a formatter, so the guard's failure did not stop the cleanup (n=1, low)
- [INC-0362](../../incidents/INC-0362-a-landing-loop-written-for-one-shell-s-arrays-ran-under-anot.md) - A landing loop written for one shell's arrays ran under another and committed one of two files (n=1, low)
- [INC-0369](../../incidents/INC-0369-a-bare-syntax-check-resolved-to-a-different-runtime-that-ign.md) - A bare syntax check resolved to a different runtime that ignored the flag and executed the script (n=1, low)
- [INC-0370](../../incidents/INC-0370-a-scrub-command-was-refused-as-a-broad-home-directory-scan-b.md) - A scrub command was refused as a broad home-directory scan by the operating system's privacy layer (n=1, low)
- [INC-0407](../../incidents/INC-0407-a-lead-signature-line-containing-the-assistant-s-product-nam.md) - A lead signature line containing the assistant's product name failed the scrub (n=1, low)
- [INC-0422](../../incidents/INC-0422-a-scoped-compiler-config-flagged-an-import-style-that-the-ca.md) - A scoped compiler config flagged an import style that the canonical build never compiles (n=1, low)
- [INC-0426](../../incidents/INC-0426-a-generated-migration-needed-a-lint-only-edit-so-the-evidenc.md) - A generated migration needed a lint-only edit, so the evidence carries the raw and delivered hashes and the one-line diff (n=1, low)
- [INC-0437](../../incidents/INC-0437-evidence-receipts-leaked-absolute-paths-into-branch-history.md) - Evidence receipts leaked absolute paths into branch history, and the lead landed by squash instead of rewriting history (n=1, low)
- [INC-0439](../../incidents/INC-0439-a-generated-down-migration-dropped-a-table-with-cascade-and.md) - A generated down migration dropped a table with cascade and then dropped the removed constraint again (n=1, low)
- [INC-0446](../../incidents/INC-0446-a-fresh-worktree-can-be-provisioned-by-a-copy-on-write-clone.md) - A fresh worktree can be provisioned by a copy-on-write clone of the dependency tree instead of an install that may hit dead store links (n=1, low)
- [INC-0464](../../incidents/INC-0464-color-escape-codes-in-a-report-broke-an-extraction-assertion.md) - Color escape codes in a report broke an extraction assertion, and only the zero match assertion caught it (n=1, low)
- [INC-0469](../../incidents/INC-0469-a-long-acceptance-run-launched-with-a-detached-command-insid.md) - A long acceptance run launched with a detached command inside a subshell from a tool shell never started, and no output file existed minutes later (n=1, low)
- [INC-0475](../../incidents/INC-0475-a-process-guard-stopped-a-run-twice-the-listing-was-padded-w.md) - A process guard stopped a run twice: the listing was padded with trailing spaces, and the guard's own command line matched its search (n=1, low)
- [INC-0518](../../incidents/INC-0518-a-landing-tool-read-a-bare-file-name-as-a-test-root-name-so.md) - A landing tool read a bare file name as a test-root name, so a file was left out of a landing and the identifier check failed (n=1, low)
- [INC-0519](../../incidents/INC-0519-a-root-was-passed-to-a-landing-helper-by-name-and-by-path-an.md) - A root was passed to a landing helper by name and by path, and the cleanup removed a file twice and stopped (n=1, low)
- [INC-0545](../../incidents/INC-0545-a-landing-helper-guessed-the-kind-of-each-argument-from-its.md) - A landing helper guessed the kind of each argument from its shape, so a plain file name was read as a pending root (n=1, low)
- [INC-0546](../../incidents/INC-0546-a-reviewer-asked-for-a-mutant-to-run-with-a-case-filter-but.md) - A reviewer asked for a mutant to run with a case filter, but the row runner takes one row and no filter (n=1, low)
- [INC-0561](../../incidents/INC-0561-a-verifier-matched-plain-text-in-colored-logs-and-stopped.md) - A verifier matched plain text in colored logs and stopped (n=1, low)
- [INC-0565](../../incidents/INC-0565-a-second-request-for-a-part-row-driver-showed-that-the-row-r.md) - A second request for a part-row driver showed that the row runner needs a case filter (n=1, low)
- [INC-0574](../../incidents/INC-0574-two-mutation-drivers-stopped-before-the-restored-green-becau.md) - Two mutation drivers stopped before the restored green because they matched a log-tail string the harness does not print (n=1, low)
- [INC-0581](../../incidents/INC-0581-a-brief-named-the-revision-id-as-the-row-and-the-row-runner.md) - A brief named the revision id as the row, and the row runner refused before any test ran (n=1, low)
- [INC-0582](../../incidents/INC-0582-a-landing-helper-treated-a-top-level-file-name-with-no-slash.md) - A landing helper treated a top-level file name with no slash as a test root, so it copied nothing for it (n=1, low)
- [INC-0603](../../incidents/INC-0603-a-measurement-wrapper-called-an-agent-cli-inside-a-locked-sh.md) - A measurement wrapper called an agent CLI inside a locked shell and failed before any child ran, and the one-invocation bound was kept by voiding the attempt (n=1, low)
- [INC-0604](../../incidents/INC-0604-a-row-runner-selected-by-family-while-the-brief-named-a-revi.md) - A row runner selected by family while the brief named a revision, so the run stopped before the harness (n=1, low)
- [INC-0607](../../incidents/INC-0607-a-sandboxed-shell-refused-a-directory-change-whose-target-wa.md) - A sandboxed shell refused a directory change whose target was held in a variable (n=1, low)
- [INC-0622](../../incidents/INC-0622-an-unbraced-shell-variable-followed-by-a-colon-and-a-letter.md) - An unbraced shell variable followed by a colon and a letter was read as a history modifier, so a revision was mangled and the hash printed was of empty input (n=1, low)
- [INC-0636](../../incidents/INC-0636-a-shell-loop-meant-to-send-four-messages-sent-none-because-t.md) - A shell loop meant to send four messages sent none, because the shell does not split an unquoted variable into words (n=1, low)

## Also tagged tooling-paths

30 incidents filed under another home class also carry this class. Listed by the node where they live:

- [false-green](../false-green/README.md): INC-0056, INC-0058, INC-0070, INC-0163, INC-0196, INC-0200, INC-0203, INC-0205, INC-0280, INC-0322, INC-0344, INC-0356
- [spec-and-scope](../spec-and-scope/README.md): INC-0189, INC-0267, INC-0332
- [test-isolation](../test-isolation/README.md): INC-0286, INC-0340, INC-0351
- [vcs-destruction](../vcs-destruction/README.md): INC-0114, INC-0162, INC-0309
- [concurrency](../concurrency/README.md): INC-0117, INC-0368
- [detector-fail-closed](../detector-fail-closed/README.md): INC-0238, INC-0327
- [detector-fail-open](../detector-fail-open/README.md): INC-0029, INC-0037
- [delegation](../delegation/README.md): INC-0179
- [observability](../observability/README.md): INC-0073
- [stale-module](../stale-module/README.md): INC-0123

## Practices touching this class

- [PRA-0004](../CORE.md#practices) - Choose the constraint surface before choosing the enforcement strength
