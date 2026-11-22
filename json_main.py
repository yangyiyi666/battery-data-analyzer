from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
from battery_analysis import calculate_average_capacity,find_hottest_experiment
import json
with open(BASE_DIR/"battery_data.json","r",encoding="utf-8") as file:
    data=json.load(file)
experiments=data["experiments"]
average_capacity=calculate_average_capacity(experiments)
hottest_experiment=find_hottest_experiment(experiments)
analysis_result = {
   "project": data["project"],
    "average_capacity": average_capacity,
    "hottest_experiment": hottest_experiment,
    "status": "completed"
}
with open(BASE_DIR/"analysis_result.json","w",encoding="utf-8") as file:
    json.dump(analysis_result,file,ensure_ascii=False,indent=4)