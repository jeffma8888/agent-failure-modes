---
id: INC-0672
title: A pre-commit scrub kept its own short pattern list, so a file naming a model by its raw identifier was committed and only the post-commit leak guard caught it
date: 2026-11-27
classes: [detector-fail-open]
severity: low
status: fixed
topic: detector-fail-open/wrong-parser-or-pattern
occurrences: 1
---

# INC-0672 - A pre-commit scrub kept its own short pattern list, so a file naming a model by its raw identifier was committed and only the post-commit leak guard caught it

**Catalog:** [root](../catalog/README.md) / [detector-fail-open](../catalog/detector-fail-open/README.md) / [A parser or pattern reads the wrong evidence](../catalog/detector-fail-open/wrong-parser-or-pattern.md)

**Cost:** One commit amended while still unpushed; the reviewed file changed at two spots, with both digests recorded.

## Signature - how you recognise it

A file passes the pre-commit scrub and then fails the leak guard on a term the scrub does not list.

## What happened

A reviewer disclosed a model fallback, as asked, but wrote the raw model identifier with its provider prefix twice. The lead's pre-landing scrub checked home paths, user names and dashes from a hand-kept list, not every term the repository's leak guard forbids, so the landing helper copied and committed the file. The post-commit leak guard over the unpushed range then failed with two hits. The commit was still the unpushed head, so the two identifiers were removed (the display name beside each stayed), the commit was amended, and the guard and both checkers re-ran clean.

## Root cause

Two pattern lists guarded the same boundary: the guard's, kept in the repository, and a shorter hand copy in the lead's scrub, which had drifted from it.

## Why it was hard to see

The scrub had passed on every earlier landing, and the post-commit guard still caught the leak before any push, so the gap showed only when a new term appeared in a file.

## Fix

The landing helper now runs a pre-staging scan that loads the guard's own patterns from the guard's source and fails closed (a distinct exit code) if it cannot load them or read a file. Tested on a planted hit, a clean file and a missing file. Briefs ask for model display names only.

## Verification

Checked: the scan exits non-zero on a planted hit and on a missing file, zero on a clean file, and the amended commit passes the guard. Not checked: whether the guard's own patterns cover every identifier form a teammate might write.

## Transferable rule

> Make every pre-commit scrub load the leak guard's own pattern source, run it before staging and fail closed when it cannot load; fix a leak found in an unpushed head by amending that head alone, never by a later commit.

## Related

[INC-0081](./INC-0081-reviewers-and-qa-wrote-absolute-home-paths-and-notes-paths-i.md) [INC-0504](./INC-0504-a-branch-scrubbed-a-local-path-in-a-later-commit-and-a-range.md) [INC-0364](./INC-0364-a-hand-written-landing-chain-swallowed-a-failed-post-commit.md) [INC-0224](./INC-0224-a-classifier-kept-a-legacy-pattern-list-beside-a-new-exact-s.md)
