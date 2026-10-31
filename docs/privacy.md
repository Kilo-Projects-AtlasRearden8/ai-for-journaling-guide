# Privacy Rules — Keeping Your Journal Safe

Your journal is yours. Always. AI journaling tools can be powerful, but they also
raise real questions about who sees your innermost thoughts.

This page covers the rules we follow and recommend.

## The Golden Rules

### 1. Your Thoughts Are Not Training Data
- Never paste entries into tools that explicitly state they use your input
  for model training
- When in doubt, prefer local or self-hosted models
- Read the terms of service — look for clauses about "data usage"

### 2. Treat AI Like a Trusted Stranger
- You wouldn't hand your journal to someone on the street
- AI assistants are sophisticated, but they are not human confidants
- Avoid sharing names, locations, medical records, financial data, or
  deeply identifying details

### 3. Local-First Whenever Possible
Local tools process your data on your machine — no servers, no retention:
- **Ollama** (runs LLMs locally on Mac, Linux, Windows)
- **LM Studio** (desktop app with local models)
- **Jan** (open-source, privacy-focused)

```bash
# Ollama example — everything stays on your computer
ollama run mistral
```

### 4. Encrypt Before Sharing
If you must use a cloud-based tool:
- Redact personal details before pasting
- Use a local text editor, not a collaborative document
- Consider encrypting entries with a tool like `age` or `gpg`

### 5. Own Your Data
- Store journal entries in plain text or markdown files you control
- Back up regularly — to an external drive, not just the cloud
- Use version control (e.g., git) for your entries if you're comfortable:

```bash
git init ~/my-journal
git add -A
git commit -m "daily entry"
```

### 6. No Health Insights From AI

<div class="warning"><strong>Never use AI journaling as a substitute for professional mental health support.</strong> AI cannot diagnose, treat, or replace therapy. If you're struggling, reach out to a qualified professional.</div>

## What This Site Does

This manual and its templates:

- Contain **no API keys, secrets, or credentials**
- Are **fully static** — no tracking, no cookies, no analytics
- Are **local-first** — build and view on your own machine
- Are licensed under the **MIT License** — use freely, no strings attached

## Quick Privacy Checklist

| ✅ | I do this |
|---|---|
| ✓ | Use a private browser window for cloud AI tools |
| ✓ | Redact names and identifying details before pasting |
| ✓ | Prefer local or self-hosted models when possible |
| ✓ | Save entries in files I control, not platform notes |
| ✓ | Review tool permissions and data policies regularly |
| ✓ | Remember AI is a tool, not a therapist |

---

**Copyright (c) 2026 Asdale Dynamics, LLC**
