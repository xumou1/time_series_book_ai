# 附录 B · 工具安装与速查

> 本书所有示例对应的 Python/R 工具。安装一行搞定；"何时用"对应章节。

## B.1 Python 生态（一条命令装全家）

```bash
pip install pandas numpy matplotlib scipy statsmodels scikit-learn
pip install statsforecast neuralforecast       # Nixtla：统计+深度基线（第 6、8 章）
pip install darts                                # 统一 API 预测库（第 6–16 章实践）
pip install sktime                               # scikit-learn 风格时序工具箱（第 13 章）
pip install gluonts                              # 深度概率预测（DeepAR，第 16 章）
pip install chronos-forecasting uni2ts           # 基础模型推理（第 17 章）
pip install mapie                                # 保形预测（第 19 章）
pip install arch                                 # GARCH 族（第 10 章）
```

## B.2 R 生态

```r
install.packages(c("forecast", "fable", "tsibble", "bsts"))
# forecast/fable：ETS、ARIMA、STL、概率预测（第 6、8 章）
# bsts：贝叶斯结构时间序列（第 9 章）
```

## B.3 按任务速查

| 任务 | 首选工具 | 对应章节 |
|---|---|---|
| 探索：画图/分解/ACF | `matplotlib`、`statsmodels`（STL、plot_acf） | 1、2、4 |
| 平稳性检验 | `statsmodels.tsa.stattools`（adfuller、kpss） | 4 |
| 指数平滑/ARIMA | `statsforecast` 或 `statsmodels` | 6、8 |
| 自动选阶 ARIMA | `pmdarima.auto_arima` 或 R `auto.arima` | 8 |
| 状态空间/结构时序 | `statsmodels.UnobservedComponents` | 9 |
| GARCH | `arch` | 10 |
| 协整/VAR | `statsmodels`（coint_johansen、VAR） | 11 |
| 机制转换 | `statsmodels.MarkovRegression` | 12 |
| 树模型/特征 | `scikit-learn`、`lightgbm` | 13 |
| 深度学习 | `PyTorch`、`darts`、`TSLib`（thuml/Time-Series-Library） | 14、15 |
| 概率/生成式 | `gluonts`（DeepAR）、`darts` | 16 |
| 基础模型零样本 | `chronos-forecasting`、`uni2ts`、`timesfm` | 17 |
| 保形预测 | `mapie` | 19 |

## B.4 常见坑（环境相关）

1. **TSLib 依赖旧版 PyTorch**：按仓库 README 指定版本安装，别用最新版硬试（第 15 章练习）。
2. **`statsmodels` 与 `pandas` 版本冲突**：升级/固定 `pandas>=2.0` 通常可解。
3. **GluonTS 需要 `torch`**：先装 PyTorch 再装 gluonts。
4. **Windows 上 LightGBM**：官方 wheel 直接可用；报错先升级 pip。
5. **时区/日期解析**：读 CSV 时用 `pd.to_datetime(..., errors="coerce")` 并检查 `NaT`（第 1 章第 2 步）。

## B.5 数据源

| 数据 | 获取 |
|---|---|
| M4/M5 竞赛 | `forecast` R 包内置部分；M5 在 Kaggle |
| ETT/Weather/Exchange | TSLib 仓库自带下载脚本（第 15 章） |
| LOTSA（Moirai 语料） | `uni2ts` 包下载 |
| 经典测试序列（太阳黑子等） | `statsmodels.datasets` |

## B.6 本书配套示例项目（`examples/`）

本书自带一个 **uv 管理的可运行示例项目**（`E:\Dropbox\TimeSeries\examples`），数据与插图均与书中章节一一对应：

```bash
cd examples
uv sync                                     # 安装依赖（matplotlib/pandas/numpy/statsmodels）
uv run python scripts/make_data.py          # 生成示例数据 → data/
uv run python scripts/make_figures.py       # 生成书中插图 → book/figures/
```

- 数据：景区游客量（第 2/8 章）、奶茶店销售额（第 20 章案例）、白噪声/随机游走/GARCH 模拟（第 3/4/10 章）；
- 插图：9 张图分别嵌入第 1/2/4/5/6/8/10/15 章；
- 若 `uv` 不在 PATH：用完整路径调用，如 `"$HOME/.cherrystudio/bin/uv.exe" run python scripts/make_data.py`。
- 详见 `examples/README.md`。
