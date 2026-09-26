from setuptools import setup, find_packages

setup(
    name="sgtest-fcf",
    version="0.1.0",
    description="FCF Google Sheets model",
    packages=find_packages(where=["src"]),
    package_dir={"": "src"},
    python_requires=">=3.9",
    install_requires=[
        "gspread>=5.7.0",
        "google-auth>=2.15.0",
        "google-auth-oauthlib>=1.0.0",
        "pandas>=2.0.0",
        "numpy>=1.24.0",
        "openpyxl>=3.1.0",
    ],
)