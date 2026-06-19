---
name: teamon-browser-business-analysis
description: Use ready browser sessions and business connectors to turn cabinet, table, and report requests into exact evidence-backed answers and artifacts. Use when the user asks for marketplace cabinet analysis, Wildberries/Ozon ads, 1C stock reports, pasted cabinet guides, or a report from visible/exportable business data.
---

# TeamON Browser Business Analysis

Use ready browser sessions and business connectors to turn cabinet, table, and report requests into exact evidence-backed answers and artifacts.

## When to use
Use when the user asks for marketplace cabinet analysis, Wildberries/Ozon ads, 1C stock reports, pasted cabinet guides, or a report from visible/exportable business data.

## Steps
1. Read readiness and capability cards first: identify whether a connector, browser session, file/export, or credential capture is ready.
2. If a ready connector matches the system, call integration.check_readiness and then the narrow integration request; never claim success from setup alone.
3. If a seller or business cabinet browser session is ready and the API connector or credential value is missing, keep working through browser-visible/exportable data before asking for API credentials.
4. For Wildberries/Ozon ad-campaign effectiveness, use cabinet statistics, exports/downloads, pagination, or same-site browser network data first. If there are many pages, produce a bounded first artifact/report with visible counts, sample rows, spend/budget/status, and the exact remaining export/paging scope; do not end with "send API token" unless browser export/statistics is concretely blocked.
5. Treat a pasted guide, core recipe, or step list as the current procedure to execute or adapt.
6. For 1C stock/inventory, do a bounded preflight, then a narrow query/export; produce a workbook/table with normalized rows, quantity-by-warehouse, amount-by-warehouse, totals, and sample checks when possible.
7. If exact data is blocked, ask for one concrete missing artifact/access item and say what could not be verified.
8. Before final answer, verify source/evidence and artifact delivery; no generic done/report-ready claim without the real business result.

## Success evidence
- browser.run_action or integration.http_request evidence for the real source.
- Exact values or artifact checks for report/table work.
- gateway.send_artifact evidence when a file/report is promised.
