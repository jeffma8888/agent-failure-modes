# A cited baseline, count, line, or digest no longer matches its source

[Catalog](../README.md) / [spec-and-scope](README.md) / records-drift-or-lose-provenance

**Go here if:** A baseline, count, citation, finding, or ruling no longer matches its source; moved or signed bytes differ, or review re-reads unchanged ranges and misses the actual delta.

**Rule:** Pin derived records to current source revisions, preserve reviewed bytes, and reconcile citations, counts, rulings, and signatures against the exact source; diff unchanged ranges before reviewing the actual delta.

12 incidents, 12 occurrences. Ordered by occurrences, then severity, then id.

## Incidents

### [INC-0055](../../incidents/INC-0055-a-scope-cut-was-mapped-against-the-previous-version-of-its-b.md) - A scope cut was mapped against the previous version of its baseline document
- occurrences 1, severity medium, status fixed
- **Signature:** A derived document cites a baseline by version label only, and the baseline has changed since the author last read it.
- **Rule:** Before mapping against a baseline document, read its current version and commit from disk and write that commit into the header of the derived document.

### [INC-0147](../../incidents/INC-0147-a-moved-history-row-was-silently-modernized-instead-of-stayi.md) - A moved history row was silently modernized instead of staying byte identical
- occurrences 1, severity medium, status fixed
- **Signature:** A move that is described as byte identical changes a this version label.
- **Rule:** Separate source-preserving relocation from attributed status changes.

### [INC-0194](../../incidents/INC-0194-a-citation-check-by-search-alone-could-miss-a-changed-fact.md) - A citation check by search alone could miss a changed fact
- occurrences 1, severity medium, status fixed
- **Signature:** A moved range was matched by text while its behavior changed.
- **Rule:** Compare cited ranges by diff when a version bump moves pinned-source citations

### [INC-0198](../../incidents/INC-0198-a-ledger-derived-from-a-token-range-went-stale-when-a-row-jo.md) - A ledger derived from a token range went stale when a row joined the range
- occurrences 1, severity medium, status fixed
- **Signature:** The ledger no longer matched the plan.
- **Rule:** Regenerate a ledger derived from a range at each revision and state the derived count

### [INC-0217](../../incidents/INC-0217-a-fixed-test-count-in-an-exit-criterion-went-stale.md) - A fixed test count in an exit criterion went stale
- occurrences 1, severity medium, status fixed
- **Signature:** The count no longer matched the suite.
- **Rule:** State an exit as the full active inventory with zero failed or skipped, name the qualifying-run rule, and disclose excluded runs

### [INC-0235](../../incidents/INC-0235-a-revision-review-could-re-read-an-unchanged-downstream-tabl.md) - A revision review could re-read an unchanged downstream table
- occurrences 1, severity medium, status fixed
- **Signature:** The unchanged part cost review time and hid the real delta.
- **Rule:** Diff the downstream table first when a revision only adds upstream rows

### [INC-0296](../../incidents/INC-0296-plan-line-anchors-drifted-with-each-plan-version.md) - Plan line anchors drifted with each plan version
- occurrences 1, severity medium, status fixed
- **Signature:** Correct line citations became off by one after a later plan revision.
- **Rule:** Cite plan rows by identity; line drift alone is not a finding

### [INC-0302](../../incidents/INC-0302-a-plan-revision-left-stale-operative-text-that-only-an-indep.md) - A plan revision left stale operative text that only an independent review caught
- occurrences 1, severity medium, status fixed
- **Signature:** A revised plan still directed work to a superseded file and carried wrong counts.
- **Rule:** After a revision, check every operative sentence and count against the replacement, using a reviewer who did not write it

### [INC-0326](../../incidents/INC-0326-a-signer-recomputed-the-declared-digest-before-signing-and-k.md) - A signer recomputed the declared digest before signing and kept the signature outside the hashed range
- occurrences 1, severity medium, status fixed
- **Signature:** A declared digest was about to be signed without the signer having hashed the bytes.
- **Rule:** A signature binds to bytes the signer has hashed himself, and appending the signature must not change the hashed range

### [INC-0335](../../incidents/INC-0335-a-pinned-base-digest-froze-a-file-that-a-later-row-split-nee.md) - A pinned base digest froze a file that a later row split needed to change
- occurrences 1, severity medium, status fixed
- **Signature:** A needed edit to a file would have invalidated the digest that prepared patches pin.
- **Rule:** When prepared patches pin a file's digest, treat that file as frozen and route every change through a later patch with the same regenerate caveat

### [INC-0338](../../incidents/INC-0338-a-review-pinned-before-the-fix-reported-findings-that-were-a.md) - A review pinned before the fix reported findings that were already closed
- occurrences 1, severity medium, status fixed
- **Signature:** A review of an older checkpoint listed findings as open that had since been fixed and closed.
- **Rule:** When a review's pin is older than the latest fix, land it with a note naming the commit and review that supersede each stale finding

### [INC-0346](../../incidents/INC-0346-a-ruling-sent-in-a-message-was-never-written-to-the-ruling-l.md) - A ruling sent in a message was never written to the ruling log
- occurrences 1, severity medium, status fixed
- **Signature:** A reviewer found a ruling missing from the log, and it had to be reconstructed from message text with a caveat.
- **Rule:** Write a ruling into the log in the same step as sending it; a ruling that exists only in a message is invisible to every other reader
