# An edit anchor or text match hit different bytes than you meant

[Catalog](../README.md) / [tooling-paths](README.md) / edit-or-match-hit-wrong-bytes

**Go here if:** Empty () or control characters in a file you just wrote; a symbol vanished or doubled after a 'confined' edit; a rewrite changed only a prefix; zero matches in visible text; a guard matched itself

**Rule:** Treat strings as bytes the tool will interpret: quote heredocs (<<'EOF'), anchor replacements on the whole unique line and diff afterwards, put specific rewrite rules before general ones, strip escape codes and trailing padding before matching, exclude your own command from process searches, and assert the match count.

9 incidents, 9 occurrences. Ordered by occurrences, then severity, then id.

## Incidents

### [INC-0464](../../incidents/INC-0464-color-escape-codes-in-a-report-broke-an-extraction-assertion.md) - Color escape codes in a report broke an extraction assertion, and only the zero match assertion caught it
- occurrences 2, severity low, status fixed
- **Signature:** An extraction found no matches in a report that held the text.
- **Rule:** Strip terminal escape codes before parsing a report, and keep a zero match assertion so a failed extraction writes nothing
- **Recurrences:**
  - [INC-0561](../../incidents/INC-0561-a-verifier-matched-plain-text-in-colored-logs-and-stopped.md) - 2026-11-04 - A verifier matched plain text in colored logs and stopped

### [INC-0024](../../incidents/INC-0024-backtick-command-substitution-in-a-heredoc-corrupts-and-exec.md) - Backtick command substitution in a heredoc corrupts and executes
- occurrences 1, severity high, status fixed
- **Signature:** A file written via an UNQUOTED heredoc contains empty `()` where citations should be, has control characters or carriage-return spam, and `wc -l` disagrees wildly with byte size.
- **Rule:** In an UNQUOTED heredoc, backticks and $() are executed by the shell - both corrupting file content and potentially running arbitrary commands. Use a QUOTED heredoc (`<<'EOF'`) for any write containing code citations, and verify the resulting file for control characters and empty `()` pairs afterwards. And nothing after the terminator on the same line.

### [INC-0030](../../incidents/INC-0030-rewriting-a-region-by-slicing-between-two-markers-deletes-wh.md) - Rewriting a region by slicing between two markers deletes whatever else lives there
- occurrences 1, severity high, status fixed
- **Signature:** A tool that worked stops working immediately after an edit you believe was confined to one region, raising NameError or AttributeError for a symbol you never touched. The file still parses.
- **Rule:** Never rewrite a file region by slicing between two found markers: the slice is defined by position, so it silently deletes whatever else sits in the gap. Use an anchored replace whose anchor is asserted to occur exactly once, and after any slice edit diff against the last known-good revision - 'N insertions, 0 deletions' is the proof.

### [INC-0043](../../incidents/INC-0043-an-anchored-replace-that-matches-a-prefix-of-a-line-is-still.md) - An anchored replace that matches a PREFIX of a line is still 'exactly once'
- occurrences 1, severity high, status fixed
- **Signature:** An edit asserted to match exactly once succeeds, and afterwards the file contains a duplicated fragment of the line you replaced - or one symbol defined twice, the later definition shadowing the earlier.
- **Rule:** An anchor that is a PREFIX of the real line still matches 'exactly once', so a uniqueness assertion certifies ambiguity and never completeness - anchor on the whole line or include its terminator. In a shared appended structure never assume the next sequential symbol name is free: read the live file and history, and assert AFTER writing that each symbol is defined exactly once.

### [INC-0047](../../incidents/INC-0047-in-an-ordered-replacement-list-a-general-rule-placed-before.md) - In an ordered replacement list, a general rule placed before a specific one consumes its match
- occurrences 1, severity low, status fixed
- **Signature:** A replacement list gains a broad pattern at the top, above a narrower pattern for a case the broad one also matches.
- **Rule:** In ordered rewrite lists (sed scripts, replacement files, routing tables) put specific rules before general ones, and verify on the OUTPUT, not on the rules.

### [INC-0475](../../incidents/INC-0475-a-process-guard-stopped-a-run-twice-the-listing-was-padded-w.md) - A process guard stopped a run twice: the listing was padded with trailing spaces, and the guard's own command line matched its search
- occurrences 1, severity low, status fixed
- **Signature:** A guard that searches the process list failed on padding and on matching itself.
- **Rule:** A process guard normalises only trailing whitespace in process list output and searches with a self excluding pattern in a call that contains nothing else; it keeps failing closed.

### [INC-0574](../../incidents/INC-0574-two-mutation-drivers-stopped-before-the-restored-green-becau.md) - Two mutation drivers stopped before the restored green because they matched a log-tail string the harness does not print
- occurrences 1, severity low, status mitigated
- **Signature:** A driver waits for a text in a log tail, and the text is never printed or is colored.
- **Rule:** A mutation driver must judge exit codes, not log tails; if text must be matched, strip escapes for matching only.

### [INC-0664](../../incidents/INC-0664-a-text-edit-wrote-literal-escape-sequences-instead-of-the-in.md) - A text edit wrote literal escape sequences instead of the intended characters
- occurrences 1, severity low, status mitigated
- **Signature:** An edited document displays backslash escape spellings where line breaks or punctuation were intended.
- **Rule:** Treat edit arguments as literal text unless decoding is documented; supply the actual intended characters and read the changed file on disk after every edit.
