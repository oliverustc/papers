---
title: "Composable and modular anonymous credentials: Definitions and practical constructions"
标题简称:
论文类型: conference
会议简称: ASIACRYPT
发表年份: 2015
created: 2025-05-15 10:38:27
modified: 2025-05-26 05:05:15
---

## Composable and modular anonymous credentials: Definitions and practical constructions

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-662-48800-3_11)

## 作者

+ [Jan Camenisch](Jan%20Camenisch.md)
+ Maria Dubovitskaya
+ Kristiyan Haralambiev
+ [Markulf Kohlweiss](Markulf%20Kohlweiss.md)

## 笔记

### 背景与动机

匿名凭证系统需要支持多发行者、选择性属性披露和假名，同时保证不可链接性。早期的CL签名方案 [30,31] 虽然启发了大量隐私保护协议，但存在三大缺陷：非交互式证明依赖Fiat-Shamir启发式从而丧失随机预言机模型外的安全保证；在UC模型 [35] 中无法使用直通提取（straight-line extraction），被迫将离散对数形式的证据加密，代价高昂；签名证明的大小随属性数量线性增长。结构保持签名 [1–3] 与 Groth-Sahai 证明 [45] 的结合虽能避免随机预言机，但证明大小依然与属性数成线性关系，且常数因子更大。现有可编辑签名方案 [7,38,51,55] 要么效率过低，要么仅支持一次性凭证，要么缺乏形式化定义和可组合性。因此，本文旨在同时克服上述三大缺陷，构造首个高效、可组合、无需随机预言机且证明大小与属性数无关的匿名凭证系统。

### 相关工作

[7] Ahn, J.H., Boneh, D., Camenisch, J., Hohenberger, S., Shelat, A., Waters, B.: Computing on authenticated data. **TCC 2012** [Google Scholar](https://scholar.google.com/scholar?q=Computing+on+authenticated+data)
> 核心思路：提出同态签名框架，支持对已签名数据的任意函数计算。
> 局限与区别：其引用（quoting）操作效率低，尤其当属性向量长度大时，本文的向量承诺方案能实现常数大小证明。

[12] Belenkiy, M., Chase, M., Kohlweiss, M., Lysyanskaya, A.: P-signatures and non-interactive anonymous credentials. **TCC 2008** [Google Scholar](https://scholar.google.com/scholar?q=P-signatures+and+non-interactive+anonymous+credentials)
> 核心思路：基于P签名构造非交互匿名凭证，支持多个属性。
> 局限与区别：本文的URS方案效率几乎是其两倍，且P签名不支持多消息签名，而URS支持。

[29] Camenisch, J.L., Lysyanskaya, A.: An efficient system for non-transferable anonymous credentials with optional anonymity revocation. **EUROCRYPT 2001** [Google Scholar](https://scholar.google.com/scholar?q=An+efficient+system+for+non-transferable+anonymous+credentials)
> 核心思路：首个高效多-show匿名凭证方案，基于CL签名和Schnorr证明。
> 局限与区别：非交互式必须依赖随机预言机，且证明大小随属性线性增长，不支持UC安全。

[31] Camenisch, J.L., Lysyanskaya, A.: Signature schemes and anonymous credentials from bilinear maps. **CRYPTO 2004** [Google Scholar](https://scholar.google.com/scholar?q=Signature+schemes+and+anonymous+credentials+from+bilinear+maps)
> 核心思路：基于双线性映射的CL签名，支持多消息签名和高效证明。
> 局限与区别：同[29]，依赖随机预言机，线性大小，且不满足UC安全。

[38] Chase, M., Kohlweiss, M., Lysyanskaya, A., Meiklejohn, S.: Malleable signatures: new definitions and delegatable anonymous credentials. **CSF 2014** [Google Scholar](https://scholar.google.com/scholar?q=Malleable+signatures+new+definitions+and+delegatable+anonymous+credentials)
> 核心思路：形式化定义可控可编辑签名，包括模拟性、不可伪造性和上下文隐藏。
> 局限与区别：其构造效率极低，本文给出更具体、更高效的可实现定义，并利用向量承诺提升性能。

[47] Hanser, C., Slamanig, D.: Structure-preserving signatures on equivalence classes and their application to anonymous credentials. **ASIACRYPT 2014** [Google Scholar](https://scholar.google.com/scholar?q=Structure-preserving+signatures+on+equivalence+classes+and+their+application+to+anonymous+credentials)
> 核心思路：基于等价类的结构保持签名，实现常数大小凭证证明。
> 局限与区别：其方案仅在通用群模型中安全，且使用哈希函数编码属性，无法支持高效的协议设计（如Groth-Sahai证明），本文方案在标准假设下安全且与Groth-Sahai兼容。

[50] Izabachène, M., Libert, B., Vergnaud, D.: Block-wise P-signatures and non-interactive anonymous credentials with efficient attributes. **IMACC 2011** [Google Scholar](https://scholar.google.com/scholar?q=Block-wise+P-signatures+and+non-interactive+anonymous+credentials+with+efficient+attributes)
> 核心思路：将向量承诺与P签名结合，降低证明大小。
> 局限与区别：其方案不满足本文定义的安全性（如不可伪造性和不可链接性），且未证明可组合安全。

[51] Kate, A., Zaverucha, G.M., Goldberg, I.: Constant-size commitments to polynomials and their applications. **ASIACRYPT 2010** [Google Scholar](https://scholar.google.com/scholar?q=Constant-size+commitments+to+polynomials+and+their+applications)
> 核心思路：提出多项式承诺，实现常数大小的向量承诺。
> 局限与区别：原始方案缺少打开不可伪造性（opening non-malleability），本文对其修改并添加因子 x 以解决该问题。

[55] Kohlweiss, M., Rial, A.: Optimally private access control. **WPES 2013** [Google Scholar](https://scholar.google.com/scholar?q=Optimally+private+access+control)
> 核心思路：利用向量承诺实现一次性凭证。
> 局限与区别：仅支持一次性展示，且方案需要交互，本文支持多-show且非交互。

### 核心技术与方案

本文提出不可链接可编辑签名（URS）作为构建匿名凭证的核心原语，其构造分为三个层次：底层向量承诺、中层URS方案、上层匿名凭证系统。各层设计如下：

**1. 改进的向量承诺方案**

基础是Kate等人的多项式承诺 [51]，但为满足打开不可伪造性（opening non-malleability）进行了关键修改。设双线性群参数 $grp = (p, \mathbb{G}, \tilde{\mathbb{G}}, \mathbb{G}_t, e, G, \tilde{G})$，选取随机 $\alpha \in \mathbb{Z}_p$，公开参数 $pp$ 包含 $G^{\alpha^i}$ 和 $\tilde{G}^{\alpha^i}$（$i=1,\dots,n+1$）。对消息向量 $\boldsymbol{m} = (m_1,\dots,m_n) \in \mathbb{Z}_p^n$，定义拉格朗日多项式 $f_i(x) = \prod_{j \neq i} (x-j)/(i-j)$，则承诺为 $C = \prod_{i=1}^n F_i^{m_i} \cdot P^r$，其中 $F_i = G^{f_i(\alpha)}$，$P = G^{p(\alpha)}$，$p(x)=x \prod_{i=1}^n (x-i)$，$r$ 为随机盲化因子。对子集 $I \subseteq [1,n]$，打开证据为 $W = G^{\frac{f(\alpha)-f_I(\alpha)+r\cdot p(\alpha)}{p_I(\alpha)}}$，其中 $p_I(x) = x \prod_{i \in I} (x-i)$。验证方程：$e(C, \tilde{G}) = e(W, \tilde{P}_I) \cdot e(\prod_{i\in I} F_i^{m_i}, \tilde{G})$，其中 $\tilde{P}_I = \tilde{G}^{p_I(\alpha)}$。引入因子 $x$ 到 $p_I(x)$ 确保了当 $I=\emptyset$ 时无法利用承诺本身作为打开证据，从而满足打开不可伪造性（基于 $n$-RootDH 假设）。满批次绑定基于 $(n+1)$-BSDH 假设。

**2. URS 方案构造**

URS.SGen 生成双线性群参数、向量承诺参数 $pp$ 和证明系统 CRS。URS.Kg 调用结构保持签名 (SPS) 的密钥生成，输出 $pk = (pk_{sps}, SP)$。URS.Sign 对消息 $\boldsymbol{m}$ 计算承诺 $C$，并用 SPS 签名 $C$，得到 $\sigma = (\Sigma, C, r)$。URS.Derive 根据子集 $I$ 计算打开 $W$，可选随机化 $\Sigma$，然后生成零知识证明 $\pi$，证明存在 $(C, W, \psi_{wit}(\Sigma'))$ 使得 SPS.Verify 和 VC.Check 同时成立。输出 $\sigma_I = (\psi_{rnd}(\Sigma'), \pi)$。URS.Verify 验证 $\pi$ 和 VC.Check。不可伪造性依赖 SPS 的不可伪造性、向量承诺的批次绑定和打开不可伪造性以及证明系统的可提取性。不可链接性由证明系统的证据不可区分性保证（证明中隐藏了 $C$ 和 $r$ 等信息）。

为满足 UC 要求，需添加密钥提取能力：URS.Kg 额外生成一个 NIZK 证明 $\pi_{sk}$，证明 $\exists (sk^*, r)$ 使得 $(pk^*, sk^*) = URS^*.Kg(SP^*; r)$。URS.SGenT 使用模拟设置生成 CRS 和提取陷门。URS.ExtractKey 通过提取 $\pi_{sk}$ 获得秘密密钥。这通过全结构保持签名 (FSPS) [5] 实现高效提取，额外开销约 15-18 个群元素。

**3. 匿名凭证系统**

将 URS 扩展为用户密钥和假名。用户生成秘密 $X = G^x$，假名 $P$ 是对 $X$ 的结构保持承诺。Issuer 使用 URS.Sign 对 $(P, Y_{\text{Cred}}, \boldsymbol{a})$ 签名（其中 $Y_{\text{Cred}}$ 是难题实例的公钥）。凭证展示时，用户运行 URS.Derive 得到签名 $\sigma_I$，并生成零知识证明 $\pi_{X,\text{Cred}}$，证明：她知道秘密 $X$ 和承诺打开，$\sigma_I$ 是对包含 $P$ 和 $Y_{\text{Cred}}$ 的向量在子集 $I$ 上的有效签名，且 $X_{\text{Cred}}$ 满足难题关系。证明通过模拟可提取的 NIZK 实现，上下文 $cxt$ 作为标签防止重放。安全证明依赖于 URS 的性质、承诺的绑定性和隐藏性、以及证明系统的模拟可提取性。

复杂性：凭证证明大小约为 178 个群元素（约 11 KB 在 128 位安全级别），与属性总数 $n$ 无关，仅与展示的属性数 $|I|$ 有关（通过向量承诺打开大小恒为 1 个群元素，但证明中的 Groth-Sahai 证明大小与 $|I|$ 成线性，不过常数因子很小，$|I|$ 通常远小于 $n$）。

### 核心公式与流程

**向量承诺验证方程**
$$ e(C, \tilde{G}) = e(W, \tilde{P}_I) \cdot e\Bigl(\prod_{i\in I} F_i^{m_i}, \tilde{G}\Bigr) $$
> 作用：用于验证承诺 $C$ 在子集 $I$ 上对消息 $m_i$ 的打开 $W$ 是否正确。其中 $\tilde{P}_I = \tilde{G}^{p_I(\alpha)}$，$p_I(x)=x\prod_{i\in I}(x-i)$，$F_i = G^{f_i(\alpha)}$。

**URS 签名生成**
$$ C = \prod_{i=1}^n F_i^{m_i} \cdot P^r,\quad \Sigma \leftarrow \mathsf{SPS.Sign}(sk_{sps}, C) $$
> 作用：对消息向量 $\boldsymbol{m}$ 计算多项式承诺 $C$（随机盲化因子 $r$），并用结构保持签名对承诺签名。

**URS 派生证明**
$$ \pi \leftarrow \Pi.\mathsf{Prove}\bigl(CRS;\, (C, W, \psi_{wit}(\Sigma'));\; \mathsf{SPS.Verify}(pk_{sps},\Sigma',C)=1 \land \mathsf{VC.Check}(pp,C,\boldsymbol{m}_I,W)=1 \bigr) $$
> 作用：生成证据不可区分证明，证明拥有一个有效的承诺打开和一个有效的结构保持签名，同时隐藏承诺值和打开信息，实现不可链接性。

**凭证展示证明语句**
$$ \begin{aligned}
\exists &(X, P, aux(P), aux(P)', Y_{\text{Cred}}, X_{\text{Cred}}):\\
&\mathsf{NymVerify}(SP, X, P', aux(P)') = 1 \;\land\; \mathsf{NymVerify}(SP, X, P, aux(P)) = 1\\
&\land\; \mathsf{URS.Verify}(pk, \sigma_I, (P, Y_{\text{Cred}}, \boldsymbol{a})_I) = 1\\
&\land\; \mathcal{V}_{\mathsf{Rgap}}(X_{\text{Cred}}, Y_{\text{Cred}}) = 1
\end{aligned} $$
> 作用：用户向验证者证明她拥有一个凭证，可以揭示属性子集 $\boldsymbol{a}_I$，同时承诺的用户秘密 $X$ 与展示假名 $P'$ 和凭证中假名 $P$ 一致，且满足难题关系。

**UC 凭证功能的关键检查**
$$\begin{aligned}
&\text{Verify 步骤中，如果} \; pk = pk' \land \lnot \text{keyleak} \land \text{User 诚实，则：}\\
&\text{从证明中提取} (X', aux(P)'), \text{检查} \;\mathsf{NymVerify}(SP, P', X', aux(P)') = 1;\\
&\text{若} \; \exists (\text{ISS}, \mathcal{U}, X', \boldsymbol{a}) \in \mathcal{M}_{\text{ISS}} \text{且用户} \mathcal{U} \text{被腐蚀且} \boldsymbol{a}_I = \boldsymbol{a}_I', \text{输出 1；否则 0。}
\end{aligned}$$
> 作用：在 UC 模型中防止混合匹配攻击——只有提取到的秘密 $X'$ 与假名 $P'$ 一致，且该秘密确实获得了对应属性的凭证（来自被腐蚀用户），证明才被接受。

### 实验结果

论文未进行传统实验，但提供了详细的效率分析和数值估计。在 128 位安全级别，采用 SXDH 假设，使用 Groth-Sahai 证明和 FSPS [5] 时，凭证证明大小约为 178 个群元素（约 11 KB）；若改用非 UC 版本的 SPS [2]，可降至 148 个群元素（约 9 KB）。与 Idemix [31] 相比，Idemix 的证明大小随属性数线性增长（例如 10 个属性约 5 KB 但需 RSA 群组，实际带宽相近但安全假设更弱且依赖随机预言机），而本方案证明大小与属性总数无关，仅与展示属性数弱线性相关（通过 Groth-Sahai 证明中的乘积项）。与 Izabachène 等 [50] 的 8 KB 证明相比，本方案的 UC 安全版本更大，但提供了更强的可组合安全保证。与 Hanser-Slamanig [47] 的约 1 KB 证明相比，本方案虽然更大，但依赖标准假设且兼容 Groth-Sahai 证明，便于进一步协议设计。凭证签发阶段（Sign）的计算量与属性总数 $n$ 成线性（需计算承诺和签名），但实际中 $n$ 通常不大。展示阶段（Prove）的计算量主要来自 Groth-Sahai 证明，与 $|I|$ 成线性，约 $O(|I|)$ 个配对运算。在 128 位安全水平下，整个协议可在普通笔记本上数秒内完成。

### 局限性与开放问题

当前方案的凭证证明大小虽然与属性总数无关，但比基于等价类签名的最优方案 [47] 大约一个数量级，如何结合两者的优势（即标准假设下实现 [47] 的效率）是一个开放问题。另外，向量承诺的打开不可伪造性基于非标准的 $n$-RootDH 假设，将其归约到更标准的假设（如 CDH 或 SXDH）值得研究。论文还指出，缺乏打开不可伪造性可能被用于攻击现有构造，但尚未有具体攻击示例，这为后续工作提供了方向。

### 强关联论文

[5] Abe, M., Kohlweiss, M., Ohkubo, M., Tibouchi, M.: Fully structure-preserving signatures and shrinking commitments. **EUROCRYPT 2015** [Google Scholar](https://scholar.google.com/scholar?q=Fully+structure-preserving+signatures+and+shrinking+commitments)

[12] Belenkiy, M., Chase, M., Kohlweiss, M., Lysyanskaya, A.: P-signatures and non-interactive anonymous credentials. **TCC 2008** [Google Scholar](https://scholar.google.com/scholar?q=P-signatures+and+non-interactive+anonymous+credentials)

[29] Camenisch, J.L., Lysyanskaya, A.: An efficient system for non-transferable anonymous credentials with optional anonymity revocation. **EUROCRYPT 2001** [Google Scholar](https://scholar.google.com/scholar?q=An+efficient+system+for+non-transferable+anonymous+credentials)

[31] Camenisch, J.L., Lysyanskaya, A.: Signature schemes and anonymous credentials from bilinear maps. **CRYPTO 2004** [Google Scholar](https://scholar.google.com/scholar?q=Signature+schemes+and+anonymous+credentials+from+bilinear+maps)

[38] Chase, M., Kohlweiss, M., Lysyanskaya, A., Meiklejohn, S.: Malleable signatures: new definitions and delegatable anonymous credentials. **CSF 2014** [Google Scholar](https://scholar.google.com/scholar?q=Malleable+signatures+new+definitions+and+delegatable+anonymous+credentials)

[45] Groth, J., Sahai, A.: Efficient non-interactive proof systems for bilinear groups. **EUROCRYPT 2008** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+non-interactive+proof+systems+for+bilinear+groups)

[47] Hanser, C., Slamanig, D.: Structure-preserving signatures on equivalence classes and their application to anonymous credentials. **ASIACRYPT 2014** [Google Scholar](https://scholar.google.com/scholar?q=Structure-preserving+signatures+on+equivalence+classes+and+their+application+to+anonymous+credentials)

[50] Izabachène, M., Libert, B., Vergnaud, D.: Block-wise P-signatures and non-interactive anonymous credentials with efficient attributes. **IMACC 2011** [Google Scholar](https://scholar.google.com/scholar?q=Block-wise+P-signatures+and+non-interactive+anonymous+credentials+with+efficient+attributes)

[51] Kate, A., Zaverucha, G.M., Goldberg, I.: Constant-size commitments to polynomials and their applications. **ASIACRYPT 2010** [Google Scholar](https://scholar.google.com/scholar?q=Constant-size+commitments+to+polynomials+and+their+applications)


## 关键词

+ 匿名凭证
+ UC安全
+ 不可链接可编辑签名
+ 选择性属性披露
+ 可组合密码学
+ 多发行者系统