from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# project root directory
BASE_DIR = Path(__file__).resolve().parents[2] #resolve()获取绝对路径 parents[2]获取上两级目录

DATA_PATH = BASE_DIR / "data" / "cleaned" / "retail_clean.csv" #数据路径 BASE_DIR/data/cleaned/retail_clean.csv
OUTPUT_DIR = BASE_DIR / "outputs" / "figures" #输出路径 BASE_DIR/outputs/figures


def load_data() -> pd.DataFrame: #->只是一个提示符而已，告诉调用者这个函数应该返回一个DataFrame对象
    df = pd.read_csv(DATA_PATH, parse_dates=["InvoiceDate"])#因为我们之前把xlsx文件转换成了csv（不记录文本格式），所以这里用pd.read_csv来读取数据，并且指定parse_dates参数来解析InvoiceDate列为日期格式

    # ensure output folder exists
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # clean column names if needed
    df.columns = df.columns.str.strip() #去掉列名的空格，防止后续操作中因为列名有空格而导致错误
    return df


def set_plot_style() -> None:
    sns.set_theme(style="whitegrid") #设置seaborn的主题为白色网格，这样图表看起来更清晰
    plt.rcParams["figure.figsize"] = (12, 6) #图表大小 = 12 × 6 英寸
    plt.rcParams["axes.titlesize"] = 14 #标题大小
    plt.rcParams["axes.labelsize"] = 12 #坐标轴标签大小
    plt.rcParams["xtick.labelsize"] = 10 #x轴刻度标签大小
    plt.rcParams["ytick.labelsize"] = 10 #y轴刻度标签大小
    plt.rcParams["figure.dpi"] = 120 #图表分辨率