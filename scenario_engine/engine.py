import random
from typing import Callable, Dict, Any, List, Tuple

class ScenarioEngine:
    """
    Timeline-based stochastic simulation engine.

    You provide:
        - data: list of time-series data points
        - initial_state: dict with starting simulation state
        - step_fn(state, datapoint) -> state
        - failure_fn(state) -> bool
        - years_distribution() -> int
    """

    def __init__(
        self,
        data: List[Any],
        initial_state: Dict[str, Any],
        step_fn: Callable[[Dict[str, Any], Any], Dict[str, Any]],
        failure_fn: Callable[[Dict[str, Any]], bool],
        years_distribution: Callable[[], int],
        wraparound: bool = True,
    ):
        self.data = data
        self.initial_state = initial_state
        self.step_fn = step_fn
        self.failure_fn = failure_fn
        self.years_distribution = years_distribution
        self.wraparound = wraparound

    # ----------------------------------------------------------------------

    def _sample_window(self, duration: int) -> List[Any]:
        """Pick a random continuous segment of the data."""
        start = random.randrange(0, len(self.data))
        window = []

        for i in range(duration):
            idx = (start + i) % len(self.data) if self.wraparound else start + i
            if idx >= len(self.data):
                break
            window.append(self.data[idx])

        return window

    # ----------------------------------------------------------------------

    def run(self, num_cases: int = 10_000) -> Tuple[List[Dict[str, Any]], int]:
        """
        Run N scenarios and return:
            - list of final states
            - number of failures
        """
        outcomes = []
        failures = 0

        for _ in range(num_cases):
            state = self.initial_state.copy()
            duration = self.years_distribution()
            window = self._sample_window(duration)

            failed = False
            for datapoint in window:
                state = self.step_fn(state, datapoint)
                if self.failure_fn(state):
                    failed = True
                    break

            outcomes.append(state)
            if failed:
                failures += 1

        return outcomes, failures
