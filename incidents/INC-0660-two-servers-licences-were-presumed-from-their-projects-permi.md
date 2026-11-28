---
id: INC-0660
title: Two servers' licences were presumed from their projects' permissive SDKs, and both packaged servers shipped under source-available licences
date: 2026-11-25
classes: [spec-and-scope, false-green]
severity: medium
status: mitigated
topic: spec-and-scope/claims-outrun-available-evidence
occurrences: 1
---

# INC-0660 - Two servers' licences were presumed from their projects' permissive SDKs, and both packaged servers shipped under source-available licences

**Catalog:** [root](../catalog/README.md) / [spec-and-scope](../catalog/spec-and-scope/README.md) / [Claims or instructions say more than the evidence supports](../catalog/spec-and-scope/claims-outrun-available-evidence.md)

**Cost:** Two licence claims were wrong in a draft that fed architecture and white-label recommendations; the author caught both before any recommendation went out. Had they stood, an option might have been recommended that its licence restricts.

## Signature - how you recognise it

A licence statement about a server or engine rests on the project's SDK, client library or overview page, and no LICENSE file of the packaged server artifact is cited.

## What happened

An author presumed the licences of two self-hostable servers from their projects' permissive SDK messaging. Reading the LICENSE files of the packaged servers showed two different source-available licences with use restrictions a permissive licence does not have, which bear directly on an architecture or white-label recommendation.

## Root cause

A project's licence narrative was treated as covering every artifact it ships. Open-core projects commonly license the client SDK permissively and the server under a different, restrictive licence, so the SDK's licence carries no information about the server.

## Why it was hard to see

Project pages lead with the open, permissive SDK, and the repository a reader lands on is often the SDK's. The server's licence sits in a different repository or package, and both share the project's name.

## Fix

The author read and cited the LICENSE file of the exact packaged server for each candidate; licence claims now name the artifact they cover.

## Verification

Checked: both servers' LICENSE files were read and cited. Not checked: the server licences of other candidates, and whether a licence differs between versions of the same server.

## Transferable rule

> Before any architecture or white-label recommendation, read and cite the LICENSE of the exact packaged artifact and version you would deploy; a project's SDK or client licence says nothing about its server.
