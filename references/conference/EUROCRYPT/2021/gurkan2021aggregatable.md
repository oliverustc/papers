---
title: "Aggregatable distributed key generation"
doi: 10.1007/978-3-030-77870-5_6
标题简称:
论文类型: conference
会议简称: EUROCRYPT
发表年份: 2021
created: 2025-05-12 09:16:31
modified: 2025-05-12 09:18:12
---
## Aggregatable distributed key generation

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-030-77870-5_6)

## 作者

+ Kobi Gurkan
+ [Philipp Jovanovic](Philipp%20Jovanovic.md)
+ [Mary Maller](Mary%20Maller.md)
+ [Sarah Meiklejohn](Sarah%20Meiklejohn.md)
+ Gilad Stern
+ [[Alin Tomescu]]

## 笔记

### 背景与动机

分布式密钥生成（DKG）是阈值密码学的核心原语，通过将每个参与方转化为秘密共享的“经销商”来联合生成密钥对，从而消除单点故障。现有DKG协议普遍要求所有方广播线性大小的消息，并要求每个方对其他各方的份额进行验证，导致每个参与方的通信与验证复杂度达到二次方，严重限制了系统的可扩展性。部分方案虽将单方复杂度降至线性，但依赖需要可信设置的多项式承诺方案，引入了额外的信任假设。此外，经典的Pedersen DKG被证明无法生成均匀分布的密钥（缺乏保密性），而Gennaro等人提出的满足保密性的替代方案效率更低，且一轮协议在面对预发（rushing）敌手时不可避免地会受到输出偏置的影响。因此，如何设计一个既能实现公开可验证、又具有线性复杂度且无需可信设置的DKG，同时建立更宽松却依然可证明安全性的定义，成为了核心挑战。

### 相关工作

[53] Pedersen, T.P. A Threshold Cryptosystem without a Trusted Party. **EUROCRYPT 1991** [Google Scholar](https://scholar.google.com/scholar?q=A+Threshold+Cryptosystem+without+a+Trusted+Party)
> 核心思路：首个高效的离散对数DKG协议，通过并行运行Feldman VSS生成密钥。
> 局限与区别：输出密钥分布不满足统计均匀性（Gennaro等人指出），且验证和通信复杂度均为O(n²)；不满足公开可验证，需投诉轮次。

[31] Gennaro, R. et al. Secure Distributed Key Generation for Discrete-Log Based Cryptosystems. **Journal of Cryptology 2007** [Google Scholar](https://scholar.google.com/scholar?q=Secure+Distributed+Key+Generation+for+Discrete-Log+Based+Cryptosystems)
> 核心思路：提出首个满足统计保密性的DKG协议，并建立了安全性的形式化定义。
> 局限与区别：该协议效率显著低于Pedersen DKG；其保密性定义过于严格，导致一轮DKG协议（如本文关注的方案）无法满足，迫使本文采用更弱但更实用的“安全保持”定义。

[27] Fouque, P.-A., Stern, J. One Round Threshold Discrete-Log Key Generation without Private Channels. **PKC 2001** [Google Scholar](https://scholar.google.com/scholar?q=One+Round+Threshold+Discrete-Log+Key+Generation+without+Private+Channels)
> 核心思路：提出首个一轮、公开可验证的DKG协议，无需投诉轮次。
> 局限与区别：最终分发大小为O(n²)，且其安全性证明无法处理预发敌手；本文协议将分发大小压缩为O(n)并提供了处理预发敌手的证明。

[42] Kate, A. Distributed Key Generation and its Applications. **PhD Thesis 2010** [Google Scholar](https://scholar.google.com/scholar?q=Distributed+Key+Generation+and+its+Applications)
> 核心思路：利用常数大小的多项式承诺（需要可信设置）将广播消息大小降为O(1)。
> 局限与区别：依赖可信设置；协议仍需要投诉轮次，且不具备公开可验证性；本文的方法无需可信设置，且在非对称双线性群中通过聚合实现公开可验证。

[32] Gennaro, R. et al. Secure Applications of Pedersen’s Distributed Key Generation Protocol. **CT-RSA 2003** [Google Scholar](https://scholar.google.com/scholar?q=Secure+Applications+of+Pedersen%E2%80%99s+Distributed+Key+Generation+Protocol)
> 核心思路：证明Pedersen DKG可用于构造阈值Schnorr签名。
> 局限与区别：Benhamouda等人后续发现该方案在面对并发敌手时存在攻击；本文则重新审视了Pedersen DKG的安全性，证明其对可重密钥（rekeyable）方案（如BLS、ElGamal）是安全保持的且并发安全。

[18] Cascudo, I., David, B. SCRAPE: Scalable Randomness Attested by Public Entities. **ACNS 2017** [Google Scholar](https://scholar.google.com/scholar?q=SCRAPE+Scalable+Randomness+Attested+by+Public+Entities)
> 核心思路：提出具有O(n)验证复杂度的PVSS方案“Scrape”。
> 局限与区别：本文对Scrape进行了修改（在G₂中增加元素û₂以支持安全证明），并对Scrape的分发实现了聚合，这是原文未有之特性。

[12] Boneh, D., Boyen, X. Efficient Selective Identity-Based Encryption Without Random Oracles. **Journal of Cryptology 2011** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+Selective+Identity-Based+Encryption+Without+Random+Oracles)
> 核心思路：定义了BDH假设。
> 关联：本文VUF的不预测性依赖于BDH假设。

[8] Ballard, L. et al. Correlation-Resistant Storage via Keyword-Searchable Encryption. **IACR ePrint 2005** [Google Scholar](https://scholar.google.com/scholar?q=Correlation-Resistant+Storage+via+Keyword-Searchable+Encryption)
> 核心思路：定义了SXDH假设在非对称双线性群中的变体。
> 关联：本文DKG和VUF的安全性均基于SXDH假设。

[1] Abe, M. et al. On the Impossibility of Structure-Preserving Deterministic Primitives. **Journal of Cryptology 2019** [Google Scholar](https://scholar.google.com/scholar?q=On+the+Impossibility+of+Structure-Preserving+Deterministic+Primitives)
> 核心思路：证明任何纯粹的代数结构保持签名方案都不能用作VUF或VRF。
> 关联：通过打破完全结构保持的限制（使用哈希函数），本文构造的VUF（分量是群元素）回避了这一不可能性。

### 核心技术与方案

本文的整体框架包含三项核心贡献：一个可聚合且可公开验证的DKG协议（基于修改的Scrape PVSS）；一组用于分析DKG安全性的新定义（可重密钥性与密钥可表达性）；以及一个将群元素作为密钥的VUF构造。

**改进的SCRAPE PVSS与聚合**
Scrape PVSS允许一个经销商将秘密 $a_0 \in \mathbb{F}$ 以份额 $\hat{h}_1^{f(\omega_i)}$ 的形式分发给各方，其中 $f(X)$ 是 $t$ 次多项式。公开分发包含对多项式系数的Feldman承诺 $F_i = g_1^{a_i}$，对份额的承诺 $A_i = g_1^{f(\omega_i)}$，以及加密的份额 $\hat{Y}_i = \mathsf{ek}_i^{f(\omega_i)}$。本文的关键修改是在分发中增加了一个元素 $\hat{u}_2 = \hat{u}_1^{a_0}$，其中 $\hat{u}_1$ 是一个公共随机数且无人知其离散对数，这一修改对于在DKG的安全证明中模拟敌手至关重要。
聚合的核心在于Scrape本质上是一个加法同态秘密共享。给定两个分发 $\mathsf{pvss}_1$ 和 $\mathsf{pvss}_2$（对应于多项式 $f_1$ 和 $f_2$），其聚合后的分发对应于多项式 $f_1 + f_2$。具体地，聚合后的承诺为 $F_i = F_{1,i} F_{2,i}$，份额承诺为 $A_i = A_{1,i} A_{2,i}$，加密份额为 $\hat{Y}_i = \hat{Y}_{1,i} \hat{Y}_{2,i}$，以及 $\hat{u}_2 = \hat{u}_{1,2} \hat{u}_{2,2}$。验证算法通过检查 $e(A_i, \hat{h}_1) = e(g_1, \hat{A}_i)$ 来确认份额是否正确，并通过拉格朗日插值验证多项式承诺与份额承诺的一致性。

**可聚合DKG协议**
DKG运行流程如下：每方 $P_i$ 选择随机贡献 $c_i$，广播承诺 $C_i = g_1^{c_i}$ 和知识签名 $\sigma_i$（即对 $C_i$ 的签名，证明其知道 $c_i$）。随后，各方利用改进的Scrape PVSS将各自的贡献 $c_i$ 以 $t$ 次多项式 $f_i(X)$ 秘密分享，并将包含 $F_{i,k}, \hat{u}_{i,2}, A_{i,j}, \hat{Y}_{i,j}$ 的分发通过Gossip网络传播。接收方对收到的分发进行验证并逐步聚合。最终的分发 $\mathsf{pvss}$ 对应的秘密为 $a = \sum w_i c_i$，其中 $w_i$ 是各贡献的聚合权重（由聚合过程中各分发被合并的次数决定）。最终公钥为 $\mathsf{pk} = (g_1^a, \hat{u}_1^a)$，秘密钥为 $\mathsf{sk} = \hat{h}_1^a$。DKG分发中记录了各方的承诺 $C_i$、权重 $w_i$、知识签名 $\sigma_i$，验证时需检查 $C_1^{w_1} \cdots C_n^{w_n} = F_0$ 以确保承诺与聚合多项式常数项一致。
Gossip协议采用乐观方法，容忍少于 $n/2$ 的崩溃节点，但对恶意节点的容错仅有 $\log n$ 个。每方向期望 $\log n$ 个邻居转发聚合后的分发，并在持有“完整”分发（权重和 $\geq t+1$）后以概率 $2/n$ 广播。

**安全定义与证明**
本文放弃了经典但难以实现的“保密性”定义，转而定义“安全保持”概念：若一个DKG与一个密码学原语组合使用时，任意敌手的优势不超过其在原原语安全游戏中的优势，则称该DKG是安全保持的。为此，作者引入了两个核心概念：
1.  **可重密钥性（Rekeyability）**：指一个原语（如BLS、ElGamal）的算法（如签名、加密）可以在不解密或知道原密钥的情况下，将结果从一个密钥“转移”到另一个密钥的线性组合 $f(\alpha, \mathsf{pk}_1, \mathsf{pk}_2) = \alpha \mathsf{pk}_1 + \mathsf{pk}_2$ 下。
2.  **密钥可表达性（Key Expressability）**：指存在一个模拟器，其在控制DKG中所有诚实方的情况下，能够将最终输出的公钥控制为 $\mathsf{pk} = \alpha \mathsf{pk}_1 + \mathsf{pk}_2$，其中 $\mathsf{pk}_1$ 是外部输入的公钥，且模拟器知道 $\alpha$ 和 $(\mathsf{pk}_2, \mathsf{sk}_2)$。
证明主线是：若一个DKG是密钥可表达的，而目标原语是可重密钥的，则该DKG对于该原语是安全保持的。证明通过构造一个归约完成：对DKG安全游戏的敌手，利用DKG的模拟器将其输出转换为标准安全游戏（敌手直接获得公钥 $\mathsf{pk}_1$）中的敌手，其优势不变。本文证明了提出的DKG、Pedersen DKG以及Fouque-Stern DKG均满足密钥可表达性。

**VUF构造**
VUF的公钥为 $(g_1^a, \hat{u}_1^a)$，秘密钥为 $\hat{h}_1^a$。对消息 $m$，计算 $Z = \mathsf{Hash}_{\mathbb{G}_1}(m)$，函数值为 $e(Z, \mathsf{sk})$。签名算法借鉴了Escala-Groth NIZK证明，用于“承诺”秘密钥并对消息进行证明。签名者选择随机盲因子 $\alpha, \beta$，计算承诺 $(\hat{\pi}_1, \hat{\pi}_2) = (\hat{h}_1^{-\alpha} \hat{h}_2^{-\beta}, \mathsf{sk} \cdot \hat{h}_3^{-\alpha} \hat{h}_4^{-\beta})$ 和相应盲因子对应群元素 $(\pi_1, \pi_2, \pi_3, \pi_4) = (g_1^\alpha, Z^\alpha, g_1^\beta, Z^\beta)$。验证通过检查三个配对等式来完成，它们共同保证了签名对应于正确的秘密钥。VUF的派生算法通过组合配对计算来提取唯一的函数输出 $T$。唯一性依赖于SXDH假设：在绑定模式（SXDH实例）下，同一个消息不可能对应两个不同的有效函数值。不可预测性则依赖于BDH假设：在随机预言机模型中，通过嵌入BDH挑战（将部分挑战嵌入公钥和哈希查询）来模拟签名（需要知道随机选择点的离散对数），并猜测敌手预测的目标。

### 核心公式与流程

**SCRAPE 聚合算法**
$$
\begin{aligned}
&\text{对于 } 0 \le i \le t: F_i \gets F_{1,i} F_{2,i}\\
&\text{对于 } 1 \le i \le n: A_i \gets A_{1,i} A_{2,i}, \hat{Y}_i \gets \hat{Y}_{1,i} \hat{Y}_{2,i}\\
&\hat{u}_2 \gets \hat{u}_{1,2} \hat{u}_{2,2}
\end{aligned}
$$
> 作用：加法同态地聚合两个Scrape PVSS分发，为新多项式 $f_1+f_2$ 产生一个新的有效分发。

**DKG 验证检查**
$$
C_1^{w_1} C_2^{w_2} \cdots C_n^{w_n} = F_0
$$
> 作用：确保聚合分发的多项式常数项 $F_0 = g_1^{f(0)}$ 与各方承诺 $C_i$ 的加权和一致。

**DKG 公钥与秘密钥**
$$
\mathsf{pk} = (g_1^a, \hat{u}_1^a) \in \mathbb{G}_1 \times \mathbb{G}_2, \quad \mathsf{sk} = \hat{h}_1^a \in \mathbb{G}_2, \quad a \in \mathbb{F}
$$
> 作用：定义DKG输出的密钥形式，秘密钥仍保持为群元素。

**VUF 验证等式**
$$
1 = e(g_1, \hat{\pi}_1) e(\pi_1, \hat{h}_1) e(\pi_3, \hat{h}_2)
$$
$$
1 = e(Z, \hat{\pi}_1) e(\pi_2, \hat{h}_1) e(\pi_4, \hat{h}_2)
$$
$$
e(\mathsf{pk}_1, \hat{h}_1) = e(g_1, \hat{\pi}_2) e(\pi_1, \hat{h}_3) e(\pi_3, \hat{h}_4)
$$
> 作用：验证者通过这三个配对等式确信签名 $\sigma$ 是对秘密钥 $\mathsf{sk}$ 的一个正确承诺，且对应正确的消息。

**VUF 派生**
$$
T = e(Z, \hat{\pi}_2) e(\pi_2, \hat{h}_3) e(\pi_4, \hat{h}_4)
$$
> 作用：从签名中提取唯一的、不可预测的函数输出，若签名正确则 $T = e(Z, \mathsf{sk})$。

### 实验结果

本文使用 Rust 语言实现了DKG和VUF协议，基于 libzexe 库和 BLS12-381 曲线，运行在 Intel i7-8700k CPU 上。对于64、128、256和8192个参与方的DKG，其分发生成时间（DKG.Deal）分别为71ms、124ms、271ms和8000ms；对完整分发的验证时间（DKG.Verify）分别为359ms、704ms、1305ms和42600ms。验证时间与参与方数目 $n$ 呈现准线性增长（$O(n \log^2 n)$），相对于经典方案中的 $O(n^2)$ 有实质提升。分发的总大小也与 $n$ 线性相关，8192方时分发约3MB。
在VUF性能方面，本文提出的基本VUF签名和验证分别耗时3.47ms和4.73ms。通过进一步优化（旋转/使用随机数证明），签名与验证时间分别降至0.58ms和2.39ms，与BLS签名的0.44ms和2.15ms极为接近，但VUF保留了唯一性这一额外安全性质。VUF的派生运算耗时2.37ms。

### 局限性与开放问题

本文的DKG秘密钥和分片均为群元素 $\mathbb{G}_2$ 而非域元素 $\mathbb{F}$，这限制了一些需要用域元素作为密钥的密码学原语（如Schnorr签名）的直接应用。DKG的鲁棒性仅针对对数级别的恶意节点，虽然声明这在实践中可接受，但限制了在强恶意环境下的适用性。VUF的安全性证明依赖于随机预言机模型（RO）并使用了非标准假设（SXDH和BDH），且不可预测性的证明因需要猜测敌手目标查询而并非紧致。

### 强关联论文

[53] Pedersen, T.P. A Threshold Cryptosystem without a Trusted Party. **EUROCRYPT 1991** [Google Scholar](https://scholar.google.com/scholar?q=A+Threshold+Cryptosystem+without+a+Trusted+Party)

[31] Gennaro, R. et al. Secure Distributed Key Generation for Discrete-Log Based Cryptosystems. **Journal of Cryptology 2007** [Google Scholar](https://scholar.google.com/scholar?q=Secure+Distributed+Key+Generation+for+Discrete-Log+Based+Cryptosystems)

[27] Fouque, P.-A., Stern, J. One Round Threshold Discrete-Log Key Generation without Private Channels. **PKC 2001** [Google Scholar](https://scholar.google.com/scholar?q=One+Round+Threshold+Discrete-Log+Key+Generation+without+Private+Channels)

[42] Kate, A. Distributed Key Generation and its Applications. **PhD Thesis 2010** [Google Scholar](https://scholar.google.com/scholar?q=Distributed+Key+Generation+and+its+Applications)

[32] Gennaro, R. et al. Secure Applications of Pedersen’s Distributed Key Generation Protocol. **CT-RSA 2003** [Google Scholar](https://scholar.google.com/scholar?q=Secure+Applications+of+Pedersen%E2%80%99s+Distributed+Key+Generation+Protocol)

[18] Cascudo, I., David, B. SCRAPE: Scalable Randomness Attested by Public Entities. **ACNS 2017** [Google Scholar](https://scholar.google.com/scholar?q=SCRAPE+Scalable+Randomness+Attested+by+Public+Entities)

[13] Boneh, D. et al. Short Signatures from the Weil Pairing. **ASIACRYPT 2001** [Google Scholar](https://scholar.google.com/scholar?q=Short+Signatures+from+the+Weil+Pairing)

[10] Benhamouda, F. et al. On the (in)security of ROS. **IACR ePrint 2020** [Google Scholar](https://scholar.google.com/scholar?q=On+the+%28in%29security+of+ROS)

[1] Abe, M. et al. On the Impossibility of Structure-Preserving Deterministic Primitives. **Journal of Cryptology 2019** [Google Scholar](https://scholar.google.com/scholar?q=On+the+Impossibility+of+Structure-Preserving+Deterministic+Primitives)

[24] Escala, A., Groth, J. Fine-Tuning Groth-Sahai Proofs. **PKC 2014** [Google Scholar](https://scholar.google.com/scholar?q=Fine-Tuning+Groth-Sahai+Proofs)


## 关键词

+ 分布式密钥生成
+ 可聚合公开可验证转录
+ BLS签名门限化
+ 可验证不可预测函数
+ Pedersen DKG