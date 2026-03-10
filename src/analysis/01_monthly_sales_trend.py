import matplotlib.pyplot as plt
from utils import load_data, set_plot_style, OUTPUT_DIR


def main():
    df = load_data()
    set_plot_style()

    # create year-month column
    df["YearMonth"] = df["InvoiceDate"].dt.to_period("M").astype(str)

    monthly_sales = (
        df.groupby("YearMonth")["TotalPrice"]
        .sum()
        .reset_index()
    )

    plt.figure()
    plt.plot(monthly_sales["YearMonth"], monthly_sales["TotalPrice"], marker="o")
    plt.title("Monthly Sales Trend (2009-2011)")
    plt.xlabel("Month")
    plt.ylabel("Revenue")
    plt.xticks(rotation=45)
    plt.tight_layout()

    output_path = OUTPUT_DIR / "01_monthly_sales_trend.png"
    plt.savefig(output_path, bbox_inches="tight")
    plt.show()

    print(f"Saved to: {output_path}")


if __name__ == "__main__":
    main()