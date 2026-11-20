# The tool's own resolution or defaults, not the target, caused it

[Catalog](../README.md) / [tooling-paths](README.md) / tool-defaults-not-target

**Go here if:** 'command not found' in a log, a syntax check ran the script, a launch with no process or output, a wrapper ran zero tests, a scoped-config error the real build never raises, a fetch called 'blocked'

**Rule:** Pin tools by absolute path and verify each wrapper, launch form and config exists and behaves as assumed in THIS shell before relying on it; close gates only through the canonical entry; read the tool's error stream and name the failure class before attributing a failure to the target.

8 incidents, 8 occurrences. Ordered by occurrences, then severity, then id.

## Incidents

### [INC-0072](../../incidents/INC-0072-four-different-fetch-failures-were-all-reported-as-the-site.md) - Four different fetch failures were all reported as 'the site blocks automated access'
- occurrences 1, severity medium, status mitigated
- **Signature:** A fetch returns a connection error, a redirect error or a 403, and the agent's next sentence says the site 'blocks automated access' without naming which of those it was.
- **Rule:** Never report 'the site blocks automated access' from a fetch-tool error. Name the failure class first: client error, redirect loop (cookies), form token, or a challenge page. Only a challenge page or an explicit policy is a real block, and the answer to it is an official API or another source, not a disguise.

### [INC-0307](../../incidents/INC-0307-a-measurement-wrapper-inherited-the-environment-the-tests-re.md) - A measurement wrapper inherited the environment the tests replace
- occurrences 1, severity medium, status fixed
- **Signature:** A timing wrapper found its tool through variables the tests replace on purpose, so runs failed before measuring anything.
- **Rule:** A wrapper that only adds reporting uses fixed absolute tool paths and reads no variable the tests set or replace; an invalid invocation is kept but is neither a red nor a measurement

### [INC-0342](../../incidents/INC-0342-a-shortcut-launcher-lacked-the-protection-the-canonical-entr.md) - A shortcut launcher lacked the protection the canonical entry supplies implicitly
- occurrences 1, severity medium, status fixed
- **Signature:** A gate was run by starting the test runner directly, and a nested fixture's package manager then pruned the host dependency tree.
- **Rule:** Close a gate only through the canonical entry; a shortcut launcher may lack protections the canonical path supplies implicitly

### [INC-0060](../../incidents/INC-0060-a-probe-hung-on-a-background-child-that-held-the-pipe-and-th.md) - A probe hung on a background child that held the pipe, and the timeout wrapper it relied on did not exist
- occurrences 1, severity low, status fixed
- **Signature:** A shell one-liner starts a long-lived server with a trailing background marker inside a captured pipeline, and wraps the client in a timeout command.
- **Rule:** Never background a long-lived process inside a captured pipeline, and confirm every wrapper command exists on the target OS before relying on it. Read the error stream before theorising about the hang.

### [INC-0369](../../incidents/INC-0369-a-bare-syntax-check-resolved-to-a-different-runtime-that-ign.md) - A bare syntax check resolved to a different runtime that ignored the flag and executed the script
- occurrences 1, severity low, status fixed
- **Signature:** A syntax-check command executed the script it was meant only to parse.
- **Rule:** Run syntax checks with the pinned binary by absolute path, and make every script that can act externally refuse at its first line without its required environment

### [INC-0422](../../incidents/INC-0422-a-scoped-compiler-config-flagged-an-import-style-that-the-ca.md) - A scoped compiler config flagged an import style that the canonical build never compiles
- occurrences 1, severity low, status fixed
- **Signature:** A scoped compile failed on a file the canonical build does not compile.
- **Rule:** Check a scoped compiler diagnostic against the canonical build before calling it a defect; fix a scoped-config artifact in the retained config, not the repository

### [INC-0469](../../incidents/INC-0469-a-long-acceptance-run-launched-with-a-detached-command-insid.md) - A long acceptance run launched with a detached command inside a subshell from a tool shell never started, and no output file existed minutes later
- occurrences 1, severity low, status fixed
- **Signature:** A launched run left no output and no process.
- **Rule:** Launch a long run as a tracked background task, and check that its first output file exists right after the launch

### [INC-0603](../../incidents/INC-0603-a-measurement-wrapper-called-an-agent-cli-inside-a-locked-sh.md) - A measurement wrapper called an agent CLI inside a locked shell and failed before any child ran, and the one-invocation bound was kept by voiding the attempt
- occurrences 1, severity low, status mitigated
- **Signature:** A bounded run exits before any child process starts.
- **Rule:** When a bounded run fails before any child runs, void it openly as a wrapper defect and report the corrected invocation; do not retry silently.
