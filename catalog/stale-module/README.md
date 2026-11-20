# stale-module

[Catalog](../README.md) / stale-module

A long-running process runs the code it imported at launch. Later commits to that module are inert while git and the changelog report them shipped.

**Ask:** When did this process start, and how many commits to the code it imported have landed since - with no reload or restart?

**You are probably here if:** Running behavior ignores merged changes, a gate checks another tree, or a packet, registry, or exact list describes obsolete files or exports.

8 incidents filed here (8 occurrences); 4 more filed elsewhere are also tagged stale-module.

## Incidents

This class has no topics, so this node is the leaf. Ordered by occurrences, then severity, then id.

### [INC-0390](../../incidents/INC-0390-a-dispatch-packet-written-for-a-future-branch-went-stale-whe.md) - A dispatch packet written for a future branch went stale when a later ruling started the work elsewhere
- occurrences 2, severity low, status fixed
- **Signature:** A packet named a branch and checkout that a later ruling had superseded.
- **Rule:** Reconcile a dispatch packet with the newest ruling when it lands
- **Recurrences:**
  - [INC-0401](../../incidents/INC-0401-a-dispatch-packet-called-a-root-absent-an-hour-after-it-had.md) - 2026-11-02 - A dispatch packet called a root absent an hour after it had landed

### [INC-0021](../../incidents/INC-0021-stale-module-import-shipped-is-not-live.md) - Stale module import: 'shipped' is not 'live'
- occurrences 1, severity high, status mitigated
- **Signature:** A long-running dispatcher's uptime is measured in days. `git log --since=<start>` on the module it imported shows dozens of commits since. The behavior on disk does not match what the process seems to be running.
- **Rule:** A long-running process runs the code it imported AT LAUNCH. Merged is not shipped is not live: git can say 'landed' while the process is still on the old bytecode. Ship a live-lag check that compares process start-time against `git log --since` on the imported module. Role/prompt files read per-run ARE live even when the module is frozen - distinguish them. New config semantics need a restart too.

### [INC-0123](../../incidents/INC-0123-after-activation-a-registry-line-named-a-pending-path-that-n.md) - After activation a registry line named a pending path that no longer existed, and a verifier flagged it
- occurrences 1, severity medium, status fixed
- **Signature:** A verifier reports a missing path that was legitimately moved at activation.
- **Rule:** A verifier must follow moves through history, not require the old path to exist.

### [INC-0145](../../incidents/INC-0145-a-readiness-check-measured-the-lead-checkout-while-preship-m.md) - A readiness check measured the lead checkout while preship measures the Foundry clone
- occurrences 1, severity medium, status fixed
- **Signature:** A readiness verdict is taken from one checkout and the gate reads another.
- **Rule:** Check the tree the gate actually reads.

### [INC-0405](../../incidents/INC-0405-the-demo-server-served-a-build-made-before-the-merge-so-a-wa.md) - The demo server served a build made before the merge, so a walk after a source merge would have observed nothing new
- occurrences 1, severity low, status fixed
- **Signature:** A walk after a merge would have run against a server built before it.
- **Rule:** A milestone walk needs a fresh build of the merged SHA on its own port, never the running demo server

### [INC-0414](../../incidents/INC-0414-a-static-package-constant-check-before-dispatch-found-a-desi.md) - A static package-constant check before dispatch found a design constant absent on main
- occurrences 1, severity low, status fixed
- **Signature:** A design named a constant that the code on main did not export.
- **Rule:** Before dispatch, check statically that every constant and export the design names exists on main

### [INC-0577](../../incidents/INC-0577-an-exact-list-in-a-test-was-authored-on-an-older-base-and-re.md) - An exact list in a test was authored on an older base and reviewed on a newer one where a new collection already existed
- occurrences 1, severity low, status mitigated
- **Signature:** An exact list of business items is authored before a merge that adds an item, and reviewed after.
- **Rule:** A review of an exact list compares it with the current main product source, including business items, not the internal entries alone.

## Also tagged stale-module

4 incidents filed under another home class also carry this class. Listed by the node where they live:

- [tooling-paths/tree-lacks-what-job-needs](../tooling-paths/tree-lacks-what-job-needs.md): INC-0264, INC-0301
- [ipc-and-env](../ipc-and-env/README.md): INC-0064
- [spec-and-scope/records-drift-or-lose-provenance](../spec-and-scope/records-drift-or-lose-provenance.md): INC-0296

## Practices touching this class

- [PRA-0002](../CORE.md#practices) - Classify a control by its enforcement point, never by its medium
