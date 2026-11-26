# A test oracle, locator or review claim came from memory, not source

[Catalog](../README.md) / [false-green](README.md) / oracle-or-claim-written-from-memory

**Go here if:** A locator never matches, an absence check matches a hidden input the library renders, an assertion expects what the design never defined, an identifier is slightly wrong, or a behavior claim is false.

**Rule:** Bind every oracle, locator, identifier and behavior claim to its source of truth at the installed or pinned version: cite the line that renders or defines it and search for each name. Treat a fix or review claim as a new claim to verify, and review independently by deriving your own list before reading the author's. Run a new root green on unchanged code before any mutation.

12 incidents, 12 occurrences. Ordered by occurrences, then severity, then id.

## Incidents

### [INC-0523](../../incidents/INC-0523-three-test-roots-by-three-authors-used-the-same-guessed-loca.md) - Three test roots by three authors used the same guessed locator for a generated field that the installed library does not render
- occurrences 2, severity medium, status mitigated
- **Signature:** Several browser tests scope a generated field by a role or label that its library never renders.
- **Rule:** Do not guess a locator for a generated field; cite the installed source line that renders it, and when one guess is found, audit every root for the same guess.
- **Recurrences:**
  - [INC-0530](../../incidents/INC-0530-an-icon-only-button-had-no-accessible-name-so-a-role-name-lo.md) - 2026-11-02 - An icon-only button had no accessible name, so a role-name locator could never match and the test timed out

### [INC-0042](../../incidents/INC-0042-self-review-does-not-catch-recurrences-of-your-own-documente.md) - Self-review does not catch recurrences of your own documented rules
- occurrences 1, severity high, status mitigated
- **Signature:** An artifact passes its author's careful self-review, and an independent pass immediately finds defects that match rules the author can quote from memory.
- **Rule:** Self-review is graded by the context that produced the defect, so a rule can be perfectly known and still not applied - knowing and executing are different capabilities. Use an independent verifier with access to the artifact and primary sources but NOT your reasoning, and treat a recurrence as evidence about the enforcement point, never as a reason to reword the rule.

### [INC-0056](../../incidents/INC-0056-test-seams-declared-from-memory-carried-wrong-field-names-an.md) - Test seams declared from memory carried wrong field names, and a bulk replacement silently missed a row
- occurrences 1, severity medium, status fixed
- **Signature:** A test oracle or interface section lists identifiers that nobody has searched for in the design, and the document has had bulk edits applied by script.
- **Rule:** Search for every identifier you put into a test oracle; never declare a seam from memory. Make each bulk replacement assert its expected match count.

### [INC-0057](../../incidents/INC-0057-a-revision-that-closed-every-finding-introduced-new-defects.md) - A revision that closed every finding introduced new defects in the seams it added
- occurrences 1, severity medium, status mitigated
- **Signature:** Each review round's fix adds new concrete claims (types, hooks, signatures), and the next round's findings are mostly about those additions.
- **Rule:** An accepted finding is not a closed finding. Re-verify every new concrete claim a fix introduces against its source of truth before declaring the finding closed.

### [INC-0061](../../incidents/INC-0061-exhaustive-test-wording-created-expectations-the-design-neve.md) - Exhaustive test wording created expectations the design never defined
- occurrences 1, severity medium, status mitigated
- **Signature:** A test requirement says 'every' member of a set, and the source of truth defines behaviour for only some of them.
- **Rule:** A per-ID test oracle may only require values its source of truth defines. 'Every' in a test requirement needs a check that the source covers every member.

### [INC-0062](../../incidents/INC-0062-a-reviewer-s-claim-about-framework-behaviour-was-wrong-and-a.md) - A reviewer's claim about framework behaviour was wrong, and accepting it would have put a wrong assertion into the tests
- occurrences 1, severity medium, status mitigated
- **Signature:** A review finding states what a library or framework does, in confident terms, and the proposed change follows directly from that statement.
- **Rule:** A reviewer's statement about framework or library behaviour is a hypothesis with the same standing as the author's. Verify it at the pinned version, reading the whole function, before it changes a test or a design.

### [INC-0234](../../incidents/INC-0234-a-ledger-review-that-started-from-the-author-list-could-inhe.md) - A ledger review that started from the author list could inherit its gaps
- occurrences 1, severity medium, status fixed
- **Signature:** The reviewer saw only what the author listed.
- **Rule:** Derive a ledger from the plan yourself before reading the author list, then compare

### [INC-0527](../../incidents/INC-0527-an-absence-check-for-a-hidden-field-matched-the-hidden-input.md) - An absence check for a hidden field matched the hidden input the library renders, so a regression root was red on unchanged code
- occurrences 1, severity medium, status mitigated
- **Signature:** A test asserts that a selector for a hidden field matches nothing, and the library renders a hidden input with the field id.
- **Rule:** A regression root must be green on unchanged code before any mutation; an absence selector for a hidden field must account for the hidden input the library still renders.

### [INC-0455](../../incidents/INC-0455-a-provenance-check-that-the-generator-can-never-satisfy-the.md) - A provenance check that the generator can never satisfy: the zero parent id on every snapshot
- occurrences 1, severity low, status fixed
- **Signature:** A required check was impossible to pass whatever the code did.
- **Rule:** Prove a diff base from what the generated SQL does and does not emit, and never demand a check the generator can not satisfy

### [INC-0578](../../incidents/INC-0578-not-visible-was-the-wrong-oracle-for-a-collapsed-sidebar-bec.md) - Not visible was the wrong oracle for a collapsed sidebar, because the closed navigation stays in the page with opacity zero and inert
- occurrences 1, severity low, status mitigated
- **Signature:** A closed menu is still in the DOM, and the visibility matcher ignores inert and off-screen position.
- **Rule:** Bind a collapsed or open state to the attributes the framework sets, not to a visibility matcher.

### [INC-0651](../../incidents/INC-0651-an-author-self-certified-review-findings-as-fixed-inside-the.md) - An author self-certified review findings as fixed inside the document being reviewed
- occurrences 1, severity low, status mitigated
- **Signature:** An artifact under review states that all blocking findings are fixed, but the attestation is authored by the person whose work is being reviewed rather than by the reviewer.
- **Rule:** Keep verification status in a reviewer-authored review log; authors may describe changes but must not self-certify that blocking findings are verified closed in the artifact under review.
