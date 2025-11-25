# ScenarioEngine

ScenarioEngine is a general-purpose stochastic simulation framework for modeling
timeline-based systems. It is designed for scenarios where outcomes depend on
sequences of historical or synthetic data, probabilistic variation, and
definitions of system failure.

This library is domain-agnostic and can be used for:

- financial planning and sequence-of-returns risk
- homestead and off-grid resource modeling
- livestock production variability
- renewable energy yield and battery depletion
- cyber risk and uptime predictions
- biological or behavioral simulations
- any system that changes over time under uncertainty

## Features

- Continuous-window historical sampling
- Optional wrap-around sampling
- State-based step functions
- Custom failure detection logic
- Flexible duration distributions
- Simple, composable API

## Basic Example
from scenario_engine.engine import ScenarioEngine

data = [0.05, -0.02, 0.12]

initial = {“balance”: 100000}

def step_fn(state, r):
state[“balance”] *= (1 + r)
return state

def failure_fn(state):
return state[“balance”] <= 0

years = lambda: 30

sim = ScenarioEngine(data, initial, step_fn, failure_fn, years)
outcomes, failures = sim.run(50000)

## Installation

Clone the repository:
git clone https://github.com/ginesthoii/ScenarioEngine
