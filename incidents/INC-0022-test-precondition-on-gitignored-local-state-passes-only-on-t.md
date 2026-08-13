---
id: INC-0022
title: Test precondition on gitignored local state passes only on this machine
date: 2026-08-11
classes: [test-isolation]
severity: high
status: fixed
---

# INC-0022 - Test precondition on gitignored local state passes only on this machine

**Cost:** A ship went green and the post-release fresh-clone gate immediately went BROKEN, because the test asserted counts that were true only in the developer's working tree.

## Signature - how you recognise it

A test passes locally on every developer machine, then fails immediately in a fresh CI clone. The diff between environments is directories or files gitignored by policy.

## What happened

A test asserted that a `products/` directory held more than 6000 files. True in the working tree from gitignored per-iteration state and history; false in a fresh clone that had only the 4 tracked config files. Same trap for counts of iteration dirs, log files, LEARNINGS.md, or a repo directory basename.

## Root cause

The test read AMBIENT filesystem state instead of building its own fixture. Ambient state was gitignored - which is the whole point of gitignore - so the fresh clone had no such state and the assertion failed.

## Why it was hard to see

The test passes on every machine that has ever run the loop, because they all have the accumulated gitignored state. It only fails on a machine that has NEVER run the loop, which is exactly what CI is.

## Fix

Every ship is re-verified from a THROWAWAY FRESH CLONE. Before asserting on any path, ask whether git tracks it; if not, build the fixture in `tmp_path` instead of asserting on the ambient tree. Same trap for a repo directory's basename: assert on tracked file content, not on `os.path.basename(cwd)`.

## Verification

The test was rewritten to build its expected structure in tmp_path. It now passes in a fresh clone. A regression test asserts fresh-clone parity in CI.

## Transferable rule

> A test that reads ambient filesystem state depends on gitignored files a fresh clone does not have. Before asserting on a path, ask whether git tracks it; if not, build the fixture yourself in `tmp_path` instead of asserting on the ambient tree. A test that passes only on this machine is not a test.

## Related

[INC-0023](./INC-0023-ci-shallow-clone-breaks-tests-that-read-git-history.md)
