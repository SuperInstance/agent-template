# Future Integration: agent-template

## Current State
Git-native agent template for the SuperInstance ecosystem. Fork to create a new agent. Agent identity in `agent.json`, skills as JSONL packs in `skills/`, state in `memory/` (gitignored), config in `config/`, migrations in `migrations/`. The DNA of new fleet members.

## Integration Opportunities

### With new fleet member bootstrapping
agent-template IS how new fleet members are created. Fork the template → customize agent.json → add skills → deploy. The template provides the standard structure: identity, skills, state, config, migrations. Every new vessel starts here.

### With construct-core skill system
The template's skills/ directory maps to construct-core's SkillSpec system. Each JSONL skill pack defines a skill's capabilities, dependencies, and compilation targets. When the agent boots, construct-core loads the skill packs and makes them available via load_skill/unload_skill.

### With room-as-codespace
When a new room needs an ensign, it forks agent-template with room-specific configuration. The ensign boots with the room's skills, connects to the room's cell grid, and begins ticking. Template → ensign in 3 minutes.

## Dormant Ideas Now Unlockable
The template was for static agent configuration. Now construct-core provides dynamic skill loading, ternary-registry provides capability discovery, and room-as-codespace provides deployment. The template becomes a living starting point.

## Potential in Mature Systems
agent-template is the fleet's reproduction mechanism. Every new agent, every new ensign, every new room starts from this template. The fleet grows by forking.

## Cross-Pollination Ideas
- **SuperInstance-Starter-Agent**: Starter Agent's philosophy informs the template
- **git-agent-codespace**: Template + Codespace = operational agent
- **oracle1-vessel**: Oracle1 manages the fleet of template-forked agents

## Dependencies for Next Steps
- Template → construct-core SkillSpec bridge
- Room-specific template configurations
- Fleet registration on fork (auto-notify Oracle1)
