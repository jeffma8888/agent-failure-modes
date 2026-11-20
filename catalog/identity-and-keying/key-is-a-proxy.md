# A name, path string or digest stands in for the real identity, drifts

[Catalog](../README.md) / [identity-and-keying](README.md) / key-is-a-proxy

**Go here if:** Two values that must agree were typed separately (display name vs model id, two spellings of one path, digest vs its path, commit order from memory); a proof omits a dimension; one field, many facts.

**Rule:** Identify a thing by its canonical identity and derive everything else from it: compare resolved real paths not strings, verify path-to-digest pairs not membership, derive display names from ids, record the tool versions with any stored proof and compare them at use, read identities from the log rather than memory, and keep one fact per field.

6 incidents, 6 occurrences. Ordered by occurrences, then severity, then id.

## Incidents

### [INC-0122](../../incidents/INC-0122-a-digest-present-anywhere-in-a-manifest-was-taken-as-proof-i.md) - A digest present anywhere in a manifest was taken as proof it belonged to its file
- occurrences 1, severity medium, status fixed
- **Signature:** A check finds the digest somewhere in the manifest and passes.
- **Rule:** Verify pairs, not membership.

### [INC-0149](../../incidents/INC-0149-marker-sha-reviewer-approval-scope-successor-closure-and-act.md) - Marker SHA, reviewer approval scope, successor closure and activation ownership were treated as one fact
- occurrences 1, severity medium, status fixed
- **Signature:** A marker is read as proof of approval, closure and ownership at once.
- **Rule:** One fact per field.

### [INC-0359](../../incidents/INC-0359-a-stored-admission-record-left-out-the-tool-versions-it-was.md) - A stored admission record left out the tool versions it was produced under
- occurrences 1, severity medium, status fixed
- **Signature:** A per-file audit that admits concurrent test runs recorded no tool versions, so a proof from one toolchain would unlock the fast route under another.
- **Rule:** A stored proof that unlocks a faster or riskier route must carry the tool versions it was produced under and compare them at use; a mismatch or a missing field takes the safe route with a named reason, never the fast one

### [INC-0054](../../incidents/INC-0054-a-display-name-drifted-from-the-model-identifier-it-was-supp.md) - A display name drifted from the model identifier it was supposed to describe
- occurrences 1, severity low, status fixed
- **Signature:** Credits, rosters or reports carry a hand-typed model name next to an identifier that was typed separately.
- **Rule:** Record the exact model ID wherever a model is credited, and derive the display name from it. A display name is not evidence of which model did the work.

### [INC-0386](../../incidents/INC-0386-a-path-identity-guard-compared-strings-while-a-temp-director.md) - A path-identity guard compared strings while a temp directory has two spellings on the host
- occurrences 1, severity low, status fixed
- **Signature:** Two spellings of one directory compared unequal.
- **Rule:** A path-identity guard compares real paths, never strings

### [INC-0433](../../incidents/INC-0433-a-job-text-swapped-two-commit-identities-and-reading-the-log.md) - A job text swapped two commit identities, and reading the log caught it
- occurrences 1, severity low, status fixed
- **Signature:** Two commits were named the wrong way round in an instruction.
- **Rule:** Read the log for every commit a job text names before acting on it, and record the correction
