---
id: INC-0670
title: A blocking tag was attached to a sub-variant that was not a listed option, so a viable option read as blocked and an unlisted variant read as eliminated
date: 2026-11-26
classes: [spec-and-scope]
severity: low
status: fixed
topic: spec-and-scope/requirements-and-limits-collide
occurrences: 1
---

# INC-0670 - A blocking tag was attached to a sub-variant that was not a listed option, so a viable option read as blocked and an unlisted variant read as eliminated

**Catalog:** [root](../catalog/README.md) / [spec-and-scope](../catalog/spec-and-scope/README.md) / [Requirements, units, or hard limits cannot hold together](../catalog/spec-and-scope/requirements-and-limits-collide.md)

**Cost:** One instance caught by the author's tag check, and the same defect again in the next version, caught by a second-model reviewer; part of one extra revision round.

## Signature - how you recognise it

A comparison table or con list carries a blocking tag whose subject is one way of building an option, not one of the options the document lists.

## What happened

A design document compared listed options and tagged each con blocking or advisory; this record covers three versions of it. While the first was being drafted, a blocking tag sat on a sub-variant described inside an option that stayed viable, so the option read as viable with a blocking con; the author's automated tag check caught it. In the second, the comparison table recorded a sub-variant's defect as an elimination although that variant was not a listed option; a second-model reviewer caught it. In the third, before narrowing an eliminated option into a viable variant, the author first checked whether that variant already existed as a listed option. It did, which settled the question without a new entry.

## Root cause

The tag vocabulary was defined for options, but the prose discussed variants of options alongside them, and nothing required the subject of a tag to be an entry in the option list.

## Why it was hard to see

The defect described was real, so each sentence was true. Only the unit was wrong: a reader scanning tags cannot tell a con of the option from a con of one way to build it.

## Fix

Tag only listed options. Describe a bad variant inside its option and state that it is not this option; if a variant deserves its own verdict, check whether an equivalent option is already listed, and otherwise add it to the list before tagging it.

## Verification

The author's tag check and a second-model review found the two instances and both were rewritten; the third version's existing-option check was reported by the author. Not checked: whether the tag check now rejects a tag whose subject is not a listed option.

## Transferable rule

> Attach a blocking or advisory tag only to an option in the document's own option list; describe a bad sub-variant inside its option and say it is not this option, and before promoting a variant to an option check whether an equivalent one is already listed.

## Related

[INC-0650](./INC-0650-an-options-comparison-applied-the-same-hard-constraint-at-di.md)
