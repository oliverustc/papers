---
title: "An Efficient and Extensible Zero-knowledge Proof Framework for Neural Networks"
标题简称:
论文类型: preprint
预印本简称: archive
发表年份: 2024
modified: 2025-04-11 12:06:14
---

## An Efficient and Extensible Zero-knowledge Proof Framework for Neural Networks

## 发表信息

+ [原文链接](https://eprint.iacr.org/2024/703)

## 作者

+ 

## 笔记

### 背景与动机

在机器学习的云服务模式中，客户将数据提交给云服务商，由后者使用其专有的神经网络模型进行推理并返回结果。然而，由于模型被视为知识产权，客户无法验证返回结果的正确性。懒惰或恶意的服务商可能提供错误的计算结果，这在医疗等安全攸关领域是不可接受的。零知识证明为解决这一问题提供了密码学手段，它允许服务商（证明者）在不泄露模型参数的前提下，证明推理结果是正确计算的。尽管已有大量工作致力于为神经网络构建零知识证明，但这些方案的计算开销极高，尤其是针对神经网络中的非线性层。例如，现有方案 zkCNN [40] 为 VGG-11 [53] 网络的单张图片推理生成证明需要超过 50 秒，而 Mystique [60] 为非线性层生成证明的时间超过总运行时间的 90%。此外，随着大语言模型时代的到来，Transformer 网络（如 GPT [48, 49]）变得越来越重要，但大多数现有方案无法扩展到处理其复杂的非线性层（如 Softmax 和 GELU）。虽然 Mystique [60] 和 ZKML [10] 能够为这些复杂非线性层生成证明，但其为 GPT-2 [49] 生成证明需要数小时。因此，非线性层证明的效率和可扩展性是当前构建实用神经网络零知识证明系统的两大核心挑战。

### 相关工作

[10] Chen等. ZKML: An Optimizing System for ML Inference in Zero-Knowledge Proofs. **EuroSys 2024** [Google Scholar](https://scholar.google.com/scholar?q=ZKML%3A+An+Optimizing+System+for+ML+Inference+in+Zero-Knowledge+Proofs)
> 核心思路：利用 Halo2 [67] 作为 ZKP 后端，支持 Transformer 神经网络的推理证明。
> 局限与区别：生成 GPT-2 [49] 的证明需要数小时，计算开销巨大。

[60] Weng等. Mystique: Efficient conversions for {Zero-Knowledge} proofs with applications to machine learning. **USENIX Security 2021** [Google Scholar](https://scholar.google.com/scholar?q=Mystique%3A+Efficient+conversions+for+Zero-Knowledge+proofs+with+applications+to+machine+learning)
> 核心思路：基于 VOLE 的 ZKP 方案，为卷积神经网络提供了高效的线性层证明。
> 局限与区别：其非线性层证明依赖比特分解技术，导致超过 90% 的运行时间用于非线性层，且无法高效扩展到 Transformer 网络。

[40] Liu等. ZkCNN: Zero knowledge proofs for convolutional neural network predictions and accuracy. **CCS 2021** [Google Scholar](https://scholar.google.com/scholar?q=ZkCNN%3A+Zero+knowledge+proofs+for+convolutional+neural+network+predictions+and+accuracy)
> 核心思路：基于 GKR 协议 [25] 的 ZKP 方案，专注于卷积神经网络的证明。
> 局限与区别：方案主要针对 CNN，难以扩展到包含不同非线性层的 Transformer 网络。

[29] Hao等. Scalable Zero-knowledge Proofs for Non-linear Functions in Machine Learning. **2024** [Google Scholar](https://scholar.google.com/scholar?q=Scalable+Zero-knowledge+Proofs+for+Non-linear+Functions+in+Machine+Learning)
> 核心思路：利用基于 ZK-RAM [64] 的查找证明来构建非线性层证明。
> 局限与区别：其方案因缺乏兼容性，无法直接部署到实践中的现有神经网络上。

[54] Sun等. zkLLM: Zero Knowledge Proofs for Large Language Models. **2024** [Google Scholar](https://scholar.google.com/scholar?q=zkLLM%3A+Zero+Knowledge+Proofs+for+Large+Language+Models)
> 核心思路：为 Transformer 神经网络定制的 GPU 加速方案。
> 局限与区别：本文目标是提供一个适用于各种神经网络的 CPU 上的高效可扩展框架。

[8] Bünz等. Bulletproofs: Short proofs for confidential transactions and more. **IEEE S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Bulletproofs%3A+Short+proofs+for+confidential+transactions+and+more)
> 核心思路：基于比特分解的经典范围证明方案。
> 局限与区别：其证明计算开销大，不适用于本文需要处理数百万次范围证明的场景。

[19] Gabizon等. plookup: A simplified polynomial protocol for lookup tables. **ePrint 2020** [Google Scholar](https://scholar.google.com/scholar?q=plookup%3A+A+simplified+polynomial+protocol+for+lookup+tables)
> 核心思路：基于多项式承诺的查找证明，适用于小规模查找表。
> 局限与区别：虽然通信量小，但证明者的计算开销显著高于本文的 VOLE 基方案。

### 核心技术与方案

本文提出了一个基于向量不经意线性评估的零知识证明框架，旨在高效、可扩展地为神经网络推理生成可验证证明。该框架采用模块化设计，主要包括两个基础模块：范围证明和查找证明，以及基于这两个模块构建的非线性操作约束。

**基础模块一：改进的范围证明。** 该模块用于证明一个秘密值 $x$ 在区间 $[0, B]$ 内。其核心基于 Legendre 三平方定理，即一个整数 $x$ 属于 $[0, B]$ 当且仅当存在三个整数 $y_1, y_2, y_3$ 满足 $4x(B-x)+1 = y_1^2 + y_2^2 + y_3^2$。为了高效地找到这三个整数，本文改进了 Rabin 和 Shallit [47] 的搜索方法。具体步骤是：首先找到最大的偶整数 $y_1$，使得 $4x(B-x)+1 = y_1^2 + q$，且 $q$ 为素数。然后，根据 Fermat 平方和定理，当 $q \equiv 1 \pmod{4}$ 时，素数 $q$ 可表示为两个平方数之和，记为 $q = y_2^2 + y_3^2$，这可以通过查询预计算表高效获得，从而实现期望时间复杂度从 $O(b^2)$ 降至 $O(b)$，其中 $b$ 是 $x$ 的比特长度。为防止有限域上的回绕现象，证明者与验证者需运行一个短小测试，通过多次随机线性组合检查 $x, y_1, y_2, y_3$ 是否足够小。整个协议通过多项式证明了 $4x(B-x)+1 = y_1^2 + y_2^2 + y_3^2$ 在整数上的成立，并利用掩码方案和安全性博弈证明，其纠错率至多为 $R/L$，统计安全错误至多为 $1/p + 1/2^R$。

**基础模块二：改进的查找证明。** 该模块用于证明一个秘密向量 $\mathbf{X}$ 中的所有元素都属于一个公开的表 $\mathbf{T}$。其核心是利用子集引理 [19]，即证明多项式 $g(\alpha, \beta, \gamma)$ 和 $h(\alpha, \beta, \gamma)$ 等价。其中，$g$ 由 $\mathbf{X}$ 和 $\mathbf{T}$ 定义，$h$ 由集合 $\mathbf{S}$（即 $\mathbf{X}$ 和 $\mathbf{T}$ 的并集并按 $\mathbf{T}$ 中的顺序排序）定义。证明者首先需要计算出 $\mathbf{S}$。由于在本文场景中 $\mathbf{X}$ 的元素只有少量不同值，优化地，证明者通过将具有相同值的元素分组，可以在 $O(n)$ 时间内完成排序，其中 $n$ 是查找元素个数。随后，验证者随机选取三个随机数 $(r_1, r_2, r_3)$ 作为参数，若两个多项式等价，则 $l(r_1, r_2, r_3) = g(r_1, r_2, r_3) - h(r_1, r_2, r_3) = 0$。最后，双方利用一个多项式证明语句验证这个求值结果为零。该协议在 $\mathcal{F}_{\mathrm{authZK}}$ 混合模型下，以统计可靠性误差至多为 $(n+d)(w+1)/p$ 实现了 UC 安全，其中 $d$ 是表大小，$w$ 是表元素的维度。

**非线性操作约束的构建。** 本文利用上述范围和查找证明作为基础，将非线性层中的复杂计算转换为一系列范围和指数关系。例如，对于右移操作 $m = q \gg b$，只需要一个范围关系 $0 \leq q - m 2^b \leq 2^b - 1$ 即可唯一约束其正确性，相比于需要数百个关系的比特分解方法，实现了约两个数量级的约束数量减少。对于ReLU、MaxPooling、AvgPooling、Softmax、GELU、Normalization等层，本文通过组合多个原始操作（如 max, min, 符号, 绝对值, 移位, 取整, 除法取整）的约束来构建其对应的零知识证明。例如，Normalization 层通过将计算分解为求均值、求方差、求标准差和一系列基于取整操作的除法与开方，每个步骤都对应为文档表1中列出的原始操作的约束。为确保约束的唯一性和正确性，文档证明了在给定范围关系下，满足约束的解是唯一的。

**整体框架组装。** 整个框架将非线性层转换为范围和指数约束，并通过范围证明和查找证明来验证其满足性。线性层（如卷积、全连接层）的计算本质是矩阵乘法，其证明直接利用前人工作中的多项式证明。框架在 UC 安全模型下，通过组合各层的过程来构建整个网络的证明。同时，为了让证明与浮点运算兼容，框架将浮点数近似为整数或定点数，例如通过 $x = S(q - Z)$ 将浮点数映射为 Q-bit 整数，并兼容了如 IBert [37] 中描述的近似方法，以最小化精度损失。

### 核心公式与流程

**[范围证明核心引理]**
$$
\forall x \in [0, B], \exists y_1, y_2, y_3 \in \mathbb{Z} \text{ s.t. } 4x(B-x)+1 = y_1^2 + y_2^2 + y_3^2
$$
> 作用：将范围证明问题转化为证明一个等式成立的问题。证明者只需找到这三个整数，并证明该等式成立以及各值在有限域上无回绕，即可完成证明。

**[查找证明核心引理（子集引理）]**
$$ 
g(\alpha,\beta,\gamma) := (1+\beta)^n \cdot \prod_{i=1}^n \left(\gamma + \sum_{k=1}^w \alpha^{k-1}x_{ik}\right) \cdot \prod_{i=1}^{d-1} \left(\gamma(1+\beta) + \sum_{k=1}^w \alpha^{k-1}(t_{ik} + \beta t_{(i+1)k})\right)  
$$
$$ 
h(\alpha,\beta,\gamma) := \prod_{i=1}^{n+d-1} \left(\gamma(1+\beta) + \sum_{k=1}^w \alpha^{k-1}(s_{ik} + \beta s_{(i+1)k})\right)  
$$
> 作用：这两个多项式的等价性完全等价于集合 $\mathbf{X} = \{x_i\}$ 是集合 $\mathbf{T} = \{t_j\}$ 的子集，且集合 $\mathbf{S} = \{s_i\}$ 是两者并集在 $\mathbf{T}$ 上的排序。这构成了查找证明的基础，证明者需构建 $\mathbf{S}$ 并证明多项式的等价性。

**[非线性操作约束示例：右移操作]**
$$
0 \leq q - m \cdot 2^b \leq 2^b - 1
$$
> 作用：对于整数 $q$ 的 $b$ 位右移操作 $m = q \gg b$，这个范围关系唯一地约束了结果 $m$ 的正确性。与比特分解形成对比，它仅用一个范围关系和应满足的指数关系就完成了证明，极大降低了约束数量。

### 实验结果

实验在配备 AMD Ryzen 3700X CPU 和 32GB 内存的机器上进行，使用 254 比特域，达到 128 比特计算安全和 40 比特统计安全。对于**范围证明**，当证明 $2^{18}$ 个元素在 $[0, 2^{24}]$ 内时，本文方案证明者耗时 287ms，验证者耗时 142ms，分别比 Bulletproofs [8] 快 847 倍和 75 倍，比 Lasso [51] 快 7.5 倍和 0.76 倍。对于**查找证明**，当证明 $2^{18}$ 个元素属于一个公开表时，本文方案证明者耗时 1066ms，比 Plookup [19] 快 115 倍。对于**非线性层**，与 Mystique [60] 相比，本文方案在 ReLU、Softmax、GELU 和 Normalization 层上分别实现了 477 倍、582 倍、1173 倍和 995 倍的加速比。对于**整体网络**的证明，本文方案为 ResNet-101 网络生成证明仅耗时 9.5 秒，比 Mystique [60] 快 41.4 倍；为 GPT-2 模型（1.17 亿参数）生成证明总时长为 287.1 秒，比 ZKML [10] 快 35.7 倍。在精度方面，本文方案在 CIFAR-10 上的 ResNet-101 模型准确率达到 93.79%，与原始网络相差仅 0.04%；对于 GPT-2 模型，输出余弦相似度达到 99.95%。

### 局限性与开放问题

本文方案虽然显著提升了现有 ZKP 系统的性能，但它仍缺乏 GPU 加速能力，这限制了其在更大规模模型上的潜在性能上限。框架依赖于将浮点运算近似为整数运算，这虽然在文中报告了高精度，但在一些对精度极其敏感的领域可能仍不适用。此外，当前的框架主要是为推理过程设计的，是否可以高效、可扩展地扩展到证明模型的训练过程是未来的一个重要挑战。

### 强关联论文

[10] Chen et al. ZKML: An Optimizing System for ML Inference in Zero-Knowledge Proofs. **EuroSys 2024** [Google Scholar](https://scholar.google.com/scholar?q=ZKML%3A+An+Optimizing+System+for+ML+Inference+in+Zero-Knowledge+Proofs)

[19] Gabizon and Williamson. plookup: A simplified polynomial protocol for lookup tables. **ePrint 2020** [Google Scholar](https://scholar.google.com/scholar?q=plookup%3A+A+simplified+polynomial+protocol+for+lookup+tables)

[29] Hao et al. Scalable Zero-knowledge Proofs for Non-linear Functions in Machine Learning. **2024** [Google Scholar](https://scholar.google.com/scholar?q=Scalable+Zero-knowledge+Proofs+for+Non-linear+Functions+in+Machine+Learning)

[40] Liu et al. ZkCNN: Zero knowledge proofs for convolutional neural network predictions and accuracy. **CCS 2021** [Google Scholar](https://scholar.google.com/scholar?q=ZkCNN%3A+Zero+knowledge+proofs+for+convolutional+neural+network+predictions+and+accuracy)

[47] Rabin and Shallit. Randomized algorithms in number theory. **Communications on Pure and Applied Mathematics 1986** [Google Scholar](https://scholar.google.com/scholar?q=Randomized+algorithms+in+number+theory)

[51] Setty et al. Unlocking the lookup singularity with Lasso. **ePrint 2023** [Google Scholar](https://scholar.google.com/scholar?q=Unlocking+the+lookup+singularity+with+Lasso)

[60] Weng et al. Mystique: Efficient conversions for {Zero-Knowledge} proofs with applications to machine learning. **USENIX Security 2021** [Google Scholar](https://scholar.google.com/scholar?q=Mystique%3A+Efficient+conversions+for+Zero-Knowledge+proofs+with+applications+to+machine+learning)

[63] Yang et al. Quicksilver: Efficient and affordable zero-knowledge proofs for circuits and polynomials over any field. **CCS 2021** [Google Scholar](https://scholar.google.com/scholar?q=Quicksilver%3A+Efficient+and+affordable+zero-knowledge+proofs+for+circuits+and+polynomials+over+any+field)


## 关键词

+ 神经网络零知识证明框架
+ 非线性层范围指数关系约束
+ 卷积Transformer神经网络ZKP
+ 云端模型推断可验证性
+ 模块化ZKP框架高效可扩展