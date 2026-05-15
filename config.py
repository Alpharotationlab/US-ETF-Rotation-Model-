# -*- coding: utf-8 -*-
"""Configuration for US ETF rotation simplified model."""

# ETF universe (基于你提供的列表，选择流动性较好、历史悠久的部分)
ETF_UNIVERSE = [
    'SPY',   # 标普500
    'QQQ',   # 纳斯达克100
    'SOXX',  # 半导体
    'IGV',   # 软件
    'QTUM',  # 量子计算
    'BOTZ',  # 机器人AI
    'CLOU',  # 云计算
    'XBI',   # 生物科技
    'XHB',   # 房屋建造
    'TAN',   # 太阳能
    'XLF',   # 金融
    'KBE',   # 银行
    'XLI',   # 工业
    'XLB',   # 材料
    'PAVE',  # 基建
    'ITA',   # 军工
    'XLE',   # 能源
    'COPX',  # 铜矿
    'REMX',  # 稀土
    'DBC',   # 大宗商品
]

# 策略参数（用户可在命令行或此处修改）
MOMENTUM_WINDOW = 20      # 动量计算窗口（交易日）
TOP_K = 3                  # 持有排名前K只ETF
MA_WINDOW = 200            # 均线过滤窗口
REBALANCE_FREQ = 5         # 调仓频率（每N个交易日）
TRANSACTION_COST = 0.001   # 单边交易成本（0.1%）

# 回测时间
START_DATE = '2019-01-01'
END_DATE = '2026-04-30'

# 基准（用于对比）
BENCHMARK = 'SPY'

# 是否输出图表
SAVE_CHART = True
CHART_PATH = 'output/equity_curve.png'