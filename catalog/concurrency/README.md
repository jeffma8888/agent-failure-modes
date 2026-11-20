# concurrency

[Catalog](../README.md) / concurrency

Independent agents or sessions contend for one shared resource - a rate-limited API quota, a git index, a working tree - and degrade or corrupt each other, often silently.

**Ask:** How many live agents share this one resource right now, and what happens to the one you are waiting on when a second appears?

20 incidents filed here (20 occurrences); 16 more filed elsewhere are also tagged concurrency.

## Incidents

This class has no topics, so this node is the leaf. Ordered by occurrences, then severity, then id.

### [INC-0011](../../incidents/INC-0011-concurrent-agent-brains-silently-starve-and-kill-each-other.md) - Concurrent agent brains silently starve and kill each other
- occurrences 1, severity critical, status mitigated
- **Signature:** Multiple tasks fail with 'Connection stalled - no data received for 120 s' plus occasional 'service is busy'. AC power is confirmed. A long-running dispatcher process is alive.
- **Rule:** Multiple agents share a model-provider quota, and the losing brain cannot degrade gracefully - it dies silently. Before ANY batch launch: count the live brains against one account, and if a dispatcher is already alive, either wait for a quiescent window or run inline. Signature: 'connection stalled 120s' plus 'service busy' on multiple tasks with confirmed AC power.

### [INC-0585](../../incidents/INC-0585-a-lock-protected-by-an-advisory-lock-on-a-file-opened-by-pat.md) - A lock protected by an advisory lock on a file opened by path let two holders run when the file was replaced
- occurrences 1, severity high, status mitigated
- **Signature:** A guard file is unlinked and recreated, and the next caller locks a new file object.
- **Rule:** After taking a lock on a file opened by path, compare the open file identity with the path identity and retry on mismatch; never create a silent new guard.

### [INC-0587](../../incidents/INC-0587-a-release-removed-a-lock-link-by-owner-text-without-checking.md) - A release removed a lock link by owner text without checking that the link pointed at the caller's own stage
- occurrences 1, severity high, status mitigated
- **Signature:** A release compares text and removes a link that may now belong to another holder.
- **Rule:** A release removes a lock only after proving, under the guard, that the lock target is the caller's own recorded stage.

### [INC-0066](../../incidents/INC-0066-a-worker-s-end-of-run-cleanup-deleted-a-shared-scratch-direc.md) - A worker's end-of-run cleanup deleted a shared scratch directory, taking the coordinator's live watcher and its log with it
- occurrences 1, severity medium, status mitigated
- **Signature:** Two agents are told to use the same scratch directory, and one of them finishes by deleting the directory recursively.
- **Rule:** Delete only the files you created, by name, never a parent directory you were pointed at; a successful create-parents call says nothing about ownership. Give each worker its own scratch subdirectory, never run a live control process from shared temp space, and report every delete.

### [INC-0117](../../incidents/INC-0117-signalling-a-process-group-of-only-zombie-members-returned-a.md) - Signalling a process group of only zombie members returned a permission error on macOS
- occurrences 1, severity medium, status fixed
- **Signature:** Cleanup fails intermittently when the group has exited but not been reaped.
- **Rule:** Repeat race-dependent cleanup tests; classify errors by what they mean for the target.

### [INC-0219](../../incidents/INC-0219-a-shared-host-reached-load-491-and-unrelated-deadlines-faile.md) - A shared host reached load 491 and unrelated deadlines failed
- occurrences 1, severity medium, status fixed
- **Signature:** Unrelated deadlines failed under a shared load.
- **Rule:** Cap concurrent heavy runs across the team and record load at start and end

### [INC-0305](../../incidents/INC-0305-a-process-the-sandbox-could-not-see-was-judged-dead-and-its.md) - A process the sandbox could not see was judged dead and its live run was removed
- occurrences 1, severity medium, status fixed
- **Signature:** A run directory vanished mid run after another agent removed a registration it judged dead.
- **Rule:** A process your sandbox cannot see is not a dead process; ownership comes from your own run record, not from visibility or timing

### [INC-0313](../../incidents/INC-0313-tests-in-a-parallel-group-raced-a-test-that-drops-the-shared.md) - Tests in a parallel group raced a test that drops the shared inventory
- occurrences 1, severity medium, status fixed
- **Signature:** A single-file run passed or failed alone while the full parallel run could race.
- **Rule:** A test that creates shared resources goes in a serial group with no concurrent inventory reader; a focused single-file run is not evidence of isolation

### [INC-0324](../../incidents/INC-0324-a-periodic-status-sweep-took-the-index-lock-of-a-teammate-s.md) - A periodic status sweep took the index lock of a teammate's worktree
- occurrences 1, severity medium, status fixed
- **Signature:** A teammate's staging step failed on a lock created by the coordinator's monitor.
- **Rule:** A monitor of someone else's worktree must be lock free (no index refresh) or not touch that worktree at all; never delete a lock you did not create

### [INC-0368](../../incidents/INC-0368-a-new-worktree-symlinked-its-dependency-trees-to-another-wor.md) - A new worktree symlinked its dependency trees to another worktree's, and the package manager relinked through them
- occurrences 1, severity medium, status fixed
- **Signature:** A package manager command in one worktree changed the dependency links of another worktree.
- **Rule:** Never share a dependency tree between worktrees by symlink; give each worktree a private clone; never run the package manager unless the exact command is authorized; keep the verify-before-run settings off for every child; compare the full link inventory against a clean sibling after any suspected mutation

### [INC-0522](../../incidents/INC-0522-a-helper-script-was-edited-in-place-while-another-process-wa.md) - A helper script was edited in place while another process was executing it, and that run died with a syntax error at a shifted line
- occurrences 1, severity medium, status mitigated
- **Signature:** A script that other threads run is rewritten in place, and a running shell fails at a line number that no longer matches.
- **Rule:** Never rewrite a script in place while any process may run it; write a new file and switch names, and quote the helper hash in the evidence that used it.

### [INC-0554](../../incidents/INC-0554-a-host-wide-load-gate-held-a-one-shot-time-windowed-check-un.md) - A host-wide load gate held a one-shot, time-windowed check until its window passed, because processes outside the team drove the load
- occurrences 1, severity medium, status open
- **Signature:** Every runtime job, from a full suite to one read-only browser check, waits for the same host one-minute load average to fall under a fixed limit, while processes the team does not own set that load.
- **Rule:** Do not let one host-wide load threshold admit every job alike: size the gate to the job, attribute the load to its owners first, and reserve capacity for any observation that has a deadline.

### [INC-0575](../../incidents/INC-0575-a-lock-design-passed-its-own-14-tests-and-a-reviewer-s-four.md) - A lock design passed its own 14 tests, and a reviewer's four forced interleavings each broke it
- occurrences 1, severity medium, status mitigated
- **Signature:** Tests of the happy paths pass, and timing between two steps of publication is untested.
- **Rule:** A lock or queue needs tests that force a signal or cancel between every pair of publication steps; publish ownership atomically and only when complete.

### [INC-0048](../../incidents/INC-0048-citing-an-identifier-in-the-same-parallel-tool-block-that-cr.md) - Citing an identifier in the same parallel tool block that creates it makes the citation a guess
- occurrences 1, severity low, status fixed
- **Signature:** One batch of parallel tool calls contains both a step that creates an identifier (commit hash, ticket number, file path) and a step that quotes it.
- **Rule:** Never cite an identifier produced by a step that has not returned yet. If call B needs a value from call A, B goes in a later block and quotes what A actually returned.

### [INC-0445](../../incidents/INC-0445-a-migration-lock-covered-the-whole-branch-when-it-needed-to.md) - A migration lock covered the whole branch when it needed to cover only the generators and schema paths
- occurrences 1, severity low, status fixed
- **Signature:** A second branch idled although most of its work did not touch the locked resource.
- **Rule:** Scope a lock to the shared paths and commands it protects, not the whole branch, and state how a second branch rejoins after the holder merges

### [INC-0471](../../incidents/INC-0471-drafts-proposed-test-database-ports-by-reading-tracked-text.md) - Drafts proposed test database ports by reading tracked text, and two clashed with each other and two with live listeners
- occurrences 1, severity low, status fixed
- **Signature:** Proposed numbers collided with each other and with live listeners.
- **Rule:** Allocate shared numbered resources centrally and probe the live system at use time; a text search for free numbers is not a probe

### [INC-0544](../../incidents/INC-0544-a-walk-load-limit-was-unreachable-because-the-host-floor-wit.md) - A walk load limit was unreachable because the host floor without any team job sat above it
- occurrences 1, severity low, status mitigated
- **Signature:** A wait-for-load limit is below the idle load of the host, so every admission would wait forever.
- **Rule:** Measure the host load floor with no team job before fixing an admission limit; if the floor is above it, use the documented scoped limit and serialize the other runtime jobs.

### [INC-0556](../../incidents/INC-0556-a-polling-host-lock-does-not-serve-waiters-in-order-so-a-tes.md) - A polling host lock does not serve waiters in order, so a test run queued after its own setup took the lock first and failed on a database setup had not created
- occurrences 1, severity low, status open
- **Signature:** Two dependent steps are queued as separate acquisitions of a lock that waiters poll for, and the later one runs first.
- **Rule:** Never rely on start order across separate acquisitions of a polling lock; run dependent steps under one acquisition or use a first-come ticket lock.

The 2 entries below are listed by title only so this node stays under 12 KB. Open the page, or run `python3 tools/afm.py show INC-XXXX`, for its signature and rule.

- [INC-0557](../../incidents/INC-0557-the-lock-holder-waited-for-the-load-to-fall-while-still-hold.md) - The lock holder waited for the load to fall while still holding the host lock, and eleven agents fed that one lock, so waits of 20 minutes became normal (n=1, low)
- [INC-0558](../../incidents/INC-0558-two-agents-cancelled-their-queued-heavy-jobs-by-task-id-duri.md) - Two agents cancelled their queued heavy jobs by task id during a pause, but the queued shells survived; one later took the host lock and ran its test after the agent had reported it cancelled (n=1, low)

## Also tagged concurrency

16 incidents filed under another home class also carry this class. Listed by the node where they live:

- [test-isolation](../test-isolation/README.md): INC-0038, INC-0132, INC-0136, INC-0138, INC-0169
- [vcs-destruction](../vcs-destruction/README.md): INC-0012, INC-0013, INC-0229
- [false-green](../false-green/README.md): INC-0104, INC-0329
- [identity-and-keying](../identity-and-keying/README.md): INC-0079, INC-0125
- [tooling-paths](../tooling-paths/README.md): INC-0030, INC-0043
- [delegation](../delegation/README.md): INC-0237
- [stage-timeout](../stage-timeout/README.md): INC-0092

## Practices touching this class

- [PRA-0001](../CORE.md#practices) - The enforcement ladder: pick the cheapest rung that makes the failure impossible
- [PRA-0005](../CORE.md#practices) - Admission control for an agent team on a shared host
