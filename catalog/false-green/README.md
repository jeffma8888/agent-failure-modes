# false-green

[Catalog](../README.md) / false-green

A quality gate reports success while the work is not actually good: vacuous tests, tautological assertions, skipped cases, or a grader that cannot fail.

**Ask:** Could this gate be green on broken code? What is the smallest wrong change that still passes it?

124 incidents filed here (124 occurrences); 60 more filed elsewhere are also tagged false-green.

## Incidents

This class has no topics, so this node is the leaf. Ordered by occurrences, then severity, then id.

The 124 entries below are listed by title only so this node stays under 12 KB. Open the page, or run `python3 tools/afm.py show INC-XXXX`, for its signature and rule.

- [INC-0031](../../incidents/INC-0031-a-concurrency-test-with-no-forced-interleaving-passes-loudes.md) - A concurrency test with no forced interleaving passes loudest when the feature is absent (n=1, high)
- [INC-0035](../../incidents/INC-0035-two-individually-safe-options-are-unsafe-together-when-their.md) - Two individually safe options are unsafe together when their combination leaves a consumer unable to distinguish two states (n=1, high)
- [INC-0042](../../incidents/INC-0042-self-review-does-not-catch-recurrences-of-your-own-documente.md) - Self-review does not catch recurrences of your own documented rules (n=1, high)
- [INC-0250](../../incidents/INC-0250-bare-angle-bracket-slots-turned-a-markdown-note-into-raw-tex.md) - Bare angle-bracket slots turned a Markdown note into raw text after structural checks passed (n=1, high)
- [INC-0601](../../incidents/INC-0601-a-nested-driver-deleted-node-options-so-a-preload-capture-ne.md) - A nested driver deleted NODE_OPTIONS, so a preload capture never reached the nested harness and a zero counted from copied receipts was not zero (n=1, high)
- [INC-0028](../../incidents/INC-0028-when-two-distributions-overlap-there-is-no-threshold-change.md) - When two distributions overlap there is no threshold - change the signal, not the number (n=1, medium)
- [INC-0040](../../incidents/INC-0040-a-guard-that-asserts-a-lifecycle-stage-fails-at-exactly-the.md) - A guard that asserts a lifecycle stage fails at exactly the moment it was written to protect (n=1, medium)
- [INC-0056](../../incidents/INC-0056-test-seams-declared-from-memory-carried-wrong-field-names-an.md) - Test seams declared from memory carried wrong field names, and a bulk replacement silently missed a row (n=1, medium)
- [INC-0057](../../incidents/INC-0057-a-revision-that-closed-every-finding-introduced-new-defects.md) - A revision that closed every finding introduced new defects in the seams it added (n=1, medium)
- [INC-0061](../../incidents/INC-0061-exhaustive-test-wording-created-expectations-the-design-neve.md) - Exhaustive test wording created expectations the design never defined (n=1, medium)
- [INC-0062](../../incidents/INC-0062-a-reviewer-s-claim-about-framework-behaviour-was-wrong-and-a.md) - A reviewer's claim about framework behaviour was wrong, and accepting it would have put a wrong assertion into the tests (n=1, medium)
- [INC-0082](../../incidents/INC-0082-an-absence-check-passed-vacuously-because-the-forbidden-text.md) - An absence check passed vacuously because the forbidden text never matched the real title and the document may never have been read (n=1, medium)
- [INC-0083](../../incidents/INC-0083-controls-that-fail-in-only-one-direction-a-drop-guard-keyed.md) - Controls that fail in only one direction, a drop guard keyed on a name pattern, and refusal tests satisfied by unrelated connection errors (n=1, medium)
- [INC-0095](../../incidents/INC-0095-port-validation-tests-lacked-separate-absent-zero-and-shared.md) - Port validation tests lacked separate absent, zero and shared-port negatives and a positive callback control (n=1, medium)
- [INC-0104](../../incidents/INC-0104-a-process-group-kill-test-used-single-process-stubs-so-signa.md) - A process-group kill test used single-process stubs, so signalling the leader and the group looked the same (n=1, medium)
- [INC-0112](../../incidents/INC-0112-a-control-relied-on-state-the-test-had-changed-earlier-and-s.md) - A control relied on state the test had changed earlier and silently became vacuous (n=1, medium)
- [INC-0116](../../incidents/INC-0116-two-validators-enforcing-the-same-rule-masked-single-file-mu.md) - Two validators enforcing the same rule masked single-file mutations (n=1, medium)
- [INC-0120](../../incidents/INC-0120-a-guard-control-asserted-only-exit-0-so-a-warn-and-pass-guar.md) - A guard control asserted only exit 0, so a warn-and-pass guard looked like a clean pass (n=1, medium)
- [INC-0133](../../incidents/INC-0133-a-local-guard-behind-a-shared-environment-pin-was-masked-and.md) - A local guard behind a shared environment pin was masked, and a mutation claim was reasoned instead of measured (n=1, medium)
- [INC-0153](../../incidents/INC-0153-a-test-checked-only-the-dispatch-argv-of-a-child-stage-not-i.md) - A test checked only the dispatch argv of a child stage, not its semantics (n=1, medium)
- [INC-0155](../../incidents/INC-0155-a-kill-rehearsal-met-its-timeout-but-nobody-checked-what-the.md) - A kill rehearsal met its timeout but nobody checked what the killed process left behind (n=1, medium)
- [INC-0163](../../incidents/INC-0163-acceptance-ran-bare-vitest-while-the-real-gate-ran-setup-the.md) - Acceptance ran bare vitest while the real gate ran setup then the FAST runner (n=1, medium)
- [INC-0168](../../incidents/INC-0168-disjoint-project-discovery-did-not-stop-a-suite-from-running.md) - Disjoint project discovery did not stop a suite from running twice (n=1, medium)
- [INC-0174](../../incidents/INC-0174-a-count-change-was-reconciled-by-totals-and-a-route-switch-l.md) - A count change was reconciled by totals and a route switch leaked into the default path (n=1, medium)
- [INC-0190](../../incidents/INC-0190-fast-stayed-green-while-a-command-adapter-fixture-missed-a-n.md) - FAST stayed green while a command-adapter fixture missed a new execution project (n=1, medium)
- [INC-0192](../../incidents/INC-0192-a-rehearsal-mixed-automatic-guards-with-procedural-stops.md) - A rehearsal mixed automatic guards with procedural stops (n=1, medium)
- [INC-0193](../../incidents/INC-0193-a-negative-grep-was-taken-as-proof-that-a-removal-ruling-was.md) - A negative grep was taken as proof that a removal ruling was complete (n=1, medium)
- [INC-0196](../../incidents/INC-0196-an-allowlist-fix-turned-gate-tests-green-while-the-runner-sk.md) - An allowlist fix turned gate tests green while the runner skipped the new project (n=1, medium)
- [INC-0200](../../incidents/INC-0200-a-sandbox-permission-failure-was-at-risk-of-reading-as-a-cod.md) - A sandbox permission failure was at risk of reading as a code defect (n=1, medium)
- [INC-0202](../../incidents/INC-0202-one-adapter-rejection-looked-like-ten-separate-defects.md) - One adapter rejection looked like ten separate defects (n=1, medium)
- [INC-0203](../../incidents/INC-0203-a-setup-failure-was-at-risk-of-counting-as-a-test-run.md) - A setup failure was at risk of counting as a test run (n=1, medium)
- [INC-0205](../../incidents/INC-0205-a-runtime-value-was-at-risk-of-being-invented-to-quiet-the-c.md) - A runtime value was at risk of being invented to quiet the compiler (n=1, medium)
- [INC-0208](../../incidents/INC-0208-two-rows-were-green-alone-and-red-together.md) - Two rows were green alone and red together (n=1, medium)
- [INC-0213](../../incidents/INC-0213-a-network-denied-dependency-audit-was-neither-a-finding-nor.md) - A network-denied dependency audit was neither a finding nor a pass (n=1, medium)
- [INC-0214](../../incidents/INC-0214-a-helper-was-fixed-and-a-caller-still-passed-a-literal-empty.md) - A helper was fixed and a caller still passed a literal empty object (n=1, medium)
- [INC-0221](../../incidents/INC-0221-a-performance-refactor-was-checked-only-on-the-real-tree.md) - A performance refactor was checked only on the real tree (n=1, medium)
- [INC-0222](../../incidents/INC-0222-a-clean-tree-positive-did-not-exercise-the-working-file-cont.md) - A clean-tree positive did not exercise the working-file context (n=1, medium)
- [INC-0228](../../incidents/INC-0228-a-digest-manifest-without-digests-was-cited-as-evidence.md) - A digest manifest without digests was cited as evidence (n=1, medium)
- [INC-0232](../../incidents/INC-0232-a-prompt-render-succeeded-without-reading-the-card-bodies.md) - A prompt render succeeded without reading the card bodies (n=1, medium)
- [INC-0233](../../incidents/INC-0233-approval-of-role-cards-in-prose-was-at-risk-of-standing-in-f.md) - Approval of role cards in prose was at risk of standing in for a runtime check (n=1, medium)
- [INC-0234](../../incidents/INC-0234-a-ledger-review-that-started-from-the-author-list-could-inhe.md) - A ledger review that started from the author list could inherit its gaps (n=1, medium)
- [INC-0236](../../incidents/INC-0236-a-blocked-result-came-from-a-deadline-before-the-plant-ran.md) - A BLOCKED result came from a deadline before the plant ran (n=1, medium)
- [INC-0239](../../incidents/INC-0239-a-hold-outcome-had-no-proof-that-nothing-changed.md) - A hold outcome had no proof that nothing changed (n=1, medium)
- [INC-0241](../../incidents/INC-0241-automated-tests-passed-while-nobody-had-walked-the-real-site.md) - Automated tests passed while nobody had walked the real site (n=1, medium)
- [INC-0244](../../incidents/INC-0244-a-correct-not-found-page-was-served-with-a-200-status.md) - A correct not-found page was served with a 200 status (n=1, medium)
- [INC-0246](../../incidents/INC-0246-a-short-password-check-created-the-one-time-account-instead.md) - A short password check created the one-time account instead of showing an error (n=1, medium)
- [INC-0247](../../incidents/INC-0247-ancestry-was-at-risk-of-standing-in-for-a-clean-tree-or-a-ch.md) - Ancestry was at risk of standing in for a clean tree or a checker run (n=1, medium)
- [INC-0252](../../incidents/INC-0252-a-word-grep-reported-a-failure-in-a-passing-log.md) - A word grep reported a failure in a passing log (n=1, medium)
- [INC-0253](../../incidents/INC-0253-two-of-four-selected-projects-executed-no-case.md) - Two of four selected projects executed no case (n=1, medium)
- [INC-0259](../../incidents/INC-0259-sum-every-runner-the-earlier-record-summed.md) - Sum every runner the earlier record summed (n=1, medium)
- [INC-0265](../../incidents/INC-0265-a-rendered-not-found-view-is-not-proof-of-a-404-status.md) - A rendered not-found view is not proof of a 404 status (n=1, medium)
- [INC-0266](../../incidents/INC-0266-a-planned-round-with-stop-in-place-proves-nothing.md) - A planned round with STOP in place proves nothing (n=1, medium)
- [INC-0272](../../incidents/INC-0272-not-found-under-a-streaming-root-layout-answers-200-whatever.md) - Not-found under a streaming root layout answers 200 whatever the call site (n=1, medium)
- [INC-0273](../../incidents/INC-0273-a-status-check-must-take-every-client-reading.md) - A status check must take every client reading (n=1, medium)
- [INC-0275](../../incidents/INC-0275-a-probe-that-sends-a-session-cookie-alone-may-test-guest-beh.md) - A probe that sends a session cookie alone may test guest behavior (n=1, medium)
- [INC-0280](../../incidents/INC-0280-never-chain-a-write-after-a-diagnostic.md) - Never chain a write after a diagnostic (n=1, medium)
- [INC-0282](../../incidents/INC-0282-a-test-that-claims-a-role-must-prove-the-role-before-relying.md) - A test that claims a role must prove the role before relying on it (n=1, medium)
- [INC-0283](../../incidents/INC-0283-a-hold-gate-is-proven-only-while-eligible-work-exists.md) - A hold gate is proven only while eligible work exists (n=1, medium)
- [INC-0284](../../incidents/INC-0284-a-gate-result-counts-only-at-a-revision-the-gate-can-fetch-a.md) - A gate result counts only at a revision the gate can fetch and that holds its fix (n=1, medium)
- [INC-0287](../../incidents/INC-0287-an-oracle-that-matches-a-substring-or-a-loose-boundary-can-b.md) - An oracle that matches a substring or a loose boundary can be satisfied by a decoy (n=1, medium)
- [INC-0290](../../incidents/INC-0290-a-setup-hook-was-sized-from-file-time-or-from-a-refused-atte.md) - A setup hook was sized from file time, or from a refused attempt (n=1, medium)
- [INC-0291](../../incidents/INC-0291-a-known-unrelated-load-timeout-blocked-a-row-until-one-combi.md) - A known unrelated load timeout blocked a row until one combined run accepted both (n=1, medium)
- [INC-0295](../../incidents/INC-0295-a-pure-move-onto-an-existing-path-was-read-from-the-diff-s-r.md) - A pure move onto an existing path was read from the diff's rename display (n=1, medium)
- [INC-0310](../../incidents/INC-0310-a-coverage-ledger-keyed-on-report-names-missed-a-scoped-run.md) - A coverage ledger keyed on report names missed a scoped run of the exact bytes (n=1, medium)
- [INC-0314](../../incidents/INC-0314-a-probe-based-test-never-ran-its-probe-so-its-red-proved-not.md) - A probe-based test never ran its probe, so its red proved nothing about the probe (n=1, medium)
- [INC-0315](../../incidents/INC-0315-a-static-checker-s-pass-was-read-as-acceptance-without-an-an.md) - A static checker's PASS was read as acceptance without an anchored baseline (n=1, medium)
- [INC-0318](../../incidents/INC-0318-a-path-guard-probed-only-with-nonexistent-paths-could-never.md) - A path guard probed only with nonexistent paths could never fail (n=1, medium)
- [INC-0321](../../incidents/INC-0321-a-green-parallel-run-was-cited-although-the-parallel-group-h.md) - A green parallel run was cited although the parallel group held no files (n=1, medium)
- [INC-0322](../../incidents/INC-0322-a-search-helper-ended-a-gather-loop-at-the-first-file-withou.md) - A search helper ended a gather loop at the first file without a match (n=1, medium)
- [INC-0323](../../incidents/INC-0323-a-red-run-that-also-renamed-its-checks-counted-name-drift-as.md) - A red run that also renamed its checks counted name drift as defects (n=1, medium)
- [INC-0329](../../incidents/INC-0329-a-pool-saturation-probe-waited-on-a-connection-its-own-adapt.md) - A pool saturation probe waited on a connection its own adapter retained (n=1, medium)
- [INC-0336](../../incidents/INC-0336-a-tier-exclusion-was-added-only-after-a-witness-failed-witho.md) - A tier exclusion was added only after a witness failed without it (n=1, medium)
- [INC-0339](../../incidents/INC-0339-a-mutant-of-a-shared-helper-proved-sensitivity-but-not-the-r.md) - A mutant of a shared helper proved sensitivity but not the real resource's end state (n=1, medium)
- [INC-0343](../../incidents/INC-0343-a-weakened-final-check-survived-a-contract-suite-that-lacked.md) - A weakened final check survived a contract suite that lacked the right-signal, wrong-detail case (n=1, medium)
- [INC-0344](../../incidents/INC-0344-focused-runs-after-a-refactor-hid-static-check-residue-until.md) - Focused runs after a refactor hid static-check residue until the first canonical run (n=1, medium)
- [INC-0347](../../incidents/INC-0347-a-final-print-in-a-wrapper-replaced-the-command-s-failure-wi.md) - A final print in a wrapper replaced the command's failure with success (n=1, medium)
- [INC-0356](../../incidents/INC-0356-a-reviewed-recipe-never-ran-its-real-tool-queries-because-ev.md) - A reviewed recipe never ran its real tool queries because every control stubbed them (n=1, medium)
- [INC-0388](../../incidents/INC-0388-a-baseline-comparison-graded-only-rows-present-in-the-baseli.md) - A baseline comparison graded only rows present in the baseline, so a new failing row passed (n=1, medium)
- [INC-0396](../../incidents/INC-0396-a-multi-step-command-reported-success-for-its-later-steps-wh.md) - A multi-step command reported success for its later steps while its middle step had not happened (n=1, medium)
- [INC-0482](../../incidents/INC-0482-tests-added-by-a-branch-were-never-run-before-the-merge-and.md) - Tests added by a branch were never run before the merge, and the full suite failed on them afterwards (n=1, medium)
- [INC-0490](../../incidents/INC-0490-a-wrapper-exited-zero-while-a-step-record-said-the-step-fail.md) - A wrapper exited zero while a step record said the step failed (n=1, medium)
- [INC-0496](../../incidents/INC-0496-an-acceptance-record-was-ready-for-signature-with-every-test.md) - An acceptance record was ready for signature with every test tier green while the main page of the row was blank (n=1, medium)
- [INC-0497](../../incidents/INC-0497-a-flag-that-hides-the-token-from-responses-left-first-user-r.md) - A flag that hides the token from responses left first-user registration with an empty session cookie (n=1, medium)
- [INC-0498](../../incidents/INC-0498-the-first-browser-run-of-new-end-to-end-cases-found-two-prod.md) - The first browser run of new end-to-end cases found two product defects that config reads and other tiers missed (n=1, medium)
- [INC-0505](../../incidents/INC-0505-a-run-command-silently-dropped-a-named-option-and-three-test.md) - A run command silently dropped a named option, and three tests that ran it asserted only things that are true for the full data set too (n=1, medium)
- [INC-0523](../../incidents/INC-0523-three-test-roots-by-three-authors-used-the-same-guessed-loca.md) - Three test roots by three authors used the same guessed locator for a generated field that the installed library does not render (n=1, medium)
- [INC-0527](../../incidents/INC-0527-an-absence-check-for-a-hidden-field-matched-the-hidden-input.md) - An absence check for a hidden field matched the hidden input the library renders, so a regression root was red on unchanged code (n=1, medium)
- [INC-0533](../../incidents/INC-0533-a-named-mutant-was-masked-by-an-independent-guard-upstream-s.md) - A named mutant was masked by an independent guard upstream, so the case could never turn red for the stated reason (n=1, medium)
- [INC-0534](../../incidents/INC-0534-a-configuration-mutation-failed-a-setup-assertion-before-any.md) - A configuration mutation failed a setup assertion before any case oracle ran, so the red proved nothing about the cases (n=1, medium)
- [INC-0620](../../incidents/INC-0620-a-publish-gate-chain-ran-a-build-script-at-a-path-that-does.md) - A publish gate chain ran a build script at a path that does not exist, printed the failing exit status and carried on to the export and the leak scan (n=1, medium)
- [INC-0623](../../incidents/INC-0623-a-helper-piped-to-tail-and-followed-by-ran-the-next-step-alt.md) - A helper piped to tail and followed by && ran the next step although the helper failed, because a pipeline's status is its last command's (n=1, medium)
- [INC-0625](../../incidents/INC-0625-a-walk-script-ran-a-signed-write-whose-precondition-was-abse.md) - A walk script ran a signed write whose precondition was absent because the step before it had been refused, and the write succeeded on a record that never met the condition (n=1, medium)
- [INC-0628](../../incidents/INC-0628-a-walk-s-no-write-audit-counted-every-non-get-request-as-a-w.md) - A walk's no-write audit counted every non-GET request as a write, and the capture held no request headers or bodies, so override reads stopped the walk (n=1, medium)
- [INC-0058](../../incidents/INC-0058-a-broad-exception-handler-hid-the-difference-between-not-fou.md) - A broad exception handler hid the difference between 'not found' and 'unknown name' (n=1, low)
- [INC-0070](../../incidents/INC-0070-two-reviewers-table-parsers-undercounted-rows-on-escaped-pip.md) - Two reviewers' table parsers undercounted rows on escaped pipes and a sum included a header (n=1, low)
- [INC-0363](../../incidents/INC-0363-a-module-presence-guard-went-through-the-test-s-own-file-sys.md) - A module-presence guard went through the test's own file-system mock, so a missing-API label was never proven (n=1, low)
- [INC-0382](../../incidents/INC-0382-a-click-around-walk-that-always-exits-1-from-a-known-gap-can.md) - A click-around walk that always exits 1 from a known gap cannot gate regressions (n=1, low)
- [INC-0389](../../incidents/INC-0389-two-plan-checks-ran-at-a-wrong-script-path-and-the-last-line.md) - Two plan checks ran at a wrong script path and the last line of their output looked like a result (n=1, low)
- [INC-0408](../../incidents/INC-0408-an-evidence-gap-a-temporary-config-not-retained-was-closed-b.md) - An evidence gap, a temporary config not retained, was closed by a lead re-run that kept it, not by asking the author to reconstruct it (n=1, low)
- [INC-0412](../../incidents/INC-0412-a-whole-unit-re-run-showed-five-failures-in-unrelated-files.md) - A whole-unit re-run showed five failures in unrelated files because a required environment variable was unset in the shell (n=1, low)
- [INC-0421](../../incidents/INC-0421-a-closure-packet-freeze-test-turned-positive-on-a-control-on.md) - A closure packet freeze test turned positive on a control-only landing and the lead admitted it narrowly (n=1, low)
- [INC-0447](../../incidents/INC-0447-tests-authored-but-never-executed-passed-acceptance-and-the.md) - Tests authored but never executed passed acceptance, and the first run of the heavy tier found a failing case (n=1, low)
- [INC-0455](../../incidents/INC-0455-a-provenance-check-that-the-generator-can-never-satisfy-the.md) - A provenance check that the generator can never satisfy: the zero parent id on every snapshot (n=1, low)
- [INC-0461](../../incidents/INC-0461-a-hook-ran-a-query-on-create-with-an-undefined-id-once-a-reg.md) - A hook ran a query on create with an undefined id once a registry became non empty: a latent defect exposed by data, not code (n=1, low)
- [INC-0474](../../incidents/INC-0474-a-whitespace-check-over-the-branch-range-failed-on-generated.md) - A whitespace check over the branch range failed on generated SQL, while the same check on the working tree alone had passed (n=1, low)
- [INC-0476](../../incidents/INC-0476-unit-mutation-testing-on-a-merged-change-found-two-survivors.md) - Unit mutation testing on a merged change found two survivors while every named test passed (n=1, low)
- [INC-0477](../../incidents/INC-0477-a-browser-test-failed-at-its-first-request-and-after-that-wa.md) - A browser test failed at its first request, and after that was fixed the next run failed at a step that had never run (n=1, low)
- [INC-0480](../../incidents/INC-0480-a-push-gate-that-piped-the-test-run-into-a-trimming-command.md) - A push gate that piped the test run into a trimming command would have pushed even if the tests had failed (n=1, low)
- [INC-0484](../../incidents/INC-0484-a-test-fixture-failed-an-earlier-check-than-the-one-under-te.md) - A test fixture failed an earlier check than the one under test (n=1, low)
- [INC-0485](../../incidents/INC-0485-a-merge-checklist-drafted-early-found-a-test-change-the-merg.md) - A merge checklist drafted early found a test change the merge would have broken (n=1, low)
- [INC-0487](../../incidents/INC-0487-a-setting-that-strips-tokens-from-responses-also-stripped-th.md) - A setting that strips tokens from responses also stripped them from the test helper (n=1, low)
- [INC-0524](../../incidents/INC-0524-a-root-named-a-mutation-its-assertions-could-not-see-because.md) - A root named a mutation its assertions could not see, because the next line returned the same status (n=1, low)
- [INC-0525](../../incidents/INC-0525-a-feedback-check-accepted-any-visible-alert-on-the-page-so-a.md) - A feedback check accepted any visible alert on the page, so a stale alert could satisfy it (n=1, low)
- [INC-0530](../../incidents/INC-0530-an-icon-only-button-had-no-accessible-name-so-a-role-name-lo.md) - An icon-only button had no accessible name, so a role-name locator could never match and the test timed out (n=1, low)
- [INC-0541](../../incidents/INC-0541-a-reviewer-accepted-an-initial-red-that-only-proved-a-new-fu.md) - A reviewer accepted an initial red that only proved a new function was missing, and said so (n=1, low)
- [INC-0542](../../incidents/INC-0542-a-mutation-that-flipped-a-field-level-unique-flag-was-masked.md) - A mutation that flipped a field-level unique flag was masked by a unique index the migration had already created (n=1, low)
- [INC-0560](../../incidents/INC-0560-a-mutant-made-the-product-raise-its-own-domain-error-inside.md) - A mutant made the product raise its own domain error inside the awaited expectation, before the matcher ran, and the agent disclosed that it was not an assertion error (n=1, low)
- [INC-0566](../../incidents/INC-0566-a-run-wrapper-exited-zero-although-one-of-its-steps-exited-o.md) - A run wrapper exited zero although one of its steps exited one (n=1, low)
- [INC-0571](../../incidents/INC-0571-a-pre-action-zero-count-check-in-a-browser-test-showed-the-e.md) - A pre-action zero-count check in a browser test showed the error selector already matched one element before any action (n=1, low)
- [INC-0578](../../incidents/INC-0578-not-visible-was-the-wrong-oracle-for-a-collapsed-sidebar-bec.md) - Not visible was the wrong oracle for a collapsed sidebar, because the closed navigation stays in the page with opacity zero and inert (n=1, low)
- [INC-0588](../../incidents/INC-0588-a-reviewer-s-original-race-script-could-not-run-unmodified-a.md) - A reviewer's original race script could not run unmodified against the revision because the step it interrupted no longer exists, and the reviewer reported it as stale test semantics (n=1, low)
- [INC-0608](../../incidents/INC-0608-a-mutant-was-witnessed-red-only-on-the-first-item-of-a-loop.md) - A mutant was witnessed red only on the first item of a loop, so the second row was not witnessed under the mutant (n=1, low)
- [INC-0634](../../incidents/INC-0634-a-record-naming-a-commit-id-was-written-in-the-same-parallel.md) - A record naming a commit id was written in the same parallel batch as the call that creates the commit, so a plausible id was written instead of the real one (n=1, low)
- [INC-0637](../../incidents/INC-0637-a-ledger-named-a-nonexistent-commit-after-a-short-sha-was-le.md) - A ledger named a nonexistent commit after a short SHA was lengthened by hand (n=1, low)

## Also tagged false-green

60 incidents filed under another home class also carry this class. Listed by the node where they live:

- [spec-and-scope](../spec-and-scope/README.md): INC-0026, INC-0063, INC-0075, INC-0086, INC-0102, INC-0105, INC-0134, INC-0173, INC-0194, INC-0198, INC-0217, INC-0269, INC-0276, INC-0285, INC-0289, INC-0300, INC-0302, INC-0311, INC-0328, INC-0330
- [detector-fail-open](../detector-fail-open/README.md): INC-0069, INC-0078, INC-0113, INC-0118, INC-0129, INC-0141, INC-0142, INC-0148, INC-0151, INC-0224
- [identity-and-keying](../identity-and-keying/README.md): INC-0027, INC-0154, INC-0167, INC-0204, INC-0216, INC-0240
- [test-isolation](../test-isolation/README.md): INC-0084, INC-0172, INC-0183, INC-0303, INC-0320
- [tooling-paths](../tooling-paths/README.md): INC-0051, INC-0156, INC-0170, INC-0260, INC-0364
- [ipc-and-env](../ipc-and-env/README.md): INC-0180, INC-0223, INC-0256
- [observability](../observability/README.md): INC-0039, INC-0146, INC-0231
- [stage-timeout](../stage-timeout/README.md): INC-0139, INC-0209, INC-0271
- [checkpoint](../checkpoint/README.md): INC-0258, INC-0349
- [delegation](../delegation/README.md): INC-0298
- [reward-hacking](../reward-hacking/README.md): INC-0001
- [vcs-destruction](../vcs-destruction/README.md): INC-0632
