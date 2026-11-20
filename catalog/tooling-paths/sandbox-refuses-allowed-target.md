# Sandbox cannot resolve or authorize the target you actually meant

[Catalog](../README.md) / [tooling-paths](README.md) / sandbox-refuses-allowed-target

**Go here if:** Refused as outside the workspace though the path is allowed, a regex literal blocked as a path, cd to a variable refused, a search refused as a home-directory scan, a setuid tool denied by a profile.

**Rule:** Give the sandbox only what it can check statically. Discriminators: cd only to a literal absolute path; probe code from a file inside the scratch tree, never a regex literal on the command line; scope searches to tracked files in your own tree; list every binary a profile must exec, setuid ones included; prove a path-alias fix with the default spelling and no workaround.

6 incidents, 6 occurrences. Ordered by occurrences, then severity, then id.

## Incidents

### [INC-0249](../../incidents/INC-0249-a-cd-to-a-path-in-a-variable-was-refused-by-the-sandbox.md) - A cd to a path in a variable was refused by the sandbox
- occurrences 2, severity medium, status fixed
- **Signature:** The command was refused although the path was allowed.
- **Rule:** Use literal paths for cd in a sandbox
- **Recurrences:**
  - [INC-0607](../../incidents/INC-0607-a-sandboxed-shell-refused-a-directory-change-whose-target-wa.md) - 2026-11-04 - A sandboxed shell refused a directory change whose target was held in a variable

### [INC-0094](../../incidents/INC-0094-macos-sandbox-exec-refused-to-exec-a-setuid-binary-so-a-sand.md) - macOS sandbox-exec refused to exec a setuid binary, so a sandboxed acceptance profile failed on the process-introspection tool
- occurrences 1, severity medium, status fixed
- **Signature:** A sandboxed run fails when a fixture runs ps or another setuid tool.
- **Rule:** List every binary a fixture executes, setuid ones included, when writing a sandbox profile.

### [INC-0211](../../incidents/INC-0211-a-regex-literal-was-read-as-a-file-path-by-the-permission-ch.md) - A regex literal was read as a file path by the permission checker
- occurrences 1, severity medium, status fixed
- **Signature:** A harmless probe was blocked as a path access.
- **Rule:** Put probe code in a file inside the scratch tree; prefer plain string tests over regex literals on a command line

### [INC-0260](../../incidents/INC-0260-prove-an-alias-fix-by-the-exact-sha-run-with-the-default-spe.md) - Prove an alias fix by the exact-SHA run with the default spelling
- occurrences 1, severity medium, status fixed
- **Signature:** A path-alias fix could be proven only with a workaround in place.
- **Rule:** Prove a path-alias fix by running the exact SHA with the default spelling and no workaround

### [INC-0370](../../incidents/INC-0370-a-scrub-command-was-refused-as-a-broad-home-directory-scan-b.md) - A scrub command was refused as a broad home-directory scan by the operating system's privacy layer
- occurrences 1, severity low, status fixed
- **Signature:** A search step was refused by the operating system as a scan of the whole home directory.
- **Rule:** Scope searches to tracked files in your own tree; never scan the home directory
