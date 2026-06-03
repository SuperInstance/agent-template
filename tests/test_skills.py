import json


def test_skills_format():
    with open("skills/base.jsonl") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            data = json.loads(line)
            assert "intent" in data
            assert "command" in data
