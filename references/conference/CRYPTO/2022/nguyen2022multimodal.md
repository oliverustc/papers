---
title: "Multimodal private signatures"
标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 2022
created: 2025-05-23 01:12:39
modified: 2025-05-23 02:50:19
---

## Multimodal private signatures

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-15979-4_27)
+ [archive](https://eprint.iacr.org/2022/1008)

## 作者

+ [Khoa Nguyen](Khoa%20Nguyen.md)
+ Fuchun Guo
+ [Willy Susilo](Willy%20Susilo.md)
+ Guomin Yang

## 笔记

### 背景与动机
隐私保护签名系统面临“隐私 vs 问责”的根本矛盾：用户希望完全匿名，而权威机构需要能够追究恶意行为。现有方案要么赋予用户绝对匿名权（如环签名 [50]），要么允许权威无条件追溯用户全部身份（如群签名 [17]），两者都显得过于极端。2021年提出的分叉匿名签名（BiAS）[42] 首次允许用户自行选择签名是否可追溯，但追溯时仍会泄露完整的个人身份信息，对隐私的侵犯仍然严重。在许多实际场景中（如匿名交易、举报、调查），权威只需获知部分身份信息（如年龄、所属机构、国家等），而非全量身份。本文提出多模态私人签名（MPS），填补了“细粒度、可管控的信息披露”这一空白——签名者可预先决定披露哪一级别的部分身份信息，权威只能获得该部分信息而无法获取更多，从而实现了更平衡的隐私与问责。

### 相关工作

[17] Chaum and van Heyst. Group signatures. **EUROCRYPT 1991** [Google Scholar](https://scholar.google.com/scholar?q=Group+signatures+Chaum+van+Heyst+1991)
> 核心思路：群组成员可匿名签名，但开启权威能完全追溯签名者身份。
> 局限与区别：MPS将其推广为可只披露部分身份信息，而非全量。

[50] Rivest et al. How to leak a secret. **ASIACRYPT 2001** [Google Scholar](https://scholar.google.com/scholar?q=How+to+leak+a+secret+Rivest+2001)
> 核心思路：环签名提供无条件匿名，无任何追溯能力。
> 局限与区别：MPS通过引入披露函数，使得部分追溯成为可能。

[42] Libert et al. Bifurcated signatures: folding the accountability vs. anonymity dilemma into a single private signing scheme. **EUROCRYPT 2021** [Google Scholar](https://scholar.google.com/scholar?q=Bifurcated+signatures+Libert+2021)
> 核心思路：允许签名者选择“环签名模式”或“群签名模式”，且模式不可区分。
> 局限与区别：BiAS仅支持全有或全无的追踪，MPS将其扩展为任意细粒度的信息披露。

[8] Bootle et al. Short accountable ring signatures based on DDH. **ESORICS 2015** [Google Scholar](https://scholar.google.com/scholar?q=Short+accountable+ring+signatures+Bootle+2015)
> 核心思路：结合环签名与群签名功能，但两种模式是分离且可区分的。
> 局限与区别：MPS中不同披露级别是统一且不可区分的。

[32] Kiayias et al. Traceable signatures. **EUROCRYPT 2004** [Google Scholar](https://scholar.google.com/scholar?q=Traceable+signatures+Kiayias+2004)
> 核心思路：每次签名可被追踪到同一用户，但泄露的是完整身份。
> 局限与区别：MPS允许只泄露部分身份，且用户可控制披露程度。

[51] Sakai et al. Group signatures with message-dependent opening. **Pairing 2012** [Google Scholar](https://scholar.google.com/scholar?q=Group+signatures+with+message-dependent+opening+Sakai+2012)
> 核心思路：签名是否可追踪取决于消息内容，但追踪仍揭示全量身份。
> 局限与区别：MPS进一步将追踪结果限制为部分身份信息。

[36] Kohlweiss and Miers. Accountable metadata-hiding escrow: a group signature case study. **PoPETs 2015** [Google Scholar](https://scholar.google.com/scholar?q=Accountable+metadata-hiding+escrow+Kohlweiss+2015)
> 核心思路：通过可问责的托管实现部分元数据隐藏，但身份仍完全暴露。
> 局限与区别：MPS提供更灵活的部分身份信息披露机制。

[44] Maji et al. Attribute-based signatures. **CT-RSA 2011** [Google Scholar](https://scholar.google.com/scholar?q=Attribute-based+signatures+Maji+2011)
> 核心思路：签名者需满足特定属性策略才能签名，但属性本身不用于追溯。
> 局限与区别：MPS使用披露函数来释放部分身份信息而非属性。

[3] Bellare and Fuchsbauer. Policy-based signatures. **PKC 2014** [Google Scholar](https://scholar.google.com/scholar?q=Policy-based+signatures+Bellare+2014)
> 核心思路：签名需满足策略，但策略仅控制“能否签名”，不控制信息披露程度。
> 局限与区别：MPS的签名函数同时决定签名的可签署性和信息披露级别。

[7] Boneh et al. Functional encryption: a new vision for public-key cryptography. **Communications of the ACM 2012** [Google Scholar](https://scholar.google.com/scholar?q=Functional+encryption+a+new+vision+Boneh+2012)
> 核心思路：解密仅揭示明文的一个函数，而非全部明文。
> 局限与区别：本文指出MPS与功能加密概念相似，但技术构造上尚未建立直接联系，MPS仍沿用“签名-加密-证明”范式。

### 核心技术与方案

MPS系统关联一个签名函数集合 $\mathcal{F}$ 和一个披露函数集合 $\mathcal{G}=\{G_1,\dots,G_K\}$。签名函数 $F(M,w,\mathrm{id})$ 输出 $j\in[0,K]$：若 $j=0$ 则不可签署；否则签署后开启权威只能获得 $G_j(\mathrm{id})$。安全性要求有两方面：隐私性（针对两种敌手：不控制OA与控制OA）和不可伪造性（针对两种伪造者：追溯性敌手和非陷害性敌手）。由于原始算法不能直接判断 $(M^\star,F^\star,\Sigma^\star)$ 是否构成伪造，引入了辅助算法 SimSetup 和 Extract 来提取签名者身份和见证。

**通用构造**：采用经典的“签名-加密-证明”范式。用户加入时由GM签发证书 $\mathsf{cert}_\mathrm{id}$（对 $(\mathrm{id}\|\mathsf{upk})$ 的签名）。签署时生成一次性密钥对 $(otk,ovk)$，用用户秘密密钥 $usk$ 签署 $ovk$，计算 $j=F(M,w,\mathrm{id})$，加密 $G_j(\mathrm{id})$ 得到密文 $c$，然后生成NIZK论证证明满足以下关系：$c$ 正确加密了 $G_j(\mathrm{id})$，且 $\mathrm{id}$ 拥有合法证书，且 $j=F(M,w,\mathrm{id})\neq0$。最后用 $otk$ 对 $(M,F,c,\pi)$ 签署得到 $sig$，输出 $\Sigma=(ovk,c,\pi,sig)$。该通用构造的正确性、隐私性、不可伪造性可归约到所用普通签名、一次性签名、公钥加密和双模式NIZK的安全性。

**配对基构造**：针对特定签名函数（基于Pedersen承诺中的值 $w_1$ 落入四个区间）和四个披露函数（分别泄露 $\mathrm{id}$ 的不同分量）。利用 Groth-Sahai 证明系统证明承诺值范围，将 $w_1-A_i$ 转为二进制并添加额外比特指示区间索引，从而支持 $\mathbb{G}_1$ 中元素的提取。采用结构保持签名 [35]、Boneh-Boyen签名 [6]、tag-based PKE [34] 等组件。

**格基构造**：在随机预言机模型下基于 LWE 和 SIS 假设实现。使用 KTX 承诺 [31]、SIS 签名 [37]、GPV IBE [26] 经 CHK 变换得到的 CCA2 安全加密、以及 Stern 类 [52] 统计 ZK 论证框架 [40]。核心难点是零知识证明加密的明文字段 $\mathbf{y}=G_j(\mathrm{id})$，为此将 $W_1$ 与阈值比较转化为二元加法方程，并用两个比特 $f_0,f_1$ 编码 $j$，最终归结为模2的线性方程组，与模 $q$ 的格方程融合。整体签名大小 $\widetilde{O}(\lambda^2)$ 比特。

### 核心公式与流程

**[通用构造中的关系 $\mathcal{R}$]**
$$
\begin{array}{l} \mathcal{R} := \left\{ \begin{array}{l} \left(\operatorname{mpk}, \operatorname{opk}, \mathbf{c}, M, F, o v k\right), \left(\operatorname{id}, \operatorname{upk}, \operatorname{cert} _ {\operatorname{id}}, s, w, j, r\right): \end{array} \right. \\ (S. \operatorname{Ver} (\mathrm{upk}, o v k, s) = 1) \wedge (S. \operatorname{Ver} (\mathrm{mpk}, (\mathrm{id} \| \mathrm{upk}), \mathrm{cert} _ {\mathrm{id}}) = 1) \wedge \\ \left. \left(F (M, w, \mathrm{id}) = j\right) \wedge (j \in [ 1, K ]) \wedge (\mathbf{c} = \mathsf{E}. \mathsf{E n c} (\mathsf{o p k}, G _ {j} (\mathrm{id}); r)) \right\}. \\ \end{array}
$$
> 作用：定义签名者需向NIZK证明的语句，确保证书、一次性签名、函数计算和加密的正确性。

**[配对基构造中区间判断与披露的关系]**
$$
\begin{aligned}
b_1 & \iff (W_1 \geq A_1), \\
b_2 & \iff (W_1 \geq A_2), \\
b_3 & \iff (W_1 \geq A_3), \\
(f_0,f_1) & = 
\begin{cases}
(0,0) & \text{if } j=1,\\
(0,1) & \text{if } j=2,\\
(1,0) & \text{if } j=3,\\
(1,1) & \text{if } j=4,
\end{cases}
\end{aligned}
$$
> 作用：将值 $W_1$ 所属区间转化为二进制向量，从而允许使用 Groth-Sahai 证明系统证明二进制值并实现提取。

**[格基构造中用于证明 $\mathbf{y}=G_j(\mathrm{id})$ 的模2方程]**
$$
\mathbf{M}_2 \cdot \mathbf{p}_2 = \mathbf{u}_2 \pmod{2},
$$
> 作用：将披露函数、区间判断、加法进位等所有二进制关系编码为一个线性方程模2，与模 $q$ 的格方程（$\mathbf{M}_1 \cdot \mathbf{p}_1 = \mathbf{u}_1 \pmod{q}$）一同通过 Stern 类论证证明。

### 实验结果
本文是理论密码学论文，未提供实验实现或性能基准测试。所有构造的分析均为渐进复杂度估计：配对基构造使用标准模型下的 Groth-Sahai 证明，签名大小与所支持的区间数量线性相关；格基构造的公共参数大小为 $\widetilde{O}(\lambda^2)$ 比特，签名大小也为 $\widetilde{O}(\lambda^2)$ 比特，用户密钥大小为 $\widetilde{O}(\lambda)$ 比特。两组构造均未报告具体数值或与现有方案的比对，因为 MPS 是全新概念，尚无同类方案可比。

### 局限性与开放问题
本文仅给出了通用构造和两个具体实例（配对与格基），但披露函数局限于线性变换（如选择特定坐标的子集），尚未支持更复杂的表达式（如区间交集、多项式函数）。理论连接方面，MPS 与功能加密、全同态加密之间的深层关系仍不清楚，可能有助于构造更高效的方案。此外，目前的所有构造均未考虑公钥可验证开启、用户撤销等实际部署中重要的附加功能，且格基构造仅满足随机预言机模型，标准模型下的高效构造仍为开放问题。

### 强关联论文

[42] Libert et al. Bifurcated signatures: folding the accountability vs. anonymity dilemma into a single private signing scheme. **EUROCRYPT 2021** [Google Scholar](https://scholar.google.com/scholar?q=Bifurcated+signatures+Libert+2021)

[17] Chaum and van Heyst. Group signatures. **EUROCRYPT 1991** [Google Scholar](https://scholar.google.com/scholar?q=Group+signatures+Chaum+van+Heyst+1991)

[50] Rivest et al. How to leak a secret. **ASIACRYPT 2001** [Google Scholar](https://scholar.google.com/scholar?q=How+to+leak+a+secret+Rivest+2001)

[35] Kiltz et al. Structure-preserving signatures from standard assumptions, revisited. **CRYPTO 2015** [Google Scholar](https://scholar.google.com/scholar?q=Structure-preserving+signatures+from+standard+assumptions+revisited+Kiltz+2015)

[31] Kawachi et al. Concurrently secure identification schemes based on the worst-case hardness of lattice problems. **ASIACRYPT 2008** [Google Scholar](https://scholar.google.com/scholar?q=Concurrently+secure+identification+schemes+based+on+the+worst-case+hardness+of+lattice+problems+Kawachi+2008)

[37] Libert et al. Signature schemes with efficient protocols and dynamic group signatures from lattice assumptions. **ASIACRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=Signature+schemes+with+efficient+protocols+and+dynamic+group+signatures+from+lattice+assumptions+Libert+2016)

[26] Gentry et al. Trapdoors for hard lattices and new cryptographic constructions. **STOC 2008** [Google Scholar](https://scholar.google.com/scholar?q=Trapdoors+for+hard+lattices+and+new+cryptographic+constructions+Gentry+2008)

[40] Libert et al. Zero-knowledge arguments for lattice-based PRFs and applications to E-cash. **ASIACRYPT 2017** [Google Scholar](https://scholar.google.com/scholar?q=Zero-knowledge+arguments+for+lattice-based+PRFs+and+applications+to+E-cash+Libert+2017)

[30] Groth and Sahai. Efficient non-interactive proof systems for bilinear groups. **EUROCRYPT 2008** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+non-interactive+proof+systems+for+bilinear+groups+Groth+Sahai+2008)

[7] Boneh et al. Functional encryption: a new vision for public-key cryptography. **Communications of the ACM 2012** [Google Scholar](https://scholar.google.com/scholar?q=Functional+encryption+a+new+vision+Boneh+2012)


## 关键词

+ 密码学
+ 零知识
+ 协议