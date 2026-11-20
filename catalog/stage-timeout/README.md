# stage-timeout

[Catalog](../README.md) / stage-timeout

A hard per-step wall-clock cap (beneath any outer timeout you set) silently kills work that runs too long. The narration drops and the step looks like it produced nothing.

**Ask:** What is the hardest time cap actually enforced on one step, and how close is the real work to it?

**You are probably here if:** Work dies at a repeatable duration, passes alone but times out in a suite, or never starts because a load or deadline gate refuses it.

40 incidents filed here (40 occurrences); 9 more filed elsewhere are also tagged stage-timeout.

## Topics

n = occurrences: incidents filed in the topic plus their repeats.

| Topic | Go here if | n | Link |
|---|---|---|---|
| Work outgrows hidden caps or loses timeout headroom | Attempts die at an identical limit, a growing suite stops mid-report or a test passes alone but times out under parallel load. | 14 | [work-outgrows-enforced-timeouts](work-outgrows-enforced-timeouts.md) |
| Stale or overbroad load gates block or mis-admit work | A launch ignores a denying read, uses stale approval or a blanket gate repeatedly refuses small or timing-insensitive work. | 8 | [stale-or-overbroad-load-admission](stale-or-overbroad-load-admission.md) |
| Timing models or optimizations are not measured | A split saves nothing, a speedup ignores serial work or an incomplete or loaded run is treated as calibrated headroom. | 8 | [timing-models-and-critical-path](timing-models-and-critical-path.md) |
| Timeout policy ignores purpose, call path or lifecycle | The same timeout contract is enforced differently from what its current policy promises when the work reaches the actual execution path. | 7 | [timeout-policy-and-lifecycle-boundaries](timeout-policy-and-lifecycle-boundaries.md) |

## Class-level incidents

Filed in this class but in none of its topics.

### [INC-0218](../../incidents/INC-0218-two-loaded-host-reds-shared-one-cause-and-were-at-risk-of-a.md) - Two loaded-host reds shared one cause and were at risk of a timeout bump
- occurrences 1, severity medium, status fixed
- **Signature:** The cheap fix hid the shared cause.
- **Rule:** When reds share a cause class that a pending row removes, carry the acceptance to that row, not a timeout or a retry

### [INC-0444](../../incidents/INC-0444-a-static-closure-packet-that-did-not-converge-in-three-round.md) - A static closure packet that did not converge in three rounds was replaced by running the thing and diagnosing the receipts
- occurrences 1, severity low, status fixed
- **Signature:** Static review rounds kept finding the same open items.
- **Rule:** When a static closure packet does not converge in three rounds, replace it by running the thing on current code and diagnosing the receipts

### [INC-0501](../../incidents/INC-0501-an-error-named-only-the-leaf-of-an-import-chain-and-a-rule-t.md) - An error named only the leaf of an import chain, and a rule to add a link only when the next run named it spent a run per link
- occurrences 1, severity low, status mitigated
- **Signature:** A load error names one package, but that package is reached through others that fail the same way.
- **Rule:** When an error names only the leaf of a dependency chain, trace the chain in source and act on all of it, rather than letting each run name the next link.

## Also tagged stage-timeout

9 incidents filed under another home class also carry this class. Listed by the node where they live:

- [false-green/red-for-the-wrong-reason](../false-green/red-for-the-wrong-reason.md): INC-0236, INC-0291
- [checkpoint](../checkpoint/README.md): INC-0006
- [concurrency](../concurrency/README.md): INC-0219
- [false-green/green-but-cases-never-ran](../false-green/green-but-cases-never-ran.md): INC-0290
- [false-green/verified-a-different-target](../false-green/verified-a-different-target.md): INC-0168
- [observability/misleading-metrics-and-status](../observability/misleading-metrics-and-status.md): INC-0007
- [spec-and-scope/requirements-and-limits-collide](../spec-and-scope/requirements-and-limits-collide.md): INC-0071
- [verdict-token](../verdict-token/README.md): INC-0005

## Practices touching this class

- [PRA-0001](../CORE.md#practices) - The enforcement ladder: pick the cheapest rung that makes the failure impossible
- [PRA-0003](../CORE.md#practices) - Six conditions for a gate that cannot be skipped
- [PRA-0005](../CORE.md#practices) - Admission control for an agent team on a shared host
