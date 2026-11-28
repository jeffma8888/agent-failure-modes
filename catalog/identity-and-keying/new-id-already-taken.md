# A newly minted id or name collides with one already in use

[Catalog](../README.md) / [identity-and-keying](README.md) / new-id-already-taken

**Go here if:** A new id, batch name, enum name or short key turns out to be taken: entries vanish, a branch already exists, a cache serves another record's data, a refused id is reissued, a status silently narrows.

**Rule:** Before minting an identifier, check every place that kind of identifier has ever lived (history, branches, other writers' entries, generated defaults), not only the current list of survivors; namespace shared short names by owner, check uniqueness globally rather than per batch, and never key derived state on an id a rejection or rename can recycle.

7 incidents, 7 occurrences. Ordered by occurrences, then severity, then id.

## Incidents

### [INC-0027](../../incidents/INC-0027-a-cache-keyed-on-a-recycled-id-judged-each-record-on-its-pre.md) - A cache keyed on a recycled id judged each record on its predecessor's evidence
- occurrences 1, severity critical, status fixed
- **Signature:** A mass verdict whose stated reason is IDENTICAL across hundreds of distinct inputs. Runtime is also far higher than it should be, because the cache is not actually caching anything.
- **Rule:** Never key derived evidence on an identifier a rejection can recycle: 'next free' ids are unique only among ACCEPTED records. Before believing a mass verdict, count its DISTINCT reasons - one identical reason across hundreds of inputs indicts the judge, not the data. Always re-run a gate on the full population; a hand-labelled sample finds only the false positives it contains.

### [INC-0080](../../incidents/INC-0080-two-writers-used-the-same-short-question-id-for-different-ga.md) - Two writers used the same short question ID for different gaps, so a real gap looked ruled
- occurrences 1, severity medium, status fixed
- **Signature:** A shared question table uses short bare names, and several writers add questions without a namespace.
- **Rule:** Give every shared ID a namespace one writer owns, such as the row or author; a bare short name is a collision waiting to happen.

### [INC-0125](../../incidents/INC-0125-a-marker-generator-listing-every-earlier-unmarked-root-made.md) - A marker generator listing every earlier unmarked root made a root approved later repeat an old path that a later marker already held
- occurrences 1, severity medium, status fixed
- **Signature:** Two markers name the same old path because a generator listed all earlier unmarked roots.
- **Rule:** Check uniqueness across all markers, and re-read inputs immediately before reporting.

### [INC-0079](../../incidents/INC-0079-a-second-writer-reused-a-shared-registry-s-batch-name-and-it.md) - A second writer reused a shared registry's batch name and its entries silently vanished
- occurrences 1, severity low, status fixed
- **Signature:** Two writers extend one registry and pick the next batch name from their own expectation of what is next.
- **Rule:** Before adding to a shared registry, read the current last value of every identifier kind you will create (record IDs, batch names, keys), not only the record ID.

### [INC-0448](../../incidents/INC-0448-two-fields-mapping-to-one-database-enum-made-the-generated-m.md) - Two fields mapping to one database enum made the generated migration narrow a five-state status to two states
- occurrences 1, severity low, status fixed
- **Signature:** A generated migration silently narrowed a status to fewer states than the field allows.
- **Rule:** Give each field that persists a state set its own enum name per table, and check the generated SQL for every state before generating types

### [INC-0481](../../incidents/INC-0481-two-new-work-item-ids-were-minted-from-the-current-list-alon.md) - Two new work item ids were minted from the current list alone, and both had already been used by merged work
- occurrences 1, severity low, status fixed
- **Signature:** A checker that read only the current list passed ids that history had already used.
- **Rule:** Before minting an id, check every place ids have ever lived (branch names, commit subjects, plan text), not only the current list; a checker that reads only the current list cannot catch reuse.

### [INC-0671](../../incidents/INC-0671-an-incident-id-from-a-private-log-was-read-as-an-id-in-a-pub.md) - An incident id from a private log was read as an id in a public corpus that numbers its records separately
- occurrences 1, severity low, status mitigated
- **Signature:** A note or brief says a failure is already recorded under an id, and the id has the target corpus's format but comes from a different log.
- **Rule:** Resolve every cross-reference into a corpus with that corpus's own lookup (check, search or show) and read the record before using the id; never carry an id from one repository's numbering into another unresolved.
