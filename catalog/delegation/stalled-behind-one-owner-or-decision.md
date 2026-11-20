# Parallel work stalls behind one busy owner, open decision or slot cap

[Catalog](../README.md) / [delegation](README.md) / stalled-behind-one-owner-or-decision

**Go here if:** Teammates sit idle while one part of a document, one busy owner, one undecided batch of amendments, a runtime cap or a brief low-load window holds everything.

**Rule:** Split what can proceed from what must wait. Discriminators: sign the stable re-checked part of a document and name what stays held; separate apply-now amendments from author-decides; start the red phase while a recheck runs; redo a mechanical merge yourself and prove the delta path by path; release idle teammates to free slots; dispatch gated runs the moment the window opens.

7 incidents, 7 occurrences. Ordered by occurrences, then severity, then id.

## Incidents

### [INC-0237](../../incidents/INC-0237-a-team-runtime-cap-blocked-new-teammates-behind-retained-idl.md) - A team runtime cap blocked new teammates behind retained idle ones
- occurrences 1, severity medium, status fixed
- **Signature:** The cap was reached with idle teammates that could not be closed.
- **Rule:** Release then close the longest idle teammate to free a slot; prefer larger batches over more teammates

### [INC-0277](../../incidents/INC-0277-sign-the-stable-re-checked-part-of-a-design-addendum-instead.md) - Sign the stable re-checked part of a design addendum instead of waiting
- occurrences 1, severity medium, status fixed
- **Signature:** Several authors were idle while one open part of a design addendum was pending.
- **Rule:** Unblock parallel work by signing the stable re-checked part of a document and naming what stays held

### [INC-0379](../../incidents/INC-0379-splitting-a-review-s-amendments-kept-the-engineer-busy-while.md) - Splitting a review's amendments kept the engineer busy while decisions were pending
- occurrences 1, severity low, status fixed
- **Signature:** An engineer would have waited for all amendments of one review to be decided.
- **Rule:** Split a review's amendments into apply-now and author-decides, and write no tests for undecided items early

### [INC-0392](../../incidents/INC-0392-a-declaration-request-that-split-sourced-values-from-decisio.md) - A declaration request that split sourced values from decisions let the lead rule eleven items in one pass
- occurrences 1, severity low, status fixed
- **Signature:** A request mixed facts and open choices, which would have needed several rounds.
- **Rule:** Request declarations as sourced values and decisions, each with its gap

### [INC-0410](../../incidents/INC-0410-the-lead-re-merged-the-full-candidate-itself-rather-than-que.md) - The lead re-merged the full candidate itself rather than queue behind the busy owner, and proved the delta path by path
- occurrences 1, severity low, status fixed
- **Signature:** A mechanical merge was waiting for a busy owner.
- **Rule:** When the owner is busy, redo a mechanical merge directly and prove the new delta equals the old path by path

### [INC-0411](../../incidents/INC-0411-a-red-phase-may-start-while-a-spec-recheck-runs-because-the.md) - A red phase may start while a spec recheck runs because the reviewed bytes fix the behavior
- occurrences 1, severity low, status fixed
- **Signature:** Work waited for a recheck that could not change the reviewed behavior.
- **Rule:** Start the red phase while a spec recheck runs; only the production commit waits

### [INC-0435](../../incidents/INC-0435-a-low-load-window-needed-immediate-dispatch-of-the-gated-run.md) - A low-load window needed immediate dispatch of the gated runs
- occurrences 1, severity low, status fixed
- **Signature:** Gated runs waited while a short low-load window was open.
- **Rule:** When a low-load window opens, dispatch the gated runs at once, reading the load in its own command before each launch
