"""Free Cash Flow calculation engine."""

from dataclasses import dataclass
from typing import Optional

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
    fcff: float
    fcfe: float
    operating_cash_flow: float
    capital_expenditures: float
    depreciation: float

    @property
    def fcff(self) -> float:
        """Free Cash Flow to Firm: OCF - CapEx + Depreciation * (1 - Tax Rate)."""
        return self.operating_cash_flow - self.capital_expenditures + self.depreciation * (1 - self.tax_rate)

    @property
    def fcfe(self) -> float:
        """Free Cash Flow to Equity: OCF - CapEx + Depreciation * (1 - Tax Rate) - Net Borrowing."""
        return self.operating_cash_flow - self.capital_expenditures + self.depreciation * (1 - self.tax_rate)