# Your order collided with a tool rule, permission ceiling, guard or pin

[Catalog](../README.md) / [delegation](README.md) / order-collides-with-rule-or-guard

**Go here if:** A teammate refused a ruled helper or cannot run a removal; a gate or command guard refused the target you named; an approval prompt fired despite a chat pre-approval; you broke a rule you wrote

**Rule:** Before issuing an order, read it against the executor's tool rules and permission ceiling and the guards or digest pins of every command and file it names; a ruling never overrides those rules, a shared service restart belongs to its owner, and the rules you write for teammates bind your own shell too.

8 incidents, 8 occurrences. Ordered by occurrences, then severity, then id.

## Incidents

### [INC-0179](../../incidents/INC-0179-a-chat-pre-approval-did-not-lift-an-explicit-approval-rule.md) - A chat pre-approval did not lift an explicit approval rule
- occurrences 1, severity medium, status fixed
- **Signature:** An upload stalled on an approval prompt that expired.
- **Rule:** When an approval prompt expires, queue and report; never rephrase around the rule.

### [INC-0270](../../incidents/INC-0270-restarting-a-shared-dispatcher-is-the-shared-owner-decision.md) - Restarting a shared dispatcher is the shared owner decision
- occurrences 1, severity medium, status fixed
- **Signature:** A team lead could have restarted a shared dispatcher that affects all teams.
- **Rule:** Leave a shared service restart to its shared owner

### [INC-0654](../../incidents/INC-0654-a-successful-teammate-spawn-masked-zero-turns-on-a-disabled.md) - A successful teammate spawn masked zero turns on a disabled model
- occurrences 1, severity medium, status mitigated
- **Signature:** A spawn command returns a thread identifier for a model the operator's standing rule marks as disabled, but no teammate turn or first checkpoint file appears.
- **Rule:** Before assigning work, reconcile any user-named resource against standing disabled-resource rules; after spawn, verify an actual first turn or required checkpoint artifact within minutes. A returned thread ID is not evidence of execution.

### [INC-0452](../../incidents/INC-0452-a-ruling-cannot-override-a-teammate-tool-rules-so-the-lead-s.md) - A ruling cannot override a teammate tool rules, so the lead sleep loop load waiter was refused and withdrawn
- occurrences 1, severity low, status fixed
- **Signature:** A ruled helper was refused by the teammate it was meant for.
- **Rule:** Wait for load with an event driven observer owned by the lead, never a sleep loop in a teammate; a ruling does not override a teammate tool rules

### [INC-0453](../../incidents/INC-0453-teammates-cannot-remove-or-drop-so-teardown-belongs-to-the-l.md) - Teammates cannot remove or drop, so teardown belongs to the lead and runs from the runner names file
- occurrences 1, severity low, status fixed
- **Signature:** Cleanup could not be run by the teammate that created the things.
- **Rule:** Plan teardown as a lead owned step driven from the runner names file, and keep walk pass and cleanup pass separate

### [INC-0473](../../incidents/INC-0473-a-test-file-was-edited-on-order-although-its-digest-was-pinn.md) - A test file was edited on order although its digest was pinned by the test authors, and the integrity gate refused the run before it started
- occurrences 1, severity low, status fixed
- **Signature:** An ordered test edit made the integrity gate refuse the run before it started.
- **Rule:** Before ordering an edit to a test file, check whether a digest manifest pins it; if it does, route the change through a successor version authored by a test author, not a direct edit.

### [INC-0489](../../incidents/INC-0489-a-rule-written-in-teammate-briefs-was-broken-by-the-lead-in.md) - A rule written in teammate briefs was broken by the lead in its own shell
- occurrences 1, severity low, status mitigated
- **Signature:** The author of a standing rule broke it by reflex while setting up a new work tree.
- **Rule:** A rule written in teammate briefs binds the lead's own shell too; read your own command against the standing rules before running it, and undo any slip by its exact recorded name before any run.

### [INC-0493](../../incidents/INC-0493-an-order-named-a-scratch-target-without-reading-the-guard-of.md) - An order named a scratch target without reading the guard of the command that would fill it
- occurrences 1, severity low, status mitigated
- **Signature:** The target named in the order was on the list of targets the named command refuses.
- **Rule:** Before naming a target in an order, read the guards of every command you name against that target.
