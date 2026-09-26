"""FCF Model computation engine.

Provides the core free cash flow calculation logic with adjustable
depreciation inputs for scenario modeling.

# @helix:story [USER-98000]
"""

from dataclasses import dataclass


@dataclass
class FCFInputs:
    """Input parameters for FCF calculation.

    Attributes:
        operating_cash_flow: Operating cash flow (OCF) for the period.
        capital_expenditures: Capital expenditures (CapEx) for the period.
        depreciation: Depreciation expense for the period.
        tax_rate: Effective tax rate (default 0.25).
    """

    operating_cash_flow: float
    capital_expenditures: float
    depreciation: float
    tax_rate: float = 0.25


@dataclass
class FCFResults:
    """Results from FCF calculation.

    Attributes:
        operating_cash_flow: Operating cash flow.
        capital_expenditures: Capital expenditures.
        depreciation: Depreciation expense.
        tax_rate: Effective tax rate.
        net_borrowing: Net borrowing amount for FCFE calculation.
    """

    operating_cash_flow: float
    capital_expenditures: float
    depreciation: float
    tax_rate: float
    net_borrowing: float = 0.0

    @property
    def fcff(self) -> float:
        """Free Cash Flow to Firm: OCF - CapEx + Depreciation * (1 - Tax Rate).

        Returns:
            FCFF value reflecting cash available to all capital providers.
        """
        return self.operating_cash_flow - self.capital_expenditures + self.depreciation * (1 - self.tax_rate)

    @property
    def fcfe(self) -> float:
        """Free Cash Flow to Equity: OCF - CapEx + Depreciation * (1 - Tax Rate) - Net Borrowing.

        Returns:
            FCFE value reflecting cash available to equity holders.
        """
        return self.operating_cash_flow - self.capital_expenditures + self.depreciation * (1 - self.tax_rate) - self.net_borrowing


def compute_fcf(inputs: FCFInputs, net_borrowing: float = 0.0) -> FCFResults:
    """Compute FCF from input parameters.

    Args:
        inputs: FCF input parameters including operating cash flow,
                capital expenditures, depreciation, and tax rate.
        net_borrowing: Net borrowing amount for FCFE calculation.

    Returns:
        FCFResults containing FCFF and FCFE values.

    Example:
        >>> inputs = FCFInputs(1000, 200, 50, 0.3)
        >>> results = compute_fcf(inputs)
        >>> results.fcff
        885.0
    """
    return FCFResults(
        operating_cash_flow=inputs.operating_cash_flow,
        capital_expenditures=inputs.capital_expenditures,
        depreciation=inputs.depreciation,
        tax_rate=inputs.tax_rate,
        net_borrowing=net_borrowing,
    )