# Claims or instructions say more than the evidence supports

[Catalog](../README.md) / [spec-and-scope](README.md) / claims-outrun-available-evidence

**Go here if:** A question is already answered, a diagnosis is only conditional, a value has no source, or a landing summary claims more work than the author delivered.

**Rule:** Write each claim from the primary artifact or confirmed observation, mark unavailable facts and owner-bound gaps explicitly, and never replace missing evidence with an expected outcome or requested scope.

13 incidents, 13 occurrences. Ordered by occurrences, then severity, then id.

## Incidents

### [INC-0626](../../incidents/INC-0626-a-landing-subject-was-written-from-the-lead-s-expectation-of.md) - A landing subject was written from the lead's expectation of what a plan revision covered, and the author report said less
- occurrences 2, severity low, status mitigated
- **Signature:** A commit subject names a wider range than the artifact it lands.
- **Rule:** Write a landing subject from the artifact's own header or report, not from what you expect it covers.
- **Recurrences:**
  - [INC-0631](../../incidents/INC-0631-a-landing-subject-s-assignment-range-was-again-written-from.md) - 2026-11-07 - A landing subject's assignment range was again written from the lead's own brief instead of the author report; the second time

### [INC-0300](../../incidents/INC-0300-a-ruling-presumed-the-result-its-check-would-show.md) - A ruling presumed the result its check would show
- occurrences 1, severity medium, status fixed
- **Signature:** A ruling stated that the next check must show a particular failure.
- **Rule:** A ruling prescribes the remedy and the check, never the result the check must show

### [INC-0306](../../incidents/INC-0306-a-conditional-diagnosis-was-closed-from-the-actor-s-account.md) - A conditional diagnosis was closed from the actor's account and the code path
- occurrences 1, severity medium, status fixed
- **Signature:** A diagnosis named only conditional hazards, yet the incident needed a cause.
- **Rule:** Do not open a fix row for a hazard that is only conditional; close on the confirmed cause and track the hazard as a follow-up

### [INC-0643](../../incidents/INC-0643-a-knowledge-base-digest-s-inference-about-a-past-decision-wa.md) - A knowledge-base digest's inference about a past decision was written into the user's notes as the decision, and the primary record said the opposite
- occurrences 1, severity medium, status mitigated
- **Signature:** A decision or status in a user-facing file traces to a summary whose verbs hedge (implicitly aligns, emerged as the leading path), not to the decision record.
- **Rule:** Read the primary decision record before writing any decision or status into a user's file; treat hedged summary verbs (aligns with, emerged as, appears to) as the summarizer's inference, never as the outcome.

### [INC-0645](../../incidents/INC-0645-the-agent-taught-its-own-testability-choice-a-query-function.md) - The agent taught its own testability choice, a query function passed in as a parameter, as a property of the problem the source posed
- occurrences 1, severity medium, status fixed
- **Signature:** An explanation of a problem describes an interface detail that appears only in the agent's own solution or a secondary practice page, and in none of the primary reports.
- **Rule:** When teaching from an artifact you wrote, label each choice you made separately from what the source specifies, and check the primary reports before calling anything part of the problem.

### [INC-0648](../../incidents/INC-0648-a-current-project-thesis-relied-on-a-shutdown-report-that-ha.md) - A current project thesis relied on a shutdown report that had already been reversed
- occurrences 1, severity medium, status mitigated
- **Signature:** A dated secondary report supports a present-tense market premise, while the primary status source records a later reversal.
- **Rule:** Check every current-event premise against the primary status source at write time and record the check date; use secondary reporting to establish historical events, not present state.

### [INC-0089](../../incidents/INC-0089-a-qa-question-claimed-a-credential-or-fact-was-undefined-whe.md) - A QA question claimed a credential or fact was undefined when the cut already defined it, and a restore through a gated write needed a satisfying seed
- occurrences 1, severity low, status fixed
- **Signature:** A recorded question says a value is undefined, but a search of the cut finds it.
- **Rule:** Search the oracle before recording a question, and design seeds for the gates that tests pass through.

### [INC-0413](../../incidents/INC-0413-an-acceptance-document-cited-a-ruling-that-did-not-yet-exist.md) - An acceptance document cited a ruling that did not yet exist when it was signed
- occurrences 1, severity low, status fixed
- **Signature:** A signed record referred to a ruling that was not yet written.
- **Rule:** A signed record cites only rulings that exist, or says the item is to be ruled

### [INC-0431](../../incidents/INC-0431-interim-content-was-signed-as-clearly-marked-placeholder-cop.md) - Interim content was signed as clearly marked placeholder copy instead of being invented as sourced
- occurrences 1, severity low, status fixed
- **Signature:** Seed content needed text that no source provided.
- **Rule:** Sign interim content as a visibly marked placeholder with its open question and owner; never present an invented value as sourced

### [INC-0503](../../incidents/INC-0503-a-brief-stated-a-baseline-environment-from-a-compacted-summa.md) - A brief stated a baseline environment from a compacted summary, and the baseline script showed the opposite
- occurrences 1, severity low, status mitigated
- **Signature:** A brief says a baseline ran with a variable unset, and the script that produced the baseline sets it.
- **Rule:** State a baseline environment from the script or log that produced it, never from memory; an implementer who sees a premise contradict the artifact follows the artifact and reports it.

### [INC-0538](../../incidents/INC-0538-a-dispatch-draft-marked-every-unsourced-value-for-the-lead-t.md) - A dispatch draft marked every unsourced value for the lead to bind instead of guessing
- occurrences 1, severity low, status mitigated
- **Signature:** A packet contains values with no source in any record, such as a credential location, a clock setting or a build mode.
- **Rule:** When a value is missing, mark it for the owner to bind and list the gap; never fill it with a precedent or a guess.

### [INC-0593](../../incidents/INC-0593-a-packet-author-who-could-not-read-the-rulings-file-marked-e.md) - A packet author who could not read the rulings file marked every claim resting on it, so the recheck knew what to verify
- occurrences 1, severity low, status mitigated
- **Signature:** A packet states ruling-dependent facts that its author could not check against the source.
- **Rule:** When you cannot read a source, mark every claim that rests on it so the next checker knows what to verify.
