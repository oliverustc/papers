---
title: "Candidate indistinguishability obfuscation and functional encryption for all circuits"
标题简称:
论文类型: journal
期刊简称: SICOMP
发表年份: 2016
created: 2025-04-29 10:25:32
modified: 2025-04-29 10:26:41
---

## Candidate indistinguishability obfuscation and functional encryption for all circuits

## 发表信息

+ [原文链接](https://epubs.siam.org/doi/abs/10.1137/14095772X)

## 作者

+ [Sanjam Garg](Sanjam%20Garg.md) 
+ [Craig Gentry](Craig%20Gentry.md)
+ [Shai Halevi](Shai%20Halevi.md)
+ [Mariana Raykova](Mariana%20Raykova.md)
+ [Amit Sahai](Amit%20Sahai.md)
+ [Brent Waters](Brent%20Waters.md)
## 笔记

### 背景与动机
长久以来，程序混淆和功能加密是密码学中的两大开放问题。程序混淆旨在使程序“不可理解”的同时保持其功能，Barak等人证明了通用虚拟黑盒混淆的不可行性，但他们同时提出了较弱的不可区分性混淆概念，要求对任何两个功能等价且规模相似的电路，其混淆结果计算不可区分。然而，构造能支持所有多项式规模电路的不可区分性混淆器自2001年提出以来一直是悬而未决的难题。功能加密允许密文加密输入x，密钥对应函数f，解密得到f(x)而不泄露x的其他信息，但此前功能加密方案仅能支持非常受限的函数类，如内积谓词，远未达到支持所有电路的目标。本文的核心贡献在于首次给出了支持所有多项式规模电路的不可区分性混淆候选构造，并基于该构造解决了功能加密领域的关键问题。

### 相关工作
[Bar86] D. A. Barrington. Bounded-width polynomial-size branching programs recognize exactly those languages in $nc_1$. **Proceedings of STOC, 1986** [Google Scholar](https://scholar.google.com/scholar?q=Bounded-width+polynomial-size+branching+programs+recognize+exactly+those+languages+in+nc1)
> 核心思路：Barrington定理表明任意深度为d的扇入2布尔电路可以转化为一个长度为$4^d$的宽度为5的置换分支程序。
> 局限与区别：Barrington定理本身不涉及安全性质，本文利用其将NC1电路转换为分支程序形式，作为混淆构造的起点。

[Kil88] J. Kilian. Founding cryptography on oblivious transfer. **Proceedings of STOC, 1988** [Google Scholar](https://scholar.google.com/scholar?q=Founding+cryptography+on+oblivious+transfer)
> 核心思路：Kilian协议通过随机可逆矩阵对分支程序进行随机化，实现两方对NC1电路的安全评估。
> 局限与区别：Kilian协议的直接应用无法防止部分评估攻击和混合输入攻击，且不提供混淆安全性。本文在此协议基础上添加了书端向量和乘法捆绑技术来抵御这些攻击。

[GGH13a] S. Garg, C. Gentry, S. Halevi. Candidate multilinear maps from ideal lattices. **Proceedings of EUROCRYPT, 2013** [Google Scholar](https://scholar.google.com/scholar?q=Candidate+multilinear+maps+from+ideal+lattices)
> 核心思路：Garg等人基于理想格构造了候选多线性映射，为高级密码学原语提供了代数工具。
> 局限与区别：GGH方案提供了完整的多线性映射功能，包括公开参数的编码，但其中弱离散对数攻击不适用于本文。本文从中提取了严格子集功能，即多线性拼图，且只允许生成方进行编码。

[CLT13] J.-S. Coron, T. Lepoint, M. Tibouchi. Practical multilinear maps over the integers. **Proceedings of CRYPTO, 2013** [Google Scholar](https://scholar.google.com/scholar?q=Practical+multilinear+maps+over+the+integers)
> 核心思路：Coron等人基于整数环构造了实用的多线性映射方案，是GGH方案的另一类实现。
> 局限与区别：本文的多线性拼图框架可以基于CLT方案实现，只需利用其子集功能，同样避免了弱离散对数攻击。

[GVW13] S. Gorbunov, V. Vaikuntanathan, H. Wee. Attribute-based encryption for circuits. **Proceedings of STOC, 2013** [Google Scholar](https://scholar.google.com/scholar?q=Attribute-based+encryption+for+circuits)
> 核心思路：Gorbunov等人构造了支持任意电路的基于属性的加密方案，实现了细粒度访问控制。
> 局限与区别：ABE方案不保护属性字符串的隐私，而功能加密需要同时隐藏输入消息x。本文构造的功能加密方案提供了完全的输入隐私。

[GKP+13] S. Goldwasser, Y. Kalai, R. A. Popa, V. Vaikuntanathan, N. Zeldovich. Succinct functional encryption and applications: Reusable garbled circuits and beyond. **Proceedings of STOC, 2013** [Google Scholar](https://scholar.google.com/scholar?q=Succinct+functional+encryption+and+applications+Reusable+garbled+circuits+and+beyond)
> 核心思路：Goldwasser等人构造了具有简洁密文的单密钥功能加密方案，实现了可重用的混淆电路。
> 局限与区别：该方案仅支持单次密钥查询，不满足完全抗合谋性。本文构造的功能加密方案支持任意多项密钥查询，且实现了密文简洁性。

[GGSW13] S. Garg, C. Gentry, A. Sahai, B. Waters. Witness encryption and its applications. **Proceedings of STOC, 2013** [Google Scholar](https://scholar.google.com/scholar?q=Witness+encryption+and+its+applications)
> 核心思路：Garg等人引入了证人加密概念，允许基于NP实例进行加密，当实例有合法证人时可解密。
> 局限与区别：证人加密是功能加密的一个特例。本文展示不可区分性混淆如何直接蕴含NP完全语言的证人加密。

[BSW11] D. Boneh, A. Sahai, B. Waters. Functional encryption: Definitions and challenges. **Proceedings of Theory of Cryptography Conference, 2011** [Google Scholar](https://scholar.google.com/scholar?q=Functional+encryption+Definitions+and+challenges)
> 核心思路：Boneh等人形式化了功能加密的安全定义，并指出强模拟安全定义的不可实现性。
> 局限与区别：本文专注于可实现的不可区分性安全定义，并指出通过[CIJ+13]的变换可以升级为有意义的模拟安全。

### 核心技术与方案
本文的技术方案分为三个层次逐步构建。首先，提出了多线性拼图框架，它是多线性映射的简化变体。与GGH方案不同，多线性拼图只允许系统参数的生成方进行编码，且不提供非平凡的元素0和1的公开编码，从而避免了弱离散对数攻击。多线性拼图包含两个算法：拼图生成器JGen和拼图验证器JVer。JGen根据拼图规范器A输出质数p、私有输出X和公共输出拼图；JVer验证给定的多线性形式F是否在私有输出上求值为0，并据此输出接受或拒绝。安全性假设的核心是：对于两个功能等价的分配，其对应的拼图分布计算不可区分。

其次，基于多线性拼图和Barrington定理构造了NC1电路的不可区分性混淆候选方案。对于一个长度为n的NC1电路对应的分支程序，混淆器生成2n+5维的随机化矩阵$D_{i,b}$和$D'_{i,b}$，其中$D'_{i,b}$是恒等矩阵的缩放，构成哑元分支程序。混淆器引入书端向量s和t来防止部分评估攻击，其特殊结构（前m个分量为0或随机，后5个分量为随机向量）用于在求值后消去中间随机对角元素。为了抵御混合输入攻击，引入了乘法捆绑技术：为每个矩阵乘入随机标量$\alpha_{i,b}$，且保证对每个输入位j，所有标量乘积相等，即$\prod_{i\in I_j} \alpha_{i,0} = \prod_{i\in I_j} \alpha'_{i,0}$和$\prod_{i\in I_j} \alpha_{i,1} = \prod_{i\in I_j} \alpha'_{i,1}$。最终输出$\tilde{s} = sR_0^{-1}$、$\tilde{t} = R_n t$、$\tilde{D}_{i,b} = R_{i-1} D_{i,b} R_i^{-1}$的编码。安全性依赖于等值程序不可区分性假设，并证明在通用着色矩阵模型中该假设无条件成立。

第三，将NC1混淆提升至所有多项式规模电路。给定一个多项式规模电路C，混淆器生成两个同态加密密钥对$(PK_1, SK_1)$和$(PK_2, SK_2)$，用两个密钥分别加密电路C得到$g_1$和$g_2$。然后混淆一个NC1程序$P1^{(SK_1, g_1, g_2)}$，该程序接收输入$(m, e_1, e_2, \phi)$，检查$\phi$是否为证明$e_1$和$e_2$正确计算的低深度证明，若验证通过则用$SK_1$解密$e_1$并计算$C(m)$。安全性证明通过一系列混合论证，利用同态加密的IND-CPA安全性、NC1混淆的族不可区分性以及程序$P1$和$P2$的等价性，最终证明任意两个功能等价的电路C0和C1的混淆结果不可区分。

最后，基于不可区分性混淆构造了支持所有电路的功能加密方案。设置算法生成两个公钥加密密钥对和统计模拟无偏NIZK的CRS。加密算法对消息m用两个公钥加密，并生成证明两个密文加密同一消息的NIZK证明。密钥生成算法生成功能函数f对应的密钥，其形式为混淆程序P3，该程序验证NIZK证明后用第一个私钥解密$e_1$并计算$f(m)$。安全性证明通过一系列混合，利用NIZK的零知识性和统计模拟可靠性、公钥加密的IND-CPA安全性以及混淆的族不可区分性，最终证明加密$m_0$和$m_1$的密文不可区分。

### 核心公式与流程
**[多线性拼图生成]**
$$ \mathsf{Encode}_S(a) = \frac{\hat{a} + e \cdot g}{\prod_{i \in S} z_i} \in R_q $$
> 作用：将元素a编码到多线性映射中的级别S，其中$\hat{a} \equiv a \pmod g$，e是噪声项。

**[零测试参数]**
$$ \mathbf{p}_{zt} = \frac{h \cdot \prod_{i=1}^k z_i}{g} \in R_q $$
> 作用：用于验证最高级编码是否为0的编码。将编码乘以$\mathbf{p}_{zt}$后，若结果为0则乘积较小。

**[混淆分支程序]**
$$ \tilde{\mathbf{s}} = \mathbf{s} R_0^{-1}, \quad \tilde{\mathbf{t}} = R_n \mathbf{t}, \quad \tilde{D}_{i,b} = R_{i-1} D_{i,b} R_i^{-1}, \quad \tilde{D}_{i,b}' = R_{i-1}' D_{i,b}' (R_i')^{-1} $$
> 作用：通过随机可逆矩阵$R_i$和$R_i'$对分支程序进行随机化处理，生成混淆后的矩阵和向量。

**[功能加密的密文]**
$$ \mathrm{CT} = (e_1, e_2, \pi), \text{ where } e_1 = \mathsf{Encrypt}_{PKE}(\mathsf{PK}_{PKE}^1, m; r_1), e_2 = \mathsf{Encrypt}_{PKE}(\mathsf{PK}_{PKE}^2, m; r_2) $$
> 作用：功能加密的密文包含两个对消息m的公钥加密和一个证明它们加密同一消息的NIZK证明$\pi$。

### 实验结果
本文是理论性工作，不包含实验数据。论文提供了所有构造的详细算法描述和安全性形式化证明，没有进行实际性能测量或效率评估。

### 局限性与开放问题
该构造的安全性依赖于新的代数困难假设，仅在理想化的通用着色矩阵模型中给予证明，安全性根基较弱，需要进一步研究在LWE等标准假设下的构造。此外，基于多线性映射的实现方案在效率上可能难以实用，因为多线性参数和矩阵维度较大，导致混淆电路规模巨大。另外，NC1混淆提升到所有电路的过程需要全同态加密，这也引入了额外的性能开销。

### 强关联论文
[Bar86] D. A. Barrington. Bounded-width polynomial-size branching programs recognize exactly those languages in $nc_1$. **Proceedings of STOC, 1986** [Google Scholar](https://scholar.google.com/scholar?q=Bounded-width+polynomial-size+branching+programs+recognize+exactly+those+languages+in+nc1)

[Kil88] J. Kilian. Founding cryptography on oblivious transfer. **Proceedings of STOC, 1988** [Google Scholar](https://scholar.google.com/scholar?q=Founding+cryptography+on+oblivious+transfer)

[GGH13a] S. Garg, C. Gentry, S. Halevi. Candidate multilinear maps from ideal lattices. **Proceedings of EUROCRYPT, 2013** [Google Scholar](https://scholar.google.com/scholar?q=Candidate+multilinear+maps+from+ideal+lattices)

[CLT13] J.-S. Coron, T. Lepoint, M. Tibouchi. Practical multilinear maps over the integers. **Proceedings of CRYPTO, 2013** [Google Scholar](https://scholar.google.com/scholar?q=Practical+multilinear+maps+over+the+integers)

[GVW13] S. Gorbunov, V. Vaikuntanathan, H. Wee. Attribute-based encryption for circuits. **Proceedings of STOC, 2013** [Google Scholar](https://scholar.google.com/scholar?q=Attribute-based+encryption+for+circuits)

[GKP+13] S. Goldwasser, Y. Kalai, R. A. Popa, V. Vaikuntanathan, N. Zeldovich. Succinct functional encryption and applications: Reusable garbled circuits and beyond. **Proceedings of STOC, 2013** [Google Scholar](https://scholar.google.com/scholar?q=Succinct+functional+encryption+and+applications+Reusable+garbled+circuits+and+beyond)

[GGSW13] S. Garg, C. Gentry, A. Sahai, B. Waters. Witness encryption and its applications. **Proceedings of STOC, 2013** [Google Scholar](https://scholar.google.com/scholar?q=Witness+encryption+and+its+applications)

[BSW11] D. Boneh, A. Sahai, B. Waters. Functional encryption: Definitions and challenges. **Proceedings of Theory of Cryptography Conference, 2011** [Google Scholar](https://scholar.google.com/scholar?q=Functional+encryption+Definitions+and+challenges)

[NY90] M. Naor, M. Yung. Public-key cryptosystems provably secure against chosen ciphertext attacks. **Proceedings of STOC, 1990** [Google Scholar](https://scholar.google.com/scholar?q=Public-key+cryptosystems+provably+secure+against+chosen+ciphertext+attacks)

[Sah99] A. Sahai. Non-malleable non-interactive zero knowledge and adaptive chosen-ciphertext security. **Proceedings of FOCS, 1999** [Google Scholar](https://scholar.google.com/scholar?q=Non-malleable+non-interactive+zero+knowledge+and+adaptive+chosen-ciphertext+security)


## 关键词

+ 不可区分性混淆候选构造
+ 通用电路函数加密
+ 多线性拼图硬度假设
+ NC1混淆全同态加密组合
+ 简洁密文函数加密
+ 非交互式零知识混淆应用