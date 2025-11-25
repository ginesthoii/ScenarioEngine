from typing import List, Dict, Any

def summarize(outcomes: List[Dict[str, Any]], failures: int):
    total = len(outcomes)
    failure_rate = failures / total

    return {
        "total_runs": total,
        "failures": failures,
        "failure_rate": failure_rate,
        "success_rate": 1 - failure_rate,
        "min_state": min(outcomes, key=lambda x: list(x.values())[0]),
        "max_state": max(outcomes, key=lambda x: list(x.values())[0]),
        "avg_state": sum(list(o.values())[0] for o in outcomes) / total
    }
