# zsh reads your variable differently: colon modifier, word split, array

[Catalog](../README.md) / [tooling-paths](README.md) / zsh-expansion-surprises

**Go here if:** A value is silently truncated, 'bad object name' on sha:path, a hash equals the hash of empty input, a loop sends one argument or none, one of two files committed, a checker ran without its env.

**Rule:** Assume zsh: brace every variable before a colon (${r}:path), never rely on word splitting of an unquoted variable, iterate arrays with the quoted all-elements form, run bash-only env scripts via bash -c, and confirm each side-effecting send by its own exit status.

7 incidents, 7 occurrences. Ordered by occurrences, then severity, then id.

## Incidents

### [INC-0165](../../incidents/INC-0165-a-shell-variable-followed-by-a-colon-and-a-letter-became-a-h.md) - A shell variable followed by a colon and a letter became a history modifier
- occurrences 3, severity medium, status fixed
- **Signature:** A shell string produced a truncated value without an error.
- **Rule:** In zsh, write the braces form of a variable before a colon.
- **Recurrences:**
  - [INC-0278](../../incidents/INC-0278-brace-a-shell-variable-that-is-followed-by-a-colon.md) - 2026-11-01 - Brace a shell variable that is followed by a colon
  - [INC-0622](../../incidents/INC-0622-an-unbraced-shell-variable-followed-by-a-colon-and-a-letter.md) - 2026-11-04 - An unbraced shell variable followed by a colon and a letter was read as a history modifier, so a revision was mangled and the hash printed was of empty input

### [INC-0207](../../incidents/INC-0207-three-sends-failed-because-a-packed-string-went-out-as-one-a.md) - Three sends failed because a packed string went out as one argument
- occurrences 2, severity medium, status fixed
- **Signature:** The sends failed with exit 1.
- **Rule:** Check the exit status of every send, and pass real arguments, not a packed string
- **Recurrences:**
  - [INC-0636](../../incidents/INC-0636-a-shell-loop-meant-to-send-four-messages-sent-none-because-t.md) - 2026-11-10 - A shell loop meant to send four messages sent none, because the shell does not split an unquoted variable into words

### [INC-0248](../../incidents/INC-0248-the-env-script-could-not-be-sourced-in-zsh.md) - The env script could not be sourced in zsh
- occurrences 1, severity medium, status fixed
- **Signature:** The checker ran without its environment.
- **Rule:** Run checkers through bash -c when the env script is not zsh-compatible

### [INC-0362](../../incidents/INC-0362-a-landing-loop-written-for-one-shell-s-arrays-ran-under-anot.md) - A landing loop written for one shell's arrays ran under another and committed one of two files
- occurrences 1, severity low, status fixed
- **Signature:** A commit message claimed two files but only the first of the two was committed.
- **Rule:** Iterate arrays with an explicit form valid in the running shell (the quoted all-elements expansion), and derive a commit message from the committed diff summary after the commit, not from intent
