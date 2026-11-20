# identity-and-keying

[Catalog](../README.md) / identity-and-keying

Two distinct things share one identifier or cache key, so state computed for one is served for the other: a slot number a rejection recycles, a cache keyed on a mutable name, a record cited by its position in a re-sorted list.

**Ask:** Is this key unique across everything it will ever be asked about, or only across the subset that succeeded?

36 incidents filed here (36 occurrences); 19 more filed elsewhere are also tagged identity-and-keying.

## Incidents

This class has no topics, so this node is the leaf. Ordered by occurrences, then severity, then id.

### [INC-0027](../../incidents/INC-0027-a-cache-keyed-on-a-recycled-id-judged-each-record-on-its-pre.md) - A cache keyed on a recycled id judged each record on its predecessor's evidence
- occurrences 1, severity critical, status fixed
- **Signature:** A mass verdict whose stated reason is IDENTICAL across hundreds of distinct inputs. Runtime is also far higher than it should be, because the cache is not actually caching anything.
- **Rule:** Never key derived evidence on an identifier a rejection can recycle: 'next free' ids are unique only among ACCEPTED records. Before believing a mass verdict, count its DISTINCT reasons - one identical reason across hundreds of inputs indicts the judge, not the data. Always re-run a gate on the full population; a hand-labelled sample finds only the false positives it contains.

### [INC-0080](../../incidents/INC-0080-two-writers-used-the-same-short-question-id-for-different-ga.md) - Two writers used the same short question ID for different gaps, so a real gap looked ruled
- occurrences 1, severity medium, status fixed
- **Signature:** A shared question table uses short bare names, and several writers add questions without a namespace.
- **Rule:** Give every shared ID a namespace one writer owns, such as the row or author; a bare short name is a collision waiting to happen.

### [INC-0122](../../incidents/INC-0122-a-digest-present-anywhere-in-a-manifest-was-taken-as-proof-i.md) - A digest present anywhere in a manifest was taken as proof it belonged to its file
- occurrences 1, severity medium, status fixed
- **Signature:** A check finds the digest somewhere in the manifest and passes.
- **Rule:** Verify pairs, not membership.

### [INC-0125](../../incidents/INC-0125-a-marker-generator-listing-every-earlier-unmarked-root-made.md) - A marker generator listing every earlier unmarked root made a root approved later repeat an old path that a later marker already held
- occurrences 1, severity medium, status fixed
- **Signature:** Two markers name the same old path because a generator listed all earlier unmarked roots.
- **Rule:** Check uniqueness across all markers, and re-read inputs immediately before reporting.

### [INC-0130](../../incidents/INC-0130-an-identity-checker-rejecting-every-shared-destination-acros.md) - An identity checker rejecting every shared destination across pending roots flagged inert drafts
- occurrences 1, severity medium, status fixed
- **Signature:** Two pending drafts name one destination and the checker fails.
- **Rule:** Enforce destination uniqueness where files become active.

### [INC-0149](../../incidents/INC-0149-marker-sha-reviewer-approval-scope-successor-closure-and-act.md) - Marker SHA, reviewer approval scope, successor closure and activation ownership were treated as one fact
- occurrences 1, severity medium, status fixed
- **Signature:** A marker is read as proof of approval, closure and ownership at once.
- **Rule:** One fact per field.

### [INC-0154](../../incidents/INC-0154-a-marker-for-an-already-activated-revision-used-the-pending.md) - A marker for an already activated revision used the pending path form
- occurrences 1, severity medium, status fixed
- **Signature:** A marker was committed without running the identity checker on the exact tree.
- **Rule:** Run the identity checker on the exact tree before committing any marker.

### [INC-0157](../../incidents/INC-0157-a-split-ownership-root-could-not-activate-because-identity-h.md) - A split-ownership root could not activate because identity had no registry support
- occurrences 1, severity medium, status fixed
- **Signature:** The identity checker rejected a root whose file had been reassigned to another row.
- **Rule:** A root split by the registry needs registry-aware identity before its source row can activate.

### [INC-0161](../../incidents/INC-0161-landing-a-revision-beside-a-supersession-edge-broke-identity.md) - Landing a revision beside a supersession edge broke identity on main
- occurrences 1, severity medium, status fixed
- **Signature:** The landing script passed while the identity checker was red on main.
- **Rule:** Run the identity checker after every landing, not only after markers; resolve supersession sources only among earlier revisions.

### [INC-0164](../../incidents/INC-0164-a-reverted-and-re-landed-qa-revision-got-its-marker-approved.md) - A reverted and re-landed QA revision got its marker approved at the wrong commit
- occurrences 1, severity medium, status fixed
- **Signature:** The identity checker compared old active bytes at the approved commit.
- **Rule:** When a reverted revision is re-landed after an older copy became active, approve its marker at the re-land commit.

### [INC-0167](../../incidents/INC-0167-a-revision-marker-added-a-second-edge-to-bytes-the-previous.md) - A revision marker added a second edge to bytes the previous marker already claimed
- occurrences 1, severity medium, status fixed
- **Signature:** The identity check went red with an old digest mismatch on a marker that looked complete.
- **Rule:** Run the identity checker on a scratch clone before committing a marker, and take the edge from the newest pending earlier copy.

### [INC-0175](../../incidents/INC-0175-a-merge-of-main-left-an-activation-due-and-went-red.md) - A merge of main left an activation due and went red
- occurrences 1, severity medium, status fixed
- **Signature:** The merge commit was red on its own.
- **Rule:** A merge of main carries every activation its new markers make due.

### [INC-0182](../../incidents/INC-0182-a-marker-generator-covered-every-payload-of-a-root-when-only.md) - A marker generator covered every payload of a root when only part was approved
- occurrences 1, severity medium, status fixed
- **Signature:** A marker claimed more than the ruling approved.
- **Rule:** A marker covers only what the ruling approved.

The 23 entries below are listed by title only so this node stays under 12 KB. Open the page, or run `python3 tools/afm.py show INC-XXXX`, for its signature and rule.

- [INC-0204](../../incidents/INC-0204-a-precommit-check-reported-a-merge-brought-approval-as-unrea.md) - A precommit check reported a merge-brought approval as unreachable (n=1, medium)
- [INC-0216](../../incidents/INC-0216-a-scratch-swap-of-revision-bytes-failed-the-identity-gate-as.md) - A scratch swap of revision bytes failed the identity gate as designed (n=1, medium)
- [INC-0240](../../incidents/INC-0240-an-auto-merge-of-a-helper-could-lose-an-activation-or-covera.md) - An auto-merge of a helper could lose an activation or coverage unnoticed (n=1, medium)
- [INC-0261](../../incidents/INC-0261-a-landed-root-revision-cannot-carry-its-supersession-file-in.md) - A landed root revision cannot carry its supersession file in the same commit (n=1, medium)
- [INC-0279](../../incidents/INC-0279-replacing-an-active-test-file-moves-the-replacement-its-supe.md) - Replacing an active test file moves the replacement, its supersession record and the registry line in one commit (n=1, medium)
- [INC-0341](../../incidents/INC-0341-a-registration-subject-pinned-to-the-current-local-head-read.md) - A registration subject pinned to the current local head read as stale under a push freeze (n=1, medium)
- [INC-0359](../../incidents/INC-0359-a-stored-admission-record-left-out-the-tool-versions-it-was.md) - A stored admission record left out the tool versions it was produced under (n=1, medium)
- [INC-0513](../../incidents/INC-0513-an-activation-moved-a-superseded-root-s-spec-while-main-carr.md) - An activation moved a superseded root's spec while main carried the approved successor edge, and identity failed only after the merge (n=1, medium)
- [INC-0594](../../incidents/INC-0594-a-successor-draft-named-as-its-old-bytes-a-revision-that-was.md) - A successor draft named as its old bytes a revision that was never approved, so it cannot land against the bytes on main (n=1, medium)
- [INC-0595](../../incidents/INC-0595-an-approval-header-named-the-review-commit-whose-tree-did-no.md) - An approval header named the review commit, whose tree did not yet hold the reviewed root, and the identity checker refused it (n=1, medium)
- [INC-0054](../../incidents/INC-0054-a-display-name-drifted-from-the-model-identifier-it-was-supp.md) - A display name drifted from the model identifier it was supposed to describe (n=1, low)
- [INC-0079](../../incidents/INC-0079-a-second-writer-reused-a-shared-registry-s-batch-name-and-it.md) - A second writer reused a shared registry's batch name and its entries silently vanished (n=1, low)
- [INC-0386](../../incidents/INC-0386-a-path-identity-guard-compared-strings-while-a-temp-director.md) - A path-identity guard compared strings while a temp directory has two spellings on the host (n=1, low)
- [INC-0397](../../incidents/INC-0397-a-pending-root-whose-supersession-line-said-review-pending-f.md) - A pending root whose supersession line said review pending failed the identity checker at landing (n=1, low)
- [INC-0403](../../incidents/INC-0403-the-identity-checker-allowed-a-successor-root-s-new-path-wit.md) - The identity checker allowed a successor root's new path with no predecessor line, and a marker maps only replaced paths (n=1, low)
- [INC-0419](../../incidents/INC-0419-a-registry-edit-failed-its-own-sorted-order-assertion-and-th.md) - A registry edit failed its own sorted-order assertion, and the identity checker refuses a supersession whose old path the registry still names (n=1, low)
- [INC-0433](../../incidents/INC-0433-a-job-text-swapped-two-commit-identities-and-reading-the-log.md) - A job text swapped two commit identities, and reading the log caught it (n=1, low)
- [INC-0448](../../incidents/INC-0448-two-fields-mapping-to-one-database-enum-made-the-generated-m.md) - Two fields mapping to one database enum made the generated migration narrow a five-state status to two states (n=1, low)
- [INC-0481](../../incidents/INC-0481-two-new-work-item-ids-were-minted-from-the-current-list-alon.md) - Two new work item ids were minted from the current list alone, and both had already been used by merged work (n=1, low)
- [INC-0486](../../incidents/INC-0486-an-approval-on-main-was-not-an-ancestor-of-the-branch-that-n.md) - An approval on main was not an ancestor of the branch that needed it (n=1, low)
- [INC-0492](../../incidents/INC-0492-a-successor-test-root-was-named-so-the-identity-checker-coul.md) - A successor test root was named so the identity checker could never accept it as a successor (n=1, low)
- [INC-0514](../../incidents/INC-0514-an-implementer-proposed-editing-a-pinned-root-s-mock-to-fit.md) - An implementer proposed editing a pinned root's mock to fit a new helper contract, and the fix was a wrapper that kept the mocked shape (n=1, low)
- [INC-0520](../../incidents/INC-0520-a-manifest-listed-its-lines-unsorted-and-the-landing-gate-re.md) - A manifest listed its lines unsorted and the landing gate refused it (n=1, low)

## Also tagged identity-and-keying

19 incidents filed under another home class also carry this class. Listed by the node where they live:

- [spec-and-scope](../spec-and-scope/README.md): INC-0055, INC-0085, INC-0099, INC-0121, INC-0147, INC-0159, INC-0326, INC-0335, INC-0353
- [detector-fail-open](../detector-fail-open/README.md): INC-0108, INC-0176, INC-0186
- [test-isolation](../test-isolation/README.md): INC-0097, INC-0360
- [vcs-destruction](../vcs-destruction/README.md): INC-0185, INC-0226
- [delegation](../delegation/README.md): INC-0220
- [false-green](../false-green/README.md): INC-0083
- [tooling-paths](../tooling-paths/README.md): INC-0043
