# Mailroom

Newsletter tool for **Kettlebird Tea's Steep Club**. Python 3.12 project managed with `uv`.

## What it is

Mailroom is a command-line tool for one newsletter: Kettlebird Tea's Steep Club.
It reads the subscribers, checks an issue, and sends it to a practice mail server.

## Rules

- Use uv for everything.
- Never use a real person's email address. Use `@example.com`, and `@resend.dev` for practice sends.
- Commit and push after every step.

## Purpose

This is a learning project. The owner is learning Python from the book
"Programming Fundamentals" (Building AI Workers):
https://agentfactory.panaversity.org/building-ai-workers/programming-fundamentals/overview/

Build the newsletter incrementally, using only concepts the learner has already covered.

## Learner level

- **Covered so far: up to and including section 13.7** of the book.
- The learner will update this line as they progress. Treat it as the source of truth.
- Do not use language features or concepts from later sections without first
  explaining them briefly and saying which part of the book covers them.

## How to work with the learner

- Prefer simple, readable code over clever code. Match the learner's current level.
- Explain *why*, not just *what*. Keep explanations short.
- Make small steps; one concept per change where possible.
- Point to the relevant book section when introducing or reinforcing a concept.
- When a better, more advanced approach exists, mention it as "later" rather than using it now.
- Add type hints and docstrings only to the extent the learner has covered them.

## Commands (uv)

- Run: `uv run main.py`
- Add a dependency: `uv add <package>`
- Add a dev dependency: `uv add --dev <package>`
- Sync environment: `uv sync`
- Python version: 3.12 (pinned in `.python-version`)

## Conventions

- Never edit `uv.lock` by hand; use `uv` commands.
- Do not commit `.venv/`.
- Keep secrets (API keys, email credentials) out of the code; use environment variables or an untracked `.env`.
