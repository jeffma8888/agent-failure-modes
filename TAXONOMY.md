# Taxonomy

Failure classes observed in production autonomous-agent loops. A single incident often
belongs to several: the interesting failures sit where two classes meet.

Each class links to its node in the [catalog](catalog/README.md), which lists its topics and incidents. To find a class from what you observe, start at the catalog root or run `python3 tools/afm.py route "..."`.

## reward-hacking

The loop optimizes the letter of its reward instead of the goal - Goodhart's law in production. It games its own success signal (ships busywork, self-reports success, satisfies a metric that no longer measures value).

**Ask:** Is the reward a proxy the agent can satisfy without doing the real work? What does the loop gain points for that a human would not call progress?

**Incidents:** 2 filed here, 1 more from other classes tagged with it. **Catalog node:** [catalog/reward-hacking/](catalog/reward-hacking/README.md)

## false-green

A quality gate reports success while the work is not actually good: vacuous tests, tautological assertions, skipped cases, or a grader that cannot fail.

**Ask:** Could this gate be green on broken code? What is the smallest wrong change that still passes it?

**Incidents:** 129 filed here, 60 more from other classes tagged with it. **Catalog node:** [catalog/false-green/](catalog/false-green/README.md)

**Topics:** [A negative, absence or presence check passed for an unrelated reason](catalog/false-green/check-satisfied-by-unrelated-cause.md) (12), [A reported count, total or ledger does not match what ran](catalog/false-green/count-or-total-computed-wrong.md) (7), [The gate was green but the cases it vouches for never executed](catalog/false-green/green-but-cases-never-ran.md) (14), [A mutant or red-first witness does not prove what it is named for](catalog/false-green/mutation-witness-proves-less.md) (14), [A test oracle, locator or review claim came from memory, not source](catalog/false-green/oracle-or-claim-written-from-memory.md) (12), [An artifact that looks like evidence was cited but proves no fact](catalog/false-green/proxy-artifact-cited-as-evidence.md) (9), [Tests pass but the real page, status or session is wrong](catalog/false-green/real-page-or-response-wrong-behind-green.md) (12), [A red, blocked or failing result came from setup or environment](catalog/false-green/red-for-the-wrong-reason.md) (13), [A gate verdict came from a wrapper, pipe, chain or last line](catalog/false-green/step-failed-but-gate-passed.md) (13), [A test stays green with the behavior removed or broken](catalog/false-green/test-cannot-see-the-defect.md) (10), [Verified a shortcut, a part or an old revision instead of what ships](catalog/false-green/verified-a-different-target.md) (10)

## stage-timeout

A hard per-step wall-clock cap (beneath any outer timeout you set) silently kills work that runs too long. The narration drops and the step looks like it produced nothing.

**Ask:** What is the hardest time cap actually enforced on one step, and how close is the real work to it?

**Incidents:** 40 filed here, 9 more from other classes tagged with it. **Catalog node:** [catalog/stage-timeout/](catalog/stage-timeout/README.md)

**Topics:** [Stale or overbroad load gates block or mis-admit work](catalog/stage-timeout/stale-or-overbroad-load-admission.md) (8), [Timeout policy ignores purpose, call path or lifecycle](catalog/stage-timeout/timeout-policy-and-lifecycle-boundaries.md) (7), [Timing models or optimizations are not measured](catalog/stage-timeout/timing-models-and-critical-path.md) (8), [Work outgrows hidden caps or loses timeout headroom](catalog/stage-timeout/work-outgrows-enforced-timeouts.md) (14)

## verdict-token

A machine-parsed decision token is missing or malformed, so a downstream parser reads the absence as the pessimistic default and discards good work.

**Ask:** If the step is killed before it writes its decision, what does the parser assume - and is that assumption safe?

**Incidents:** 3 filed here, 2 more from other classes tagged with it. **Catalog node:** [catalog/verdict-token/](catalog/verdict-token/README.md)

## steering-channel

The channel meant to steer the loop (injected instructions, pinned notes) is not actually delivered - it is truncated, mis-parsed, or dropped by the consumer that was supposed to read it.

**Ask:** Did the CONSUMER's own parser emit the steering text verbatim, or did you only confirm you wrote it?

**Incidents:** 4 filed here, 1 more from other classes tagged with it. **Catalog node:** [catalog/steering-channel/](catalog/steering-channel/README.md)

## ipc-and-env

The loop breaks on its runtime environment rather than its logic: a rotated socket, an expired credential, an inherited stale variable, the machine going to sleep.

**Ask:** What environmental state did this process capture at launch that can change underneath it while it runs?

**Incidents:** 22 filed here, 14 more from other classes tagged with it. **Catalog node:** [catalog/ipc-and-env/](catalog/ipc-and-env/README.md)

## concurrency

Independent agents or sessions contend for one shared resource - a rate-limited API quota, a git index, a working tree - and degrade or corrupt each other, often silently.

**Ask:** How many live agents share this one resource right now, and what happens to the one you are waiting on when a second appears?

**Incidents:** 20 filed here, 16 more from other classes tagged with it. **Catalog node:** [catalog/concurrency/](catalog/concurrency/README.md)

## vcs-destruction

Version control is used as a weapon against the working tree: a blanket stage sweeps in unrelated edits, a revert-to-remote discards uncommitted work, or identity leaks into history.

**Ask:** Whose uncommitted work is in this tree, and what does a failure-path reset or a blanket 'add all' do to it?

**Incidents:** 21 filed here, 9 more from other classes tagged with it. **Catalog node:** [catalog/vcs-destruction/](catalog/vcs-destruction/README.md)

## delegation

A sub-agent re-delegates instead of doing the work: it spawns another loop, scaffolds a plan for a future iteration, and exits successfully having produced nothing.

**Ask:** Does the instruction forbid EVERY escape hatch - nested agents, scaffolding a loop, handing off to a later iteration - by name?

**Incidents:** 46 filed here, 23 more from other classes tagged with it. **Catalog node:** [catalog/delegation/](catalog/delegation/README.md)

**Topics:** [The brief or plan left a gap the worker fell through](catalog/delegation/brief-or-plan-left-a-gap.md) (8), [Teammates finished on disk; the reply never came or went unnoticed](catalog/delegation/finished-on-disk-no-reply.md) (6), [A record is guessed or stale, or lives only in a message or worktree](catalog/delegation/guessed-or-stale-id-name-path.md) (6), [Your order collided with a tool rule, permission ceiling, guard or pin](catalog/delegation/order-collides-with-rule-or-guard.md) (8), [The reviewer or runner you named was not independent or not free](catalog/delegation/reviewer-not-independent-or-free.md) (9), [Parallel work stalls behind one busy owner, open decision or slot cap](catalog/delegation/stalled-behind-one-owner-or-decision.md) (7)

## detector-fail-open

A monitor or safety check silently never fires: a wrong regex flavor, the wrong parsed field, a case mismatch. A negative result is mistaken for health.

**Ask:** Have you fed this detector a known-bad sample and watched it fire, AND a known-good sample and watched it stay silent?

**Incidents:** 31 filed here, 20 more from other classes tagged with it. **Catalog node:** [catalog/detector-fail-open/](catalog/detector-fail-open/README.md)

**Topics:** [The checker ran but its target coverage is unproven](catalog/detector-fail-open/coverage-and-controls-not-proven.md) (9), [A broken guard implementation still appears valid](catalog/detector-fail-open/guard-defaults-and-negative-controls.md) (6), [Syntax matching accepts decoys or rejects valid forms](catalog/detector-fail-open/syntax-shapes-and-benign-decoys.md) (7), [A parser or pattern reads the wrong evidence](catalog/detector-fail-open/wrong-parser-or-pattern.md) (7)

## detector-fail-closed

A monitor or check fires when it should not: it reports a correct artifact as broken, an honest quote as fabricated, a live process as dead. The accusation is specific and plausible, so the natural response is to repair the artifact - which is the destructive direction.

**Ask:** Before acting on this check's accusation, have you verified the ACCUSATION against the primary source - and could the check's own normalisation, base path or parser be the thing that disagrees?

**Incidents:** 15 filed here, 3 more from other classes tagged with it. **Catalog node:** [catalog/detector-fail-closed/](catalog/detector-fail-closed/README.md)

## stale-module

A long-running process runs the code it imported at launch. Later commits to that module are inert while git and the changelog report them shipped.

**Ask:** When did this process start, and how many commits to the code it imported have landed since - with no reload or restart?

**Incidents:** 8 filed here, 4 more from other classes tagged with it. **Catalog node:** [catalog/stale-module/](catalog/stale-module/README.md)

## checkpoint

An all-or-nothing step loses everything when it is interrupted, because it writes its output only at the end instead of writing a minimal-but-complete artifact first and refining in place.

**Ask:** If this step is killed at minute 8 of 10, does a usable artifact already exist on disk?

**Incidents:** 17 filed here, 15 more from other classes tagged with it. **Catalog node:** [catalog/checkpoint/](catalog/checkpoint/README.md)

## tooling-paths

The shell or tool layer betrays you: command substitution runs inside a string you meant as data, a built-in resolves paths from an unexpected root, an interpreter shim mutates the wrong environment.

**Ask:** Will any character in this string be interpreted rather than stored, and from what directory does this tool actually resolve paths?

**Incidents:** 69 filed here, 31 more from other classes tagged with it. **Catalog node:** [catalog/tooling-paths/](catalog/tooling-paths/README.md)

**Topics:** [A helper or runner reads your argument as a different kind or name](catalog/tooling-paths/argument-read-as-other-kind.md) (10), [A shell chain ran on after a failed step, or a refusal sank safe steps](catalog/tooling-paths/chain-ran-on-after-failure.md) (6), [An edit anchor or text match hit different bytes than you meant](catalog/tooling-paths/edit-or-match-hit-wrong-bytes.md) (8), [A relative path or link resolves from a different root than assumed](catalog/tooling-paths/path-resolves-from-wrong-root.md) (6), [Sandbox cannot resolve or authorize the target you actually meant](catalog/tooling-paths/sandbox-refuses-allowed-target.md) (6), [The tool's own resolution or defaults, not the target, caused it](catalog/tooling-paths/tool-defaults-not-target.md) (10), [The checkout or dependency tree you ran in lacks what the job needs](catalog/tooling-paths/tree-lacks-what-job-needs.md) (6), [Code valid alone fails in the host runtime, module form or generator](catalog/tooling-paths/valid-alone-fails-in-host.md) (8), [zsh reads your variable differently: colon modifier, word split, array](catalog/tooling-paths/zsh-expansion-surprises.md) (8)

## test-isolation

A test passes only in the environment where it was written: it depends on untracked local state, ambient file counts, a directory name, or git history a clean checkout does not have.

**Ask:** Would this test pass in a throwaway fresh clone on a different machine? What ambient state is it silently reading?

**Incidents:** 37 filed here, 33 more from other classes tagged with it. **Catalog node:** [catalog/test-isolation/](catalog/test-isolation/README.md)

**Topics:** [Assertion measures more than its contract: caches, order, whole totals](catalog/test-isolation/assertion-wider-than-contract.md) (8), [Green alone, red in the full suite, with another run, or after a merge](catalog/test-isolation/green-alone-red-together.md) (12), [Passes in a warm checkout, fails in a fresh clone, CI or other runner](catalog/test-isolation/passes-warm-fails-clean.md) (8), [The red comes from the test's own fixture, tool option or control](catalog/test-isolation/the-test-itself-is-the-defect.md) (8)

## observability

The signal you trust hides the truth: an outcome flag masks a chronically over-budget step, a lifetime average hides a spike, a hardened process reports zero usage.

**Ask:** Are you reading a distribution or a single number, a delta or a lifetime average - and could the measurement itself be denied?

**Incidents:** 43 filed here, 58 more from other classes tagged with it. **Catalog node:** [catalog/observability/](catalog/observability/README.md)

**Topics:** [Timestamp labels disagree with the actual clock](catalog/observability/clock-labels-without-clock-evidence.md) (15), [A reassuring signal contradicts the underlying evidence](catalog/observability/misleading-metrics-and-status.md) (13), [Missing evidence keeps findings unverified](catalog/observability/missing-or-unverifiable-receipts.md) (12)

## spec-and-scope

The loop does the wrong amount of work: it pursues the whole visible mission instead of its assigned slice, or picks tasks by lowest effort instead of highest value, or grows an artifact without bound.

**Ask:** Does the agent's visible context imply a bigger goal than its assigned task, and is any required-reading artifact growing every iteration?

**Incidents:** 112 filed here, 60 more from other classes tagged with it. **Catalog node:** [catalog/spec-and-scope/](catalog/spec-and-scope/README.md)

**Topics:** [Claims or instructions say more than the evidence supports](catalog/spec-and-scope/claims-outrun-available-evidence.md) (13), [A local fix leaves sibling cases or callers broken](catalog/spec-and-scope/fix-misses-related-consumers.md) (8), [Framework behavior contradicts the design or test](catalog/spec-and-scope/framework-contract-assumptions.md) (14), [Instructions fail a gate or omit the required operation](catalog/spec-and-scope/instructions-tools-cannot-follow.md) (12), [A planned step cannot run because its prerequisite is missing](catalog/spec-and-scope/missing-or-late-prerequisites.md) (11), [A cited baseline, count, line, or digest no longer matches its source](catalog/spec-and-scope/records-drift-or-lose-provenance.md) (15), [Requirements, units, or hard limits cannot hold together](catalog/spec-and-scope/requirements-and-limits-collide.md) (12), [Green tests omit or misstate required behavior](catalog/spec-and-scope/tests-do-not-prove-the-contract.md) (13), [Work lands under the wrong owner, path, or write boundary](catalog/spec-and-scope/wrong-owner-path-or-scope.md) (12)

## identity-and-keying

Two distinct things share one identifier or cache key, so state computed for one is served for the other: a slot number a rejection recycles, a cache keyed on a mutable name, a record cited by its position in a re-sorted list.

**Ask:** Is this key unique across everything it will ever be asked about, or only across the subset that succeeded?

**Incidents:** 36 filed here, 19 more from other classes tagged with it. **Catalog node:** [catalog/identity-and-keying/](catalog/identity-and-keying/README.md)

**Topics:** [An approval or activation names the wrong commit or line of history](catalog/identity-and-keying/approval-names-wrong-commit.md) (9), [A name, path string or digest stands in for the real identity, drifts](catalog/identity-and-keying/key-is-a-proxy.md) (6), [A newly minted id or name collides with one already in use](catalog/identity-and-keying/new-id-already-taken.md) (6), [A file-replacement (supersession) record is refused or claims too much](catalog/identity-and-keying/replacement-record-malformed.md) (14)
