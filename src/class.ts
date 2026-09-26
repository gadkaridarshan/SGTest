"""Free Cash Flow calculation engine."""

from dataclasses import dataclass


@dataclass
class FCFInputs:
    """Input parameters for FCF calculation."""
    operating_cash_flow: float
    capital_expenditures: float
    depreciation: float
    tax_rate: float = 0.25


@dataclass
class FCFResults:
    """Results from FCF calculation."""
    operating_cash_flow: float
    capital_expenditures: float
    depreciation: float
    tax_rate: float
    net_borrowing: float = 0.0

    @property
    def fcff(self) -> float:
        """Free Cash Flow to Firm: OCF - CapEx + Depreciation * (1 - Tax Rate)."""
        return self.operating_cash_flow - self.capital_expenditures + self.depreciation * (1 - self.tax_rate)

    @property
    def fcfe(self) -> float:
        """Free Cash Flow to Equity: OCF - CapEx + Depreciation * (1 - Tax Rate) - Net Borrowing."""
        return self.operating_cash_flow - self.capital_expenditures + self.depreciation * (1 - self.tax_rate) - self.net_borrowing


def compute_fcf(inputs: FCFInputs, net_borrowing: float = 0.0) -> FCFResults:
    """Compute FCF from input parameters.

    Args:
        inputs: FCF input parameters including operating cash flow,
                capital expenditures, depreciation, and tax rate.
        net_borrowing: Net borrowing amount for FCFE calculation.

    Returns:
        FCFResults containing FCFF and FCFE values.
    """
    return FCFResults(
        operating_cash_flow=inputs.operating_cash_flow,
        capital_expenditures=inputs.capital_expenditures,
        depreciation=inputs.depreciation,
        tax_rate=inputs.tax_rate,
        net_borrowing=net_borrowing,
    )