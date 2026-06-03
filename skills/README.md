# Skills

Skills are branches. Each skill pack is a JSONL file defining intents and commands.

## Adding a Skill

```bash
git checkout -b skill/my-skill
# Add or edit .jsonl files in skills/
git add skills/
git commit -m "Add my-skill"
git push origin skill/my-skill
# Open a PR to merge into main
```

## Skill Pack Format

Each line is a JSON object with `intent` and `command`:

```jsonl
{"intent": "describe what you want", "command": "shell command to run"}
```
