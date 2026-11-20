# The checkout or dependency tree you ran in lacks what the job needs

[Catalog](../README.md) / [tooling-paths](README.md) / tree-lacks-what-job-needs

**Go here if:** Module not found from a worktree on an older base, a tracked file 'missing' in a sparse checkout, every check exits early, an install hits the network or fails offline, a lockfile regen changes more

**Rule:** Before running or assigning work in a tree, confirm it holds the checkers, scripts and tracked files the job needs (sparse lists included) and that its dependencies install offline with a frozen install; fast-forward or use a full disposable checkout rather than patch around the gap.

6 incidents, 6 occurrences. Ordered by occurrences, then severity, then id.

## Incidents

### [INC-0288](../../incidents/INC-0288-verify-a-worktree-can-run-the-required-checks-before-assigni.md) - Verify a worktree can run the required checks before assigning work there
- occurrences 2, severity medium, status fixed
- **Signature:** Every required check failed before running because the assigned worktree lacked a script.
- **Rule:** Confirm a worktree can run the required checks before work is assigned there
- **Recurrences:**
  - [INC-0319](../../incidents/INC-0319-a-sparse-checkout-hid-a-tracked-file-that-every-brief-pointe.md) - 2026-11-01 - A sparse checkout hid a tracked file that every brief pointed at

### [INC-0181](../../incidents/INC-0181-a-package-launcher-in-an-uninstalled-source-clone-reached-fo.md) - A package launcher in an uninstalled source clone reached for the registry
- occurrences 1, severity medium, status fixed
- **Signature:** A dispatch hung or failed on a network lookup.
- **Rule:** Install offline before running a package launcher in a source clone.

### [INC-0188](../../incidents/INC-0188-an-override-changed-the-lockfile-and-an-offline-clone-could.md) - An override changed the lockfile and an offline clone could not install it
- occurrences 1, severity medium, status fixed
- **Signature:** An offline install failed for lack of supply-chain metadata.
- **Rule:** Warm override metadata with a frozen install in a scratch clone before any offline install

### [INC-0264](../../incidents/INC-0264-run-repo-checkers-from-a-tree-that-contains-them.md) - Run repo checkers from a tree that contains them
- occurrences 1, severity medium, status fixed
- **Signature:** A checker failed because the tree it ran in lacked its modules.
- **Rule:** Run a repo checker from a tree that contains it, or fast-forward the tree first

### [INC-0301](../../incidents/INC-0301-an-offline-lockfile-regeneration-carried-an-unrelated-stale.md) - An offline lockfile regeneration carried an unrelated stale resolution
- occurrences 1, severity medium, status fixed
- **Signature:** A regenerated lockfile changed entries the ruling did not cover.
- **Rule:** Keep a dependency change to the ruled lines and prove it with a frozen install
