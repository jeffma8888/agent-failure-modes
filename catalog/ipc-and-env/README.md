# ipc-and-env

[Catalog](../README.md) / ipc-and-env

The loop breaks on its runtime environment rather than its logic: a rotated socket, an expired credential, an inherited stale variable, the machine going to sleep.

**Ask:** What environmental state did this process capture at launch that can change underneath it while it runs?

22 incidents filed here (22 occurrences); 14 more filed elsewhere are also tagged ipc-and-env.

## Incidents

This class has no topics, so this node is the leaf. Ordered by occurrences, then severity, then id.

### [INC-0008](../../incidents/INC-0008-stale-ipc-endpoint-after-the-host-application-restarts.md) - Stale IPC endpoint after the host application restarts
- occurrences 1, severity high, status mitigated
- **Signature:** Every step instantly fails (same-second timing, not a timeout). Attempt logs are ~500 bytes containing CLI help text ('did not match ... check syntax'), not the timeout string. The process looks alive.
- **Rule:** A subprocess spawned with no explicit env inherits every environmental identifier the parent captured at launch - including socket paths tied to a PID that can change. When the parent long outlives its environmental assumptions, resolve identifiers at spawn time with an ACTIVE probe (connect, not exists). Never trust a PID from a filename against PID reuse.

### [INC-0009](../../incidents/INC-0009-interactive-only-credential-expiry-silently-stalls-unattende.md) - Interactive-only credential expiry silently stalls unattended loops
- occurrences 1, severity high, status mitigated
- **Signature:** Step logs say 'credential refresh failed' or 'authentication timed out'. Distinct from throttle ('service is busy') and from the hard timeout ('timed out after 600s'). The lead thread also stalls, so hours can pass silently.
- **Rule:** Any long unattended loop depending on a human-refreshable credential will eventually stall on expiry, not throttle. Watch the LONG-LIVED credential (12h class), not the short-lived derivative one, and pair a 'time-remaining' alarm with a log-string alarm - each catches what the other misses.

### [INC-0010](../../incidents/INC-0010-sleep-beats-the-wake-lock-on-battery-power.md) - Sleep beats the wake-lock on battery power
- occurrences 1, severity high, status fixed
- **Signature:** Every task fails with the same 'Connection stalled - no data received for 120 s (network issue or system sleep)' error. Retry-and-backoff works correctly and still cannot win.
- **Rule:** A wake-lock utility on a laptop is not enough on battery power - the 'prevent system sleep' primitive is often silently gated on AC. Before an overnight unattended run, plug in AC and confirm the OS assertion is actually held. If the machine sleeps, retry-and-backoff cannot save you.

### [INC-0064](../../incidents/INC-0064-a-launcher-pointed-a-live-unattended-loop-at-the-development.md) - A launcher pointed a live unattended loop at the development checkout instead of a pinned release
- occurrences 1, severity high, status fixed
- **Signature:** The path a production loop uses to call its stage engine is the same working tree where developers are still making changes.
- **Rule:** A running unattended loop executes a pinned, tagged copy of every tool it calls, never a tree someone is editing. Make upgrades an explicit step, not a side effect of a commit.

### [INC-0068](../../incidents/INC-0068-a-retry-ladder-wrapped-the-model-call-but-not-the-credential.md) - A retry ladder wrapped the model call but not the credential helper on the same path, so one helper blip became a long hold
- occurrences 1, severity high, status mitigated
- **Signature:** A credential helper that passes every manual probe exits non-zero about once an hour inside the loop, and the loop reports an expired session.
- **Rule:** A retry ladder must cover every external call on the path to a model turn, including helpers that fetch credentials. When a dependency that passes manual probes fails in the loop, log the failing attempt's stderr instead of a classification, and never let a one-shot preflight decide whether an unattended system restarts.

### [INC-0049](../../incidents/INC-0049-a-cached-credential-made-a-dependency-look-optional-and-the.md) - A cached credential made a dependency look optional, and the outage was filed under the wrong root cause
- occurrences 1, severity medium, status fixed
- **Signature:** After an outage a component works although its documented credential is known to be expired, and the conclusion drawn is that the credential is not needed.
- **Rule:** A dependency that 'works without' its credential may be riding a cache. Prove independence by checking the whole credential chain's expiry, not by one success, and do not file a root cause until the cache lifetime is accounted for.

### [INC-0059](../../incidents/INC-0059-a-client-too-old-error-was-assumed-to-be-client-side-the-gat.md) - A 'client too old' error was assumed to be client-side; the gate was on the server and keyed on the request body
- occurrences 1, severity medium, status mitigated
- **Signature:** A vendor coding CLI says a newer version is required for a feature, and the working theory is a local version check.
- **Rule:** Before working around a version or access error, find where the check lives. A server-side gate on client identity is a decision for the human who owns the access, never something to strip or fake.

### [INC-0106](../../incidents/INC-0106-deleting-postgresql-environment-variables-left-client-tools.md) - Deleting PostgreSQL environment variables left client tools free to fall back to default host and port
- occurrences 1, severity medium, status fixed
- **Signature:** A test clears PG variables to avoid the shared cluster, and a client tool uses its defaults.
- **Rule:** Pin the target explicitly; do not rely on removing the alternatives.

### [INC-0119](../../incidents/INC-0119-a-sandboxed-home-hid-tool-caches-such-as-package-manager-shi.md) - A sandboxed HOME hid tool caches such as package-manager shims
- occurrences 1, severity medium, status fixed
- **Signature:** A tool works normally and fails once HOME points at a temp directory.
- **Rule:** When replacing HOME, forward every cache the tools need and block fetching.

### [INC-0180](../../incidents/INC-0180-a-readiness-check-ran-without-the-dispatcher-environment.md) - A readiness check ran without the dispatcher environment
- occurrences 1, severity medium, status fixed
- **Signature:** A missing variable read as a missing tool.
- **Rule:** Run readiness checks with the live dispatcher environment.

### [INC-0223](../../incidents/INC-0223-an-empty-environment-caller-was-at-risk-of-being-repaired-wi.md) - An empty environment caller was at risk of being repaired with inherited values
- occurrences 1, severity medium, status fixed
- **Signature:** The inherited values hid the empty case.
- **Rule:** Prove the input is empty and that the refusal fails without its guard

### [INC-0256](../../incidents/INC-0256-evidence-commands-ran-on-a-shimmed-runtime-instead-of-the-pi.md) - Evidence commands ran on a shimmed runtime instead of the pinned one
- occurrences 1, severity medium, status fixed
- **Signature:** The version reported was not the pinned one.
- **Rule:** Run evidence commands with the pinned binary by absolute path and print its version in the log

### [INC-0257](../../incidents/INC-0257-moving-the-home-directory-broke-a-launch-that-found-its-cach.md) - Moving the home directory broke a launch that found its cache through it
- occurrences 1, severity medium, status fixed
- **Signature:** The cache location was implicit.
- **Rule:** Name every home-resolved cache explicitly when moving HOME for isolation

### [INC-0325](../../incidents/INC-0325-a-background-watcher-lacked-the-session-credentials-and-fail.md) - A background watcher lacked the session credentials and failed every poll
- occurrences 1, severity medium, status fixed
- **Signature:** A watcher reported nothing because every poll was refused.
- **Rule:** Check what a background watcher can authenticate to before relying on it; keep authenticated checks in live turns and never write a session secret to disk

### [INC-0354](../../incidents/INC-0354-gating-by-an-environment-variable-leaked-into-nested-runners.md) - Gating by an environment variable leaked into nested runners that copy the environment
- occurrences 1, severity medium, status fixed
- **Signature:** A spec claimed an opt-in feature was inert in nested child runs, but a nested helper copied the whole environment and started a fresh runner directly.
- **Rule:** Never treat an inherited environment variable as authority; bind it to the process that was authorized

### [INC-0365](../../incidents/INC-0365-a-delegated-test-run-needed-login-and-logout-which-delegates.md) - A delegated test run needed login and logout, which delegates may not do, so the lead ran the pinned script
- occurrences 1, severity low, status fixed
- **Signature:** A delegate prepared a browser walk that logs in and out but the runtime refused it for delegated agents.
- **Rule:** When a test needs an action above a delegate's permission ceiling, the delegate writes and statically validates the script and pins its hash and exact command; the lead runs it unchanged and returns the artifacts; never weaken the test to fit the ceiling, and never let the delegate claim a result it did not observe

### [INC-0367](../../incidents/INC-0367-a-brief-for-a-database-backed-run-omitted-the-test-database.md) - A brief for a database-backed run omitted the test database endpoint, so the delegate rightly stopped
- occurrences 1, severity low, status fixed
- **Signature:** A delegate stopped before a database-backed run and reported a missing environment variable.
- **Rule:** A brief that asks for a runtime run must carry its runtime environment (the exact endpoint and environment variables, which slot is free, the load gate, and what must never be touched); a delegate that finds a required environment value missing stops and asks, never infers one

The 5 entries below are listed by title only so this node stays under 12 KB. Open the page, or run `python3 tools/afm.py show INC-XXXX`, for its signature and rule.

- [INC-0418](../../incidents/INC-0418-the-milestone-runbook-shell-sourced-an-environment-file-and.md) - The milestone runbook shell-sourced an environment file and failed before the build on a value with angle brackets (n=1, low)
- [INC-0454](../../incidents/INC-0454-a-file-creation-mask-from-an-earlier-tool-call-did-not-carry.md) - A file creation mask from an earlier tool call did not carry over, and the database dump came out world readable (n=1, low)
- [INC-0463](../../incidents/INC-0463-a-subprocess-call-failed-with-not-found-when-the-pinned-runt.md) - A subprocess call failed with not found when the pinned runtime directory was missing from the search path, and the first run showed five extra failures (n=1, low)
- [INC-0543](../../incidents/INC-0543-before-two-origins-shared-one-production-build-the-engineer.md) - Before two origins shared one production build, the engineer searched the build output for the baked origin and found none (n=1, low)
- [INC-0563](../../incidents/INC-0563-a-preload-flag-on-the-package-manager-argv-would-not-reach-t.md) - A preload flag on the package manager argv would not reach the exec'd child processes (n=1, low)

## Also tagged ipc-and-env

14 incidents filed under another home class also carry this class. Listed by the node where they live:

- [tooling-paths](../tooling-paths/README.md): INC-0094, INC-0181, INC-0188, INC-0248, INC-0307
- [concurrency](../concurrency/README.md): INC-0011, INC-0305, INC-0558
- [delegation](../delegation/README.md): INC-0017, INC-0270
- [false-green](../false-green/README.md): INC-0155, INC-0174
- [observability](../observability/README.md): INC-0036, INC-0053

## Practices touching this class

- [PRA-0005](../CORE.md#practices) - Admission control for an agent team on a shared host
