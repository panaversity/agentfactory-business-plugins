"""
Generate a bar chart of monthly revenue from a CSV file.

Expected CSV format:
  - A date column (parsed automatically) OR a 'month' column
  - A 'revenue' column (numeric)

Usage:
  python monthly_revenue_chart.py data.csv
  python monthly_revenue_chart.py data.csv --output chart.png
  python monthly_revenue_chart.py data.csv --date-col transaction_date --revenue-col amount
"""

import argparse
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import pandas as pd


def load_and_aggregate(
    csv_path: str,
    date_col: str | None = None,
    revenue_col: str = "revenue",
) -> pd.DataFrame:
    """Load a CSV and return a DataFrame with monthly revenue totals."""
    df = pd.read_csv(csv_path)

    # Normalise column names to lowercase for easier matching
    df.columns = df.columns.str.strip().str.lower()
    revenue_col = revenue_col.lower()

    if revenue_col not in df.columns:
        sys.exit(f"Error: column '{revenue_col}' not found. Columns: {list(df.columns)}")

    # Determine the date column
    if date_col:
        date_col = date_col.lower()
    else:
        # Auto-detect: look for 'date', 'month', or first datetime-parseable column
        for candidate in ["date", "month", "transaction_date", "order_date"]:
            if candidate in df.columns:
                date_col = candidate
                break
        if date_col is None:
            sys.exit(
                "Error: no date column found. "
                "Use --date-col to specify one."
            )

    df[date_col] = pd.to_datetime(df[date_col], infer_datetime_format=True)
    df["year_month"] = df[date_col].dt.to_period("M")

    monthly = (
        df.groupby("year_month")[revenue_col]
        .sum()
        .sort_index()
        .reset_index()
    )
    monthly.columns = ["month", "revenue"]
    return monthly


def plot_chart(monthly: pd.DataFrame, output_path: str | None = None) -> None:
    """Render a bar chart of monthly revenue."""
    fig, ax = plt.subplots(figsize=(12, 6))

    labels = monthly["month"].astype(str)
    values = monthly["revenue"]

    bars = ax.bar(labels, values, color="#4A90D9", edgecolor="white", width=0.7)

    # Annotate bars with values
    for bar, val in zip(bars, values):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height(),
            f"${val:,.0f}",
            ha="center",
            va="bottom",
            fontsize=8,
            fontweight="bold",
        )

    ax.set_xlabel("Month", fontsize=12)
    ax.set_ylabel("Revenue ($)", fontsize=12)
    ax.set_title("Monthly Revenue", fontsize=14, fontweight="bold")
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x:,.0f}"))

    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    if output_path:
        fig.savefig(output_path, dpi=150)
        print(f"Chart saved to {output_path}")
    else:
        plt.show()


def main() -> None:
    parser = argparse.ArgumentParser(description="Bar chart of monthly revenue from CSV")
    parser.add_argument("csv", help="Path to the input CSV file")
    parser.add_argument("--output", "-o", help="Save chart to file (e.g. chart.png)")
    parser.add_argument("--date-col", help="Name of the date column (auto-detected if omitted)")
    parser.add_argument("--revenue-col", default="revenue", help="Name of the revenue column (default: revenue)")
    args = parser.parse_args()

    if not Path(args.csv).exists():
        sys.exit(f"Error: file not found: {args.csv}")

    monthly = load_and_aggregate(args.csv, args.date_col, args.revenue_col)
    print(monthly.to_string(index=False))
    plot_chart(monthly, args.output)


if __name__ == "__main__":
    main()
