---
name: teamon-reminder-delivery-diagnostics
description: Schedule, deliver, and diagnose recurring work through typed scheduler/gateway/diagnostics tools. Use when the user asks for reminders, recurring reports, status checks, restarts, or failure explanations.
---

# TeamON Reminder Delivery Diagnostics

Schedule, deliver, and diagnose recurring work through typed scheduler/gateway/diagnostics tools.

## When to use
Use when the user asks for reminders, recurring reports, status checks, restarts, or failure explanations.

## Steps
1. Create or inspect scheduler state through scheduler.* tools, not cron or systemd files.
2. Send reports/files through gateway refs and bind final claims to delivery evidence.
3. Use scheduler.*, gateway.*, and diagnostics.* typed helpers for status, delivery, and failure explanations; never raw shell commands.
4. If a long task is still running, send progress instead of appearing stuck.

## Success evidence
- scheduled job, gateway delivery, or diagnostics evidence supports the final claim.
