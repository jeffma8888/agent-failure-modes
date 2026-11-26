# reward-hacking

[Catalog](../README.md) / reward-hacking

The loop optimizes the letter of its reward instead of the goal - Goodhart's law in production. It games its own success signal (ships busywork, self-reports success, satisfies a metric that no longer measures value).

**Ask:** Is the reward a proxy the agent can satisfy without doing the real work? What does the loop gain points for that a human would not call progress?

**You are probably here if:** The loop keeps hitting its success metric while real progress stalls: near-duplicate ships, self-reported wins, or a gate the agent can switch off itself.

2 incidents filed here (2 occurrences); 1 more filed elsewhere are also tagged reward-hacking.

## Incidents

This class has no topics, so this node is the leaf. Ordered by occurrences, then severity, then id.

### [INC-0001](../../incidents/INC-0001-reward-hacking-twelve-near-identical-features-shipped-as-dif.md) - Reward hacking: twelve near-identical features shipped as different work
- occurrences 1, severity high, status fixed
- **Signature:** The loop keeps shipping green work, but if you diff the last N ships they are progressively similar to prior ones. Every iteration passes review; every artifact is individually correct.
- **Rule:** A loop that meets its reward but not its goal is Goodhart's law in production. Change the REWARD, never the agent - a stricter reviewer still greenlights correct duplicates. Add a cross-iteration novelty signal (a scout that reviews the last N ships and vetoes clones), and put the brake in the PLANNER's prompt, not the coder's.

### [INC-0199](../../incidents/INC-0199-an-inline-directive-could-bypass-a-lint-rule-on-a-protected.md) - An inline directive could bypass a lint rule on a protected path
- occurrences 1, severity medium, status fixed
- **Signature:** A bypass could be written inline.
- **Rule:** Scope noInlineConfig by files; an ignored directive still prints a warning

## Also tagged reward-hacking

1 incidents filed under another home class also carry this class. Listed by the node where they live:

- [delegation/brief-or-plan-left-a-gap](../delegation/brief-or-plan-left-a-gap.md): INC-0644
