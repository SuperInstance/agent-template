# agent-template

**Git-native agent template** for the SuperInstance ecosystem. Fork to create a new agent. Every agent IS a git repo — skills are branches, forks are clones, PRs are evolution.

## Why It Matters

The SuperInstance ecosystem contains 100+ autonomous agents, each living inside a GitHub repository. The repository IS the agent: identity lives in `agent.json`, skills are JSONL packs, state persists in `memory/`, and the git history is the agent's autobiography. This template provides the standard DNA — the minimum viable structure every new agent needs to participate in the fleet.

Standardization matters because agents must be interoperable. A fleet orchestrator dispatches tasks by reading `agent.json` and matching capabilities. A skill exchange works because all agents use the same JSONL format. State migrations run because all agents share the `migrations/` schema. Without a template, every agent would be a snowflake — unable to communicate, coordinate, or evolve through the fleet's genetic operators (fork, branch, merge, PR).

This template encodes the **git-native agent protocol**: a specification for agent-as-repository that makes agents trivially forkable, auditable via `git log`, and portable across runtimes (lever-runner, OpenClaw, Codespaces).

## How It Works

### Agent Identity (`agent.json`)

The identity file is the agent's passport. It declares:

```json
{
  "name": "my-agent",
  "version": "0.1.0",
  "description": "A git-native agent",
  "runtime": "lever-runner",
  "skills": ["base"],
  "thresholds": {
    "match_confidence": 0.7,
    "auto_promote": 0.9
  },
  "export_formats": ["nail", "jsonl"],
  "compatibility": {
    "pincherOS": ">=0.1.0",
    "lever-runner": ">=0.3.0"
  }
}
```

The `thresholds` control skill matching: incoming tasks with confidence ≥ `auto_promote` are auto-accepted; those between `match_confidence` and `auto_promote` require human review. This implements a **two-threshold acceptance policy** common in fuzzy matching systems:

```
accept(T) = { auto    if confidence(T) ≥ auto_promote
            { review  if match_confidence ≤ confidence(T) < auto_promote
            { reject  if confidence(T) < match_confidence
```

**Complexity:** Skill matching is O(K × S) where K is the number of skill keys in the task and S is the skill database size. With inverted indices, this drops to O(K × log S).

### Skill System

Skills are JSONL (JSON Lines) packs in `skills/`. Each line is one training example:

```jsonl
{"input": "summarize this", "output": "...", "skill": "base", "confidence": 0.95}
{"input": "translate to fr", "output": "...", "skill": "translate", "confidence": 0.82}
```

JSONL is chosen over JSON arrays for two reasons:

1. **Streaming** — parsers can process one line at a time, enabling incremental loading for large skill packs
2. **Append-only** — new skills append without reading or rewriting the file, making concurrent writes safe

**Big-O:** Skill lookup with linear scan: O(N) per skill pack. With pre-built hash index on skill name: O(1) average, O(N) worst case (all entries same skill).

### State and Memory

Agent state lives in `memory/` (gitignored — agent-local, not shared). The separation between shared (git) and local (memory) follows the **CQRS pattern**: the git repo is the command side (append-only decisions via commits), memory is the query side (mutable runtime cache).

State migrations in `migrations/` handle schema evolution:

```
migrations/
├── 001_initial.sql
├── 002_add_skills_table.sql
└── 003_add_confidence_column.sql
```

Applied in order, tracked by version number — standard migration pattern.

### Directory Structure

```
agent-template/
├── agent.json          # Identity (the agent's passport)
├── AGENT.md            # Ensign log — who I am in the fleet
├── README.md           # This file
├── skills/             # JSONL skill packs (can be branches)
├── config/             # Thresholds, confidence levels
├── memory/             # Agent-local state (gitignored)
├── migrations/         # State schema evolution
└── .gitignore          # Excludes memory/, .env, secrets
```

### Git as Genetic Material

The evolutionary operators are:

| Operator | Git Command | Biological Analog |
|----------|-------------|-------------------|
| Fork | `gh repo fork` | Asexual reproduction |
| Branch skill | `git branch skill-nlp` | Gene expression variant |
| Merge skill | `git merge skill-nlp` | Recombination |
| Submit PR | `gh pr create` | Fitness test |
| Accept PR | `gh pr merge` | Selection |

## Quick Start

### Create a new agent from this template

```bash
# Option 1: GitHub UI
# Click "Use this template" on the repository page

# Option 2: CLI
gh repo create my-new-agent --template SuperInstance/agent-template
cd my-new-agent

# Edit identity
vim agent.json
# Change "name" to your agent's name

# Add skills
echo '{"input":"hello","output":"hi","skill":"greeting","confidence":0.9}' >> skills/base.jsonl

# Commit your agent's birth
git add -A
git commit -m "born: my-new-agent"
git push origin main
```

### Agent.json Reference

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Agent identifier (unique in fleet) |
| `version` | string | SemVer version |
| `description` | string | One-line description |
| `runtime` | string | Execution environment (`lever-runner`, `openclaw`) |
| `skills` | string[] | Skill pack names loaded at startup |
| `thresholds.match_confidence` | float | Minimum confidence for review queue |
| `thresholds.auto_promote` | float | Confidence threshold for auto-accept |
| `export_formats` | string[] | Supported serialization formats |
| `compatibility` | object | Version constraints for runtime/platform |

## API

This is a template — no Rust API. The "API" is the file system convention:

| Path | Format | Purpose |
|------|--------|---------|
| `agent.json` | JSON | Agent identity and configuration |
| `skills/*.jsonl` | JSONL | Skill training data |
| `config/*.json` | JSON | Runtime configuration |
| `memory/*` | Any | Agent-local mutable state |
| `migrations/*.sql` | SQL | Schema evolution |

## Architecture Notes

The template instantiates the **agent genome** within the γ + η = C framework. The git repository is C — the conserved identity that survives across forks, restarts, and migrations. Agent contributions (γ) are the commits: decisions, skills, and code that shape the agent's behavior. Environmental responses (η) are the issues, PRs, and fleet interactions that shape the agent's evolution.

The conservation law ensures that forking preserves identity: the forked agent has the same skills, thresholds, and configuration. Divergence happens through subsequent commits (γ changes), and the original template's genome is conserved in the fork's history.

See the [architecture overview](https://github.com/SuperInstance/agent-template/blob/main/ARCHITECTURE.md).

## References

1. Fowler, M. (2015). "CQRS." *martinfowler.com*.
2. GitHub. "Creating a repository from a template." *GitHub Docs*.
3. Ostrom, E. (1990). *Governing the Commons*. Cambridge University Press. (Institutional design patterns for shared resources)

## License

MIT
