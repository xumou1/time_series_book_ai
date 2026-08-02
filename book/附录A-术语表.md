# 附录 A · 术语表（中英对照）

> 按字母顺序；括号内为首次出现的章节。

| 中文 | English | 一句话解释 | 章节 |
|---|---|---|---|
| 白噪声 | white noise | i.i.d.、均值 0、方差恒定的随机序列，"无记忆" | 3 |
| 保形预测 | conformal prediction | 用校准残差把任意模型的区间校准到目标覆盖率 | 19 |
| 本征/单位根 | unit root | 非平稳的一种形式，冲击永不消退 | 4 |
| 差分 | differencing | 用相邻差值替代水平值，去趋势/去季节 | 8 |
| 长期记忆 | long memory | 自相关衰减极慢的现象 | 7 提及 |
| 超参数 | hyperparameter | 训练前定死的参数（学习率、树深度等） | 13 |
| 窗宽 | window size | 滑窗/移动平均覆盖的点数 | 2 |
| 窗口 | window | 过去的一段连续观测 | 2 |
| 词元 | token | 输入的最小单元（时间片/词/量化 bin） | 15、17 |
| 格兰杰因果 | Granger causality | "过去能否改进预测"的领先关系，非干预因果 | 11 |
| 估计 | estimation | 从数据中算出模型参数的值 | 7 |
| 归因 | attribution | 把预测值分解到各特征的贡献 | 19 |
| 滚动验证 | rolling validation | 前移切分点反复评估 | 13 |
| 过拟合 | overfitting | 拟合了噪声而非信号，换数据就崩 | 7 |
| 厚尾 | heavy tail | 极端值比正态预言多的分布 | 3 |
| 滑动平均（模型） | moving average (model) | MA：今天由过去冲击的组合决定 | 7 |
| 滑动平均（平滑） | moving average (smoother) | 对窗口取平均估计趋势 | 2 |
| 混合专家 | mixture of experts (MoE) | 多个子网络按需激活，规模大推理省 | 17 |
| 基展开 | basis expansion | 把预测表示为若干基础模式的加权组合 | 16 |
| 机制转换 | regime switching | 序列在不同行为模式（状态）间跳变 | 12 |
| 季节性 | seasonality | 固定周期（已知且不变）的波动 | 2 |
| 交叉验证 | cross-validation | 多次切分训练/验证以稳定评估（时序版见滚动验证） | 13、19 |
| 均衡/协整 | cointegration | 非平稳序列的线性组合平稳＝长期均衡 | 11 |
| 卡尔曼滤波 | Kalman filter | 从噪声观测中实时追踪隐藏状态（预测-更新） | 9 |
| 可逆性 | invertibility | MA 模型的可逆条件（软件处理） | 7 |
| 零样本 | zero-shot | 不训练直接用于新任务/新数据 | 17 |
| 马尔可夫链 | Markov chain | 状态只依赖上一状态的随机过程 | 12 |
| 脉冲响应 | impulse response | 给一个变量冲击，看其他变量的反应路径 | 11 |
| 密度 | density | 分布的概率形状（直方图的连续版） | 3 |
| 面板数据 | panel data | 多个对象 × 多个时刻 | 1 |
| 偏自相关 | partial autocorrelation | 剔除中间滞后后的直接相关 | 5 |
| 平稳性 | stationarity | 均值、方差、协方差结构不随时间变 | 4 |
| 谱密度 | spectral density | 各频率的能量分布（ACF 的傅里叶变换） | 5 |
| 期望 | expectation | 随机变量的长期平均 | 3 |
| 奇异值分解 | (SVD) | 矩阵分解，PCA 的基础（第 18 章机制解释提及） | 18 |
| 迁移学习 | transfer learning | 预训练知识迁移到新任务 | 17 |
| 趋势 | trend | 长期单向的缓慢变化 | 2 |
| 弱平稳 | weak stationarity | 只要求均值/方差/协方差恒定的实用平稳 | 4 |
| 时间索引 | time index | 观测对应的时刻 | 1 |
| 时间序列 | time series | 按时间顺序、前后相关的观测集合 | 1 |
| 数据泄漏 | data leakage | 模型"见过"了测试信息，成绩虚高 | 13 |
| 随机变量 | random variable | 试验结果（未定的数） | 3 |
| 随机过程 | stochastic process | 按时间排列的随机变量族 | 3 |
| 损失函数 | loss function | 衡量预测与真实差距的函数（训练目标） | 14 |
| 特征 | feature | 模型输入的一个维度（滞后值、日历等） | 13 |
| 条件方差 | conditional variance | 给定过去信息后对方差的预测 | 10 |
| 跳跃 | jump | 结构断点：规则突然改变 | 12 |
| 外生变量 | exogenous variable | 模型之外、提供信息的变量（天气、促销） | 8、13 |
| 伪回归 | spurious regression | 非平稳序列间虚假的高相关回归 | 4 |
| 误差修正 | error correction | 短期动态 + 向长期均衡回拉的机制 | 11 |
| 协方差 | covariance | 两个变量共同变动的程度 | 3 |
| 循环 | cycle | 周期未知或很长的起伏 | 2 |
| 样本路径 | sample path | 随机过程的一次实现（你的数据） | 3 |
| 样本外 | out-of-sample | 训练时没见过的数据（测试集） | 7、19 |
| 移动平均（居中/单边） | centered/one-sided MA | 居中用于描述，单边用于预测 | 2、6 |
| 隐马尔可夫 | hidden Markov | 状态隐藏、只能从观测推断（与机制转换同族） | 12 |
| 因果发现 | causal discovery | 从观测数据恢复因果图 | 19 |
| 因果推断 | causal inference | 回答"干预会怎样"的方法 | 19 |
| 注意力 | attention | 按内容相似度对历史加权（学出来的加权） | 15 |
| 自回归 | autoregression | 今天由过去的观测值决定 | 7 |
| 自相关 | autocorrelation | 序列与自身滞后的相关 | 4 |
| 状态空间 | state space | 隐藏状态演化 + 加噪观测的两层结构 | 9 |
| 最小二乘 | least squares | 最小化误差平方和的估计方法 | 7 提及 |
