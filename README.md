# US30 Trading Analytics & Performance Pipeline

An end-to-end data engineering solution that models US30 trade executions in MySQL and automatically extracts, formats, and renders portfolio performance curves using Python.

<p align="center">
  <img src="https://raw.githubusercontent.com/folamiawwal11-dev/US30-Trading-Analytics-Pipeline/main/equity_curve.png" alt="US30 Cumulative Equity Curve" width="100%"/>
</p>

## Key Performance Metrics
- **Total Trades:** 24 Executed Trades
- **Cumulative ROI:** **+18.5R** Net Return
- **Pipeline:** Automated MySQL -> Python Pandas/Seaborn -> 300-DPI Visual Export

## Project Files
- `US30_Portfolio_Case_Study.pdf` - Full technical case study report.
- `plot_equity.py` - Python script for SQL querying and visualization generation.
- `equity_curve.png` - Automated visual performance curve output.

## System Architecture
1. **MySQL Database (`trading_analytics`):** Stores raw trade execution logs and executes server-side aggregation views (`vw_running_equity_curve`, `vw_setup_tier_performance`).
2. **Python Engine:** Authenticates database connection via `mysql-connector-python`, executes queries into `pandas` DataFrames, and renders dark-themed annotated equity curves using `seaborn` & `matplotlib`.
