# The reviewer or runner you named was not independent or not free

[Catalog](../README.md) / [delegation](README.md) / reviewer-not-independent-or-free

**Go here if:** A reviewer stops at its own author check, runs the same model as the author, was pre-named and is busy when the artifact lands, would apply its own text, or an assignment breaks the independence rule

**Rule:** Name the reviewer when the artifact lands, from whoever is free; first search commits AND review files for every earlier author or judge of the item, compare the reviewer's model with the author's, and re-read the plan's independence rules - the reviewer's own author check is the second line, never the first.

9 incidents, 9 occurrences. Ordered by occurrences, then severity, then id.

## Incidents

### [INC-0517](../../incidents/INC-0517-two-reviewers-were-named-who-had-written-or-judged-the-roots.md) - Two reviewers were named who had written or judged the roots they were to review, and both stopped at the author check
- occurrences 3, severity low, status mitigated
- **Signature:** A reviewer is named without reading the root author line and review history, and the reviewer author check refuses.
- **Rule:** Before naming a reviewer, read the root coverage author line and review history; the reviewer own author check is the second line, not the first.
- **Recurrences:**
  - [INC-0526](../../incidents/INC-0526-a-reviewer-was-named-after-checking-commit-authorship-only-a.md) - 2026-11-02 - A reviewer was named after checking commit authorship only, and the reviewer had judged the root's cases in an earlier review file
  - [INC-0539](../../incidents/INC-0539-two-reviewers-in-a-row-were-assigned-a-slice-they-had-alread.md) - 2026-11-02 - Two reviewers in a row were assigned a slice they had already worked on, because the pick did not search the record

### [INC-0220](../../incidents/INC-0220-a-reviewer-proposed-text-was-at-risk-of-being-applied-by-its.md) - A reviewer proposed text was at risk of being applied by its own author
- occurrences 1, severity medium, status fixed
- **Signature:** The author could soften the reviewer text.
- **Rule:** Apply a reviewer exact text through a third party, with digested backups, a proposer re-review and a separate re-check

### [INC-0337](../../incidents/INC-0337-reviewers-named-at-ruling-time-were-busy-when-the-artifact-l.md) - Reviewers named at ruling time were busy when the artifact landed
- occurrences 1, severity medium, status fixed
- **Signature:** A review was reassigned because the reviewer named earlier was occupied.
- **Rule:** Name the reviewer when the artifact lands, from whoever is free and is not its author; record the reassignment in the ruling

### [INC-0399](../../incidents/INC-0399-a-final-review-was-reassigned-from-a-busy-reviewer-to-an-idl.md) - A final review was reassigned from a busy reviewer to an idle one of a different model instead of queueing
- occurrences 1, severity low, status fixed
- **Signature:** A review waiting for a busy reviewer would have stalled the acceptance step.
- **Rule:** Reassign a review to an idle qualified reviewer of a different model rather than queueing it, keeping the non-author rule

### [INC-0423](../../incidents/INC-0423-a-review-was-reassigned-off-the-critical-path-so-the-reviewe.md) - A review was reassigned off the critical path so the reviewer who owned the blocking recheck stayed on it
- occurrences 1, severity low, status fixed
- **Signature:** One reviewer held two reviews while a blocking recheck waited.
- **Rule:** Keep the reviewer on the critical path on that path and reassign off-path reviews to another non-author

### [INC-0467](../../incidents/INC-0467-a-run-plan-barred-the-test-author-from-running-the-script-an.md) - A run plan barred the test author from running the script, and a later message assigned that author anyway
- occurrences 1, severity low, status fixed
- **Signature:** A message contradicted the plan it was meant to follow.
- **Rule:** Check an assignment against the independence rules of the plan before sending it

### [INC-0635](../../incidents/INC-0635-a-review-was-assigned-to-a-reviewer-by-role-name-but-the-rev.md) - A review was assigned to a reviewer by role name, but the reviewer and the author ran the same model, so it was not an independent review
- occurrences 1, severity low, status mitigated
- **Signature:** A reviewer assigned for independence runs the same model as the author of the work under review.
- **Rule:** Choose each reviewer by the model of its thread, checked against the author's thread, not by role name.
