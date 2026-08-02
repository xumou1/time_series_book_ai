# examples · 《时间序列分析》示例项目

本书配套的可运行示例项目，用 **uv** 管理环境。所有数据与插图都与书中章节一一对应：**书里能查到的数字，脚本里能跑出来。**

## 快速开始

```bash
# 安装依赖（首次会自动创建 .venv 并安装 matplotlib/pandas/numpy/statsmodels）
uv sync

# 1) 生成示例数据（输出到 data/）
uv run python scripts/make_data.py

# 2) 生成书中插图（输出到 ../book/figures/）
uv run python scripts/make_figures.py
```

> 若 `uv` 不在 PATH（如本机只有 CherryStudio 自带的 uv）：`export UV="$HOME/.cherrystudio/bin/uv.exe"`，用 `"$UV" sync` / `"$UV" run ...` 替代。

## 项目结构

```
examples/
├── pyproject.toml          # uv 项目配置（依赖与 Python 版本）
├── data/                   # 生成的示例数据（CSV）
│   ├── scenic_tourists.csv    # 景区 24 个月游客量（第 2、8 章）
│   ├── tea_shop_sales.csv     # 奶茶店 3 年日销售额（第 20 章案例）
│   └── simulated_series.csv   # 白噪声/随机游走/趋势/GARCH 模拟（第 3、4、10 章）
└── scripts/
    ├── make_data.py        # 数据生成（固定随机种子，结果可复现）
    └── make_figures.py     # 插图生成（输出到 book/figures/）
```

## 插图与章节对照

| 图 | 章节 | 内容 |
|---|---|---|
| fig01-ts-vs-cross.png | 第 1 章 1.3 | 横截面 vs 时间序列 |
| fig02-decomposition.png | 第 2 章 2.4 | 景区数据 STL 分解 |
| fig04-stationarity.png | 第 4 章 4.4 | 平稳/趋势/随机游走对比 |
| fig04-acf.png | 第 4 章 4.5 | ACF：平稳 vs 随机游走 |
| fig05-spectrum.png | 第 5 章 5.4 | 12 个月周期的时域图与周期图 |
| fig06-smoothing.png | 第 6 章 6.4 | 指数平滑 α=0.3 vs 0.9 |
| fig08-differencing.png | 第 8 章 8.3 | 原始序列 vs 一阶差分 |
| fig10-garch.png | 第 10 章 10.4 | GARCH 波动聚集与条件方差 |
| fig15-attention.png | 第 15 章 15.2 | 注意力权重与加权求和 |

## 扩展建议

- **跑真实数据**：把 `make_data.py` 换成你手边的 CSV，其余脚本思路不变；
- **复现书中练习**：第 8 章 `auto_arima`、第 15 章 TSLib 对比等可在本环境中加依赖后运行；
- **重新生成**：改任何图后重跑 `uv run python scripts/make_figures.py`，再重导全书（见 `book/_export_book.py`）。
