from pathlib import Path
import kagglehub
import shutil
import os

# project root
ROOT = Path(__file__).resolve().parent.parent

# data folder
destination = ROOT / "data" / "raw"

# download dataset
path = kagglehub.dataset_download("nankisinghsohi/online-retail-ii-dataset")

print("Downloaded to:", path)

os.makedirs(destination, exist_ok=True)

for file in os.listdir(path):
    shutil.copy(os.path.join(path, file), destination)

print("Dataset copied to:", destination)