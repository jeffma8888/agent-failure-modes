# Code valid alone fails in the host runtime, module form or generator

[Catalog](../README.md) / [tooling-paths](README.md) / valid-alone-fails-in-host

**Go here if:** A spec or helper fails at collection or load (fixture name clash, import.meta under CommonJS, non-erasable syntax); a generated file dirties the tree, fails type-check or lint, or cannot round-trip

**Rule:** Check the host before writing against it: its module form, built-in fixture names, erasable-syntax rules and generator defaults; never track a file a tool rewrites per mode; when generated output must be hand-touched, change only the named defect and record raw and delivered hashes with the diff.

8 incidents, 8 occurrences. Ordered by occurrences, then severity, then id.

## Incidents

### [INC-0156](../../incidents/INC-0156-a-test-fixture-name-collided-with-a-framework-built-in-and-o.md) - A test fixture name collided with a framework built-in and only collection revealed it
- occurrences 1, severity medium, status fixed
- **Signature:** A helper looked fine in review and failed to load in every spec that imported it.
- **Rule:** Run the framework list command on each new helper before its activation review.

### [INC-0158](../../incidents/INC-0158-a-spec-used-import-meta-under-a-package-that-loads-specs-as.md) - A spec used import.meta under a package that loads specs as CommonJS
- occurrences 1, severity medium, status fixed
- **Signature:** A module-form feature worked in the author mind and would fail when the spec first loaded.
- **Rule:** Check the module form of the host package before using import.meta in a spec.

### [INC-0170](../../incidents/INC-0170-a-tracked-file-rewritten-per-tool-mode-could-not-stay-clean.md) - A tracked file rewritten per tool mode could not stay clean in both tiers
- occurrences 1, severity medium, status fixed
- **Signature:** Two modes of one tool wrote different bytes to a tracked file.
- **Rule:** Do not track a file a tool rewrites per mode; generate it before the check that needs it.

### [INC-0171](../../incidents/INC-0171-a-generator-default-module-augmentation-made-its-committed-o.md) - A generator default module augmentation made its committed output fail the type check
- occurrences 1, severity medium, status fixed
- **Signature:** Generated output failed to type check in the package where it landed.
- **Rule:** Place generated type augmentation where the augmented module lives.

### [INC-0178](../../incidents/INC-0178-a-production-build-dirtied-the-tree-and-an-example-role-was.md) - A production build dirtied the tree and an example role was missing locally
- occurrences 1, severity medium, status fixed
- **Signature:** The tree was dirty after a successful build.
- **Rule:** Check porcelain after every build; verify an example role exists locally.

### [INC-0090](../../incidents/INC-0090-type-stripping-rejected-typescript-parameter-properties-and.md) - Type-stripping rejected TypeScript parameter properties, and admin selectors were undefined
- occurrences 1, severity low, status fixed
- **Signature:** A page object fails to load under a type-stripping runtime, or a test needs UI selectors that do not exist.
- **Rule:** Write test code in erasable TypeScript only, and assert through contracts that exist.

### [INC-0426](../../incidents/INC-0426-a-generated-migration-needed-a-lint-only-edit-so-the-evidenc.md) - A generated migration needed a lint-only edit, so the evidence carries the raw and delivered hashes and the one-line diff
- occurrences 1, severity low, status fixed
- **Signature:** A generated file failed lint while its content was correct.
- **Rule:** When a generated file needs a lint-only edit, change only the named defect and record the raw hash, the delivered hash and the diff

### [INC-0439](../../incidents/INC-0439-a-generated-down-migration-dropped-a-table-with-cascade-and.md) - A generated down migration dropped a table with cascade and then dropped the removed constraint again
- occurrences 1, severity low, status fixed
- **Signature:** A down migration contained a statement that fails after an earlier statement had already removed its target.
- **Rule:** Fix a generated down migration by a minimal named edit with raw and delivered hashes, and report it as static until a round trip proves it
