# A relative path or link resolves from a different root than assumed

[Catalog](../README.md) / [tooling-paths](README.md) / path-resolves-from-wrong-root

**Go here if:** Imports or links break after a file moves, is copied or activates at another depth; a relative path lands outside the workspace; a compare follows symlinks into the host; a link dangles from one tree

**Rule:** Write paths for where the file will RUN, not where it sits now: absolute paths across worktrees, imports checked from the active destination, manifests that do not follow symlinks, and never a link whose target depends on which tree reads it - verify every link resolves inside its own tree before any test.

6 incidents, 6 occurrences. Ordered by occurrences, then severity, then id.

## Incidents

### [INC-0633](../../incidents/INC-0633-an-untracked-workspace-link-in-the-main-checkout-was-rewritt.md) - An untracked workspace link in the main checkout was rewritten during a sibling worktree's provisioning to a target that only worked from main by accident, and four days later a gate that copied dependencies failed in a way that looked like a product fault
- occurrences 1, severity high, status mitigated
- **Signature:** A module-not-found error in a copied dependency tree for a workspace package that main resolves.
- **Rule:** Never provision a worktree by writing through the main checkout's dependency tree; a gate that copies dependencies verifies workspace links resolve inside its own tree before any test. A no-change claim about a checkout must check the ignored trees it could have touched, not only git status.

### [INC-0177](../../incidents/INC-0177-card-text-pointed-at-its-own-directory-as-the-checkout.md) - Card text pointed at its own directory as the checkout
- occurrences 1, severity medium, status fixed
- **Signature:** Cards broke silently when the card set moved.
- **Rule:** Grep every card for the executable path; do not keep a duty beside the section that overrides it.

### [INC-0212](../../incidents/INC-0212-a-relative-path-was-resolved-against-the-wrong-root.md) - A relative path was resolved against the wrong root
- occurrences 1, severity medium, status fixed
- **Signature:** The command was refused for a path it did not name.
- **Rule:** Use absolute paths when working across worktrees

### [INC-0316](../../incidents/INC-0316-a-recursive-diff-of-a-copied-tree-followed-fixture-symlinks.md) - A recursive diff of a copied tree followed fixture symlinks into the host
- occurrences 1, severity medium, status fixed
- **Signature:** A copy check wandered outside the copied tree and hit sockets and pipes.
- **Rule:** Verify copied trees with a manifest that does not follow symlinks; fixtures point symlinks at fixture-owned targets

### [INC-0532](../../incidents/INC-0532-test-roots-imported-helpers-by-paths-anchored-at-their-pendi.md) - Test roots imported helpers by paths anchored at their pending depth, so every import would break at the active destination
- occurrences 1, severity medium, status mitigated
- **Signature:** A spec imports by relative paths that resolve from its pending folder and climb outside the repository from its active folder.
- **Rule:** Check that every import of a root resolves from the path where the file will run, not only from where it is written; a pending copy that must move byte-identical cannot be repaired at activation.

### [INC-0446](../../incidents/INC-0446-a-fresh-worktree-can-be-provisioned-by-a-copy-on-write-clone.md) - A fresh worktree can be provisioned by a copy-on-write clone of the dependency tree instead of an install that may hit dead store links
- occurrences 1, severity low, status fixed
- **Signature:** An offline install failed on dead links in the package store.
- **Rule:** Provision a fresh worktree by a copy-on-write clone of the dependency tree, never by linking, when an install may hit dead store links
