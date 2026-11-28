# Missing evidence keeps findings unverified

[Catalog](../README.md) / [observability](README.md) / missing-or-unverifiable-receipts

**Go here if:** You cannot verify a finding from inspectable evidence of the actual run, and repeated inspection still leaves the same questions open.

**Rule:** Obtain inspectable evidence from a bounded diagnostic on the actual product instead of repeating inconclusive static reviews; preserve complete item-level logs and failure channels outside scratch state, verify launch artifacts and bound required reads so summaries never substitute for evidence.

13 incidents, 13 occurrences. Ordered by occurrences, then severity, then id.

## Incidents

### [INC-0041](../../incidents/INC-0041-a-verifier-that-lived-and-answered-can-still-deliver-an-unus.md) - A verifier that lived and answered can still deliver an unusable verdict
- occurrences 1, severity high, status mitigated
- **Signature:** A verifier reports a COUNT of failures in its summary line but the detail for the failing item is missing, and re-reading the stored log truncates at the same place.
- **Rule:** A verifier that answers is not a verifier that reported: transport AND the stored log can truncate at the same boundary, losing the finding entirely. Have the verifier write its full report to a FILE and reply with only the verdict table. A summary line asserting a count is a claim about findings, not a finding - never quote a partial trace as a result.

### [INC-0036](../../incidents/INC-0036-a-relaunch-that-bypasses-the-canonical-launcher-runs-healthy.md) - A relaunch that bypasses the canonical launcher runs healthy but unobservable, and the diagnostic inverts
- occurrences 1, severity medium, status fixed
- **Signature:** The process is alive with the right parent and the right arguments, but the log has no launch banner, and every freshness or liveness check that reads that log reports a problem. Restarting again reproduces the same silence.
- **Rule:** A launcher script is often part of the observability contract, not a convenience. Reproducing its command without its environment yields a process that works and cannot be seen, and every log-reading check then reports a failure that did not happen. Relaunch through the canonical entry point, and verify a restart by asserting the artifact your diagnostics read, not that the process exists.

### [INC-0144](../../incidents/INC-0144-expected-lifecycle-refusals-were-mixed-with-static-findings.md) - Expected lifecycle refusals were mixed with static findings in a sweep
- occurrences 1, severity medium, status fixed
- **Signature:** A sweep report cannot tell an intended refusal from a real finding.
- **Rule:** Report expected refusals apart from real findings.

### [INC-0227](../../incidents/INC-0227-a-retry-wrapper-logged-the-dependency-stderr-privately-and-s.md) - A retry wrapper logged the dependency stderr privately and starved the caller diagnosis
- occurrences 1, severity medium, status fixed
- **Signature:** A long outage was reported with an empty cause.
- **Rule:** A wrapper must preserve the failure channel of what it wraps, passing the last cause through on final failure.

### [INC-0254](../../incidents/INC-0254-raw-evidence-was-deleted-with-the-scratch-area.md) - Raw evidence was deleted with the scratch area
- occurrences 1, severity medium, status fixed
- **Signature:** Only extracted tables survived.
- **Rule:** Copy raw evidence and logs out of a scratch area before the cleanup runs

### [INC-0494](../../incidents/INC-0494-the-first-real-click-around-found-product-defects-that-many.md) - The first real click-around found product defects that many static review rounds and every gate had missed
- occurrences 1, severity medium, status mitigated
- **Signature:** A cheap exploratory run on a real build produced mismatches on every checklist row, within an hour of parking the strict tool.
- **Rule:** Run the real product early and often; a cheap exploratory run beats another review round of the tool that would run it.

### [INC-0381](../../incidents/INC-0381-a-whole-tree-content-digest-detected-a-dependency-change-but.md) - A whole-tree content digest detected a dependency change but could not say which file
- occurrences 1, severity low, status fixed
- **Signature:** A digest differed from the marker value and gave no hint which file changed.
- **Rule:** Record a marker-time file list as well as the whole-tree digest, so a change can be attributed to a file

### [INC-0478](../../incidents/INC-0478-a-guard-that-blocked-every-network-attempt-logged-only-the-a.md) - A guard that blocked every network attempt logged only the API name, so a second run was needed to learn the target
- occurrences 1, severity low, status fixed
- **Signature:** A blocking guard recorded what was called but not where.
- **Rule:** A blocking guard logs the API name, the full arguments and a stack trace on the first run, so one run is enough to classify the target.

### [INC-0488](../../incidents/INC-0488-static-review-rounds-on-a-test-harness-left-the-same-finding.md) - Static review rounds on a test harness left the same findings open
- occurrences 1, severity low, status mitigated
- **Signature:** Two static passes ended with the same four findings still open.
- **Rule:** When static review rounds on a harness converge slowly, run one labelled diagnostic early, on scratch state, with its result marked as neither a baseline nor an acceptance run, to learn what is really wrong.

### [INC-0491](../../incidents/INC-0491-a-browser-walker-gathered-guards-over-many-static-rounds-unt.md) - A browser walker gathered guards over many static rounds until no allowed target could pass them
- occurrences 1, severity low, status mitigated
- **Signature:** A diagnostic run packet showed the tool could not run against any allowed target.
- **Rule:** When a test tool's guards are reviewed in more rounds than the tool is run, run it or simplify it; a guard that no allowed target can pass is a defect.

### [INC-0510](../../incidents/INC-0510-mutation-restore-receipts-were-kept-only-in-tool-output-so-t.md) - Mutation restore receipts were kept only in tool output, so two independent reviewers could not verify restoration
- occurrences 1, severity low, status mitigated
- **Signature:** A reviewer asks for proof that a mutated file was restored, and the only record is output that was not saved.
- **Rule:** A mutation run keeps a receipt per mutant, the diff and the hash after restore, as a file before the scratch copy is deleted; tool output is not evidence a second reviewer can check.

### [INC-0515](../../incidents/INC-0515-a-rulings-file-grew-past-what-a-reader-s-tool-returns-and-a.md) - A rulings file grew past what a reader's tool returns, and a read of a named range was clipped, so compliance could not be certified
- occurrences 1, severity low, status mitigated
- **Signature:** An instruction requires reading a range of a file whose size exceeds what the reader tool returns.
- **Rule:** Do not require a read whose size exceeds what the reader tool returns; name the exact sections to read, and treat an unnamed old section as outside the compliance check.

### [INC-0666](../../incidents/INC-0666-a-reviewer-began-grading-from-partial-reads-a-file-view-clip.md) - A reviewer began grading from partial reads: a file view clipped in the middle and a criterion read only up to its waiver clause
- occurrences 1, severity low, status mitigated
- **Signature:** A file view shows an omission marker in the middle, or a grade is written for a criterion or section before its last clause and the requirement it cites have been read.
- **Rule:** Never grade from a partial read: if a view shows an omission marker or fewer bytes than the file holds, re-read in ranges until it is whole; read each criterion to its last clause, and open every requirement a section claims to satisfy, before writing a verdict on it.
