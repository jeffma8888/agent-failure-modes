---
id: INC-0020
title: A steering channel counts only when the consumer's own parser emits it
date: 2026-08-06
classes: [steering-channel]
severity: medium
status: fixed
---

# INC-0020 - A steering channel counts only when the consumer's own parser emits it

**Cost:** Two products' pinned steering heads were silently truncated for hours while the operator believed the guidance had been delivered.

## Signature - how you recognise it

You wrote the steering text into the right file with the right words. The next iteration's behavior shows no evidence the agent read it.

## What happened

A learnings-digest function was supposed to inject a pinned 'Patterns' head verbatim into every agent's prompt. An operator wrote a directive as `- [OPERATOR ...]`. That form is TRIPLY broken: it parses as a chronological lesson (excluded from the head), it terminates the head at that line (decapitating every bullet below), and it lands in a bounded newest-N window where a top-of-file insert is the OLDEST and gets dropped.

## Root cause

The digest was character-bounded, item-count-limited, and had a specific parser for the head that treated `- [` as the start of a lesson. The steering channel had ITS OWN parser and format; writing to it in a slightly-wrong format meant the consumer's parser did not deliver the intended text.

## Why it was hard to see

The file on disk looks correct to the operator. The distinction is entirely in the consumer's parser.

## Fix

For any steering channel: verify by importing and CALLING the consumer's own parser, then asserting your marker is in the output AND that the head still delivers its expected other bullets. Do not eyeball the file. Use `- **OPERATOR ...**` (bold, not brackets) under the `## Patterns` heading, never `- [...]` (which parses as a lesson).

## Verification

After the format fix, a parser call confirmed the directive was in the emitted head and the other pinned bullets were still present at full length.

## Transferable rule

> A steering channel counts as delivered only when the CONSUMER's own parser emits it - verify by calling that parser, not by inspecting the file. Know its rules: item budget, character budget, format markers. Read the limit in the version ACTUALLY RUNNING, not the newest source. Bound anything injected into every prompt by CHARACTERS, cap at write time, and check what survives.

## Related

[INC-0004](./INC-0004-a-monotonically-growing-required-reading-file-silently-kills.md)
