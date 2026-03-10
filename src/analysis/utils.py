from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# project root directory
BASE_DIR = Path(__file__).resolve().parents[2]

DATA_PATH = BASE_DIR / "data" / "cleaned" / "retail_clean.csv"
OUTPUT_DIR = BASE_DIR / "outputs" / "figures"


def load_data() -> pd.DataFrame:
    df = pd.read_csv(DATA_PATH, parse_dates=["InvoiceDate"])

    # ensure output folder exists
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # clean column names if needed
    df.columns = [col.strip() for col in df.columns]

    return df


def set_plot_style() -> None:
    sns.set_theme(style="whitegrid")
    plt.rcParams["figure.figsize"] = (12, 6)
    plt.rcParams["axes.titlesize"] = 14
    plt.rcParams["axes.labelsize"] = 12
    plt.rcParams["xtick.labelsize"] = 10
    plt.rcParams["ytick.labelsize"] = 10
    plt.rcParams["figure.dpi"] = 120