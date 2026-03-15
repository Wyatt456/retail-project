from pathlib import Path
import pandas as pd
from scipy.stats import pearsonr, f_oneway, ttest_ind

from utils import load_data

# project root directory
BASE_DIR = Path(__file__).resolve().parents[2]

# output path
OUTPUT_DIR = BASE_DIR / "outputs" / "figures"
RESULT_PATH = OUTPUT_DIR / "07_statistical_test_results.csv"


def quantity_revenue_correlation(df: pd.DataFrame) -> dict:
    """
    Pearson correlation test between Quantity and TotalPrice
    """
    corr, p_value = pearsonr(df["Quantity"], df["TotalPrice"])

    return {
        "test": "Pearson Correlation",
        "question": "Is there a correlation between quantity and revenue?",
        "statistic_name": "correlation_coefficient",
        "statistic": corr,
        "p_value": p_value,
        "significant_at_0_05": p_value < 0.05,
        "interpretation": (
            "There is a statistically significant correlation between quantity and revenue."
            if p_value < 0.05
            else "There is no statistically significant correlation between quantity and revenue."
        ),
    }


def country_order_value_anova(df: pd.DataFrame) -> dict:
    """
    ANOVA test for average order value across top countries
    Order value = sum of TotalPrice within each Invoice
    """
    order_value = (
        df.groupby(["Invoice", "Country"], as_index=False)["TotalPrice"]
        .sum()
        .rename(columns={"TotalPrice": "OrderValue"})
    )

    top_countries = (
        order_value.groupby("Country")["OrderValue"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
        .index
        .tolist()
    )

    groups = [
        order_value.loc[order_value["Country"] == country, "OrderValue"]
        for country in top_countries
    ]

    f_stat, p_value = f_oneway(*groups)

    return {
        "test": "ANOVA",
        "question": "Does average order value differ across countries?",
        "statistic_name": "F_statistic",
        "statistic": f_stat,
        "p_value": p_value,
        "significant_at_0_05": p_value < 0.05,
        "interpretation": (
            f"There is a statistically significant difference in average order value across the tested countries: {', '.join(top_countries)}."
            if p_value < 0.05
            else f"There is no statistically significant difference in average order value across the tested countries: {', '.join(top_countries)}."
        ),
    }


def frequent_vs_infrequent_ttest(df: pd.DataFrame) -> dict:
    """
    Independent sample t-test:
    frequent customers vs infrequent customers in total revenue

    Frequent customers are defined as customers whose purchase frequency
    is above the median purchase frequency.
    """
    customer_stats = (
        df.groupby("Customer ID", as_index=False)
        .agg(
            PurchaseFrequency=("Invoice", "nunique"),
            TotalRevenue=("TotalPrice", "sum")
        )
    )

    median_freq = customer_stats["PurchaseFrequency"].median()

    frequent = customer_stats.loc[
        customer_stats["PurchaseFrequency"] > median_freq, "TotalRevenue"
    ]

    infrequent = customer_stats.loc[
        customer_stats["PurchaseFrequency"] <= median_freq, "TotalRevenue"
    ]

    t_stat, p_value = ttest_ind(frequent, infrequent, equal_var=False)

    return {
        "test": "Independent Sample t-test",
        "question": "Do frequent customers generate more revenue than infrequent customers?",
        "statistic_name": "t_statistic",
        "statistic": t_stat,
        "p_value": p_value,
        "significant_at_0_05": p_value < 0.05,
        "interpretation": (
            "Frequent customers generate statistically significantly different revenue from infrequent customers."
            if p_value < 0.05
            else "There is no statistically significant revenue difference between frequent and infrequent customers."
        ),
    }


def print_result(result: dict) -> None:
    print("\n" + "=" * 70)
    print(f"Test: {result['test']}")
    print(f"Research Question: {result['question']}")
    print(f"{result['statistic_name']}: {result['statistic']:.6f}")
    print(f"p-value: {result['p_value']:.6f}")
    print(f"Significant at 0.05: {result['significant_at_0_05']}")
    print(f"Interpretation: {result['interpretation']}")


def main() -> None:
    df = load_data()

    results = [
        quantity_revenue_correlation(df),
        country_order_value_anova(df),
        frequent_vs_infrequent_ttest(df),
    ]

    for result in results:
        print_result(result)

    results_df = pd.DataFrame(results)
    results_df.to_csv(RESULT_PATH, index=False)

    print("\n" + "=" * 70)
    print(f"Results saved to: {RESULT_PATH}")


if __name__ == "__main__":
    main()