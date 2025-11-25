import random
from scenario_engine.engine import ScenarioEngine
from scenario_engine.sampling import triangular_years

returns = [0.05, -0.02, 0.12, 0.04]

initial = {"balance": 2_000_000}

def step_fn(state, r):
    withdrawal = 80_000
    state["balance"] -= withdrawal
    state["balance"] *= (1 + r)
    return state

def failure_fn(state):
    return state["balance"] <= 0

years_dist = lambda: triangular_years(18, 40, 25)

sim = ScenarioEngine(returns, initial, step_fn, failure_fn, years_dist)
outcomes, fails = sim.run(50_000)
print("Probability of ruin:", fails / len(outcomes))
