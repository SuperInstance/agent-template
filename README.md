# agent-template

Git-native agent template for the SuperInstance ecosystem. Fork to create a new agent.

## What is a Git-Native Agent?

In the SuperInstance ecosystem, **every agent IS a git repo**. Skills are branches. Fork to copy. PR to evolve. This template is the DNA — the starting point for building new agents.

- **Agent identity** lives in `agent.json`
- **Skills** live as JSONL packs in `skills/` (each can be its own branch)
- **State** lives in `memory/` (gitignored — agent-local)
- **Config** lives in `config/` (thresholds, confidence levels)
- **Migrations** in `migrations/` handle state schema evolution

## Quick Start

### Create a new agent from this template

1. Click **"Use this template"** on GitHub, or:
   ```bash
   # Fork it
   gh repo fork SuperInstance/agent-template --clone
   mv agent-template my-agent
   cd my-agent
   ```

2. Edit `agent.json` — set your agent's name, description, and runtime.

3. Add skills to `skills/` or create skill branches (see below).

4. Commit and push. You now have a living agent.

### Add a skill

Skills are branches. Create one, add your JSONL, and PR it:

```bash
git checkout -b skill/monitoring
# Add intents to skills/monitoring.jsonl
echo '{"intent": "check cpu load", "command": "top -bn1 | head -5"}' >> skills/monitoring.jsonl
git add skills/ && git commit -m "Add monitoring skill"
git push origin skill/monitoring
# Open a PR to merge into main
```

### Fork an agent

```bash
gh repo fork some-org/cool-agent --clone
# Now it's yours. Evolve it.
```

### Evolve through PRs

See a skill you like in another agent? Cherry-pick it or open a cross-repo PR. Agents evolve through the same social coding workflow as software:

1. **Template → Instance**: Use this template, customize `agent.json`
2. **Instance → Fork**: Someone forks your agent, takes it in a new direction
3. **Fork → Merge**: Best skills get PR'd back upstream
4. **Merge → Evolve**: The ecosystem gets better for everyone

## Lifecycle

```
Template ──→ Instance ──→ Fork ──→ Merge ──→ Evolve
                 ↑                        │
                 └────────────────────────┘
```

## File Structure

```
agent-template/
├── agent.json             # Agent identity and metadata
├── skills/                # Skill packs (JSONL)
│   ├── base.jsonl         # Core universal skills
│   └── README.md
├── memory/                # Agent state (gitignored)
├── config/
│   └── thresholds.json    # Matching thresholds
├── migrations/            # State migration scripts
├── tests/                 # Validate agent.json and skills
└── .gitignore
```

## Tests

```bash
pytest tests/
```

## License

MIT
