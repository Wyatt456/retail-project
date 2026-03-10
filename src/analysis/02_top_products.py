import matplotlib.pyplot as plt
import seaborn as sns
from utils import load_data, set_plot_style, OUTPUT_DIR


def main():
    df = load_data()
    set_plot_style()

    top_products = (
        df.groupby("Description")["TotalPrice"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .sort_values(ascending=True)
    )

    plt.figure(figsize=(12, 7))
    sns.barplot(x=top_products.values, y=top_products.index)
    plt.title("Top 10 Products by Revenue")
    plt.xlabel("Revenue")
    plt.ylabel("Product")
    plt.tight_layout()

    output_path = OUTPUT_DIR / "02_top_products.png"
    plt.savefig(output_path, bbox_inches="tight")
    plt.show()

    print(f"Saved to: {output_path}")


if __name__ == "__main__":
    main()