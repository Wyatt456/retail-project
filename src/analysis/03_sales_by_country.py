import matplotlib.pyplot as plt
import seaborn as sns
from utils import load_data, set_plot_style, OUTPUT_DIR


def main():
    df = load_data()
    set_plot_style()

    country_sales = (
        df.groupby("Country")["TotalPrice"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    plt.figure(figsize=(12, 6))
    sns.barplot(x=country_sales.index, y=country_sales.values)
    plt.title("Top 10 Countries by Revenue")
    plt.xlabel("Country")
    plt.ylabel("Revenue")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    output_path = OUTPUT_DIR / "03_sales_by_country.png"
    plt.savefig(output_path, bbox_inches="tight")
    plt.show()

    print(f"Saved to: {output_path}")


if __name__ == "__main__":
    main()