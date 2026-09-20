from chimera import Event, classify

def test_classical_recursive():
    r = classify(Event(
        object="system",
        interaction="logged result re-enters next state",
        has_classical_record=True,
        recursive_feedback=True,
        operational_recovery=False,
    ))
    assert set(r["tags"]) == {"C", "R", "D"}

def test_key_requires_map():
    r = classify(Event(
        object="state",
        interaction="correlate claimed as key",
        has_identifiable_key=True,
        has_recovery_map=False,
        operational_recovery=False,
    ))
    assert "K" not in r["tags"]

def test_quantum():
    r = classify(Event(
        object="quantum subsystem",
        interaction="entangling measurement",
        has_quantum_correlation=True,
        operational_recovery=False,
    ))
    assert "Q" in r["tags"]

if __name__ == "__main__":
    test_classical_recursive()
    test_key_requires_map()
    test_quantum()
    print("CHIMERA tests passed.")
