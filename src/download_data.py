from pathlib import Path
import kagglehub
import shutil

# project root
ROOT = Path(__file__).resolve().parent.parent #__file__是 Python 自动提供的变量，表示：当前脚本的路径 resolve()方法将路径转换为绝对路径 parent.parent表示上两级目录，也就是项目根目录

# data folder
destination = ROOT / "data" / "raw"

destination.mkdir(parents=True, exist_ok=True) #如果父目录不存在则创建父目录，如果目标文件已经存在则不报异常

# download dataset
path = Path(kagglehub.dataset_download("nankisinghsohi/online-retail-ii-dataset"))
#类型转化为Path对象，方便后续操作
print("Downloaded to:", path)

for file in path.iterdir(): #遍历下载的文件夹中的所有文件
    shutil.copy(file, destination) #shutil.copy()函数用于复制文件，第一个参数是源文件路径，第二个参数是目标文件路径，这里我们把下载的文件复制到data/raw目录下

print("Dataset copied to:", destination)