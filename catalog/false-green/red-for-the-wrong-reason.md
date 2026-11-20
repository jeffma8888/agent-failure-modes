# A red, blocked or failing result came from setup or environment

[Catalog](../README.md) / [false-green](README.md) / red-for-the-wrong-reason

**Go here if:** A failure, BLOCKED or audit hit appears, but the cause is a sandbox or network denial, an unset variable, host load, a fixture tripping an earlier guard, or probe machinery that never ran.

**Rule:** Before counting a red as a finding, name the step and guard that failed and prove the code under test ran. An environment, permission, setup or earlier-guard failure is missing evidence for the claimed product defect, never proof of it and never a pass; record a broken fixture, probe or guard as its own test defect. Pair each new probe with a positive control that is green on current code.

13 incidents, 13 occurrences. Ordered by occurrences, then severity, then id.

## Incidents

### [INC-0192](../../incidents/INC-0192-a-rehearsal-mixed-automatic-guards-with-procedural-stops.md) - A rehearsal mixed automatic guards with procedural stops
- occurrences 1, severity medium, status fixed
- **Signature:** The rehearsal could not say which guard fired.
- **Rule:** Separate automatic guards from procedural stops in a rehearsal, and plant the state change relative to the actual baseline

### [INC-0200](../../incidents/INC-0200-a-sandbox-permission-failure-was-at-risk-of-reading-as-a-cod.md) - A sandbox permission failure was at risk of reading as a code defect
- occurrences 1, severity medium, status fixed
- **Signature:** The red had nothing to do with the code.
- **Rule:** Treat a permission-denied run as missing evidence and rerun it where it is permitted

### [INC-0202](../../incidents/INC-0202-one-adapter-rejection-looked-like-ten-separate-defects.md) - One adapter rejection looked like ten separate defects
- occurrences 1, severity medium, status fixed
- **Signature:** Ten failures shared one cause.
- **Rule:** Before triaging many reds, read the child output to find the one shared cause

### [INC-0213](../../incidents/INC-0213-a-network-denied-dependency-audit-was-neither-a-finding-nor.md) - A network-denied dependency audit was neither a finding nor a pass
- occurrences 1, severity medium, status fixed
- **Signature:** The audit could not run and exited like a result.
- **Rule:** Classify a network-denied audit by its exact signature, and keep other errors with the same code failing

### [INC-0236](../../incidents/INC-0236-a-blocked-result-came-from-a-deadline-before-the-plant-ran.md) - A BLOCKED result came from a deadline before the plant ran
- occurrences 1, severity medium, status fixed
- **Signature:** The negative never reached the plant.
- **Rule:** A negative proof counts only with a passing control, the plant own execution marker and the named failed step

### [INC-0291](../../incidents/INC-0291-a-known-unrelated-load-timeout-blocked-a-row-until-one-combi.md) - A known unrelated load timeout blocked a row until one combined run accepted both
- occurrences 1, severity medium, status fixed
- **Signature:** A branch gate failed only on a known unrelated timeout under heavy load.
- **Rule:** When the only failure is a known unrelated load timeout with a fix in flight, one passing run on the combined merge accepts both rows

### [INC-0314](../../incidents/INC-0314-a-probe-based-test-never-ran-its-probe-so-its-red-proved-not.md) - A probe-based test never ran its probe, so its red proved nothing about the probe
- occurrences 1, severity medium, status fixed
- **Signature:** The test was red on the feature assertion without the probe ever executing.
- **Rule:** Add a positive control that goes green on current code before trusting a red from new probe machinery

### [INC-0329](../../incidents/INC-0329-a-pool-saturation-probe-waited-on-a-connection-its-own-adapt.md) - A pool saturation probe waited on a connection its own adapter retained
- occurrences 1, severity medium, status fixed
- **Signature:** A probe timed out at full pool size and the timeout was read as exhaustion.
- **Rule:** Measure saturation against max minus what the code under test already retains, and never read a timeout as capacity evidence without the acquired and retained counts

### [INC-0628](../../incidents/INC-0628-a-walk-s-no-write-audit-counted-every-non-get-request-as-a-w.md) - A walk's no-write audit counted every non-GET request as a write, and the capture held no request headers or bodies, so override reads stopped the walk
- occurrences 1, severity medium, status mitigated
- **Signature:** An audit reports writes for requests that the server treats as reads.
- **Rule:** Capture request headers for non-GET requests and classify override reads at capture time; do not classify a request as a write by its method alone.

### [INC-0363](../../incidents/INC-0363-a-module-presence-guard-went-through-the-test-s-own-file-sys.md) - A module-presence guard went through the test's own file-system mock, so a missing-API label was never proven
- occurrences 1, severity low, status fixed
- **Signature:** Tests labelled as missing-API reds still failed at the same guard after the module existed.
- **Rule:** Before counting a red as missing-API, prove the guard both ways (module present: silent; module absent: fires), and never route a presence check through a mock the same test installs

### [INC-0412](../../incidents/INC-0412-a-whole-unit-re-run-showed-five-failures-in-unrelated-files.md) - A whole-unit re-run showed five failures in unrelated files because a required environment variable was unset in the shell
- occurrences 1, severity low, status fixed
- **Signature:** A whole-unit run failed in files unrelated to the change under acceptance.
- **Rule:** Record failures caused by an unset environment variable as an environment gap, never a pass and never a regression

### [INC-0484](../../incidents/INC-0484-a-test-fixture-failed-an-earlier-check-than-the-one-under-te.md) - A test fixture failed an earlier check than the one under test
- occurrences 1, severity low, status mitigated
- **Signature:** The case failed on the wrong guard, so the intended guard never ran.
- **Rule:** Build a fixture that passes every guard except the one under test, and assert which guard refused; an earlier guard's refusal masks the guard the case is meant to prove.

### [INC-0487](../../incidents/INC-0487-a-setting-that-strips-tokens-from-responses-also-stripped-th.md) - A setting that strips tokens from responses also stripped them from the test helper
- occurrences 1, severity low, status mitigated
- **Signature:** Every auth check downstream of a local login failed, and the token was empty at the first step.
- **Rule:** When a security setting strips tokens from responses, it strips them from local test helpers too; capture the token before the response is sanitized and assert it is present, or every downstream auth check fails at its precondition and looks like a product defect.
