---
id: INC-0024
title: Backtick command substitution in a heredoc corrupts and executes
date: 2026-08-05
classes: [tooling-paths, vcs-destruction]
severity: high
status: fixed
---

# INC-0024 - Backtick command substitution in a heredoc corrupts and executes

**Cost:** A subagent's technical study document lost every backticked citation (leaving empty `()` in about 9 places) and had ~380KB of progress-bar spam dumped into the middle, because one substitution actually ran and opened an auth browser.

## Signature - how you recognise it

A file written via an UNQUOTED heredoc contains empty `()` where citations should be, has control characters or carriage-return spam, and `wc -l` disagrees wildly with byte size.

## What happened

A subagent wrote a document via `cat > file <<EOF ... EOF` (unquoted delimiter). Every backticked citation was command-substituted away at write time. One substitution actually EXECUTED and opened a browser auth flow, which then dumped its progress-bar output into the middle of the document.

## Root cause

In an UNQUOTED heredoc, the shell interpolates `${var}`, `$(cmd)` and backtick command substitutions. Backticks in content that looks like citations (`path.py:123`) become command substitutions and either delete the citation (empty output) or actually run something.

## Why it was hard to see

The syntax looks like a simple write. The content that triggers it is the exact form documentation writers use for code references.

## Fix

For ANY file write containing backticks, use a QUOTED heredoc: `cat > file <<'EOF' ... EOF`. The single quotes on the opening delimiter disable ALL substitution. Verify agent-written files afterwards: scan for control characters, carriage returns, and empty backtick pairs. Prefer per-file outputs over one shared master doc that multiple writers append to - blast-radius scales linearly.

## Verification

After the quoted-heredoc convention took hold, subsequent multi-writer docs contained all citations intact. A pre-write assertion scans the intended payload for suspicious patterns.

## Transferable rule

> In an UNQUOTED heredoc, backticks and $() are executed by the shell - both corrupting file content and potentially running arbitrary commands. Use a QUOTED heredoc (`<<'EOF'`) for any write containing code citations, and verify the resulting file for control characters and empty `()` pairs afterwards. And nothing after the terminator on the same line.

## Related

[INC-0012](./INC-0012-a-loop-s-git-add-a-sweeps-a-human-s-uncommitted-edits-into-a.md)
