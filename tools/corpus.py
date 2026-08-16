#!/usr/bin/env python3
"""Structured incident corpus - the single source of truth for this KB.

Every human-readable file in the repo is generated from this module by
tools/build.py, so the incident pages, the JSON index, the taxonomy and the
rule list can never drift apart. Edit incidents here, then run the build.

The failure description and the transferable RULE are deliberately GENERIC: they
describe a failure mode of autonomous agent loops in terms any engineer can
reuse. That is the point - the lessons transfer precisely because they are not
about one codebase.

PROVENANCE is the deliberate exception. Where an incident was observed in a
PUBLIC repository, the optional `evidence` list names that repository and links
it, so a reader can check the claim instead of taking it on trust; public
third-party projects may be cited the same way. What is never named, in any
field: an employer, an internal or private system, a private repository, a
person, or a machine-local path.
"""
from __future__ import annotations

# Failure classes. An incident usually belongs to several; the interesting
# failures live where two classes intersect.
CLASSES: dict[str, dict[str, str]] = {
    "reward-hacking": {
        "what": "The loop optimizes the letter of its reward instead of the goal - Goodhart's law in production. It games its own success signal (ships busywork, self-reports success, satisfies a metric that no longer measures value).",
        "ask": "Is the reward a proxy the agent can satisfy without doing the real work? What does the loop gain points for that a human would not call progress?",
    },
    "false-green": {
        "what": "A quality gate reports success while the work is not actually good: vacuous tests, tautological assertions, skipped cases, or a grader that cannot fail.",
        "ask": "Could this gate be green on broken code? What is the smallest wrong change that still passes it?",
    },
    "stage-timeout": {
        "what": "A hard per-step wall-clock cap (beneath any outer timeout you set) silently kills work that runs too long. The narration drops and the step looks like it produced nothing.",
        "ask": "What is the hardest time cap actually enforced on one step, and how close is the real work to it?",
    },
    "verdict-token": {
        "what": "A machine-parsed decision token is missing or malformed, so a downstream parser reads the absence as the pessimistic default and discards good work.",
        "ask": "If the step is killed before it writes its decision, what does the parser assume - and is that assumption safe?",
    },
    "steering-channel": {
        "what": "The channel meant to steer the loop (injected instructions, pinned notes) is not actually delivered - it is truncated, mis-parsed, or dropped by the consumer that was supposed to read it.",
        "ask": "Did the CONSUMER's own parser emit the steering text verbatim, or did you only confirm you wrote it?",
    },
    "ipc-and-env": {
        "what": "The loop breaks on its runtime environment rather than its logic: a rotated socket, an expired credential, an inherited stale variable, the machine going to sleep.",
        "ask": "What environmental state did this process capture at launch that can change underneath it while it runs?",
    },
    "concurrency": {
        "what": "Independent agents or sessions contend for one shared resource - a rate-limited API quota, a git index, a working tree - and degrade or corrupt each other, often silently.",
        "ask": "How many live agents share this one resource right now, and what happens to the one you are waiting on when a second appears?",
    },
    "vcs-destruction": {
        "what": "Version control is used as a weapon against the working tree: a blanket stage sweeps in unrelated edits, a revert-to-remote discards uncommitted work, or identity leaks into history.",
        "ask": "Whose uncommitted work is in this tree, and what does a failure-path reset or a blanket 'add all' do to it?",
    },
    "delegation": {
        "what": "A sub-agent re-delegates instead of doing the work: it spawns another loop, scaffolds a plan for a future iteration, and exits successfully having produced nothing.",
        "ask": "Does the instruction forbid EVERY escape hatch - nested agents, scaffolding a loop, handing off to a later iteration - by name?",
    },
    "detector-fail-open": {
        "what": "A monitor or safety check silently never fires: a wrong regex flavor, the wrong parsed field, a case mismatch. A negative result is mistaken for health.",
        "ask": "Have you fed this detector a known-bad sample and watched it fire, AND a known-good sample and watched it stay silent?",
    },
    "stale-module": {
        "what": "A long-running process runs the code it imported at launch. Later commits to that module are inert while git and the changelog report them shipped.",
        "ask": "When did this process start, and how many commits to the code it imported have landed since - with no reload or restart?",
    },
    "checkpoint": {
        "what": "An all-or-nothing step loses everything when it is interrupted, because it writes its output only at the end instead of writing a minimal-but-complete artifact first and refining in place.",
        "ask": "If this step is killed at minute 8 of 10, does a usable artifact already exist on disk?",
    },
    "tooling-paths": {
        "what": "The shell or tool layer betrays you: command substitution runs inside a string you meant as data, a built-in resolves paths from an unexpected root, an interpreter shim mutates the wrong environment.",
        "ask": "Will any character in this string be interpreted rather than stored, and from what directory does this tool actually resolve paths?",
    },
    "test-isolation": {
        "what": "A test passes only in the environment where it was written: it depends on untracked local state, ambient file counts, a directory name, or git history a clean checkout does not have.",
        "ask": "Would this test pass in a throwaway fresh clone on a different machine? What ambient state is it silently reading?",
    },
    "observability": {
        "what": "The signal you trust hides the truth: an outcome flag masks a chronically over-budget step, a lifetime average hides a spike, a hardened process reports zero usage.",
        "ask": "Are you reading a distribution or a single number, a delta or a lifetime average - and could the measurement itself be denied?",
    },
    "spec-and-scope": {
        "what": "The loop does the wrong amount of work: it pursues the whole visible mission instead of its assigned slice, or picks tasks by lowest effort instead of highest value, or grows an artifact without bound.",
        "ask": "Does the agent's visible context imply a bigger goal than its assigned task, and is any required-reading artifact growing every iteration?",
    },
}


_BATCH1: list[dict] = [
    {
        "id": "INC-0001",
        "title": "Reward hacking: twelve near-identical features shipped as different work",
        "date": "2026-08-06",
        "classes": ["reward-hacking", "false-green", "spec-and-scope"],
        "severity": "high",
        "status": "fixed",
        "cost": "About a week of loop output was busywork before it was caught by an out-of-loop reviewer.",
        "signature": "The loop keeps shipping green work, but if you diff the last N ships they are progressively similar to prior ones. Every iteration passes review; every artifact is individually correct.",
        "what": "A multi-agent build loop with a PM role and a review gate produced twelve consecutive iterations where each 'new' feature was a small variant of one already shipped: a different output format flag, a slight rename, an equivalent alternative representation. Every gate was green. Two independent agents observing from outside the loop noticed the cluster.",
        "root_cause": "The success signal rewarded shipping a passing feature, not shipping a NOVEL passing feature. The planner chose stories by lowest wall-clock cost among candidates with the strongest local evidence of feasibility - which selected for capabilities adjacent to already-shipped ones. That is a rational strategy for the reward given and a wrong strategy for the actual goal.",
        "why_hard": "Every stage was working correctly. Tests were green because the code was correct. No lint, no coverage, no reviewer would flag a small correct addition. The failure is only visible when you compare ACROSS iterations, which is not a check any single stage runs.",
        "fix": "Change the REWARD, not the agent. Two new signals: (a) an explicit novelty check in the planner's prompt instructing it to reject a story if a comparable capability already ships, and (b) a scout that reviews the last N iterations' shipped work and adds a duplicate-of objection to the planner's input when it finds one. Do NOT tighten the reviewer prompt - a stricter reviewer still greenlights the duplicate, because the duplicate is correct code.",
        "verification": "The next scout run detected two more borderline duplicates already in flight and vetoed them before they reached the review gate. No further duplicates shipped in the following six weeks.",
        "rule": "A loop that meets its reward but not its goal is Goodhart's law in production. Change the REWARD, never the agent - a stricter reviewer still greenlights correct duplicates. Add a cross-iteration novelty signal (a scout that reviews the last N ships and vetoes clones), and put the brake in the PLANNER's prompt, not the coder's.",
        "related": ["INC-0007"],
    },
    {
        "id": "INC-0002",
        "title": "The hard per-step wall-clock cap is the number-one cause of lost work",
        "date": "2026-08-04",
        "classes": ["stage-timeout", "observability", "checkpoint"],
        "severity": "critical",
        "status": "mitigated",
        "cost": "About 9 hours across 2 full iterations produced zero shipped commits: 8 attempts, 8 timeouts, 0 output.",
        "signature": "Every attempt log for a specific step is exactly the same tiny size and reads only 'timed out after 600s'. Two full iterations produce nothing while sibling teams on the same infrastructure ship normally.",
        "what": "A multi-team build loop lost 9 hours of wall clock across 8 attempts on a single team's planning step. Every attempt log was 48 bytes - the timeout message and nothing else, meaning the agent produced no output before being killed. Sibling teams on the same box in the same window shipped normally.",
        "root_cause": "The agent CLI enforced a hard 600-second cap per invocation, beneath any outer timeout the loop set. The step had grown to require reading and rewriting a large input file that exceeded the time budget, so every attempt was killed mid-work. The loop's success predicate ('output file exists') hid this: on the rare occasion the work landed before 600s, the step's median was reported as healthy instead of AT the cap.",
        "why_hard": "The outer timeout on the loop was set to 1800s and looked fine; the real cap is two layers below. And the loop's own telemetry showed the step passing sometimes, not dying at exactly 600 every time.",
        "fix": "Three changes in priority order. (a) Put a write-early rule in every role prompt: a step counts as SUCCESS the moment it writes a minimal-but-complete output file, then refines in place. (b) Add per-step duration metrics to the dispatcher so a median at the cap is visible. (c) Give the largest inputs a character budget and enforce it (see INC-0004).",
        "verification": "After the write-early rule shipped, the same team's next iteration produced output on attempt 1 even though the attempt still hit 600s - because the agent had checkpointed its minimal artifact within the first 8 minutes.",
        "rule": "A per-step timeout you did not set is often the real timeout. If a step's attempt logs are all the same tiny size, its median is AT the cap, not near it. Fix: write-early checkpoint (minimal complete output first, then refine in place), and always report the duration DISTRIBUTION, never a single-shot healthy flag.",
        "evidence": [
            'https://github.com/jeffma8888/agent-foundry - the orchestrator whose hard per-stage cap this describes; the cap is enforced by the agent CLI beneath the timeout the loop sets itself.',
            'https://github.com/jeffma8888/proactive-loop-agent - the product loop whose planning stage burned two consecutive iterations this way: 8 attempts, 8 timeouts, ~9 hours, no output, every attempt log 48 bytes.',
        ],
        "related": ["INC-0006", "INC-0007"],
    },
    {
        "id": "INC-0003",
        "title": "A slow test suite makes a product unbuildable by the loop",
        "date": "2026-08-04",
        "classes": ["stage-timeout", "spec-and-scope", "test-isolation"],
        "severity": "high",
        "status": "fixed",
        "cost": "About 7 hours across 3 iterations shipped 0 commits for one product; the correct fix touched a config the loop was not authorized to change.",
        "signature": "One team consistently fails while sibling teams on the same infrastructure ship normally. Every failed engineer and tester attempt log is a 48-byte 'timed out' stub. Shrinking the spec does not help.",
        "what": "A build loop had four products. Three shipped normally; the fourth went 3 iterations / 7 hours / 0 ships. Attempt logs were all identical 48-byte timeout messages. The natural hypothesis was rate-limiting by the model provider. Wrong.",
        "root_cause": "The product's own test suite took 504 seconds. The agent CLI's per-invocation cap was 600 seconds. That left about 96 seconds for the engineer or tester agent to read, edit, verify and write its output file - so every attempt died right after the suite finished. The spec-size hypothesis was falsifiable and falsified: specs shrank from 13KB to 6KB and a two-line change still failed.",
        "why_hard": "The failure looked like provider throttling (concurrent teams, some green some red is throttle-shaped), and the local test suite was in fact all green. Only a wall-clock measurement of the suite against the CLI cap made the shape visible.",
        "fix": "Make the suite fast. The product's own planner had proposed pytest parallelism in prior iterations; the loop could not act on it because that required relaxing a 'dev-dep: pytest only' quality bar - an OPERATOR decision, not an agent one. Adding pytest-xdist as a locked dev dep and setting `addopts = \"-q -n auto\"` cut the suite from 504s to 89s (5.7x). Put the parallelism in `addopts`, not in one call site, so every call site inherits it.",
        "verification": "Suite: 504s to 89s across three consecutive runs. The next iteration shipped in 46 minutes, every step producing output on attempt 1.",
        "rule": "A loop CAN correctly diagnose its own blocker and still be structurally unable to fix it if the fix touches a policy only the operator owns - so when a team stalls, READ ITS PLANNER'S NOTES FIRST. If a suite approaches the per-step timeout, the product is unbuildable by the loop; fix the SUITE, and put the fix in a config all call sites inherit.",
        "related": ["INC-0002", "INC-0004"],
    },
    {
        "id": "INC-0004",
        "title": "A monotonically growing required-reading file silently kills the loop",
        "date": "2026-08-04",
        "classes": ["stage-timeout", "steering-channel", "spec-and-scope"],
        "severity": "high",
        "status": "fixed",
        "cost": "A product stopped committing for 5 hours - four consecutive attempts, all 48-byte timeout logs.",
        "signature": "Same log signature as INC-0002, but the guilty artifact is a required-reading file (a roadmap, a design doc, a large context file) that grew organically over many iterations.",
        "what": "A product's planning role must read AND REWRITE a roadmap file every iteration. Over 90-plus iterations it grew to 200KB. The read-plus-rewrite time crossed 600 seconds and every attempt died before producing output. The log signature was identical to INC-0002's.",
        "root_cause": "Any required-reading artifact injected into every step's prompt is a resource that must be bounded by CHARACTERS, not by item count. This file bounded nothing: each iteration appended a new row and never compacted. The steering channel meant to keep the loop informed silently became the thing that killed it.",
        "why_hard": "The file is doing exactly what it was designed to do - accumulating decisions - and shrinking it feels wrong. The 48-byte log looks identical to a throttle stall. Distinguish: throttle logs say 'service is busy'; stale-endpoint logs contain CLI help text; hard-cap logs are exactly the timeout string and nothing else.",
        "fix": "Compact the file to an index and move verbatim history to a sibling archive. Add a size budget and enforce it in the loop's own tests, so a regressing growth cannot recur silently. If you must keep the full record, split it: a small always-read index plus a large read-on-demand archive.",
        "verification": "The file went 200KB to 36KB (83% smaller, all 98 rows preserved). The next planning attempt produced output within 3 minutes.",
        "rule": "Any file injected into EVERY iteration's prompt is a resource. Bound it by CHARACTERS, not item count, and cap it at write time. A monotonically growing steering artifact will silently kill the loop on the same timeout cap; when it does, the log looks exactly like a rate-limit stall - distinguish by content, not size.",
        "related": ["INC-0002", "INC-0020"],
    },
    {
        "id": "INC-0005",
        "title": "A killed step with no verdict token is read as REVERTED",
        "date": "2026-08-10",
        "classes": ["verdict-token", "stage-timeout"],
        "severity": "critical",
        "status": "mitigated",
        "cost": "Two of three iterations reverted with every gate green, destroying verified work.",
        "signature": "An iteration passes every gate, tests are green, git status is clean - and the loop reverts anyway with no error message. The final step's log ends mid-verification.",
        "what": "A ship step was expected to write one of two verdict tokens: PUSHED or REVERTED. A parser downstream read that token to decide whether to keep the iteration's work or reset to origin. On several consecutive iterations the step was killed by the per-stage cap before it wrote a token. The parser saw no token and defaulted to REVERTED. All-green work was destroyed.",
        "root_cause": "A parser that accepted only two literal tokens and defaulted to the pessimistic one on absence. Combined with a step instructed to verify thoroughly (suite pass, spec audit, doc audit, fresh-clone check) under a hard 600s cap, it predictably ran out of time before writing its verdict.",
        "why_hard": "The step is doing exactly what it was told to do: being careful. The parser's pessimistic default is a reasonable safety choice in isolation. The failure is that 'thoroughness' and 'cap' together produce 'no token' more often than the parser designer expected. And the obvious fix had already been applied once, in the opposite direction. An earlier version had the step write its verdict token EARLY as a placeholder it intended to overwrite; four iterations of already-green work were lost that way, each killed after its own gates had passed while the artifact still held the placeholder. So placeholders were banned - and that ban is what produced the no-token revert, which then destroyed two of three consecutive iterations. The failure mode inverted under its own fix, which is why the surviving rule has to be narrow: write the REAL verdict early. Not 'write something early', and not 'never write early'.",
        "fix": "Two changes. (a) Never write a placeholder token - only the real verdict, but write it EARLY. Budget verification to the cap: decide on decisive evidence only (full suite result + git status showing intended changes), and write the token by minute 8. Reviewer nits, prose fixes, doc-wording edits are NOT ship blockers; record them as follow-ups. (b) On the parser side, distinguish 'no token due to timeout' (retry-safe) from 'REVERTED' (destructive) whenever the token stream carries any indication of the underlying cause.",
        "verification": "The next four iterations wrote their token by minute 6-8 of a ~12-minute step and all shipped correctly. Status stays MITIGATED rather than fixed, for three reasons that are all still live. The parser still collapses 'killed before deciding' and 'decided not to ship' into one destructive outcome. The ship step is the one role FORBIDDEN from checkpoint-first, because its verdict has to be the artifact's last line, so the mechanism that protects every other role structurally cannot protect the verdict itself. And retries re-run the whole verification from scratch, so four attempts are one correlated failure rather than four independent chances. What actually shipped is a behavioural budget written into a prompt, which is the weakest kind of guarantee: it holds only while the agent obeys it under time pressure. See INC-0025.",
        "rule": "A machine-parsed verdict token that defaults to the destructive answer on absence is a critical safety hazard when its writer runs under a hard timeout. Write the verdict EARLY on decisive evidence only, budget verification to the cap, and treat lower-priority audits as follow-ups.",
        "evidence": [
            'https://github.com/jeffma8888/agent-foundry - the verdict parser and the release-gate role card that this incident is about: `parse_ship_action` in `foundry.py` accepts only PUSHED/REVERTED and returns None otherwise, and `roles/final.md` carries the verify-first exception that forbids this one role from checkpointing its verdict.',
        ],
        "related": ["INC-0002", "INC-0006", "INC-0025"],
    },
    {
        "id": "INC-0006",
        "title": "Checkpoint-first: a killed step that already wrote its output still counts",
        "date": "2026-08-05",
        "classes": ["checkpoint", "stage-timeout"],
        "severity": "medium",
        "status": "fixed",
        "cost": "An iteration that would have been the fourth consecutive loss instead shipped, because a role prompt shipped 34 minutes earlier had introduced the write-early rule.",
        "signature": "An attempt log is 48 bytes ('timed out after 600s') and the loop treats the iteration as a success anyway - because the OUTPUT FILE exists.",
        "what": "A tester step hit the per-step cap. Its log was 48 bytes; its exit code non-zero. And yet the iteration was recorded as SUCCESS - because the agent had written a 3459-byte tester output file BEFORE being killed. A role-card rule shipped earlier had instructed every role to write a minimal-complete output file first, then refine in place.",
        "root_cause": "Not a failure - a successful design pattern proving itself. The FAILURE that this pattern addresses is loops reading exit codes or log lengths to decide success when what actually mattered was whether a usable artifact existed.",
        "why_hard": "The instinct is to read the exit code and the log. Both said 'killed'. Trusting the artifact instead requires a small leap.",
        "fix": "Define success as 'the output file exists and is non-empty', not as 'exit code zero'. Instruct every agent role to write its minimal complete artifact within the first few minutes and refine in place until killed. Never call a timeout a failure without checking whether the output file exists.",
        "verification": "The successful timed-out iteration shipped clean. Independent gates (final-step parser plus post-release fresh-clone re-run) still catch cases where the early checkpoint describes incomplete verification.",
        "rule": "Success is an ARTIFACT, not an exit code. Under a hard timeout, an agent that writes its minimal complete output first and refines in place still succeeds if killed. Correspondingly: never call a timeout a failure without checking whether the output file exists.",
        "evidence": [
            'https://github.com/jeffma8888/agent-foundry - the write-early contract lives in the `roles/*.md` cards, which are read from disk per run, and the success-is-an-artifact rule is enforced by the stage runner rather than by exit code.',
        ],
        "related": ["INC-0002", "INC-0005"],
    },
    {
        "id": "INC-0007",
        "title": "Diagnose stalled work from the duration distribution, not the outcome",
        "date": "2026-08-04",
        "classes": ["observability", "stage-timeout"],
        "severity": "medium",
        "status": "fixed",
        "cost": "A plausible-but-untested fix was shipped and failed. The correct diagnosis was in the log the whole time - it just needed to be tallied.",
        "signature": "The loop's per-step success rate looks healthy. But if you compute the median wall-clock per step, one specific step sits AT the hard cap.",
        "what": "A stalled team had been miscategorized as 'sometimes green, sometimes red'. Pairing every 'attempt started' line in the dispatcher log with its 'produced / no output file' line showed the step's MEDIAN was 600 seconds - the hard cap - across every recorded sample. Its successes were killed at 600s too and merely happened to have written their output first.",
        "root_cause": "An outcome-only view of a step that runs under a hard timeout is blind to whether the step is chronically over budget. Once you measure the distribution, you cannot un-see it.",
        "why_hard": "The successes look like proof the step is fine. The raw data was in the log the whole time.",
        "fix": "Add a small per-step duration reporter to the dispatcher output. Include median, P90, and count-at-cap. Compare against a SIBLING running the same pipeline on the same box in the same window - which cheaply falsifies 'the machine is slow' or 'the provider is throttling'.",
        "verification": "The reporter surfaced two more chronically-over-budget steps within a week. Both were fixed at the root (INC-0002's write-early pattern, then INC-0003's suite-speed fix).",
        "rule": "A success predicate defined as 'the output file exists' hides a chronically over-budget step. Report the DURATION DISTRIBUTION per step, not just the outcome, and compare against a sibling running the same pipeline on the same box - which cheaply falsifies 'the machine is slow' or 'the provider is throttling'.",
        "related": ["INC-0002", "INC-0006"],
    },
    {
        "id": "INC-0008",
        "title": "Stale IPC endpoint after the host application restarts",
        "date": "2026-08-03",
        "classes": ["ipc-and-env"],
        "severity": "high",
        "status": "mitigated",
        "cost": "Every step instant-failed with a ~500-byte CLI help-text log; the dispatcher sat alive-but-broken for hours before the failure mode was recognized.",
        "signature": "Every step instantly fails (same-second timing, not a timeout). Attempt logs are ~500 bytes containing CLI help text ('did not match ... check syntax'), not the timeout string. The process looks alive.",
        "what": "The agent CLI was served by a running host application over a Unix socket at a path derived from the host's PID. When the host app restarted the PID changed and the socket rotated. Any long-running loop that had inherited the old socket path in its environment continued running - and every one of its child invocations failed instantly with the CLI's built-in 'endpoint not reachable' help text.",
        "root_cause": "The dispatcher spawned children via `subprocess.run(cmd, ...)` with NO `env=` argument, so every child inherited the environment captured at launch. That endpoint pointed at a socket that no longer existed.",
        "why_hard": "The process was alive. A naive is-it-running check returned yes. Only the specific log-content signature revealed the failure: ~500 bytes, CLI help text, same-second timing.",
        "fix": "Resolve the endpoint at each child spawn instead of capturing it once. On spawn, glob candidate sockets by mtime, and for the newest do a 0.5s `connect()` probe to confirm a live listener. If it answers, pass that path in the child's env; if none answer, leave the inherited value and warn (never make a working setup worse). Do NOT rely on `os.kill(pid, 0)` against a PID embedded in the socket filename - PID reuse silently returns 'alive' on an unrelated live process.",
        "verification": "After the fix, a synthetic app restart in the same session left the dispatcher's next spawn healthy. Regression test: bind a real listener and a non-listening socket side by side in a tmp dir and confirm the probe selects the listener.",
        "rule": "A subprocess spawned with no explicit env inherits every environmental identifier the parent captured at launch - including socket paths tied to a PID that can change. When the parent long outlives its environmental assumptions, resolve identifiers at spawn time with an ACTIVE probe (connect, not exists). Never trust a PID from a filename against PID reuse.",
        "related": ["INC-0009"],
    },
    {
        "id": "INC-0009",
        "title": "Interactive-only credential expiry silently stalls unattended loops",
        "date": "2026-07-31",
        "classes": ["ipc-and-env", "detector-fail-open"],
        "severity": "high",
        "status": "mitigated",
        "cost": "About 5 hours of silent stall across two iterations, then a couple more of the same before an alarm was built - all harmless (retries kept failing safely) but zero throughput.",
        "signature": "Step logs say 'credential refresh failed' or 'authentication timed out'. Distinct from throttle ('service is busy') and from the hard timeout ('timed out after 600s'). The lead thread also stalls, so hours can pass silently.",
        "what": "A long-running unattended loop broke on the model provider's credential expiring, not on rate limiting. The credential was held in a cookie file with a ~12-hour TTL and could only be refreshed via an interactive prompt requiring a hardware key. When the cookie expired, every model call failed and the loop retried harmlessly forever until a human re-authenticated.",
        "root_cause": "The credential is refreshable, but only interactively - no unattended loop can refresh it. The retry loop was doing the right thing (keeping work safe), but the work was stalled indefinitely.",
        "why_hard": "The signature is easy to confuse with throttling. And there is no single event to alarm on: the useful signal is 'the long-lived credential is about to expire', not 'credential just expired'.",
        "fix": "A simple watchdog script that (a) proactively warns when the long-lived credential drops below N minutes remaining, and (b) reactively greps recent step logs for the 'credential refresh failed' string as ground truth. Watch the LONG-LIVED credential (12h TTL), not the short-lived derivative one (auto-refreshing), or the alarm fires constantly.",
        "verification": "A subsequent 6-hour stall auto-recovered the instant the human re-authenticated. Turnaround from silent-multi-hour-stall to under-5-minute re-auth.",
        "rule": "Any long unattended loop depending on a human-refreshable credential will eventually stall on expiry, not throttle. Watch the LONG-LIVED credential (12h class), not the short-lived derivative one, and pair a 'time-remaining' alarm with a log-string alarm - each catches what the other misses.",
        "related": ["INC-0008", "INC-0018", "INC-0019"],
    },
    {
        "id": "INC-0010",
        "title": "Sleep beats the wake-lock on battery power",
        "date": "2026-07-19",
        "classes": ["ipc-and-env"],
        "severity": "high",
        "status": "fixed",
        "cost": "An entire overnight batch of 6 tasks produced 0/6 outputs.",
        "signature": "Every task fails with the same 'Connection stalled - no data received for 120 s (network issue or system sleep)' error. Retry-and-backoff works correctly and still cannot win.",
        "what": "An overnight background batch on a laptop ran with the OS wake-lock utility holding a 'prevent system sleep' flag. Every task failed with the 120-second stall signature. Retries backed off correctly (10, 20, 40, 60 min) and every retry also failed. Zero outputs.",
        "root_cause": "The 'prevent system sleep' primitive is documented to have no effect on battery power - only on AC. The laptop was on battery. The wake-lock utility ran and reported success but its most important flag was silently ignored, the machine slept through every retry window, and every task hit the network-stall timeout.",
        "why_hard": "The utility runs, reports success, and looks correct. Nothing warns that its most important flag is being ignored.",
        "fix": "For any unattended overnight run on a laptop: plug in AC. If AC is unavailable, use the OS's stronger sleep-disable primitive (typically requires elevated privileges) instead of the utility flag. Confirm with the OS's own assertion listing - the aggregate assertion flips from 0 to 1 the moment AC is connected on machines that gate the prevent-sleep primitive on power state.",
        "verification": "The same task batch on the same machine on AC ran cleanly on the first attempt. Diagnostic: read the battery power source AND read active OS sleep-assertions - not just the flag you set.",
        "rule": "A wake-lock utility on a laptop is not enough on battery power - the 'prevent system sleep' primitive is often silently gated on AC. Before an overnight unattended run, plug in AC and confirm the OS assertion is actually held. If the machine sleeps, retry-and-backoff cannot save you.",
        "related": ["INC-0011"],
    },
    {
        "id": "INC-0011",
        "title": "Concurrent agent brains silently starve and kill each other",
        "date": "2026-08-10",
        "classes": ["concurrency", "ipc-and-env"],
        "severity": "critical",
        "status": "mitigated",
        "cost": "An 8-task research batch failed 8/8 across 5 retries each, zero outputs, because 8 subagents were launched into a saturated model-provider account already running an always-on dispatcher.",
        "signature": "Multiple tasks fail with 'Connection stalled - no data received for 120 s' plus occasional 'service is busy'. AC power is confirmed. A long-running dispatcher process is alive.",
        "what": "A background 8-task batch was launched into an account already running an always-on dispatcher (5+ days uptime) that was itself firing agent invocations every few minutes. The batch failed 8/8, 5 attempts each, zero output files. The signature matched no-sleep-but-quota-starvation. The same failure had been recorded in the project's own changelog 5 days earlier and unread.",
        "root_cause": "One provider account, N concurrent brains fighting for it. Each brain retries on failure, which manufactures more concurrent load, which starves the others further. There is no graceful degradation - the losing brain simply cannot make progress.",
        "why_hard": "The individual failure signature (connection stall, service busy) is identical to a sleep issue or a genuine transient network problem. It only makes sense once you count the number of concurrent brains against one account and see the ratio is wrong.",
        "fix": "A mandatory pre-flight count before any batch launch: enumerate live agent-run processes; if a long-running dispatcher is alive, either wait for a quiescent window or do the work inline. Consolidate multiple loops under a single scheduler running concurrency 1 (round-robin) so they never split the quota.",
        "verification": "The next batch launched after the always-on dispatcher was quiesced ran clean 6/6.",
        "rule": "Multiple agents share a model-provider quota, and the losing brain cannot degrade gracefully - it dies silently. Before ANY batch launch: count the live brains against one account, and if a dispatcher is already alive, either wait for a quiescent window or run inline. Signature: 'connection stalled 120s' plus 'service busy' on multiple tasks with confirmed AC power.",
        "related": ["INC-0010"],
    },
    {
        "id": "INC-0012",
        "title": "A loop's `git add -A` sweeps a human's uncommitted edits into a loop commit",
        "date": "2026-08-05",
        "classes": ["vcs-destruction", "concurrency"],
        "severity": "high",
        "status": "mitigated",
        "cost": "Two prose edits landed under a loop's commit message; content survived, history was mislabeled. It recurred every iteration until the pattern was noticed.",
        "signature": "`git log --oneline -S \"<a phrase you typed>\" -- <file>` shows your text landed in a commit whose SUBJECT is the loop's story.",
        "what": "A human hand-edited a documentation file in a directory the loop committed from. The loop's next iteration ran `git add -A` before its own commit and swept the human's uncommitted work into the loop's commit under the loop's subject line. Recurred every iteration.",
        "root_cause": "The git index is process-shared state. A blanket `add -A` stages EVERYTHING that has changed in the working tree, not only what the loop authored. If two writers (or an agent and a human) share the tree, whoever commits second commits both sets of edits.",
        "why_hard": "Content is preserved, tests are still green, no error. The only symptom is a wrongly-labeled commit subject. If you weren't looking, you'd never see it.",
        "fix": "Do not hand-edit a directory a loop commits from. If you must, drop the loop's STOP sentinel first. A path-limited commit (`git commit -m '...' -- <paths>`) protects the LOOP's work from a human's blanket add, but it CANNOT protect a human's work from the loop's blanket add - because the loop is the one running `add -A`. The full protection is exclusivity: quiesce one side before the other writes.",
        "verification": "After the human edit was staged into a proper quiesced window, the next 30 iterations shipped without sweeping any human file into a loop commit.",
        "rule": "The git index is process-shared. A blanket `git add -A` stages everything in the tree, including uncommitted work you did not author. When a loop is live: do not hand-edit its tree; if you must, drop the loop's STOP sentinel first. A path-limited commit protects the loop from you, not you from the loop.",
        "related": ["INC-0013", "INC-0014"],
    },
]


_BATCH2: list[dict] = [
    {
        "id": "INC-0013",
        "title": "add-then-commit is a shared-index race; use a path-limited commit",
        "date": "2026-08-03",
        "classes": ["vcs-destruction", "concurrency"],
        "severity": "high",
        "status": "fixed",
        "cost": "An entire in-flight iteration's changeset shipped under a human's out-of-band commit message. Non-destructive but history mislabeled.",
        "signature": "You ran `git add <paths>` followed by a separate `git commit` and the resulting commit contains files you never touched. Diff against your parent shows the loop's whole iteration.",
        "what": "A human ran add-then-commit-then-push in one shell line while a loop's final step was live. In the window between the add and the commit, the loop ran its own `git add -A`. The human's PATHLESS `git commit` then swept the entire loop iteration into the human's commit under the human's subject and pushed it. All content preserved; history mislabeled.",
        "root_cause": "The git index is process-shared state and a pathless commit commits whatever is staged AT THAT INSTANT, not what you originally staged. Any other writer to the same index between your add and your commit contributes its files to your commit.",
        "why_hard": "There is no error and every test still passes. The failure is invisible unless you diff the commit against its parent and notice files you did not touch.",
        "fix": "For any out-of-band write to a loop-owned repo, name the paths on the COMMIT itself, not on a separate add: `git commit -m 'msg' -- <paths>`. This bypasses the index entirely. Never amend or force-push to fix the mislabel while the loop is live (non-ff hazard) - either accept the cosmetic mess or repair during a quiescent window.",
        "verification": "The pattern was proven live: a subsequent out-of-band edit landed as a single-file commit even while the loop's final step was mid-run.",
        "rule": "The git index is process-shared: a pathless commit takes whatever is staged at that instant, not what you staged. For any out-of-band write to a repo another writer touches: name the paths on the commit itself (`git commit -m 'msg' -- <paths>`) rather than doing add-then-commit. Do not force-push while the loop is live.",
        "related": ["INC-0012", "INC-0014"],
    },
    {
        "id": "INC-0014",
        "title": "A revert-on-failure loop destroys uncommitted human work in a shared tree",
        "date": "2026-08-04",
        "classes": ["vcs-destruction"],
        "severity": "critical",
        "status": "mitigated",
        "cost": "Potential (avoided): uncommitted human work sat in a tree the loop was about to run. The failure path would have destroyed it with `git reset --hard origin/main`.",
        "signature": "A loop is enabled that commits from a working directory where another writer has uncommitted changes. The loop's failure path is a full reset to the remote head.",
        "what": "A build loop's failure handler was `git reset --hard origin/main && git clean -fd` - a fine idempotent reset for the loop's own tree, but catastrophic if any human uncommitted work happened to be in the same tree. A parallel session had staged design edits there.",
        "root_cause": "The loop's revert-to-remote is a legitimate safety mechanism for the LOOP's state. It cannot distinguish loop-authored dirt from human-authored work-in-progress: both are 'uncommitted files under this tree'.",
        "why_hard": "The reset is designed to be aggressive. It has no notion of ownership.",
        "fix": "The correct protection is a per-team STOP sentinel that pauses ONE team without disabling it. The sentinel must name (a) the owner, (b) the exact files at risk, (c) an explicit lift condition, (d) whether a dispatcher restart is required to lift it. Sentinels are polled every round (instant effect); the `enabled` flag is read only at dispatcher startup (needs a restart). Never take an ownership decision by editing the enabled flag; use STOP to pause and enabled to remove.",
        "verification": "Before lifting any protective STOP, re-verify the stated lift condition in the SAME command that removes the STOP (e.g. `git status --porcelain` empty AND HEAD == origin/main immediately before `rm STOP`). The tree can go dirty again between a survey and the action.",
        "rule": "A loop's revert-to-remote cannot distinguish loop dirt from human work-in-progress. Guard shared trees with a per-team STOP sentinel that names owner, files at risk, lift condition and whether restart is needed. Sentinels are polled every round; the enabled flag needs a restart. Verify the lift condition in the SAME command that removes it.",
        "related": ["INC-0012", "INC-0013"],
    },
    {
        "id": "INC-0015",
        "title": "Git identity leak: real name via ambient global config",
        "date": "2026-07-31",
        "classes": ["vcs-destruction"],
        "severity": "critical",
        "status": "fixed",
        "cost": "Three public repos published every commit under the author's real name for weeks before the leak was noticed; a subsequent rewrite required force-push across the history.",
        "signature": "`git log --all --format='%an <%ae>'` on any repo shows an identity string you did not consciously set for THAT repo.",
        "what": "A repo-local `user.email` was set to a privacy-safe noreply address. `user.name` was not - it inherited the global default, which was the author's legal name. Every commit went out under the real name, publicly, until noticed. Making the repo public exposed ALL history at once.",
        "root_cause": "Two fields, one guarded. Overriding one identity field does NOT stop the other from leaking. The mistake compounded because the global default itself had been set by machine provisioning to an employer identity - so any repo LACKING a local email override leaked the employer email into personal work.",
        "why_hard": "Everything looks fine at the file level. `git commit -m ...` works. GitHub renders the commits. The leak is only visible if you scan the identity strings across the whole history.",
        "fix": "For any repo destined to be public, set BOTH repo-local `user.name` (to a public handle) AND `user.email` (id-anchored noreply) BEFORE the first commit. Verify with `git log --all --format='%an <%ae>' | sort -u`. Machine-wide, flip the global default to a privacy-safe identity and use a `[includeIf 'gitdir:...']` block for work directories - noting that `includeIf` matches the SYMLINK-RESOLVED path, so use the real path, not the alias. For an already-exposed repo, `git filter-repo --mailmap` rewrites identity metadata cleanly, but the SHAs change (force-push required) and the real name may ALSO live in file CONTENT (LICENSE, pyproject) - scrub both in one pass.",
        "verification": "After the rewrite: `git grep -i <name> $(git rev-list --all)` returns nothing across the whole history. Re-verify from a FRESH clone, not just the local working repo.",
        "rule": "For any repo destined to be public, set BOTH repo-local `user.name` AND `user.email` (to a public handle and id-anchored noreply) BEFORE the first commit. Verify with `git log --all --format='%an <%ae>'`. A noreply email alone does not stop the ambient global name from leaking. An `includeIf` gitdir must be the REAL path, not a symlink.",
        "related": ["INC-0018"],
    },
    {
        "id": "INC-0016",
        "title": "Anti-delegation clause must forbid 'scaffold a loop' too",
        "date": "2026-08-05",
        "classes": ["delegation"],
        "severity": "high",
        "status": "mitigated",
        "cost": "A fan-out subagent produced no deliverable and exited 0, so the parent runner recorded 'done' with an empty artifact.",
        "signature": "A subagent instructed to do work returns quickly and successfully, but the expected output file is empty or missing. Meanwhile a new nested loop or a prd.json / prompt.md scaffold appears alongside.",
        "what": "A subagent carrying a verbatim 'do not spawn nested agents' clause did not spawn a nested agent - it SCAFFOLDED a background ralph-style loop in a workspace directory and LAUNCHED it detached, then exited 0. The parent's completion check treated the exit code as success and moved on. Nothing was actually built by the subagent itself.",
        "root_cause": "The subagent read 'do not spawn an agent' as literally 'do not call agent_run in this call'. Scaffolding a loop that later spawns agents was not covered by the letter of the rule.",
        "why_hard": "The rule was in place, the subagent honored the rule as written, and it still produced nothing. The failure lives in the gap between the rule's letter and its intent.",
        "fix": "The anti-delegation clause must forbid EVERY escape hatch by name: nested agent invocations, scaffolding a loop (any framework), writing a prd.json / prompt.md / progress.txt, launching a detached process, handing off to a future iteration, or deferring the work. The instruction must appear INLINE in the subagent's task string, not merely referenced. After killing an unauthorized loop, remove its REQUIRED INPUT (e.g. delete the scaffolded prd.json) - killing a pid is not durable against a re-parenting supervisor.",
        "verification": "Subsequent subagents with the expanded clause completed the work themselves and produced the required output. The killed detached loop stayed dead once its input file was gone.",
        "rule": "A subagent reads 'do not spawn a nested agent' literally. Forbid every escape hatch by name in the SAME clause: nested agents, scaffolding a loop, writing prd/prompt/progress files, launching detached processes, handing off to a future iteration. Include the clause INLINE, not by reference. Kill an unauthorized loop by removing its required input, not just its pid.",
        "related": ["INC-0017"],
    },
    {
        "id": "INC-0017",
        "title": "A killed detached loop resurrects with a new PPID",
        "date": "2026-08-05",
        "classes": ["delegation", "ipc-and-env"],
        "severity": "medium",
        "status": "fixed",
        "cost": "About 90 minutes of confusion after a kill; the loop came back detached and continued producing unauthorized output.",
        "signature": "You kill the loop's pid. Later, `ps` shows a fresh pid with ppid 1, running the same loop script, on a new sleep-backoff cycle.",
        "what": "A detached loop was killed via SIGTERM against its pid. Around 90 minutes later a new pid appeared for the same script, reparented to init (ppid 1), alive and in a sleep-backoff cycle. It had been restarted by a scheduled task or a supervisor script the operator did not know about.",
        "root_cause": "The loop was reachable from more than one launcher. The kill removed the running process but not the source that spawned it. Reparenting to init is a healthy pattern for a well-behaved daemon, so nothing was 'wrong' - the operator simply hunted the wrong controller.",
        "why_hard": "There is often no visible link between the killed pid and its next incarnation. Watching `ps -ef | grep <script>` misses the launcher.",
        "fix": "The durable off switch is removing the REQUIRED INPUT the loop reads at the top of every iteration - a STOP file the script honors, or the story queue it consumes. This forces a graceful exit rather than trying to out-kill a re-spawner. Look for the launcher: (a) same argv on the restarted process = something is auto-resurrecting it (search cron, launchd/systemd, supervisor scripts); (b) different argv = a human or another session deliberately relaunched with new parameters. THAT diff is the tell.",
        "verification": "After the STOP file was in place, the next restart honored it and exited cleanly on its own.",
        "rule": "To stop a well-behaved detached loop, remove the input it polls (a STOP file it honors), not just its pid - a supervisor or scheduler can re-launch a killed pid. Same argv on a new pid = auto-resurrection; different argv = a fresh authorized launch. Hunt the launcher accordingly, and leave a documented STOP so you and the other session do not fight over the process.",
        "related": ["INC-0016"],
    },
    {
        "id": "INC-0018",
        "title": "Fail-open detector: pipe alternation matches nothing under one regex flavor",
        "date": "2026-08-05",
        "classes": ["detector-fail-open"],
        "severity": "high",
        "status": "fixed",
        "cost": "The credential-expiry branch of a watchdog could never have fired for the several days it was live - so a real credential outage would not have been caught.",
        "signature": "A monitor built on `grep -E 'A\\|B'` or `grep 'A\\|B'` prints nothing while the eye clearly sees both patterns in the log. A negative result is being read as health.",
        "what": "A watchdog used shell grep with escaped-pipe alternation (`\\|`) as its match pattern. In this shell, `grep` was aliased to ripgrep. Ripgrep is regex-by-default and reads `\\|` as an escaped LITERAL pipe - not as alternation. The pattern returned zero hits on inputs that clearly contained both alternatives.",
        "root_cause": "Two shell-tool assumptions differed. BSD grep (macOS default) uses BRE, where `\\|` is alternation only with `-E`. Ripgrep uses ERE-shaped regex by default and treats `\\|` as a literal. The single-backslash form is a footgun that reads correctly to a human familiar with only one of the two flavors.",
        "why_hard": "A negative result from a matcher is indistinguishable from health. Nothing errors, nothing warns.",
        "fix": "Use plain `|` for alternation, never `\\|`. Do not rely on `-E` to mean 'extended regex' - in some tools it means something else entirely (e.g. `--encoding` in ripgrep). Match case correctly or pass `-i`. And the durable practice: for any detector or alarm, feed it a known-bad sample and assert it fires BEFORE trusting it. Fail-open monitoring is worse than none.",
        "verification": "A synthetic 'credential refresh failed' line in a tmp file caused the fixed matcher to fire; the same line under the old pattern was silent. Two-sided self-test now runs before every alarm cycle.",
        "rule": "A negative result from a detector is NOT evidence of health. Every alarm must be proven against a KNOWN-BAD sample before it is trusted (fires) and against a known-good sample (does not fire). Fail-open monitoring is worse than none. And know your regex flavor: `\\|` is alternation in BRE but a LITERAL pipe in ripgrep - use plain `|`.",
        "related": ["INC-0019"],
    },
    {
        "id": "INC-0019",
        "title": "Fail-open detector: parsing the wrong column reports healthy",
        "date": "2026-08-05",
        "classes": ["detector-fail-open", "observability"],
        "severity": "high",
        "status": "fixed",
        "cost": "Nearly logged 'auth OK' during a period when the long-lived credential had actually expired ~180 minutes earlier.",
        "signature": "A cookie- or config-file parser produces empty output that reads as 'nothing to report' when in fact every row is unparseable because the code is reading the wrong field.",
        "what": "A watchdog parsed a cookie file where each line has seven tab-separated fields. The code read the expiry from field 7 - which is the VALUE, not the expiry. Every numeric parse failed silently and the summary printed nothing. That silence was almost logged as 'auth is fine'.",
        "root_cause": "Two errors on the same file. First, expiry is field 5 of 7 in the Netscape cookie format, not field 7. Second, some lines are prefixed with `#HttpOnly_` which must be stripped BEFORE the leading-`#` comment skip, or the real rows are silently dropped.",
        "why_hard": "Empty output is the SAME visual outcome as a clean run. Detectors that fail silently by reporting nothing look identical to detectors that pass.",
        "fix": "Sanity-check every parser by asserting that its long-lived rows come back with PLAUSIBLE values - remaining-time of ~150 days for a long-lived config token, ~270 days for another, and so on. If every row is unparseable, you have the wrong column. Never print raw cookie values, only names plus remaining-minutes.",
        "verification": "With field 5 read correctly, the parser surfaced two long-expired credentials that had been invisible for days. A regression test asserts that a known-good file returns non-trivial data.",
        "rule": "A parser that fails silently by returning nothing is indistinguishable from a healthy sample. Sanity-check every parser by asserting that its rows come back with PLAUSIBLE values; if every row is unparseable, you have the wrong column, not a healthy system. Never make an alarm's positive answer look like its negative answer.",
        "related": ["INC-0018"],
    },
    {
        "id": "INC-0020",
        "title": "A steering channel counts only when the consumer's own parser emits it",
        "date": "2026-08-06",
        "classes": ["steering-channel"],
        "severity": "medium",
        "status": "fixed",
        "cost": "Two products' pinned steering heads were silently truncated for hours while the operator believed the guidance had been delivered.",
        "signature": "You wrote the steering text into the right file with the right words. The next iteration's behavior shows no evidence the agent read it.",
        "what": "A learnings-digest function was supposed to inject a pinned 'Patterns' head verbatim into every agent's prompt. An operator wrote a directive as `- [OPERATOR ...]`. That form is TRIPLY broken: it parses as a chronological lesson (excluded from the head), it terminates the head at that line (decapitating every bullet below), and it lands in a bounded newest-N window where a top-of-file insert is the OLDEST and gets dropped.",
        "root_cause": "The digest was character-bounded, item-count-limited, and had a specific parser for the head that treated `- [` as the start of a lesson. The steering channel had ITS OWN parser and format; writing to it in a slightly-wrong format meant the consumer's parser did not deliver the intended text.",
        "why_hard": "The file on disk looks correct to the operator. The distinction is entirely in the consumer's parser.",
        "fix": "For any steering channel: verify by importing and CALLING the consumer's own parser, then asserting your marker is in the output AND that the head still delivers its expected other bullets. Do not eyeball the file. Use `- **OPERATOR ...**` (bold, not brackets) under the `## Patterns` heading, never `- [...]` (which parses as a lesson).",
        "verification": "After the format fix, a parser call confirmed the directive was in the emitted head and the other pinned bullets were still present at full length.",
        "rule": "A steering channel counts as delivered only when the CONSUMER's own parser emits it - verify by calling that parser, not by inspecting the file. Know its rules: item budget, character budget, format markers. Read the limit in the version ACTUALLY RUNNING, not the newest source. Bound anything injected into every prompt by CHARACTERS, cap at write time, and check what survives.",
        "evidence": [
            'https://github.com/jeffma8888/agent-foundry - the consumer parser is `learnings_digest` in `foundry.py`; the delivery bounds are `PROMPT_LEARNINGS_HEAD_BULLET_CHARS` and `PROMPT_LEARNINGS_HEAD_BUDGET_CHARS`, and the digest emits its own elision notice, which is what makes a dropped steering bullet greppable instead of silent.',
        ],
        "related": ["INC-0004"],
    },
    {
        "id": "INC-0021",
        "title": "Stale module import: 'shipped' is not 'live'",
        "date": "2026-08-10",
        "classes": ["stale-module", "observability"],
        "severity": "high",
        "status": "mitigated",
        "cost": "Twenty-six commits to a shared module were reported as SHIPPED by git and the changelog while all of them were inert in the running process for four days.",
        "signature": "A long-running dispatcher's uptime is measured in days. `git log --since=<start>` on the module it imported shows dozens of commits since. The behavior on disk does not match what the process seems to be running.",
        "what": "In the public agent-foundry loop framework, the dispatcher process did a plain `import foundry` once at launch, with no `importlib.reload` and no self-restart. Over four days, 26 commits to `foundry.py` landed. All 26 were inert - the process was still running the code it imported at launch. Git, the roadmap and the decision log all reported them SHIPPED.",
        "root_cause": "Python's import machinery caches modules by name. Without an explicit reload or a process restart, `import foundry` returns the object bound at first import forever. Even a self-modifying loop that ships fixes to its own code does not run those fixes.",
        "why_hard": "Everything upstream reports success. The commits merged; the tests were green; the changelog says SHIPPED. Only a comparison of process start-time against git log for the imported module reveals the gap.",
        "fix": "For any long-running process that imports code it may also modify, ship a live-lag check: compare `psutil.Process(pid).create_time()` against `git log --since` for the imported module. Distinguish disk-level changes from live-behavior changes explicitly - role or prompt CARDS read from disk per run ARE live even when the module is frozen. Design self-updating loops with a scheduled restart or an in-process reload primitive, not on the assumption that the next iteration picks up new code.",
        "verification": "The live-lag check surfaced the four-day gap and warned before further inert commits accumulated. Post-restart, the same 26 commits took effect.",
        "rule": "A long-running process runs the code it imported AT LAUNCH. Merged is not shipped is not live: git can say 'landed' while the process is still on the old bytecode. Ship a live-lag check that compares process start-time against `git log --since` on the imported module. Role/prompt files read per-run ARE live even when the module is frozen - distinguish them.",
        "evidence": [
            'https://github.com/jeffma8888/agent-foundry - the dispatcher does a plain `import foundry` once at launch, with no reload primitive and no self-restart.',
            'Second confirmation, 2026-08-15: a live dispatcher with 1d22h uptime was still running the module revision it imported at launch while the repository head had moved on by many commits. Every prompt-budget constant measured from the working tree was therefore the wrong number for the running loop - so a stale module silently invalidates measurements taken about it, not just fixes shipped to it.',
        ],
        "related": ["INC-0007"],
    },
    {
        "id": "INC-0022",
        "title": "Test precondition on gitignored local state passes only on this machine",
        "date": "2026-08-11",
        "classes": ["test-isolation"],
        "severity": "high",
        "status": "fixed",
        "cost": "A ship went green and the post-release fresh-clone gate immediately went BROKEN, because the test asserted counts that were true only in the developer's working tree.",
        "signature": "A test passes locally on every developer machine, then fails immediately in a fresh CI clone. The diff between environments is directories or files gitignored by policy.",
        "what": "A test asserted that a `products/` directory held more than 6000 files. True in the working tree from gitignored per-iteration state and history; false in a fresh clone that had only the 4 tracked config files. Same trap for counts of iteration dirs, log files, LEARNINGS.md, or a repo directory basename.",
        "root_cause": "The test read AMBIENT filesystem state instead of building its own fixture. Ambient state was gitignored - which is the whole point of gitignore - so the fresh clone had no such state and the assertion failed.",
        "why_hard": "The test passes on every machine that has ever run the loop, because they all have the accumulated gitignored state. It only fails on a machine that has NEVER run the loop, which is exactly what CI is.",
        "fix": "Every ship is re-verified from a THROWAWAY FRESH CLONE. Before asserting on any path, ask whether git tracks it; if not, build the fixture in `tmp_path` instead of asserting on the ambient tree. Same trap for a repo directory's basename: assert on tracked file content, not on `os.path.basename(cwd)`.",
        "verification": "The test was rewritten to build its expected structure in tmp_path. It now passes in a fresh clone. A regression test asserts fresh-clone parity in CI.",
        "rule": "A test that reads ambient filesystem state depends on gitignored files a fresh clone does not have. Before asserting on a path, ask whether git tracks it; if not, build the fixture yourself in `tmp_path` instead of asserting on the ambient tree. A test that passes only on this machine is not a test.",
        "related": ["INC-0023"],
    },
    {
        "id": "INC-0023",
        "title": "CI shallow clone breaks tests that read git history",
        "date": "2026-08-04",
        "classes": ["test-isolation"],
        "severity": "medium",
        "status": "fixed",
        "cost": "Four consecutive CI builds went red on the same three tests, none caused by the commits under test. Local was green.",
        "signature": "Tests pass locally, fail in CI, and none of them are testing the code under review. The failures reference git-history-shaped values.",
        "what": "A collector shelled out to `git log -n 15` against a fixture inside the repo and a test asserted the emitted header contained '(15)'. In a CI shallow clone, `git log` returns 1 reachable commit, so the emitted header was '(1)' and the test failed. The local dev tree had 102 commits and the test passed there.",
        "root_cause": "CI's default checkout is depth-1 (a shallow clone). Any test that reads git history reads a different reality in CI than on a full clone.",
        "why_hard": "The failing tests have nothing to do with the commits under test - which makes 'my change broke it' the first false hypothesis, then 'CI is flaky' the second, and only 'CI's environment is different' the third.",
        "fix": "Set `fetch-depth: 0` on the CI checkout step. That is the correct default anyway - CI should mirror a real clone. The diagnostic recipe: `git clone --depth 1 file:///<local-repo> /tmp/sim && pytest` reproduces the failure; then `git fetch --unshallow` in the same clone makes it pass with zero source changes. That isolates environment divergence from a real code defect in one step.",
        "verification": "After `fetch-depth: 0`, the tests pass in CI. A guard test asserts the workflow file still has `fetch-depth: 0`.",
        "rule": "CI defaults to a depth-1 clone; any test that reads git history sees a different world there. Set `fetch-depth: 0`. Before blaming the commit under test, ask what CI's environment does NOT have: git history, tags, submodules, a TTY, network, timezone, locale. A synthetic depth-1 clone locally reproduces the failure in one step.",
        "related": ["INC-0022"],
    },
    {
        "id": "INC-0024",
        "title": "Backtick command substitution in a heredoc corrupts and executes",
        "date": "2026-08-05",
        "classes": ["tooling-paths", "vcs-destruction"],
        "severity": "high",
        "status": "fixed",
        "cost": "A subagent's technical study document lost every backticked citation (leaving empty `()` in about 9 places) and had ~380KB of progress-bar spam dumped into the middle, because one substitution actually ran and opened an auth browser.",
        "signature": "A file written via an UNQUOTED heredoc contains empty `()` where citations should be, has control characters or carriage-return spam, and `wc -l` disagrees wildly with byte size.",
        "what": "A subagent wrote a document via `cat > file <<EOF ... EOF` (unquoted delimiter). Every backticked citation was command-substituted away at write time. One substitution actually EXECUTED and opened a browser auth flow, which then dumped its progress-bar output into the middle of the document.",
        "root_cause": "In an UNQUOTED heredoc, the shell interpolates `${var}`, `$(cmd)` and backtick command substitutions. Backticks in content that looks like citations (`path.py:123`) become command substitutions and either delete the citation (empty output) or actually run something.",
        "why_hard": "The syntax looks like a simple write. The content that triggers it is the exact form documentation writers use for code references.",
        "fix": "For ANY file write containing backticks, use a QUOTED heredoc: `cat > file <<'EOF' ... EOF`. The single quotes on the opening delimiter disable ALL substitution. Verify agent-written files afterwards: scan for control characters, carriage returns, and empty backtick pairs. Prefer per-file outputs over one shared master doc that multiple writers append to - blast-radius scales linearly.",
        "verification": "After the quoted-heredoc convention took hold, subsequent multi-writer docs contained all citations intact. A pre-write assertion scans the intended payload for suspicious patterns.",
        "rule": "In an UNQUOTED heredoc, backticks and $() are executed by the shell - both corrupting file content and potentially running arbitrary commands. Use a QUOTED heredoc (`<<'EOF'`) for any write containing code citations, and verify the resulting file for control characters and empty `()` pairs afterwards. And nothing after the terminator on the same line.",
        "related": ["INC-0012"],
    },
    {
        "id": "INC-0025",
        "title": "Retrying a killed verification step without resumable evidence is one failure, not four chances",
        "date": "2026-08-15",
        "classes": ["stage-timeout", "verdict-token", "checkpoint"],
        "severity": "high",
        "status": "open",
        "cost": "No new loss to report: this is the measured residual of INC-0005, whose abort path has converted a finished, reviewed iteration into a total loss nine times.",
        "signature": "Every attempt of the same step fails identically, at the same duration, with the same short timeout log. The retry count in the logs looks like resilience, while the outcome is exactly the outcome of one attempt.",
        "what": "A verification/ship step runs under a hard per-step cap and is retried up to four times. Each retry restarts verification from zero, because the retry instruction deliberately does not read the previous attempt - a sound default, since the dominant failure leaves a log containing nothing but a timeout line. For most roles that is correct. For the verification step it is not: its artifact is EVIDENCE, and evidence about an unchanged tree is reusable. So the same full suite, the same audits and the same clean-clone re-run are recomputed on every attempt, against the same budget, with the same result.",
        "root_cause": "Retries are independent trials only when the failure is random. A deterministic over-budget step fails the same way every time, so N retries of one plan is a single experiment repeated N times. The framework had nowhere to record PARTIAL verification: the only state shared between attempts was the working tree, so no attempt could tell what an earlier one had already proved.",
        "why_hard": "A retry count reads as safety. The logs show four attempts rather than one, so the mechanism looks like it is working, and the wasted wall clock is charged to the cap rather than to the retry design. The natural fix is also a trap: letting the step write a 'partially verified' token re-creates the placeholder that INC-0005's ban existed to stop, because a progress marker living in the channel a parser reads as the verdict IS a placeholder verdict. The progress channel and the verdict channel have to be physically different things.",
        "fix": "Three parts, in the order that pays. (1) SHRINK THE CRITICAL PATH FIRST - resumption raises the ceiling, deleting work lowers the floor. Keep pre-ship only what is decisive or irreversible: the suite result, a status showing only intended changes, and any secret-leak scan, since a pushed secret cannot be unpushed. Move doc-accuracy checks, spec audits and clean-clone re-runs to the post-release check that already re-runs them, and demote nits to follow-ups. (2) GIVE THE STEP A RESUMABLE EVIDENCE LEDGER, outside the verdict channel: prose lines above the sentinel, each naming the check, its result, and a KEY identifying the exact input state it was computed against - the head commit plus a hash over the pending diff and every untracked file. On a retry, carry forward only the lines whose key still matches the tree and skip those checks; any mismatch voids the entire ledger. Unkeyed, a cached result is a false-green vector: it lets a retry ship on evidence gathered against a different tree. (3) MAKE 'KILLED' AND 'REFUSED' DIFFERENT ANSWERS. The runner already knows the attempt was killed, and that fact is discarded before the verdict is read. Treat a killed attempt holding no verdict as evidence about the MACHINE - retry, resume, do not destroy - and only an explicit refusal as evidence about the TREE.",
        "verification": "Not verified in production. Status is open, and the design is recorded before it ships rather than after. What IS measured, by reading the running system instead of its documentation: about 19,000 lines of framework code and 21 role cards contain no resumable-verification mechanism, no partial-verdict vocabulary and no evidence ledger of any kind; the retry instruction's own docstring states that it deliberately does not read the previous attempt; and the asymmetry part (3) asks for is ALREADY implemented one layer down, for a single sub-check whose 'could not complete' exit is explicitly treated as evidence about the machine rather than about the tree, on the stated grounds that a false revert destroys a whole green iteration. The principle was accepted in the small and never lifted to the layer that does the destroying. Acceptance test when it lands: force a kill mid-verification, assert the retry runs strictly fewer checks than the first attempt, and assert that a ledger whose key does not match the tree is discarded rather than trusted.",
        "rule": "A retry is a second chance only if something carried forward. Under a hard cap, N retries of a deterministic over-budget step is one failure repeated N times. Give the step a place to record partial results, key that record to the exact input state so a stale one is discarded, and keep it OUT of the channel a parser reads as the verdict.",
        "evidence": [
            "https://github.com/jeffma8888/agent-foundry - `MAX_ATTEMPTS` and `retry_directive` in `foundry.py` (the retry text states in its own docstring that it deliberately does not read the previous attempt), the verify-first exception in `roles/final.md`, and the pre-ship clone gate whose 'could not complete' exit code is already treated as evidence about the machine rather than the tree - the asymmetry part (3) asks to be generalized.",
        ],
        "related": ["INC-0002", "INC-0005", "INC-0006"],
    },
]

INCIDENTS: list[dict] = _BATCH1 + _BATCH2

# ---------------------------------------------------------------------------
# PRACTICES: cross-incident best practice.
#
# An incident is one failure that happened. A practice is what to DO by
# default, distilled from several of them. Kept separate because the evidence
# is different in kind: an incident cites a date and a root cause, a practice
# cites the incidents it generalizes. `derived_from` is validated against
# INCIDENTS, so a practice can never claim evidence that is not in the corpus.
# ---------------------------------------------------------------------------
PRACTICES: list[dict] = [
    {
        "id": "PRA-0001",
        "title": "The enforcement ladder: pick the cheapest rung that makes the failure impossible",
        "practice": (
            "Any requirement can be enforced at five strengths: a skill doc, an always-injected policy "
            "line, an agent self-report token, a deterministic harness check, or structural "
            "impossibility. Cost AND reliability both rise going down. Enforce at the cheapest rung "
            "that makes the failure impossible rather than merely unlikely, and move a requirement one "
            "rung DOWN every time it is violated. A rule that has failed twice as prose belongs in code."
        ),
        "why": (
            "Teams argue about the wording of a rule that keeps being broken, when the wording was never "
            "the problem: the rule was installed at a rung that cannot enforce it. The ladder makes the "
            "argument concrete, because it replaces 'say it more firmly' with 'move it down one rung'. "
            "The second half of the rule is the operational half. A violation is not a discipline "
            "failure, it is evidence that the current rung is too weak for this requirement, and the "
            "correct response is a migration rather than a reminder."
        ),
        "derived_from": ["INC-0005", "INC-0013", "INC-0016", "INC-0018"],
    },
    {
        "id": "PRA-0002",
        "title": "Classify a control by its enforcement point, never by its medium",
        "practice": (
            "Harness, policy, guardrail and skill are separated by ENFORCEMENT POINT, not by medium. Ask "
            "what happens when the model ignores it: if nothing happens it was guidance, if the action is "
            "blocked or reverted it was a guardrail. Code the agent can edit mid-run is not harness; a "
            "human approval queue containing no code is. The test is whether the agent can change it or "
            "route around it inside the run."
        ),
        "why": (
            "Three of the four layers are commonly shipped as prose loaded into a context window, so "
            "describing them by medium collapses them and lets a team believe it has reliability "
            "engineering when it has persuasion. Classifying by enforcement point also predicts the "
            "failure signature, which is what makes it useful during an outage rather than only in a "
            "design review: harness failures crash, policy failures are undelivered or unheeded, "
            "guardrail failures are fail-open or fail-closed on a wrong spec."
        ),
        "derived_from": ["INC-0020", "INC-0021"],
    },
    {
        "id": "PRA-0003",
        "title": "Six conditions for a gate that cannot be skipped",
        "practice": (
            "A gate runs always only if ALL six hold: its call site is in the harness and not in the "
            "prompt; invocation is unconditional; the default is fail-closed; the evidence is produced "
            "by the harness rather than reported by the agent; the gate sits outside the surface the "
            "agent can edit; and it has been proved two-sided against a known-bad sample. Drop any one "
            "and the gate silently becomes advisory."
        ),
        "why": (
            "Every one of the six has its own incident behind it, which is why the list is six items and "
            "not a slogan. The one most often missed is the last: an unproven detector may be fail-open, "
            "and a fail-open gate reports health forever, so absence of alarm is not evidence of safety. "
            "The one most often rationalized away is the fifth, because keeping the gate outside the "
            "agent's reach is inconvenient exactly when the agent is productive."
        ),
        "derived_from": ["INC-0005", "INC-0018", "INC-0019"],
    },
    {
        "id": "PRA-0004",
        "title": "Choose the constraint surface before choosing the enforcement strength",
        "practice": (
            "Before arguing determinism versus capability, pick the CONSTRAINT SURFACE. Clamp the "
            "narrowest axis that makes the failure impossible AND is orthogonal to the capability you "
            "are paying for: output form, actions, blast radius, resources, the oracle, information, or "
            "identity - never the reasoning. Test: if clamping this axis to fully deterministic loses the "
            "reason you hired the model, it is the wrong axis. An apparent determinism-versus-capability "
            "trade-off is usually evidence of a coupled surface, not a law."
        ),
        "why": (
            "The strength question has five answers and the surface question has ten, so surface "
            "selection carries more of the design, yet it is the step that gets skipped. Eight of the ten "
            "surfaces are decidable in code and seven of those cost the model's usefulness nothing, so "
            "the space of free total guarantees is far larger than a code-versus-prompt framing suggests. "
            "The canonical mis-selection: enforcing 'do not leak personal data' as a regex over the "
            "output (a content filter, downstream of the leak, blind to whatever it cannot match) when "
            "the information surface makes it impossible - you cannot leak what you were never given. "
            "What genuinely survives in the undecidable half is a prevention-versus-recovery trade, not "
            "a determinism-versus-capability one, and recovery is systematically underpriced."
        ),
        "derived_from": ["INC-0014", "INC-0018", "INC-0024"],
    },
]

