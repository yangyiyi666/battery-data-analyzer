from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
from battery_analysis import calculate_average_capacity,find_hottest_experiment

#导入csv并读取数据
import csv
experiments=[]
with open(BASE_DIR/"battery_data.csv","r",encoding="utf-8") as file:
    reader=csv.DictReader(file)
    for row in reader:
        experiment={
            "temperature":int(row["temperature"]),
            "voltage":float(row["voltage"]),
            "capacity":int(row["capacity"])
        }
        experiments.append(experiment)
    
#计算平均容量和寻找最高实验温度
average_capacity=calculate_average_capacity(experiments)
hottest_experiment=find_hottest_experiment(experiments)

#打印分析结果
print("实验数据：",experiments)
print("平均容量：",average_capacity)
print("最高温度实验：",hottest_experiment)