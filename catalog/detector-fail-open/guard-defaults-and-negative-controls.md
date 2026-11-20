# A broken guard implementation still appears valid

[Catalog](../README.md) / [detector-fail-open](README.md) / guard-defaults-and-negative-controls

**Go here if:** The guard appears to satisfy its contract even though a faulty implementation can produce the same passing result.

**Rule:** Require exact guard decisions for every protected field, tag and copy, with distinguishing positive and negative controls; treat unknown or failed reads as denial or retained data, never successful validation, and choose fixtures that separate the competing implementations.

6 incidents, 6 occurrences. Ordered by occurrences, then severity, then id.

## Incidents

### [INC-0108](../../incidents/INC-0108-a-fail-closed-url-rule-copied-into-several-helpers-was-not-a.md) - A fail-closed URL rule copied into several helpers was not applied to every copy or every URL part
- occurrences 1, severity medium, status fixed
- **Signature:** One helper checks the host and another omits the database or port.
- **Rule:** One rule, every copy, every URL part.

### [INC-0113](../../incidents/INC-0113-a-rule-set-widened-by-tag-survived-dropping-one-tag-because.md) - A rule set widened by tag survived dropping one tag because only some tags had a planted violation
- occurrences 1, severity medium, status fixed
- **Signature:** A check covers several tags, and removing one tag leaves the suite green.
- **Rule:** Every tag in a rule needs its own planted violation.

### [INC-0148](../../incidents/INC-0148-ascii-only-fixtures-could-not-tell-utf-16-code-unit-order-fr.md) - ASCII-only fixtures could not tell UTF-16 code unit order from UTF-8 byte order
- occurrences 1, severity medium, status fixed
- **Signature:** A sort or compare test passes under either ordering because all data is ASCII.
- **Rule:** Choose data that separates the alternatives under test.

### [INC-0378](../../incidents/INC-0378-a-default-that-silently-let-a-guard-pass-made-a-reviewer-rea.md) - A default that silently let a guard pass made a reviewer read a requirement as met
- occurrences 1, severity medium, status fixed
- **Signature:** A guard passed on an input it had never been told about.
- **Rule:** A guard must fail closed with an explicit configuration error; never let a default make it pass

### [INC-0394](../../incidents/INC-0394-a-security-predicate-checked-for-truthiness-failed-open-on-a.md) - A security predicate checked for truthiness failed open on an undefined or null value
- occurrences 1, severity medium, status fixed
- **Signature:** A guard allowed access when its input was missing.
- **Rule:** A security predicate allows only on the exact expected value, never on truthiness

### [INC-0404](../../incidents/INC-0404-a-safe-default-could-silently-drop-data-when-an-uncertain-st.md) - A safe default could silently drop data when an uncertain state was read as gone
- occurrences 1, severity medium, status fixed
- **Signature:** A safe default treated a refused read as an absent item.
- **Rule:** When a state is uncertain, treat the item as surviving; fail closed, never read a refusal as gone
