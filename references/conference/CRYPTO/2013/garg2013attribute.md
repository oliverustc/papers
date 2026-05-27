---
title: "Attribute-based encryption for circuits from multilinear maps"
doi: 10.1007/978-3-642-40084-1_27

标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 2013
created: 2025-04-29 10:32:04
modified: 2025-04-29 10:32:49
---
## Attribute-based encryption for circuits from multilinear maps

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-642-40084-1_27)

## 作者

+ [Sanjam Garg](Sanjam%20Garg.md) 
+ [Craig Gentry](Craig%20Gentry.md)
+ [Shai Halevi](Shai%20Halevi.md)
+ [Amit Sahai](Amit%20Sahai.md)
+ [Brent Waters](Brent%20Waters.md)
## 笔记

### 背景与动机
属性基加密（ABE）允许发送方根据属性集加密消息，只有满足特定策略的用户才能解密。自Sahai和Waters [SW05] 提出以来，ABE的两个主要变体——密钥策略（KP-ABE）和密文策略（CP-ABE）——得到了广泛研究。然而，此前所有基于双线性映射的ABE方案均局限于fanout为1的电路，即布尔公式（对应复杂度类NC¹）。实现一般电路（任意fanout）的ABE是该领域长期悬而未决的核心挑战。现有方案存在一种“回溯攻击”（backtracking attack）：当OR门的一个输入为1时，解密算法会同时获得另一输入（值为0）的中间值，若该另一输入同时扇出到其他门，攻击者便可利用该信息错误地声称该路径满足条件，从而突破安全性。本文利用多线性映射（multilinear maps）首次构造了支持一般电路（任意fanout）的ABE方案，并证明了在标准模型下基于k-MDDH假设的选择性安全性。该构造直接适用于Garg、Gentry和Halevi [GGH12b] 的近似多线性映射框架。

### 相关工作

[GPSW06] Goyal, V., Pandey, O., Sahai, A., Waters, B. Attribute-Based Encryption for Fine-Grained Access Control of Encrypted Data. **ACM CCS 2006** [Google Scholar](https://scholar.google.com/scholar?q=Attribute-Based+Encryption+for+Fine-Grained+Access+Control+of+Encrypted+Data)
> 核心思路：基于双线性映射的KP-ABE，支持布尔公式（fanout=1的电路），利用线性秘密共享方案进行解密。
> 局限与区别：仅支持fanout=1的电路，存在回溯攻击，无法推广到一般电路。本文使用多线性映射的“前向移动+移位”机制克服该攻击。

[SW05] Sahai, A., Waters, B. Fuzzy Identity-Based Encryption. **EUROCRYPT 2005** [Google Scholar](https://scholar.google.com/scholar?q=Fuzzy+Identity-Based+Encryption)
> 核心思路：提出模糊IBE，可视为ABE的雏形，支持阈值策略。
> 局限与区别：策略表达能力有限，不支持任意电路。

[BS02] Boneh, D., Silverberg, A. Applications of Multilinear Forms to Cryptography. **IACR ePrint 2002/080** [Google Scholar](https://scholar.google.com/scholar?q=Applications+of+Multilinear+Forms+to+Cryptography)
> 核心思路：提出多线性映射的概念并讨论其应用，如k轮Diffie-Hellman密钥交换。
> 局限与区别：当时未给出具体实现，本文利用其实例化（通过GGH12）构造ABE。

[GGH12b] Garg, S., Gentry, C., Halevi, S. Candidate Multilinear Maps from Ideal Lattices and Applications. **EUROCRYPT 2013** (full version ePrint 2012/610) [Google Scholar](https://scholar.google.com/scholar?q=Candidate+Multilinear+Maps+from+Ideal+Lattices+and+Applications)
> 核心思路：基于理想格构造“近似”多线性映射（分级编码系统），为本文提供底层工具。
> 局限与区别：本文将其抽象为多线性映射模型，并证明构造直接适用于该框架。

[GVW13] Gorbunov, S., Vaikuntanathan, V., Wee, H. Attribute-Based Encryption for Circuits. **STOC 2013** [Google Scholar](https://scholar.google.com/scholar?q=Attribute-Based+Encryption+for+Circuits)
> 核心思路：基于LWE假设独立构造了支持一般电路的ABE，密文大小与电路深度成线性关系。
> 局限与区别：本文基于多线性映射，两者假设不同；本文的证明技术路线（前向移动+移位）与GVW的格方法有本质区别。

[GGSW13] Garg, S., Gentry, C., Sahai, A., Waters, B. Witness Encryption and its Applications. **STOC 2013** [Google Scholar](https://scholar.google.com/scholar?q=Witness+Encryption+and+its+Applications)
> 核心思路：提出见证加密（witness encryption），结合NIWI证明可构造电路ABE。
> 局限与区别：构造依赖不同的NP实例假设，而本文为直接构造。

### 核心技术与方案

**系统模型**：本文构造的是密钥策略ABE（KP-ABE）。Setup算法输入安全参数λ、输入长度n和电路最大深度ℓ，生成多线性映射群序列G₁,…,Gₖ（k=ℓ+1），随机选取α∈Zₚ和h₁,…,hₙ∈G₁，公开参数PP包含gₖ^α和h₁,…,hₙ，主密钥MSK为(g_{k-1})^α。Encrypt算法对属性向量x∈{0,1}ⁿ和消息M∈Gₖ，随机选取s∈Zₚ，输出密文CT=(C_M=M·(gₖ^α)^s, g^s, {h_i^s}对于满足x_i=1的i)。KeyGen算法为电路f（深度≤ℓ）生成密钥：为每个线w关联随机值r_w，输出头K_H=g_{k-1}^{α-r_{n+q}}，并根据线类型生成不同组件。Decrypt算法首先计算E'=e(K_H,g^s)=gₖ^{αs}·gₖ^{-r_{n+q}s}，然后自底向上计算各线w（若f_w(x)=1）的E_w=(g_{depth(w)+1})^{s r_w}，最终得到E_{n+q}=gₖ^{r_{n+q}s}，恢复gₖ^{αs}并解密。

**关键机制**：OR门和AND门的解密采用“前向移动+移位”两步。以OR门为例，设线w深度为j，若输入A(w)为1，则计算：
1. e(E_{A(w)}, K_{w,1}) = e(g_j^{s r_{A(w)}}, g^{a_w}) = g_{j+1}^{s a_w r_{A(w)}}（前向移动）；
2. e(K_{w,3}, g^s) = e(g_j^{r_w - a_w·r_{A(w)}}, g^s) = g_{j+1}^{s(r_w - a_w r_{A(w)})}（移位）；
两者相乘得g_{j+1}^{s r_w}。关键安全特性：若B(w)为0，攻击者无法通过反向操作从g_{j+1}得到g_j，从而阻止回溯攻击。AND门类似，需要两个输入均为1，通过三个配对项计算。

**安全性**：方案基于k-MDDH假设（k-Multilinear Decisional Diffie-Hellman），在标准模型下证明选择性安全：攻击者提前声明挑战属性x*，可查询任意满足f(x*)=0的电路密钥，无法区分挑战密文中的消息。证明通过模拟器构造，逐一处理密钥查询并利用多线性映射的代数性质保持模拟的一致性；详细证明见全文版本[GGH+13b]。

**复杂度**：公钥大小O(n)，密文大小O(|x|)（即属性中1的个数），密钥大小与电路规模（线数+门数）线性相关。解密计算量：对于每条满足的线，执行常数次配对运算，总配对次数等于电路中满足线的数量。所有操作均在多项式时间内完成。

### 核心公式与流程

**[Setup]**
$$k = \ell + 1, \quad \mathcal{G}(1^\lambda, k) \to (\mathbb{G}_1,\dots,\mathbb{G}_k), \quad |\mathbb{G}_i| = p > 2^\lambda$$
$$\alpha \xleftarrow{R} \mathbb{Z}_p, \quad h_1,\dots,h_n \xleftarrow{R} \mathbb{G}_1$$
$$\mathrm{PP} = (g_k^\alpha, h_1,\dots,h_n), \quad \mathrm{MSK} = g_{k-1}^\alpha$$
> 作用：生成多线性群、公共参数和主密钥。

**[Encrypt]**
$$s \xleftarrow{R} \mathbb{Z}_p, \quad C_M = M \cdot (g_k^\alpha)^s$$
$$\mathrm{CT} = \big(C_M,\; g^s,\; \{C_i = h_i^s \mid x_i = 1\}\big)$$
> 作用：用属性x加密消息M，输出密文。

**[KeyGen – OR gate]**
令 $j = \mathrm{depth}(w)$，随机 $a_w, b_w \in \mathbb{Z}_p$，
$$K_{w,1} = g^{a_w},\quad K_{w,2} = g^{b_w},\quad K_{w,3} = g_j^{r_w - a_w \cdot r_{A(w)}},\quad K_{w,4} = g_j^{r_w - b_w \cdot r_{B(w)}}$$
> 作用：为OR门生成密钥组件，包含两个移动密钥和两个移位密钥。

**[Decrypt – OR gate (first input 1)]**
$$E_w = e(E_{A(w)}, K_{w,1}) \cdot e(K_{w,3}, g^s) = e(g_j^{s r_{A(w)}}, g^{a_w}) \cdot e(g_j^{r_w - a_w r_{A(w)}}, g^s) = g_{j+1}^{s r_w}$$
> 作用：利用前向移动和移位计算输出线w的中间值。

**[Decrypt – AND gate]**
$$E_w = e(E_{A(w)}, K_{w,1}) \cdot e(E_{B(w)}, K_{w,2}) \cdot e(K_{w,3}, g^s)$$
$$= e(g_j^{s r_{A(w)}}, g^{a_w}) \cdot e(g_j^{s r_{B(w)}}, g^{b_w}) \cdot e(g_j^{r_w - a_w r_{A(w)} - b_w r_{B(w)}}, g^s) = g_{j+1}^{s r_w}$$
> 作用：AND门需要两个输入均为1，通过三项配对得到输出。

### 实验结果
本文为理论性工作，未提供实验评估。构造基于理想的多线性映射抽象模型，在GGH12 [GGH12b] 分级编码系统中有候选实现，但实际性能取决于底层格参数的设定。文中未报告任何具体实现、运行时间或通信开销数值。

### 局限性与开放问题
构造要求电路为分层单调电路，通用电路可通过De Morgan律和输入取反转化为单调电路，但会引入额外开销。方案选定最大深度ℓ在Setup阶段固定，无法支持深度超过ℓ的电路。安全性为选择性安全，未能达到完全自适应安全（adaptive security）。底层多线性映射的候选构造（如GGH12）安全性依赖于非标准假设，且存在已知攻击导致参数需保守选择。另一个开放方向是设计基于更标准假设（如LWE）的高效电路ABE，或实现支持任意深度电路的可重置多线性映射。

### 强关联论文

[SW05] Sahai, A., Waters, B. Fuzzy Identity-Based Encryption. **EUROCRYPT 2005** [Google Scholar](https://scholar.google.com/scholar?q=Fuzzy+Identity-Based+Encryption)

[GPSW06] Goyal, V., Pandey, O., Sahai, A., Waters, B. Attribute-Based Encryption for Fine-Grained Access Control of Encrypted Data. **ACM CCS 2006** [Google Scholar](https://scholar.google.com/scholar?q=Attribute-Based+Encryption+for+Fine-Grained+Access+Control+of+Encrypted+Data)

[BS02] Boneh, D., Silverberg, A. Applications of Multilinear Forms to Cryptography. **IACR ePrint 2002/080** [Google Scholar](https://scholar.google.com/scholar?q=Applications+of+Multilinear+Forms+to+Cryptography)

[GGH12b] Garg, S., Gentry, C., Halevi, S. Candidate Multilinear Maps from Ideal Lattices and Applications. **EUROCRYPT 2013** (full version ePrint 2012/610) [Google Scholar](https://scholar.google.com/scholar?q=Candidate+Multilinear+Maps+from+Ideal+Lattices+and+Applications)

[GVW13] Gorbunov, S., Vaikuntanathan, V., Wee, H. Attribute-Based Encryption for Circuits. **STOC 2013** [Google Scholar](https://scholar.google.com/scholar?q=Attribute-Based+Encryption+for+Circuits)

[GGSW13] Garg, S., Gentry, C., Sahai, A., Waters, B. Witness Encryption and its Applications. **STOC 2013** [Google Scholar](https://scholar.google.com/scholar?q=Witness+Encryption+and+its+Applications)

[PRV12] Parno, B., Raykova, M., Vaikuntanathan, V. How to Delegate and Verify in Public: Verifiable Computation from Attribute-Based Encryption. **TCC 2012** [Google Scholar](https://scholar.google.com/scholar?q=How+to+Delegate+and+Verify+in+Public+Verifiable+Computation+from+Attribute-Based+Encryption)


## 关键词

+ 属性基加密一般电路多线性映射
+ 密钥策略密文策略ABE双变体
+ 标准模型选择性安全BDDH多线性
+ 多线性映射框架通用ABE构造
+ 属性基加密可满足电路表达