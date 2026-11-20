# Taxonomy

Failure classes observed in production autonomous-agent loops. A single incident often
belongs to several: the interesting failures sit where two classes meet.

Each class links to its node in the [catalog](catalog/README.md), which lists its topics and incidents. To find a class from what you observe, start at the catalog root or run `python3 tools/afm.py route "..."`.

## reward-hacking

The loop optimizes the letter of its reward instead of the goal - Goodhart's law in production. It games its own success signal (ships busywork, self-reports success, satisfies a metric that no longer measures value).

**Ask:** Is the reward a proxy the agent can satisfy without doing the real work? What does the loop gain points for that a human would not call progress?

**Incidents:** 2 filed here, 0 more from other classes tagged with it. **Catalog node:** [catalog/reward-hacking/](catalog/reward-hacking/README.md)

## false-green

A quality gate reports success while the work is not actually good: vacuous tests, tautological assertions, skipped cases, or a grader that cannot fail.

**Ask:** Could this gate be green on broken code? What is the smallest wrong change that still passes it?

**Incidents:** 124 filed here, 60 more from other classes tagged with it. **Catalog node:** [catalog/false-green/](catalog/false-green/README.md)

## stage-timeout

A hard per-step wall-clock cap (beneath any outer timeout you set) silently kills work that runs too long. The narration drops and the step looks like it produced nothing.

**Ask:** What is the hardest time cap actually enforced on one step, and how close is the real work to it?

**Incidents:** 40 filed here, 9 more from other classes tagged with it. **Catalog node:** [catalog/stage-timeout/](catalog/stage-timeout/README.md)

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

**Incidents:** 44 filed here, 21 more from other classes tagged with it. **Catalog node:** [catalog/delegation/](catalog/delegation/README.md)

## detector-fail-open

A monitor or safety check silently never fires: a wrong regex flavor, the wrong parsed field, a case mismatch. A negative result is mistaken for health.

**Ask:** Have you fed this detector a known-bad sample and watched it fire, AND a known-good sample and watched it stay silent?

**Incidents:** 31 filed here, 20 more from other classes tagged with it. **Catalog node:** [catalog/detector-fail-open/](catalog/detector-fail-open/README.md)

## detector-fail-closed

A monitor or check fires when it should not: it reports a correct artifact as broken, an honest quote as fabricated, a live process as dead. The accusation is specific and plausible, so the natural response is to repair the artifact - which is the destructive direction.

**Ask:** Before acting on this check's accusation, have you verified the ACCUSATION against the primary source - and could the check's own normalisation, base path or parser be the thing that disagrees?

**Incidents:** 14 filed here, 3 more from other classes tagged with it. **Catalog node:** [catalog/detector-fail-closed/](catalog/detector-fail-closed/README.md)

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

**Incidents:** 68 filed here, 30 more from other classes tagged with it. **Catalog node:** [catalog/tooling-paths/](catalog/tooling-paths/README.md)

## test-isolation

A test passes only in the environment where it was written: it depends on untracked local state, ambient file counts, a directory name, or git history a clean checkout does not have.

**Ask:** Would this test pass in a throwaway fresh clone on a different machine? What ambient state is it silently reading?

**Incidents:** 36 filed here, 33 more from other classes tagged with it. **Catalog node:** [catalog/test-isolation/](catalog/test-isolation/README.md)

## observability

The signal you trust hides the truth: an outcome flag masks a chronically over-budget step, a lifetime average hides a spike, a hardened process reports zero usage.

**Ask:** Are you reading a distribution or a single number, a delta or a lifetime average - and could the measurement itself be denied?

**Incidents:** 43 filed here, 56 more from other classes tagged with it. **Catalog node:** [catalog/observability/](catalog/observability/README.md)

## spec-and-scope

The loop does the wrong amount of work: it pursues the whole visible mission instead of its assigned slice, or picks tasks by lowest effort instead of highest value, or grows an artifact without bound.

**Ask:** Does the agent's visible context imply a bigger goal than its assigned task, and is any required-reading artifact growing every iteration?

**Incidents:** 104 filed here, 58 more from other classes tagged with it. **Catalog node:** [catalog/spec-and-scope/](catalog/spec-and-scope/README.md)

## identity-and-keying

Two distinct things share one identifier or cache key, so state computed for one is served for the other: a slot number a rejection recycles, a cache keyed on a mutable name, a record cited by its position in a re-sorted list.

**Ask:** Is this key unique across everything it will ever be asked about, or only across the subset that succeeded?

**Incidents:** 36 filed here, 19 more from other classes tagged with it. **Catalog node:** [catalog/identity-and-keying/](catalog/identity-and-keying/README.md)
