# -*- coding: utf-8 -*-
"""生成《时间序列分析》书籍插图（保存到 book/figures/）。

所有图都使用 examples/data/ 中的示例数据（与书中数字一致）。
用法：uv run python scripts/make_figures.py
"""
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

# 中文字体（Windows）
matplotlib.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "sans-serif"]
matplotlib.rcParams["axes.unicode_minus"] = False

ROOT = Path(__file__).resolve().parents[2]  # E:\Dropbox\TimeSeries
DATA = ROOT / "examples" / "data"
FIG = ROOT / "book" / "figures"
FIG.mkdir(exist_ok=True)


def load() -> dict:
    scenic = pd.read_csv(DATA / "scenic_tourists.csv", parse_dates=["date"])
    shop = pd.read_csv(DATA / "tea_shop_sales.csv", parse_dates=["date"])
    sim = pd.read_csv(DATA / "simulated_series.csv", parse_dates=["date"])
    return {"scenic": scenic, "shop": shop, "sim": sim}


def fig01_ts_vs_cross(d):
    """第 1 章：横截面数据 vs 时间序列。"""
    fig, axes = plt.subplots(1, 2, figsize=(10, 3.6))
    # 左：横截面（模拟 6 个省人口）
    provinces = ["北京", "上海", "广东", "四川", "新疆", "黑龙江"]
    pop = [21.9, 24.9, 12.7, 8.4, 2.6, 3.1]
    axes[0].bar(provinces, pop, color="#5b9bd5")
    axes[0].set_title("横截面数据：2024 年各省人口（亿）——顺序可任意排列", fontsize=11)
    axes[0].set_ylabel("人口（亿）")
    # 右：奶茶店 12 个月营业额（第 1.5 节的数字）
    x = np.arange(1, 13)
    y = [8.1, 6.2, 8.5, 9.0, 9.8, 11.2, 12.5, 12.8, 11.9, 12.2, 11.5, 13.6]
    axes[1].plot(x, y, marker="o", color="#c55a11")
    axes[1].set_xticks(x)
    axes[1].set_xlabel("月份")
    axes[1].set_title("时间序列：奶茶店 2024 年营业额（万元）——顺序不能打乱", fontsize=11)
    axes[1].set_ylabel("营业额（万元）")
    fig.tight_layout()
    fig.savefig(FIG / "fig01-ts-vs-cross.png", dpi=150)
    plt.close(fig)


def fig02_decomposition(d):
    """第 2 章：景区 24 个月 STL 分解（period=12）。"""
    from statsmodels.tsa.seasonal import STL
    s = d["scenic"]
    y = s["tourists_10k"].values
    res = STL(y, period=12, robust=True).fit()
    fig, axes = plt.subplots(4, 1, figsize=(9, 7), sharex=True)
    labels = ["原始序列（2023–2024 逐月）", "趋势分量 T(t)", "季节分量 S(t)", "残差分量 ε(t)"]
    for ax, comp, lab in zip(axes, [y, res.trend, res.seasonal, res.resid], labels):
        ax.plot(s["date"], comp, color="#2c5f8a", lw=1.5)
        ax.set_ylabel(lab, fontsize=9, rotation=0, ha="right", va="center")
    axes[0].set_title("景区游客量 STL 分解：趋势逐年上升 + 7 月高峰（季节）+ 随机残差", fontsize=11)
    axes[-1].set_xlabel("时间")
    fig.tight_layout()
    fig.savefig(FIG / "fig02-decomposition.png", dpi=150)
    plt.close(fig)


def fig04_stationarity(d):
    """第 4 章：平稳 / 趋势 / 随机游走 三种序列对比。"""
    sim = d["sim"]
    fig, axes = plt.subplots(3, 1, figsize=(9, 6.2), sharex=True)
    cases = [
        ("平稳：白噪声（均值 0、方差恒定）", "white_noise", "#2c5f8a"),
        ("非平稳：带上升趋势（均值漂移）", "trend_series", "#c55a11"),
        ("非平稳：随机游走（冲击永不消退）", "random_walk", "#7f7f7f"),
    ]
    for ax, (title, col, color) in zip(axes, cases):
        ax.plot(sim["date"], sim[col], color=color, lw=0.9)
        ax.set_title(title, fontsize=10, loc="left")
    fig.tight_layout()
    fig.savefig(FIG / "fig04-stationarity.png", dpi=150)
    plt.close(fig)


def fig04_acf(d):
    """第 4 章：ACF 对比——平稳短序列（快衰减）vs 随机游走（慢衰减）。"""
    from statsmodels.graphics.tsaplots import plot_acf
    fig, axes = plt.subplots(1, 2, figsize=(10, 3.6))
    seq = np.array([2, 4, 3, 5, 4, 6])  # 第 4.5 节手算序列
    plot_acf(seq, lags=4, ax=axes[0], title="平稳短序列 2,4,3,5,4,6 的 ACF：ρ(1)≈−0.10、ρ(2)≈0.40（虚线 ±1.96/√6≈±0.80 内，不显著）")
    rw = d["sim"]["random_walk"].values[:200]
    plot_acf(rw, lags=20, ax=axes[1], title="随机游走的 ACF：衰减极慢（“记仇”型，非平稳）")
    fig.tight_layout()
    fig.savefig(FIG / "fig04-acf.png", dpi=150)
    plt.close(fig)


def fig05_spectrum(d):
    """第 5 章：12 个月周期 + 噪声的时域图与周期图（尖峰在 1/12≈0.083）。"""
    t = np.arange(1, 36 + 1)  # 3 年
    rng = np.random.default_rng(7)
    x = 5 * np.sin(2 * np.pi * t / 12) + rng.normal(0, 0.8, len(t))
    # 周期图（numpy FFT）
    n = len(x)
    f = np.fft.rfftfreq(n, d=1.0)
    power = np.abs(np.fft.rfft(x - x.mean())) ** 2 / n
    fig, axes = plt.subplots(1, 2, figsize=(10, 3.6))
    axes[0].plot(t, x, color="#2c5f8a", lw=1.2)
    axes[0].set_title("时域：x(t)=5·sin(2πt/12)+噪声——肉眼难判周期", fontsize=10)
    axes[0].set_xlabel("月份"); axes[0].set_ylabel("x(t)")
    axes[1].plot(f, power, color="#c55a11", lw=1.0)
    axes[1].axvline(1 / 12, color="red", ls="--", lw=1.2, label="1/12 ≈ 0.083/月（主周期 12 个月）")
    axes[1].set_title("周期图：频率 0.083 处竖起显著尖峰", fontsize=10)
    axes[1].set_xlabel("频率（1/月）"); axes[1].set_ylabel("能量"); axes[1].legend(fontsize=9)
    fig.tight_layout()
    fig.savefig(FIG / "fig05-spectrum.png", dpi=150)
    plt.close(fig)


def fig06_smoothing(d):
    """第 6 章：指数平滑 α=0.3 vs α=0.9 对比（数据含噪声上升）。"""
    rng = np.random.default_rng(3)
    x = np.cumsum(rng.normal(0.2, 0.5, 30)) + 10
    a1, a2 = 0.3, 0.9
    s1, s2 = [x[0]], [x[0]]
    for v in x[1:]:
        s1.append(a1 * v + (1 - a1) * s1[-1])
        s2.append(a2 * v + (1 - a2) * s2[-1])
    fig, ax = plt.subplots(figsize=(8.5, 3.8))
    ax.plot(x, "o-", color="#999", lw=1.0, ms=4, label="原始序列")
    ax.plot(s1, color="#2c5f8a", lw=2.0, label="α=0.3：平滑、反应慢（更稳）")
    ax.plot(s2, color="#c55a11", lw=2.0, label="α=0.9：紧跟数据（也跟噪声）")
    ax.set_xlabel("t"); ax.set_ylabel("x")
    ax.set_title("简单指数平滑：α 是“记忆旋钮”——小 α 平滑，大 α 灵敏", fontsize=11)
    ax.legend(fontsize=9)
    fig.tight_layout()
    fig.savefig(FIG / "fig06-smoothing.png", dpi=150)
    plt.close(fig)


def fig08_differencing(d):
    """第 8 章：景区数据原始 vs 一阶差分（对应 8.3 手算）。"""
    s = d["scenic"]
    y = s["tourists_10k"].values
    dy = np.diff(y)
    fig, axes = plt.subplots(2, 1, figsize=(9, 5.4))
    axes[0].plot(s["date"], y, color="#2c5f8a", lw=1.5)
    axes[0].set_title("原始序列：先升后降的季节单峰（非平稳）", fontsize=10, loc="left")
    axes[1].plot(s["date"][1:], dy, color="#c55a11", lw=1.5)
    axes[1].axhline(0, color="gray", lw=0.8, ls="--")
    axes[1].set_title("一阶差分：在 ±1 附近波动、均值≈0（平稳得多）", fontsize=10, loc="left")
    axes[1].set_xlabel("时间")
    fig.tight_layout()
    fig.savefig(FIG / "fig08-differencing.png", dpi=150)
    plt.close(fig)


def fig10_garch(d):
    """第 10 章：GARCH(1,1) 模拟——收益率波动聚集与条件方差。"""
    sim = d["sim"]
    fig, axes = plt.subplots(2, 1, figsize=(9, 5.2), sharex=True)
    axes[0].plot(sim["date"], sim["garch_ret"], color="#2c5f8a", lw=0.8)
    axes[0].set_title("GARCH(1,1) 模拟收益率：大波动后跟着大波动（波动聚集）", fontsize=10, loc="left")
    axes[1].plot(sim["date"], sim["garch_var"], color="#c55a11", lw=1.2)
    axes[1].set_title("条件方差 σ²_t：方差的“记忆”让波动持续", fontsize=10, loc="left")
    axes[1].set_xlabel("时间")
    fig.tight_layout()
    fig.savefig(FIG / "fig10-garch.png", dpi=150)
    plt.close(fig)


def fig15_attention():
    """第 15 章：注意力权重示意图（查询×键 热力图 + 加权求和）。"""
    rng = np.random.default_rng(11)
    n = 8
    W = rng.random((n, n))
    np.fill_diagonal(W, W.max(axis=1))  # 对角线强
    W = W / W.sum(axis=1, keepdims=True)
    fig, axes = plt.subplots(1, 2, figsize=(10, 3.8))
    im = axes[0].imshow(W, cmap="YlOrRd", aspect="auto")
    axes[0].set_title("注意力权重：每个查询（行）对历史键（列）的相似度，行和为 1", fontsize=10)
    axes[0].set_xlabel("键 K（历史位置）"); axes[0].set_ylabel("查询 Q（当前位置）")
    fig.colorbar(im, ax=axes[0], fraction=0.046)
    # 右：加权求和示意
    v = rng.normal(0, 1, n)
    out = W[3] @ v
    axes[1].bar(range(n), v, color="#5b9bd5", alpha=0.7)
    axes[1].bar(range(n), W[3] * v, color="#c55a11", alpha=0.9)
    axes[1].axhline(out, color="k", ls="--", lw=1.2)
    axes[1].set_title(f"第 4 个查询的输出 = Σ 权重×值 ≈ {out:.2f}（橙色条×权重再求和）", fontsize=10)
    axes[1].set_xlabel("历史位置（值 V）"); axes[1].set_ylabel("数值")
    fig.tight_layout()
    fig.savefig(FIG / "fig15-attention.png", dpi=150)
    plt.close(fig)


def main() -> None:
    d = load()
    fig01_ts_vs_cross(d)
    fig02_decomposition(d)
    fig04_stationarity(d)
    fig04_acf(d)
    fig05_spectrum(d)
    fig06_smoothing(d)
    fig08_differencing(d)
    fig10_garch(d)
    fig15_attention()
    print("已生成插图:")
    for f in sorted(FIG.glob("fig*.png")):
        print(f"  - book/figures/{f.name} ({f.stat().st_size / 1024:.0f} KB)")


if __name__ == "__main__":
    main()
