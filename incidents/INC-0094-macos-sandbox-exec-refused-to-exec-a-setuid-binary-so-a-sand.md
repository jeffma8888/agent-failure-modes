---
id: INC-0094
title: macOS sandbox-exec refused to exec a setuid binary, so a sandboxed acceptance profile failed on the process-introspection tool
date: 2026-10-30
classes: [tooling-paths, ipc-and-env]
severity: medium
status: fixed
---

# INC-0094 - macOS sandbox-exec refused to exec a setuid binary, so a sandboxed acceptance profile failed on the process-introspection tool

**Cost:** Minor: caught in review, a re-check or acceptance before it shipped.

## Signature - how you recognise it

A sandboxed run fails when a fixture runs ps or another setuid tool.

## What happened

sandbox-exec refuses to exec any setuid binary, including ps, so the acceptance profile failed where the fixture used it to inspect processes.

## Root cause

The profile denied exec by default and the fixture needed a setuid tool.

## Why it was hard to see

The tool works outside the sandbox, so the failure looks like a fixture bug.

## Fix

Add an explicit exec exception for the fixture process-introspection tool in the sandboxed profile.

## Verification

Checked by the engineer, reviewer or lead who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> List every binary a fixture executes, setuid ones included, when writing a sandbox profile.
