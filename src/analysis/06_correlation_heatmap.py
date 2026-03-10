import matplotlib.pyplot as plt
import seaborn as sns
from utils import load_data, set_plot_style, OUTPUT_DIR


def main():
    df = load_data()
    set_plot_style()

    customer_features = (
        df.groupby("Customer ID")
        .agg(
            TotalQuantity=("Quantity", "sum"),
            AvgPrice=("Price", "mean"),
            TotalRevenue=("TotalPrice", "sum"),
            NumOrders=("Invoice", "nunique"),
            NumProducts=("StockCode", "nunique"),
        )
    )

    corr_matrix = customer_features.corr()

    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap="Blues", fmt=".2f", square=True)
    plt.title("Correlation Heatmap of Customer-Level Features")
    plt.tight_layout()

    output_path = OUTPUT_DIR / "06_correlation_heatmap.png"
    plt.savefig(output_path, bbox_inches="tight")
    plt.show()

    print(f"Saved to: {output_path}")


if __name__ == "__main__":
    main()