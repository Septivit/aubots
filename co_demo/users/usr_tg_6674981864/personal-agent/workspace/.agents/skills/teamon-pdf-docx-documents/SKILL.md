---
name: teamon-pdf-docx-documents
description: Read, extract, draft, edit, redline, render, and verify document artifacts without treating document work as a connector problem. Use when the user sends, asks to analyze, create, edit, convert, summarize, redline, or deliver PDF, DOC, DOCX, Word, policy, contract, brief, or long-form document artifacts.
---

# TeamON PDF And DOCX Documents

Read, extract, draft, edit, redline, render, and verify document artifacts without treating document work as a connector problem.

## When to use
Use when the user sends, asks to analyze, create, edit, convert, summarize, redline, or deliver PDF, DOC, DOCX, Word, policy, contract, brief, or long-form document artifacts.

## Steps
1. Use native Read/document parsing first for current PDFs, DOCX files, inbox files, and explicit document refs; use media.read_document only when native reading cannot access the artifact.
2. For extraction and analysis, identify pages or sections, keep source quotations short, and separate verified text from inference or missing/OCR-uncertain parts.
3. For DOCX creation or edits, preserve document structure: headings, lists, tables, links, footnotes, page breaks, and comments where available. Avoid flattening a structured document into plain text unless requested.
4. For PDF outputs, build or convert from a controlled source document, then render or inspect enough pages to catch blank pages, broken fonts, clipped tables, unreadable images, and pagination errors.
5. For redlines or review notes, keep changes traceable: original issue, proposed edit, location, and reason. Do not silently rewrite legal, financial, or policy wording without marking assumptions.
6. If the document is private behind a cloud viewer, try the public export/read path first; if access is blocked, ask for sharing or an uploaded file instead of blaming the browser.
7. When a deliverable is promised, reopen or render the final file, then send it with gateway.send_artifact and claim delivery only after gateway evidence.

## Success evidence
- Source document was read with page/section or file evidence.
- Generated or edited document was reopened/rendered enough to catch layout corruption.
- gateway.send_artifact evidence exists when the user was promised the document.
