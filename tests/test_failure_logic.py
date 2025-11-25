from scenario_engine.engine import ScenarioEngine

def test_failure_detected():
    data = [1]

    initial = {"x": 0}

    def step_fn(state, dp):
        state["x"] -= 10
        return state

    def failure_fn(state):
        return state["x"] < -5

    years = lambda: 3

    sim = ScenarioEngine(data, initial, step_fn, failure_fn, years)
    outcomes, fails = sim.run(50)

    assert fails > 0
