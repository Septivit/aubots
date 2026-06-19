---
name: teamon-new-agent-onboarding
description: "Bring a new Personal or Process Agent online: provision the gateway bot when needed, create/configure the Agent, attach context, connectors, credentials, skills, and verify readiness. Use when the Owner asks to create a new agent for themself, another user, a department, or a client bot, including a Telegram bot appliance."
---

# TeamON New Agent Onboarding

Bring a new Personal or Process Agent online: provision the gateway bot when needed, create/configure the Agent, attach context, connectors, credentials, skills, and verify readiness.

## When to use
Use when the Owner asks to create a new agent for themself, another user, a department, or a client bot, including a Telegram bot appliance.

## Steps
1. Confirm Owner scope and target: Personal Agent for a user, Process Agent for work, or Telegram bot appliance plus Agent. For a user-owned Personal Agent, load teamon-personal-agent-onboarding first.
2. For invite-gated onboarding, issue or inspect invite codes through owner.manage_invite_code; the new user sends the code after /start.
3. Capture or check required credentials by ref first: bot token, integration keys, and browser sessions; never put raw secrets in config or skill text. Model auth normally inherits the company model-provider token pool/server auth; pass model_auth_ref only for an explicit per-bot override.
4. For a Telegram bot appliance, call ops.provision_bot with bot_token_ref, slug, port, telegram_owner_id, and mode dry_run before apply. Do not ask the Owner for Anthropic/Claude keys when the company token pool or server auth already runs Agent turns.
5. Create or configure the Agent through owner.prepare_personal_agent, owner.create_process_agent, and owner.configure_agent; keep purpose, model, effort, interface_kind, display name, and approved Telegram group ids explicit.
6. When the Owner gives facts like "Alfred reports to A and B" or "this bot is responsible for social networks", write them to agent-scoped context immediately and configure the Agent purpose when appropriate; then verify the read-model before saying it is saved.
7. Ingest durable company/user/agent context with owner.write_context, context.ingest, or memory.write; keep procedural steps in skills and facts in context.
8. Create agent-local connectors with connector.write_local, attach shared resources with owner.assign_resource, then verify with integration.check_readiness, readiness.read, diagnostics.read_runtime_status, and ops.service_state when a service exists.
9. Finish only after the capability that matters has its own evidence: bot health/service state, readiness, or a first successful delivery/use result.

## Success evidence
- ops provisioning/service evidence when a gateway bot was created.
- owner control evidence for Agent creation/configuration/resource assignment.
- agent-scoped context or memory evidence for Owner-stated responsibilities, reporting lines, and operating notes.
- readiness or diagnostics evidence proves the new Agent can use the configured capabilities.
