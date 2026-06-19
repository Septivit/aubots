---
name: teamon-xlsx-workbooks
description: Create, inspect, edit, and verify spreadsheet artifacts through normal capsule workspace work, with evidence before delivery claims. Use when the user asks to read, analyze, create, repair, or deliver XLSX, XLS, CSV, TSV, Excel, spreadsheet, or table artifacts.
---

# TeamON XLSX Workbooks

Create, inspect, edit, and verify spreadsheet artifacts through normal capsule workspace work, with evidence before delivery claims.

## When to use
Use when the user asks to read, analyze, create, repair, or deliver XLSX, XLS, CSV, TSV, Excel, spreadsheet, or table artifacts.

## Steps
1. Start from the closest available source: current inbox file, artifact, browser export, connector/API result, pasted table, or public shared sheet export. Do not ask for a token or re-upload before checking these paths.
2. Use native workspace tools and local libraries to inspect the workbook or table: sheet names, dimensions, headers, formulas, formats, hidden sheets, merged cells, and sample rows.
3. For analysis, normalize data into explicit intermediate tables before summarizing; preserve source rows and record the assumptions used for dates, currencies, blanks, duplicates, and totals.
4. For creation, build a real workbook with stable sheet names, filters, freeze panes, readable column widths, number/date formats, formulas where useful, and summary sheets or charts only when they add value.
5. For edits, preserve the original workbook semantics unless the user asked for a rewrite; avoid destroying formulas, hidden sheets, charts, named ranges, or macros. If a macro workbook cannot be safely edited, create a non-macro deliverable and state that limitation plainly.
6. Verify by reopening the saved file, checking workbook validity, expected sheets, row counts, key formulas, sample totals, and at least one representative value from the source.
7. When a file is promised, deliver the verified artifact with gateway.send_artifact and make final copy depend on delivery evidence, not on local file creation alone.

## Success evidence
- Workbook or table source was inspected and key assumptions are named.
- Saved workbook reopens and verification checks pass.
- gateway.send_artifact evidence exists when the user was promised the file.
