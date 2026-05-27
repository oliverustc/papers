---
title: "Posterior Security: Anonymity and Message Hiding of Standard Signatures"
doi: 10.1145/3719027.3744797
标题简称:
论文类型: preprint
预印本简称: archive
发表年份: 2025
created: 2025-05-23 02:00:07
modified: 2025-05-23 02:03:02
---
## Posterior Security: Anonymity and Message Hiding of Standard Signatures

## 发表信息

+ [原文链接](https://eprint.iacr.org/2025/855)

已经被CCS 2025接受，后续等到有链接之后再更新此笔记的位置

## 作者

+ [Tsz Hon Yuen](Tsz%20Hon%20Yuen.md)
+ Ying-Teng Chen
+ Shimin Pan
+ Jiangshan Yu
+ Joseph K Liu

## 笔记

### 背景与动机

在数字签名广泛应用的现实场景中，用户常常面临着无法自由修改签名算法的困境。例如，当签名私钥被存放在硬件安全模块（HSM）或托管钱包中时，用户只能通过标准化接口调用标准签名算法，无法在签名生成阶段添加任何额外的隐私保护功能 [1]。然而，在诸如两层中央银行数字货币（CBDC）的架构中，却存在着强烈的隐私需求：用户希望在进行银行间结算时，能够隐藏自己的公钥（身份）和交易金额（消息），以保护交易隐私，同时又不影响第一层用户端的标准签名体验 [3]。

现有的隐私保护签名方案，如群签名和环签名，虽然能够提供匿名性，但它们要求修改底层的签名算法，因此不适用于上述只能使用标准化签名 API 的场景 [12, 29]。这些方案也无法在签名事后，由一个不拥有私钥的第三方来非交互地添加隐私属性。本文正是要填补这一空白，提出“后验安全”的概念，即允许一个独立的转换者在标准签名生成之后，在不访问私钥的情况下，为签名添加匿名性或消息隐藏功能。

### 相关工作

[4] Bender et al. Ring Signatures: Stronger Definitions, and Constructions Without Random Oracles. **TCC 2006**
> 核心思路：为环签名定义了完善的安全模型，包括匿名性和不可伪造性，并提出了标准模型下的构造。
> 局限与区别：环签名要求签名者本人在生成签名时选择环成员，并修改签名算法。本文的 incognito signature 则分离了签名者和匿名化者的角色，允许非签名者事后转换标准签名。

[15] Faz-Hernández et al. ZKAttest: Ring and Group Signatures for Existing ECDSA Keys. **SAC 2021**
> 核心思路：提出了首个基于 ECDSA 的环签名和群签名方案，通过 Σ-协议和 Groth-Kohlweiss 成员证明来验证带有承诺公钥的 ECDSA 签名。
> 局限与区别：zkAttest 构造复杂且签名尺寸巨大（197KB+），本文的 incognito ECDSA 签名尺寸在相同安全级别下小 152 倍以上。更重要的是，zkAttest 将非签名者转换视为“多协议攻击”，而未考虑签名者与转换者分离的安全模型。

[33] Yuen et al. DualRing: Generic Construction of Ring Signatures with Efficient Instantiations. **CRYPTO 2021**
> 核心思路：提出了一种通用的环签名构造范式，并给出了基于椭圆曲线的紧凑高效实例化。
> 局限与区别：DualRing 仍是环签名，需要修改签名过程。本文的 incognito signature 虽在签名大小上常数因子略大，但提供了全新的后验匿名性功能，这是 DualRing 等传统方案无法实现的。

[2] Ateniese et al. Sanitizable Signatures. **ESORICS 2005**
> 核心思路：允许授权的半可信第三方在不与签名者交互的情况下，以受控方式修改已签名消息的特定部分。
> 局限与区别：可净化签名旨在修改消息内容（如健康记录中的部分字段），而本文的 concealed signature 旨在完全隐藏消息内容，并通过承诺和零知识证明来实现，而非局部修改。

[22] Krawczyk and Rabin. Chameleon Signatures. **NDSS 2000**
> 核心思路：使用变色龙哈希函数，使得拥有陷门的第三方可以在签名后修改消息，同时保持签名对原哈希值的验证有效。
> 局限与区别：变色龙签名允许消息替换，而本文的 concealed signature 的目标是隐藏消息，并通过承诺绑定消息，转换后消息不可更改。此外，变色龙签名通常需要交互式设置陷门。

### 核心技术与方案

本文定义了两种后验安全原语：**incognito signature** 和 **concealed signature**，并给出了通用的构造框架。

**1. Incognito Signature**

该原语的核心在于引入一个 **IS.Convert** 算法，该算法由不拥有私钥的转换者执行。其输入是一个标准签名 $\sigma$、消息 $m$、原始签名者的公钥 $\mathsf{pk}^*$ 和一个包含 $n$ 个公钥的集合 $\mathbf{pk}$。转换者通过生成一个关于以下关系的非交互零知识论证（NIZKAoK）$\pi$ 来产生匿名签名 $\sigma_I$：

$$\text{NIZKAoK}\{( \sigma, \mathsf{pk}, \vec{b}): \text{Verify}(\sigma, m, \mathsf{pk}) = 1 \land \mathsf{pk} = \prod_{i=1}^n \mathsf{pk}_i^{b_i} \land \vec{b} \in \{0,1\}^n \land \|\vec{b}\|_1 = 1\}$$

该关系证明存在一个长度为 $n$ 的二进制向量 $\vec{b}$，其汉明重量为1，且原始公钥 $\mathsf{pk}$ 正是公钥集中由 $\vec{b}$ 索引的那个。这样，验证者只需检验 $\pi$ 对 $(m, \mathbf{pk})$ 的有效性，而无需知道哪个是真正的签名者。

该通用构造的安全性由两个定理保证：
- **不可伪造性**：基于底层标准签名的不可伪造性和 NIZKAoK 的可靠性。证明通过模拟器 $S$ 将敌手的伪造规约到底层签名方案。
- **强后验匿名性**：基于 NIZKAoK 的零知识性。即使攻击者拥有所有私钥和原始签名，也无法区分 $\sigma_I$ 是由哪个公钥转换而来。

**2. Concealed Signature**

该原语的目的是隐藏消息。转换者执行 **CS.Convert** 算法，首先生成一个对消息 $m$ 的承诺 $C$，然后生成一个 NIZKAoK $\pi$：

$$\text{NIZKAoK}\{(\sigma, m, \text{aux}): \text{Verify}(\sigma, m, \mathsf{pk}) = 1 \land \text{Decom}(m, C, \text{aux}) = 1\}$$

隐藏签名 $\sigma_{CS} = (\pi, C)$。验证者可以验证 $\sigma_{CS}$，但无法得知消息 $m$。只有在需要时，持有辅助信息 $\text{aux}$ 的一方才能通过出示 $m$ 和 $(\pi, C)$ 来开承诺，证明该签名对应特定消息。

**3. 组合与实例化**

两者可以组合为 **incognito concealed signature**，其 NIZKAoK 关系同时包含公钥隐藏和消息隐藏。论文给出了基于 Schnorr、ECDSA、GQ 和 Falcon 的 incognito signature 具体构造，以及基于 Boneh-Boyen 签名的 concealed signature 构造。例如，incognito Schnorr signature 的签名大小为 $O(\log n)$，包含 $(2\log n + 8)$ 个群元素和 8 个 $\mathbb{Z}_p$ 元素，这得益于 Bulletproofs 证明系统对向量关系的紧凑证明。

### 核心公式与流程

**[Incognito Schnorr/ECDSA Signature 的验证方程]**
$$ g^{s_z} g_0^{s_\beta c} = R_z R^{c_z} C_{\mathsf{pk}}^{c \cdot c_z} $$
> 作用：该方程是转换后的匿名签名 $\sigma_I = (R, C_{\mathsf{pk}}, \pi_z, \pi_{\vec{b}}')$ 中零知识证明 $\pi_z$ 的核心验证等式。它结合了原 Schnorr 验证方程 $g^z = R \cdot \mathsf{pk}_j^c$ 和对承诺公钥的证明，确保 $\pi_z$ 对应的秘密值 $z$ 所证明的公开密钥与 $\pi_{\vec{b}}'$ 中所承诺的二进制向量 $\vec{b}$ 一致。

**[Incognito (EC)DSA Signature 的验证方程]**
$$ K^{s_z} g_0^{s_\beta r} = R_z (g^{H(m)} C_{\mathsf{pk}}^r)^{c_z} $$
> 作用：该方程对应于 incognito ECDSA 签名中 $\pi_z$ 的验证。它验证了零知识证明中所用的秘密值 $s$ 和公钥承诺 $C_{\mathsf{pk}}$ 满足原 ECDSA 验证方程 $K^s = g^{H(m)} \cdot \mathsf{pk}_j^r$，其中 $r = f(K)$。

**[Concealed Boneh-Boyen Signature 的核心构造]**
$$ C = g_2^m h_2^t, \quad \text{NIZKAoK for: } \hat{e}(s, X \cdot C \cdot h_2^{-t} \cdot Y^r) = \hat{e}(g_1, g_2) $$
> 作用：该公式展示了如何将 Boneh-Boyen 签名 $(s, r)$ 转换为隐藏签名。$C$ 是一个 Pedersen 承诺，用于隐藏消息 $m$。NIZKAoK 证明了存在秘密 $s, r, t$ 使得等式成立，从而验证了签名的有效性，但未泄露 $m$。其中 $t$ 是辅助信息，用于将来开承诺。

### 实验结果

论文将 incognito Schnorr signature 和 incognito ECDSA signature 的性能与 DualRing-EC 和 zkAttest 进行了对比。实验在装备了双路 Intel Xeon Gold 6226R CPU (2.90GHz)、256GB RAM 的服务器上进行，使用 secp256k1 曲线和 Rust 语言的 k256 库实现。核心性能数据如表 1 所示：对于 $n=2$ 的环，incognito ECDSA 签名大小为 586 字节，而 zkAttest 的签名大小为 197,504 字节，两者相差 337 倍。对于 $n=4096$ 的大环，incognito ECDSA 的签名大小仅为 1,312 字节，仍比 zkAttest 的 199,968 字节小 152 倍。在运行时间方面，如图 1 所示，incognito Schnorr signature 的签名阶段（Sign）极为高效，耗时小于 0.2ms，整个签名+转换过程（Sign+Convert）的耗时在环大小为 1024 时仍小于 1 秒。这表明该方案非常适合签名端资源受限（如手机端）而转换端为高性能服务器的应用场景。与 DualRing-EC（一个不具备后验安全性且非标准签名的方案）相比，本方案的运行时间更长，但其提供了 DualRing-EC 所不具备的全新功能。在已部署着 ECDSA 的商业场景，该方案的性能优势尤为突出。

### 局限性与开放问题

本文所提方案的一个固有局限是要求转换者必须知道真正的原始公钥，这在用户不拥有私钥的场景下（如 HSM）是成立的，但在某些隐私要求更高的场景下可能存在顾虑。此外，虽然 incognito signature 的签名大小是 $O(\log n)$，但其常数因子是现有 $O(\log n)$ 环签名方案的两倍左右（例如，DualRing-EC 为 $2\log n + 1$ 个群元素，本方案为 $2\log n + 8$ 个），这在实际大环场景中可能带来存储和传输开销。最后，本文仅探讨了完全匿名性，未来可以探索在 incognito signature 中融合更细粒度的匿名-问责性的权衡模型，例如允许通过陷门实现对特定签名的身份追踪。

### 强关联论文

[1] Abe et al. 1-out-of-n Signatures from a Variety of Keys. **ASIACRYPT 2002**
[4] Bender et al. Ring Signatures: Stronger Definitions, and Constructions Without Random Oracles. **TCC 2006**
[7] Boneh and Boyen. Short Signatures Without Random Oracles and the SDH Assumption in Bilinear Groups. **J. Cryptol. 2008**
[8] Bünz et al. Bulletproofs: Short Proofs for Confidential Transactions and More. **IEEE SP 2018**
[15] Faz-Hernández et al. ZKAttest: Ring and Group Signatures for Existing ECDSA Keys. **SAC 2021**
[21] Kiltz et al. Structure-Preserving Signatures from Standard Assumptions, Revisited. **CRYPTO 2015**
[26] Lyubashevsky et al. Lattice-Based Zero-Knowledge Proofs and Applications: Shorter, Simpler, and More General. **CRYPTO 2022**
[29] Rivest et al. How to Leak a Secret. **ASIACRYPT 2001**
[33] Yuen et al. DualRing: Generic Construction of Ring Signatures with Efficient Instantiations. **CRYPTO 2021**
[34] Yuen et al. RingCT 3.0 for Blockchain Confidential Transaction: Shorter Size and Stronger Security. **FC 2020**


## 关键词

+ 后验安全性数字签名匿名性
+ 隐匿签名转换器标准签名匿名化
+ 隐藏签名消息承诺零知识
+ 匿名ECDSA对数环签名大小
+ 中央银行数字货币隐私支付