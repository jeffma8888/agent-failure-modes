---
id: INC-0072
title: Four different fetch failures were all reported as 'the site blocks automated access'
date: 2026-10-29
classes: [tooling-paths, detector-fail-closed]
severity: medium
status: mitigated
---

# INC-0072 - Four different fetch failures were all reported as 'the site blocks automated access'

**Cost:** A research report told the user to run four public-record lookups by hand in a browser. All four were readable from the agent's own shell within minutes once each failure was classified; one needed a different, official source.

## Signature - how you recognise it

A fetch returns a connection error, a redirect error or a 403, and the agent's next sentence says the site 'blocks automated access' without naming which of those it was.

## What happened

An agent's built-in fetch tool failed on four public-records pages (license registries and court records), and the agent reported all four as sites that block automated access. Classified afterwards, they were four different things. (1) A court site's main host: 'error sending request', a client-level failure; plain curl with its default User-Agent got HTTP 200 from the same host. (2) A license directory: 'error following redirect'. The server answers a browser-like User-Agent with a 302 back to the same URL until a session cookie comes back, so a client with no cookie jar loops (curl stopped after 10 redirects, exit 47); with a cookie jar it loads, and curl's own User-Agent got a 200 with no redirect at all. (3) A lookup that is a form: the POST needs the page's anti-forgery token, the cookie issued with it, and a valid value for every select. A POST missing the select value returned a bare 302; the complete one redirected to a plain GET detail URL that works on its own. (4) A court-records search and a docket aggregator: HTTP 403 with a 'Just a moment...' managed bot-challenge page, the same with any User-Agent.

## Root cause

One failure message collapsed four causes, and the fetch tool's defaults (its HTTP client, its User-Agent, no cookie persistence, no form handling) were read as the site's policy. 'Blocked' was a conclusion about the site drawn from evidence about the tool.

## Why it was hard to see

Each message is plausible as a bot block, and believing it fails quietly: the work is handed back to the human instead of visibly breaking, so nothing forces a second look.

## Fix

Classify before concluding. Retry once with a plain HTTP client (curl), with a cookie jar, following redirects, and read the status line and the first bytes of the body. A 403 whose body is a challenge page is a real refusal: stop, and get the same data from an official source (the registry's open-data API served the identical record) or another public mirror. A form gets a GET for its token, then the POST; save the redirect target as a deep link the user can open.

## Verification

All four lookups returned the official records afterwards, three directly and one through the registry's open-data API. Each failure class was then isolated with single-variable retries (User-Agent alone, cookie jar alone, a different client).

## Transferable rule

> Never report 'the site blocks automated access' from a fetch-tool error. Name the failure class first: client error, redirect loop (cookies), form token, or a challenge page. Only a challenge page or an explicit policy is a real block, and the answer to it is an official API or another source, not a disguise.

## Related

[INC-0029](./INC-0029-when-a-check-reports-missing-content-the-extractor-is-the-fi.md)
