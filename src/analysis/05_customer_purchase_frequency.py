import matplotlib.pyplot as plt
import seaborn as sns
from utils import load_data, set_plot_style, OUTPUT_DIR


def main():
    df = load_data()
    set_plot_style()

    purchase_frequency = (
        df.groupby("Customer ID")["Invoice"]
        .nunique()
    )

    plt.figure(figsize=(12, 6))
    sns.histplot(purchase_frequency, bins=40, kde=True)
    plt.title("Customer Purchase Frequency Distribution")
    plt.xscale("log")
    plt.xlabel("Number of Orders per Customer (log scale)")
    plt.ylabel("Frequency")
    plt.tight_layout()

    output_path = OUTPUT_DIR / "05_customer_purchase_frequency.png"
    plt.savefig(output_path, bbox_inches="tight")
    plt.show()

    print(f"Saved to: {output_path}")


if __name__ == "__main__":
    main()