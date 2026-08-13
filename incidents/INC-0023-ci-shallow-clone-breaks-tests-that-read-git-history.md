---
id: INC-0023
title: CI shallow clone breaks tests that read git history
date: 2026-08-04
classes: [test-isolation]
severity: medium
status: fixed
---

# INC-0023 - CI shallow clone breaks tests that read git history

**Cost:** Four consecutive CI builds went red on the same three tests, none caused by the commits under test. Local was green.

## Signature - how you recognise it

Tests pass locally, fail in CI, and none of them are testing the code under review. The failures reference git-history-shaped values.

## What happened

A collector shelled out to `git log -n 15` against a fixture inside the repo and a test asserted the emitted header contained '(15)'. In a CI shallow clone, `git log` returns 1 reachable commit, so the emitted header was '(1)' and the test failed. The local dev tree had 102 commits and the test passed there.

## Root cause

CI's default checkout is depth-1 (a shallow clone). Any test that reads git history reads a different reality in CI than on a full clone.

## Why it was hard to see

The failing tests have nothing to do with the commits under test - which makes 'my change broke it' the first false hypothesis, then 'CI is flaky' the second, and only 'CI's environment is different' the third.

## Fix

Set `fetch-depth: 0` on the CI checkout step. That is the correct default anyway - CI should mirror a real clone. The diagnostic recipe: `git clone --depth 1 file:///<local-repo> /tmp/sim && pytest` reproduces the failure; then `git fetch --unshallow` in the same clone makes it pass with zero source changes. That isolates environment divergence from a real code defect in one step.

## Verification

After `fetch-depth: 0`, the tests pass in CI. A guard test asserts the workflow file still has `fetch-depth: 0`.

## Transferable rule

> CI defaults to a depth-1 clone; any test that reads git history sees a different world there. Set `fetch-depth: 0`. Before blaming the commit under test, ask what CI's environment does NOT have: git history, tags, submodules, a TTY, network, timezone, locale. A synthetic depth-1 clone locally reproduces the failure in one step.

## Related

[INC-0022](./INC-0022-test-precondition-on-gitignored-local-state-passes-only-on-t.md)
