# Telegram bot provisioning requires BotFather token

When an owner asks to connect a new Telegram bot to a process agent, do not claim the bot is connected from @username alone. First verify whether an agent-scoped TELEGRAM_BOT_TOKEN credential exists for the target process agent. If no ready credential exists, ask the owner for the BotFather token for that bot and capture it behind the credential boundary for that exact process agent. Then call ops.provision_bot with bot_token_ref set to the exact credential ref returned by credential capture/status, plus telegram_owner_id, model_auth_ref, port, slug, and apply/start/verify options as required. If ops.provision_bot returns credential_ref_not_found, explain that the token is missing or stored under the wrong scope/label and do not say /start will work yet.

<!-- teamon-managed: owner-rule -->
