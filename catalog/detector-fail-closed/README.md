# detector-fail-closed

[Catalog](../README.md) / detector-fail-closed

A monitor or check fires when it should not: it reports a correct artifact as broken, an honest quote as fabricated, a live process as dead. The accusation is specific and plausible, so the natural response is to repair the artifact - which is the destructive direction.

**Ask:** Before acting on this check's accusation, have you verified the ACCUSATION against the primary source - and could the check's own normalisation, base path or parser be the thing that disagrees?

**You are probably here if:** A check, scanner, lint or guard accuses an artifact you can see is correct: the quote is on the page, the file never ships, the bytes match main.

14 incidents filed here (14 occurrences); 3 more filed elsewhere are also tagged detector-fail-closed.

## Incidents

This class has no topics, so this node is the leaf. Ordered by occurrences, then severity, then id.

### [INC-0032](../../incidents/INC-0032-removing-a-veto-exposes-the-broken-classifier-it-was-masking.md) - Removing a veto exposes the broken classifier it was masking
- occurrences 1, severity high, status fixed
- **Signature:** You remove a blocking aggregate gate expecting a flood of passes, and get a small number of confident, specific refusals instead. Each surviving refusal is individually plausible and quotable - which is exactly why you believe it.
- **Rule:** A blocking gate upstream of a classifier hides that classifier's errors, so removing the gate does not create the refusals you then see - it reveals them. Treat the first batch of refusals after unblocking as unverified, hand-check them against the primary source, and re-run the repaired check over the historical verdicts before letting any of them stand.

### [INC-0033](../../incidents/INC-0033-one-normaliser-is-not-enough-if-it-maps-the-two-sides-into-d.md) - One normaliser is not enough if it maps the two sides into different conventions
- occurrences 1, severity high, status fixed
- **Signature:** A checker reports that a string is absent from a document where you can see it with your own eyes. The near-miss it prints is a clean prefix or suffix of the real text, or differs from it only in whitespace or punctuation.
- **Rule:** One normaliser on both sides is not enough - it must map both sides into the SAME convention. A rule right for one input (tags become spaces) is corruption on an input that never had tags. Prove a comparison with a known-GOOD pair as well as a known-bad one, and when a checker accuses an artifact you can see is correct, suspect the checker: a fail-closed defect points at a destructive repair.

### [INC-0034](../../incidents/INC-0034-a-malformed-item-aborts-the-per-item-pass-and-the-crash-rein.md) - A malformed item aborts the per-item pass, and the crash reinstates the veto wearing a traceback
- occurrences 1, severity medium, status fixed
- **Signature:** The pass that was supposed to judge items one at a time dies with a type error naming one item, and nothing is promoted. The log reads as an unrelated bug rather than as a policy decision, so the outcome is never recognised as the failure you just eliminated.
- **Rule:** Per-item isolation lives in the error path, not the loop. A for-loop makes the WORK per item; only a per-item catch makes the FAILURES per item, and an uncaught exception is a batch-wide verdict however granular the loop. Validate each item's shape, quarantine a bad one with a reason, and test that good items in the SAME batch still get through.

### [INC-0238](../../incidents/INC-0238-a-leak-scanner-matched-part-of-a-generated-name-and-blocked.md) - A leak scanner matched part of a generated name and blocked uploads
- occurrences 1, severity medium, status fixed
- **Signature:** The scan failed closed on a merge long after the files were added.
- **Rule:** Scan the whole tree after every merge, and fix a scanner false match with an encoded safe prefix proved by planted cases

### [INC-0327](../../incidents/INC-0327-a-marker-checker-matched-a-bare-word-and-pushed-authors-to-a.md) - A marker checker matched a bare word and pushed authors to a workaround
- occurrences 1, severity medium, status fixed
- **Signature:** A checker reported many focused-test markers that were only object keys.
- **Rule:** Anchor a marker check on call syntax, not a bare word; when a checker false positive forces a workaround, record it and fix the checker rather than spreading workarounds

### [INC-0569](../../incidents/INC-0569-denying-unexplained-loopback-connects-in-an-egress-observer.md) - Denying unexplained loopback connects in an egress observer broke the app, and the agent stopped instead of widening
- occurrences 1, severity medium, status mitigated
- **Signature:** A strict denial rule blocks connects the application makes to its own native listeners.
- **Rule:** Do not widen an egress allowlist to make the app work; attribute each listener by an operating system query, and allow only listeners owned by instrumented processes.

### [INC-0052](../../incidents/INC-0052-a-hygiene-rule-written-against-surface-syntax-rejects-valid.md) - A hygiene rule written against surface syntax rejects valid cases; enforce the property at the boundary where it happens
- occurrences 1, severity low, status fixed
- **Signature:** A rule meant to guarantee a behaviour (no network calls) is phrased as a ban on a syntactic form (no URL literals), and the code under test legitimately handles that form.
- **Rule:** Enforce a property where it happens (the network boundary), not by banning the syntax that usually precedes it. Before adopting a hygiene rule, run it against the features the project must test and ask what valid input it would reject.

### [INC-0366](../../incidents/INC-0366-a-walk-checklist-attached-another-request-variant-s-clause-t.md) - A walk checklist attached another request variant's clause to the keyless request, so a correct response read as a failure
- occurrences 1, severity low, status fixed
- **Signature:** A walk reported one failure on a response that matched the delivered spec.
- **Rule:** Derive each checklist expectation verbatim from the delivered spec row and cite the row; triage every failure against the spec, the code and the active tests before calling it a defect

### [INC-0371](../../incidents/INC-0371-a-byte-count-compare-at-the-exact-old-length-reported-end-of.md) - A byte-count compare at the exact old length reported end of file on a prefix that matched
- occurrences 1, severity low, status fixed
- **Signature:** A prefix check on an append-only file exited non-zero although the old bytes were unchanged.
- **Rule:** Verify append-only files with an explicit byte-prefix compare, not a limited-length compare at the exact length

### [INC-0438](../../incidents/INC-0438-a-lint-rule-against-a-throw-inside-a-finally-block-caught-a.md) - A lint rule against a throw inside a finally block caught a real defect in production code
- occurrences 1, severity low, status fixed
- **Signature:** A final lint gate failed on code that looked finished.
- **Rule:** Treat a lint error as a defect: restructure, pin each intended behavior with a unit case, and add no disable comment or rule change

### [INC-0462](../../incidents/INC-0462-an-identity-guard-compared-to-a-plain-address-while-the-data.md) - An identity guard compared to a plain address while the database cast rendered the address with a mask, so it could never pass, and a silent catch hid which check failed
- occurrences 1, severity low, status fixed
- **Signature:** A walk stopped at its helper with one generic error.
- **Rule:** Probe a guard against the real value it will see; a guard that can never pass is a defect, and a catch must print which step failed without secrets

### [INC-0479](../../incidents/INC-0479-a-leak-scanner-that-walked-the-working-directory-reported-an.md) - A leak scanner that walked the working directory reported an ignored local file, and the push gate blocked on a file that never ships
- occurrences 1, severity low, status fixed
- **Signature:** A scan of the working directory flagged a file outside the pushed tree.
- **Rule:** Gate a push on a scan of an export of the tracked tree; a scan of the working directory blocks on files that never ship.

### [INC-0552](../../incidents/INC-0552-the-walker-helper-produced-two-provisional-mismatches-of-its.md) - The walker helper produced two provisional mismatches of its own, which it traced and corrected append-only before any defect was filed
- occurrences 1, severity low, status mitigated
- **Signature:** A walk check reports a mismatch that comes from the helper expectation, not from the product.
- **Rule:** Trace a provisional mismatch to its expectation before filing a defect, and correct it append-only with evidence.

### [INC-0564](../../incidents/INC-0564-a-merge-check-rejected-a-generated-migration-for-whitespace.md) - A merge check rejected a generated migration for whitespace that every earlier generated migration also had
- occurrences 1, severity low, status mitigated
- **Signature:** A whitespace check rejects the output of a code generator.
- **Rule:** Do not hand-edit generated files to satisfy a whitespace check; exempt them by an exact pattern and keep checking all other files.

## Also tagged detector-fail-closed

3 incidents filed under another home class also carry this class. Listed by the node where they live:

- [detector-fail-open/wrong-parser-or-pattern](../detector-fail-open/wrong-parser-or-pattern.md): INC-0029
- [observability/missing-or-unverifiable-receipts](../observability/missing-or-unverifiable-receipts.md): INC-0144
- [tooling-paths/tool-defaults-not-target](../tooling-paths/tool-defaults-not-target.md): INC-0072
