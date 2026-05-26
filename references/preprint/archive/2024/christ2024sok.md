---
title: "SoK: Zero-knowledge range proofs"
标题简称:
论文类型: preprint
预印本简称: archive
发表年份: 2024
modified: 2025-04-16 10:12:14
created: 2025-04-11 11:51:08
---

## SoK: Zero-knowledge range proofs

## 发表信息

+ [原文链接](https://eprint.iacr.org/2024/430)

## 作者

+ [Miranda Christ](Miranda%20Christ.md)
+ [Foteini Baldimtsi](Foteini%20Baldimtsi.md)
+ Konstantinos Kryptos Chalkias 
+ [Deepak Maram](Deepak%20Maram.md)
+ [Arnab Roy](Arnab%20Roy.md)
+ Joy Wang 

## 笔记

### 背景与动机

零知识区间证明允许证明者向验证者证明一个秘密值落在给定区间内，而不泄露该值本身。这一原语在匿名凭证、保密交易、隐私投票和区块链审计等众多应用中扮演着关键角色。随着去中心化系统和加密货币的兴起，对高效区间证明的需求激增，例如在保密交易中，发送方必须证明输出金额为正，以避免凭空创造货币。然而，文献中存在大量ZKP区间证明方案，它们基于不同的构建技术（如平方分解、二进制分解和哈希链），各自拥有独特的性能权衡，如证明大小、验证时间、是否需要可信设置以及是否支持聚合。这种多样性使得开发者为其特定应用选择最合适的方案变得极具挑战性。虽然存在一篇早期的调研[64]，但其覆盖范围有限，遗漏了诸如Sharp[31]和BFGW[12]等许多高效的现代方案，也未进行全面的性能基准测试。为了填补这一空白，本文旨在系统化地梳理关于零知识区间证明的知识，建立一个统一的分类体系，并对各类方案的属性与效率进行详尽比较，最终为实践者提供一个清晰的选择指南。

### 相关工作

[64] Morais, Koens, van Wijk, and Koren. A survey on zero knowledge range proofs and applications. **arXiv 2019** [Google Scholar](https://scholar.google.com/scholar?q=A+survey+on+zero+knowledge+range+proofs+and+applications)
> 核心思路：该工作是对零知识区间证明的早期调研。
> 局限与区别：其技术部分主要集中于Boudot的四平方分解[15]、CCs的签名构建[24]和Bulletproofs[19]，未深入探讨许多其他重要方案，如基于编码的方案、更新的平方分解方案（如Sharp）、基于多项式承诺的方案、哈希链方案和基于格的结构。本文提供了显著更全面的覆盖、统一的分类和新的基准测试。

### 核心技术与方案

本文的核心贡献是将所有已知的零知识区间证明方案归类为三种底层技术方法，并对每种方法进行详细剖析和比较。

**平方分解法** 利用了拉格朗日四平方定理，即任何非负整数都可以表示为四个整数的平方和。为了证明一个承诺值 *z* 是非负的，证明者只需证明他知道四个整数 *x₁, x₂, x₃, x₄* 使得 $z = x_1^2 + x_2^2 + x_3^2 + x_4^2$ 成立。这种方法的关键在于使用“整数承诺”方案，例如Fujisaki-Okamoto承诺[43]。这类承诺方案的绑定性质在整数域上成立，而非模某个群阶，从而确保了等式在整数上而非模某个数下成立。这类方案（如Boudot[15]，Lipmaa[59]，CKLR[32]，Sharp[31]）通常需要一个隐藏阶群（如RSA群或类群）来实现完整性，这往往意味着需要可信设置（RSA群）或在工程上不够高效（类群）。Sharp[31]是此路线的最新代表，它通过将CKLR的修改从承诺转移到证明中，兼容了标准Pedersen承诺，并在牺牲部分可靠性以换取效率（$\text{Sharp}_{\text{GS}}, \text{Sharp}_{\text{SO}}^{\text{PO}}$）或通过引入隐藏阶群来获得完全可靠性（$\text{Sharp}_{\text{HO}}$）之间提供了不同变体。

**n进制分解法** 是当前最主流的方法，其核心是将被证明的值 *z* 在基 *n*（通常为2）下进行分解。证明者首先承诺 *z* 的每一位数字 *zᵢ*，然后证明两个关键谓词：**数字有效性 (DV)**，即每个 $z_i \in \{0, \dots, n-1\}$；以及**表示正确性 (Rep)**，即 $z = \sum z_i \cdot n^i$。实现这些谓词的工具主要包括：集合成员证明（如CCs[24]）、乘积与内积参数以及多项式承诺。内积参数法（IPA）是Bulletproofs[19]及其衍生方案（Bulletproofs+[30], Bulletproofs++[38]）的核心技术。Bulletproofs巧妙地结合了数字有效性检查和表示正确性检查，通过一个单一的IPA证明三者（$\mathbf{a_L} \circ \mathbf{a_R} = \mathbf{0}^k$, $\mathbf{a_L} - \mathbf{a_R} = \mathbf{1}^k$, $\langle \mathbf{a_L}, \mathbf{2}^k \rangle = x$）同时成立，从而实现了对数级别的证明大小 $O(\log k)$。Bulletproofs++[38] 进一步扩展递归参数至任意基，通过查找论证实现了 $O(\log k / \log \log k)$ 的更优渐进复杂度。另一条路线是基于多项式承诺的BFGW[12]方案，它通过多项式在特定子群上的求值来编码二进制表示，并使用多项式恒零检验来同时证明数字有效性和表示正确性，从而获得常数级证明大小（当与KZG[52]承诺结合时）。基于格的方案（如ALS[4]）也采用此框架，但它们通常基于Stern协议[71]，具有常数级可靠性误差，需重复 $O(\lambda)$ 次，导致证明体积庞大。

**哈希链法** 的核心思想是用一个哈希函数迭代计算来承诺一个值，即 $C_z = H^z(r)$。要证明 $z \geq t$，证明者只需提供 $\pi = H^{z-t}(r)$，验证者则检查 $H^t(\pi)$ 是否等于 $C_z$。其安全性依赖于哈希函数的抗原像性，如果 $z < t$，计算负指数次迭代是不可行的。此方法的关键优势在于其极致的计算效率，因为它只涉及哈希运算。HashWires[26] 通过使用基数分解（最小支配分区）优化了原始方案，使得证明大小和计算复杂度与对数 *k* 成正比，而非线性。然而，HashWires 工作在一个更受限的“基于凭证的区间证明”模型下，其可靠性依赖于承诺由可信发行方生成，这限制了其通用性。

### 核心公式与流程

**[平方分解 (四平方定理)]**
$$z = x_1^2 + x_2^2 + x_3^2 + x_4^2$$
> 作用：将证明 *z* 非负性的问题转化为证明存在四个整数满足等式的问题。

**[Bulletproofs的二进制分解检查]**
$$
(1) \ \mathbf{a}_{\mathrm{L}} \circ \mathbf{a}_{\mathrm{R}} = \mathbf{0}^{\mathrm{k}}, \quad (2) \ \mathbf{a}_{\mathrm{L}} - \mathbf{a}_{\mathrm{R}} = \mathbf{1}^{\mathrm{k}}, \quad (3) \ \langle \mathbf{a}_{\mathrm{L}}, \mathbf{2}^{\mathrm{k}} \rangle = x
$$
> 作用：将数字有效性（每位为0或1）和表示正确性（*x* 是其二进制表示）三个条件组合成一个系统。条件(1)和(2)确保 $\mathbf{a_L}$ 的每个分量是1或0，条件(3)确保这些分量正确表示了 *x*。

**[BFGW的多项式恒零检验]**
$$
w_2 = g \cdot (1 - g) (X - 1) (X - \omega) \dots (X - \omega^{k-2})
$$
$$
w_3 = \left[ g(X) - 2g(X\omega) \right] \cdot \left[ 1 - g(X) + 2g(X\omega) \right] \cdot \left(X - \omega^{k-1}\right)
$$
> 作用：在BFGW方案中，多项式 *w₂* 和 *w₃* 在子群 *H* 上的零点分别编码了数字有效性和表示正确性。证明者通过证明这些多项式在 *H* 上恒为零（通过多项式承诺和Schwartz-Zippel引理），从而完成区间证明。

**[HashWires的哈希链验证]**
$$C_z = H^z(r), \quad \pi = H^{z-t}(r), \quad \text{Verifier checks: } H^t(\pi) \stackrel{?}{=} C_z$$
> 作用：定义了基于哈希链的承诺和验证过程。证明者提供一个预像 *π*，验证者通过 *t* 次哈希计算确认 *π* 的 *t* 次迭代等于原始承诺，从而证明 $z \geq t$。

### 实验结果

本文通过提供新的基准测试（开源在 https://github.com/joyqvq/range-proof-benches）和汇编已有数据，对多种主流ZKP区间证明方案进行了详细的效率比较。实验在AMD EPYC 7443P 24-Core处理器上运行。对于64位区间，**HashWires（基数16）** 的证明生成时间最快，仅0.061毫秒，验证时间也最快，仅0.002毫秒。**HashWires（基数256）** 的证明大小最小，为199字节。**Bulletproofs** 的证明大小为675字节，验证时间2.51毫秒。**Bulletproofs++** 的证明大小更小（416字节），验证时间0.84毫秒，均快于标准Bulletproofs。具有常数级证明大小的方案中，**BFGW+KZG** 的证明大小为576字节，但验证时间（5.682毫秒）和生成时间（12.569毫秒）均较长。**Groth16**（使用Poseidon承诺）的证明大小最小，仅192字节，但验证时间为4毫秒，生成时间长达34.46毫秒，是所有方案中最慢的。基于平方分解的 **Sharp** 方案在效率上表现均衡，例如 $\text{Sharp}_{\text{SO}}^{\text{PO}}$ 的验证时间为0.75毫秒，证明大小为389字节。相比之下，**基于格**的方案，如ALS[4]和ESLL[39]，其证明体积巨大，分别为5,900字节和93,000字节，远高于其他方案，显示了它们在实际应用中的效率瓶颈。

### 局限性与开放问题

本文指出了多个未来研究方向，其中最突出的是缺乏一个同时具备实用性、透明设置和恒定大小证明的ZKP区间证明方案。当前，Bulletproofs家族具有透明设置但证明大小为 $O(\log k)$，而BFGW+KZG有恒定大小证明但需要可信设置。此外，对于后量子安全的格基和编码基方案，其证明体积仍然过大，且不支持多证明者聚合，尚无法与基于离散对数的方案竞争。另一个研究空白是构建与LWE密码系统兼容的高效后量子ZKP区间证明，以实现抗量子安全的可验证加密。

### 强关联论文

[12] Boneh, Fisch, Gabizon, and Williamson. A Simple Range Proof from Polynomial Commitments. **Cryptology ePrint Archive 2020** [Google Scholar](https://scholar.google.com/scholar?q=A+Simple+Range+Proof+from+Polynomial+Commitments)

[15] Boudot. Efficient Proofs that a Committed Number Lies in an Interval. **EUROCRYPT 2000** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+Proofs+that+a+Committed+Number+Lies+in+an+Interval)

[19] Bünz, Bootle, Boneh, Poelstra, Wuille, and Maxwell. Bulletproofs: Short Proofs for Confidential Transactions and More. **IEEE S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Bulletproofs%3A+Short+Proofs+for+Confidential+Transactions+and+More)

[24] Camenisch, Chaabouni, and Shelat. Efficient Protocols for Set Membership and Range Proofs. **ASIACRYPT 2008** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+Protocols+for+Set+Membership+and+Range+Proofs)

[26] Chalkias, Cohen, Lewi, Moezinia, and Romailler. HashWires: Hyperefficient Credential-Based Range Proofs. **PoPETs 2021** [Google Scholar](https://scholar.google.com/scholar?q=HashWires%3A+Hyperefficient+Credential-Based+Range+Proofs)

[31] Couteau, Goudarzi, Klooß, and Reichle. Sharp: Short Relaxed Range Proofs. **ACM CCS 2022** [Google Scholar](https://scholar.google.com/scholar?q=Sharp%3A+Short+Relaxed+Range+Proofs)

[32] Couteau, Klooß, Lin, and Reichle. Efficient Range Proofs with Transparent Setup from Bounded Integer Commitments. **EUROCRYPT 2021** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+Range+Proofs+with+Transparent+Setup+from+Bounded+Integer+Commitments)

[38] Eagen. Bulletproofs++. **Cryptology ePrint Archive 2022** [Google Scholar](https://scholar.google.com/scholar?q=Bulletproofs%2B%2B)

[47] Groth. On the Size of Pairing-Based Non-Interactive Arguments. **EUROCRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=On+the+Size+of+Pairing-Based+Non-Interactive+Arguments)

[52] Kate, Zaverucha, and Goldberg. Constant-Size Commitments to Polynomials and Their Applications. **ASIACRYPT 2010** [Google Scholar](https://scholar.google.com/scholar?q=Constant-Size+Commitments+to+Polynomials+and+Their+Applications)


## 关键词

+ 零知识范围证明系统化综述
+ ZKRP匿名凭证保密交易应用
+ 范围证明构建技术分类比较
+ 加密货币区间证明效率
+ 范围证明方案选择指南