# Agent Failure Modes

Post-mortems from running autonomous multi-agent build loops in production. Every incident here is a real failure that cost real time, followed by the specific fix that resolved it and a one-line rule terse enough to drop into an agent prompt.

The point of this collection is that these failures are *transferable*. They are not one team's or one framework's problems - they are what LLM-driven agent loops do when they meet real infrastructure. If you are building anything that runs unattended, the incidents here are what you will hit.

## What is in here

- **[incidents/](incidents/)** - 25 human-readable post-mortems, one per file. Each has: signature (how to recognise it), what happened, root cause, why it was hard to see, fix, verification, and a transferable rule.
- **[TAXONOMY.md](TAXONOMY.md)** - the 16 failure classes, each with the diagnostic question that surfaces it.
- **[RULES.md](RULES.md)** - every transferable rule in one place, ordered by severity. Intended as a prompt payload: paste it into an agent's system message or into a role card and the rules apply.
- **[data/incidents.json](data/incidents.json)** - the same content in machine-readable form for anyone who wants to query it or build tooling on top.

The corpus is the file at [`tools/corpus.py`](tools/corpus.py). Everything else is generated from it by [`tools/build.py`](tools/build.py), so the incident pages, the JSON index and the taxonomy cannot drift apart.

## Where these come from

These are post-mortems from loops I build, run and maintain myself, on my own machine, over months of unattended operation. They are not hypotheticals or a literature review. The public repositories the incidents were observed in:

- **[agent-foundry](https://github.com/jeffma8888/agent-foundry)** - an always-on multi-role build loop: a product agent, an engineer, a reviewer, a QA engineer firewalled from the source it tests, and an independent release gate that is the only role permitted to touch git. Most of the incidents below were observed here.
- **[proactive-loop-agent](https://github.com/jeffma8888/proactive-loop-agent)** - the proactivity layer above it: it scans working context, synthesizes a ranked slate of candidate goals, gates them through an explicit autonomy contract, and dispatches only the approved ones.
- **[resilient-agent-loop-primitives](https://github.com/jeffma8888/resilient-agent-loop-primitives)** - the retry, backoff and checkpoint primitives that came out of the failures catalogued here.

**What is generic, and what is attributed.** The failure description and the transferable rule are deliberately generic, because the whole point is that they transfer to any framework or agent runtime. Provenance is the deliberate exception: where an incident's artifact can be pointed at in a public repository, the incident's `Provenance` section names it and links it, so the claim is checkable rather than anecdotal. Public third-party projects are cited the same way where relevant. What is never named, anywhere in this repo, is an employer, an internal or private system, a private repository, a person, or a machine-local path.

## The failure classes

| Class | What it looks like |
|---|---|
| **reward-hacking** | The loop optimises the letter of its reward, not the goal. Ships busywork, satisfies a metric that no longer measures value. |
| **false-green** | A gate reports success while the work is bad: vacuous tests, tautological assertions, a grader that cannot fail. |
| **stage-timeout** | A hard per-step wall-clock cap (beneath any outer timeout) silently kills work. Narration drops; the step looks empty. |
| **verdict-token** | A machine-parsed decision token is missing or malformed, so a parser reads absence as the pessimistic default and destroys good work. |
| **steering-channel** | The channel meant to steer the loop is not actually delivered - truncated, mis-parsed, or dropped by the consumer that was supposed to read it. |
| **ipc-and-env** | The loop breaks on its runtime environment rather than its logic: rotated sockets, expired credentials, inherited stale variables, the machine sleeping. |
| **concurrency** | Independent agents or sessions contend for one shared resource - a rate-limited API, a git index, a working tree - and silently corrupt each other. |
| **vcs-destruction** | Version control used as a weapon on the tree: a blanket `add -A` sweeps unrelated edits, a failure-path reset discards uncommitted work. |
| **delegation** | A sub-agent re-delegates instead of doing the work: spawns another loop, scaffolds a plan for a future iteration, and exits 0 having produced nothing. |
| **detector-fail-open** | A monitor silently never fires: wrong regex flavor, wrong parsed field, case mismatch. A negative result is mistaken for health. |
| **stale-module** | A long-running process runs the code it imported at launch. Later commits are inert while git reports them shipped. |
| **checkpoint** | An all-or-nothing step loses everything when interrupted, because it writes its output only at the end. |
| **tooling-paths** | The shell layer betrays you: command substitution runs inside a string you meant as data, a built-in resolves paths from an unexpected root. |
| **test-isolation** | A test passes only in the environment where it was written: untracked local state, ambient file counts, a directory name, git history a clean checkout does not have. |
| **observability** | The signal you trust hides the truth: an outcome flag masks a chronically over-budget step, a lifetime average hides a spike. |
| **spec-and-scope** | The loop does the wrong amount of work: pursues the whole visible mission instead of its assigned slice, or grows an artifact without bound. |

## The most load-bearing rules

If you read nothing else, these three rules would have prevented most of the incidents here:

1. **Success is an ARTIFACT, not an exit code.** Under a hard timeout, an agent that writes its minimal complete output file first and refines in place still succeeds if killed. Correspondingly: never call a timeout a failure without checking whether the output file exists. ([INC-0006](incidents/INC-0006-checkpoint-first-a-killed-step-that-already-wrote-its-outp.md))
2. **A negative result from a detector is NOT evidence of health.** Every alarm must be proven against a known-bad sample (fires) and a known-good sample (does not fire) before it is trusted. Fail-open monitoring is worse than none. ([INC-0018](incidents/INC-0018-fail-open-detector-pipe-alternation-matches-nothing-und.md), [INC-0019](incidents/INC-0019-fail-open-detector-parsing-the-wrong-column-reports-hea.md))
3. **Change the REWARD, not the agent.** A loop that meets its reward but not its goal is Goodhart's law in production; a stricter reviewer still greenlights correct duplicates. Add a cross-iteration signal, and put the brake in the PLANNER's prompt. ([INC-0001](incidents/INC-0001-reward-hacking-twelve-near-identical-features-shipped-a.md))

## Provenance and honesty

These incidents come from a specific autonomous multi-agent build loop that ran unattended over weeks, shipping across four concurrent products. The failures are recorded with real dates and real costs. Names of specific tools, employers, and internal services have been genericised - the classes and mechanisms transfer regardless, which is the point.

The file [`tools/leakscan.py`](tools/leakscan.py) is a banned-token scanner that runs before every publish. It has a two-sided self-test: every rule must fire on a planted known-bad sample, and a known-good sample must not trip. A detector never proven against a known-bad sample is worthless, which is itself one of the incidents here ([INC-0018](incidents/INC-0018-fail-open-detector-pipe-alternation-matches-nothing-und.md)).

It has two tiers, and the split is deliberate. **Public structural rules** ship in the repo: absolute home paths, bare emails, private IPs, credential-shaped strings. **Private literal rules** - an employer name, a person's name, an internal system - load from a gitignored `.leakscan-private` file, because the literals *are* the sensitive thing and shipping them in the scanner would publish exactly what the scanner exists to prevent. See [`.leakscan-private.example`](.leakscan-private.example) for the format.

An earlier version of this file did carry the author's real name in a self-test sample, and reported the tree clean, because a scanner skips itself. That is [INC-0019](incidents/INC-0019-fail-open-detector-parsing-the-wrong-column-reports-hea.md) and [INC-0015](incidents/INC-0015-git-identity-leak-real-name-via-ambient-global-config.md) meeting in one file: a gate cannot see inside its own exemption, and a clean commit identity says nothing about clean file content. It was caught by sweeping every commit tree rather than trusting the gate. If you find a leak I missed, open an issue.

## Contributing

If you have hit a failure that generalises and does not fit any of the 16 classes, open an issue. If it fits an existing class, a PR against [`tools/corpus.py`](tools/corpus.py) is welcome. Constraints:

- Every incident needs a signature, a fix, and a transferable rule of at most 400 characters.
- Prefer honest cost estimates ("about 5 hours of silent stall") to marketing-shaped numbers.
- Generic language throughout. No employer names, personal identity, or machine-local paths - the leak scanner enforces this.
- Run `python3 tools/build.py` after any change; commit the regenerated `incidents/`, `data/`, `RULES.md`, `TAXONOMY.md` alongside the corpus edit.

## Regenerate

```
python3 tools/build.py     # rebuild everything from tools/corpus.py
python3 tools/leakscan.py  # scan for banned tokens across the tree
python3 -m pytest tests/   # run the invariants
```

## License

MIT. See [LICENSE](LICENSE).
