---
id: INC-0367
title: A brief for a database-backed run omitted the test database endpoint, so the delegate rightly stopped
date: 2026-11-01
classes: [ipc-and-env]
severity: low
status: fixed
---

# INC-0367 - A brief for a database-backed run omitted the test database endpoint, so the delegate rightly stopped

**Cost:** Minor: one round trip before the run could start; nothing was touched that should not have been.

## Signature - how you recognise it

A delegate stopped before a database-backed run and reported a missing environment variable.

## What happened

the lead asked a QA delegate to run database-backed full-tier test cases, but the brief did not give the dedicated test database endpoint. The delegate refused to guess one or to use a shared cluster, stopped, and reported the missing environment variable. The lead then supplied the endpoint and the run went ahead, costing one round trip

## Root cause

the brief named the runs but not the runtime environment they need, so the endpoint existed only in the lead's head

## Why it was hard to see

The brief read as complete because every other instruction was present, and the safe behaviour of the delegate (stop and ask) is what exposed the gap rather than any failure.

## Fix

The lead supplied the endpoint; a brief that asks for a runtime run now carries its runtime environment: the exact endpoint and environment variables, which slot is free, the load gate, and what must never be touched

## Verification

Checked by the person who reported it. Not checked: whether the new rule prevents recurrence.

## Transferable rule

> A brief that asks for a runtime run must carry its runtime environment (the exact endpoint and environment variables, which slot is free, the load gate, and what must never be touched); a delegate that finds a required environment value missing stops and asks, never infers one

## Related

[INC-0074](./INC-0074-a-brief-named-a-source-directory-the-repository-does-not-hav.md) [INC-0136](./INC-0136-a-cross-agent-inventory-flake-came-from-sharing-one-harness.md) [INC-0365](./INC-0365-a-delegated-test-run-needed-login-and-logout-which-delegates.md)
