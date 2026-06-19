---
name: teamon-new-agent-onboarding
description: "Guide the Owner through bringing a new Personal or Process Agent online: scope, create/configure, attach context, connectors, credentials, skills, and verify readiness. Use when the Owner asks to be guided through setup or to create a new agent for themself, another user, a department, or a client bot, including a Telegram bot appliance."
---

# TeamON New Agent Onboarding

Guide the Owner through bringing a new Personal or Process Agent online: scope, create/configure, attach context, connectors, credentials, skills, and verify readiness.

## When to use
Use when the Owner asks to be guided through setup or to create a new agent for themself, another user, a department, or a client bot, including a Telegram bot appliance.

## Steps
1. Confirm Owner scope and target: Personal Agent for a user, Process Agent for work, or Telegram bot appliance plus Agent. This is Owner guided setup, not the one-time first-run user bootstrap.
2. For a broad "проведи за ручку" setup, keep a short working checklist in the reply: target user/agent, purpose and starter context, skills/Apps/connectors, credentials/browser sessions, access/group scope, and proof of first use. Do not turn it into a long questionnaire; collect the minimum missing fact and then execute the next owner tool.
3. If the Owner asks for company-wide language, locale, or timezone defaults, use owner.configure_company; per-user language/timezone belongs in owner.prepare_personal_agent.
4. For a user-owned Personal Agent, load teamon-personal-agent-onboarding first so invite, Telegram identity, private credentials, starter context, and people-and-access summary follow the narrower Personal Agent rules.
5. For invite-gated onboarding, issue or inspect invite codes through owner.manage_invite_code; the new user sends the code after /start.
6. Capture or check required credentials by ref first: bot token, integration keys, and browser sessions; never put raw secrets in config or skill text. Model auth normally inherits the company model-provider token pool/server auth; pass model_auth_ref only for an explicit per-bot override.
7. If the turn contains a [TeamON credential intake] block with TELEGRAM_BOT_TOKEN, use that credential_N_ref directly as ops.provision_bot bot_token_ref. Do not ask the Owner to paste the token again, use an admin console, or create a separate secret intake. If the target Agent was just created in this conversation, continue from that agent_ref/slug.
8. When a bot token credential is scoped to an Agent, treat that Agent as canonical: use its existing agent_ref/slug from the TeamON read-model and never derive the provisioned service slug from @bot username, t.me link, or token label.
9. For bot username or connected-bots inventory questions, answer from the TeamON graph/read-model: app.list, readiness.read, owner tools, and ops.service_state. Do not call api.telegram.org through generic integration.http_request and do not construct Bot API URLs with bot tokens.
10. For a Telegram bot appliance, call ops.provision_bot with bot_token_ref, slug, port, telegram_owner_id, and mode dry_run before apply. Do not ask the Owner for Anthropic/Claude keys when the company token pool or server auth already runs Agent turns.
11. For follow-up questions such as "ты подключил/поднял/запустил бота?", run ops.service_state or ops.provision_bot again before answering. Do not reuse an older host-helper failure from context as current service truth.
12. When the Owner asks to remove a test or extra bot service, use ops.deprovision_bot with the service name or slug, then verify with ops.service_state before claiming cleanup. Do not delete durable state unless the Owner explicitly asks for destructive cleanup.
13. Create or configure the Agent through owner.prepare_personal_agent, owner.create_process_agent, and owner.configure_agent; keep purpose, model, effort, interface_kind, display name, and approved Telegram group ids explicit.
14. For direct Telegram work-bot groups, distinguish access/mode from reminders: allowed_group_chat_ids plus group_behavior_mode are owner.configure_agent settings. If the Owner asks what behavior mode is needed for scheduled group messages, explain silent/mention/active and ask or apply the mode; do not create or claim a scheduler/reminder unless the concrete time, content, and delivery target are provided.
15. When the Owner gives facts like "Alfred reports to A and B" or "this bot is responsible for social networks", write them to agent-scoped context immediately and configure the Agent purpose when appropriate; then verify the read-model before saying it is saved.
16. Ingest durable company/user/agent context with owner.write_context, context.ingest, or memory.write; keep procedural steps in skills and facts in context.
17. Create agent-local connectors with connector.write_local, attach shared resources with owner.assign_resource, then verify with integration.check_readiness, readiness.read, diagnostics.read_runtime_status, and ops.service_state when a service exists.
18. After provisioning or resource changes, read app.list, readiness.read, activity.read, trace.read, or context.search as needed and give the Owner a people-and-access summary: who can use what, which resources are assigned, what has actually been used, blockers, and the next live proof. Do not dump raw private chats by default.
19. Finish only after the capability that matters has its own evidence: bot health/service state, readiness, or a first successful delivery/use result.

## Success evidence
- ops provisioning/service evidence when a gateway bot was created.
- owner control evidence for Agent creation/configuration/resource assignment.
- agent-scoped context or memory evidence for Owner-stated responsibilities, reporting lines, and operating notes.
- Owner-facing people-and-access summary is grounded in control/readiness/activity evidence.
- readiness or diagnostics evidence proves the new Agent can use the configured capabilities.
