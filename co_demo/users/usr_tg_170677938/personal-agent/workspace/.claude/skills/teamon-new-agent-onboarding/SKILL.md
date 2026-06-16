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
3. Capture or check required credentials by ref first: bot token, model auth, integration keys, and browser sessions; never put raw secrets in config or skill text.
4. For a Telegram bot appliance, call ops.provision_bot with bot_token_ref, slug, port, telegram_owner_id, model_auth_ref, and mode dry_run before apply.
5. Create or configure the Agent through owner.prepare_personal_agent, owner.create_process_agent, and owner.configure_agent; keep purpose, model, effort, interface_kind, and display name explicit.
6. Ingest durable company/user/agent context with context.ingest or memory.write; keep procedural steps in skills and facts in context.
7. Create agent-local connectors with connector.write_local, attach shared resources with owner.assign_resource, then verify with integration.check_readiness, readiness.read, diagnostics.read_runtime_status, and ops.service_state when a service exists.
8. Finish only after the capability that matters has its own evidence: bot health/service state, readiness, or a first successful delivery/use result.

## Owner-action wording rule
Before successful owner/ops/credential tool evidence, do not say "creating",
"adding", "done", "created", "configured", "issued", "removed", or equivalent
Russian wording such as "создаю", "добавляю", "готово", "создал", "настроил",
"выдал", "удалил".

If the Owner request is missing names, purposes, users, bot usernames, tokens,
or other required inputs, ask a neutral clarification question instead. Use
phrasing like "нужны названия и назначения" or "уточни список", not "сейчас
создам" or "сразу заведу".

If enough data is present and the tool is available, call the typed tool first.
Only after the tool result/evidence may the final answer claim the action is
done and list created/changed refs.

## Success evidence
- ops provisioning/service evidence when a gateway bot was created.
- owner control evidence for Agent creation/configuration/resource assignment.
- readiness or diagnostics evidence proves the new Agent can use the configured capabilities.
