"""Main entry point for the FCF Google Sheets model."""

from src.fcf.calculation import compute_fcf, FCFInputs


def main() -> None:
    inputs = FCFInputs(
        operating_cash_flow=1000000.0,
        capital_expenditures=200000.0,
        depreciation=50000.0,
        tax_rate=0.25,
    )
    results = compute_fcf(inputs)
    print(f"FCFF: {results.fcff}")
    print(f"FCFE: {results.fcfe}")


if __name__ == "__main__":
    main()