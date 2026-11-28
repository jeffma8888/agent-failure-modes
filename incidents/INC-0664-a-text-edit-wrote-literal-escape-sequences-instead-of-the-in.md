---
id: INC-0664
title: A text edit wrote literal escape sequences instead of the intended characters
date: 2026-11-26
classes: [tooling-paths]
severity: low
status: mitigated
topic: tooling-paths/edit-or-match-hit-wrong-bytes
occurrences: 1
---

# INC-0664 - A text edit wrote literal escape sequences instead of the intended characters

**Catalog:** [root](../catalog/README.md) / [tooling-paths](../catalog/tooling-paths/README.md) / [An edit anchor or text match hit different bytes than you meant](../catalog/tooling-paths/edit-or-match-hit-wrong-bytes.md)

**Cost:** An edit left malformed document text until the author read it back; the number of affected lines and repair time were not recorded.

## Signature - how you recognise it

An edited document displays backslash escape spellings where line breaks or punctuation were intended.

## What happened

An author supplied replacement text containing escaped newline and hexadecimal apostrophe spellings to a text-edit tool. The tool stored those sequences literally rather than decoding them, so the file contained visible escape text instead of the intended line breaks and apostrophes. Viewing the file after the edit exposed the mismatch.

## Root cause

The caller assumed that the edit argument would undergo another escape-decoding pass, although it was treated as literal text.

## Why it was hard to see

The edit can succeed and match the expected anchor while writing the wrong replacement bytes; a successful tool response does not validate document formatting.

## Fix

Supply the actual intended characters in replacement text unless the tool explicitly documents an escape-decoding step, then inspect the changed file on disk.

## Verification

The author viewed the file after editing and observed the literal escapes. A successful correction and a regression test of argument decoding were not established.

## Transferable rule

> Treat edit arguments as literal text unless decoding is documented; supply the actual intended characters and read the changed file on disk after every edit.

## Related

[INC-0024](./INC-0024-backtick-command-substitution-in-a-heredoc-corrupts-and-exec.md) [INC-0464](./INC-0464-color-escape-codes-in-a-report-broke-an-extraction-assertion.md)
