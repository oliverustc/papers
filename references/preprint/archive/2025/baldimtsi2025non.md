---
title: "Non-interactive Anonymous Tokens with Private Metadata Bit"
标题简称:
论文类型: preprint
预印本简称: archive
发表年份: 2025
created: 2025-05-09 14:27:36
modified: 2025-05-09 14:29:15
---

## Non-interactive Anonymous Tokens with Private Metadata Bit

## 发表信息

+ [原文链接](https://eprint.iacr.org/2025/430)

## 作者

+ [Foteini Baldimtsi](Foteini%20Baldimtsi.md)
+ [Lucjan Hanzlik](Lucjan%20Hanzlik.md)
+ Quan Nguyen
+ Aayush Yadav

## 笔记

### 背景与动机

匿名令牌是一种强大的隐私保护原语，广泛应用于CDN访问、隐私浏览、欺诈检测等场景。现有匿名令牌方案（如Privacy Pass [1]、PMBTokens [8]、ATHM [10]）均要求客户端与发行者之间进行交互式的令牌颁发协议——客户端发起请求，发行者在线执行昂贵的签名运算并返回结果。这种交互模式在实际部署中带来延迟问题、可扩展性瓶颈，尤其当发行者需要同时处理大量请求时，在线签名操作成为性能短板。此外，现有交互式方案均不支持私有元数据位（private metadata bit）与公开验证（public verification）的非交互式组合。本文旨在填补这一空白：提出第一个非交互式匿名令牌（NIAT）方案，支持私有元数据位的嵌入与提取，同时保持公开可验证性，并进一步扩展至双花识别功能。

### 相关工作

[1] Davidson 等. Privacy pass: Bypassing internet challenges anonymously. **PoPETs 2018** [Google Scholar](https://scholar.google.com/scholar?q=Privacy+pass%3A+Bypassing+internet+challenges+anonymously)
> 核心思路：基于VOPRF的交互式匿名令牌，用于CDN隐私保护。
> 局限与区别：需要交互，不支持私有元数据位；本文实现非交互式且支持私有位。

[8] Kreuter 等. Anonymous tokens with private metadata bit. **CRYPTO 2020** [Google Scholar](https://scholar.google.com/scholar?q=Anonymous+tokens+with+private+metadata+bit)
> 核心思路：扩展VOPRF以嵌入一个私有元数据位，称为PMBTokens。
> 局限与区别：仍需交互，且令牌仅支持私有验证；本文实现了非交互式公开验证。

[10] Chase 等. Anonymous tokens with stronger metadata bit hiding from algebraic MACs. **CRYPTO 2023** [Google Scholar](https://scholar.google.com/scholar?q=Anonymous+tokens+with+stronger+metadata+bit+hiding+from+algebraic+MACs)
> 核心思路：基于代数MAC的交互式匿名令牌，统一验证与位提取定义。
> 局限与区别：交互式且不支持公开验证；本文为非交互式并支持公开验证。

[15] Hanzlik. Non-interactive blind signatures for random messages. **EUROCRYPT 2023** [Google Scholar](https://scholar.google.com/scholar?q=Non-interactive+blind+signatures+for+random+messages)
> 核心思路：首次提出非交互式盲签名（NIBS），基于SPS-EQ实现。
> 局限与区别：不支持元数据位和双花识别；本文扩展其NIBS构造至NIAT。

[19] Fuchsbauer 等. Structure-preserving signatures on equivalence classes and constant-size anonymous credentials. **Journal of Cryptology 2019** [Google Scholar](https://scholar.google.com/scholar?q=Structure-preserving+signatures+on+equivalence+classes+and+constant-size+anonymous+credentials)
> 核心思路：提出SPS-EQ签名方案，支持等价类签名与随机表示变换。
> 局限与区别：仅提供基本签名功能；本文将其用作NIAT的底层原语。

[16] Baldimtsi 等. Non-interactive blind signatures: Post-quantum and stronger security. **ASIACRYPT 2024** [Google Scholar](https://scholar.google.com/scholar?q=Non-interactive+blind+signatures%3A+Post-quantum+and+stronger+security)
> 核心思路：基于格的非交互式盲签名，提供后量子安全性。
> 局限与区别：参数较大，效率不如SPS-EQ方案；本文选择更为高效的SPS-EQ路线。

[17] Hanzlik 等. Non-interactive blind signatures from RSA assumption and more. **EUROCRYPT 2025** [Google Scholar](https://scholar.google.com/scholar?q=Non-interactive+blind+signatures+from+RSA+assumption+and+more)
> 核心思路：基于RSA的非交互式盲签名，依赖PKI基础设施。
> 局限与区别：客户端公钥需来自标准PKI，灵活性较低；本文允许客户端注册自定义密钥。

[9] Benhamouda 等. Publicly verifiable anonymous tokens with private metadata bit. **ePrint 2022/004** [Google Scholar](https://scholar.google.com/scholar?q=Publicly+verifiable+anonymous+tokens+with+private+metadata+bit)
> 核心思路：提出公开可验证的匿名令牌并支持私有元数据位，但仍为交互式。
> 局限与区别：需要3轮交互；本文仅需1轮非交互式颁发。

### 核心技术与方案

本文的核心构造分为两个层次：基础NIAT（Section 4）和带双花识别的NIAT（Section 5）。两者均基于结构保持签名与等价类（SPS-EQ）[19]和非交互式零知识证明（NIZK）。

**基础NIAT构造思路**：扩展Hanzlik的NIBS方案[15]，在发行者生成的预签名中嵌入一个私有元数据位$b \in \{0,1\}$。具体地，发行者拥有密钥对$(\mathsf{ek}_I, \mathsf{sk}_I)$，其中$\mathsf{ek}_I = (x_1, x_2) \in (\mathbb{Z}_p^*)^2$用于编码位，$\mathsf{sk}_I = (y_1, y_2, y_3) \in (\mathbb{Z}_p^*)^3$用于SPS-EQ签名。客户端拥有密钥对$(\mathsf{pk}_C = g_1^\alpha, \mathsf{sk}_C = \alpha)$。发行者生成一个随机数$r \leftarrow \{0,1\}^\lambda$，计算$R = H(r)$（$H$为随机预言机），$S = R^{(1-b)x_1 + b x_2}$，然后对向量$( \mathsf{pk}_C, R, S )$运行SPS-EQ签名得到$\overline{\sigma}$，并附上NIZK证明$\pi$（证明$b \in \{0,1\}$且满足公钥关系）。预签名$\mathsf{psig} = (\overline{\sigma}, S, \pi)$和随机数$\mathsf{nonce} = r$发送给客户端。客户端验证$\pi$和$\overline{\sigma}$后，通过SPS-EQ的$\mathsf{ChRep}$算法将签名重新随机化到$(g_1, R^{\alpha^{-1}}, S^{\alpha^{-1}})$上，得到令牌$(t = (t_1, t_2), \sigma)$，其中$t_1 = H(r)^{\alpha^{-1}}$，$t_2 = S^{\alpha^{-1}}$。验证时，公开验证$\sigma$是否为$(g_1, t_1, t_2)$的有效SPS-EQ签名。位提取时，检查$t_1^{x_{1+b}} \stackrel{?}{=} t_2$输出$b$。安全性依赖逆DDH假设、SPS-EQ的EUnf-CMA安全性和NIZK的零知识性。

**双花识别扩展**（Section 5）：在基础构造基础上，修改签名的消息为$(g_1, \mathsf{pk}_C \cdot g_1^{\hat{r}}, R, S)$，其中$\hat{r} = H_{\mathbb{Z}}(r)$。客户端生成令牌时，将$(\alpha + \hat{r})^{-1}$作为指数变换，并额外计算一个ElGamal加密$\phi$，加密其身份标识id，附上NIZK证明$\pi_{\circ}$。当同一令牌被两次使用（即相同的$t$但不同的$\sigma$）时，任何人都可以公开计算$(\phi_2^{-1} \cdot \phi_2')^{(\mathrm{id}' - \mathrm{id})^{-1}} = g_1^{\alpha + \hat{r}}$，从而识别出客户端公钥$\mathsf{pk}_C$。该性质在逆DDH、SPS-EQ和NIZK的可靠性假设下证明。

**复杂度**：通信量上，预签名约464字节（含3个$G_1$元素、1个$G_2$元素、6个整数和随机数），令牌约288字节（4个$G_1$元素、1个$G_2$元素）。计算量上（经批量配对优化），发行者平均每令牌约0.94 ms，客户端令牌生成约1.4 ms（摊销），验证约1.2 ms（摊销），位提取额外0.06 ms。

### 核心公式与流程

**[SPS-EQ签名与验证（[19]方案）]**
$$\begin{aligned}
&\text{Sign}(\mathsf{sk}_{\mathsf{EQ}} = (x_1,\dots,x_\ell), \mathbf{m}):\quad \nu \leftarrow \mathbb{Z}_p^*,\ Z := (\prod_i m_i^{x_i})^\nu,\ Y_1 := g_1^{1/\nu},\ Y_2 := g_2^{1/\nu},\ \sigma := (Z,Y_1,Y_2)\\
&\text{Verify}(\mathsf{pk}_{\mathsf{EQ}} = (g_2^{x_1},\dots,g_2^{x_\ell}), \mathbf{m}, \sigma):\quad \prod_i \mathsf{e}(m_i, g_2^{x_i}) \stackrel{?}{=} \mathsf{e}(Z, Y_2)\ \land\ \mathsf{e}(Y_1, g_2) \stackrel{?}{=} \mathsf{e}(g_1, Y_2)
\end{aligned}$$
> 作用：用于生成对消息向量$\mathbf{m}$的等价类签名，支持随机表示变换。

**[NIAT预签名发行（Issuer）]**
$$
\begin{aligned}
&r \leftarrow \{0,1\}^\lambda,\ R := H(r),\ S := R^{(1-b)x_1 + b x_2}\\
&\overline{\sigma} \leftarrow \text{EQ.Sign}((y_1,y_2,y_3),\ (\mathsf{pk}_C, R, S))\\
&\pi \leftarrow \text{NIZK.Prove}(\text{crs},\ x:=(\mathsf{pk}_I, R, S),\ w:=(\mathsf{ek}_I, \mathsf{sk}_I, b))\\
&\mathsf{psig} := (\overline{\sigma}, S, \pi),\ \mathsf{nonce} := r
\end{aligned}
$$
> 作用：发行者离线生成预签名，以非交互方式嵌入私有位$b$。

**[客户端令牌生成（Obtain）]**
$$
\begin{aligned}
&R := H(r),\ \mathbf{m} := (\mathsf{pk}_C, R, S)\\
&\text{若 NIZK.Verify 或 EQ.Verify 失败，则返回 }\perp\\
&t := (R^{\alpha^{-1}}, S^{\alpha^{-1}}),\ \sigma \leftarrow \text{EQ.ChRep}(\mathbf{m}, \overline{\sigma}, \alpha^{-1})
\end{aligned}
$$
> 作用：客户端利用私钥$\alpha$从预签名中提取最终令牌$(t, \sigma)$。

**[公开验证（Verify）]**
$$
\text{EQ.Verify}((\mathsf{pk}_I^{(3)},\mathsf{pk}_I^{(4)},\mathsf{pk}_I^{(5)}),\ (g_1, t_1, t_2), \sigma)
$$
> 作用：任何人可验证令牌有效性。

**[位提取（ReadBit）]**
$$
\text{for each } b \in \{0,1\}:\ \text{若 } t_1^{\mathsf{ek}_I^{(1+b)}} = t_2,\ \text{则返回 } b;\ \text{否则 } \perp
$$
> 作用：只有持有提取密钥$\mathsf{ek}_I$者可读取嵌入位。

**[双花识别（DSIden）]**
$$
h := (\phi_2^{-1} \cdot \phi_2')^{(\mathrm{id}' - \mathrm{id})^{-1}},\ \text{在 aux 中查找使得 } h = \mathsf{pk}_C \cdot g_1^{\hat{r}} \text{ 的 } (\mathsf{pk}_C, \text{nonce})
$$
> 作用：当同一令牌被两次使用时，公开识别出客户端的公钥。

### 实验结果

实验基于C++实现（mcl库），BLS12-381曲线，Apple M3 Pro芯片，1000次运行平均值。单次操作时间：$G_1$指数运算0.047 ms，$G_2$指数运算0.088 ms，配对运算0.445 ms。发行者令牌生成0.94 ms，客户端预签名验证2.07 ms、NIZK证明验证0.83 ms、令牌最终化0.34 ms；验证方签名验证1.98 ms、位提取0.06 ms。批量验证（如一次处理30个预签名）可显著摊销：客户端每令牌验证时间从2.07 ms降至0.28 ms（批量30），0.24 ms（批量100）。令牌通信大小：预签名约464字节，令牌约288字节。与现有交互式方案[8][9][10]相比，本文非交互式牺牲少量计算开销（因SPS-EQ和NIZK），但在异步场景中消除了在线签名延迟，且支持公开验证与私有元数据位的独特组合。

### 局限性与开放问题

本文方案依赖随机预言机模型和知识密钥假设（KOSK），可进一步推广至标准模型或基于后量子假设（如格）的版本，以增强安全性基础。双花识别扩展需要线性搜索辅助数据集，虽然可通过高效索引优化，但存储成本随客户端数增长。此外，NIZK证明的大小（约6个整数）在当前椭圆曲线上尚可接受，但在带宽受限环境中仍有优化空间。

### 强关联论文

[1] Davidson 等. Privacy pass: Bypassing internet challenges anonymously. **PoPETs 2018** [Google Scholar](https://scholar.google.com/scholar?q=Privacy+pass%3A+Bypassing+internet+challenges+anonymously)
[8] Kreuter 等. Anonymous tokens with private metadata bit. **CRYPTO 2020** [Google Scholar](https://scholar.google.com/scholar?q=Anonymous+tokens+with+private+metadata+bit)
[9] Benhamouda 等. Publicly verifiable anonymous tokens with private metadata bit. **ePrint 2022/004** [Google Scholar](https://scholar.google.com/scholar?q=Publicly+verifiable+anonymous+tokens+with+private+metadata+bit)
[10] Chase 等. Anonymous tokens with stronger metadata bit hiding from algebraic MACs. **CRYPTO 2023** [Google Scholar](https://scholar.google.com/scholar?q=Anonymous+tokens+with+stronger+metadata+bit+hiding+from+algebraic+MACs)
[15] Hanzlik. Non-interactive blind signatures for random messages. **EUROCRYPT 2023** [Google Scholar](https://scholar.google.com/scholar?q=Non-interactive+blind+signatures+for+random+messages)
[16] Baldimtsi 等. Non-interactive blind signatures: Post-quantum and stronger security. **ASIACRYPT 2024** [Google Scholar](https://scholar.google.com/scholar?q=Non-interactive+blind+signatures%3A+Post-quantum+and+stronger+security)
[17] Hanzlik 等. Non-interactive blind signatures from RSA assumption and more. **EUROCRYPT 2025** [Google Scholar](https://scholar.google.com/scholar?q=Non-interactive+blind+signatures+from+RSA+assumption+and+more)
[19] Fuchsbauer 等. Structure-preserving signatures on equivalence classes and constant-size anonymous credentials. **Journal of Cryptology 2019** [Google Scholar](https://scholar.google.com/scholar?q=Structure-preserving+signatures+on+equivalence+classes+and+constant-size+anonymous+credentials)


## 关键词

+ 非交互式匿名令牌私有元数据位
+ NIAT非交互盲签名认证
+ SPS-EQ等价类结构保持签名
+ 匿名客户端认证信任信号
+ 双重使用检测匿名令牌扩展