# Tests pass but the real page, status or session is wrong

[Catalog](../README.md) / [false-green](README.md) / real-page-or-response-wrong-behind-green

**Go here if:** Every tier is green, yet the real site shows a blank page, a not-found with status 200, raw markup or a guest instead of staff, a probe used up one-time state, or a flow needing a hidden token fails.

**Rule:** Before accepting a user-facing change, observe it on the real target: walk the real build, assert HTTP status with the body from every client, prove the identity a request claims with a positive marker, render with the target renderer, run destructive probes last, and test every flow that needs what a change hides.

12 incidents, 12 occurrences. Ordered by occurrences, then severity, then id.

## Incidents

### [INC-0241](../../incidents/INC-0241-automated-tests-passed-while-nobody-had-walked-the-real-site.md) - Automated tests passed while nobody had walked the real site
- occurrences 2, severity medium, status fixed
- **Signature:** The suite covered what was written, not what a person would click.
- **Rule:** Walk the real site after each milestone and feature close, and write each defect as a failing test first
- **Recurrences:**
  - [INC-0496](../../incidents/INC-0496-an-acceptance-record-was-ready-for-signature-with-every-test.md) - 2026-11-02 - An acceptance record was ready for signature with every test tier green while the main page of the row was blank

### [INC-0244](../../incidents/INC-0244-a-correct-not-found-page-was-served-with-a-200-status.md) - A correct not-found page was served with a 200 status
- occurrences 2, severity medium, status fixed
- **Signature:** The page looked right and the status was wrong.
- **Rule:** Assert the response status and the rendered body together
- **Recurrences:**
  - [INC-0265](../../incidents/INC-0265-a-rendered-not-found-view-is-not-proof-of-a-404-status.md) - 2026-11-01 - A rendered not-found view is not proof of a 404 status

### [INC-0275](../../incidents/INC-0275-a-probe-that-sends-a-session-cookie-alone-may-test-guest-beh.md) - A probe that sends a session cookie alone may test guest behavior
- occurrences 2, severity medium, status fixed
- **Signature:** A probe that sent only a session cookie silently tested guest behavior.
- **Rule:** Send every header an authenticated request needs, and run a control that proves the identity the probe claims
- **Recurrences:**
  - [INC-0282](../../incidents/INC-0282-a-test-that-claims-a-role-must-prove-the-role-before-relying.md) - 2026-11-01 - A test that claims a role must prove the role before relying on it

### [INC-0250](../../incidents/INC-0250-bare-angle-bracket-slots-turned-a-markdown-note-into-raw-tex.md) - Bare angle-bracket slots turned a Markdown note into raw text after structural checks passed
- occurrences 1, severity high, status fixed
- **Signature:** The note passed every structural check and still showed raw text after the first slot.
- **Rule:** Verify Markdown by the target renderer's own parse, not by structural lint; never leave a bare <slot> outside code.

### [INC-0246](../../incidents/INC-0246-a-short-password-check-created-the-one-time-account-instead.md) - A short password check created the one-time account instead of showing an error
- occurrences 1, severity medium, status fixed
- **Signature:** The probe succeeded and consumed the one-time form.
- **Rule:** Run destructive checks on a one-time form last, and use a repeatable form for validation checks

### [INC-0272](../../incidents/INC-0272-not-found-under-a-streaming-root-layout-answers-200-whatever.md) - Not-found under a streaming root layout answers 200 whatever the call site
- occurrences 1, severity medium, status fixed
- **Signature:** Every call site for a not-found error still returned 200.
- **Rule:** When a root layout streams its shell, set the status before it, not from the rendered view

### [INC-0273](../../incidents/INC-0273-a-status-check-must-take-every-client-reading.md) - A status check must take every client reading
- occurrences 1, severity medium, status fixed
- **Signature:** One client reading of a status disagreed with the others.
- **Rule:** Take every client reading of a status before calling it fixed

### [INC-0497](../../incidents/INC-0497-a-flag-that-hides-the-token-from-responses-left-first-user-r.md) - A flag that hides the token from responses left first-user registration with an empty session cookie
- occurrences 1, severity medium, status mitigated
- **Signature:** Registration returned success and stored the admin, and the browser landed on the login page.
- **Rule:** When a change hides or removes a credential from responses, test every flow that needs that credential to finish, not only that it is hidden.

### [INC-0498](../../incidents/INC-0498-the-first-browser-run-of-new-end-to-end-cases-found-two-prod.md) - The first browser run of new end-to-end cases found two product defects that config reads and other tiers missed
- occurrences 1, severity medium, status mitigated
- **Signature:** A config listed a column and a field, and the real page showed neither as intended.
- **Rule:** A config that lists a column or a field is not evidence that the page shows it or works offline; only a browser run on the real page is.
