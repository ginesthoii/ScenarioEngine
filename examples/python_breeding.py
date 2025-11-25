import random
from scenario_engine.engine import ScenarioEngine

clutches = [4, 6, 8, 10]

initial = {"offspring": 0}

def step_fn(state, clutch):
    state["offspring"] += int(clutch * 0.85)
    return state

def failure_fn(state):
    return False

years_dist = lambda: random.randint(1, 10)

sim = ScenarioEngine(clutches, initial, step_fn, failure_fn, years_dist)
outcomes, fails = sim.run(1000)
print("Avg offspring:", sum(o["offspring"] for o in outcomes) / len(outcomes))
