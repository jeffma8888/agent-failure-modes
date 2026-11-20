# A parser or pattern reads the wrong evidence

[Catalog](../README.md) / [detector-fail-open](README.md) / wrong-parser-or-pattern

**Go here if:** A detector sees nothing, matches injected text or classifies the wrong substring despite visible evidence.

**Rule:** Prove extraction and classification against actual-format records, malformed input and adversarial decoys inside the full failure boundary; require plausible parsed values and the exact intended output evidence before trusting silence or a match.

7 incidents, 7 occurrences. Ordered by occurrences, then severity, then id.

## Incidents

### [INC-0018](../../incidents/INC-0018-fail-open-detector-pipe-alternation-matches-nothing-under-on.md) - Fail-open detector: pipe alternation matches nothing under one regex flavor
- occurrences 1, severity high, status fixed
- **Signature:** A monitor built on `grep -E 'A\|B'` or `grep 'A\|B'` prints nothing while the eye clearly sees both patterns in the log. A negative result is being read as health.
- **Rule:** A negative result from a detector is NOT evidence of health. Every alarm must be proven against a KNOWN-BAD sample before it is trusted (fires) and against a known-good sample (does not fire). Fail-open monitoring is worse than none. And know your regex flavor: `\|` is alternation in BRE but a LITERAL pipe in ripgrep - use plain `|`.

### [INC-0019](../../incidents/INC-0019-fail-open-detector-parsing-the-wrong-column-reports-healthy.md) - Fail-open detector: parsing the wrong column reports healthy
- occurrences 1, severity high, status fixed
- **Signature:** A cookie- or config-file parser produces empty output that reads as 'nothing to report' when in fact every row is unparseable because the code is reading the wrong field.
- **Rule:** A parser that fails silently by returning nothing is indistinguishable from a healthy sample. Sanity-check every parser by asserting that its rows come back with PLAUSIBLE values; if every row is unparseable, you have the wrong column, not a healthy system. Never make an alarm's positive answer look like its negative answer.

### [INC-0029](../../incidents/INC-0029-when-a-check-reports-missing-content-the-extractor-is-the-fi.md) - When a check reports missing content, the extractor is the first suspect
- occurrences 1, severity high, status fixed
- **Signature:** The reported-missing content forms a clean PREFIX plus SUFFIX of the whole, instead of being scattered through the middle. Two different ways of counting the same units disagree.
- **Rule:** When a check reports missing content, suspect the extractor before the artifact: a false negative about content points at a destructive remedy. Count the units two ways (strict pattern versus loose structural) and let disagreement indict the measurement. Read the real format off disk before writing any repair, and never grade delegated work by a runner's success ledger.

### [INC-0077](../../incidents/INC-0077-keeping-an-error-prefix-did-not-keep-the-downstream-classifi.md) - Keeping an error prefix did not keep the downstream classification, and a free-text reason could carry markers or secrets
- occurrences 1, severity high, status mitigated
- **Signature:** New text is appended to a log line that a downstream classifier scans, on the argument that the line keeps its prefix.
- **Rule:** When output feeds a downstream classifier, test the classifier's verdict on it, not its prefix. Emit fixed categories instead of free text when the text could carry secrets or markers.

### [INC-0078](../../incidents/INC-0078-a-subprocess-wrapper-decoded-output-strictly-so-malformed-by.md) - A subprocess wrapper decoded output strictly, so malformed bytes skipped the retry and redaction path
- occurrences 1, severity medium, status fixed
- **Signature:** A wrapper runs an external command with strict text decoding, and every test feeds it clean strings.
- **Rule:** Put transport decoding inside the same failure boundary as the call, and test the boundary with a real process emitting malformed bytes, not only fakes returning clean text.

### [INC-0118](../../incidents/INC-0118-a-reason-regex-matched-text-the-test-itself-injected-and-mis.md) - A reason regex matched text the test itself injected and missed the reason on the error line
- occurrences 1, severity medium, status fixed
- **Signature:** A refusal assertion passes because its pattern matches the test input.
- **Rule:** Anchor a reason match to the error line and keep injected text out of its reach.

### [INC-0224](../../incidents/INC-0224-a-classifier-kept-a-legacy-pattern-list-beside-a-new-exact-s.md) - A classifier kept a legacy pattern list beside a new exact signature
- occurrences 1, severity medium, status fixed
- **Signature:** The legacy list still matched lookalikes.
- **Rule:** Probe a classifier extension with lookalike negatives
