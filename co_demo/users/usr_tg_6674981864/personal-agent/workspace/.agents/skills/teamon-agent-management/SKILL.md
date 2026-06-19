---
name: teamon-agent-management
description: Create, inspect, configure, guide setup, assign, and revoke capabilities for Personal and Process Agents through owner-scoped tools. Use when the Owner asks naturally to create or tune agents, be guided through setup, give/remove a skill/App/connector, or inspect what an agent can do.
---

# TeamON Agent Management

Create, inspect, configure, guide setup, assign, and revoke capabilities for Personal and Process Agents through owner-scoped tools.

## When to use
Use when the Owner asks naturally to create or tune agents, be guided through setup, give/remove a skill/App/connector, or inspect what an agent can do.

## Steps
1. Read the resident context to confirm actor scope and target Agent/User.
2. For broad Owner guided setup requests such as "проведи за ручку", "что дальше", "настрой сотрудников", or company access setup, first identify the target lane: new employee Personal Agent, Work/Process Agent, bot appliance, group access, or existing-user repair. Ask for at most the one missing target detail, then act through the owner tools.
3. For company-wide default language or timezone, use owner.configure_company. For one person, use owner.prepare_personal_agent language/timezone so the user override wins over the company default.
4. For a new user-owned Personal Agent, use teamon-personal-agent-onboarding, owner.manage_invite_code, and owner.prepare_personal_agent before assigning resources.
5. Use owner.* tool cards for company graph mutations and record control evidence.
6. When the Owner states durable facts about an Agent (responsibility, reporting line, assigned people, social/app ownership, knowledge scope, or operating notes), persist them before claiming success: use owner.configure_agent for purpose/interface/model changes and owner.write_context or memory.write for narrative facts scoped to that Agent/User/company.
7. If a mutation or memory write has no evidence, do not loop on "I do not see confirmation"; perform the matching write/read/check once or ask for the one missing target detail.
8. When the current user asks for their own TeamON app/desktop pairing code for this agent, call gateway.issue_bridge_code and give them the returned code (it is shown once). When the Owner asks for their owner Personal Agent code, call owner.issue_bridge_code.
9. Use ability/context reads to show current capabilities before changing them.
10. After changing access or resources, end with an Owner-facing people-and-access summary when useful: prepared users/agents, assigned skills/Apps/connectors/credentials, actual usage signals, current blockers, and next proof step. Do not dump raw private chats by default.
11. Never present slash commands as the primary product interface; commands are only fallback shortcuts.

## Success evidence
- owner/control evidence for each mutation.
- Updated capability or assignment ref is visible after the change.
- Owner summary is grounded in control/readiness/activity evidence when requested.
