---
title: "martfl: Enabling utility-driven data marketplace with a robust and verifiable federated learning architecture"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2023
created: 2025-04-19 11:08:28
modified: 2025-04-19 11:09:10
---

## martfl: Enabling utility-driven data marketplace with a robust and verifiable federated learning architecture

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3576915.3623134)

## 作者

+ [Qi Li](Qi%20Li.md)
+ Zhuotao Liu 
+ [Qi Li](Qi%20Li.md)
+ Ke Xu 

## 笔记

好的，作为一名密码学领域的研究助手，我将严格按照您的要求，对这篇论文进行深度阅读和分析，并输出结构化的笔记。

### 背景与动机

在人工智能模型训练中，高质量数据的获取是关键瓶颈，而数据市场为此提供了交易平台。然而，随着数据隐私法规（如GDPR、PIPL）的日益严格，直接交易原始数据变得不合规甚至违法，这促使市场范式从交易原始数据转向交易数据效用。联邦学习作为一种不共享原始数据即可协同训练模型的范式，被看作是构建效用驱动型数据市场的理想工具。然而，将现有联邦学习架构直接应用于数据市场面临三大挑战：首先，在数据交易前，数据需求方无法在不获取数据提供方本地模型更新的情况下评估其质量，导致“先有鸡还是先有蛋”的困境；其次，现有的鲁棒聚合协议在处理恶意数据提供方时，在鲁棒性（排除恶意方）与包容性（包含良性方）之间存在根本性的权衡，特别是当数据需求方的根数据集存在偏差时，容易出现过拟合问题；最后，现有联邦学习设计缺乏一个可验证的计费机制，无法保证数据需求方根据每个数据提供方对模型的实际贡献（即聚合权重）来公平地分配奖励。本文旨在填补这一空白，提出一个集鲁棒性与可验证性于一体的新型联邦学习架构。

### 相关工作

[12] Blanchard et al. Machine Learning with Adversaries: Byzantine Tolerant Gradient Descent. **NeurIPS 2017** [Google Scholar](https://scholar.google.com/scholar?q=Machine+Learning+with+Adversaries%3A+Byzantine+Tolerant+Gradient+Descent)
> 核心思路：提出Krum算法，通过选择与多数其他梯度最相似的梯度来容忍拜占庭故障，是客户端驱动的鲁棒聚合代表。
> 局限与区别：该算法依赖诚实多数假设，在数据交易场景中此假设可能不成立；且其包容性受限于对恶意节点比例的预设。

[18] Cao et al. FLTrust: Byzantine-robust Federated Learning via Trust Bootstrapping. **NDSS 2021** [Google Scholar](https://scholar.google.com/scholar?q=FLTrust%3A+Byzantine-robust+Federated+Learning+via+Trust+Bootstrapping)
> 核心思路：提出服务器驱动的鲁棒聚合方法，利用数据需求方持有的可信根数据集来评估和校准各数据提供方的模型更新。
> 局限与区别：该方法的包容性受限于其根数据集的质量和分布；当根数据集有偏时，会过滤掉许多与根数据集分布不同的良性数据提供方，导致过拟合。本文通过动态基线调整克服了这一局限。

[12] (此条目已在之前列出，与[18]不同)
[51] Liang et al. OmniLytics: A Blockchain-based Secure Data Market for Decentralized Machine Learning. **FL-ICML 2021** [Google Scholar](https://scholar.google.com/scholar?q=OmniLytics%3A+A+Blockchain-based+Secure+Data+Market+for+Decentralized+Machine+Learning)
> 核心思路：通过在区块链上直接执行整个模型聚合过程（使用安全聚合和多Krum算法）来实现公平交易。
> 局限与区别：该方案强制数据需求方公开其评估和聚合算法，限制了其使用复杂、专有算法的能力；且仅支持少量数据提供方，计算开销巨大。本文的证明方案只关注关键的聚合计算，开销与算法和模型大小解耦。

[57] Lyu et al. Towards Fair and Privacy-preserving Federated Deep Models. **TPDS 2020** [Google Scholar](https://scholar.google.com/scholar?q=Towards+Fair+and+Privacy-preserving+Federated+Deep+Models)
> 核心思路：利用区块链和特殊块结构实现公平的联邦学习。
> 局限与区别：该方法将模型评估协议公开置于区块链上，导致聚合算法无法处理恶意数据提供方。本文仅在链上验证聚合的正确性，而将复杂的质量评估过程放在线下由数据需求方私有执行。

[58] McMahan et al. Communication-efficient Learning of Deep Networks From Decentralized Data. **AISTATS 2017** [Google Scholar](https://scholar.google.com/scholar?q=Communication-efficient+Learning+of+Deep+Networks+From+Decentralized+Data)
> 核心思路：提出联邦平均算法（FedAvg），开创了联邦学习范式。
> 局限与区别：该基线算法完全无法抵御恶意攻击，且缺乏数据交易和公平计费机制。本文在其基本框架上增加了鲁棒性、可评估性和可验证性。

### 核心技术与方案

martFL 的整体框架围绕两个核心创新设计展开，以解决现有FL架构在数据市场中的三大挑战。

**质量感知模型评估协议。**

此协议旨在消除现有鲁棒聚合方法中鲁棒性与包容性的权衡。其核心逻辑是：数据需求方利用其自有（可能存偏）的根数据集训练一个基线模型，并用此模型为所有数据提供方提交的本地模型更新打分，分数为余弦相似度：
$$s_{i}^{t} = \text{Cosine}(u_{g}^{t}, u_{i}^{t}) = \frac{u_{g}^{t} \cdot u_{i}^{t}}{||u_{g}^{t}|| \cdot ||u_{i}^{t}||}$$
得到所有分数后，协议并非简单截断（如FLTrust），而是执行一个分层聚类算法（HCA）来智能筛选。首先，通过Gap统计量确定分数集合的最佳聚类数$\hat{g}$。然后，根据聚类结果采取不同策略：
*   单簇集中分布（范围小于门限$T$）：视所有模型质量相当，全部纳入。
*   单簇分散分布：执行二次聚类（$K$-Means, $\hat{g}=2$），分为高、低质量簇，仅保留高质量簇。
*   多簇分布：将第一次聚类的簇分为高、低质量两类。在高质量类别中，最高分簇的模型直接入选（$\mathcal{P}_1$），其余簇的模型根据其与最高分簇中心的距离进行加权，成为“合格”模型（$\mathcal{P}_2$）。协议会从$\mathcal{P}_1$和随机小部分$\mathcal{P}_2$中选取模型进行聚合。

此方法的关键在于，它通过分析全局分数分布而非仅依赖基线模型，从而避免了对根数据集的过拟合。为了进一步解决根数据集偏差问题，协议设计了**动态基线调整**机制：在每轮训练结束后，数据需求方评估所有被选中的本地模型在根数据集上的Kappa系数，并选择系数最高的数据提供方作为下一轮的基线。这相当于用在上轮中表现最好的数据提供方来部分替代或补充原有的（可能有偏的）基线。

在交易前，为确保数据提供方不会在评估后反悔，模型评估过程在密文（CKKS同态加密）下进行。数据需求方加密基线更新，数据提供方在密文上计算并返回余弦相似度，使数据需求方能在不获得明文模型的情况下完成评估。

**可验证交易协议。**

此协议旨在确保公平计费，其核心是一个零知识证明系统。该证明系统不试图证明整个训练过程，而是只证明一个关键计算——加权平均聚合，即$W_{g}^{t} = W_{g}^{t-1} + \sum K^{t} U^{t}$。数据需求方作为证明者，向公众（如数据提供方）证明它确实使用其已承诺的聚合权重$K^{t}$对承诺的本地模型$U^{t}$进行了线性组合，得到了公开的全局模型$W_{g}^{t}$。这足以保证公平性，因为奖励分配完全由权重$K^{t}$驱动。

为了降低证明复杂度，特别是使证明开销与模型大小解耦，协议引入了**可验证抽样**技术。通过使用可验证延迟函数（VDF）从模型中随机选取固定数量c个参数进行证明。只要数据需求方能对抽样出的参数提供正确证明，就能以高概率保证其对所有参数都进行了正确计算。此时，证明电路复杂度从$O(n \cdot m)$（n为DP数量，m为参数总量）降低为与m无关的$O(n \cdot c)$。证明过程使用zk-SNARK（Groth16），量化后的聚合和更新步骤被编译成算术电路。量化通过扩展数值范围避免了溢出问题，确保了正确性。

该系统的安全性依赖于：区块链提供了不可篡改的公共账本和自动执行的智能合约；zk-SNARK协议的零知识性（保护本地模型隐私）和可靠性（防止DA作弊）；VDF的随机性确保抽样不受DA控制。系统复杂度方面，数据需求方的线下计算包括加密、聚类、量化、电路编译和证明生成，其计算量由DP数量和抽样参数数量决定。链上验证的计算量极小（仅需四次双线性配对检查），且与模型大小无关。数据提供方的成本主要是本地训练和链上验证智能合约。

### 核心公式与流程

**[质量感知模型评分]**
$$s_{i}^{t} = \text{Cosine}(u_{g}^{t}, u_{i}^{t}) = \frac{u_{g}^{t} \cdot u_{i}^{t}}{||u_{g}^{t}|| \cdot ||u_{i}^{t}||}$$
> 作用：用于评估每个数据提供方提交的本地模型更新$u_i^t$相对于数据需求方自更新$u_g^t$的相似度，是后续聚类和筛选的基础。

**[量化聚合电路核心计算]**
$$2^{\eta} \mathbb{U}_{i, j}^{q^{\prime}} = \mathbb{R}_{i, j}^{a} + 2^{\eta} U^{z^{\prime}} + \left\lfloor 2^{\eta} \frac{K^s U^s}{U^{s^{\prime}}}\left(M_1 + M_4 - M_2 - M_3\right) \right\rfloor$$
$$
\text{ s.t. } M_1 = \sum_{k=1}^{n} \mathbb{K}_{i, k}^{q} \mathbb{U}_{k, j}^{q}, M_2 = U^{z} \sum_{k=1}^{n} \mathbb{K}_{i, k}^{q},
$$
$$
M_3 = K^{z} \sum_{k=1}^{n} \mathbb{U}_{k, j}^{q}, M_4 = n K^{z} U^{z}
$$
> 作用：在有限域$\mathbb{F}_q$中，以整数形式实现加权和的计算$U^{t^{\prime}} = K^{t}U^{t}$，这是证明电路的核心部分。通过引入大整数$2^\eta$和重排计算顺序（$M_1 + M_4 - M_2 - M_3$），消除了计算中的负数，使其成为ZKP友好的形式。

**[量化更新电路核心计算]**
$$2^{\eta} \mathbb{W}_{i, j}^{q^{\prime}} = \mathbb{R}_{i, j}^{u} + 2^{\eta} W^{z^{\prime}} + \left\lfloor 2^{\eta} \left(N_1 + N_3 - N_2 - N_4\right) \right\rfloor$$
> 作用：在有限域中实现全局模型的更新$W_g^t = W_g^{t-1} + U^{t^{\prime}}$。该式与聚合电路的计算形式类似，同样通过符号重排消除了负数，使其易于用算术电路表示。

### 实验结果

实验在配置Intel Xeon Gold 6348 CPU和NVIDIA RTX A100 GPU的服务器上进行，使用PyTorch实现FL，SEAL库实现同态加密，以太坊测试网部署智能合约。数据集包括图像分类（FMNIST, CIFAR）和文本分类（TREC, AGNEWS）。对比基线包括服务器驱动方法（FLTrust, CFFL）和客户端驱动方法（FedAvg, Krum, Median, RFFL）。

*   **准确性与成本**：在数据需求方根数据集有偏的场景下，martFL在所有任务上均显著优于FLTrust和CFFL。例如，在TREC任务上，当20%的数据提供方持有偏态数据时，martFL的MTA为88.80%，而FLTrust仅为67.40%。同时，martFL的数据获取成本（DAC, 平均每轮购买的模型百分比）显著低于CFFL（始终为100%），在TREC上约为51.79%-53.88%。
*   **鲁棒性**：martFL在面对自由骑手攻击、符号随机化攻击、后门攻击、标签翻转攻击和女巫攻击时，在绝大多数情况下均能取得最高MTA和最低ASR。例如，在CIFAR数据集上面对标签翻转攻击时，martFL的ASR始终稳定在约15%，而其他基线方法的ASR随恶意DP比例增加而上升至40%以上。
*   **量化损失**：为支持可验证证明而引入的量化和反量化操作对模型性能影响极小，MTA和F1损失均小于1%。
*   **系统开销**：martFL的链上智能合约函数执行开销极低（均低于$0.25 \times 10^6$ wei，约0.0025美元），链下同态加解密耗时也很短。与Omnilytics相比，martFL的Gas成本至少低1000倍，同时支持更多参与者和更大的模型。

### 局限性与开放问题

1.  本文提出的可验证证明方案依赖于一个受信设置（Trusted Setup），探索无需受信设置的、透明的零知识证明方案是未来工作的一个方向。
2.  动态基线调整算法在数据需求方和持有偏态数据的数据提供方存在相同偏态（Type-I Bias）且总类别数很少时，选择正确基线的概率会有所下降（例如TREC任务中为65.33%），算法在极端场景下的鲁棒性仍有提升空间。
3.  当前模型评估协议主要基于当前轮的分数进行聚类，未来可考虑融入数据提供方的历史信誉信息（如动量），以进一步减少对数据需求方根数据集的依赖并补偿基线选择中的偏差。
4.  论文未详细探讨如何为FL的数据市场中的数据定价，而是假设奖励与聚合权重成比例，一个更全面的数据估值与定价机制是值得研究的方向。

### 强关联论文

[12] Blanchard et al. Machine Learning with Adversaries: Byzantine Tolerant Gradient Descent. **NeurIPS 2017** [Google Scholar](https://scholar.google.com/scholar?q=Machine+Learning+with+Adversaries%3A+Byzantine+Tolerant+Gradient+Descent)

[18] Cao et al. FLTrust: Byzantine-robust Federated Learning via Trust Bootstrapping. **NDSS 2021** [Google Scholar](https://scholar.google.com/scholar?q=FLTrust%3A+Byzantine-robust+Federated+Learning+via+Trust+Bootstrapping)

[51] Liang et al. OmniLytics: A区块链-based Secure Data Market for Decentralized Machine Learning. **FL-ICML 2021** [Google Scholar](https://scholar.google.com/scholar?q=OmniLytics%3A+A+Blockchain-based+Secure+Data+Market+for+Decentralized+Machine+Learning)

[57] Lyu et al. Towards Fair and Privacy-preserving Federated Deep Models. **IEEE TPDS 2020** [Google Scholar](https://scholar.google.com/scholar?q=Towards+Fair+and+Privacy-preserving+Federated+Deep+Models)

[58] McMahan et al. Communication-efficient Learning of Deep Networks From Decentralized Data. **AISTATS 2017** [Google Scholar](https://scholar.google.com/scholar?q=Communication-efficient+Learning+of+Deep+Networks+From+Decentralized+Data)

[37] Groth. On the Size of Pairing-based Non-interactive Arguments. **EUROCRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=On+the+Size+of+Pairing-based+Non-interactive+Arguments)

[21] Cheon et al. Homomorphic Encryption for Arithmetic of Approximate Numbers. **ASIACRYPT 2017** [Google Scholar](https://scholar.google.com/scholar?q=Homomorphic+Encryption+for+Arithmetic+of+Approximate+Numbers)

[72] Yin et al. Byzantine-robust Distributed Learning: Towards Optimal Statistical Rates. **ICML 2018** [Google Scholar](https://scholar.google.com/scholar?q=Byzantine-robust+Distributed+Learning%3A+Towards+Optimal+Statistical+Rates)

[56] Lyu et al. Collaborative Fairness in Federated Learning. **Federated Learning 2020** [Google Scholar](https://scholar.google.com/scholar?q=Collaborative+Fairness+in+Federated+Learning)


## 关键词

+ 联邦学习
+ 数据市场
+ 零知识证明
+ 可验证性
+ 模型聚合
+ 隐私保护
+ 恶意防护