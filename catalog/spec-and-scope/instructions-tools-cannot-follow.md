# Instructions fail a gate or omit the required operation

[Catalog](../README.md) / [spec-and-scope](README.md) / instructions-tools-cannot-follow

**Go here if:** A gate cannot pass after its preceding step, a required command or parameter is unavailable, a tool exceeds promised effects, a runner cannot reach a check, or cleanup only seeds and leaves old rows.

**Rule:** Walk each instruction through the installed tool and real checker on the intended post-step tree, including effects, parameters, permissions, and exact cleanup hook bodies; ask before substituting a private driver, and verify restored green through the standard runner.

13 incidents, 13 occurrences. Ordered by occurrences, then severity, then id.

## Incidents

### [INC-0267](../../incidents/INC-0267-a-check-named-lint-can-write.md) - A check named lint can write
- occurrences 1, severity medium, status fixed
- **Signature:** A check named as read only could create directories.
- **Rule:** Do not assume a read-named check is read only; read its loader

### [INC-0330](../../incidents/INC-0330-a-runbook-described-steps-its-own-script-s-gate-refused.md) - A runbook described steps its own script's gate refused
- occurrences 1, severity medium, status fixed
- **Signature:** The documented run record failed the script's gate because the gate wanted a second record with other keys.
- **Rule:** Walk every runbook step through the script's gates offline before calling the runbook ready

### [INC-0609](../../incidents/INC-0609-a-brief-said-to-move-a-post-case-full-seed-to-afterall-but-t.md) - A brief said to move a post-case full seed to afterAll, but the seed is find-or-create, so a seed without a reset first does not restore the baseline
- occurrences 1, severity medium, status mitigated
- **Signature:** A cleanup hook that only seeds leaves earlier rows in place.
- **Rule:** When a brief moves a cleanup, state the exact body to run; a seed that is find-or-create without a reset first does not restore a baseline.

### [INC-0616](../../incidents/INC-0616-a-signed-packet-required-a-tail-only-migration-rollback-but.md) - A signed packet required a tail-only migration rollback, but the named command rolls back a whole batch, so on a fresh database it would undo every migration
- occurrences 1, severity medium, status mitigated
- **Signature:** A signed proof step names a command whose installed semantics are broader than the claim it must prove.
- **Rule:** Before signing, read the tool's installed semantics against each requirement it must prove; a command name is not evidence it proves the claim.

### [INC-0629](../../incidents/INC-0629-a-ruling-said-a-test-helper-needed-no-revision-route-because.md) - A ruling said a test helper needed no revision route because one search seemed to show it was in no identity manifest, and the full gate then failed that check on exactly that entry
- occurrences 1, severity medium, status mitigated
- **Signature:** A repo checker that runs in under a second fails late in a long gate on a point already ruled.
- **Rule:** Before ruling a route, run the repo's own checker on the candidate tip instead of inferring from a search.

### [INC-0457](../../incidents/INC-0457-a-ruling-wrote-a-media-directory-binding-from-memory-that-co.md) - A ruling wrote a media directory binding from memory that contradicted the pinned scripts, and the runner stopped instead of substituting
- occurrences 1, severity low, status fixed
- **Signature:** A written binding contradicted the scripts it was meant to drive.
- **Rule:** Check a binding against the pinned scripts before writing it, and stop on a contradiction rather than substitute

### [INC-0549](../../incidents/INC-0549-a-reviewer-wrote-its-own-browser-only-driver-to-reach-a-muta.md) - A reviewer wrote its own browser-only driver to reach a mutant after the row runner stopped at an integration red, without asking
- occurrences 1, severity low, status mitigated
- **Signature:** The standard runner cannot reach the part of a row a mutant needs, and the runner is replaced by an ad hoc script.
- **Rule:** When a mutant needs only part of a row, ask the lead first; do not write a private driver, and run every restored green through the standard runner.

### [INC-0576](../../incidents/INC-0576-a-reviewer-tested-a-proposed-supersession-line-with-the-real.md) - A reviewer tested a proposed supersession line with the real checker and found it in the wrong form for an already active predecessor
- occurrences 1, severity low, status mitigated
- **Signature:** A replacement marker is written in the form for a pending predecessor when the predecessor is already active.
- **Rule:** Test a proposed replacement marker with the real checker, and use the form that matches the predecessor state.

### [INC-0612](../../incidents/INC-0612-a-ruling-set-a-lock-wait-the-installed-lock-could-not-honour.md) - A ruling set a lock wait the installed lock could not honour, because the tool hard-codes the wait and reads no variable
- occurrences 1, severity low, status mitigated
- **Signature:** A ruling names a tool parameter that the installed tool does not expose.
- **Rule:** Before ruling a parameter, read the tool to confirm it exposes that parameter; if a ruling cannot be carried out as written, ask instead of improvising a copy.

### [INC-0614](../../incidents/INC-0614-a-signed-command-allow-list-written-from-the-runtime-list-om.md) - A signed command allow-list written from the runtime list omitted the commands the packet's own test-first and static steps needed, and the engineer stopped
- occurrences 1, severity low, status mitigated
- **Signature:** A packet requires a step whose command is not on its own signed allow-list.
- **Rule:** Derive a signed command allow-list by walking every required step of the packet, including test-first reds and static gates, not from the runtime list alone.

### [INC-0615](../../incidents/INC-0615-a-gate-order-put-the-typecheck-right-after-type-generation-w.md) - A gate order put the typecheck right after type generation without walking the type dependency, and the engineer stopped again
- occurrences 1, severity low, status mitigated
- **Signature:** A gate required green immediately after a step that creates the error it checks.
- **Rule:** Before ordering gates, trace each generated artifact to every caller it can break, and place the typecheck after the step that fixes the last caller.

### [INC-0621](../../incidents/INC-0621-a-gate-list-named-a-pending-root-validator-after-a-pure-rena.md) - A gate list named a pending-root validator after a pure-rename activation that removes the very payload the validator requires, and the engineer stopped
- occurrences 1, severity low, status mitigated
- **Signature:** A named gate cannot pass on the tree the preceding step produces.
- **Rule:** Before naming a check in a gate list, read what the check requires and confirm it can pass on the post-step tree.

### [INC-0665](../../incidents/INC-0665-a-process-spec-required-a-check-to-pass-before-the-event-tha.md) - A process spec required a check to pass before the event that triggers the check
- occurrences 1, severity low, status fixed
- **Signature:** A phase list places a gate before an event, and the check behind that gate only starts when the event happens.
- **Rule:** When specifying approval phases, name the event that triggers each check and walk the sequence to confirm it can run in that order; a gate must never wait on a result that exists only after the step it gates.
