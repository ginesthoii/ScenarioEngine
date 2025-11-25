from scenario_engine.engine import ScenarioEngine

def test_run_loop_completes():
    data = [1, 2, 3]

    initial = {"x": 0}

    def step_fn(state, dp):
        state["x"] += dp
        return state

    def failure_fn(state):
        return False

    years = lambda: 5

    sim = ScenarioEngine(data, initial, step_fn, failure_fn, years)
    outcomes, fails = sim.run(100)

    assert len(outcomes) == 100
    assert fails == 0
