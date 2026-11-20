# The brief or plan left a gap the worker fell through

[Catalog](../README.md) / [delegation](README.md) / brief-or-plan-left-a-gap

**Go here if:** A worker scaffolded a loop a clause did not name, edited a file the brief never listed, stopped on an undefined term, got another role's template line, or hit a prerequisite the audit missed

**Rule:** Close every hatch by name: forbid each escape route inline in one clause, list the only files a job may touch, define every term an independence rule uses, keep one template per role, derive dependency edges from what each file actually needs, and run a red check before the build agent starts.

7 incidents, 7 occurrences. Ordered by occurrences, then severity, then id.

## Incidents

### [INC-0016](../../incidents/INC-0016-anti-delegation-clause-must-forbid-scaffold-a-loop-too.md) - Anti-delegation clause must forbid 'scaffold a loop' too
- occurrences 1, severity high, status mitigated
- **Signature:** A subagent instructed to do work returns quickly and successfully, but the expected output file is empty or missing. Meanwhile a new nested loop or a prd.json / prompt.md scaffold appears alongside.
- **Rule:** A subagent reads 'do not spawn a nested agent' literally. Forbid every escape hatch by name in the SAME clause: nested agents, scaffolding a loop, writing prd/prompt/progress files, launching detached processes, handing off to a future iteration. Include the clause INLINE, not by reference. Kill an unauthorized loop by removing its required input, not just its pid.

### [INC-0087](../../incidents/INC-0087-an-import-level-audit-missed-helper-calls-that-needed-a-late.md) - An import-level audit missed helper calls that needed a later row, and only the engineer stop rule caught it
- occurrences 1, severity medium, status fixed
- **Signature:** A helper call such as a registered-resource lookup needs a feature delivered by a later row.
- **Rule:** Pair static audits with a stop rule so an engineer halts when a call needs later-row behavior.

### [INC-0098](../../incidents/INC-0098-an-acyclic-declared-dependency-graph-hid-producer-rows-that.md) - An acyclic declared dependency graph hid producer rows that an acceptance file needed
- occurrences 1, severity medium, status fixed
- **Signature:** The dependency graph validates, yet an acceptance file needs a row that is not listed.
- **Rule:** An acyclic graph is necessary but not sufficient; derive edges from what each file requires.

### [INC-0135](../../incidents/INC-0135-a-qa-template-line-pasted-into-an-engineer-task-contradicted.md) - A QA-template line pasted into an engineer task contradicted the engineer commit duty
- occurrences 1, severity medium, status fixed
- **Signature:** A task carries an instruction from another role template.
- **Rule:** One template per role.

### [INC-0298](../../incidents/INC-0298-harness-and-ownership-defects-were-left-for-the-build-agent.md) - Harness and ownership defects were left for the build agent to find
- occurrences 1, severity medium, status fixed
- **Signature:** Defects unrelated to the product were found only after the build started.
- **Rule:** Run a red check before the build agent starts and classify each first failure

### [INC-0331](../../incidents/INC-0331-a-job-edited-a-file-outside-its-brief.md) - A job edited a file outside its brief
- occurrences 1, severity medium, status fixed
- **Signature:** A commit changed a file the brief never named.
- **Rule:** Name the only files a job may touch, and check the diff file list on landing

### [INC-0507](../../incidents/INC-0507-an-independence-rule-did-not-say-what-counts-as-an-agent-or.md) - An independence rule did not say what counts as an agent or as a part, and four of nine parallel slices stopped at once
- occurrences 1, severity medium, status mitigated
- **Signature:** A rule says to stop if you authored or reviewed any part, and different agents read part and agent differently.
- **Rule:** Define independence per agent instance, and name which artifacts block (wrote the test or judged its cases) and which only need disclosure (inventories, citation audits).
