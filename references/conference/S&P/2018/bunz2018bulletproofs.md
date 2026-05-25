---
title: "Bulletproofs: Short proofs for confidential transactions and more"
标题简称:
论文类型: conference
会议简称: S&P
发表年份: 2018
modified: 2025-04-22 16:06:33
created: 2025-04-08 17:03:06
---

## Bulletproofs: Short proofs for confidential transactions and more

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/8418611)

## 作者

+ [Benedikt Bünz](Benedikt%20Bünz.md)
+ [Jonathan Bootle](Jonathan%20Bootle.md)
+ [Dan Boneh](Dan%20Boneh.md)
+ Andrew Poelstra
+ Pieter Wuille
+ Greg Maxwell

## 笔记

### 背景与动机
在区块链加密货币中，交易金额的隐私至关重要，但现有方案如比特币缺乏任何金额保密性。Maxwell提出的机密交易（CT）通过Pedersen承诺隐藏金额，但需要零知识证明来确保交易有效性（如输入大于输出且所有输出为正数）。当前CT中使用的范围证明大小与范围（如32位）呈线性关系，导致一个仅有两个输出的32位机密交易大小为5.4KB，其中范围证明就占了5KB，成为主要存储和传输开销。更理想的方案是使用SNARKs，但它们需要可信设置，这在分布式区块链环境中是一个严重的安全隐患（若设置被破坏，可伪造证明）。基于离散对数假设的证明系统（如Bootle等人的工作）虽然避免了可信设置，但其内积论证的通信复杂度为6log₂(n)，且直接应用会产生较大开销。此外，现有方案（如STARKs）的证明虽为对数大小，但在实际中（如60位安全级别下）仍超过200KB，且生成证明的内存成本极高。Bulletproofs旨在填补这一空白，提供一个无需可信设置、仅基于离散对数假设、且证明大小仅为2log₂(n)+9个群/域元素的短证明系统，尤其适用于高效的范围证明，并能支持多个证明的聚合，大幅减少存储和验证成本。

### 相关工作
- **基于SNARKs的系统**（如Groth16, Pinocchio）：证明大小恒定（如几百字节），验证速度快，但需要复杂且带有陷阱门的可信设置，生成分布式设置成本高昂，依赖于强假设（如知识指数假设）。本质区别：Bulletproofs无需可信设置，仅依赖离散对数假设。
- **基于STARKs的系统**（如Ben-Sasson等人的工作）：无需可信设置，但证明在实际中仍较大（如超过200KB @60位安全级），且生成证明需要大量内存（FFT计算）。本质区别：Bulletproofs的证明更短（约1KB @同级别电路），生成过程没有大型FFT开销。
- **Bootle等人的内积论证** (EUROCRYPT 2016)：首次提出通信高效的内积论证，但通信量为6log₂(n)个群/域元素。本质区别：Bulletproofs通过修改所证明的关系（从证明两个独立承诺的约束变成证明一个组合承诺满足内积关系），将通信量降低了约3倍，降至2log₂(n)。
- **基于Sigma协议的经典范围证明**（如Camenisch等人）：需要可信设置（如RSA模数或特定签名方案），且证明大小与位数线性或依赖于特定数字分解。本质区别：Bulletproofs无需可信设置，并且证明大小是对数的。
- **Mimblewimble (Poelstra)**：改进了CT，消除了脚本，支持交易聚合，但核心范围证明仍是效率瓶颈。本质区别：Bulletproofs可直接作为其核心范围证明的替换，并在聚合场景下提供进一步压缩。

### 核心技术与方案
**整体框架**：Bulletproofs的核心是一个改进的内积论证（Inner-Product Argument, Protocol 2），它允许证明者让验证者相信，对于一个已知的群元素P（承诺），存在向量a, b ∈ Zₚⁿ使得P = gᵃ hᵇ 且 c = <a, b>。论证过程通过对数轮数递归进行，每轮将向量维度减半，通信量为2log₂(n)个群元素。

**关键技术步骤**：
1. **改进的内积论证**：与Bootle等人论证区别在于，Bulletproofs不单独证明对a和b的承诺，而是直接证明一个组合承诺P满足内积关系。递归步骤中，证明者发送两个群元素L, R，验证者发送随机挑战x，双方通过公式 P' = x⁻¹·L · P · x·R 计算出新的聚合承诺P'，其对应的内积向量变为 (a[:n/2]·x, a[n/2:]·x⁻¹) 和类似变换的b'。递归执行，最终证明者只需发送一个标量r'（即降维后的内积结果）。
2. **零知识范围证明构建**：对于秘密值v ∈ [0, 2ⁿ-1]，证明者将其表示为n个比特a_L ∈ {0,1}ⁿ，满足v = <a_L, 2ⁿ>。证明者构造相关向量a_R = a_L - 1ⁿ（保证比特关系），并承诺a_L, a_R的线性组合以隐藏它们。然后利用多项式编码和quadratic系数提取，将条件“a_L是比特向量”和“a_R = a_L - 1ⁿ”转化为一个关于挑战变量x, y, z的多项式恒等式 t(x) = <l(x), r(x)>，其中l(x)和r(x)是包含a_L, a_R和随机盲化向量的线性函数。证明的核心就是通过内积论证证明这个多项式恒等式成立。
3. **聚合范围证明**：要同时证明m个承诺V_j的值v_j ∈ [0, 2ⁿ-1]，将每个承诺的比特表示拼接成一个mn维向量，并引入额外的挑战z。通过构建一个聚合多项式，将m个独立的比特条件编码到同一个高次多项式中，使得最终的证明大小仅增加O(log(m))个群元素。
4. **批验证**：验证多个独立的Bulletproofs时，可以利用一个随机挑战将多个证明的正确性方程组合成一个整体进行验证。由于验证者的主要开销（指数运算）与证明数量成线性关系，批验证通过减少群指数运算（利用Pippenger算法）降低了边际验证成本。
5. **通用算术电路证明**：将范围证明推广到一般NP语言。电路被表示为扇入为2的加法和乘法门。核心技术类似，将电路约束（如乘法门的输出等于输入积）编码为二次算术程序（QAP）形式的矩阵方程，然后通过类似的随机多项式组合和内积论证来证明可满足性，证明大小仍为对数。

**核心洞察**：成功的关键在于巧妙地通过双挑战（用于聚合不同的承诺和向量分量）将复杂的约束条件（如比特分解、算术电路门关系）转化为一个单一、简洁的多项式恒等式，使得证明者只需对这个恒等式进行内积论证，从而获得对数大小的证明。

### 核心公式与流程

**[改进的内积论证递归步骤]**
设当前证明维数为n，承诺为P（满足P = gᵃ hᵇ且c = <a, b>）。证明者计算：
$$ L = \mathbf{g}_{[n/2:]}^{ \mathbf{a}_{[:n/2]} } \cdot \mathbf{h}_{[:n/2]}^{ \mathbf{b}_{[n/2:]} } $$
$$ R = \mathbf{g}_{[:n/2]}^{ \mathbf{a}_{[n/2:]} } \cdot \mathbf{h}_{[n/2:]}^{ \mathbf{b}_{[:n/2]} } $$
发送L, R给验证者。验证者发送随机挑战x ∈ ℤₚ。双方计算：
$$ \mathbf{g}' = \mathbf{g}_{[:n/2]}^{(x^{-1})} \circ \mathbf{g}_{[n/2:]}^{(x)} $$
$$ \mathbf{h}' = \mathbf{h}_{[:n/2]}^{(x)} \circ \mathbf{h}_{[n/2:]}^{(x^{-1})} $$
$$ P' = L^{(x^{2})} \cdot P \cdot R^{(x^{-2})} $$
新的声明是P' = (g')ᵃ' (h')ᵇ' 且 c = <a', b'>，其中a' = a_{[:n/2]}·x + a_{[n/2:]}·x⁻¹, b' = b_{[:n/2]}·x⁻¹ + b_{[n/2:]}·x。
> 作用：将n维内积问题递归地归约为n/2维问题，每轮通信2个群元素（L, R），最终获得对数级通信量。

**[范围证明的多项式构造]**
设挑战为y, z。定义向量多项式 l(X), r(X) ∈ ℤₚ^{n}，使得对于挑战X = x:
$$ l(x) = (a_L - z·1ⁿ) + s_L·x $$
$$ r(x) = yⁿ∘[(a_R + z·1ⁿ) + s_R·x] + z²·2ⁿ $$
证明者计算t(x) = <l(x), r(x)>，并承诺其系数（t₁, t₂等）。验证者检查：
$$ T_1 = g^{t_1} h^{τ_1}, T_2 = g^{t_2} h^{τ_2} $$
最终，通过内积论证证明t(x) = <l(x), r(x)>。
> 作用：通过多项式的二次展开并检查系数，迫使a_L是比特向量且a_R = a_L - 1，从而证明v在[0, 2ⁿ-1]内。

**[聚合多个范围证明的挑战设置]**
对于m个承诺V_j，其对应的秘密值v_j，验证者生成挑战z, y。定义拼接的比特向量a_L ∈ ℤₚ^{mn}。则lg函数中的“被扰动的”向量r(x)修改为:
$$ r(x) = y^{mn} \circ [(a_R + z·1^{mn}) + s_R·x] + \sum_{j=1}^m z^{j+1}·(0^{(j-1)n} || 2^n || 0^{(m-j)n}) $$
这通过z的不同幂次将各承诺的比特条件“叠加”到同一个多项式恒等式中。
> 作用：用一个单一的内积论证绑定多个独立证明的条件，实现了仅增加O(log(m))通信量的聚合效果。

### 实验结果
实验在Intel Core i7-6820HQ CPU @2.70GHz上进行。对于单个64位范围证明（n=64），证明大小为1.5KB（2log₂(64)+9 = 21个元素），生成时间约0.87ms，验证时间约10.0ms。对比当前CT方案（如基于Borromean Ring Signatures的线性范围证明），64位证明大小约3.8-5.0KB（线性大小），Bulletproofs将其压缩了约2.5-3倍。精度翻倍（从32位到64位）仅增加约64字节（一对L, R）。对于聚合32个64位范围证明（m=32, n=64），证明大小为1.6KB（仅增加约100字节），生成和验证时间分别为30ms和340ms。边际验证成本低于验证32个ECCDSA签名（约0.2ms vs 0.3ms）。在Mimblewimble场景下，用于比特币约50M个UTXO的16GB范围证明数据（52位表示），使用聚合Bulletproofs可降至不到17GB，约10倍压缩。

### 局限性与开放问题
1. **验证时间线性**：虽然证明尺寸是对数的，但证明和验证的时间复杂度仍然是线性的（O(n)），对于大规模电路（如数百万门），验证者需要执行与电路大小成线性关系的群指数运算。尽管批验证可以降低边际成本，但不能改变最坏情况下的验证复杂度。
2. **依赖离散对数假设**：与基于配对的方案（如SNARKs）相比，Bulletproofs依赖离散对数假设，不能获得恒定验证时间。
3. **开放问题**：如何进一步降低验证成本以实现线性甚至亚线性时间的验证？是否能设计出无需可信设置的可验证计算方案，同时保持Bulletproofs的对数证明大小和线性验证速度？如何抵抗量子攻击？

### 强关联论文
- Bootle et al., "Efficient Zero-Knowledge Arguments for Arithmetic Circuits in the Discrete Log Setting", EUROCRYPT 2016
  🔗 https://scholar.google.com/scholar?q=Efficient+Zero-Knowledge+Arguments+for+Arithmetic+Circuits+in+the+Discrete+Log+Setting
- Maxwell, "Confidential Transactions", 2015
  🔗 https://scholar.google.com/scholar?q=Confidential+Transactions
- Poelstra, "Mimblewimble", 2016
  🔗 https://scholar.google.com/scholar?q=Mimblewimble
- Ben-Sasson et al., "Scalable, transparent, and post-quantum secure computational integrity", 2018 (STARKs)
  🔗 https://scholar.google.com/scholar?q=Scalable+transparent+and+post-quantum+secure+computational+integrity
- Groth, "On the Size of Pairing-Based Non-interactive Arguments", EUROCRYPT 2016
  🔗 https://scholar.google.com/scholar?q=On+the+Size+of+Pairing-Based+Non-interactive+Arguments
- Wahby et al., "Double-authentication-preventing signatures", 2018 (on verifiable shuffle related work)
  🔗 https://scholar.google.com/scholar?q=Double-authentication-preventing+signatures
- Ames et al., "Ligero: Lightweight Sublinear Arguments Without a Trusted Setup", CCS 2017
  🔗 https://scholar.google.com/scholar?q=Ligero:+Lightweight+Sublinear+Arguments+Without+a+Trusted+Setup
- Bootle et al., "A Practical Verifiable Shuffle with Sublinear Proof Size", 2015 (mentioned in related work)
  🔗 https://scholar.google.com/scholar?q=A+Practical+Verifiable+Shuffle+with+Sublinear+Proof+Size


## 关键词

+ Bulletproofs
+ 范围证明
+ 非交互式零知识证明
+ 保密交易
+ 无可信设置
+ 离散对数假设