# detector-fail-open

[Catalog](../README.md) / detector-fail-open

A monitor or safety check silently never fires: a wrong regex flavor, the wrong parsed field, a case mismatch. A negative result is mistaken for health.

**Ask:** Have you fed this detector a known-bad sample and watched it fire, AND a known-good sample and watched it stay silent?

31 incidents filed here (31 occurrences); 20 more filed elsewhere are also tagged detector-fail-open.

## Incidents

This class has no topics, so this node is the leaf. Ordered by occurrences, then severity, then id.

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

### [INC-0596](../../incidents/INC-0596-an-observer-recorded-zero-denied-connects-while-it-also-miss.md) - An observer recorded zero denied connects while it also missed the server's database connect, so zero denied proved nothing
- occurrences 1, severity high, status mitigated
- **Signature:** A monitor reports zero violations and zero of an event that must occur.
- **Rule:** Before trusting a zero-violations monitor, require a positive control: a known event it must record in the process that makes it.

### [INC-0037](../../incidents/INC-0037-a-liveness-check-built-on-a-process-table-grep-counts-itself.md) - A liveness check built on a process-table grep counts itself
- occurrences 1, severity medium, status fixed
- **Signature:** A 'something is running' check is never false. The measured count is exactly one more than the truth, and it reads one at moments when you know for certain that nothing is running.
- **Rule:** A process-table grep counts itself - the measuring command's arguments contain the search term, so a 'something is running' check is never false. Use a matcher that excludes its own process, and prove any busy/idle check TWO-SIDED: zero when nothing runs, non-zero with one known worker. A check never seen returning false has not been tested.

### [INC-0069](../../incidents/INC-0069-a-gate-compared-the-candidate-commit-with-itself-because-a-l.md) - A gate compared the candidate commit with itself because a local clone redefines the remote-tracking ref
- occurrences 1, severity medium, status mitigated
- **Signature:** A check diffs against the main branch of the remote, and it runs in a fresh clone of a local checkout rather than of the real remote.
- **Rule:** A check that runs inside a clone must not rely on remote-tracking refs. State the baseline commit explicitly, and reproduce the ref topology in a scratch repo before trusting the check.

### [INC-0078](../../incidents/INC-0078-a-subprocess-wrapper-decoded-output-strictly-so-malformed-by.md) - A subprocess wrapper decoded output strictly, so malformed bytes skipped the retry and redaction path
- occurrences 1, severity medium, status fixed
- **Signature:** A wrapper runs an external command with strict text decoding, and every test feeds it clean strings.
- **Rule:** Put transport decoding inside the same failure boundary as the call, and test the boundary with a real process emitting malformed bytes, not only fakes returning clean text.

### [INC-0108](../../incidents/INC-0108-a-fail-closed-url-rule-copied-into-several-helpers-was-not-a.md) - A fail-closed URL rule copied into several helpers was not applied to every copy or every URL part
- occurrences 1, severity medium, status fixed
- **Signature:** One helper checks the host and another omits the database or port.
- **Rule:** One rule, every copy, every URL part.

### [INC-0113](../../incidents/INC-0113-a-rule-set-widened-by-tag-survived-dropping-one-tag-because.md) - A rule set widened by tag survived dropping one tag because only some tags had a planted violation
- occurrences 1, severity medium, status fixed
- **Signature:** A check covers several tags, and removing one tag leaves the suite green.
- **Rule:** Every tag in a rule needs its own planted violation.

The 21 entries below are listed by title only so this node stays under 12 KB. Open the page, or run `python3 tools/afm.py show INC-XXXX`, for its signature and rule.

- [INC-0118](../../incidents/INC-0118-a-reason-regex-matched-text-the-test-itself-injected-and-mis.md) - A reason regex matched text the test itself injected and missed the reason on the error line (n=1, medium)
- [INC-0129](../../incidents/INC-0129-a-syntax-hygiene-rule-flagging-every-literal-timer-over-one.md) - A syntax hygiene rule flagging every literal timer over one second also flagged a cancellation watchdog (n=1, medium)
- [INC-0140](../../incidents/INC-0140-a-known-red-was-listed-before-checking-the-scan-roots-of-the.md) - A known red was listed before checking the scan roots of the hygiene rule that raised it (n=1, medium)
- [INC-0141](../../incidents/INC-0141-a-static-watchdog-rule-accepting-only-an-inline-await-of-a-n.md) - A static watchdog rule accepting only an inline await of a new promise flagged stored promises and other valid shapes (n=1, medium)
- [INC-0142](../../incidents/INC-0142-a-redirect-test-searching-for-one-allowed-substring-accepted.md) - A redirect test searching for one allowed substring accepted a bad target beside a benign decoy (n=1, medium)
- [INC-0148](../../incidents/INC-0148-ascii-only-fixtures-could-not-tell-utf-16-code-unit-order-fr.md) - ASCII-only fixtures could not tell UTF-16 code unit order from UTF-8 byte order (n=1, medium)
- [INC-0150](../../incidents/INC-0150-a-missing-independently-callable-guard-lacked-protocol-cases.md) - A missing independently callable guard lacked protocol cases, and macOS path aliases looked like regressions (n=1, medium)
- [INC-0151](../../incidents/INC-0151-a-hygiene-rule-against-conditional-test-omission-needed-a-pr.md) - A hygiene rule against conditional test omission needed a precise flagged and allowed set (n=1, medium)
- [INC-0166](../../incidents/INC-0166-a-conditional-omission-could-hide-behind-a-helper-an-alias-o.md) - A conditional omission could hide behind a helper, an alias or an early return (n=1, medium)
- [INC-0176](../../incidents/INC-0176-a-shape-regex-was-used-as-ownership-evidence-for-a-sweep.md) - A shape regex was used as ownership evidence for a sweep (n=1, medium)
- [INC-0186](../../incidents/INC-0186-a-per-root-checker-summary-undercounted-edges.md) - A per-root checker summary undercounted edges (n=1, medium)
- [INC-0215](../../incidents/INC-0215-a-commit-skipped-the-machine-wide-pre-commit-scanner.md) - A commit skipped the machine-wide pre-commit scanner (n=1, medium)
- [INC-0224](../../incidents/INC-0224-a-classifier-kept-a-legacy-pattern-list-beside-a-new-exact-s.md) - A classifier kept a legacy pattern list beside a new exact signature (n=1, medium)
- [INC-0292](../../incidents/INC-0292-a-snapshot-recorder-that-finished-was-taken-as-proof-it-had.md) - A snapshot recorder that finished was taken as proof it had collected (n=1, medium)
- [INC-0372](../../incidents/INC-0372-a-test-run-s-command-line-exclusion-flag-did-not-take-effect.md) - A test run's command-line exclusion flag did not take effect, so excluded cases ran and called the package manager (n=1, medium)
- [INC-0378](../../incidents/INC-0378-a-default-that-silently-let-a-guard-pass-made-a-reviewer-rea.md) - A default that silently let a guard pass made a reviewer read a requirement as met (n=1, medium)
- [INC-0394](../../incidents/INC-0394-a-security-predicate-checked-for-truthiness-failed-open-on-a.md) - A security predicate checked for truthiness failed open on an undefined or null value (n=1, medium)
- [INC-0404](../../incidents/INC-0404-a-safe-default-could-silently-drop-data-when-an-uncertain-st.md) - A safe default could silently drop data when an uncertain state was read as gone (n=1, medium)
- [INC-0374](../../incidents/INC-0374-a-clause-survival-script-flagged-21-digest-rules-that-a-word.md) - A clause-survival script flagged 21 digest rules that a word diff showed were only wording compressions (n=1, low)
- [INC-0458](../../incidents/INC-0458-a-generated-down-migration-defect-fixed-once-came-back-in-th.md) - A generated down migration defect fixed once came back in the next row because the fix was never turned into a check (n=1, low)
- [INC-0504](../../incidents/INC-0504-a-branch-scrubbed-a-local-path-in-a-later-commit-and-a-range.md) - A branch scrubbed a local path in a later commit, and a range scan found it still in history (n=1, low)

## Also tagged detector-fail-open

20 incidents filed under another home class also carry this class. Listed by the node where they live:

- [false-green](../false-green/README.md): INC-0028, INC-0040, INC-0082, INC-0095, INC-0120, INC-0213, INC-0221, INC-0250, INC-0314, INC-0318, INC-0343, INC-0347
- [identity-and-keying](../identity-and-keying/README.md): INC-0122, INC-0161
- [ipc-and-env](../ipc-and-env/README.md): INC-0009
- [observability](../observability/README.md): INC-0227
- [reward-hacking](../reward-hacking/README.md): INC-0199
- [spec-and-scope](../spec-and-scope/README.md): INC-0191
- [test-isolation](../test-isolation/README.md): INC-0126
- [verdict-token](../verdict-token/README.md): INC-0152

## Practices touching this class

- [PRA-0001](../CORE.md#practices) - The enforcement ladder: pick the cheapest rung that makes the failure impossible
- [PRA-0003](../CORE.md#practices) - Six conditions for a gate that cannot be skipped
- [PRA-0004](../CORE.md#practices) - Choose the constraint surface before choosing the enforcement strength
