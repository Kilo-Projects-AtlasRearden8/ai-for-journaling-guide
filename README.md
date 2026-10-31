# AI for Journaling — A Beginner's Manual

A warm, low-pressure guide to using AI as a journaling companion. Learn reflection
prompts, mood tracking, entry organization, and how to turn your notes into
meaningful insights — all with strong privacy rules and a local-first mindset.

**Created by Asdale Dynamics, LLC** — founded by Dylan Asdale, a registered nurse
turned AI author based in Indiana. Asdale Dynamics, LLC (formed October 2026)
focuses on beginner-friendly AI education, books and guides, and practical tools.
Dylan also writes *The Massive AI Manual* and runs the hub site
[dylanasdale.github.io](https://dylanasdale.github.io), where he explains AI
*like a friend would*: plain English, step by step, never condescending.

This manual is part of the Asdale Dynamics, LLC catalog of accessible,
life-admin-friendly guides — designed for beginners, healthcare workers,
caregivers, and anyone who wants AI as a gentle companion, not a replacement
for their own voice.

## What's Inside

| Topic | What You'll Learn |
|---|---|
| Getting Started | How AI journaling works and how to begin safely |
| Privacy Rules | Keeping your entries private and your data yours |
| Reflection Prompts | AI-powered questions for daily, weekly, monthly reflection |
| Mood Tracking | Simple mood logs and spotting patterns over time |
| Organizing Entries | Tagging, categorizing, and finding your writing easily |
| Insights | Using AI to surface themes and turn notes into action |
| Printable Templates | Downloadable and printable journal pages |

## Quick Start

```bash
# Clone or download this repository
cd ai-for-journaling-guide

# Build the static site
python3 build.py

# Run verification tests
make test

# Serve locally (optional)
python3 -m http.server 8000 --directory site/

# Open in your browser
# http://localhost:8000/
```

## Project Structure

```
.
├── docs/                    # Markdown source for the manual
├── site/                    # Generated static HTML site (output)
├── templates/               # Printable journal templates
├── assets/                  # Site stylesheets
├── build.py                 # Static site generator + test suite
├── Makefile                 # Build and test shortcuts
├── LICENSE                  # MIT License
├── README.md                # This file
├── AGENTS.md                # Build & test guide
└── STATUS.md                # Build status and verification
```

## Privacy First

This manual and its templates:

- Contain **no API keys, secrets, or credentials**
- Are **fully static** — no tracking, no cookies, no analytics
- Are **local-first** — build and view on your own machine
- Are licensed under the **MIT License** — use freely, no strings attached

See the [Privacy Rules](docs/privacy.md) page for guidance on keeping your
journal entries safe with AI tools.

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE)
file for details.

**Copyright (c) 2026 Asdale Dynamics, LLC**

Credit: Asdale Dynamics, LLC — beginner-friendly AI education, books, and
practical tools.
