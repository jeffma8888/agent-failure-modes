# AGENTS.md - operating manual for agents

This repository is a corpus of post-mortems from autonomous agent loops. Use it to avoid
repeating a known failure, and to record a new one without duplicating an old one. The
single source of truth is `tools/corpus.py`; every other content file is generated from it
by `tools/build.py`.

<!-- BEGIN GENERATED: agents-stats -->
- Incidents: 637 (595 canonical, 42 recurrence records, 0 recorded repeats, 637 occurrences in total).
- Failure classes: 18; topics: 54; practices: 5.
- Highest occurrence count: 10 (INC-0274).
<!-- END GENERATED: agents-stats -->

## Read protocol

Never load these whole: `RULES.md`, `TAXONOMY.md`, `data/incidents.json`, `tools/corpus.py`,
or a listing of `incidents/`. Each costs tens of thousands of tokens and most of it is noise
for your question.

1. **CLI first.** `tools/afm.py` is stdlib-only and runs from any directory:
   - `python3 tools/afm.py route "what you observe"` - the best catalog nodes for a symptom.
   - `python3 tools/afm.py search "text" [-k 8] [--class C]` - ranked incidents with their rules.
   - `python3 tools/afm.py show INC-0042 [--rule]` - one incident page, or only its rule.
   - `python3 tools/afm.py top [-n 20]` - the failures that happen most.
2. **Else walk the tree.** Start at [catalog/README.md](catalog/README.md), pick the class
   whose "you are probably here if" matches what you SEE, then the topic whose "go here if"
   matches, then the incident page. Every node is small enough to read whole.
3. **Standing guidance for a prompt:** load [catalog/CORE.md](catalog/CORE.md) (bounded,
   prompt-sized) - never `RULES.md`, which is the complete list and is not.
4. Phrase queries as symptoms ("gate green on broken code"), not as this repo's vocabulary.

## Write protocol

1. **Sync first.** `git fetch origin` and rebase onto `origin/main` before you mint anything.
2. **Dedupe check.** Run
   `python3 tools/afm.py check "draft title + signature + root cause"` and read the top
   candidates' pages. The output is a ranked list, not a verdict: lexical similarity cannot
   tell a repeat from a neighbour, so you decide.
3. **Same mechanism AND same rule** as a candidate: it is a repeat. Do NOT mint an id.
   Append to that incident's `recurrences` list in `tools/corpus.py`:
   `{"date": "YYYY-MM-DD", "note": "what recurred and where, max 300 chars", "evidence": [...]}`
   (`evidence` optional). Same topic or similar wording is NOT enough; if the rule that
   would have prevented it differs, it is a new incident.
4. **Otherwise a new incident.** `python3 tools/afm.py next-id`, then add a dict to the last
   batch in `tools/corpus.py` with every required field (`tools/build.py` REQUIRED). The
   first entry of `classes` is the HOME class: it decides where the incident lives. The
   `rule` is one imperative line, max 400 characters.
5. **Topic.** If the home class has topics (its catalog node shows a Topics table), set
   `"topic": "{class}/{slug}"` - pick it with `afm.py route`. At most 3 home incidents per
   topic class may stay at class level. A new topic is registered in `TOPICS` in
   `tools/corpus.py` (title max 70, go_here_if max 200, rule max 400).
6. **Never** set `recurrence_of` on a new record: it exists for historical duplicates that
   already have an id. It must point at an earlier canonical in the same class and topic.
7. **Build and verify:** `python3 tools/build.py`, then `python3 -m pytest tests -q`, then
   `python3 tools/leakscan.py .` (the scan root is the positional argument). Commit the
   corpus edit together with every regenerated file.

## Provenance rules

- Text is GENERIC: describe the failure mode, not one codebase. Never name an employer, an
  internal or private system, a private repository, a person, or a machine-local path, in
  any field. The leak scanner enforces the structural part; the rest is on you.
- `evidence` may cite PUBLIC repositories and public third-party projects only, each with a
  line saying what the link shows.
- Costs are honest estimates ("about 5 hours of silent stall"), not marketing numbers.
- `verification` says what was checked AND what was not.
- Never edit a generated file by hand (`incidents/`, `catalog/`, `data/`, `RULES.md`,
  `TAXONOMY.md`, the generated regions of `README.md` and this file). Edit the corpus and rebuild.

## Push checklist

1. `git fetch origin` and rebase. Re-check ids after the rebase: two sessions once minted
   the same id, and the merge had to renumber one of them.
2. `python3 tools/build.py` leaves no diff and no untracked file (`git status --porcelain`
   is empty after committing).
3. `python3 -m pytest tests -q` is green.
4. `python3 tools/leakscan.py .` is clean - with your private literal list
   (`.leakscan-private`, gitignored) if you have one.
5. Commit identity is the repository-local noreply address: check `git config user.email`
   before committing, never rely on a global identity.
6. If counts changed, `python3 tools/sync_repo_meta.py` prints the repository description;
   `--apply` updates it on GitHub.
