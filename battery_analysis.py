#1.计算平均容量
def calculate_average_capacity(experiments):
    if not experiments:
        return None
    return sum(experiment["capacity"] for experiment in experiments)/len(experiments)

#2.返回温度最高的实验字典
def find_hottest_experiment(experiments):
    if not experiments:
        return None
    hottest_experiment=experiments[0]
    for experiment in experiments:
        if experiment["temperature"]>hottest_experiment["temperature"]:
            hottest_experiment=experiment
    return hottest_experiment
