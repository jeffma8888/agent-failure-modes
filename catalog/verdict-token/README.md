# verdict-token

[Catalog](../README.md) / verdict-token

A machine-parsed decision token is missing or malformed, so a downstream parser reads the absence as the pessimistic default and discards good work.

**Ask:** If the step is killed before it writes its decision, what does the parser assume - and is that assumption safe?

**You are probably here if:** Good work was discarded, or unfinished work proceeded, with no error: the decision token was missing, cut off or advisory, and the parser applied its default.

3 incidents filed here (3 occurrences); 2 more filed elsewhere are also tagged verdict-token.

## Incidents

This class has no topics, so this node is the leaf. Ordered by occurrences, then severity, then id.

### [INC-0005](../../incidents/INC-0005-a-killed-step-with-no-verdict-token-is-read-as-reverted.md) - A killed step with no verdict token is read as REVERTED
- occurrences 1, severity critical, status mitigated
- **Signature:** An iteration passes every gate, tests are green, git status is clean - and the loop reverts anyway with no error message. The final step's log ends mid-verification.
- **Rule:** A machine-parsed verdict token that defaults to the destructive answer on absence is a critical safety hazard when its writer runs under a hard timeout. Write the verdict EARLY on decisive evidence only, budget verification to the cap, and treat lower-priority audits as follow-ups.

### [INC-0152](../../incidents/INC-0152-an-exit-code-2-advisory-wording-in-the-gate-runner-defaulted.md) - An exit code 2 advisory wording in the gate runner defaulted to proceed
- occurrences 1, severity medium, status fixed
- **Signature:** A gate returns an advisory status that a caller treats as pass.
- **Rule:** Override permissive defaults on the release path.

### [INC-0428](../../incidents/INC-0428-a-supersession-marker-was-deferred-to-each-row-s-activation.md) - A supersession marker was deferred to each row's activation because writing it now would trip the freeze test
- occurrences 1, severity low, status fixed
- **Signature:** A control write was due while a freeze condition forbade control changes.
- **Rule:** Defer a marker or registry change that would trip an active freeze test to the activation step, and name the approval it will cite

## Also tagged verdict-token

2 incidents filed under another home class also carry this class. Listed by the node where they live:

- [observability/missing-or-unverifiable-receipts](../observability/missing-or-unverifiable-receipts.md): INC-0041
- [stage-timeout/work-outgrows-enforced-timeouts](../stage-timeout/work-outgrows-enforced-timeouts.md): INC-0025

## Practices touching this class

- [PRA-0001](../CORE.md#practices) - The enforcement ladder: pick the cheapest rung that makes the failure impossible
- [PRA-0003](../CORE.md#practices) - Six conditions for a gate that cannot be skipped
