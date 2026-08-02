# KNOWLEDGE · 方法改进先验库（ts-research-method 的记忆）

> 本文件是 `ts-research-method` skill 的"记忆"，随文献积累不断追加。**每次运行后把可复用模式追加到末尾；下次运行先读。** 与 `literature/` 一起 git 同步。

## 八层模块 × 代表组件速查（案例定位用）
1. 数据/预处理：RevIN（逐实例归一化）、分解预处理、数据增强
2. 表示：patch 分片、量化 token、时间/频率/变量嵌入
3. 架构：稀疏/线性注意力、倒置注意力、SSM(Mamba)、MLP/线性、卷积(TCN)、RNN/LSTM
4. 结构先验：分解内嵌、自相关/频域、通道策略（独立 vs 混合）
5. 训练目标：掩码自监督、分位数/似然损失、对比学习、蒸馏
6. 输出：直接多步 vs 自回归、概率/分布、生成式（扩散）
7. 效率：稀疏 MoE、线性注意力/SSM、量化/蒸馏
8. 推理/适配：零样本/少样本、提示/重编程、微调

## 12 热点 × 代表论文速查（第 24 章框架）
①基础模型：TimesFM/Chronos/Moirai/MOMENT/Time-MoE
②LLM4TS：GPT4TS/Time-LLM/LLMTime + 批判（arXiv:2406.16964）
③线性之争：LTSF-Linear/DLinear、PatchTST、仿射映射剖析（2305.10721）
④通道策略：iTransformer（混合）、PatchTST（独立）、CI 权衡（2304.05206）
⑤可逆归一化：RevIN、NS-Transformer（2205.13015）、Dish-TS（2302.14829）
⑥分解多尺度：Autoformer、DLinear、TimeMixer（2405.14616）
⑦Mamba：S-Mamba（2403.11144）、TimeMachine（2403.09898）
⑧概率生成式：DeepAR、TimeGrad、CSDI、TimeDiff、Diffusion-TS
⑨掩码自监督：SimMTM、UniTS、TS2Vec
⑩效率规模化：Time-MoE（2409.16040）、scaling laws（2410.12360）、FITS
⑪评估协议：LTSF-Linear、泄漏复现（2207.07048）
⑫因果可解释：PCMCI（1702.07007）、CUTS、TFT

## 常见审稿陷阱（案例里若论文踩坑，指出）
- 无消融 → 不知赢在哪（方法论文命门）
- 基线过时 / 不跑统计基线（ETS/线性）→ 审稿红线
- 只报赢的数据集 / 单次运行 → 选择性报告
- 超参调优冒充机制改进
- 不公平对比（算力/参数不同）

## 案例写作要点
- 必须给出"模块定位 + 动机 + 证据（消融）"三件套；
- 用"赢了 ≥2/3 组合且显著 + 消融成立 + 公平对比"三件套评判论文达标度；
- 区分机制改进与工程 trick。

## 追加记录（每次运行后追加）
