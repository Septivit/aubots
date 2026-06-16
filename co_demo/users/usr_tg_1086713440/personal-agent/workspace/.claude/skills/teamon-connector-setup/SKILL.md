---
name: teamon-connector-setup
description: Create or repair App/Connector capability cards while keeping credentials and browser sessions behind refs. Use when the user says an integration, webhook, API, App, connector, or browser login should be added or fixed.
---

# TeamON Connector Setup

Create or repair App/Connector capability cards while keeping credentials and browser sessions behind refs.

## When to use
Use when the user says an integration, webhook, API, App, connector, or browser login should be added or fixed.

## Steps
1. Identify whether the request is product App, technical Connector, Credential, Browser session, or all of them.
2. Check existing capability cards and readiness before asking for new access.
3. Write agent-local connector manifests for self setup; use owner.write_connector plus owner assignment for shared connectors.
4. Store only refs/status/allowed origins/tool namespace in connector manifests.

## Success evidence
- connector manifest write or owner assignment evidence.
- readiness next action is ready or points to the correct repair rail.
