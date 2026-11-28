# delegation

[Catalog](../README.md) / delegation

A sub-agent re-delegates instead of doing the work: it spawns another loop, scaffolds a plan for a future iteration, and exits successfully having produced nothing.

**Ask:** Does the instruction forbid EVERY escape hatch - nested agents, scaffolding a loop, handing off to a later iteration - by name?

**You are probably here if:** Delegated work stalls or misfires: finished files but no reply, a reviewer stopping at an author check, an order a rule refuses, a brief with a gap.

46 incidents filed here (46 occurrences); 25 more filed elsewhere are also tagged delegation.

## Topics

n = occurrences: incidents filed in the topic plus their repeats.

| Topic | Go here if | n | Link |
|---|---|---|---|
| The reviewer or runner you named was not independent or not free | A reviewer stops at its own author check, runs the same model as the author, was pre-named and is busy when the artifact lands, would apply its own text, or an assignment breaks the independence rule | 9 | [reviewer-not-independent-or-free](reviewer-not-independent-or-free.md) |
| The brief or plan left a gap the worker fell through | A worker scaffolded a loop a clause did not name, edited a file the brief never listed, stopped on an undefined term, got another role's template line, or hit a prerequisite the audit missed | 8 | [brief-or-plan-left-a-gap](brief-or-plan-left-a-gap.md) |
| Your order collided with a tool rule, permission ceiling, guard or pin | A teammate refused a ruled helper or cannot run a removal; a gate or command guard refused the target you named; an approval prompt fired despite a chat pre-approval; you broke a rule you wrote | 8 | [order-collides-with-rule-or-guard](order-collides-with-rule-or-guard.md) |
| Parallel work stalls behind one busy owner, open decision or slot cap | Teammates sit idle while one part of a document, one busy owner, one undecided batch of amendments, a runtime cap or a brief low-load window holds everything. | 7 | [stalled-behind-one-owner-or-decision](stalled-behind-one-owner-or-decision.md) |
| Teammates finished on disk; the reply never came or went unnoticed | A thread shows finished or paused with no message, a reply arrived while you were busy and was never read, an output file stopped changing, or you are about to end a turn waiting on a message. | 6 | [finished-on-disk-no-reply](finished-on-disk-no-reply.md) |
| A record is guessed or stale, or lives only in a message or worktree | A wrong commit id in a message, a report naming the previous reviewer, a stale roster, a brief pointing at a tree-local path, text only in a message lost, or untracked worktree files as the only copy. | 6 | [guessed-or-stale-id-name-path](guessed-or-stale-id-name-path.md) |

## Class-level incidents

Filed in this class but in none of its topics.

### [INC-0017](../../incidents/INC-0017-a-killed-detached-loop-resurrects-with-a-new-ppid.md) - A killed detached loop resurrects with a new PPID
- occurrences 1, severity medium, status fixed
- **Signature:** You kill the loop's pid. Later, `ps` shows a fresh pid with ppid 1, running the same loop script, on a new sleep-backoff cycle.
- **Rule:** To stop a well-behaved detached loop, remove the input it polls (a STOP file it honors), not just its pid - a supervisor or scheduler can re-launch a killed pid. Same argv on a new pid = auto-resurrection; different argv = a fresh authorized launch. Hunt the launcher accordingly, and leave a documented STOP so you and the other session do not fight over the process.

### [INC-0385](../../incidents/INC-0385-two-engineers-answered-the-same-stop-diagnosis-independently.md) - Two engineers answered the same STOP diagnosis independently, and agreeing answers let the lead route at once
- occurrences 1, severity low, status fixed
- **Signature:** A STOP had an unknown cause and a single diagnosis would have been unchecked.
- **Rule:** When a STOP cause is unknown, ask for two independent static answers before routing the fix

## Also tagged delegation

25 incidents filed under another home class also carry this class. Listed by the node where they live:

- [spec-and-scope/missing-or-late-prerequisites](../spec-and-scope/missing-or-late-prerequisites.md): INC-0109, INC-0115, INC-0242, INC-0304
- [spec-and-scope/wrong-owner-path-or-scope](../spec-and-scope/wrong-owner-path-or-scope.md): INC-0074, INC-0076, INC-0197, INC-0251
- [false-green/oracle-or-claim-written-from-memory](../false-green/oracle-or-claim-written-from-memory.md): INC-0042, INC-0651, INC-0657
- [false-green/proxy-artifact-cited-as-evidence](../false-green/proxy-artifact-cited-as-evidence.md): INC-0232, INC-0233
- [concurrency](../concurrency/README.md): INC-0557
- [identity-and-keying/new-id-already-taken](../identity-and-keying/new-id-already-taken.md): INC-0671
- [ipc-and-env](../ipc-and-env/README.md): INC-0365
- [observability/missing-or-unverifiable-receipts](../observability/missing-or-unverifiable-receipts.md): INC-0041
- [spec-and-scope/fix-misses-related-consumers](../spec-and-scope/fix-misses-related-consumers.md): INC-0225
- [spec-and-scope/requirements-and-limits-collide](../spec-and-scope/requirements-and-limits-collide.md): INC-0655
- [spec-and-scope/tests-do-not-prove-the-contract](../spec-and-scope/tests-do-not-prove-the-contract.md): INC-0184
- [stage-timeout/work-outgrows-enforced-timeouts](../stage-timeout/work-outgrows-enforced-timeouts.md): INC-0143
- [tooling-paths/path-resolves-from-wrong-root](../tooling-paths/path-resolves-from-wrong-root.md): INC-0177
- [tooling-paths/tree-lacks-what-job-needs](../tooling-paths/tree-lacks-what-job-needs.md): INC-0319
- [tooling-paths/zsh-expansion-surprises](../tooling-paths/zsh-expansion-surprises.md): INC-0207
- [vcs-destruction](../vcs-destruction/README.md): INC-0103

## Practices touching this class

- [PRA-0001](../CORE.md#practices) - The enforcement ladder: pick the cheapest rung that makes the failure impossible
- [PRA-0005](../CORE.md#practices) - Admission control for an agent team on a shared host
