from scenario_engine.engine import ScenarioEngine
import random

sun = [4, 2, 1, 6, 5]  # kWh/day solar

initial = {"battery": 5000}

def step_fn(state, peak):
    state["battery"] += peak * 700
    state["battery"] -= 1200
    return state

def failure_fn(state):
    return state["battery"] <= 0

years_dist = lambda: 365

sim = ScenarioEngine(sun, initial, step_fn, failure_fn, years_dist)
outcomes, fails = sim.run(20000)
print("Blackout risk:", fails / len(outcomes))
