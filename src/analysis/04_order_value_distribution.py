import matplotlib.pyplot as plt
import seaborn as sns
from utils import load_data, set_plot_style, OUTPUT_DIR


def main():
    df = load_data()
    set_plot_style()

    order_values = (
        df.groupby("Invoice")["TotalPrice"]
        .sum()
    )

    plt.figure(figsize=(12, 6))
    sns.histplot(order_values, bins=50, kde=True)
    plt.title("Order Value Distribution")
    plt.xscale("log")
    plt.xlabel("Order Value (log scale)")
    plt.ylabel("Frequency")
    plt.tight_layout()

    output_path = OUTPUT_DIR / "04_order_value_distribution.png"
    plt.savefig(output_path, bbox_inches="tight")
    plt.show()

    print(f"Saved to: {output_path}")


if __name__ == "__main__":
    main()