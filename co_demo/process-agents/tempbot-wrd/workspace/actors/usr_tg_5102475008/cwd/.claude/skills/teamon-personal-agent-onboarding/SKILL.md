---
name: teamon-personal-agent-onboarding
description: "Guide the Owner through preparing a new user-owned Personal Agent from chat: Telegram identity, model, rights, connectors, credentials, skills, and starter context. Use when the Owner says they are preparing Alpha or another Personal Agent for a new person and wants to do the setup conversationally."
---

# TeamON Personal Agent Onboarding

Guide the Owner through preparing a new user-owned Personal Agent from chat: Telegram identity, model, rights, connectors, credentials, skills, and starter context.

## When to use
Use when the Owner says they are preparing Alpha or another Personal Agent for a new person and wants to do the setup conversationally.

## Steps
1. Collect only the setup facts needed now: display name, Telegram @username, numeric Telegram user id if available, language/timezone, purpose, model, effort, interface_kind, starter context, expected connectors/skills/apps/knowledge.
2. If the new user should self-enter through the bot, call owner.manage_invite_code with mode="issue"; tell the Owner to share only that invite code. Unknown users who send /start get the invite-code challenge before any Agent turn.
3. Call owner.prepare_personal_agent with display_name, telegram_username, telegram_user_id when known, purpose, model, effort, interface_kind, and initial_context. Treat @username as a label; do not claim Telegram routing is live until the numeric id is known or the user sends the bot a first message.
4. If the Owner explicitly asks to give this user full/admin access, include delegated_admin=true. Do not infer delegated-admin from questions or opinions; rights changes require an explicit grant.
5. For Telegram/WhatsApp userbot interfaces, prepare the interface passport and direct the Owner to Control for account linking. Do not ask for phone codes, 2FA, QR payloads, session strings, or raw auth-state in chat.
6. When a prepared @username user later sends an invite/first message, use that prepared user_ref/agent_ref and link the numeric Telegram id; do not create a duplicate numeric user and leave prior rights on the username placeholder.
7. Use owner.configure_agent for later model, effort, interface_kind, name, purpose, or direct Telegram work-bot group allowlist changes; it works for Personal Agents as well as Process Agents.
8. Grant rights with owner.assign_resource to the returned user_ref or agent_ref: skills, Apps, workflows, connectors, knowledge, and templates. Remove mistaken or obsolete grants with owner.revoke_resource. Prefer explicit per-user/per-agent targets over broad all-users grants.
9. For credentials, run credential.status first. If the Owner explicitly provides a secret for this user, agent, or company, call owner.capture_credential with scope plus target_user_ref or target_agent_ref; for private user-owned secrets, ask the new user to paste them in their own Personal Agent chat.
10. For connectors, attach existing shared connector resources with owner.assign_resource. Agent-local connector.write_local configures the current Agent capsule; do not pretend it configured another user capsule unless the target Agent actually runs that tool.
11. Verify with readiness.read, integration.check_readiness, diagnostics.read_runtime_status, and finally a real Telegram route/agent-turn or capability-use evidence before saying the Personal Agent is ready.

## Success evidence
- owner.prepare_personal_agent returned user_ref and agent_ref.
- owner control evidence exists for every resource/right/model change.
- credential capture/status evidence exists for each configured credential, without raw values.
- readiness, diagnostics, or first Telegram turn evidence proves the setup works.
