---
id: INC-0250
title: Bare angle-bracket slots turned a Markdown note into raw text after structural checks passed
date: 2026-11-01
classes: [false-green, detector-fail-open]
severity: high
status: fixed
---

# INC-0250 - Bare angle-bracket slots turned a Markdown note into raw text after structural checks passed

**Cost:** One note rendered as raw text from the first slot to the end, and the same bug sat in 20 more notes, two of them templates that seeded it. The user had been told the formatting was fine.

## Signature - how you recognise it

The note passed every structural check and still showed raw text after the first slot.

## What happened

An agent wrote Markdown study notes with angle-bracket slots such as <validation>, <contract test> and <one reason> in prose, and a generic type such as Stream<Student> in a quote. A Markdown note app's live editor opens an inline HTML element on a less-than sign followed by a letter-word. No slot was ever closed, so the editor stayed in HTML mode and every later line (headings, lists, tables, diagram code fences) showed as raw text to the end of the note. Measured with the app's own tokenizer: 674 of 700 lines showed as raw text, and only 0 of 4 diagrams and 3 of 74 headings rendered. The reading view silently deleted the slot words. The agent had earlier said the formatting was fine, based on balanced fences and present headings. Only the user seeing the broken note caught it. A second trap turned up in the fix: a backslash escape right after a bare URL does not escape, because the editor's bare-URL token swallows the backslash. Backticks work.

## Root cause

Formatting was judged by structural lint (balanced fences, headings present) instead of by the target renderer's own parse. The renderer's inline-HTML start rule and bare-URL rule were never modelled, so an unclosed element passed every check.

## Why it was hard to see

The file is valid Markdown by every structural measure and the reading view hides the damage by deleting the slot words. The failure shows only in the live editor, and the generic type in a quote looks harmless.

## Fix

Escape or backtick every slot, fence pasted code, and use backticks rather than a backslash after a bare URL. A stdlib checker models the editor's block rules, its HTML-start rule, its HTML-mode exit (only when every opened element closes, or at the next pipe inside a recognized table) and its bare-URL rule. An independent audit found the first version wrong in four ways: it flagged slots inside indented code and math, missed a nested element left open, and rejected a close tag written in code that the editor still reads. It was rebuilt as a line-by-line state machine and gated into the doc verifiers with seeded tests. The same bug was fixed in 20 more notes, including the two templates.

## Verification

Checked: the tokenizer was re-run on the fixed notes; the rebuilt checker matched the real tokenizer's HTML-mode verdict on every line of 1,270 test documents (170 hand-written, 1,100 generated), and seeded tests fail on planted slots. The first version had agreed with the tokenizer on 1,428 real notes and still missed all four defects, because real notes rarely hold the edge cases. Not checked: whether the rule prevents recurrence.

## Transferable rule

> Verify Markdown by the target renderer's own parse, not by structural lint; never leave a bare <slot> outside code.

## Related

[INC-0070](./INC-0070-two-reviewers-table-parsers-undercounted-rows-on-escaped-pip.md) [INC-0241](./INC-0241-automated-tests-passed-while-nobody-had-walked-the-real-site.md)
