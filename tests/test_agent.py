import json


def test_agent_json_valid():
    with open("agent.json") as f:
        data = json.load(f)
    assert "name" in data
    assert "version" in data
    assert "skills" in data
    assert "runtime" in data
