# A reassuring signal contradicts the underlying evidence

[Catalog](../README.md) / [observability](README.md) / misleading-metrics-and-status

**Go here if:** The reported result looks settled, but inspecting the actual target does not support what the signal or summary claims.

**Rule:** Verify operational claims against fresh, complete evidence for the exact target and tree; bind probes to the actual rendered elements and inspect distributions, effective metadata and causal attribution rather than trusting a convenient signal or summary.

13 incidents, 14 occurrences. Ordered by occurrences, then severity, then id.

## Incidents

### [INC-0039](../../incidents/INC-0039-a-budget-is-not-a-sample-a-sorted-head-is-a-permanent-filter.md) - A budget is not a sample: a sorted head is a permanent filter, disguised as a performance knob
- occurrences 2, severity high, status fixed
- **Signature:** A bounded pass reports steady healthy throughput, but its OUTPUT is concentrated in one region of the input space - and that region is the one that sorts first.
- **Rule:** For ANY truncated pass, ask whether the ORDER is independent of the PROPERTY being measured. Filename, insertion, directory and id order almost never are - so a sorted head is a permanent filter wearing a performance knob's clothes. Round-robin across the dimension you care about, best-first inside each bucket, and give unclassifiable items their own bucket.
- **Recurrences:**
  - 2026-11-26 - A design review's first sample of 48 citations left two sections under-covered; the reviewer's own per-section tally showed it. Citation samples are now tallied per section before the table is closed.

### [INC-0007](../../incidents/INC-0007-diagnose-stalled-work-from-the-duration-distribution-not-the.md) - Diagnose stalled work from the duration distribution, not the outcome
- occurrences 1, severity medium, status fixed
- **Signature:** The loop's per-step success rate looks healthy. But if you compute the median wall-clock per step, one specific step sits AT the hard cap.
- **Rule:** A success predicate defined as 'the output file exists' hides a chronically over-budget step. Report the DURATION DISTRIBUTION per step, not just the outcome, and compare against a sibling running the same pipeline on the same box - which cheaply falsifies 'the machine is slow' or 'the provider is throttling'.

### [INC-0053](../../incidents/INC-0053-a-command-line-agent-silently-ran-an-older-model-than-assume.md) - A command-line agent silently ran an older model than assumed and ignored an explicit model override
- occurrences 1, severity medium, status fixed
- **Signature:** A model setting is accepted without error, the tool answers normally, and nobody has read the model identifier from the response metadata.
- **Rule:** A model setting is verified only by the model ID in the response metadata. A flag that is accepted is not a flag that took effect, and a tool that falls back instead of failing makes every override unverifiable until you read the metadata.

### [INC-0073](../../incidents/INC-0073-a-bundled-retry-worked-and-the-fix-was-credited-to-looking-l.md) - A bundled retry worked and the fix was credited to 'looking like a normal browser', which was wrong in every case tested
- occurrences 1, severity medium, status mitigated
- **Signature:** Several changes go into one retry (new client, new User-Agent, cookie jar, form handling), the retry succeeds, and the summary names the change the agent expected to matter.
- **Rule:** When a bundled retry works, isolate the variable before naming the fix: a 200 confirms the bundle, not your story. Read robots.txt before retrying a site that refused, stop on a disallow, and treat a challenge page as a refusal: use an official API or hand the user the link.

### [INC-0146](../../incidents/INC-0146-a-truncated-fast-run-stopped-at-the-first-red-stage-and-unde.md) - A truncated FAST run stopped at the first red stage and understated the stage sum by about half
- occurrences 1, severity medium, status fixed
- **Signature:** A timing taken from a run that stopped early is used as a full measurement.
- **Rule:** Measure the complete run before claiming a budget.

### [INC-0231](../../incidents/INC-0231-a-measurement-was-at-risk-of-coming-from-an-overlay-in-a-scr.md) - A measurement was at risk of coming from an overlay in a scratch tree
- occurrences 1, severity medium, status fixed
- **Signature:** The figures had no tree behind them.
- **Rule:** Measure on the exact tree that carries the file and label every figure with its SHA

### [INC-0406](../../incidents/INC-0406-two-load-readings-around-a-sub-second-run-were-equal-because.md) - Two load readings around a sub-second run were equal because the host load average updates on a fixed interval
- occurrences 1, severity low, status fixed
- **Signature:** Two readings of host load were identical around a very short run.
- **Rule:** Equal load readings around a sub-second run are expected from the fixed update interval; record each as read, never copy

### [INC-0470](../../incidents/INC-0470-a-count-change-in-an-acceptance-document-was-attributed-to-s.md) - A count change in an acceptance document was attributed to specific items without a per file check
- occurrences 1, severity low, status fixed
- **Signature:** A count change was credited to rows with no per file evidence.
- **Rule:** State a count delta with its base commit, and attribute it to a row only after a per file check

### [INC-0509](../../incidents/INC-0509-an-agent-reported-a-background-run-as-running-from-its-launc.md) - An agent reported a background run as running from its launch, but the task had only echoed a prompt and no test process existed
- occurrences 1, severity low, status mitigated
- **Signature:** A background task exists and a launch was acknowledged, but no process of the run exists.
- **Rule:** Report a run as running only from its own output (a launch line, a PID that exists); a started task is not a started run.

### [INC-0547](../../incidents/INC-0547-a-walker-harness-could-not-open-a-blank-autosave-draft-from.md) - A walker harness could not open a blank autosave draft from the list because its name link had no text, and a second selector matched three links
- occurrences 1, severity low, status mitigated
- **Signature:** A list link has no accessible text, and a looser selector matches more than the one intended link.
- **Rule:** Reuse the exact recorded link instead of a looser selector, and record the element evidence for a link that cannot be clicked.

### [INC-0555](../../incidents/INC-0555-a-load-average-of-176-was-read-as-cpu-demand-while-no-proces.md) - A load average of 176 was read as CPU demand while no process used more than one core, because the number counts waiting work and lags
- occurrences 1, severity low, status mitigated
- **Signature:** A one-minute load average far above the core count while the per-process CPU list shows no process above one core.
- **Rule:** Before acting on a high load average, list the top processes by CPU with their owners; a load far above the core count with no process above one core is waiting work or lag, not CPU demand.

### [INC-0570](../../incidents/INC-0570-two-lead-rulings-narrated-facts-that-git-disagreed-with-and.md) - Two lead rulings narrated facts that git disagreed with, and the corrections were appended after checking git
- occurrences 1, severity low, status mitigated
- **Signature:** A ruling states a branch base or a new file that the commit history contradicts.
- **Rule:** Before stating a branch base or a new file in a ruling, read it from git; correct by an appended note.

### [INC-0579](../../incidents/INC-0579-a-broad-any-alert-selector-matched-the-framework-s-empty-rou.md) - A broad any-alert selector matched the framework's empty route announcer before any action, and a second whole-document probe found the real refusal messages in toasts
- occurrences 1, severity low, status mitigated
- **Signature:** A union selector matches an empty framework element before the action under test.
- **Rule:** Before authoring an error oracle, diff the whole document, including shadow roots, and bind the new element to the installed source.
