# TeamON Instance State

**Это — цифровой след вашей компании.** Память ваших AI-агентов, библиотека навыков,
контекст процессов. Всё, что команда накопила, взаимодействуя с TeamON, живёт здесь.

Код платформы TeamON обновляется отдельно. **Этот репозиторий — ваш.** Если завтра вы
уходите с платформы — вы уносите эту папку и поднимаете всё на любом другом хосте с TeamON.

## Что сюда НЕ попадает (и почему)

- секреты инстанса (deploy-ключ, токены) — `secrets/`
- per-agent OAuth-креды интеграций — `credential-secrets/`
- control-plane SQLite (бинарник; восстанавливается из слоёв) — `control-plane.sqlite`
- состояние каналов (bot token) — `*-gateway-state.json`
- per-capsule runtime / browser-state / cache — `agents/*/{runtime,browser-state,...}`

Проверено тройной защитой: `.gitignore` + defensive `git reset` в плане sync +
path-allowlist в чистом планировщике (unit-tested против секрет-директорий инстанса).

## Как работает sync

State sync инициируется из Control Room (операторская сессия, никогда не автоматически).
TeamON через типизированный инструмент `ops.git_sync` делает `git add` операторских путей,
подписанный `git commit` и `git push`. Работа идёт от имени НЕ-root сервис-пользователя
инстанса; deploy-ключ лежит под secretsDir с правами 0600 и наружу не выходит.

## Как восстановить из бэкапа

На новом хосте: разверни TeamON, затем на голом instance root до запуска —
`git init && git remote add origin <url> && git fetch origin && git checkout origin/main`,
после чего запусти сервис. (Формальный restore через UI — отдельный sub-project, пока manual.)

---

_Управляется [TeamON](https://github.com/) — self-hosted AI-agent platform.
Автообновление выключено по умолчанию (оператор нажимает Sync, когда готов)._
