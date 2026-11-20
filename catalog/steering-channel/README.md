# steering-channel

[Catalog](../README.md) / steering-channel

The channel meant to steer the loop (injected instructions, pinned notes) is not actually delivered - it is truncated, mis-parsed, or dropped by the consumer that was supposed to read it.

**Ask:** Did the CONSUMER's own parser emit the steering text verbatim, or did you only confirm you wrote it?

**You are probably here if:** A directive, pinned note or reply that should steer the loop was written, yet the consumer acted as if it never arrived, or saw it and never acted on it.

4 incidents filed here (4 occurrences); 1 more filed elsewhere are also tagged steering-channel.

## Incidents

This class has no topics, so this node is the leaf. Ordered by occurrences, then severity, then id.

### [INC-0020](../../incidents/INC-0020-a-steering-channel-counts-only-when-the-consumer-s-own-parse.md) - A steering channel counts only when the consumer's own parser emits it
- occurrences 1, severity medium, status fixed
- **Signature:** You wrote the steering text into the right file with the right words. The next iteration's behavior shows no evidence the agent read it.
- **Rule:** A steering channel counts as delivered only when the CONSUMER's own parser emits it - verify by calling that parser, not by inspecting the file. Know its rules: item budget, character budget, format markers. Read the limit in the version ACTUALLY RUNNING, not the newest source. Bound anything injected into every prompt by CHARACTERS, cap at write time, and check what survives.

### [INC-0067](../../incidents/INC-0067-an-operator-directive-was-visible-to-the-planner-but-no-rule.md) - An operator directive was visible to the planner but no rule ranked it, so it was deferred while the loop shipped its own picks
- occurrences 1, severity medium, status fixed
- **Signature:** A directive is placed in the file every role reads first, and the planning role's output acknowledges it and then does something else.
- **Rule:** A directive to an agent system needs a route into the decision, not only visibility. Before queuing one, read the picker's prompt and confirm which rule will select it; if none does, write that rule first.

### [INC-0449](../../incidents/INC-0449-the-lead-missed-six-teammate-replies-across-a-context-compac.md) - The lead missed six teammate replies across a context compaction and left the critical-path engineer idle for 35 minutes
- occurrences 1, severity low, status fixed
- **Signature:** Replies sat unread after a compaction.
- **Rule:** Check thread activity right after every context compaction, before any other step

### [INC-0451](../../incidents/INC-0451-the-lead-missed-eight-teammate-replies-with-no-compaction-an.md) - The lead missed eight teammate replies with no compaction and saw them only through thread activity
- occurrences 1, severity low, status fixed
- **Signature:** Replies were missing from the lead view while the work sat finished.
- **Rule:** Check thread states after every landing batch, not only after a context compaction

## Also tagged steering-channel

1 incidents filed under another home class also carry this class. Listed by the node where they live:

- [stage-timeout/work-outgrows-enforced-timeouts](../stage-timeout/work-outgrows-enforced-timeouts.md): INC-0004

## Practices touching this class

- [PRA-0002](../CORE.md#practices) - Classify a control by its enforcement point, never by its medium
