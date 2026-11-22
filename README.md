# Battery Data Analyzer

**基于 Python 的锂电池实验数据分析工具**

## 1. 项目简介

Battery Data Analyzer 是一个面向锂离子电池科研实验数据的轻量级分析工具，支持读取 CSV 和 JSON 格式的实验数据，并完成基础数据统计与分析。

本项目结合材料科学与锂离子电池研究背景，尝试将科研实验数据处理流程进行程序化和模块化。

## 2. 核心功能

- CSV 实验数据读取与解析
- JSON 实验数据读取与解析
- 多组实验平均容量计算
- 最高温度实验记录识别
- JSON 格式分析结果输出
- 模块化函数设计

## 3. 技术栈

- Python 3.12
- pathlib
- csv
- json
- 函数与模块化编程
- Git / GitHub

项目目前使用 Python 标准库，无需安装额外第三方依赖。

## 4. 项目结构

```text
battery-data-analyzer/
│
├── battery_analysis.py   # 核心数据分析函数
├── main.py               # CSV数据分析入口
├── json_main.py          # JSON数据分析入口
│
├── battery_data.csv      # CSV实验数据
├── battery_data.json    # JSON实验数据
├── analysis_result.json  # JSON分析结果
│
├── .gitignore
├── data.txt
└── result.txt
```

## 5. 运行方法

确保已安装 Python 3.12。

运行 CSV 数据分析：

```bash
python main.py
```

运行 JSON 数据分析：

```bash
python json_main.py
```

## 6. 示例分析结果

基于当前示例实验数据：

- 实验组数：4
- 平均容量：2450 mAh
- 最高实验温度：45 ℃
- 对应实验电压：3.9 V
- 对应实验容量：2300 mAh

## 7. 项目学习目标

本项目是 Python 编程学习阶段的实践作品，主要用于训练科研数据读取、处理、统计分析、文件操作及软件工程基础能力。

后续计划逐步增加数据可视化、异常数据识别、自动化实验分析及 AI 辅助科研功能。
