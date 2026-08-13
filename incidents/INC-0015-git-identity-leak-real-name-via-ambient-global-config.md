---
id: INC-0015
title: Git identity leak: real name via ambient global config
date: 2026-07-31
classes: [vcs-destruction]
severity: critical
status: fixed
---

# INC-0015 - Git identity leak: real name via ambient global config

**Cost:** Three public repos published every commit under the author's real name for weeks before the leak was noticed; a subsequent rewrite required force-push across the history.

## Signature - how you recognise it

`git log --all --format='%an <%ae>'` on any repo shows an identity string you did not consciously set for THAT repo.

## What happened

A repo-local `user.email` was set to a privacy-safe noreply address. `user.name` was not - it inherited the global default, which was the author's legal name. Every commit went out under the real name, publicly, until noticed. Making the repo public exposed ALL history at once.

## Root cause

Two fields, one guarded. Overriding one identity field does NOT stop the other from leaking. The mistake compounded because the global default itself had been set by machine provisioning to an employer identity - so any repo LACKING a local email override leaked the employer email into personal work.

## Why it was hard to see

Everything looks fine at the file level. `git commit -m ...` works. GitHub renders the commits. The leak is only visible if you scan the identity strings across the whole history.

## Fix

For any repo destined to be public, set BOTH repo-local `user.name` (to a public handle) AND `user.email` (id-anchored noreply) BEFORE the first commit. Verify with `git log --all --format='%an <%ae>' | sort -u`. Machine-wide, flip the global default to a privacy-safe identity and use a `[includeIf 'gitdir:...']` block for work directories - noting that `includeIf` matches the SYMLINK-RESOLVED path, so use the real path, not the alias. For an already-exposed repo, `git filter-repo --mailmap` rewrites identity metadata cleanly, but the SHAs change (force-push required) and the real name may ALSO live in file CONTENT (LICENSE, pyproject) - scrub both in one pass.

## Verification

After the rewrite: `git grep -i <name> $(git rev-list --all)` returns nothing across the whole history. Re-verify from a FRESH clone, not just the local working repo.

## Transferable rule

> For any repo destined to be public, set BOTH repo-local `user.name` AND `user.email` (to a public handle and id-anchored noreply) BEFORE the first commit. Verify with `git log --all --format='%an <%ae>'`. A noreply email alone does not stop the ambient global name from leaking. An `includeIf` gitdir must be the REAL path, not a symlink.

## Related

[INC-0018](./INC-0018-fail-open-detector-pipe-alternation-matches-nothing-under-on.md)
