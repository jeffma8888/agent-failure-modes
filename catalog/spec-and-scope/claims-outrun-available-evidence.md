# Claims or instructions say more than the evidence supports

[Catalog](../README.md) / [spec-and-scope](README.md) / claims-outrun-available-evidence

**Go here if:** A question is already answered, a diagnosis is only conditional, a value has no source, or a landing summary claims more work than the author delivered.

**Rule:** Write each claim from the primary artifact or confirmed observation, mark unavailable facts and owner-bound gaps explicitly, and never replace missing evidence with an expected outcome or requested scope.

17 incidents, 19 occurrences. Ordered by occurrences, then severity, then id.

## Incidents

### [INC-0648](../../incidents/INC-0648-a-current-project-thesis-relied-on-a-shutdown-report-that-ha.md) - A current project thesis relied on a shutdown report that had already been reversed
- occurrences 2, severity medium, status mitigated
- **Signature:** A dated secondary report supports a present-tense market premise, while the primary status source records a later reversal.
- **Rule:** Check every current-event premise against the primary status source at write time and record the check date; use secondary reporting to establish historical events, not present state.
- **Recurrences:**
  - 2026-11-25 - A research author assumed a precedent product still took new customers and offered it as a deployable alternative; its live docs said new-customer signup was closed and pointed elsewhere. Caught when the author fetched the live docs: a present-state premise again went unchecked at write time.

### [INC-0089](../../incidents/INC-0089-a-qa-question-claimed-a-credential-or-fact-was-undefined-whe.md) - A QA question claimed a credential or fact was undefined when the cut already defined it, and a restore through a gated write needed a satisfying seed
- occurrences 2, severity low, status fixed
- **Signature:** A recorded question says a value is undefined, but a search of the cut finds it.
- **Rule:** Search the oracle before recording a question, and design seeds for the gates that tests pass through.
- **Recurrences:**
  - 2026-11-26 - A design reviewer first classified an unresolved tier as a contradiction; the upstream handoff note already recorded it as a hold owned by an external approver. Caught on re-reading the handoff before the finding was issued; a gap is now classified by its stated owner first.

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

### [INC-0656](../../incidents/INC-0656-provider-technical-properties-were-asserted-from-a-category.md) - Provider technical properties were asserted from a category label, one consumer's configuration and a marketing page, not from the provider's technical documentation
- occurrences 1, severity medium, status mitigated
- **Signature:** A comparison groups or describes providers in the words of a marketing category, a landing page or one customer's setup, while the provider's own runtime or deployment documentation lists a different default or several options.
- **Rule:** Take a provider's technical property (isolation boundary, persistence, deployment model) only from its own technical documentation for the specific offering and runtime class, and check it on the page cited; a category label, a marketing page or one consumer's configuration is never the provider's contract.

### [INC-0660](../../incidents/INC-0660-two-servers-licences-were-presumed-from-their-projects-permi.md) - Two servers' licences were presumed from their projects' permissive SDKs, and both packaged servers shipped under source-available licences
- occurrences 1, severity medium, status mitigated
- **Signature:** A licence statement about a server or engine rests on the project's SDK, client library or overview page, and no LICENSE file of the packaged server artifact is cited.
- **Rule:** Before any architecture or white-label recommendation, read and cite the LICENSE of the exact packaged artifact and version you would deploy; a project's SDK or client licence says nothing about its server.

### [INC-0662](../../incidents/INC-0662-two-derived-summaries-repeated-a-pricing-unit-error-and-near.md) - Two derived summaries repeated a pricing unit error and nearly corroborated each other
- occurrences 1, severity medium, status mitigated
- **Signature:** Two derived documents agree on a price unit, while their canonical fact section describes a different charging basis.
- **Rule:** Check each price and its charging unit against the canonical fact section before writing or grading it; agreement between derived summaries is not independent corroboration.

### [INC-0668](../../incidents/INC-0668-an-options-analysis-eliminated-alternatives-on-blocking-cons.md) - An options analysis eliminated alternatives on blocking cons that the cited sources did not support
- occurrences 1, severity medium, status fixed
- **Signature:** A con tagged blocking carries a citation, and the cited passage says only that the option is harder or needs more parts, or names a different constraint from the one the option breaks.
- **Rule:** Tag a con blocking only if you can quote the source line or name the exact invariant that makes the option infeasible; if the source says only harder or needs more parts, tag it advisory; and list every option the upstream document kept viable so none is eliminated by omission.

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
