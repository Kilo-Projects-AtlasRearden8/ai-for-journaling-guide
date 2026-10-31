# Organizing Entries — Your Journal, Your System

An organized journal is easier to revisit — and AI can help you find meaning
in old entries without drowning in folders and tags.

## The Minimum-Viable System

You don't need elaborate categories. Start with:

1. **Date** — filename or header (e.g., `2024-10-20.md`)
2. **One tag** — a single word at the top (`#gratitude`, `#stress`, `#idea`)
3. **Search** — Ctrl+F or `grep` to find entries

That's enough. You can always evolve it later.

## Naming and Filing

**Option A: Folder by month**
```
journal/
  2024-10/
    2024-10-20.md
    2024-10-21.md
```

**Option B: Flat folder with date prefixes**
```
journal/
  2024-10-20.md
  2024-10-21.md
```

**Option C: Tag-based**
```
journal/
  gratitude/
  reflections/
  ideas/
```

Pick whatever feels effortless — then stick with it for 30 days before changing.

## Using Tags Wisely

Tags are shortcuts for your future self. Add 1–2 per entry:

- `#reflection` — deeper processing
- `#idea` — sparks worth revisiting
- `#gratitude` — things you're thankful for
- `#stress` — worries or challenges
- `#insight` — "aha" moments
- `#todo` — small next steps

## AI-Powered Organization

Ask AI to help once a month:

> "I have 30 journal entries tagged with various topics. Could you summarize
> the main themes I keep writing about?"

Or for deeper dives:

> "Find entries where I mentioned 'overwhelmed' and summarize what I was
> going through."

## Search Strategies

### With your editor or terminal
```bash
# Find all entries mentioning a word
grep -r "overwhelmed" journal/

# Find by tag
grep -r "#stress" journal/
```

### With AI assistance
> "In my entries from last month, when did I mention feeling uncertain?"

## Retrospective: "What Did I Learn?"

At the end of each month, ask AI to help you surface insights:

> "Here are my 4 entries from this week. What themes or recurring thoughts do
> you notice? What might I want to explore further next month?"

## Digital vs. Paper Organization

| Digital | Paper |
|---|---|
| Fast search (Ctrl+F) | Physical, tactile |
| Tags are easy to edit | Harder to reorganize later |
| Backups to cloud/drive | No risk of file corruption |
| AI can scan 100s of entries | Private by default |

Choose what aligns with your energy and privacy needs. You can even mix —
write by hand some days, type others.

## Templates for Organization

This manual includes printable organization aids:

- Monthly index pages for your binder
- Tag reference sheets
- Entry templates with built-in prompts

See [Printable Templates](templates.html) for the full set.

---

**Copyright (c) 2026 Asdale Dynamics, LLC**
