---
name: teamon-presentations-pptx
description: Build, edit, verify, and deliver presentation decks as real PPTX/PDF artifacts with layout checks and source-grounded content. Use when the user asks to create, improve, edit, summarize into, or deliver a presentation, deck, slides, PPT, PPTX, Keynote-style, or Google Slides-targeted artifact.
---

# TeamON Presentations PPTX

Build, edit, verify, and deliver presentation decks as real PPTX/PDF artifacts with layout checks and source-grounded content.

## When to use
Use when the user asks to create, improve, edit, summarize into, or deliver a presentation, deck, slides, PPT, PPTX, Keynote-style, or Google Slides-targeted artifact.

## Steps
1. Clarify the audience and outcome only if missing; otherwise create a concise outline from the user request, source document, data, or current context.
2. Use native workspace tooling to build a real deck artifact, not a chat-only outline. Keep slide count, aspect ratio, title hierarchy, tables, charts, and visual assets appropriate to the audience.
3. Keep content source-grounded: cite or retain the source data internally, avoid invented metrics, and mark assumptions when a slide needs missing numbers.
4. For edits, preserve the existing deck structure and theme unless the user asked for a redesign; do not overwrite speaker notes, charts, or embedded media without reason.
5. Verify by rendering or inspecting slides for blank pages, overlapping text, clipped charts, missing images, unreadable font sizes, and broken layout on representative slides or every slide when feasible.
6. Export a PDF preview when useful for verification or user review, but deliver the requested PPTX/PDF format explicitly.
7. When the deck is promised, send the verified artifact through gateway.send_artifact and make final claims only from delivery evidence.

## Success evidence
- Deck artifact exists in the requested format with slide count and title checks.
- Rendered or inspected slides show no obvious layout corruption.
- gateway.send_artifact evidence exists when the user was promised the deck.
