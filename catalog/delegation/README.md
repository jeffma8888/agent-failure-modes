# delegation

[Catalog](../README.md) / delegation

A sub-agent re-delegates instead of doing the work: it spawns another loop, scaffolds a plan for a future iteration, and exits successfully having produced nothing.

**Ask:** Does the instruction forbid EVERY escape hatch - nested agents, scaffolding a loop, handing off to a later iteration - by name?

44 incidents filed here (44 occurrences); 21 more filed elsewhere are also tagged delegation.

## Incidents

This class has no topics, so this node is the leaf. Ordered by occurrences, then severity, then id.

### [INC-0016](../../incidents/INC-0016-anti-delegation-clause-must-forbid-scaffold-a-loop-too.md) - Anti-delegation clause must forbid 'scaffold a loop' too
- occurrences 1, severity high, status mitigated
- **Signature:** A subagent instructed to do work returns quickly and successfully, but the expected output file is empty or missing. Meanwhile a new nested loop or a prd.json / prompt.md scaffold appears alongside.
- **Rule:** A subagent reads 'do not spawn a nested agent' literally. Forbid every escape hatch by name in the SAME clause: nested agents, scaffolding a loop, writing prd/prompt/progress files, launching detached processes, handing off to a future iteration. Include the clause INLINE, not by reference. Kill an unauthorized loop by removing its required input, not just its pid.

### [INC-0630](../../incidents/INC-0630-a-lead-ended-its-turn-waiting-for-a-reviewer-s-completion-me.md) - A lead ended its turn waiting for a reviewer's completion message while the reviewer's finished files were already on disk, and nothing moved for days
- occurrences 1, severity high, status mitigated
- **Signature:** A team is idle while the work it waits for is already on disk.
- **Rule:** Act on verified on-disk outputs when the author is silent, and never end a turn waiting on a message alone.

### [INC-0017](../../incidents/INC-0017-a-killed-detached-loop-resurrects-with-a-new-ppid.md) - A killed detached loop resurrects with a new PPID
- occurrences 1, severity medium, status fixed
- **Signature:** You kill the loop's pid. Later, `ps` shows a fresh pid with ppid 1, running the same loop script, on a new sleep-backoff cycle.
- **Rule:** To stop a well-behaved detached loop, remove the input it polls (a STOP file it honors), not just its pid - a supervisor or scheduler can re-launch a killed pid. Same argv on a new pid = auto-resurrection; different argv = a fresh authorized launch. Hunt the launcher accordingly, and leave a documented STOP so you and the other session do not fight over the process.

The 41 entries below are listed by title only so this node stays under 12 KB. Open the page, or run `python3 tools/afm.py show INC-XXXX`, for its signature and rule.

- [INC-0087](../../incidents/INC-0087-an-import-level-audit-missed-helper-calls-that-needed-a-late.md) - An import-level audit missed helper calls that needed a later row, and only the engineer stop rule caught it (n=1, medium)
- [INC-0091](../../incidents/INC-0091-teammate-replies-arrived-while-the-lead-was-busy-and-were-mi.md) - Teammate replies arrived while the lead was busy and were missed, leaving finished work idle for about 30 minutes (n=1, medium)
- [INC-0098](../../incidents/INC-0098-an-acyclic-declared-dependency-graph-hid-producer-rows-that.md) - An acyclic declared dependency graph hid producer rows that an acceptance file needed (n=1, medium)
- [INC-0128](../../incidents/INC-0128-finished-work-sat-for-hours-because-replies-never-arrived-th.md) - Finished work sat for hours because replies never arrived, the clock was misread and worktrees were not swept (n=1, medium)
- [INC-0135](../../incidents/INC-0135-a-qa-template-line-pasted-into-an-engineer-task-contradicted.md) - A QA-template line pasted into an engineer task contradicted the engineer commit duty (n=1, medium)
- [INC-0179](../../incidents/INC-0179-a-chat-pre-approval-did-not-lift-an-explicit-approval-rule.md) - A chat pre-approval did not lift an explicit approval rule (n=1, medium)
- [INC-0201](../../incidents/INC-0201-two-review-titles-named-the-wrong-reviewer.md) - Two review titles named the wrong reviewer (n=1, medium)
- [INC-0206](../../incidents/INC-0206-a-guessed-commit-id-was-sent-to-two-teammates.md) - A guessed commit id was sent to two teammates (n=1, medium)
- [INC-0220](../../incidents/INC-0220-a-reviewer-proposed-text-was-at-risk-of-being-applied-by-its.md) - A reviewer proposed text was at risk of being applied by its own author (n=1, medium)
- [INC-0237](../../incidents/INC-0237-a-team-runtime-cap-blocked-new-teammates-behind-retained-idl.md) - A team runtime cap blocked new teammates behind retained idle ones (n=1, medium)
- [INC-0263](../../incidents/INC-0263-refresh-the-team-roster-at-each-phase-change.md) - Refresh the team roster at each phase change (n=1, medium)
- [INC-0270](../../incidents/INC-0270-restarting-a-shared-dispatcher-is-the-shared-owner-decision.md) - Restarting a shared dispatcher is the shared owner decision (n=1, medium)
- [INC-0277](../../incidents/INC-0277-sign-the-stable-re-checked-part-of-a-design-addendum-instead.md) - Sign the stable re-checked part of a design addendum instead of waiting (n=1, medium)
- [INC-0298](../../incidents/INC-0298-harness-and-ownership-defects-were-left-for-the-build-agent.md) - Harness and ownership defects were left for the build agent to find (n=1, medium)
- [INC-0317](../../incidents/INC-0317-finished-teammates-sat-unnoticed-because-their-completion-re.md) - Finished teammates sat unnoticed because their completion replies never arrived (n=1, medium)
- [INC-0331](../../incidents/INC-0331-a-job-edited-a-file-outside-its-brief.md) - A job edited a file outside its brief (n=1, medium)
- [INC-0337](../../incidents/INC-0337-reviewers-named-at-ruling-time-were-busy-when-the-artifact-l.md) - Reviewers named at ruling time were busy when the artifact landed (n=1, medium)
- [INC-0507](../../incidents/INC-0507-an-independence-rule-did-not-say-what-counts-as-an-agent-or.md) - An independence rule did not say what counts as an agent or as a part, and four of nine parallel slices stopped at once (n=1, medium)
- [INC-0573](../../incidents/INC-0573-teammate-replies-stopped-reaching-the-lead-for-about-25-minu.md) - Teammate replies stopped reaching the lead for about 25 minutes while their files landed on disk (n=1, medium)
- [INC-0379](../../incidents/INC-0379-splitting-a-review-s-amendments-kept-the-engineer-busy-while.md) - Splitting a review's amendments kept the engineer busy while decisions were pending (n=1, low)
- [INC-0385](../../incidents/INC-0385-two-engineers-answered-the-same-stop-diagnosis-independently.md) - Two engineers answered the same STOP diagnosis independently, and agreeing answers let the lead route at once (n=1, low)
- [INC-0392](../../incidents/INC-0392-a-declaration-request-that-split-sourced-values-from-decisio.md) - A declaration request that split sourced values from decisions let the lead rule eleven items in one pass (n=1, low)
- [INC-0399](../../incidents/INC-0399-a-final-review-was-reassigned-from-a-busy-reviewer-to-an-idl.md) - A final review was reassigned from a busy reviewer to an idle one of a different model instead of queueing (n=1, low)
- [INC-0410](../../incidents/INC-0410-the-lead-re-merged-the-full-candidate-itself-rather-than-que.md) - The lead re-merged the full candidate itself rather than queue behind the busy owner, and proved the delta path by path (n=1, low)
- [INC-0411](../../incidents/INC-0411-a-red-phase-may-start-while-a-spec-recheck-runs-because-the.md) - A red phase may start while a spec recheck runs because the reviewed bytes fix the behavior (n=1, low)
- [INC-0416](../../incidents/INC-0416-ten-teammate-threads-showed-state-paused-with-complete-outpu.md) - Ten teammate threads showed state paused with complete outputs on disk and no reply message (n=1, low)
- [INC-0423](../../incidents/INC-0423-a-review-was-reassigned-off-the-critical-path-so-the-reviewe.md) - A review was reassigned off the critical path so the reviewer who owned the blocking recheck stayed on it (n=1, low)
- [INC-0435](../../incidents/INC-0435-a-low-load-window-needed-immediate-dispatch-of-the-gated-run.md) - A low-load window needed immediate dispatch of the gated runs (n=1, low)
- [INC-0452](../../incidents/INC-0452-a-ruling-cannot-override-a-teammate-tool-rules-so-the-lead-s.md) - A ruling cannot override a teammate tool rules, so the lead sleep loop load waiter was refused and withdrawn (n=1, low)
- [INC-0453](../../incidents/INC-0453-teammates-cannot-remove-or-drop-so-teardown-belongs-to-the-l.md) - Teammates cannot remove or drop, so teardown belongs to the lead and runs from the runner names file (n=1, low)
- [INC-0467](../../incidents/INC-0467-a-run-plan-barred-the-test-author-from-running-the-script-an.md) - A run plan barred the test author from running the script, and a later message assigned that author anyway (n=1, low)
- [INC-0473](../../incidents/INC-0473-a-test-file-was-edited-on-order-although-its-digest-was-pinn.md) - A test file was edited on order although its digest was pinned by the test authors, and the integrity gate refused the run before it started (n=1, low)
- [INC-0489](../../incidents/INC-0489-a-rule-written-in-teammate-briefs-was-broken-by-the-lead-in.md) - A rule written in teammate briefs was broken by the lead in its own shell (n=1, low)
- [INC-0493](../../incidents/INC-0493-an-order-named-a-scratch-target-without-reading-the-guard-of.md) - An order named a scratch target without reading the guard of the command that would fill it (n=1, low)
- [INC-0517](../../incidents/INC-0517-two-reviewers-were-named-who-had-written-or-judged-the-roots.md) - Two reviewers were named who had written or judged the roots they were to review, and both stopped at the author check (n=1, low)
- [INC-0526](../../incidents/INC-0526-a-reviewer-was-named-after-checking-commit-authorship-only-a.md) - A reviewer was named after checking commit authorship only, and the reviewer had judged the root's cases in an earlier review file (n=1, low)
- [INC-0539](../../incidents/INC-0539-two-reviewers-in-a-row-were-assigned-a-slice-they-had-alread.md) - Two reviewers in a row were assigned a slice they had already worked on, because the pick did not search the record (n=1, low)
- [INC-0548](../../incidents/INC-0548-an-activator-could-not-recover-an-earlier-brief-mutant-text.md) - An activator could not recover an earlier brief mutant text, so it named its own mutant and said so (n=1, low)
- [INC-0589](../../incidents/INC-0589-the-only-copies-of-eight-reviewed-drafts-sat-untracked-in-on.md) - The only copies of eight reviewed drafts sat untracked in one worktree, and the ruling kept them untouched (n=1, low)
- [INC-0610](../../incidents/INC-0610-landing-a-review-moved-it-out-of-the-reviewer-tree-while-ano.md) - Landing a review moved it out of the reviewer tree while another teammate had been told to read it there (n=1, low)
- [INC-0635](../../incidents/INC-0635-a-review-was-assigned-to-a-reviewer-by-role-name-but-the-rev.md) - A review was assigned to a reviewer by role name, but the reviewer and the author ran the same model, so it was not an independent review (n=1, low)

## Also tagged delegation

21 incidents filed under another home class also carry this class. Listed by the node where they live:

- [spec-and-scope](../spec-and-scope/README.md): INC-0074, INC-0076, INC-0109, INC-0115, INC-0184, INC-0197, INC-0225, INC-0242, INC-0251, INC-0304
- [false-green](../false-green/README.md): INC-0042, INC-0232, INC-0233
- [tooling-paths](../tooling-paths/README.md): INC-0177, INC-0207, INC-0319
- [concurrency](../concurrency/README.md): INC-0557
- [ipc-and-env](../ipc-and-env/README.md): INC-0365
- [observability](../observability/README.md): INC-0041
- [stage-timeout](../stage-timeout/README.md): INC-0143
- [vcs-destruction](../vcs-destruction/README.md): INC-0103

## Practices touching this class

- [PRA-0001](../CORE.md#practices) - The enforcement ladder: pick the cheapest rung that makes the failure impossible
- [PRA-0005](../CORE.md#practices) - Admission control for an agent team on a shared host
