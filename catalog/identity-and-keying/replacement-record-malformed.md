# A file-replacement (supersession) record is refused or claims too much

[Catalog](../README.md) / [identity-and-keying](README.md) / replacement-record-malformed

**Go here if:** A record saying which file replaces which is refused or over-claims: duplicate edge, more edges than approved, name outside its family, old path in pending form, old digest not on main, unsorted list.

**Rule:** A replacement record maps exactly the paths the ruling approved; its old path takes the predecessor's current form (active once activated, else the newest pending copy), its old digest the bytes on main, never an unapproved chain; the new name sits inside the family; land it with its registry line and moved file in one commit, manifest sorted; run the checker's own rule on a scratch clone first.

14 incidents, 14 occurrences. Ordered by occurrences, then severity, then id.

## Incidents

### [INC-0279](../../incidents/INC-0279-replacing-an-active-test-file-moves-the-replacement-its-supe.md) - Replacing an active test file moves the replacement, its supersession record and the registry line in one commit
- occurrences 2, severity medium, status fixed
- **Signature:** A supersession record was refused in both path forms because the replacement had not moved yet.
- **Rule:** Move a replacement, its supersession record and its registry line together in one commit when the old file is already active
- **Recurrences:**
  - [INC-0419](../../incidents/INC-0419-a-registry-edit-failed-its-own-sorted-order-assertion-and-th.md) - 2026-11-02 - A registry edit failed its own sorted-order assertion, and the identity checker refuses a supersession whose old path the registry still names

### [INC-0130](../../incidents/INC-0130-an-identity-checker-rejecting-every-shared-destination-acros.md) - An identity checker rejecting every shared destination across pending roots flagged inert drafts
- occurrences 1, severity medium, status fixed
- **Signature:** Two pending drafts name one destination and the checker fails.
- **Rule:** Enforce destination uniqueness where files become active.

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

### [INC-0167](../../incidents/INC-0167-a-revision-marker-added-a-second-edge-to-bytes-the-previous.md) - A revision marker added a second edge to bytes the previous marker already claimed
- occurrences 1, severity medium, status fixed
- **Signature:** The identity check went red with an old digest mismatch on a marker that looked complete.
- **Rule:** Run the identity checker on a scratch clone before committing a marker, and take the edge from the newest pending earlier copy.

### [INC-0182](../../incidents/INC-0182-a-marker-generator-covered-every-payload-of-a-root-when-only.md) - A marker generator covered every payload of a root when only part was approved
- occurrences 1, severity medium, status fixed
- **Signature:** A marker claimed more than the ruling approved.
- **Rule:** A marker covers only what the ruling approved.

### [INC-0216](../../incidents/INC-0216-a-scratch-swap-of-revision-bytes-failed-the-identity-gate-as.md) - A scratch swap of revision bytes failed the identity gate as designed
- occurrences 1, severity medium, status fixed
- **Signature:** The gate failed for the right reason, which the proof had not intended.
- **Rule:** Use the real approved chain in a causal proof, not just the bytes

### [INC-0594](../../incidents/INC-0594-a-successor-draft-named-as-its-old-bytes-a-revision-that-was.md) - A successor draft named as its old bytes a revision that was never approved, so it cannot land against the bytes on main
- occurrences 1, severity medium, status mitigated
- **Signature:** A successor line names old bytes that differ from the helper actually on main.
- **Rule:** Before landing a successor, check that its named old bytes equal the bytes on main; if they name an unapproved revision, park it.

### [INC-0403](../../incidents/INC-0403-the-identity-checker-allowed-a-successor-root-s-new-path-wit.md) - The identity checker allowed a successor root's new path with no predecessor line, and a marker maps only replaced paths
- occurrences 1, severity low, status fixed
- **Signature:** A successor root added a path that had no earlier copy, and it was unclear whether a marker line was owed.
- **Rule:** A marker maps only replaced paths; a successor's new path needs no predecessor line

### [INC-0492](../../incidents/INC-0492-a-successor-test-root-was-named-so-the-identity-checker-coul.md) - A successor test root was named so the identity checker could never accept it as a successor
- occurrences 1, severity low, status mitigated
- **Signature:** The successor carried a name from a different family than the root it replaced.
- **Rule:** Name a successor after the family it supersedes, and read the checker's acceptance rule before writing the mapping; never loosen the gate to fit the artifact.

### [INC-0514](../../incidents/INC-0514-an-implementer-proposed-editing-a-pinned-root-s-mock-to-fit.md) - An implementer proposed editing a pinned root's mock to fit a new helper contract, and the fix was a wrapper that kept the mocked shape
- occurrences 1, severity low, status mitigated
- **Signature:** A new return contract is incompatible with a pinned test's mock, and the proposed fix edits the pinned file.
- **Rule:** When a new contract collides with a pinned test mock, keep the mocked function return shape and add a new function or wrapper for the new contract; change the test only through a successor root authored by someone else.

### [INC-0520](../../incidents/INC-0520-a-manifest-listed-its-lines-unsorted-and-the-landing-gate-re.md) - A manifest listed its lines unsorted and the landing gate refused it
- occurrences 1, severity low, status mitigated
- **Signature:** The identity check requires sorted manifest lines, and a manifest lists one group before another.
- **Rule:** Run the landing gate own identity check on a root before handing it over, so a mechanical ordering rule is met by the author and not found at the landing.
