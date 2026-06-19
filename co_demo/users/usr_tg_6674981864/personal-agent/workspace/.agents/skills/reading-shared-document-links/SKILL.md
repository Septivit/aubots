---
name: reading-shared-document-links
description: Pull the real data behind a shared cloud-document view link (Google Sheets, Docs, Slides and similar) by fetching its export endpoint with the web tools, instead of failing on the JavaScript viewer page or routing to the fragile browser. Use whenever a user shares a link to a Google Sheet, Doc, or Slides deck (or a similar online document viewer) and you need the data or text inside it.
---

# Reading Data From Shared Document Links

Pull the real data behind a shared cloud-document view link (Google Sheets, Docs, Slides and similar) by fetching its export endpoint with the web tools, instead of failing on the JavaScript viewer page or routing to the fragile browser.

## When to use
Use whenever a user shares a link to a Google Sheet, Doc, or Slides deck (or a similar online document viewer) and you need the data or text inside it.

## Steps
1. Try the shared link directly with WebFetch first — public viewers like Google Sheets often return readable content straight from the plain view link.
2. For clean tabular or text data, transform the view link into its export endpoint: Google Sheets edit?...gid=NUMBER becomes export?format=csv&gid=NUMBER (or gviz/tq?tqx=out:csv&gid=NUMBER); Google Docs becomes export?format=txt; Google Slides becomes export?format=pdf.
3. Fetch the export link with native WebFetch in a verified workspace, or integration.http_request when routed; if it answers with a one-time signed redirect to another host, fetch that redirected link to get the bytes.
4. If the response is a sign-in or request-access page, the document is private — ask the owner to share it as anyone-with-the-link viewer or to add a credential or connector; never report this as a broken browser or tool.

## Success evidence
- The document actual rows or text are returned (not the empty viewer shell), with the source link cited as evidence.
- When access is blocked, the reply names the exact cause (document is private or needs sharing), not a generic tool failure.
