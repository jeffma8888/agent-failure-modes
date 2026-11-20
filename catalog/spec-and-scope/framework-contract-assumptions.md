# Framework behavior contradicts the design or test

[Catalog](../README.md) / [spec-and-scope](README.md) / framework-contract-assumptions

**Go here if:** The framework transforms input before a check, swallows a refusal, adds unexpected defaults, makes an undeclared request, or loses behavior when a component is replaced.

**Rule:** Verify framework-dependent claims in the installed source end to end and test the complete observable contract, including transformations, errors, side effects, and replaced defaults.

14 incidents, 14 occurrences. Ordered by occurrences, then severity, then id.

## Incidents

### [INC-0134](../../incidents/INC-0134-a-qa-case-followed-only-3xx-redirects-while-payload-3-admin.md) - A QA case followed only 3xx redirects while Payload 3 admin redirects under Next 16 are soft redirects with HTTP 200
- occurrences 1, severity medium, status fixed
- **Signature:** A test expecting a 3xx fails on a correct redirect.
- **Rule:** Assert what the user sees, not the transport mechanism.

### [INC-0245](../../incidents/INC-0245-a-third-party-avatar-request-was-made-without-anyone-noticin.md) - A third-party avatar request was made without anyone noticing
- occurrences 1, severity medium, status fixed
- **Signature:** The page looked right and still contacted a third party.
- **Rule:** Assert that a page makes no request to a third-party origin unless declared

### [INC-0276](../../incidents/INC-0276-do-not-hand-match-paths-a-framework-matches-with-a-richer-sy.md) - Do not hand-match paths a framework matches with a richer syntax
- occurrences 1, severity medium, status fixed
- **Signature:** A hand matcher understood fewer path forms than the framework it mirrored.
- **Rule:** Reuse the framework path matcher instead of a hand matcher, or test every syntax form it supports

### [INC-0395](../../incidents/INC-0395-handing-a-counting-stream-to-a-framework-that-catches-stream.md) - Handing a counting stream to a framework that catches stream failures lost the custom refusal contract
- occurrences 1, severity medium, status fixed
- **Signature:** A custom refusal never reached the caller once the framework wrapped the stream.
- **Rule:** Own the refusal contract before handing a stream to a framework that catches stream failures

### [INC-0506](../../incidents/INC-0506-two-fields-claimed-the-same-publication-state-and-the-seed-w.md) - Two fields claimed the same publication state, and the seed wrote only one, so the admin and the public predicate disagreed
- occurrences 1, severity medium, status mitigated
- **Signature:** An application status says published and the framework draft status says draft for the same record.
- **Rule:** When two fields can claim one state, derive one from the other or assert both in the same test, and write through the framework supported transition.

### [INC-0528](../../incidents/INC-0528-a-fix-gave-a-list-column-a-custom-cell-and-dropped-the-defau.md) - A fix gave a list column a custom cell and dropped the default cell's link to the record, so the list lost its only way to open a record
- occurrences 1, severity medium, status mitigated
- **Signature:** A custom cell component replaces the default cell, and the default cell carried the record link.
- **Rule:** Replacing a framework default cell, field or component replaces everything it did, not only what the change targeted; list what the default provided before replacing it, and test it.

### [INC-0599](../../incidents/INC-0599-a-checklist-expected-a-slug-first-link-and-excused-absent-he.md) - A checklist expected a slug first link and excused absent headers, and installed UI source and a reviewer disproved both
- occurrences 1, severity medium, status mitigated
- **Signature:** A manual checklist states what the UI will show without reading the installed UI code.
- **Rule:** Before a checklist states what a screen shows, verify it against installed UI source; do not infer request type or excuse missing headers.

### [INC-0618](../../incidents/INC-0618-three-successive-oracle-changes-were-ruled-for-one-test-with.md) - Three successive oracle changes were ruled for one test without first reading the whole framework function that mutates the object under test, so the engineer stopped three times
- occurrences 1, severity medium, status mitigated
- **Signature:** Each fix to a test oracle passes its assertion and fails the next one that reads the same mutated object.
- **Rule:** Before ruling an oracle that depends on framework behaviour, read the entire installed function chain end to end and rule every affected assertion at once.

### [INC-0425](../../incidents/INC-0425-a-framework-operation-order-showed-that-file-data-is-generat.md) - A framework operation order showed that file data is generated before the field validators, so a security check moved to the operation hook
- occurrences 1, severity low, status fixed
- **Signature:** A content check ran after the framework had already rewritten the input it was meant to inspect.
- **Rule:** Place a security check on original input in a hook that runs before the framework transforms the input, verified in the installed source, and record any move as a named deviation

### [INC-0434](../../incidents/INC-0434-a-reviewer-s-framework-claim-was-corrected-from-the-installe.md) - A reviewer's framework claim was corrected from the installed source: a draft save writes only the versions table
- occurrences 1, severity low, status fixed
- **Signature:** A reviewer stated a framework behavior that the installed source does not show.
- **Rule:** Verify a reviewer's framework claim in the installed source before adopting it, and cite the source

### [INC-0440](../../incidents/INC-0440-an-image-library-throw-on-undecodable-bytes-surfaced-as-a-se.md) - An image library throw on undecodable bytes surfaced as a server error instead of a refusal
- occurrences 1, severity low, status fixed
- **Signature:** Malformed upload bytes produced a server error.
- **Rule:** Catch a library throw on untrusted input and refuse with a client error status and a stable reason code; pin it with a valid-signature, bad-body case

### [INC-0553](../../incidents/INC-0553-a-proposal-found-that-the-product-itself-writes-the-state-a.md) - A proposal found that the product itself writes the state a fixture needed, which turned a validation-bypass question into a product path
- occurrences 1, severity low, status mitigated
- **Signature:** A fixture needs a record that normal validation would refuse, which suggests bypassing validation.
- **Rule:** Before bypassing validation for a fixture, look for a product path that writes the state; if none works, stop and report rather than fall back to SQL.

### [INC-0559](../../incidents/INC-0559-a-successor-root-was-authored-and-approved-without-a-run-and.md) - A successor root was authored and approved without a run, and its first baseline failed because the installed config had one more internal collection than its exact list
- occurrences 1, severity low, status mitigated
- **Signature:** An exact list of framework internals in a root is stale against the installed configuration.
- **Rule:** A root that pins a list of framework internals must be checked against the installed configuration and run once before approval; a setup failure is a root defect, fixed by a new successor, never by an in-place edit.

### [INC-0580](../../incidents/INC-0580-a-dependency-had-no-switch-for-a-dev-only-outbound-call-and.md) - A dependency had no switch for a dev-only outbound call, and the implementer stopped instead of guessing
- occurrences 1, severity low, status mitigated
- **Signature:** A requirement to disable an outbound call has no switch in the installed dependency.
- **Rule:** Do not patch a dependency or mask fetch to silence a dev-only call; find which mode reaches it, and place the zero-outbound check where the shipped app runs.
