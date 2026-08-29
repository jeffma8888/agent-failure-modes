---
id: INC-0030
title: Rewriting a region by slicing between two markers deletes whatever else lives there
date: 2026-08-28
classes: [tooling-paths, concurrency, vcs-destruction]
severity: high
status: fixed
---

# INC-0030 - Rewriting a region by slicing between two markers deletes whatever else lives there

**Cost:** Silently deleted an unrelated helper function from a working tool. The tool then died on its next run with a NameError for a symbol the edit never mentioned.

## Signature - how you recognise it

A tool that worked stops working immediately after an edit you believe was confined to one region, raising NameError or AttributeError for a symbol you never touched. The file still parses.

## What happened

To rewrite one function, an agent replaced everything between two located markers - the target definition and the next definition it could find. An unrelated helper that happened to live between those two anchors was deleted along with the region.

## Root cause

A marker-to-marker slice is defined by POSITION, not by content, so its blast radius is whatever the file's current layout happens to put in the gap. The edit is correct for the region the author was thinking about and wrong for the region the file actually contains.

## Why it was hard to see

The slice looks right, the resulting file is syntactically valid, and the loss only surfaces when the deleted symbol is next called - which may be a different code path, a later stage, or another session's test run.

## Fix

Prefer an anchored replace whose anchor is asserted to occur EXACTLY ONCE, so the edit is defined by content rather than position. After any slice-based edit, diff against the last known-good revision and read the insertion and deletion counts rather than trusting the intent of the edit.

## Verification

The verbatim restoration was proven by a diff against the committed revision reporting 221 insertions and 0 deletions - which simultaneously proved that a concurrent session's committed changes to the same file had not been clobbered. That same diff is the cheap standing proof for merge-never-overwrite when two writers share a file.

## Transferable rule

> Never rewrite a file region by slicing between two found markers: the slice is defined by position, so it silently deletes whatever else sits in the gap. Use an anchored replace whose anchor is asserted to occur exactly once, and after any slice edit diff against the last known-good revision - 'N insertions, 0 deletions' is the proof.

## Provenance

Where this was observed, so the claim is checkable rather than anecdotal:

- https://github.com/jeffma8888/agent-gap-radar - tools/promote.py, whose _rank helper sat between the two anchors and was deleted and then restored verbatim.

## Related

[INC-0012](./INC-0012-a-loop-s-git-add-a-sweeps-a-human-s-uncommitted-edits-into-a.md) [INC-0024](./INC-0024-backtick-command-substitution-in-a-heredoc-corrupts-and-exec.md)
