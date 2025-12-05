"""
E-commerce Customer Retention Analysis – 2024

Author email (for verification): 23f2001336@ds.study.iitm.ac.in

This script:
- Loads quarterly customer retention data for 2024
- Computes the average retention rate
- Compares performance to the industry target (85)
- Produces visualizations:
    - Line chart of quarterly retention trend
    - Horizontal line for industry benchmark
- Prints key metrics to the console
"""

import matplotlib.pyplot as plt
import pandas as pd


def load_data() -> pd.DataFrame:
    data = {
        "quarter": ["Q1", "Q2", "Q3", "Q4"],
        "retention_rate": [70.65, 70.47, 70.68, 75.70],
    }
    return pd.DataFrame(data)


def compute_metrics(df: pd.DataFrame, industry_target: float = 85.0) -> dict:
    avg_retention = df["retention_rate"].mean()
    gap = industry_target - avg_retention
    return {
        "average_retention": avg_retention,
        "industry_target": industry_target,
        "gap_to_target": gap,
    }


def plot_retention(df: pd.DataFrame, metrics: dict, output_path: str = "retention_trend.png") -> None:
    plt.figure(figsize=(8, 5))
    plt.plot(df["quarter"], df["retention_rate"], marker="o", label="Customer Retention Rate (2024)")
    plt.axhline(y=metrics["industry_target"], linestyle="--", label="Industry Target (85)")
    plt.axhline(y=metrics["average_retention"], linestyle=":", label=f"2024 Average ({metrics['average_retention']:.2f})")
    plt.title("Customer Retention Rate – 2024 vs Industry Benchmark")
    plt.xlabel("Quarter")
    plt.ylabel("Retention Rate")
    plt.ylim(60, 90)
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_path, dpi=120)
    plt.close()


def main():
    df = load_data()
    metrics = compute_metrics(df)
    print("Average 2024 retention rate:", round(metrics["average_retention"], 2))
    print("Industry target:", metrics["industry_target"])
    print("Gap to target:", round(metrics["gap_to_target"], 2))
    plot_retention(df, metrics)


if __name__ == "__main__":
    main()
