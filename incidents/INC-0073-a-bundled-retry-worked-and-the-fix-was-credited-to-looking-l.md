---
id: INC-0073
title: A bundled retry worked and the fix was credited to 'looking like a normal browser', which was wrong in every case tested
date: 2026-10-29
classes: [observability, tooling-paths]
severity: medium
status: mitigated
---

# INC-0073 - A bundled retry worked and the fix was credited to 'looking like a normal browser', which was wrong in every case tested

**Cost:** The user was told the trick was making requests look like a browser, and asked for that technique to be recorded as the lesson. One target's robots.txt disallowed all automated agents and had not been read before the requests.

## Signature - how you recognise it

Several changes go into one retry (new client, new User-Agent, cookie jar, form handling), the retry succeeds, and the summary names the change the agent expected to matter.

## What happened

After four failed public-record lookups succeeded on a retry, the agent summarized the fix as 'making the requests look like a normal browser'. Isolating each change afterwards, the User-Agent did not matter in any case that was tested. On a court site's main host, curl's default User-Agent got the same 200 as a browser string; the fix was the HTTP client. On a license directory, a browser User-Agent with no cookies CAUSED the redirect loop and curl's own User-Agent avoided it; the fix was the cookie jar. The challenge-protected sites refused every User-Agent; the fix was an official open-data API. The agent had also not read robots.txt first: the form lookup's host serves 'User-agent: *' with 'Disallow: /'.

## Root cause

The retry bundled four changes, and the success was credited to the one that matched the agent's prior story. Site policy (robots.txt, terms) was treated as an obstacle discovered by failing, not a check made before the first retry.

## Why it was hard to see

A 200 confirms the bundle, not any member of it. 'Pretend to be a browser' is the folk explanation for scraping blocks, so it reads as obviously right and nobody asks for the control case.

## Fix

Re-ran each case changing one variable at a time, and corrected the summary to the user, including the robots.txt miss. Before retrying a site that refused, read its robots.txt and stop on a disallow covering the path: hand the user the deep link to open in their own browser. Prefer, in order, an official API or open-data copy, the site's own GET detail URL, then a plain client with cookies. Never try to get past a challenge page.

## Verification

Single-variable retries reproduced each case: the same 200 with the default and the browser User-Agent on the court host; a 302 loop only with a browser User-Agent and no cookie jar on the directory; a 403 challenge with every User-Agent on the protected sites. robots.txt was fetched for every host involved.

## Transferable rule

> When a bundled retry works, isolate the variable before naming the fix: a 200 confirms the bundle, not your story. Read robots.txt before retrying a site that refused, stop on a disallow, and treat a challenge page as a refusal: use an official API or hand the user the link.

## Related

[INC-0049](./INC-0049-a-cached-credential-made-a-dependency-look-optional-and-the.md) [INC-0072](./INC-0072-four-different-fetch-failures-were-all-reported-as-the-site.md)
