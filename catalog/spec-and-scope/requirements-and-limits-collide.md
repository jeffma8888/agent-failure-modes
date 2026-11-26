# Requirements, units, or hard limits cannot hold together

[Catalog](../README.md) / [spec-and-scope](README.md) / requirements-and-limits-collide

**Go here if:** A duration exceeds its cap, a count has no unit, a complete identity cannot fit the transport, or a validator rejects a value its producer must emit.

**Rule:** Check all requirements together on explicit units and edge cases before signing, including dependency contracts, hard size limits, producer-consumer compatibility, and final-step rounding.

12 incidents, 12 occurrences. Ordered by occurrences, then severity, then id.

## Incidents

### [INC-0071](../../incidents/INC-0071-a-plan-claimed-minutes-denominated-stage-times-fit-inside-a.md) - A plan claimed minutes-denominated stage times fit inside a cap stated in seconds
- occurrences 1, severity medium, status mitigated
- **Signature:** A budget in one unit is compared with an estimate in another, and the document states that one fits inside the other.
- **Rule:** Convert every budget and estimate to one unit before writing that one fits inside the other.

### [INC-0102](../../incidents/INC-0102-a-success-control-that-forbade-every-connection-pinned-an-im.md) - A success control that forbade every connection pinned an implementation from before a later startup step that must connect
- occurrences 1, severity medium, status fixed
- **Signature:** A control test forbids all connections while a later row adds a startup step that connects.
- **Rule:** Write prohibitions against the full startup contract, not the current implementation.

### [INC-0127](../../incidents/INC-0127-a-document-already-at-its-hard-size-cap-had-no-room-for-the.md) - A document already at its hard size cap had no room for the next transcription, so the cap was met only after editing
- occurrences 1, severity medium, status fixed
- **Signature:** An edit is made first and the size cap is discovered afterward.
- **Rule:** Plan against a hard cap before the edit, not after.

### [INC-0189](../../incidents/INC-0189-an-override-was-written-without-reading-the-dependent-declar.md) - An override was written without reading the dependent declared range
- occurrences 1, severity medium, status fixed
- **Signature:** An override landed outside the range the dependent declares.
- **Rule:** Read the dependent declared range in the registry before writing an override; an out of range override needs a direct probe of the code path

### [INC-0334](../../incidents/INC-0334-a-bare-number-beside-a-time-threshold-invited-a-unit-misread.md) - A bare number beside a time threshold invited a unit misread
- occurrences 1, severity medium, status fixed
- **Signature:** A count was readable as seconds because the cell had no unit.
- **Rule:** Put units in every numeric cell that sits near a time threshold

### [INC-0352](../../incidents/INC-0352-a-size-limit-on-each-transported-record-and-a-full-identity.md) - A size limit on each transported record and a full-identity requirement were specified together with no framing
- occurrences 1, severity medium, status fixed
- **Signature:** A timing spec required every record to fit 512 bytes and to carry full file and case identity, and a long path could not satisfy both.
- **Rule:** When a transport limit and a completeness requirement meet, specify the framing and reconstruction, and test with long and non-ASCII identities

### [INC-0650](../../incidents/INC-0650-an-options-comparison-applied-the-same-hard-constraint-at-di.md) - An options comparison applied the same hard constraint at different severities
- occurrences 1, severity medium, status fixed
- **Signature:** The same disqualifying condition is blocking for one alternative and advisory for others; a limitation shared by all alternatives is presented as uniquely blocking.
- **Rule:** Write each decision invariant once, apply the same severity to every option that shares its condition, and never label a disadvantage common to all options as uniquely blocking; recompute verdicts after corrections.

### [INC-0424](../../incidents/INC-0424-a-captions-upload-relation-in-a-spec-would-have-added-a-medi.md) - A captions upload relation in a spec would have added a media referrer to a collection defined as image-only
- occurrences 1, severity low, status fixed
- **Signature:** A relation targeted a collection that does not accept its content.
- **Rule:** Before adding a relation to a shared collection, check what the collection holds and which referrer lists it joins; defer and record a gap if it does not fit

### [INC-0430](../../incidents/INC-0430-a-route-validator-rejected-a-width-that-the-generator-was-re.md) - A route validator rejected a width that the generator was required to emit
- occurrences 1, severity low, status fixed
- **Signature:** A consumer refused a value that its own producer was required to emit.
- **Rule:** Check every producer output against every consumer validator before signing a design, with a control for the edge output and for each refused value

### [INC-0441](../../incidents/INC-0441-a-geometry-spec-s-rounded-intermediate-broke-a-test-toleranc.md) - A geometry spec's rounded intermediate broke a test tolerance, caught by independent arithmetic
- occurrences 1, severity low, status fixed
- **Signature:** A spec's numbers did not meet the test tolerance they were written for.
- **Rule:** Recompute spec geometry independently against the oracle tolerance, round at the last step, and never loosen the oracle

### [INC-0572](../../incidents/INC-0572-a-brief-said-one-sorted-line-for-a-root-with-two-specs-which.md) - A brief said one sorted line for a root with two specs, which could be read two ways
- occurrences 1, severity low, status mitigated
- **Signature:** A count in a brief does not say what it counts.
- **Rule:** When a brief and a file header disagree on a count, ask for the unit before editing.

### [INC-0655](../../incidents/INC-0655-a-delegation-brief-contained-examples-forbidden-by-its-own-r.md) - A delegation brief contained examples forbidden by its own rule
- occurrences 1, severity low, status mitigated
- **Signature:** A teammate brief bans personal names while its own background section includes personal names.
- **Rule:** Before issuing a delegation brief, apply every prohibition and formatting check in it to the entire brief itself, including context and examples; remove contradictions before a teammate receives them.
