# Work lands under the wrong owner, path, or write boundary

[Catalog](../README.md) / [spec-and-scope](README.md) / wrong-owner-path-or-scope

**Go here if:** A task needs unowned files, a brief forbids a required output, a file is never collected, tools disagree on ownership, or a rule covers a whole commit instead of its affected files.

**Rule:** Derive each assignment and write boundary from the governing layout and ownership registry, check every affected file and dependency before dispatch, and apply a ruling to the individual files it governs rather than the whole commit.

12 incidents, 12 occurrences. Ordered by occurrences, then severity, then id.

## Incidents

### [INC-0085](../../incidents/INC-0085-a-helper-owned-by-one-test-root-was-imported-by-later-roots.md) - A helper owned by one test root was imported by later roots, creating an undeclared dependency
- occurrences 1, severity medium, status fixed
- **Signature:** A shared helper lives under one row or root and other rows import it without declaring the dependency.
- **Rule:** Record the owner of every shared helper, and treat an import from another root as a declared dependency.

### [INC-0099](../../incidents/INC-0099-a-test-reassignment-written-only-in-prose-was-not-enforced-b.md) - A test reassignment written only in prose was not enforced by any tool
- occurrences 1, severity medium, status fixed
- **Signature:** A rule about which row owns a test exists in text, and tools disagree or ignore it.
- **Rule:** Put a reassignment in one registry that every enforcing tool reads.

### [INC-0121](../../incidents/INC-0121-a-rule-scoped-to-work-after-a-ruling-was-applied-per-commit.md) - A rule scoped to work after a ruling was applied per commit while one commit held old and new patterns
- occurrences 1, severity medium, status fixed
- **Signature:** One commit contains files that predate the ruling and files that follow it.
- **Rule:** Scope a rule by the file, not the commit that carries it.

### [INC-0197](../../incidents/INC-0197-a-typecheck-failed-in-a-shared-helper-the-revision-did-not-o.md) - A typecheck failed in a shared helper the revision did not own
- occurrences 1, severity medium, status fixed
- **Signature:** The red was in code the revision could not touch.
- **Rule:** Fix a shared helper in its own row, never inside the consumer root

### [INC-0251](../../incidents/INC-0251-a-qa-file-was-placed-where-neither-the-identity-checker-nor.md) - A QA file was placed where neither the identity checker nor the project would take it
- occurrences 1, severity medium, status fixed
- **Signature:** The file was never collected.
- **Rule:** Every QA brief states the allowed destination prefixes and file suffix

### [INC-0289](../../incidents/INC-0289-a-passing-identity-check-was-taken-as-agreement-with-the-sig.md) - A passing identity check was taken as agreement with the signed plan
- occurrences 1, severity medium, status fixed
- **Signature:** A file resolved to the wrong owner while its identity check passed.
- **Rule:** Identity validity is not plan agreement; compare the resolved owner with the signed plan

### [INC-0074](../../incidents/INC-0074-a-brief-named-a-source-directory-the-repository-does-not-hav.md) - A brief named a source directory the repository does not have, written from a conventional layout instead of a listing
- occurrences 1, severity low, status fixed
- **Signature:** A brief scopes work to a directory by name, and the name is the conventional one for the language or framework rather than one anyone listed.
- **Rule:** Write path rules in a brief from a listing taken when the brief is written, never from memory of a conventional layout.

### [INC-0076](../../incidents/INC-0076-a-teammate-s-write-boundary-contradicted-the-charter-s-file.md) - A teammate's write boundary contradicted the charter's file layout, so a required record landed where activation would reject it
- occurrences 1, severity low, status fixed
- **Signature:** A brief limits writes to one directory, and the governing charter requires an output in a different one.
- **Rule:** Derive a teammate's write boundary from the governing charter's layout, and check the two agree before sending the brief.

### [INC-0376](../../incidents/INC-0376-a-signed-design-heading-outranked-a-plan-census-parenthetica.md) - A signed design heading outranked a plan census parenthetical when two reviews disagreed on a file location
- occurrences 1, severity low, status fixed
- **Signature:** Two reviews gave different locations for the same file.
- **Rule:** When reviews disagree on a file location, read the signed design text first; it outranks a plan parenthetical

### [INC-0420](../../incidents/INC-0420-a-reviewer-finding-moved-a-hook-registration-owner-twice-in.md) - A reviewer finding moved a hook registration owner twice in one hour
- occurrences 1, severity low, status fixed
- **Signature:** The owner of one registration changed twice in about an hour.
- **Rule:** Assign a hook registration owner only after reading which row owns the hook's neighbours

### [INC-0502](../../incidents/INC-0502-an-implementer-was-assigned-after-checking-only-who-wrote-th.md) - An implementer was assigned after checking only who wrote the test payload, and the root also held a coverage statement the implementer had written
- occurrences 1, severity low, status mitigated
- **Signature:** An author-conflict check was run on one file of a root, and a different file of the same root named the assignee as author.
- **Rule:** An author-conflict check covers every file of the root, including coverage statements and approval markers, by log and a name search, before the assignment is sent; the implementer own check stays as the second line.

### [INC-0540](../../incidents/INC-0540-a-successor-root-needed-to-change-a-file-owned-by-another-ro.md) - A successor root needed to change a file owned by another row family, and the identity checker allows replacement only within one family
- occurrences 1, severity low, status mitigated
- **Signature:** One successor root must edit a file that a different row family owns.
- **Rule:** When a change touches files owned by different row families, plan one successor per family; do not widen the checker or add a cross-family marker.
