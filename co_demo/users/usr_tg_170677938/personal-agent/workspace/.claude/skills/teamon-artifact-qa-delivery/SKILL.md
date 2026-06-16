---
name: teamon-artifact-qa-delivery
description: Verify generated files before user-visible claims, then deliver through the gateway with honest evidence-bound final copy. Use whenever the user asks for a file, report, workbook, document, deck, image, HTML page, archive, download, conversion, or delivery to chat.
---

# TeamON Artifact QA And Delivery

Verify generated files before user-visible claims, then deliver through the gateway with honest evidence-bound final copy.

## When to use
Use whenever the user asks for a file, report, workbook, document, deck, image, HTML page, archive, download, conversion, or delivery to chat.

## Steps
1. Treat local creation, provider setup, connector setup, and export URLs as preparation only. They do not prove the user received the promised artifact.
2. Before delivery, inspect the final artifact type, size, extension, name, and basic contents. For structured files, reopen or render them; for data files, sample rows; for archives, list contents; for HTML, open or smoke-check it.
3. Check that the artifact matches the user request: requested format, language, scope, period, source data, key fields, and any explicit naming or layout constraints.
4. If verification fails, repair once through the narrowest path and verify again. If still blocked, say what failed and offer the closest safe artifact without pretending it is complete.
5. Use gateway.send_artifact for chat delivery when the user asked to receive a file. Do not substitute a path, internal ref, or "saved locally" claim for delivery.
6. Final copy should be plain: what was delivered, what was checked, and any meaningful limitation. Hide internal refs, host paths, tool names, and storage details unless debug detail was requested.

## Success evidence
- Artifact verification evidence exists for the final file, not an earlier draft.
- gateway.send_artifact evidence exists for promised chat delivery.
- If blocked, final copy names the exact missing verification or delivery step.
