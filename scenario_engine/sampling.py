import random

def triangular_years(min_years: int, max_years: int, mode_years: int) -> int:
    return int(random.triangular(min_years, max_years, mode_years))

def uniform_years(min_years: int, max_years: int) -> int:
    return random.randint(min_years, max_years)

def fixed_years(years: int) -> int:
    return years
