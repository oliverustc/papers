---
title: "zkCNN: Zero Knowledge Proofs for Convolutional Neural Network Predictions and Accuracy"
标题简称: zkCNN
论文类型: conference
会议简称: CCS
发表年份: 2021
modified: 2025-04-08 09:59:55
---

## zkCNN: Zero Knowledge Proofs for Convolutional Neural Network Predictions and Accuracy

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3460120.3485379)
+ [code](https://github.com/TAMUCrypto/zkCNN)
+ 

## 作者

+ [Tianyi Liu](Tianyi%20Liu.md)
+ [Xiang Xie](Xiang%20Xie.md)
+ [Yupeng Zhang](Yupeng%20Zhang.md)

## 笔记

### 背景与动机

深度神经网络，特别是卷积神经网络，在众多机器学习任务中取得了显著成功，但随之而来的是模型预测结果的完整性验证问题。在许多实际场景中，用户需要确信推理结果确实是由一个合法且具有高准确率的模型计算得出的，这被称为机器学习预测的完整性。最直接的解决方案是公开模型，但模型通常由敏感数据训练而来，是所有者重要的知识产权，实践中无法分享。通用零知识证明方案虽可用于任何算术电路计算，但它们在证明者端引入了巨大的计算开销，无法扩展到现实世界中大规模CNN模型的规模。因此，迫切需要一种针对CNN设计的高效零知识证明方案，既能保护模型参数隐私，又能确保预测结果的正确性。

### 相关工作

[20] Graham Cormode等. Practical Verified Computation with Streaming Interactive Proofs. **ITCS 2012** [Google Scholar](https://scholar.google.com/scholar?q=Practical+Verified+Computation+with+Streaming+Interactive+Proofs)
> 核心思路：改进了GKR协议，将证明者时间从$O(|C|^3)$降低到$O(|C|\log|C|)$。
> 局限与区别：该工作针对通用电路，未利用CNN中卷积操作的结构化特性，本文通过为FFT设计新的求和检查协议，将证明者时间优化至$O(n^2)$，优于计算FFT的$O(n\log n)$。

[23] Boyuan Feng等. ZEN: Efficient Zero-Knowledge Proofs for Neural Networks. **ePrint 2021** [Google Scholar](https://scholar.google.com/scholar?q=ZEN:+Efficient+Zero-Knowledge+Proofs+for+Neural+Networks)
> 核心思路：提出一种对零知识证明友好的量化技术来处理实数。
> 局限与区别：ZEN仍基于SNARK，其证明者时间开销很大，本文的证明时间是其213倍以上。本文采用了更简单的量化方案[28]，并指出ZEN的量化技术可以兼容。

[25] Zahra Ghodsi等. SafetyNets: Verifiable Execution of Deep Neural Networks on an Untrusted Cloud. **NeurIPS 2017** [Google Scholar](https://scholar.google.com/scholar?q=SafetyNets:+Verifiable+Execution+of+Deep+Neural+Networks+on+an+Untrusted+Cloud)
> 核心思路：使用GKR协议证明神经网络推理的正确性。
> 局限与区别：该方案假设模型和数据对双方都公开，本质是验证计算，不提供隐私保护，而本文实现了零知识。

[26] Shafi Goldwasser等. Delegating Computation: Interactive Proofs for Muggles. **J. ACM 2015** [Google Scholar](https://scholar.google.com/scholar?q=Delegating+Computation:+Interactive+Proofs+for+Muggles)
> 核心思路：提出了著名的GKR协议，用于分层算术电路的双效交互式证明。
> 局限与区别：原始GKR协议的证明者时间较高。本文在其基础上进行推广，引入了广义门、任意层输入等改进，并针对CNN结构设计了专用协议。

[34] Seunghwa Lee等. vCNN: Verifiable Convolutional Neural Network based on zk-SNARKs. **ePrint 2020** [Google Scholar](https://scholar.google.com/scholar?q=vCNN:+Verifiable+Convolutional+Neural+Network+based+on+zk-SNARKs)
> 核心思路：通过将卷积转化为多项式乘法，并利用QAP和多项式QAP来验证。
> 局限与区别：vCNN的证明者时间非常慢，尤其在大型网络上。本文通过直接对卷积使用求和检查协议，证明者速度快了1264倍（VGG16）。

[35] Carsten Lund等. Algebraic Methods for Interactive Proof Systems. **J. ACM 1992** [Google Scholar](https://scholar.google.com/scholar?q=Algebraic+Methods+for+Interactive+Proof+Systems)
> 核心思路：提出了求和检查协议，用于高效地验证一个多元多项式在布尔超立方体上所有点值的和。
> 局限与区别：本文以该协议为基石，并为其设计了针对FFT的全新算法，使得证明者时间达到线性，并在卷积验证中应用。

[39] Srinath Setty. Spartan: Efficient and general-purpose zkSNARKs without trusted setup. **CRYPTO 2020** [Google Scholar](https://scholar.google.com/scholar?q=Spartan:+Efficient+and+general-purpose+zkSNARKs+without+trusted+setup)
> 核心思路：提出了一种基于离散对数假设、无需可信设置的高效多项式承诺方案。
> 局限与区别：本文直接采用了该多项式承诺方案来实现对CNN模型和辅助输入的承诺，并将其与改进的GKR协议结合，构建完整的零知识论证系统。

[41] Justin Thaler. Time-Optimal Interactive Proofs for Circuit Evaluation. **CRYPTO 2013** [Google Scholar](https://scholar.google.com/scholar?q=Time-Optimal+Interactive+Proofs+for+Circuit+Evaluation)
> 核心思路：提出了一个用于矩阵乘法的求和检查协议，其证明者时间是$O(n^2)$，快于计算结果的$O(n^3)$。
> 局限与区别：本文借鉴了其“线性证明者时间”的思想，但本文的创新在于为FFT设计了类似的线性时间求和检查协议，这是实现高效卷积验证的关键。

[51] Jiaheng Zhang等. Doubly Efficient Interactive Proofs for General Arithmetic Circuits with Linear Prover Time. **ePrint 2020** [Google Scholar](https://scholar.google.com/scholar?q=Doubly+Efficient+Interactive+Proofs+for+General+Arithmetic+Ciruits+with+Linear+Prover+Time)
> 核心思路：提出了一种GKR协议的变体，允许门从任意层（而非仅仅上一层）接收输入，且不增加证明者时间。
> 局限与区别：本文将该技术与广义门结合，设计了一个高效的CNN电路，其中卷积层和全连接层可以直接连接到输入层的模型参数，避免了参数在电路中层层传递的开销。

[52] Jiaheng Zhang等. Transparent Polynomial Delegation and Its Applications to Zero Knowledge Proof. **S&P 2020** [Google Scholar](https://scholar.google.com/scholar?q=Transparent+Polynomial+Delegation+and+Its+Applications+to+Zero+Knowledge+Proof)
> 核心思路：利用交互式证明和多项式承诺构造零知识论证系统。
> 局限与区别：本文采用了相似的框架，但本文的核心贡献在于为框架中的最核心计算模块——卷积——提供了全新的、高效的求和检查协议。

### 核心技术与方案

本文构建的zkCNN系统是一个基于交互式证明和多项式承诺的零知识论证方案。其整体框架遵循“证明者首先生成证据（CNN参数）的承诺，然后与验证者运行多方次交互式证明，最终将预测正确性的验证归结为对承诺的少量求值”。方案的创新核心在于以下几个层次：

**1. 针对FFT的新求和检查协议**

验证卷积最有效的方式是通过FFT。标准求和检查协议若直接用于验证等式 $\tilde{a}(y) = \sum_{x \in \{0,1\}^{\log N}} \tilde{c}(x) \tilde{F}(y, x)$，计算表$\tilde{F}(u, x)$（$\tilde{F}$是傅里叶矩阵的多线性扩展）的朴素方法需要$O(NM)$时间。本文的关键洞察在于，利用$\tilde{F}(u, x)$的封闭形式：$\tilde{F}(u, x) = \prod_{i=0}^{\log M -1} ((1-u_i) + u_i \cdot \omega_{2^{i+1}}^{\chi})$，其中$\omega_{2^{i+1}}$是$2^{i+1}$次单位根。这个公式使得证明者可以通过一个迭代过程（Algorithm 2），在$O(M+N)$时间内计算出所有$\tilde{F}(u,x)$的值。结合动态规划方法（Algorithm 1），整个求和检查协议的证明者时间降低至$O(N)$，比计算FFT本身的$O(N \log N)$更快。协议的证明大小为$O(\log N)$，验证者时间为$O(\log N)$。若以增加证明大小至$O(\log^2 N)$为代价，可进一步将验证者时间降至$O(\log^2 N)$。

**2. 面向CNN的GKR协议推广**

为了高效处理CNN的复杂结构，本文对GKR协议进行了多项推广：
- **广义加法和乘法门**：定义了新的函数$a\tilde{d}d_i(z,x)$和$X\tilde{m}ult_i(z,x,y)$，允许一个加法门有多个输入，或直接表示内积。这使得原本需要多层加法树的求和操作（如全连接层中的向量间点积）能在单个求和检查中完成，将证明大小和门数量都减少了对数因子。
- **从任意层输入**：结合[51]的技术，修改后的GKR协议允许一个门（如卷积门）同时从上一层和电路的输入层（即模型参数W）接收数据。这避免了将模型参数作为输入层数据，在电路中层层传递至对应层的高昂开销。电路结构（如图2所示）使得卷积层、全连接层可以直接“指向”模型参数。
- **卷积层优化**：利用FFT的线性性质，将带有多个输入通道$ch_{in}$和输出通道$ch_{out}$的卷积计算重写为$\bar{U}_{\tau} = \operatorname{IFFT}\left(\sum_{\sigma=0}^{ch_{in}-1} \operatorname{FFT}(\bar{X}_{\sigma}) \odot \operatorname{FFT}(\bar{W}_{\tau,\sigma})\right)$。这使得IFFT的次数从$ch_{in} \cdot ch_{out}$降低到$ch_{out}$，显著提升了实际效率。

**3. 激活函数与池化的电路设计**

将ReLU和最大值池化等非线性操作实现为算术电路是zkCNN的一个关键挑战。
- **ReLU**：要求证明者为输入值$x$提供其绝对值$|x|$的比特分解和符号位$b_Q$。电路随后验证比特分解的正确性，并根据符号位输出$b_Q$乘以截断后的值。这确保了ReLU操作的零知识验证。
- **最大值池化与ReLU的组合**：对于$k$个值$x_0,...,x_{k-1}$，证明者直接提供结果$\bar{x}_{max} = \max\{ \text{ReLU}(x_0),...,\text{ReLU}(x_{k-1}) \}$作为辅助输入。验证者通过两个条件检查其正确性：(1) $\bar{x}_{max} - x_j \geq 0$对所有$j$成立（通过比特分解验证非负性）；(2) $\bar{x}_{max} \cdot \prod_{j=0}^{k-1} (\bar{x}_{max} - x_j) = 0$，确保$\bar{x}_{max}$要么是0，要么等于某个$x_j$。此设计仅比单个ReLU多了一个比特分解的开销。

**安全性证明**

该方案首先基于GKR协议和求和检查协议的可靠性，通过类似“层间归约”的标准论证确保预测结果的正确性。如果证明者提供了一个错误的预测，那么在协议的多轮交互中，它几乎必然会被验证者拒绝，除非它能伪造多项式承诺的打开结果。因此，最终方案的安全性归约到底层多项式承诺方案（[39]）的知识可靠性，该方案基于离散对数假设。通过引入零知识求和检查与低次扩展，可以将该交互式证明方案转化为零知识论证。

**系统复杂度**
在零知识版本中，证明者时间约为$O(\sum_i (n_i^2 \cdot ch_{in,i} \cdot ch_{out,i} + n_i^2 \cdot ch_{out,i} \cdot Q) + S_{in})$，其中$Q$是比特分解的位宽，$S_{in}$是输入（模型参数+辅助输入）的总大小。证明大小和验证者时间分别为$O(\sum_i \log^2(...) + \sqrt{S_{in}})$，其中$\sqrt{S_{in}}$项来自于多项式承诺。

### 核心公式与流程

**[FFT新求和检查的核心公式]**
$$
\tilde{F}(u, x) = \prod_{i=0}^{\log M-1} \left((1-u_i) + u_i \cdot \omega_{2^{i+1}}^{\chi}\right)
$$
> 作用：该公式是本文最重要理论贡献。它给出了傅里叶矩阵多线性扩展的闭式表达，将计算所有$\tilde{F}(u,x)$（$x$遍历布尔超立方体）的时间从$O(NM)$降至$O(N+M)$，从而使FFT求和检查的证明者时间达到线性。

**[二维卷积转换为一维卷积]**
$$
U_{j,k} = \sum_{t=0,l=0}^{w-1,w-1} X_{j+t,k+l}W_{t,l} = \bar{U}_{n^2-1-jn-k}
$$
> 作用：此公式展示了CNN中的二维卷积可以通过对输入和Kernel进行特定的重排（反序、补零、拉直），转化为标准的一维卷积。这是后续使用FFT实现高效验证的前提。

**[带多个通道的卷积层优化]**
$$
\bar{U}_{\tau} = \operatorname{IFFT}\left(\sum_{\sigma=0}^{ch_{in}-1} \operatorname{FFT}(\bar{X}_{\sigma}) \odot \operatorname{FFT}(\bar{W}_{\tau,\sigma})\right)
$$
> 作用：利用FFT的线性性，将多个通道的卷积结果在频域求和后再进行逆变换。这个公式使得IFFT的次数从$ch_{in} \cdot ch_{out}$减少到$ch_{out}$，有效降低了方案的计算开销。

**[广义GKR层间归约公式]**
$$
\tilde{V}_i(z) = \sum_{x} X\tilde{a}dd_i(z,x) \cdot \tilde{V}_{i+1}(x) + \sum_{x,y} X\tilde{m}ult_i(z,x,y) \cdot \tilde{V}_{i+1}(x)\tilde{V}_{i+1}(y)
$$
> 作用：这是GKR协议的核心，将层$i$的输出值通过一个二变量多项式联系起来。本文的推广在于重新定义了$X\tilde{a}dd$和$X\tilde{m}ult$函数，使其能够更灵活地表示具有多个输入的加法或内积操作，并能从不同层获取输入，从而高效地构建CNN电路。

### 实验结果

本文使用AMD EPYC 7R32 64核处理器和128GB内存的机器进行了实验。系统用C++实现，基于开源代码[48, 51, 52]和BLS12-381椭圆曲线。在单个CPU核心上运行。
- **性能数值**：对于拥有15.2M参数和16层的VGG16网络，zkCNN生成一个预测证明需要88.3秒，证明大小为341KB，验证时间仅为59.3毫秒。
- **与Baseline对比**：相比已有的方案vCNN [34]，zkCNN的证明者时间在LeNet上快了11.2倍，在VGG16上估计快了1264倍（vCNN在VGG16上估计需31小时）。相比ZEN [23]，在LeNet上快213倍。
- **FFT求和检查协议**：对大小为$2^{18}$的向量生成证明仅需0.1秒，比使用GKR于FFT电路的方法快33.2倍。
- **卷积验证**：对于256x256输入和64x64卷积核，其证明者时间（1.7秒）甚至比直接使用FFT计算卷积（0.97秒）慢约1.8倍，但比朴素实现快291倍，验证者时间仅0.3ms。
- **适用规模**：系统成功支撑了多个样本（如20张CIFAR-10图像）的预测准确性证明，证明时间为520秒，表明其具有一定的可扩展性。

### 局限性与开放问题

尽管结果显著，但zkCNN的内存使用是主要瓶颈，在VGG16上达到了24GB，限制了向更大规模或更多样本的扩展。此外，当前的零知识版本需要引入额外的归约技术，这会带来额外的开销，论文中未详细评估这部分性能。未来的工作可以探索如何优化内存使用，以及集成更先进的实数处理方案（如ZEN的量化技术）以提高通用性。目前方案仅保护模型参数，不保护网络结构，隐藏结构将是一个开放挑战。

### 强关联论文

[23] Boyuan Feng, Lianke Qin, Zhenfei Zhang, Yufei Ding, and Shumo Chu. ZEN: Efficient Zero-Knowledge Proofs for Neural Networks. **ePrint 2021** [Google Scholar](https://scholar.google.com/scholar?q=ZEN:+Efficient+Zero-Knowledge+Proofs+for+Neural+Networks)

[34] Seunghwa Lee, Hankyung Ko, Jihye Kim, and Hyunok Oh. vCNN: Verifiable Convolutional Neural Network based on zk-SNARKs. **ePrint 2020** [Google Scholar](https://scholar.google.com/scholar?q=vCNN:+Verifiable+Convolutional+Neural+Network+based+on+zk-SNARKs)

[41] Justin Thaler. Time-Optimal Interactive Proofs for Circuit Evaluation. **CRYPTO 2013** [Google Scholar](https://scholar.google.com/scholar?q=Time-Optimal+Interactive+Proofs+for+Circuit+Evaluation)

[48] Tiacheng Xie, Jiaheng Zhang, Yupeng Zhang, Charalampos Papamanthou, and Dawn Song. Libra: Succinct Zero-Knowledge Proofs with Optimal Prover Computation. **CRYPTO 2019** [Google Scholar](https://scholar.google.com/scholar?q=Libra:+Succinct+Zero-Knowledge+Proofs+with+Optimal+Prover+Computation)

[51] Jiaheng Zhang, Weijie Wang, Yinuo Zhang, and Yupeng Zhang. Doubly Efficient Interactive Proofs for General Arithmetic Circuits with Linear Prover Time. **ePrint 2020** [Google Scholar](https://scholar.google.com/scholar?q=Doubly+Efficient+Interactive+Proofs+for+General+Arithmetic+Circuits+with+Linear+Prover+Time)

[52] Jiaheng Zhang, Tiancheng Xie, Yupeng Zhang, and Dawn Song. Transparent Polynomial Delegation and Its Applications to Zero Knowledge Proof. **S&P 2020** [Google Scholar](https://scholar.google.com/scholar?q=Transparent+Polynomial+Delegation+and+Its+Applications+to+Zero+Knowledge+Proof)

[39] Srinath Setty. Spartan: Efficient and general-purpose zkSNARKs without trusted setup. **CRYPTO 2020** [Google Scholar](https://scholar.google.com/scholar?q=Spartan:+Efficient+and+general-purpose+zkSNARKs+without+trusted+setup)

[44] Riad S. Wahby, Ioanna Tzialla, Abhi Shelat, Justin Thaler, and Michael Walfish. Doubly-efficient zkSNARKs without trusted setup. **S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Doubly-efficient+zkSNARKs+without+trusted+setup)

[26] Shafi Goldwasser, Yael Tauman Kalai, and Guy N. Rothblum. Delegating Computation: Interactive Proofs for Muggles. **J. ACM 2015** [Google Scholar](https://scholar.google.com/scholar?q=Delegating+Computation:+Interactive+Proofs+for+Muggles)

[35] Carsten Lund, Lance Fortnow, Howard Karloff, and Noam Nisan. Algebraic Methods for Interactive Proof Systems. **J. ACM 1992** [Google Scholar](https://scholar.google.com/scholar?q=Algebraic+Methods+for+Interactive+Proof+Systems)


## 关键词

+ 零知识证明
+ 卷积神经网络
+ 机器学习
+ 求和检查协议
+ 隐私保护