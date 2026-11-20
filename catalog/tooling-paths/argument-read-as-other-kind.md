# A helper or runner reads your argument as a different kind or name

[Catalog](../README.md) / [tooling-paths](README.md) / argument-read-as-other-kind

**Go here if:** A bare file name taken as a root name, an item named twice acted on twice, a revision id refused where the runner wants the base row, an option the runner lacks is requested, a missing db gets created

**Rule:** Never let a tool guess what a token is: pass each item once in its one explicit form, check which name and options the runner actually takes before briefing a run, treat a selection error before any test as 'not run'; a tool that cannot tell must fail closed, never create or copy by guess.

10 incidents, 10 occurrences. Ordered by occurrences, then severity, then id.

## Incidents

### [INC-0518](../../incidents/INC-0518-a-landing-tool-read-a-bare-file-name-as-a-test-root-name-so.md) - A landing tool read a bare file name as a test-root name, so a file was left out of a landing and the identifier check failed
- occurrences 3, severity low, status mitigated
- **Signature:** A tool accepts root names and file paths, and a bare file name is taken as a root name.
- **Rule:** A tool that accepts both root names and file paths must not guess which one a bare token is; list what it will land and compare with what was intended before it runs.
- **Recurrences:**
  - [INC-0545](../../incidents/INC-0545-a-landing-helper-guessed-the-kind-of-each-argument-from-its.md) - 2026-11-02 - A landing helper guessed the kind of each argument from its shape, so a plain file name was read as a pending root
  - [INC-0582](../../incidents/INC-0582-a-landing-helper-treated-a-top-level-file-name-with-no-slash.md) - 2026-11-04 - A landing helper treated a top-level file name with no slash as a test root, so it copied nothing for it

### [INC-0581](../../incidents/INC-0581-a-brief-named-the-revision-id-as-the-row-and-the-row-runner.md) - A brief named the revision id as the row, and the row runner refused before any test ran
- occurrences 2, severity low, status mitigated
- **Signature:** A runner receives a revision id where it expects the base row name.
- **Rule:** A runner selection error before any test is not run, never a red; briefs name the base row.
- **Recurrences:**
  - [INC-0604](../../incidents/INC-0604-a-row-runner-selected-by-family-while-the-brief-named-a-revi.md) - 2026-11-04 - A row runner selected by family while the brief named a revision, so the run stopped before the harness

### [INC-0137](../../incidents/INC-0137-a-database-adapter-created-an-absent-database-even-with-sche.md) - A database adapter created an absent database even with schema push disabled
- occurrences 1, severity medium, status fixed
- **Signature:** A misspelled or missing database name silently becomes a new empty database.
- **Rule:** Make a missing database fail by name instead of creating it.

### [INC-0597](../../incidents/INC-0597-a-run-before-approve-test-asked-for-a-runtime-route-that-kee.md) - A run-before-approve test asked for a runtime route that keeps the harness untouched instead of bypassing identity
- occurrences 1, severity medium, status mitigated
- **Signature:** A candidate test must run before approval but the normal row selection would pick the active predecessor.
- **Rule:** When a run-before-approve needs a swap, ask for a runtime route with a trap restore instead of editing identity records, and give it no credit.

### [INC-0519](../../incidents/INC-0519-a-root-was-passed-to-a-landing-helper-by-name-and-by-path-an.md) - A root was passed to a landing helper by name and by path, and the cleanup removed a file twice and stopped
- occurrences 1, severity low, status mitigated
- **Signature:** The same item is given to a helper in two forms, and a later step acts on it twice.
- **Rule:** Give a landing helper each item once and in its one documented form; an item named twice is a cleanup that can fail halfway.

### [INC-0546](../../incidents/INC-0546-a-reviewer-asked-for-a-mutant-to-run-with-a-case-filter-but.md) - A reviewer asked for a mutant to run with a case filter, but the row runner takes one row and no filter
- occurrences 1, severity low, status mitigated
- **Signature:** A review note names a run option that the runner does not have.
- **Rule:** When a runner cannot filter cases, run the whole row and attribute each red to its own case line; never credit another case baseline red as a kill.

### [INC-0565](../../incidents/INC-0565-a-second-request-for-a-part-row-driver-showed-that-the-row-r.md) - A second request for a part-row driver showed that the row runner needs a case filter
- occurrences 1, severity low, status mitigated
- **Signature:** A runner cannot run one case, so people ask for private drivers.
- **Rule:** A second request for a part-row driver means the runner needs a case filter; until it has one, ask for each sanction.
