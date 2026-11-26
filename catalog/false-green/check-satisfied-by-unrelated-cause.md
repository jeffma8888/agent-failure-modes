# A negative, absence or presence check passed for an unrelated reason

[Catalog](../README.md) / [false-green](README.md) / check-satisfied-by-unrelated-cause

**Go here if:** A refusal, zero-count, absence or 'error shown' assertion passed, but it would also pass on an unrelated error, a nonexistent target, an unread page, a decoy or a stale element.

**Rule:** Pair every negative or absence check with a positive control from the same read and state that must flip it, use one negative per rejection reason, assert the exact error or element rather than any match, and for a reaction assert the target is absent before the action and present after it.

12 incidents, 12 occurrences. Ordered by occurrences, then severity, then id.

## Incidents

### [INC-0601](../../incidents/INC-0601-a-nested-driver-deleted-node-options-so-a-preload-capture-ne.md) - A nested driver deleted NODE_OPTIONS, so a preload capture never reached the nested harness and a zero counted from copied receipts was not zero
- occurrences 1, severity high, status mitigated
- **Signature:** A results file reports an empty denial list while the log lists denials.
- **Rule:** A capture injected through an inherited environment variable is blind to any child that clears it; count from the log, and treat a zero from copies as unproven until a positive control shows the capture reaches the innermost process.

### [INC-0082](../../incidents/INC-0082-an-absence-check-passed-vacuously-because-the-forbidden-text.md) - An absence check passed vacuously because the forbidden text never matched the real title and the document may never have been read
- occurrences 1, severity medium, status fixed
- **Signature:** A test asserts a string occurs zero times in a page, and the count is zero for reasons unrelated to the page content.
- **Rule:** Every absence assertion needs a positive control from the same read, and matching must be substring-tolerant of the real data shape.

### [INC-0083](../../incidents/INC-0083-controls-that-fail-in-only-one-direction-a-drop-guard-keyed.md) - Controls that fail in only one direction, a drop guard keyed on a name pattern, and refusal tests satisfied by unrelated connection errors
- occurrences 1, severity medium, status fixed
- **Signature:** Refusal tests pass against a stub that accepts everything, or against a guard that does nothing because the target is unreachable anyway.
- **Rule:** A control counts only if it fails in both directions; scope destructive guards to recorded identities, and assert the specific refusal, not any error.

### [INC-0095](../../incidents/INC-0095-port-validation-tests-lacked-separate-absent-zero-and-shared.md) - Port validation tests lacked separate absent, zero and shared-port negatives and a positive callback control
- occurrences 1, severity medium, status fixed
- **Signature:** One combined negative case passes for any of several unrelated reasons.
- **Rule:** One negative per rejection reason, and a positive control in the same flow.

### [INC-0112](../../incidents/INC-0112-a-control-relied-on-state-the-test-had-changed-earlier-and-s.md) - A control relied on state the test had changed earlier and silently became vacuous
- occurrences 1, severity medium, status fixed
- **Signature:** A control that depends on a signed-in or seeded state runs after the test changed that state.
- **Rule:** Place a control in the state it needs, and show it can change.

### [INC-0193](../../incidents/INC-0193-a-negative-grep-was-taken-as-proof-that-a-removal-ruling-was.md) - A negative grep was taken as proof that a removal ruling was complete
- occurrences 1, severity medium, status fixed
- **Signature:** The forbidden token was gone and the duty remained.
- **Rule:** Check each named duty and its follow-through lines; a negative grep alone proves nothing

### [INC-0287](../../incidents/INC-0287-an-oracle-that-matches-a-substring-or-a-loose-boundary-can-b.md) - An oracle that matches a substring or a loose boundary can be satisfied by a decoy
- occurrences 1, severity medium, status fixed
- **Signature:** An assertion passed on a decoy that merely contained the expected text.
- **Rule:** Prove a claim on the exact element or attribute, and show the oracle rejects a decoy

### [INC-0318](../../incidents/INC-0318-a-path-guard-probed-only-with-nonexistent-paths-could-never.md) - A path guard probed only with nonexistent paths could never fail
- occurrences 1, severity medium, status fixed
- **Signature:** Every negative target returned allowed because the probed paths did not exist.
- **Rule:** Negative targets must exist; pair every guard with a positive control that must return the other value, and run one selftest on the real unpatched checker

### [INC-0642](../../incidents/INC-0642-a-quote-check-passed-on-the-collector-s-own-annotations-beca.md) - A quote check passed on the collector's own annotations because it only asked whether the text appeared anywhere in the capture file
- occurrences 1, severity medium, status fixed
- **Signature:** A claim says the source names something, its supporting quote is in the capture file, and the same words are not on the live page.
- **Rule:** Keep verbatim captures and collector notes in visibly separate blocks, and grade every quote against the verbatim block only; a match anywhere in a capture file is not a match in the source.

### [INC-0058](../../incidents/INC-0058-a-broad-exception-handler-hid-the-difference-between-not-fou.md) - A broad exception handler hid the difference between 'not found' and 'unknown name'
- occurrences 1, severity low, status fixed
- **Signature:** A handler catches a parent exception type first, and a sibling error with a different meaning is a subclass of it.
- **Rule:** When one error type subclasses another, order handlers narrow to broad and test the exact type. A broad assertion is green for every cause beneath it.

### [INC-0525](../../incidents/INC-0525-a-feedback-check-accepted-any-visible-alert-on-the-page-so-a.md) - A feedback check accepted any visible alert on the page, so a stale alert could satisfy it
- occurrences 1, severity low, status mitigated
- **Signature:** An assertion looks for any visible alert, and an alert from earlier or from another field satisfies it.
- **Rule:** A feedback assertion must fail without the action under test: assert the element is absent before the action and present after it, on a fresh page and scoped to the field, never on any alert on the page.

### [INC-0571](../../incidents/INC-0571-a-pre-action-zero-count-check-in-a-browser-test-showed-the-e.md) - A pre-action zero-count check in a browser test showed the error selector already matched one element before any action
- occurrences 1, severity low, status mitigated
- **Signature:** The error-visible selector matches an element before the action under test.
- **Rule:** Assert that an error selector matches nothing before the action; otherwise a post-action visibility check can pass for the wrong reason.
