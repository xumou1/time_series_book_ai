# -*- coding: utf-8 -*-
"""生成《时间序列分析》书籍配套的示例数据（CSV，保存到 data/）。

数据全部与书中示例数字一致（第 1/2/8/20 章等），保证"书里能查、脚本能跑"。
用法：uv run python scripts/make_data.py
"""
from pathlib import Path
import numpy as np
import pandas as pd

DATA = Path(__file__).resolve().parents[1] / "data"
DATA.mkdir(exist_ok=True)
rng = np.random.default_rng(42)  # 固定种子，结果可复现


def scenic_tourists() -> pd.DataFrame:
    """景区 24 个月游客量（第 2、8 章用到的数字）。"""
    vals = [
        3.0, 2.8, 3.5, 4.2, 5.0, 6.1, 7.2, 7.0, 5.8, 5.0, 4.0, 3.6,
        3.4, 3.2, 3.9, 4.6, 5.4, 6.5, 7.6, 7.4, 6.2, 5.4, 4.4, 4.0,
    ]
    idx = pd.date_range("2023-01-01", periods=24, freq="MS")
    return pd.DataFrame({"date": idx, "tourists_10k": vals})


def tea_shop_sales() -> pd.DataFrame:
    """奶茶店 3 年日销售额（第 20 章案例：趋势 + 周季节 + 节假日 + 促销 + 气温）。"""
    idx = pd.date_range("2022-01-01", periods=3 * 365, freq="D")
    n = len(idx)
    t = np.arange(n)
    # 基础：逐年上升约 5%/年 + 周季节（周末高 30%）+ 年度季节（夏季略高）
    trend = 800 * (1 + 0.05 * t / 365)
    weekly = 1 + 0.30 * ((idx.dayofweek >= 5).astype(float))
    seasonal = 1 + 0.12 * np.sin(2 * np.pi * (idx.dayofyear - 180) / 365)
    # 节假日（春节前后 7 天提升，国庆提升）
    holiday = np.ones(n)
    year = idx.year
    for y in year.unique():
        lunar = None  # 简化：用每年 2 月 1 日附近模拟春节
        spring = pd.Timestamp(f"{y}-02-01")
        for d in range(-3, 5):
            mask = (idx >= spring + pd.Timedelta(days=d)) & (idx < spring + pd.Timedelta(days=d + 1))
            holiday[mask] = 1.5
        nat = pd.Timestamp(f"{y}-10-01")
        for d in range(0, 7):
            mask = (idx >= nat + pd.Timedelta(days=d)) & (idx < nat + pd.Timedelta(days=d + 1))
            holiday[mask] = 1.35
    # 促销：随机 15% 的日子促销 +30%
    promo = 1 + 0.30 * (rng.random(n) < 0.15)
    # 气温（模拟，U 形影响：太冷太热都卖得少）
    temp = 15 + 12 * np.sin(2 * np.pi * (idx.dayofyear - 100) / 365) + rng.normal(0, 2, n)
    temp_effect = 1 + 0.08 * np.sin(np.pi * (temp - 5) / 20)  # 简化 U 形
    noise = 1 + rng.normal(0, 0.06, n)
    sales = trend * weekly * seasonal * holiday * promo * temp_effect * noise
    return pd.DataFrame({"date": idx, "sales": sales.round(0), "temp": temp.round(1),
                         "holiday": holiday, "promo": promo})


def simulated_series() -> pd.DataFrame:
    """模拟序列集（第 3/4/10 章）：白噪声、随机游走、GARCH 收益率。"""
    n = 500
    idx = pd.date_range("2020-01-01", periods=n, freq="D")
    white = rng.normal(0, 1, n)
    rw = np.cumsum(rng.normal(0, 1, n))
    trend = np.linspace(0, 10, n) + rng.normal(0, 1, n)
    # GARCH(1,1) 模拟：σ²_t = 0.05 + 0.15 ε²_{t-1} + 0.8 σ²_{t-1}
    sigma2 = np.zeros(n); sigma2[0] = 1.0
    garch = np.zeros(n)
    for i in range(1, n):
        garch[i] = rng.normal(0, np.sqrt(sigma2[i - 1]))
        sigma2[i] = 0.05 + 0.15 * garch[i - 1] ** 2 + 0.80 * sigma2[i - 1]
    return pd.DataFrame({"date": idx, "white_noise": white, "random_walk": rw,
                         "trend_series": trend, "garch_ret": garch, "garch_var": sigma2})


def main() -> None:
    scenic_tourists().to_csv(DATA / "scenic_tourists.csv", index=False)
    tea_shop_sales().to_csv(DATA / "tea_shop_sales.csv", index=False)
    simulated_series().to_csv(DATA / "simulated_series.csv", index=False)
    print("已生成:")
    for f in sorted(DATA.glob("*.csv")):
        print(f"  - {f.name} ({f.stat().st_size / 1024:.0f} KB)")


if __name__ == "__main__":
    main()
