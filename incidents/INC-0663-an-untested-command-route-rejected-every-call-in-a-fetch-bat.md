---
id: INC-0663
title: An untested command route rejected every call in a fetch batch
date: 2026-11-25
classes: [tooling-paths]
severity: low
status: mitigated
topic: tooling-paths/tool-defaults-not-target
occurrences: 1
---

# INC-0663 - An untested command route rejected every call in a fetch batch

**Catalog:** [root](../catalog/README.md) / [tooling-paths](../catalog/tooling-paths/README.md) / [The tool's own resolution or defaults, not the target, caused it](../catalog/tooling-paths/tool-defaults-not-target.md)

**Cost:** The entire initial fetch batch was rejected before the command route was corrected; its size and elapsed time were not recorded.

## Signature - how you recognise it

Every item in a bulk fetch fails at command dispatch before any source can be retrieved.

## What happened

An author ran a bulk-fetch script whose invocation used the wrong CLI route for the fetch tool. Every call was rejected. The shared route was corrected after the batch failed, rather than being tested with one real request before repetition.

## Root cause

The script multiplied an assumed command interface without a representative end-to-end invocation through that same dispatch path.

## Why it was hard to see

A loop can look ready once its inputs and arguments are assembled, even though no single iteration has demonstrated that the tool can be reached.

## Fix

Try one representative fetch through the exact script invocation, confirm it reaches the tool and returns the intended source, and expand to the remaining inputs only after that succeeds.

## Verification

The author observed all initial calls being rejected and corrected the CLI route. A successful rerun of the full batch and future adherence to the single-call preflight were not established.

## Transferable rule

> Before batching a new CLI invocation, run one representative request through the exact dispatch path and verify the intended result; do not multiply an untested command route.

## Related

[INC-0603](./INC-0603-a-measurement-wrapper-called-an-agent-cli-inside-a-locked-sh.md) [INC-0060](./INC-0060-a-probe-hung-on-a-background-child-that-held-the-pipe-and-th.md)
