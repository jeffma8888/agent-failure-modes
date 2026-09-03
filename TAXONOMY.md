# Taxonomy

Failure classes observed in production autonomous-agent loops. A single incident often
belongs to several: the interesting failures sit where two classes meet.

## reward-hacking

The loop optimizes the letter of its reward instead of the goal - Goodhart's law in production. It games its own success signal (ships busywork, self-reports success, satisfies a metric that no longer measures value).

**Ask:** Is the reward a proxy the agent can satisfy without doing the real work? What does the loop gain points for that a human would not call progress?

**Incidents (1):** [INC-0001](incidents/INC-0001-reward-hacking-twelve-near-identical-features-shipped-as-dif.md)

## false-green

A quality gate reports success while the work is not actually good: vacuous tests, tautological assertions, skipped cases, or a grader that cannot fail.

**Ask:** Could this gate be green on broken code? What is the smallest wrong change that still passes it?

**Incidents (9):** [INC-0001](incidents/INC-0001-reward-hacking-twelve-near-identical-features-shipped-as-dif.md) [INC-0026](incidents/INC-0026-a-whole-batch-verification-veto-turns-one-bad-item-into-a-pe.md) [INC-0027](incidents/INC-0027-a-cache-keyed-on-a-recycled-id-judged-each-record-on-its-pre.md) [INC-0028](incidents/INC-0028-when-two-distributions-overlap-there-is-no-threshold-change.md) [INC-0031](incidents/INC-0031-a-concurrency-test-with-no-forced-interleaving-passes-loudes.md) [INC-0035](incidents/INC-0035-two-individually-safe-options-are-unsafe-together-when-their.md) [INC-0039](incidents/INC-0039-a-budget-is-not-a-sample-a-sorted-head-is-a-permanent-filter.md) [INC-0040](incidents/INC-0040-a-guard-that-asserts-a-lifecycle-stage-fails-at-exactly-the.md) [INC-0042](incidents/INC-0042-self-review-does-not-catch-recurrences-of-your-own-documente.md)

## stage-timeout

A hard per-step wall-clock cap (beneath any outer timeout you set) silently kills work that runs too long. The narration drops and the step looks like it produced nothing.

**Ask:** What is the hardest time cap actually enforced on one step, and how close is the real work to it?

**Incidents (7):** [INC-0002](incidents/INC-0002-the-hard-per-step-wall-clock-cap-is-the-number-one-cause-of.md) [INC-0003](incidents/INC-0003-a-slow-test-suite-makes-a-product-unbuildable-by-the-loop.md) [INC-0004](incidents/INC-0004-a-monotonically-growing-required-reading-file-silently-kills.md) [INC-0005](incidents/INC-0005-a-killed-step-with-no-verdict-token-is-read-as-reverted.md) [INC-0006](incidents/INC-0006-checkpoint-first-a-killed-step-that-already-wrote-its-output.md) [INC-0007](incidents/INC-0007-diagnose-stalled-work-from-the-duration-distribution-not-the.md) [INC-0025](incidents/INC-0025-retrying-a-killed-verification-step-without-resumable-eviden.md)

## verdict-token

A machine-parsed decision token is missing or malformed, so a downstream parser reads the absence as the pessimistic default and discards good work.

**Ask:** If the step is killed before it writes its decision, what does the parser assume - and is that assumption safe?

**Incidents (3):** [INC-0005](incidents/INC-0005-a-killed-step-with-no-verdict-token-is-read-as-reverted.md) [INC-0025](incidents/INC-0025-retrying-a-killed-verification-step-without-resumable-eviden.md) [INC-0041](incidents/INC-0041-a-verifier-that-lived-and-answered-can-still-deliver-an-unus.md)

## steering-channel

The channel meant to steer the loop (injected instructions, pinned notes) is not actually delivered - it is truncated, mis-parsed, or dropped by the consumer that was supposed to read it.

**Ask:** Did the CONSUMER's own parser emit the steering text verbatim, or did you only confirm you wrote it?

**Incidents (2):** [INC-0004](incidents/INC-0004-a-monotonically-growing-required-reading-file-silently-kills.md) [INC-0020](incidents/INC-0020-a-steering-channel-counts-only-when-the-consumer-s-own-parse.md)

## ipc-and-env

The loop breaks on its runtime environment rather than its logic: a rotated socket, an expired credential, an inherited stale variable, the machine going to sleep.

**Ask:** What environmental state did this process capture at launch that can change underneath it while it runs?

**Incidents (6):** [INC-0008](incidents/INC-0008-stale-ipc-endpoint-after-the-host-application-restarts.md) [INC-0009](incidents/INC-0009-interactive-only-credential-expiry-silently-stalls-unattende.md) [INC-0010](incidents/INC-0010-sleep-beats-the-wake-lock-on-battery-power.md) [INC-0011](incidents/INC-0011-concurrent-agent-brains-silently-starve-and-kill-each-other.md) [INC-0017](incidents/INC-0017-a-killed-detached-loop-resurrects-with-a-new-ppid.md) [INC-0036](incidents/INC-0036-a-relaunch-that-bypasses-the-canonical-launcher-runs-healthy.md)

## concurrency

Independent agents or sessions contend for one shared resource - a rate-limited API quota, a git index, a working tree - and degrade or corrupt each other, often silently.

**Ask:** How many live agents share this one resource right now, and what happens to the one you are waiting on when a second appears?

**Incidents (6):** [INC-0011](incidents/INC-0011-concurrent-agent-brains-silently-starve-and-kill-each-other.md) [INC-0012](incidents/INC-0012-a-loop-s-git-add-a-sweeps-a-human-s-uncommitted-edits-into-a.md) [INC-0013](incidents/INC-0013-add-then-commit-is-a-shared-index-race-use-a-path-limited-co.md) [INC-0030](incidents/INC-0030-rewriting-a-region-by-slicing-between-two-markers-deletes-wh.md) [INC-0038](incidents/INC-0038-a-determinism-test-that-scans-the-live-working-tree-cannot-p.md) [INC-0043](incidents/INC-0043-an-anchored-replace-that-matches-a-prefix-of-a-line-is-still.md)

## vcs-destruction

Version control is used as a weapon against the working tree: a blanket stage sweeps in unrelated edits, a revert-to-remote discards uncommitted work, or identity leaks into history.

**Ask:** Whose uncommitted work is in this tree, and what does a failure-path reset or a blanket 'add all' do to it?

**Incidents (6):** [INC-0012](incidents/INC-0012-a-loop-s-git-add-a-sweeps-a-human-s-uncommitted-edits-into-a.md) [INC-0013](incidents/INC-0013-add-then-commit-is-a-shared-index-race-use-a-path-limited-co.md) [INC-0014](incidents/INC-0014-a-revert-on-failure-loop-destroys-uncommitted-human-work-in.md) [INC-0015](incidents/INC-0015-git-identity-leak-real-name-via-ambient-global-config.md) [INC-0024](incidents/INC-0024-backtick-command-substitution-in-a-heredoc-corrupts-and-exec.md) [INC-0030](incidents/INC-0030-rewriting-a-region-by-slicing-between-two-markers-deletes-wh.md)

## delegation

A sub-agent re-delegates instead of doing the work: it spawns another loop, scaffolds a plan for a future iteration, and exits successfully having produced nothing.

**Ask:** Does the instruction forbid EVERY escape hatch - nested agents, scaffolding a loop, handing off to a later iteration - by name?

**Incidents (4):** [INC-0016](incidents/INC-0016-anti-delegation-clause-must-forbid-scaffold-a-loop-too.md) [INC-0017](incidents/INC-0017-a-killed-detached-loop-resurrects-with-a-new-ppid.md) [INC-0041](incidents/INC-0041-a-verifier-that-lived-and-answered-can-still-deliver-an-unus.md) [INC-0042](incidents/INC-0042-self-review-does-not-catch-recurrences-of-your-own-documente.md)

## detector-fail-open

A monitor or safety check silently never fires: a wrong regex flavor, the wrong parsed field, a case mismatch. A negative result is mistaken for health.

**Ask:** Have you fed this detector a known-bad sample and watched it fire, AND a known-good sample and watched it stay silent?

**Incidents (7):** [INC-0009](incidents/INC-0009-interactive-only-credential-expiry-silently-stalls-unattende.md) [INC-0018](incidents/INC-0018-fail-open-detector-pipe-alternation-matches-nothing-under-on.md) [INC-0019](incidents/INC-0019-fail-open-detector-parsing-the-wrong-column-reports-healthy.md) [INC-0028](incidents/INC-0028-when-two-distributions-overlap-there-is-no-threshold-change.md) [INC-0029](incidents/INC-0029-when-a-check-reports-missing-content-the-extractor-is-the-fi.md) [INC-0037](incidents/INC-0037-a-liveness-check-built-on-a-process-table-grep-counts-itself.md) [INC-0040](incidents/INC-0040-a-guard-that-asserts-a-lifecycle-stage-fails-at-exactly-the.md)

## detector-fail-closed

A monitor or check fires when it should not: it reports a correct artifact as broken, an honest quote as fabricated, a live process as dead. The accusation is specific and plausible, so the natural response is to repair the artifact - which is the destructive direction.

**Ask:** Before acting on this check's accusation, have you verified the ACCUSATION against the primary source - and could the check's own normalisation, base path or parser be the thing that disagrees?

**Incidents (4):** [INC-0029](incidents/INC-0029-when-a-check-reports-missing-content-the-extractor-is-the-fi.md) [INC-0032](incidents/INC-0032-removing-a-veto-exposes-the-broken-classifier-it-was-masking.md) [INC-0033](incidents/INC-0033-one-normaliser-is-not-enough-if-it-maps-the-two-sides-into-d.md) [INC-0034](incidents/INC-0034-a-malformed-item-aborts-the-per-item-pass-and-the-crash-rein.md)

## stale-module

A long-running process runs the code it imported at launch. Later commits to that module are inert while git and the changelog report them shipped.

**Ask:** When did this process start, and how many commits to the code it imported have landed since - with no reload or restart?

**Incidents (1):** [INC-0021](incidents/INC-0021-stale-module-import-shipped-is-not-live.md)

## checkpoint

An all-or-nothing step loses everything when it is interrupted, because it writes its output only at the end instead of writing a minimal-but-complete artifact first and refining in place.

**Ask:** If this step is killed at minute 8 of 10, does a usable artifact already exist on disk?

**Incidents (4):** [INC-0002](incidents/INC-0002-the-hard-per-step-wall-clock-cap-is-the-number-one-cause-of.md) [INC-0006](incidents/INC-0006-checkpoint-first-a-killed-step-that-already-wrote-its-output.md) [INC-0025](incidents/INC-0025-retrying-a-killed-verification-step-without-resumable-eviden.md) [INC-0034](incidents/INC-0034-a-malformed-item-aborts-the-per-item-pass-and-the-crash-rein.md)

## tooling-paths

The shell or tool layer betrays you: command substitution runs inside a string you meant as data, a built-in resolves paths from an unexpected root, an interpreter shim mutates the wrong environment.

**Ask:** Will any character in this string be interpreted rather than stored, and from what directory does this tool actually resolve paths?

**Incidents (5):** [INC-0024](incidents/INC-0024-backtick-command-substitution-in-a-heredoc-corrupts-and-exec.md) [INC-0029](incidents/INC-0029-when-a-check-reports-missing-content-the-extractor-is-the-fi.md) [INC-0030](incidents/INC-0030-rewriting-a-region-by-slicing-between-two-markers-deletes-wh.md) [INC-0037](incidents/INC-0037-a-liveness-check-built-on-a-process-table-grep-counts-itself.md) [INC-0043](incidents/INC-0043-an-anchored-replace-that-matches-a-prefix-of-a-line-is-still.md)

## test-isolation

A test passes only in the environment where it was written: it depends on untracked local state, ambient file counts, a directory name, or git history a clean checkout does not have.

**Ask:** Would this test pass in a throwaway fresh clone on a different machine? What ambient state is it silently reading?

**Incidents (6):** [INC-0003](incidents/INC-0003-a-slow-test-suite-makes-a-product-unbuildable-by-the-loop.md) [INC-0022](incidents/INC-0022-test-precondition-on-gitignored-local-state-passes-only-on-t.md) [INC-0023](incidents/INC-0023-ci-shallow-clone-breaks-tests-that-read-git-history.md) [INC-0031](incidents/INC-0031-a-concurrency-test-with-no-forced-interleaving-passes-loudes.md) [INC-0038](incidents/INC-0038-a-determinism-test-that-scans-the-live-working-tree-cannot-p.md) [INC-0040](incidents/INC-0040-a-guard-that-asserts-a-lifecycle-stage-fails-at-exactly-the.md)

## observability

The signal you trust hides the truth: an outcome flag masks a chronically over-budget step, a lifetime average hides a spike, a hardened process reports zero usage.

**Ask:** Are you reading a distribution or a single number, a delta or a lifetime average - and could the measurement itself be denied?

**Incidents (16):** [INC-0002](incidents/INC-0002-the-hard-per-step-wall-clock-cap-is-the-number-one-cause-of.md) [INC-0007](incidents/INC-0007-diagnose-stalled-work-from-the-duration-distribution-not-the.md) [INC-0019](incidents/INC-0019-fail-open-detector-parsing-the-wrong-column-reports-healthy.md) [INC-0021](incidents/INC-0021-stale-module-import-shipped-is-not-live.md) [INC-0026](incidents/INC-0026-a-whole-batch-verification-veto-turns-one-bad-item-into-a-pe.md) [INC-0027](incidents/INC-0027-a-cache-keyed-on-a-recycled-id-judged-each-record-on-its-pre.md) [INC-0028](incidents/INC-0028-when-two-distributions-overlap-there-is-no-threshold-change.md) [INC-0029](incidents/INC-0029-when-a-check-reports-missing-content-the-extractor-is-the-fi.md) [INC-0031](incidents/INC-0031-a-concurrency-test-with-no-forced-interleaving-passes-loudes.md) [INC-0032](incidents/INC-0032-removing-a-veto-exposes-the-broken-classifier-it-was-masking.md) [INC-0033](incidents/INC-0033-one-normaliser-is-not-enough-if-it-maps-the-two-sides-into-d.md) [INC-0036](incidents/INC-0036-a-relaunch-that-bypasses-the-canonical-launcher-runs-healthy.md) [INC-0037](incidents/INC-0037-a-liveness-check-built-on-a-process-table-grep-counts-itself.md) [INC-0039](incidents/INC-0039-a-budget-is-not-a-sample-a-sorted-head-is-a-permanent-filter.md) [INC-0041](incidents/INC-0041-a-verifier-that-lived-and-answered-can-still-deliver-an-unus.md) [INC-0042](incidents/INC-0042-self-review-does-not-catch-recurrences-of-your-own-documente.md)

## spec-and-scope

The loop does the wrong amount of work: it pursues the whole visible mission instead of its assigned slice, or picks tasks by lowest effort instead of highest value, or grows an artifact without bound.

**Ask:** Does the agent's visible context imply a bigger goal than its assigned task, and is any required-reading artifact growing every iteration?

**Incidents (6):** [INC-0001](incidents/INC-0001-reward-hacking-twelve-near-identical-features-shipped-as-dif.md) [INC-0003](incidents/INC-0003-a-slow-test-suite-makes-a-product-unbuildable-by-the-loop.md) [INC-0004](incidents/INC-0004-a-monotonically-growing-required-reading-file-silently-kills.md) [INC-0026](incidents/INC-0026-a-whole-batch-verification-veto-turns-one-bad-item-into-a-pe.md) [INC-0035](incidents/INC-0035-two-individually-safe-options-are-unsafe-together-when-their.md) [INC-0039](incidents/INC-0039-a-budget-is-not-a-sample-a-sorted-head-is-a-permanent-filter.md)

## identity-and-keying

Two distinct things share one identifier or cache key, so state computed for one is served for the other: a slot number a rejection recycles, a cache keyed on a mutable name, a record cited by its position in a re-sorted list.

**Ask:** Is this key unique across everything it will ever be asked about, or only across the subset that succeeded?

**Incidents (2):** [INC-0027](incidents/INC-0027-a-cache-keyed-on-a-recycled-id-judged-each-record-on-its-pre.md) [INC-0043](incidents/INC-0043-an-anchored-replace-that-matches-a-prefix-of-a-line-is-still.md)
