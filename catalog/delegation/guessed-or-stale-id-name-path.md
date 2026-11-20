# A record is guessed or stale, or lives only in a message or worktree

[Catalog](../README.md) / [delegation](README.md) / guessed-or-stale-id-name-path

**Go here if:** A wrong commit id in a message, a report naming the previous reviewer, a stale roster, a brief pointing at a tree-local path, text only in a message lost, or untracked worktree files as the only copy.

**Rule:** Write coordination records from the source and keep them where they survive. Discriminators: put ids, names and paths in messages only after reading them from git output, the live roster or main; refresh the roster at each phase change; put content others need in files, not messages; before cleaning a worktree, triage untracked items against main and keep what nothing supersedes.

6 incidents, 6 occurrences. Ordered by occurrences, then severity, then id.

## Incidents

### [INC-0201](../../incidents/INC-0201-two-review-titles-named-the-wrong-reviewer.md) - Two review titles named the wrong reviewer
- occurrences 1, severity medium, status fixed
- **Signature:** The report carried another reviewer name.
- **Rule:** Check the attribution line of every report before landing it

### [INC-0206](../../incidents/INC-0206-a-guessed-commit-id-was-sent-to-two-teammates.md) - A guessed commit id was sent to two teammates
- occurrences 1, severity medium, status fixed
- **Signature:** Two teammates received a wrong id.
- **Rule:** Never cite a commit id in a message before git has printed it

### [INC-0263](../../incidents/INC-0263-refresh-the-team-roster-at-each-phase-change.md) - Refresh the team roster at each phase change
- occurrences 1, severity medium, status fixed
- **Signature:** A team roster went stale for ten rounds.
- **Rule:** Refresh the team roster at each phase change so thread IDs and models stay findable

### [INC-0548](../../incidents/INC-0548-an-activator-could-not-recover-an-earlier-brief-mutant-text.md) - An activator could not recover an earlier brief mutant text, so it named its own mutant and said so
- occurrences 1, severity low, status mitigated
- **Signature:** The brief that carried the mutant text is no longer available to the activator.
- **Rule:** If an assigned mutant cannot be recovered, name your own, say so, and record its diff and restore hash; put mutant text in a file, not only in a message.

### [INC-0589](../../incidents/INC-0589-the-only-copies-of-eight-reviewed-drafts-sat-untracked-in-on.md) - The only copies of eight reviewed drafts sat untracked in one worktree, and the ruling kept them untouched
- occurrences 1, severity low, status mitigated
- **Signature:** Reviewed work exists only as untracked files in a worktree that someone may clean.
- **Rule:** Before cleaning a worktree, triage its untracked items against main; keep untouched any item nothing supersedes.

### [INC-0610](../../incidents/INC-0610-landing-a-review-moved-it-out-of-the-reviewer-tree-while-ano.md) - Landing a review moved it out of the reviewer tree while another teammate had been told to read it there
- occurrences 1, severity low, status mitigated
- **Signature:** A brief names a path in a worktree and the file later lives only on main.
- **Rule:** In a brief, name the path on main, or land the file first; a path in another tree stops being valid when the file lands.
