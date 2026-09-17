# Agent Failure Modes

Post-mortems from running autonomous multi-agent build loops in production. Every incident here is a real failure that cost real time, followed by the specific fix that resolved it and a one-line rule terse enough to drop into an agent prompt.

The point of this collection is that these failures are *transferable*. They are not one team's or one framework's problems - they are what LLM-driven agent loops do when they meet real infrastructure. If you are building anything that runs unattended, the incidents here are what you will hit.

## What is in here

<!-- BEGIN GENERATED: corpus-summary -->
- **[incidents/](incidents/)** - 43 human-readable post-mortems, one per file. Each has: signature (how to recognise it), what happened, root cause, why it was hard to see, fix, verification, and a transferable rule.
- **[TAXONOMY.md](TAXONOMY.md)** - the 18 failure classes, each with the diagnostic question that surfaces it.
<!-- END GENERATED: corpus-summary -->
- **[RULES.md](RULES.md)** - every transferable rule in one place, ordered by severity. Intended as a prompt payload: paste it into an agent's system message or into a role card and the rules apply.
- **Practices** (a section inside [RULES.md](RULES.md)) - cross-incident best practice: what to do by DEFAULT, rather than what went wrong once. An incident cites a date and a root cause; a practice cites the incidents it generalizes, and a test enforces that it can never claim evidence this corpus lacks.
- **[data/incidents.json](data/incidents.json)** - the same content in machine-readable form for anyone who wants to query it or build tooling on top.

The corpus is the file at [`tools/corpus.py`](tools/corpus.py). Everything else is generated from it by [`tools/build.py`](tools/build.py), so the incident pages, the JSON index and the taxonomy cannot drift apart.

## Where these come from

These are post-mortems from loops I build, run and maintain myself, on my own machine, over months of unattended operation. They are not hypotheticals or a literature review. The public repositories the incidents were observed in:

- **[agent-foundry](https://github.com/jeffma8888/agent-foundry)** - an always-on multi-role build loop: a product agent, an engineer, a reviewer, a QA engineer firewalled from the source it tests, and an independent release gate that is the only role permitted to touch git. Most of the incidents below were observed here.
- **[proactive-loop-agent](https://github.com/jeffma8888/proactive-loop-agent)** - the proactivity layer above it: it scans working context, synthesizes a ranked slate of candidate goals, gates them through an explicit autonomy contract, and dispatches only the approved ones.
- **[resilient-agent-loop-primitives](https://github.com/jeffma8888/resilient-agent-loop-primitives)** - the retry, backoff and checkpoint primitives that came out of the failures catalogued here.

**What is generic, and what is attributed.** The failure description and the transferable rule are deliberately generic, because the whole point is that they transfer to any framework or agent runtime. Provenance is the deliberate exception: where an incident's artifact can be pointed at in a public repository, the incident's `Provenance` section names it and links it, so the claim is checkable rather than anecdotal. Public third-party projects are cited the same way where relevant. What is never named, anywhere in this repo, is an employer, an internal or private system, a private repository, a person, or a machine-local path.

## How this stays current

These are captured while the loops are running, not reconstructed from memory afterwards. Two tools do it, and neither makes a model call:

- **[tools/mine_learnings.py](tools/mine_learnings.py)** - the census. It classifies every lesson a loop has ever written into the classes above and ranks them by a signal heuristic, so the highest-value exemplars surface out of a multi-megabyte log instead of being read linearly.
- **[tools/watch_loops.py](tools/watch_loops.py)** - the incremental version, run on a schedule. It keeps a watermark of lessons already reviewed, so each run reports only what is NEW, ranked by how thin this knowledge base's coverage of that failure class already is. A lesson the taxonomy cannot classify at all ranks highest, because that is weak evidence of a failure mode nobody has named yet. The fingerprint is deliberately independent of line numbers, so editing a log does not re-report everything in it.

Both take the watched directory as an argument and write only to a gitignored path, because the loops they read are machine-local and some are private. Nothing about them is committed here.

## The failure classes

<!-- BEGIN GENERATED: failure-classes -->
| Class | What it looks like |
|---|---|
| **reward-hacking** | The loop optimizes the letter of its reward instead of the goal - Goodhart's law in production. It games its own success signal (ships busywork, self-reports success, satisfies a metric that no longer measures value). |
| **false-green** | A quality gate reports success while the work is not actually good: vacuous tests, tautological assertions, skipped cases, or a grader that cannot fail. |
| **stage-timeout** | A hard per-step wall-clock cap (beneath any outer timeout you set) silently kills work that runs too long. The narration drops and the step looks like it produced nothing. |
| **verdict-token** | A machine-parsed decision token is missing or malformed, so a downstream parser reads the absence as the pessimistic default and discards good work. |
| **steering-channel** | The channel meant to steer the loop (injected instructions, pinned notes) is not actually delivered - it is truncated, mis-parsed, or dropped by the consumer that was supposed to read it. |
| **ipc-and-env** | The loop breaks on its runtime environment rather than its logic: a rotated socket, an expired credential, an inherited stale variable, the machine going to sleep. |
| **concurrency** | Independent agents or sessions contend for one shared resource - a rate-limited API quota, a git index, a working tree - and degrade or corrupt each other, often silently. |
| **vcs-destruction** | Version control is used as a weapon against the working tree: a blanket stage sweeps in unrelated edits, a revert-to-remote discards uncommitted work, or identity leaks into history. |
| **delegation** | A sub-agent re-delegates instead of doing the work: it spawns another loop, scaffolds a plan for a future iteration, and exits successfully having produced nothing. |
| **detector-fail-open** | A monitor or safety check silently never fires: a wrong regex flavor, the wrong parsed field, a case mismatch. A negative result is mistaken for health. |
| **detector-fail-closed** | A monitor or check fires when it should not: it reports a correct artifact as broken, an honest quote as fabricated, a live process as dead. The accusation is specific and plausible, so the natural response is to repair the artifact - which is the destructive direction. |
| **stale-module** | A long-running process runs the code it imported at launch. Later commits to that module are inert while git and the changelog report them shipped. |
| **checkpoint** | An all-or-nothing step loses everything when it is interrupted, because it writes its output only at the end instead of writing a minimal-but-complete artifact first and refining in place. |
| **tooling-paths** | The shell or tool layer betrays you: command substitution runs inside a string you meant as data, a built-in resolves paths from an unexpected root, an interpreter shim mutates the wrong environment. |
| **test-isolation** | A test passes only in the environment where it was written: it depends on untracked local state, ambient file counts, a directory name, or git history a clean checkout does not have. |
| **observability** | The signal you trust hides the truth: an outcome flag masks a chronically over-budget step, a lifetime average hides a spike, a hardened process reports zero usage. |
| **spec-and-scope** | The loop does the wrong amount of work: it pursues the whole visible mission instead of its assigned slice, or picks tasks by lowest effort instead of highest value, or grows an artifact without bound. |
| **identity-and-keying** | Two distinct things share one identifier or cache key, so state computed for one is served for the other: a slot number a rejection recycles, a cache keyed on a mutable name, a record cited by its position in a re-sorted list. |
<!-- END GENERATED: failure-classes -->

## The most load-bearing rules

If you read nothing else, these three rules would have prevented most of the incidents here:

1. **Success is an ARTIFACT, not an exit code.** Under a hard timeout, an agent that writes its minimal complete output file first and refines in place still succeeds if killed. Correspondingly: never call a timeout a failure without checking whether the output file exists. ([INC-0006](incidents/INC-0006-checkpoint-first-a-killed-step-that-already-wrote-its-output.md))
2. **A negative result from a detector is NOT evidence of health.** Every alarm must be proven against a known-bad sample (fires) and a known-good sample (does not fire) before it is trusted. Fail-open monitoring is worse than none. ([INC-0018](incidents/INC-0018-fail-open-detector-pipe-alternation-matches-nothing-under-on.md), [INC-0019](incidents/INC-0019-fail-open-detector-parsing-the-wrong-column-reports-healthy.md))
3. **Change the REWARD, not the agent.** A loop that meets its reward but not its goal is Goodhart's law in production; a stricter reviewer still greenlights correct duplicates. Add a cross-iteration signal, and put the brake in the PLANNER's prompt. ([INC-0001](incidents/INC-0001-reward-hacking-twelve-near-identical-features-shipped-as-dif.md))

## Provenance and honesty

These incidents come from a specific autonomous multi-agent build loop that ran unattended over weeks, shipping across four concurrent products. The failures are recorded with real dates and real costs. Names of specific tools, employers, and internal services have been genericised - the classes and mechanisms transfer regardless, which is the point.

The file [`tools/leakscan.py`](tools/leakscan.py) is a banned-token scanner that runs before every publish. It has a two-sided self-test: every rule must fire on a planted known-bad sample, and a known-good sample must not trip. A detector never proven against a known-bad sample is worthless, which is itself one of the incidents here ([INC-0018](incidents/INC-0018-fail-open-detector-pipe-alternation-matches-nothing-under-on.md)).

It has two tiers, and the split is deliberate. **Public structural rules** ship in the repo: absolute home paths, bare emails, private IPs, credential-shaped strings. **Private literal rules** - an employer name, a person's name, an internal system - load from a gitignored `.leakscan-private` file, because the literals *are* the sensitive thing and shipping them in the scanner would publish exactly what the scanner exists to prevent. See [`.leakscan-private.example`](.leakscan-private.example) for the format.

An earlier version of this file did carry the author's real name in a self-test sample, and reported the tree clean, because a scanner skips itself. That is [INC-0019](incidents/INC-0019-fail-open-detector-parsing-the-wrong-column-reports-healthy.md) and [INC-0015](incidents/INC-0015-git-identity-leak-real-name-via-ambient-global-config.md) meeting in one file: a gate cannot see inside its own exemption, and a clean commit identity says nothing about clean file content. It was caught by sweeping every commit tree rather than trusting the gate. If you find a leak I missed, open an issue.

## Contributing

If you have hit a failure that generalises and does not fit any existing class, open an issue. If it fits an existing class, a PR against [`tools/corpus.py`](tools/corpus.py) is welcome. Constraints:

- Every incident needs a signature, a fix, and a transferable rule of at most 400 characters.
- Prefer honest cost estimates ("about 5 hours of silent stall") to marketing-shaped numbers.
- Generic language throughout. No employer names, personal identity, or machine-local paths - the leak scanner enforces this.
- Run `python3 tools/build.py` after any change; commit the regenerated `incidents/`, `data/`, `RULES.md`, `TAXONOMY.md`, and README regions alongside the corpus edit.

## Regenerate

```
python3 tools/build.py     # rebuild everything from tools/corpus.py
python3 tools/leakscan.py  # scan for banned tokens across the tree
python3 -m pytest tests/   # run the invariants
```

## Part of a pipeline

This register is the **upstream** of two siblings, and its `## Practices` section in `RULES.md` is a machine-readable contract, not just prose:

- [`agent-gap-radar`](https://github.com/jeffma8888/agent-gap-radar) cites these incident rules as evidence for **unsolved gaps**.
- [`agent-practice-index`](https://github.com/jeffma8888/agent-practice-index) **parses the `## Practices` section** (`practice from-rules RULES.md`) and drafts a practice record for every `PRA-NNNN` not yet in its index, quoting the bullet verbatim. Keep that section's `- **[PRA-NNNN]** text` / `_derived from:_` shape stable: a downstream tool reads it.

Full data flow and commands: [ECOSYSTEM.md](https://github.com/jeffma8888/agent-practice-index/blob/main/ECOSYSTEM.md).

## License

MIT. See [LICENSE](LICENSE).
