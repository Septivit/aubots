---
name: teamon-agent-management
description: Create, inspect, configure, assign, and revoke capabilities for Personal and Process Agents through owner-scoped tools. Use when the Owner asks naturally to create or tune agents, give/remove a skill/App/connector, or inspect what an agent can do.
---

# TeamON Agent Management

Create, inspect, configure, assign, and revoke capabilities for Personal and Process Agents through owner-scoped tools.

## When to use
Use when the Owner asks naturally to create or tune agents, give/remove a skill/App/connector, or inspect what an agent can do.

## Steps
1. Read the resident context to confirm actor scope and target Agent/User.
2. For a new user-owned Personal Agent, use teamon-personal-agent-onboarding, owner.manage_invite_code, and owner.prepare_personal_agent before assigning resources.
3. Use owner.* tool cards for company graph mutations and record control evidence.
4. Use ability/context reads to show current capabilities before changing them.
5. Never present slash commands as the primary product interface; commands are only fallback shortcuts.
6. Never claim or imply an owner mutation is happening or finished before a successful owner.* tool result. If data is missing, ask for the missing data with neutral wording; do not write "creating", "adding", "done", "создаю", "добавляю", "готово", "сразу заведу" before evidence.

## Success evidence
- owner/control evidence for each mutation.
- Updated capability or assignment ref is visible after the change.
