# A local fix leaves sibling cases or callers broken

[Catalog](../README.md) / [spec-and-scope](README.md) / fix-misses-related-consumers

**Go here if:** A fix leaves sibling payloads or callers using old arguments, state, or commands; a second defect remains, or a tiny conflict hides inconsistent automatically merged code.

**Rule:** Enumerate every sibling, call site, payload, and encoded rule affected by a change, then verify their exact contracts together; after a merge conflict inspect the entire merged file, including automatically resolved lines, and run the typecheck.

8 incidents, 8 occurrences. Ordered by occurrences, then severity, then id.

## Incidents

### [INC-0086](../../incidents/INC-0086-after-a-dependency-fix-two-rows-still-called-the-same-seed-f.md) - After a dependency fix, two rows still called the same seed function with different payloads
- occurrences 1, severity medium, status fixed
- **Signature:** A fix is verified by name, but the same seed function is called with different arguments elsewhere.
- **Rule:** Verify the call site and arguments, not only the function name, after a dependency change.

### [INC-0173](../../incidents/INC-0173-a-ruling-widened-a-shared-valid-state-and-only-some-payloads.md) - A ruling widened a shared valid state and only some payloads followed
- occurrences 1, severity medium, status fixed
- **Signature:** Some negatives passed against the tip only.
- **Rule:** When a ruling widens a shared valid state, change every payload that builds it.

### [INC-0225](../../incidents/INC-0225-a-fix-was-named-for-one-card-while-four-siblings-carried-the.md) - A fix was named for one card while four siblings carried the same command
- occurrences 1, severity medium, status fixed
- **Signature:** The siblings were left unfixed or silently changed.
- **Rule:** When applying a fix, search for siblings of the named instance and report them

### [INC-0255](../../incidents/INC-0255-one-batch-finding-hid-45-files-with-the-same-dependency.md) - One batch finding hid 45 files with the same dependency
- occurrences 1, severity medium, status fixed
- **Signature:** The defect was a conflict between two documents, not a batch fault.
- **Rule:** When a finding names a mechanism, sweep the suite for it before fixing one batch, and resolve a design conflict at its source

### [INC-0499](../../incidents/INC-0499-the-first-defect-of-a-kind-prompted-an-audit-of-the-whole-ki.md) - The first defect of a kind prompted an audit of the whole kind, which found a second
- occurrences 1, severity medium, status mitigated
- **Signature:** One hard-coded external host was found in a page that must work offline, and a second, silent one existed on the server.
- **Rule:** When one instance of a defect class appears, audit for the whole class before fixing only the instance.

### [INC-0459](../../incidents/INC-0459-a-new-required-argument-broke-an-older-direct-caller-that-th.md) - A new required argument broke an older direct caller that the change did not list
- occurrences 1, severity low, status fixed
- **Signature:** A whole unit run showed one more failure after a signature change.
- **Rule:** When an argument becomes required, list every direct caller, tests included, and keep the old call path or update every caller in the same change

### [INC-0466](../../incidents/INC-0466-a-script-carried-internal-load-vetoes-that-contradicted-a-la.md) - A script carried internal load vetoes that contradicted a later decision, and the script bytes were immutable
- occurrences 1, severity low, status fixed
- **Signature:** A script stopped a run on a gate that a ruling had removed.
- **Rule:** When a ruling changes a gate, list every script that encodes the old gate before the ruling is relied on

### [INC-0536](../../incidents/INC-0536-a-one-line-comment-conflict-hid-a-type-break-from-the-automa.md) - A one-line comment conflict hid a type break from the automatic part of the merge
- occurrences 1, severity low, status mitigated
- **Signature:** A merge conflict looks like one stale comment, while the automatically merged lines of the same file are inconsistent with each other.
- **Rule:** After any merge conflict, inspect the whole merged file for changes the tool resolved automatically and run the type check before accepting; a tester does not resolve product conflicts.
