---
title: "Mystique: Efficient Conversions for Zero-Knowledge Proofs with Applications to Machine Learning"
标题简称:
论文类型: conference
会议简称: USENIX Security
发表年份: 2021

modified: 2025-04-10 17:13:27
---

## Mystique: Efficient Conversions for Zero-Knowledge Proofs with Applications to Machine Learning

## 发表信息

+ [原文链接](https://www.usenix.org/conference/usenixsecurity21/presentation/weng)

## 作者

+ [Chenkai Weng](Chenkai%20Weng.md)
+ [Kang Yang](Kang%20Yang.md)
+ [Xiang Xie](Xiang%20Xie.md)
+ [Jonathan Katz](Jonathan%20Katz.md)
+ [Xiao Wang](Xiao%20Wang.md)

## 笔记

### 背景与动机
现有交互式零知识证明协议在大规模计算场景中的效率已取得显著提升，但面对深度神经网络等复杂计算时仍缺乏足够的表达力与可扩展性。zk-SNARKs 虽然证明尺寸小、验证快，但其证明者内存需求与陈述规模成正比，例如证明十亿约束的陈述约需 640 GB 内存，只能处理决策树等简单模型。基于子域向量不经意线性评估的交互式 ZK 协议在时间和内存开销上具有优势，但无法高效处理公开承诺数据，且整体通信量仍然较大。这些方案还各自仅支持算术电路或布尔电路，缺乏混合模式计算能力，难以高效实现包含非线性激活函数和矩阵乘法的神经网络推理。本文旨在设计一套支持多种高效转换的系统，填补现有 sVOLE 类 ZK 协议在混合电路、承诺数据集成及精度管理方面的空白，从而首次实现百层以上神经网络的零知识推理。

### 相关工作

[7] Baum 等. Mac'n'Cheese: Zero-Knowledge Proofs for Arithmetic Circuits with Nested Disjunctions. **IACR ePrint 2020** [Google Scholar](https://scholar.google.com/scholar?q=Mac%27n%27Cheese%3A+Zero-Knowledge+Proofs+for+Arithmetic+Circuits+with+Nested+Disjunctions)
> 核心思路：基于 sVOLE 的高效算术电路 ZK 证明。
> 局限与区别：仅支持算术电路，不支持布尔电路及转换。

[27] Dittmer 等. Line-Point Zero Knowledge and Its Applications. **IACR ePrint 2020** [Google Scholar](https://scholar.google.com/scholar?q=Line-Point+Zero+Knowledge+and+Its+Applications)
> 核心思路：提出了另一种 sVOLE 类 ZK 协议变体。
> 局限与区别：同样不支持混合算术-布尔电路及承诺转换。

[28] Escudero 等. Improved Primitives for MPC over Mixed Arithmetic-Binary Circuits. **Crypto 2020** [Google Scholar](https://scholar.google.com/scholar?q=Improved+Primitives+for+MPC+over+Mixed+Arithmetic-Binary+Circuits)
> 核心思路：在安全多方计算中提出扩展双重认证比特用于混合电路。
> 局限与区别：本文将其思路适配到 ZK 环境，并设计 ZK 友好的 edaBits 构造与一致性检查协议。

[31] Freivalds. Probabilistic Machines Can Use Less Running Time. **IFIP Congress 1977** [Google Scholar](https://scholar.google.com/scholar?q=Probabilistic+Machines+Can+Use+Less+Running+Time)
> 核心思路：通过随机线性组合验证矩阵乘法。
> 局限与区别：本文将该算法推广到算术电路，并嵌入 sVOLE 认证框架以实现通信量仅与矩阵维度之和相关的 ZK 证明。

[52] Weng 等. Wolverine: Fast, Scalable, and Communication-Efficient Zero-Knowledge Proofs for Boolean and Arithmetic Circuits. **IEEE S&P 2021** [Google Scholar](https://scholar.google.com/scholar?q=Wolverine%3A+Fast%2C+Scalable%2C+and+Communication-Efficient+Zero-Knowledge+Proofs+for+Boolean+and+Arithmetic+Circuits)
> 核心思路：高效的 sVOLE 类 ZK 证明系统。
> 局限与区别：本文基于其框架，新增转换和矩阵乘法优化。

[54] Yang 等. Quicksilver: Efficient and Affordable Zero-Knowledge Proofs for Circuits and Polynomials over Any Field. **CCS 2021** [Google Scholar](https://scholar.google.com/scholar?q=Quicksilver%3A+Efficient+and+Affordable+Zero-Knowledge+Proofs+for+Circuits+and+Polynomials+over+Any+Field)
> 核心思路：最新的 sVOLE 类 ZK 协议，支持域上多项式证明。
> 局限与区别：本文将其作为底层 ZK 引擎，并实现上层转换和优化。

### 核心技术与方案

系统的整体架构如图 1 所示：证明者首先将其秘密输入通过承诺-认证转换得到认证值，然后在线性层使用改进的矩阵乘法协议，在非线性层通过定点-浮點转换与算术-布尔转换计算激活函数等操作，最终输出认证结果。

**zk-edaBits 构造与一致性检查。** zk-edaBits 是混合电路转换的基础。一个 zk-edaBit 包含 m 个随机认证比特 $[r_0]_2,\dots,[r_{m-1}]_2$ 和一个随机认证域元素 $[r]_p$，满足 $r=\sum_{h=0}^{m-1}r_h\cdot 2^h \pmod p$。但直接并行生成时恶意证明者可能输出不一致的比特-域值对。为此，论文采用“切-桶”技术：首先生成 $N(B-1)+c$ 个候选 zk-edaBits，通过随机置换打乱后打开最后 c 个进行正确性检查；然后将剩余 N(B-1) 个分配到 N 个桶中，每个桶内比较第一个与其余 B-1 个的一致性——具体地，计算 $[t]_p=[r]_p+[s]_p$ 和 $\text{AdderModp}([r_0]_2,\dots,[r_{m-1}]_2,[s_0]_2,\dots,[s_{m-1}]_2)$ 得到 $[t_0]_2,\dots,[t_{m-1}]_2$，打开这些比特并检查 $\sum t_h 2^h \stackrel{?}{=} t \pmod p$。该协议在 $\mathcal{F}_{\text{authZK}}$ 混合模型中 UC 实现，统计错误至多为 $\binom{N(B-1)+c}{B-1}^{-1}+1/p^k$。

**算术-布尔转换协议。** 给定一个认证值 $[x]_p$ 需要转换为 m 个认证比特 $[x_0]_2,\dots,[x_{m-1}]_2$：利用一个随机 zk-edaBit $([r_0]_2,\dots,[r_{m-1}]_2,[r]_p)$，打开 $[z]_p=[x]_p-[r]_p$ 得到 z，计算其比特分解 $(z_0,\dots,z_{m-1})$，再通过加法电路 $\text{AdderModp}(z_0,\dots,z_{m-1},[r_0]_2,\dots,[r_{m-1}]_2)$ 得到 $[x_0]_2,\dots,[x_{m-1}]_2$。反向转换（布尔到算术）同理。该协议统计安全，依赖 zk-edaBits 的一致性和 $\mathcal{F}_{\text{authZK}}$ 的零知识性。

**承诺-认证转换。** 为将公开承诺值导入 sVOLE 认证框架，论文设计了一种混合承诺方案：证明者选择密钥 $sk\in\{0,1\}^\lambda$，计算 $\text{com}_0=H(sk,r)$ 和对每个数据块 $\boldsymbol{x}_i\in\mathbb{F}_q^m$ 加密 $\boldsymbol{c}_i=\text{PRF}(sk,i)+\boldsymbol{x}_i$，并构建 Merkle 树得到根 $\text{com}_1$，最终承诺为 $(\text{com}_0,\text{com}_1)$。在转换阶段，证明者发送 $\boldsymbol{c}_i$ 和 Merkle 路径，然后通过 $\mathcal{F}_{\text{authZK}}$ 证明其知道 $sk,r$ 使得 $\text{com}_0=H(sk,r)$ 且 $\boldsymbol{x}_i=\boldsymbol{c}_i-\text{PRF}(sk,i)$，从而将 $\boldsymbol{x}_i$ 的每个分量转换为认证值。该协议在随机预言机和伪随机函数假设下 UC 执行，借助 LowMC 实例化 PRF 以降低布尔电路复杂度。

**矩阵乘法优化。** 采用 Freivalds 随机检查的推广：验证者采样随机向量 $\boldsymbol{u}\in(\mathbb{F}_{q^k})^n,\boldsymbol{v}\in(\mathbb{F}_{q^k})^\ell$，各方本地计算 $[\boldsymbol{x}]^\top=\boldsymbol{u}^\top[\mathbf{A}], [\boldsymbol{y}]=[\mathbf{B}]\boldsymbol{v}, [z]=\boldsymbol{u}^\top[\mathbf{C}]\boldsymbol{v}$，然后只需证明 $\boldsymbol{x}^\top\cdot\boldsymbol{y}=z$。一次证明通信量仅为 $O(k\log q)$ 比特，与 n,m,ℓ 无关，且计算量由证明者本地 $O(nm\ell)$ 矩阵乘法主导。与 Quicksilver [54] 相比，相同矩阵维度（1024×1024）下快 7 倍。

**定点-浮点转换与 TensorFlow 集成。** 线性层用 $\mathbb{F}_p$ 编码定点数（Mersenne 素数 $p=2^{61}-1$，精度 s=16），非线性层使用 IEEE-754 单精度浮点。通过算术-布尔转换与移位电路实现双向转换。系统集成至 Rosetta 框架，通过静态图变换和动态执行将 TensorFlow 算子的数据流转换为认证值流，支持 ReLU,Sigmoid,Max Pooling,SoftMax,Batch Normalization 等操作。

### 核心公式与流程

**[zk-edaBits 一致性检查等式]**
$$\begin{aligned}
[t]_p &:= [r]_p + [s]_p \\
([t_0]_2,\dots,[t_{m-1}]_2) &:= \text{AdderModp}([r_0]_2,\dots,[r_{m-1}]_2,[s_0]_2,\dots,[s_{m-1}]_2) \\
&\text{验证: } \sum_{h=0}^{m-1} t_h \cdot 2^h \stackrel{?}{=} t \pmod p
\end{aligned}$$
> 作用：检查桶内两个 zk-edaBits 的比特分解与域值是否一致，若恶意证明者提交不一致值则高概率被检测。

**[矩阵乘法减少等式]**
$$\boldsymbol{u}^\top \cdot [\mathbf{A}] \cdot [\mathbf{B}] \cdot \boldsymbol{v} = \boldsymbol{u}^\top \cdot [\mathbf{C}] \cdot \boldsymbol{v}$$
> 作用：将 $n\times m$ 乘 $m\times \ell$ 矩阵乘法验证化简为一个内积 $\boldsymbol{x}^\top\cdot\boldsymbol{y}=z$，通信量独立于矩阵维度。

**[承诺方案结构]**
$$\begin{aligned}
\text{com}_0 &:= H(sk, r) \\
\boldsymbol{c}_i &:= \text{PRF}(sk, i) + \boldsymbol{x}_i \in \mathbb{F}_q^m \\
\text{com}_1 &:= \text{MerkleRoot}(H(\boldsymbol{c}_1),\dots, H(\boldsymbol{c}_\ell))
\end{aligned}$$
> 作用：用短密钥 sk 对大批量数据块进行高效承诺，后续在零知识中证明已知 sk 和 $\boldsymbol{x}_i$ 满足上述关系，从而将公开承诺值转换为认证值。

### 实验结果

实验在两台 Amazon EC2 m5.2xlarge 机器上进行（32 GB 内存，CPU 全资源），使用 CIFAR-10 数据集，安全参数 $\lambda=128, \rho\ge 40$。在 200 Mbps 带宽下，算术-布尔转换（A2B/B2A）约需 45–49 µs，承诺-认证转换（C2A）约 55 µs，定点-浮点转换约 46 µs。非线性操作中，Sigmoid 需 1.6 ms，Max Pooling 0.5 ms，ReLU 0.26 ms，SoftMax-10 约 157 ms，Batch Normalization 约 261 ms。矩阵乘法在 1024×1024 维度下需 1.48 s，比 Quicksilver [54] 快 7 倍。端到端推理方面：公开模型、私有图像时，LeNet-5 需 6.5 s（50 Mbps）– 4.9 s（200 Mbps），ResNet-50 需 210 s – 158 s，ResNet-101 需 369 s – 262 s；全部私有时，ResNet-101 需 736 s – 535 s。精度损失仅 0.02%，ResNet-101 的 95% 测试样本 $\ell_2$ 向量差异小于 0.006。端到端应用中，零知识逃逸攻击证明（LeNet-5）需 9.8 s，真实推理证明（ResNet-101）需 28 min，私有基准测试（100 张图像）需 7.3 h。

### 局限性与开放问题
系统仅支持对单一验证者证明，不具公开可验证性，且通信量远高于 zk-SNARKs。Batch Normalization 在整体时间中占 70%，其涉及多次定点-浮点转换与复杂算术运算，存在进一步优化空间。混合协议集成方面，当前仅支持 ZK 证明，与 MPC 或同态加密的协同尚未探索。

### 强关联论文

[7] Baum 等. Mac'n'Cheese: Zero-Knowledge Proofs for Arithmetic Circuits with Nested Disjunctions. **IACR ePrint 2020** [Google Scholar](https://scholar.google.com/scholar?q=Mac%27n%27Cheese%3A+Zero-Knowledge+Proofs+for+Arithmetic+Circuits+with+Nested+Disjunctions)

[27] Dittmer 等. Line-Point Zero Knowledge and Its Applications. **IACR ePrint 2020** [Google Scholar](https://scholar.google.com/scholar?q=Line-Point+Zero+Knowledge+and+Its+Applications)

[28] Escudero 等. Improved Primitives for MPC over Mixed Arithmetic-Binary Circuits. **Crypto 2020** [Google Scholar](https://scholar.google.com/scholar?q=Improved+Primitives+for+MPC+over+Mixed+Arithmetic-Binary+Circuits)

[31] Freivalds. Probabilistic Machines Can Use Less Running Time. **IFIP Congress 1977** [Google Scholar](https://scholar.google.com/scholar?q=Probabilistic+Machines+Can+Use+Less+Running+Time)

[52] Weng 等. Wolverine: Fast, Scalable, and Communication-Efficient Zero-Knowledge Proofs for Boolean and Arithmetic Circuits. **IEEE S&P 2021** [Google Scholar](https://scholar.google.com/scholar?q=Wolverine%3A+Fast%2C+Scalable%2C+and+Communication-Efficient+Zero-Knowledge+Proofs+for+Boolean+and+Arithmetic+Circuits)

[54] Yang 等. Quicksilver: Efficient and Affordable Zero-Knowledge Proofs for Circuits and Polynomials over Any Field. **CCS 2021** [Google Scholar](https://scholar.google.com/scholar?q=Quicksilver%3A+Efficient+and+Affordable+Zero-Knowledge+Proofs+for+Circuits+and+Polynomials+over+Any+Field)


## 关键词

+ Mystique零知识证明转换
+ 算术布尔混合ZK协议
+ 深度神经网络推断验证
+ 矩阵乘法ZK优化
+ 浮点定点转换证明
+ TensorFlow隐私保护框架
