---
title: "SafetyNets: Verifiable Execution of Deep Neural Networks on an Untrusted Cloud"
标题简称: SafetyNets
论文类型: conference
会议简称: NIPS
发表年份: 2017
modified: 2025-04-09 09:19:49
---

## SafetyNets: Verifiable Execution of Deep Neural Networks on an Untrusted Cloud

## 发表信息

+ [原文链接](https://proceedings.neurips.cc/paper/2017/hash/6048ff4e8cb07aa60b6777b6f7384d52-Abstract.html)

## 作者

+ Zahra Ghodsi
+ Tianyu Gu
+ Siddharth Garg

## 笔记

### 背景与动机
将深度神经网络的推理任务外包至云服务器面临着严峻的信任挑战：云服务商可能为降低自身计算开销而使用更简化的模型，或恶意篡改推理结果。传统的基于可信平台模块或执行时间审计的解决方案需要客户端信任硬件制造商或精确掌握服务器硬件配置，而这些假设难以独立验证。交互式证明系统可以提供无条件的数学保证，但此前针对通用电路的交互式证明协议往往导致证明方的开销比原始计算高出数个量级。Thaler [18] 指出，特定类型的计算（如算术电路）能够支持高效的交互式证明。本文在此基础上设计了 SafetyNets——首个面向可表示为算术电路的深度神经网络的专用交互式证明协议，使客户端能够以极低的额外开销验证推理结果的正确性。

### 相关工作

[5] Cormode 等. Verifying computations with streaming interactive proofs. **VLDB 2011** [Google Scholar](https://scholar.google.com/scholar?q=Verifying+computations+with+streaming+interactive+proofs)
> 核心思路：提出流式交互证明，支持对数据流上函数的多轮验证。
> 局限与区别：该框架未针对深度神经网络的结构进行优化，直接应用会导致通信和计算开销过高。

[8] Gilad-Bachrach 等. Cryptonets: Applying neural networks to encrypted data with high throughput and accuracy. **ICML 2016** [Google Scholar](https://scholar.google.com/scholar?q=Cryptonets%3A+Applying+neural+networks+to+encrypted+data+with+high+throughput+and+accuracy)
> 核心思路：使用同态加密在加密数据上执行神经网络推理，保护数据隐私。
> 局限与区别：CryptoNets 不提供完整性保证，且客户端与服务器的计算开销均远高于 SafetyNets，例如 MNIST 上客户端耗时约 600 秒。

[9] Goldwasser 等. Delegating computation: interactive proofs for muggles. **STOC 2008** [Google Scholar](https://scholar.google.com/scholar?q=Delegating+computation%3A+interactive+proofs+for+muggles)
> 核心思路：提出 GKR 协议，利用 sum-check 协议验证分层算术电路的输出。
> 局限与区别：GKR 针对通用电路，未针对神经网络中矩阵乘法和二次激活的特定结构做优化，导致证明方开销较高。

[13] Lund 等. Algebraic methods for interactive proof systems. **JACM 1992** [Google Scholar](https://scholar.google.com/scholar?q=Algebraic+methods+for+interactive+proof+systems)
> 核心思路：提出 sum-check 协议，用于验证多项式求和问题。
> 局限与区别：sum-check 是构建所有后续交互式证明系统的基础工具，但单独使用无法直接高效验证神经网络。

[18] Thaler. Time-optimal interactive proofs for circuit evaluation. **CRYPTO 2013** [Google Scholar](https://scholar.google.com/scholar?q=Time-optimal+interactive+proofs+for+circuit+evaluation)
> 核心思路：给出针对“规则”算术电路的时间最优交互证明，特别是对矩阵乘法的高效 sum-check 协议。
> 局限与区别：Thaler 的协议未处理非线性激活层，本文将其与二次激活专用协议组合，实现端到端可验证。

[19] Vu 等. A hybrid architecture for interactive verifiable computation. **S&P 2013** [Google Scholar](https://scholar.google.com/scholar?q=A+hybrid+architecture+for+interactive+verifiable+computation)
> 核心思路：提出混合架构，将交互证明与验证计算结合，降低客户端负担。
> 局限与区别：该架构未针对神经网络中常见的稀疏矩阵（卷积）或非线性激活做专门设计。

[21] Walfish 等. Verifying computations without reexecuting them. **CACM 2015** [Google Scholar](https://scholar.google.com/scholar?q=Verifying+computations+without+reexecuting+them)
> 核心思路：综述验证计算技术，分析交互与非交互协议的优缺点。
> 局限与区别：本文在此基础上选择了交互式证明路线，并针对神经网络场景实现了具体化。

### 核心技术与方案

SafetyNets 的整体框架基于交互式证明系统，其中服务器扮演证明方，客户端扮演验证方。协议的核心是将深度神经网络的每一层表示为对有限域 $\mathbb{F}_p$ 上元素的算术操作，然后使用 sum-check 协议递归地验证从输出层到输入层的计算结果。为了支持这一递归，SafetyNets 首先将网络的参数和中间张量表示为多重线性扩展。例如，权重矩阵 $\mathbf{w}\in\mathbb{F}_p^{n\times n}$ 可被表示为函数 $W:\{0,1\}^m\times\{0,1\}^m\to\mathbb{F}_p$，其多重线性扩展 $\tilde{W}:\mathbb{F}_p^m\times\mathbb{F}_p^m\to\mathbb{F}_p$ 在单位超立方体上与 $W$ 一致且每个变量上为 1 次。SafetyNets 要求客户端验证输出层之前的线性变换结果 $\mathbf{z}_{L-1}$（而非最终的 softmax 输出），因为 softmax 不满足算术电路限制。客户端可以在本地由 $\mathbf{z}_{L-1}$ 计算出最终的分类结果。

验证过程从 $\mathbf{z}_{L-1}$ 开始。客户端随机选取点 $\mathbf{q}_{L-1}\in\mathbb{F}_p^{\log(n_L)}$ 和 $\mathbf{r}_{L-1}\in\mathbb{F}_p^{\log(b)}$，要求证明方提供 $\tilde{Z}_{L-1}(\mathbf{q}_{L-1},\mathbf{r}_{L-1})$ 的值。该值正确的证明被归约为对矩阵乘法层和二次激活层的 sum-check 协议。具体地，对于矩阵乘法 $\mathbf{z}_i = \mathbf{w}_i \mathbf{y}_i$，有
$$
\tilde{Z}_i(\mathbf{q}_i,\mathbf{r}_i) = \sum_{\mathbf{j}\in\{0,1\}^{\log(n_i)}} \tilde{W}_i(\mathbf{q}_i,\mathbf{j})\cdot \tilde{Y}_i(\mathbf{j},\mathbf{r}_i),
$$
这与 sum-check 协议的标准形式一致，因此可以利用 Thaler [18] 的协议进行验证。该 sum-check 协议需要 $\log(n_i)$ 轮，每轮证明方发送一个一元多项式。最终验证方得到关于 $\tilde{W}_i$（可由客户端本地计算）和 $\tilde{Y}_i$ 的断言。

对于二次激活层 $\mathbf{y}_i = \sigma_{\text{quad}}(\mathbf{z}_{i-1})$，SafetyNets 设计了专用的 sum-check 协议。注意到激活函数是逐元素平方，因此
$$
\tilde{Y}_i(\mathbf{s}_i,\mathbf{r}_i) = \sum_{\mathbf{j}\in\{0,1\}^{\log(n_i)},\ \mathbf{k}\in\{0,1\}^{\log(b)}} \tilde{I}(\mathbf{s}_i,\mathbf{j})\tilde{I}(\mathbf{r}_i,\mathbf{k})\ \tilde{Z}_{i-1}^2(\mathbf{j},\mathbf{k}),
$$
其中 $\tilde{I}$ 是单位矩阵的多重线性扩展。该求和形式同样适用 sum-check 协议，共 $2\log(n_i b)$ 轮。协议结束后，验证方获得关于 $\tilde{Z}_{i-1}$ 的断言，进而递归到下一层（矩阵乘法层）。

上述递归持续进行，直到到达输入层，此时验证方在本地计算 $\tilde{X}$ 并检验断言。如果任一 sum-check 实例失败，则验证方拒绝。整个协议利用了 Thaler 矩阵乘法协议和 SafetyNets 二次激活协议的组合，实现了端到端的可验证性。根据 Lemma 3.1，验证方拒绝错误计算的概率至少为 $1-\epsilon$，其中 soundness error $\epsilon = \tfrac{3b\sum_{i=0}^{L} n_i}{p}$。在实际参数和素域 $p=2^{61}-1$ 下，$\epsilon<2^{-30}$，可以忽略。

渐进复杂度方面：对于 layer $i$ 的矩阵乘法协议，证明方计算量为 $O(n_i(n_{i-1}+b))$，验证方为 $O(n_i n_{i-1})$，通信量为 $4\log(n_i)$ 个域元素。对于二次激活协议，证明方计算量为 $O(b n_i)$，验证方为 $O(\log(b n_i))$，通信量为 $5\log(b n_i)$ 个域元素。整个协议的总带宽通常低于 8 KB，远小于传输输入输出所需的带宽。

### 核心公式与流程

**[多层神经网络模型]**
$$
\begin{aligned}
\mathbf{y}_i &= \sigma_{\text{quad}}(\mathbf{w}_{i-1}\mathbf{y}_{i-1}+\mathbf{b}_{i-1}\mathbf{1}^T),\quad i\in[1,L-1], \\
\mathbf{y}_L &= \sigma_{\text{out}}(\mathbf{w}_{L-1}\mathbf{y}_{L-1}+\mathbf{b}_{L-1}\mathbf{1}^T).
\end{aligned}
$$
> 作用：定义本文可验证的网络结构，限定激活函数为二次函数，输出层可用任意函数（最终由客户端本地计算）。

**[Sum-check 协议基础]**
$$
y = \sum_{x_1\in\{0,1\}}\sum_{x_2\in\{0,1\}}\cdots\sum_{x_n\in\{0,1\}} g(x_1,x_2,\ldots,x_n).
$$
> 作用：证明方声称所有 $2^n$ 个点上的求和为 $y$，验证方通过多轮交互以压倒性概率检验该声明的正确性。

**[矩阵乘法的 sum-check 表示]**
$$
\tilde{Z}_i(\mathbf{q}_i,\mathbf{r}_i) = \sum_{\mathbf{j}\in\{0,1\}^{\log(n_i)}} \tilde{W}_i(\mathbf{q}_i,\mathbf{j})\cdot \tilde{Y}_i(\mathbf{j},\mathbf{r}_i).
$$
> 作用：将验证 $\mathbf{z}_i=\mathbf{w}_i\mathbf{y}_i$ 的断言转化为 sum-check 实例，从而利用 Thaler 的协议进行高效验证。

**[二次激活的 sum-check 表示]**
$$
\tilde{Y}_i(\mathbf{s}_i,\mathbf{r}_i) = \sum_{\mathbf{j}\in\{0,1\}^{\log(n_i)},\ \mathbf{k}\in\{0,1\}^{\log(b)}} \tilde{I}(\mathbf{s}_i,\mathbf{j})\tilde{I}(\mathbf{r}_i,\mathbf{k})\ \tilde{Z}_{i-1}^2(\mathbf{j},\mathbf{k}).
$$
> 作用：将验证二次激活输出 $\mathbf{y}_i=\mathbf{z}_{i-1}^2$ 的断言转化为 sum-check 实例，是 SafetyNets 专门设计的核心协议。

**[Soundness error 上界]**
$$
\epsilon = \frac{3b\sum_{i=0}^{L} n_i}{p}.
$$
> 作用：给出整个协议的安全参数，表明通过选择足够大的素数 $p$（如 $2^{61}-1$）可使错误概率可忽略不计。

### 实验结果

实验在 Intel Core i7-4600U CPU 上进行，测试了三个分类任务：MNIST 手写数字识别、MNIST-Back-Rand（随机背景变体）和 TIMIT 语音识别。网络结构为 CNN-2-Quad（两层卷积+二次激活+求和池化）和 FcNN-3-Quad（三层全连接+二次激活）。与使用 ReLU 的对应网络相比，二次激活网络在测试精度上具有竞争力：MNIST 达到 99.4%，TIMIT 达到 75.22%（与现有最优结果相当）。在性能方面，对于 FcNN-3-Quad 网络，客户端的验证时间比本地执行快 8 倍到 82 倍，并且随着批处理量增大，加速比进一步增加。服务器的额外开销（生成证明的时间）仅为基线执行时间的 5% 以内。交互协议的总带宽小于 8 KB（批处理量 2048 时），远小于传输输入输出所需的通信量。安全参数方面，所有设置下的 soundness error $\epsilon$ 均小于 $2^{-30}$。与 CryptoNets [8] 相比，SafetyNets 的客户端耗时（MNIST 上小于 10 秒）远低于 CryptoNets 的约 600 秒，且无需处理高成本的同态加密。

### 局限性与开放问题

SafetyNets 要求网络激活函数为二次函数、池化为求和池化，不能直接支持 ReLU 或 max 池化，这限制了其应用范围。此外，网络中的输入、权重和中间值必须量化为有限域元素，量化误差可能影响精度，需要仔细选择缩放因子。当前方案仅保证完整性而不保护隐私，未来工作可以结合 Pinocchio [17] 等非交互式验证技术同时实现隐私与完整性，或设计专用的硬件加速器以降低证明开销。对于更深层的网络，sum-check 协议的递归轮数线性增长，通信和计算开销仍需进一步优化。

### 强关联论文

[5] Cormode 等. Verifying computations with streaming interactive proofs. **VLDB 2011** [Google Scholar](https://scholar.google.com/scholar?q=Verifying+computations+with+streaming+interactive+proofs)

[8] Gilad-Bachrach 等. Cryptonets: Applying neural networks to encrypted data with high throughput and accuracy. **ICML 2016** [Google Scholar](https://scholar.google.com/scholar?q=Cryptonets%3A+Applying+neural+networks+to+encrypted+data+with+high+throughput+and+accuracy)

[9] Goldwasser 等. Delegating computation: interactive proofs for muggles. **STOC 2008** [Google Scholar](https://scholar.google.com/scholar?q=Delegating+computation%3A+interactive+proofs+for+muggles)

[13] Lund 等. Algebraic methods for interactive proof systems. **JACM 1992** [Google Scholar](https://scholar.google.com/scholar?q=Algebraic+methods+for+interactive+proof+systems)

[18] Thaler. Time-optimal interactive proofs for circuit evaluation. **CRYPTO 2013** [Google Scholar](https://scholar.google.com/scholar?q=Time-optimal+interactive+proofs+for+circuit+evaluation)

[19] Vu 等. A hybrid architecture for interactive verifiable computation. **S&P 2013** [Google Scholar](https://scholar.google.com/scholar?q=A+hybrid+architecture+for+interactive+verifiable+computation)

[21] Walfish 等. Verifying computations without reexecuting them. **CACM 2015** [Google Scholar](https://scholar.google.com/scholar?q=Verifying+computations+without+reexecuting+them)


## 关键词

+ 深度神经网络可验证推断
+ 交互式证明协议
+ 算术电路
+ 不可信云计算
+ ZK-SNARK应用
+ 机器学习安全性