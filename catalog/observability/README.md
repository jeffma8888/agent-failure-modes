# observability

[Catalog](../README.md) / observability

The signal you trust hides the truth: an outcome flag masks a chronically over-budget step, a lifetime average hides a spike, a hardened process reports zero usage.

**Ask:** Are you reading a distribution or a single number, a delta or a lifetime average - and could the measurement itself be denied?

43 incidents filed here (43 occurrences); 56 more filed elsewhere are also tagged observability.

## Incidents

This class has no topics, so this node is the leaf. Ordered by occurrences, then severity, then id.

### [INC-0039](../../incidents/INC-0039-a-budget-is-not-a-sample-a-sorted-head-is-a-permanent-filter.md) - A budget is not a sample: a sorted head is a permanent filter, disguised as a performance knob
- occurrences 1, severity high, status fixed
- **Signature:** A bounded pass reports steady healthy throughput, but its OUTPUT is concentrated in one region of the input space - and that region is the one that sorts first.
- **Rule:** For ANY truncated pass, ask whether the ORDER is independent of the PROPERTY being measured. Filename, insertion, directory and id order almost never are - so a sorted head is a permanent filter wearing a performance knob's clothes. Round-robin across the dimension you care about, best-first inside each bucket, and give unclassifiable items their own bucket.

The 42 entries below are listed by title only so this node stays under 12 KB. Open the page, or run `python3 tools/afm.py show INC-XXXX`, for its signature and rule.

- [INC-0041](../../incidents/INC-0041-a-verifier-that-lived-and-answered-can-still-deliver-an-unus.md) - A verifier that lived and answered can still deliver an unusable verdict (n=1, high)
- [INC-0007](../../incidents/INC-0007-diagnose-stalled-work-from-the-duration-distribution-not-the.md) - Diagnose stalled work from the duration distribution, not the outcome (n=1, medium)
- [INC-0036](../../incidents/INC-0036-a-relaunch-that-bypasses-the-canonical-launcher-runs-healthy.md) - A relaunch that bypasses the canonical launcher runs healthy but unobservable, and the diagnostic inverts (n=1, medium)
- [INC-0053](../../incidents/INC-0053-a-command-line-agent-silently-ran-an-older-model-than-assume.md) - A command-line agent silently ran an older model than assumed and ignored an explicit model override (n=1, medium)
- [INC-0073](../../incidents/INC-0073-a-bundled-retry-worked-and-the-fix-was-credited-to-looking-l.md) - A bundled retry worked and the fix was credited to 'looking like a normal browser', which was wrong in every case tested (n=1, medium)
- [INC-0144](../../incidents/INC-0144-expected-lifecycle-refusals-were-mixed-with-static-findings.md) - Expected lifecycle refusals were mixed with static findings in a sweep (n=1, medium)
- [INC-0146](../../incidents/INC-0146-a-truncated-fast-run-stopped-at-the-first-red-stage-and-unde.md) - A truncated FAST run stopped at the first red stage and understated the stage sum by about half (n=1, medium)
- [INC-0227](../../incidents/INC-0227-a-retry-wrapper-logged-the-dependency-stderr-privately-and-s.md) - A retry wrapper logged the dependency stderr privately and starved the caller diagnosis (n=1, medium)
- [INC-0231](../../incidents/INC-0231-a-measurement-was-at-risk-of-coming-from-an-overlay-in-a-scr.md) - A measurement was at risk of coming from an overlay in a scratch tree (n=1, medium)
- [INC-0254](../../incidents/INC-0254-raw-evidence-was-deleted-with-the-scratch-area.md) - Raw evidence was deleted with the scratch area (n=1, medium)
- [INC-0274](../../incidents/INC-0274-write-times-from-a-command-output-not-from-memory.md) - Write times from a command output, not from memory (n=1, medium)
- [INC-0358](../../incidents/INC-0358-a-restated-rule-gained-a-qualifier-the-original-ruling-never.md) - A restated rule gained a qualifier the original ruling never had (n=1, medium)
- [INC-0494](../../incidents/INC-0494-the-first-real-click-around-found-product-defects-that-many.md) - The first real click-around found product defects that many static review rounds and every gate had missed (n=1, medium)
- [INC-0562](../../incidents/INC-0562-the-first-real-run-of-a-new-egress-observer-on-unchanged-mai.md) - The first real run of a new egress observer on unchanged main caught the dev server phoning home, and the agent stopped instead of widening the allowlist (n=1, medium)
- [INC-0586](../../incidents/INC-0586-a-waiter-whose-helper-could-not-open-its-guard-spun-to-the-w.md) - A waiter whose helper could not open its guard spun to the wait limit with tracebacks, and a malformed owner record was skipped silently (n=1, medium)
- [INC-0350](../../incidents/INC-0350-time-stamps-written-from-an-estimate-ran-ahead-of-the-clock.md) - Time stamps written from an estimate ran ahead of the clock (n=1, low)
- [INC-0373](../../incidents/INC-0373-two-replies-were-stamped-with-times-ahead-of-the-clock.md) - Two replies were stamped with times ahead of the clock (n=1, low)
- [INC-0381](../../incidents/INC-0381-a-whole-tree-content-digest-detected-a-dependency-change-but.md) - A whole-tree content digest detected a dependency change but could not say which file (n=1, low)
- [INC-0383](../../incidents/INC-0383-a-ruling-was-stamped-four-minutes-ahead-of-the-clock-because.md) - A ruling was stamped four minutes ahead of the clock because the time was written before the clock was read (n=1, low)
- [INC-0384](../../incidents/INC-0384-the-lead-stamped-a-brief-four-minutes-ahead-of-the-clock-aga.md) - The lead stamped a brief four minutes ahead of the clock again, one round after the same correction (n=1, low)
- [INC-0406](../../incidents/INC-0406-two-load-readings-around-a-sub-second-run-were-equal-because.md) - Two load readings around a sub-second run were equal because the host load average updates on a fixed interval (n=1, low)
- [INC-0415](../../incidents/INC-0415-a-ruling-timestamp-was-written-from-an-estimate-and-correcte.md) - A ruling timestamp was written from an estimate and corrected minutes later, twice in one round (n=1, low)
- [INC-0442](../../incidents/INC-0442-the-lead-wrote-a-ruling-timestamp-before-reading-the-clock.md) - The lead wrote a ruling timestamp before reading the clock (n=1, low)
- [INC-0456](../../incidents/INC-0456-the-lead-wrote-ruling-timestamps-from-memory-three-times-and.md) - The lead wrote ruling timestamps from memory three times and had to correct them (n=1, low)
- [INC-0470](../../incidents/INC-0470-a-count-change-in-an-acceptance-document-was-attributed-to-s.md) - A count change in an acceptance document was attributed to specific items without a per file check (n=1, low)
- [INC-0478](../../incidents/INC-0478-a-guard-that-blocked-every-network-attempt-logged-only-the-a.md) - A guard that blocked every network attempt logged only the API name, so a second run was needed to learn the target (n=1, low)
- [INC-0488](../../incidents/INC-0488-static-review-rounds-on-a-test-harness-left-the-same-finding.md) - Static review rounds on a test harness left the same findings open (n=1, low)
- [INC-0491](../../incidents/INC-0491-a-browser-walker-gathered-guards-over-many-static-rounds-unt.md) - A browser walker gathered guards over many static rounds until no allowed target could pass them (n=1, low)
- [INC-0509](../../incidents/INC-0509-an-agent-reported-a-background-run-as-running-from-its-launc.md) - An agent reported a background run as running from its launch, but the task had only echoed a prompt and no test process existed (n=1, low)
- [INC-0510](../../incidents/INC-0510-mutation-restore-receipts-were-kept-only-in-tool-output-so-t.md) - Mutation restore receipts were kept only in tool output, so two independent reviewers could not verify restoration (n=1, low)
- [INC-0515](../../incidents/INC-0515-a-rulings-file-grew-past-what-a-reader-s-tool-returns-and-a.md) - A rulings file grew past what a reader's tool returns, and a read of a named range was clipped, so compliance could not be certified (n=1, low)
- [INC-0547](../../incidents/INC-0547-a-walker-harness-could-not-open-a-blank-autosave-draft-from.md) - A walker harness could not open a blank autosave draft from the list because its name link had no text, and a second selector matched three links (n=1, low)
- [INC-0555](../../incidents/INC-0555-a-load-average-of-176-was-read-as-cpu-demand-while-no-proces.md) - A load average of 176 was read as CPU demand while no process used more than one core, because the number counts waiting work and lags (n=1, low)
- [INC-0567](../../incidents/INC-0567-heading-times-in-several-rulings-and-briefs-ran-thirty-to-se.md) - Heading times in several rulings and briefs ran thirty to seventy minutes ahead of the real clock (n=1, low)
- [INC-0570](../../incidents/INC-0570-two-lead-rulings-narrated-facts-that-git-disagreed-with-and.md) - Two lead rulings narrated facts that git disagreed with, and the corrections were appended after checking git (n=1, low)
- [INC-0579](../../incidents/INC-0579-a-broad-any-alert-selector-matched-the-framework-s-empty-rou.md) - A broad any-alert selector matched the framework's empty route announcer before any action, and a second whole-document probe found the real refusal messages in toasts (n=1, low)
- [INC-0606](../../incidents/INC-0606-ruling-labels-written-from-an-estimated-clock-ran-up-to-six.md) - Ruling labels written from an estimated clock ran up to six minutes ahead of the real clock (n=1, low)
- [INC-0611](../../incidents/INC-0611-a-time-label-was-written-in-the-same-script-that-read-the-cl.md) - A time label was written in the same script that read the clock afterwards, minutes after a rule to read the clock first was recorded (n=1, low)
- [INC-0613](../../incidents/INC-0613-a-time-label-was-typed-in-the-same-parallel-batch-of-calls-t.md) - A time label was typed in the same parallel batch of calls that read the clock, so it was written before the clock was seen; the third recurrence (n=1, low)
- [INC-0617](../../incidents/INC-0617-a-ruling-quoted-a-clock-value-that-was-never-read-because-th.md) - A ruling quoted a clock value that was never read, because the write ran in the same parallel batch as the clock call; the fourth recurrence (n=1, low)
- [INC-0619](../../incidents/INC-0619-a-clock-label-slip-recurred-a-fifth-time-and-the-clock-call.md) - A clock label slip recurred a fifth time, and the clock call became the only call in its batch (n=1, low)
- [INC-0624](../../incidents/INC-0624-the-clock-call-ran-alone-in-its-own-message-yet-the-ruling-l.md) - The clock call ran alone in its own message, yet the ruling label was typed from expectation instead of copied from the returned value; the seventh recurrence (n=1, low)

## Also tagged observability

56 incidents filed under another home class also carry this class. Listed by the node where they live:

- [false-green](../false-green/README.md): INC-0028, INC-0031, INC-0042, INC-0062, INC-0202, INC-0228, INC-0239, INC-0244, INC-0247, INC-0252, INC-0253, INC-0259, INC-0266, INC-0273, INC-0283, INC-0310
- [spec-and-scope](../spec-and-scope/README.md): INC-0026, INC-0127, INC-0235, INC-0245, INC-0262, INC-0306, INC-0334, INC-0346, INC-0352
- [delegation](../delegation/README.md): INC-0091, INC-0128, INC-0201, INC-0206, INC-0263, INC-0317
- [detector-fail-open](../detector-fail-open/README.md): INC-0019, INC-0029, INC-0037, INC-0077, INC-0140, INC-0292
- [ipc-and-env](../ipc-and-env/README.md): INC-0049, INC-0059, INC-0068, INC-0325
- [concurrency](../concurrency/README.md): INC-0048, INC-0554, INC-0558
- [stage-timeout](../stage-timeout/README.md): INC-0002, INC-0195, INC-0210
- [detector-fail-closed](../detector-fail-closed/README.md): INC-0032, INC-0033
- [identity-and-keying](../identity-and-keying/README.md): INC-0027, INC-0054
- [stale-module](../stale-module/README.md): INC-0021, INC-0145
- [tooling-paths](../tooling-paths/README.md): INC-0060, INC-0081
- [test-isolation](../test-isolation/README.md): INC-0361

## Practices touching this class

- [PRA-0002](../CORE.md#practices) - Classify a control by its enforcement point, never by its medium
- [PRA-0003](../CORE.md#practices) - Six conditions for a gate that cannot be skipped
- [PRA-0005](../CORE.md#practices) - Admission control for an agent team on a shared host
