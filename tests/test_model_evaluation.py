import json

def test_model_accuracy():
    metrics = json.load(open("model/metrics.json"))
    assert metrics["accuracy"] >= 0.9, f"Low model accuracy: {metrics['accuracy']}"
