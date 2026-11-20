# Syntax matching accepts decoys or rejects valid forms

[Catalog](../README.md) / [detector-fail-open](README.md) / syntax-shapes-and-benign-decoys

**Go here if:** A static rule recognizes one syntax shape, misses aliases or accepts a benign substring beside an invalid target.

**Rule:** Test detectors against equivalent valid forms and adversarial invalid forms with alias resolution and decoys; enforce the semantic condition across every candidate instead of accepting a convenient syntax shape or one allowed substring.

7 incidents, 7 occurrences. Ordered by occurrences, then severity, then id.

## Incidents

### [INC-0129](../../incidents/INC-0129-a-syntax-hygiene-rule-flagging-every-literal-timer-over-one.md) - A syntax hygiene rule flagging every literal timer over one second also flagged a cancellation watchdog
- occurrences 1, severity medium, status fixed
- **Signature:** A rule against long timers rejects a bound that fails and is cleared.
- **Rule:** A hygiene rule should test intent, not only syntax.

### [INC-0141](../../incidents/INC-0141-a-static-watchdog-rule-accepting-only-an-inline-await-of-a-n.md) - A static watchdog rule accepting only an inline await of a new promise flagged stored promises and other valid shapes
- occurrences 1, severity medium, status fixed
- **Signature:** A rule written against one syntax shape rejects equivalent valid code.
- **Rule:** Widen a rule by shape and prove it with near-miss negatives.

### [INC-0142](../../incidents/INC-0142-a-redirect-test-searching-for-one-allowed-substring-accepted.md) - A redirect test searching for one allowed substring accepted a bad target beside a benign decoy
- occurrences 1, severity medium, status fixed
- **Signature:** A redirect check passes because one acceptable string appears among several candidates.
- **Rule:** Validate all candidates, not the first acceptable one.

### [INC-0151](../../incidents/INC-0151-a-hygiene-rule-against-conditional-test-omission-needed-a-pr.md) - A hygiene rule against conditional test omission needed a precise flagged and allowed set
- occurrences 1, severity medium, status fixed
- **Signature:** A conditional skip or registration hides a test from the suite.
- **Rule:** State both the flagged and the allowed set of a hygiene rule.

### [INC-0166](../../incidents/INC-0166-a-conditional-omission-could-hide-behind-a-helper-an-alias-o.md) - A conditional omission could hide behind a helper, an alias or an early return
- occurrences 1, severity medium, status fixed
- **Signature:** A hygiene rule allowed omissions that took registrations out of a suite.
- **Rule:** Forbid conditional omission anywhere, with the same alias resolution as describe.

### [INC-0176](../../incidents/INC-0176-a-shape-regex-was-used-as-ownership-evidence-for-a-sweep.md) - A shape regex was used as ownership evidence for a sweep
- occurrences 1, severity medium, status fixed
- **Signature:** A sweep matched files it did not own.
- **Rule:** A sweep that decides by shape needs decoys.

### [INC-0374](../../incidents/INC-0374-a-clause-survival-script-flagged-21-digest-rules-that-a-word.md) - A clause-survival script flagged 21 digest rules that a word diff showed were only wording compressions
- occurrences 1, severity low, status fixed
- **Signature:** A clause-survival check flagged many rules as lost although their meaning was intact.
- **Rule:** Run a word diff before treating a flagged rule as lost
