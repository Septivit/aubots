---
name: teamon-credential-browser-readiness
description: Diagnose saved credentials and browser sessions without asking users to resend already stored authority. Use when an integration appears disconnected, a browser session expires, or the agent is unsure which refs it already has.
---

# TeamON Credential And Browser Readiness

Diagnose saved credentials and browser sessions without asking users to resend already stored authority.

## When to use
Use when an integration appears disconnected, a browser session expires, or the agent is unsure which refs it already has.

## Steps
1. Read authority inventory and capability cards before asking the user for anything.
2. Use credential.status for API/webhook/provider secrets.
3. Use browser.readiness for cookies, login state, CAPTCHA, VNC/noVNC, and auth handoff.
4. Report MCP/socket/tool-surface outages as tool-surface failures, not as missing user tokens.

## Success evidence
- credential or browser readiness evidence.
- final user copy names the exact missing rail without raw secret content.
