# identity-and-keying

[Catalog](../README.md) / identity-and-keying

Two distinct things share one identifier or cache key, so state computed for one is served for the other: a slot number a rejection recycles, a cache keyed on a mutable name, a record cited by its position in a re-sorted list.

**Ask:** Is this key unique across everything it will ever be asked about, or only across the subset that succeeded?

**You are probably here if:** A lookup lands on the wrong thing: one identical reason across many inputs, entries vanish, a new id was already taken, a revision is tied to the wrong commit.

36 incidents filed here (36 occurrences); 19 more filed elsewhere are also tagged identity-and-keying.

## Topics

n = occurrences: incidents filed in the topic plus their repeats.

| Topic | Go here if | n | Link |
|---|---|---|---|
| A file-replacement (supersession) record is refused or claims too much | A record saying which file replaces which is refused or over-claims: duplicate edge, more edges than approved, name outside its family, old path in pending form, old digest not on main, unsorted list. | 14 | [replacement-record-malformed](replacement-record-malformed.md) |
| An approval or activation names the wrong commit or line of history | A gate tying a revision to its approval refuses or wrongly passes: the named commit is not an ancestor, predates what it approves, is HEAD mid-merge, precedes review; a merge leaves activation due. | 9 | [approval-names-wrong-commit](approval-names-wrong-commit.md) |
| A name, path string or digest stands in for the real identity, drifts | Two values that must agree were typed separately (display name vs model id, two spellings of one path, digest vs its path, commit order from memory); a proof omits a dimension; one field, many facts. | 6 | [key-is-a-proxy](key-is-a-proxy.md) |
| A newly minted id or name collides with one already in use | A new id, batch name, enum name or short key turns out to be taken: entries vanish, a branch already exists, a cache serves another record's data, a refused id is reissued, a status silently narrows. | 6 | [new-id-already-taken](new-id-already-taken.md) |

## Class-level incidents

Filed in this class but in none of its topics.

### [INC-0341](../../incidents/INC-0341-a-registration-subject-pinned-to-the-current-local-head-read.md) - A registration subject pinned to the current local head read as stale under a push freeze
- occurrences 1, severity medium, status fixed
- **Signature:** An owner packet asserted checkout, clone and remote at one hash, and the assertion went stale only because local commits accumulated.
- **Rule:** Under a push freeze, pin the subject by role and corroborate the freeze with a remote query (one tip query does not prove the history); a stale remote-tracking ref is not freeze evidence

## Also tagged identity-and-keying

19 incidents filed under another home class also carry this class. Listed by the node where they live:

- [spec-and-scope/records-drift-or-lose-provenance](../spec-and-scope/records-drift-or-lose-provenance.md): INC-0055, INC-0147, INC-0326, INC-0335
- [spec-and-scope/wrong-owner-path-or-scope](../spec-and-scope/wrong-owner-path-or-scope.md): INC-0085, INC-0099, INC-0121
- [test-isolation/green-alone-red-together](../test-isolation/green-alone-red-together.md): INC-0097, INC-0360
- [vcs-destruction](../vcs-destruction/README.md): INC-0185, INC-0226
- [delegation/reviewer-not-independent-or-free](../delegation/reviewer-not-independent-or-free.md): INC-0220
- [detector-fail-open/coverage-and-controls-not-proven](../detector-fail-open/coverage-and-controls-not-proven.md): INC-0186
- [detector-fail-open/guard-defaults-and-negative-controls](../detector-fail-open/guard-defaults-and-negative-controls.md): INC-0108
- [detector-fail-open/syntax-shapes-and-benign-decoys](../detector-fail-open/syntax-shapes-and-benign-decoys.md): INC-0176
- [false-green/check-satisfied-by-unrelated-cause](../false-green/check-satisfied-by-unrelated-cause.md): INC-0083
- [spec-and-scope/missing-or-late-prerequisites](../spec-and-scope/missing-or-late-prerequisites.md): INC-0353
- [spec-and-scope/tests-do-not-prove-the-contract](../spec-and-scope/tests-do-not-prove-the-contract.md): INC-0159
- [tooling-paths/edit-or-match-hit-wrong-bytes](../tooling-paths/edit-or-match-hit-wrong-bytes.md): INC-0043
