"""Depreciation calculation module for FCF model."""

from enum import Enum
from typing import List

class DepreciationMethod(Enum):
    """Supported depreciation methods."""
    STRAIGHT_LINE = "straight_line"
    DECLINING_BALANCE = "declining_balance"
    SUM_OF_YEARS = "sum_of_years"

def calculate_depreciation(
    asset_value: float,
    useful_life: int,
    method: DepreciationMethod = DepreciationMethod.STRAIGHT_LINE,
    salvage_value: float = 0.0,
) -> List[float]:
    """Calculate depreciation amounts for each period.

    Args:
        asset_value: Initial value of the asset.
        useful_life: Useful life in years.
        method: Depreciation method to use.
        salvage_value: Residual value at end of useful life.

    Returns:
        List of depreciation amounts per period.
    """
    if useful_life <= 0:
        raise ValueError("Useful life must be greater than zero.")
    if asset_value < salvage_value:
        raise ValueError("Asset value cannot be less than salvage value.")

    if method == DepreciationMethod.STRAIGHT_LINE:
        annual_depreciation = (asset_value - salvage_value) / useful_life
        return [annual_depreciation] * useful_life

    elif method == DepreciationMethod.DECLINING_BALANCE:
        rate = 2.0 / useful_life
        depreciation_schedule = []
        book_value = asset_value
        for _ in range(useful_life):
            depreciation = book_value * rate
            depreciation = min(depreciation, book_value - salvage_value)
            depreciation_schedule.append(depreciation)
            book_value -= depreciation
        return depreciation_schedule

    elif method == DepreciationMethod.SUM_OF_YEARS:
        sum_of_years = sum(range(1, useful_life + 1))
        depreciation_schedule = []
        for year in range(1, useful_life + 1):
            fraction = (useful_life - year + 1) / sum_of_years
            depreciation = (asset_value - salvage_value) * fraction
            depreciation_schedule.append(depreciation)
        return depreciation_schedule

    raise ValueError(f"Unsupported depreciation method: {method}")