from scenario_engine.engine import ScenarioEngine

rain = [3.2, 1.1, 0.0, 5.3]  # inches/month

initial = {"water": 10_000}

def step_fn(state, rainfall):
    state["water"] += rainfall * 150
    state["water"] -= 400
    return state

def failure_fn(state):
    return state["water"] <= 0

years_dist = lambda: 36  # 3 years

sim = ScenarioEngine(rain, initial, step_fn, failure_fn, years_dist)
outcomes, fails = sim.run(10_000)
print("Failure probability:", fails / len(outcomes))
