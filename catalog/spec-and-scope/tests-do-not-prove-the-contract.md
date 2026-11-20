# Green tests omit or misstate required behavior

[Catalog](../README.md) / [spec-and-scope](README.md) / tests-do-not-prove-the-contract

**Go here if:** A named parameter is untested, moved files vanish from a run, coverage summarizes a tier, an oracle pins the wrong detail, or static gates miss a unit regression.

**Rule:** Maintain an executable per-case inventory tying each required behavior to a collected assertion and qualifying run, with discovery witnesses, stable oracles, and whole-suite comparison after product changes.

13 incidents, 13 occurrences. Ordered by occurrences, then severity, then id.

## Incidents

### [INC-0105](../../incidents/INC-0105-a-function-signature-named-in-the-plan-but-never-called-by-a.md) - A function signature named in the plan but never called by any test shipped ignoring its second argument
- occurrences 1, severity medium, status fixed
- **Signature:** The plan names a parameter that no test exercises.
- **Rule:** Every planned parameter needs a test that makes it matter.

### [INC-0159](../../incidents/INC-0159-a-second-reader-of-the-same-registry-file-was-at-risk-of-rep.md) - A second reader of the same registry file was at risk of replacing the first
- occurrences 1, severity medium, status fixed
- **Signature:** Two rows each needed to parse the same assignments file.
- **Rule:** One parser per shared file format, reviewed with a mutant and a malformed-input case.

### [INC-0184](../../incidents/INC-0184-a-docs-only-row-was-accepted-by-judgment-instead-of-one-mech.md) - A docs-only row was accepted by judgment instead of one mechanical diff
- occurrences 1, severity medium, status fixed
- **Signature:** Acceptance depended on reading.
- **Rule:** Accept a docs-only row by one name-status diff against the stated parent.

### [INC-0191](../../incidents/INC-0191-a-one-parser-requirement-was-pinned-by-only-one-kind-of-test.md) - A one-parser requirement was pinned by only one kind of test
- occurrences 1, severity medium, status fixed
- **Signature:** A second parser could appear without failing a test.
- **Rule:** Pin a one-parser requirement both structurally and behaviorally

### [INC-0285](../../incidents/INC-0285-a-tier-level-coverage-table-hides-untraced-cases.md) - A tier-level coverage table hides untraced cases
- occurrences 1, severity medium, status fixed
- **Signature:** A coverage table summarized a tier while individual cases had no trace.
- **Rule:** Trace coverage per case, never per tier

### [INC-0311](../../incidents/INC-0311-moving-tests-into-a-new-group-silently-dropped-them-from-cal.md) - Moving tests into a new group silently dropped them from callers that select the old group by name
- occurrences 1, severity medium, status fixed
- **Signature:** A proposed move would have made every selector that names the old group omit the moved files.
- **Rule:** Before re-routing tests between groups, list every caller that selects the group by name and prove each still selects the same files

### [INC-0328](../../incidents/INC-0328-a-selector-mirroring-a-config-s-exclusions-matched-basenames.md) - A selector mirroring a config's exclusions matched basenames at any depth
- occurrences 1, severity medium, status fixed
- **Signature:** Files in nested directories with an excluded name vanished from a selection the config would keep.
- **Rule:** When code mirrors a config's file selection, compare anchored paths, not basenames, and keep an executable union check with planted nested witnesses

### [INC-0332](../../incidents/INC-0332-a-tier-exclusion-matched-only-one-file-extension.md) - A tier exclusion matched only one file extension
- occurrences 1, severity medium, status fixed
- **Signature:** Slow proofs moved to a differently suffixed file would have stayed in the per-commit tier.
- **Rule:** When tiering by filename suffix, check the exclusion glob against every extension in use and keep a discovery witness per tier (absent here, exactly once there)

### [INC-0391](../../incidents/INC-0391-an-implementer-s-evidence-admitted-one-case-that-contradicte.md) - An implementer's evidence admitted one case that contradicted its own every-undeclared-case-throws rule
- occurrences 1, severity medium, status fixed
- **Signature:** The evidence listed a case the stated rule said could not exist.
- **Rule:** When evidence contradicts a stated rule, the rule wins: change the code, not the wording

### [INC-0568](../../incidents/INC-0568-a-feature-branch-merged-on-static-gates-only-and-a-unit-test.md) - A feature branch merged on static gates only, and a unit test elsewhere that encoded the old seed order then went red on main
- occurrences 1, severity medium, status mitigated
- **Signature:** A branch that changes product code passes type, lint, identity and backlog checks, but no whole-unit comparison ran.
- **Rule:** A branch that changes product code merges only after a whole-unit comparison equal to the frozen baseline.

### [INC-0387](../../incidents/INC-0387-one-review-asked-to-delete-an-error-text-assertion-while-ano.md) - One review asked to delete an error-text assertion while another asked to pin the text
- occurrences 1, severity low, status fixed
- **Signature:** Two reviews gave opposite instructions about the same assertion.
- **Rule:** Pin an error name, never message text, as the oracle

### [INC-0535](../../incidents/INC-0535-a-standing-promise-to-guard-every-proven-behavior-had-no-inv.md) - A standing promise to guard every proven behavior had no inventory, so partial protection could pass as coverage
- occurrences 1, severity low, status mitigated
- **Signature:** A broad request such as never break what already works is acknowledged but never turned into a per-item count of what is guarded.
- **Rule:** Turn a broad protection promise into a per-item inventory with strict status definitions, a count, and a proposed guard for every gap; partial protection of a row is a gap.

### [INC-0584](../../incidents/INC-0584-an-exception-that-allowed-two-known-failures-in-a-unit-compa.md) - An exception that allowed two known failures in a unit comparison was closed the moment their fix merged
- occurrences 1, severity low, status mitigated
- **Signature:** A comparison exception outlives the failures it was written for.
- **Rule:** An exception for known failures must end when its fix merges; require the tree to contain the fix and compare to the frozen set.
