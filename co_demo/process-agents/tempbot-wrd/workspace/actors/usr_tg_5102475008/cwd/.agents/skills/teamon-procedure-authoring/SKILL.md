---
name: teamon-procedure-authoring
description: Turn repeated work into a compact procedural skill without copying raw secrets or company data into the skill body. Use when a user asks the agent to remember a procedure, improve itself, or package a repeatable workflow.
---

# TeamON Skill Authoring

Turn repeated work into a compact procedural skill without copying raw secrets or company data into the skill body.

## When to use
Use when a user asks the agent to remember a procedure, improve itself, or package a repeatable workflow.

## Steps
1. Separate procedure from knowledge: keep steps in the skill and read facts/policies through context or library tools.
2. Include when-to-use, ordered steps, required capability refs, and success evidence.
3. Validate that the body contains no raw credential values, cookies, storage state, or handoff URLs.
4. Author the skill with skill.write_local — it stores it as .claude/skills/<name>/SKILL.md so the native loader picks it up; write locally first and promote to Hub only through owner approval.

## Success evidence
- skill package validates.
- local skill ref or promoted Hub skill ref is returned.
