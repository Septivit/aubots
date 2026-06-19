# Конфигурация: @SPTV_SMM_bot → группа SEPTIVIT ДЕЛА

**Дата:** 2026-06-19

## Что настроено

| Элемент | Ref / значение |
|---|---|
| Коннектор | `connector:company:co_demo:telegram_smm_outgoing` |
| Контекст agt_smm | `smm_telegram_group_septivit_dela` (chat_id `-1003615346714`) |
| Скилл agt_smm | `send-to-septivit-group` |

## Как работает скилл

agt_smm при вызове скилла `send-to-septivit-group`:

1. Берёт `TELEGRAM_BOT_TOKEN` из env-переменной сервиса
2. Делает POST на `https://api.telegram.org/bot{token}/sendMessage`
3. Отправляет текст в группу `chat_id = -1003615346714`
4. Подтверждает `"ok": true` в ответе API

## Что нужно сделать вам

1. **Добавьте @SPTV_SMM_bot в группу SEPTIVIT ДЕЛА** как участника (с правом отправки сообщений)
2. Напишите боту в личку: `отправь тест в группу SEPTIVIT ДЕЛА`

## Почему gateway.send_artifact не подходит для групп

`gateway.send_artifact` — рельс доставки привязан к текущей поверхности (чат с пользователем). Для отправки в **другой** групповой чат нужен прямой вызов Telegram Bot API с токеном бота — именно это и делает новый скилл через `terminal_shell`.
