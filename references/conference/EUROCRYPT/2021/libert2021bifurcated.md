---
title: "Bifurcated signatures: folding the accountability vs anonymity dilemma into a single private signing scheme"
doi: 10.1007/978-3-030-77883-5_18
标题简称:
论文类型: conference
会议简称: EUROCRYPT
发表年份: 2021
created: 2025-05-23 01:41:37
modified: 2025-05-23 01:42:47
---
## Bifurcated signatures: folding the accountability vs anonymity dilemma into a single private signing scheme

## 发表信息

+ [原文链接]()

## 作者

+ [Benoît Libert](Benoît%20Libert.md)
+ [Khoa Nguyen](Khoa%20Nguyen.md)
+ Thomas Peters
+ Moti Yung

## 笔记

### 背景与动机
匿名签名领域长期以来存在一个刚性对立：群签名 [18] 允许可信开启机构（OA）追溯签名者身份以实现问责，但牺牲了用户的绝对匿名性；环签名 [45] 则赋予用户无条件匿名性，但完全无法追责。这种“非此即彼”的二元选择在实际应用中并不理想——例如，在金融交易中，小额或同国交易应保护隐私，而大额跨境交易需可追溯；在数字图书馆中，浏览无害书籍应匿名，而访问危险内容则应可识别。现有方案如消息相关开启群签名 [46] 和可追责追踪签名 [32,33] 虽限制了开启权限，但仍无法实现“点对点”的细粒度控制，即用户匿名与否应由签名消息的具体内容和上下文（由谓词 P 定义）动态决定，而非由方案类型或当局单方固定。本文提出分叉匿名签名（BiAS），旨在将绝对匿名性和有条件可追踪性“折叠”进同一个签名方案中，且签名本身隐藏其属于哪个分支（分支隐藏性），从而填补了密码学中缺乏这种灵活且隐私友好的条件可追踪原语的空白。

### 相关工作

[18] Chaum D., van Heyst E. Group Signatures. **EUROCRYPT 1991** [Google Scholar](https://scholar.google.com/scholar?q=Group+Signatures)
> 核心思路：允许群成员匿名签名，但授权OA可追溯任何签名至其作者。
> 局限与区别：OA拥有无限制的追溯能力，用户始终无法获得绝对匿名性，与BiAS中用户可在合适场景下获得无条件匿名的目标相悖。

[45] Rivest R., Shamir A., Tauman Y. How to Leak a Secret. **ASIACRYPT 2001** [Google Scholar](https://scholar.google.com/scholar?q=How+to+Leak+a+Secret)
> 核心思路：用户无需注册，可自发选择环成员生成签名，提供无条件匿名性。
> 局限与区别：完全不提供任何问责机制，无法在需要时追溯恶意用户，与BiAS有条件追溯的设计理念不同。

[46] Sakai Y.等人. Group Signatures with Message-Dependent Opening. **Pairing 2012** [Google Scholar](https://scholar.google.com/scholar?q=Group+Signatures+with+Message-Dependent+Opening)
> 核心思路：引入消息依赖开启，OA只能开启与特定消息关联的签名，限制了开启范围。
> 局限与区别：OA仍可自由开启目标消息集的签名，用户无绝对匿名，且追溯与否不由上下文谓词自动判定。

[32, 33] Kohlweiss M., Miers I. Accountable Tracing Signatures. **PoPETs 2015** [Google Scholar](https://scholar.google.com/scholar?q=Accountable+Tracing+Signatures)
> 核心思路：允许极端情况共存：用户要么始终无条件匿名，要么始终可追溯，决定由用户加入系统时由当局做出。
> 局限与区别：追溯属性与用户绑定，而非点对点依赖消息，用户不被告知自身状态，与BiAS中用户知晓且有意识选择的理念相反。

[21] Garms L., Lehmann A. Group Signatures with Selective Linkability. **PKC 2019** [Google Scholar](https://scholar.google.com/scholar?q=Group+Signatures+with+Selective+Linkability)
> 核心思路：引入“转换器”可盲化签名并关联至假名，但OA在签名未盲化时始终可追溯。
> 局限与区别：仅提供计算匿名性，且OA权限强大，无法保证绝对匿名性。

### 核心技术与方案
**整体框架与安全模型**：BiAS方案定义了一个谓词族 P，用于决定每个签名是否应被追溯。当谓词 P(M, id, w) = 1 时，签名提供无条件匿名性，开启算法 Open 返回 ⊥；否则，签名为可追溯。方案必须满足分支隐藏性（外人无法判断签名分支）和分支可靠性（不存在签名可违反谓词判定）。安全性在动态群组模型（类Kiayias-Yung模型 [29]）下形式化为完全匿名性（含可追溯与不可追溯两个子情况）、抗误识别攻击（可追溯性）和抗诬陷攻击。

**通用构造**：构造基于四大原语：$\mathcal{R}_{\mathsf{NEQ}}$-lossy PKE方案（一种标签加密，满足注入/损耗双模式）、同态模糊承诺（HEC）方案 [27]、数字签名方案和双模式NIZK论证系统。核心思路如下：
1. 用户加入时生成签名密钥对 (sk_id, pk_id)，从群管理员（GM）获得证书 cert_id（GM对 (id, pk_id) 的签名）。
2. 签名时，生成一次性签名密钥对 (VK, SK)。使用 $\mathcal{R}_{\mathsf{NEQ}}$-lossy PKE加密对 (id, w) 得到密文 ct_(id,w)，其中标签为 VK。同时用 HEC 的方案生成对 (id, w) 的承诺 com_(id,w)。
3. 通过 HEC 的求值算法计算谓词结果 $c_{ev} = C_M(id, w)$ 以及证明 $\pi_{C,M}$。接着，使用标准lossy PKE加密 $(1-c_{ev})\cdot id$ 得到 ct_id。若 $c_{ev}=1$（即匿名分支），ct_id加密的是零向量，并与 id 统计无关；若 $c_{ev}=0$（可追溯分支），ct_id加密的是 id 本身。
4. 最后，用一次性签名密钥 SK 对 (ct_(id,w), com_(id,w), ct_id, π) 签名，并生成NIZK论证，证明所有环节（包括证书有效性、HEC评价正确性、签名合法性）的正确性。
最终签名 Σ = (VK, (ct_(id,w), com_(id,w), ct_id, π), sig)。

**安全性证明直觉**：分支可靠性通过一系列hybrid论证证明，从真实设置（HEC承诺统计隐藏、NIZK为ZK模式、$\mathcal{R}_{\mathsf{NEQ}}$密钥为损耗模式）逐步切换至可抽取设置（HEC承诺结合、NIZK为提取模式、$\mathcal{R}_{\mathsf{NEQ}}$密钥为注入模式）。完全匿名性则分别处理可追溯和不可追溯两种情形。在不可追溯情形（谓词=1）中，由于 ct_id 加密零向量，com_(id,w) 统计隐藏，且 $\mathcal{R}_{\mathsf{NEQ}}$ 密文在损耗密钥下也是统计隐藏的，因此签名与用户身份统计无关。在可追溯情形下，通过切换一次性签名密钥来模拟挑战密文，并利用 $\mathcal{R}_{\mathsf{NEQ}}$ 和lossy PKE的不可区分性以及NIZK的零知识性证明计算匿名性。

**复杂度**：签名长度主要受限于 $\mathcal{R}_{\mathsf{NEQ}}$ 密文（$O((\log N + |w|) \cdot \lambda^c)$ 比特，其中N为群组大小，c为常数）和NIZK论证的大小。得益于HEC的高效验证性质，签名长度与判定电路的大小无关，仅依赖电路深度。

### 核心公式与流程

**[用户加入]**
用户生成签名密钥对 (sk_id, pk_id)←Π^{sig}.Kg(1^λ)，发送 (id, pk_id, sig_id) 给GM，GM返回证书 cert_id = Π^{sig}.Sign(sk_sig, (id, pk_id))。
> 作用：注册用户，建立身份-证书绑定，用于后续签名验证。

**[签名生成]**
1. 生成一次性签名密钥：(VK, SK)←Π^{ots}.Kg(1^λ)。
2. 加密 (id, w)：ct_(id,w) = Π^{RLE}.Encrypt(pk_RLE, VK, (id, w); r_{id,w})。
3. HEC承诺：com_(id,w) = HEC.Commit(pp, ek, (id, w); r^{hec})。
4. 计算谓词结果：c_{ev} = C_M(id, w)，得到证明 π_{C,M} 和承诺 com_ev。
5. 加密追溯信息：ct_id = Π^{lpke}.Encrypt(pk_e, (1-c_{ev})·id; r^{lpke})。
6. 签名消息：σ←Π^{sig}.Sign(sk_id, (M, P, ct_(id,w)))。
7. NIZK论证：π←NIZK.Prove(ρ, x, w)，证明存在 (id, w, pk_id, cert_id, σ, 随机数等) 满足证书验证、签名验证和HEC验证等式。
8. 一次性签名：sig←Π^{ots}.Sign(SK, (ct_(id,w), com_(id,w), ct_id, π))。
输出 Σ = (VK, (ct_(id,w), com_(id,w), ct_id, π), sig)
> 作用：生成满足分支条件的可验证签名，其中各组件协同实现条件追溯和分支隐藏。

**[验证]**
解析 Σ，验证一次性签名 sig 的有效性，并检查NIZK论证 π 对于语句 x（包含 com_ev = HEC.Eval^{out}(ek, C_M, com_(id,w))）的正确性。
> 作用：确保签名由合法用户产生，且谓词求值过程诚实。

**[开启]**
使用 OA 密钥 sk_e 解密 ct_id 得到 t_id。若 t_id = 0^ℓ 返回⊥；否则在状态 St 中查找匹配的 id。
> 作用：在可追溯分支下提取签名者身份。

### 实验结果
原文为理论密码学构造论文，未提供具体实验数据或数值结果。该工作主要贡献在于概念定义、安全模型构建和通用构造，并给出了基于LWE和双线性对的标准模型下的可行性实例化。签名长度在基于配对的实例化中可实现与电路大小无关，具体比特复杂度为 O((log N + |w|) * λ^c)。由于未进行实现，无法提供与现有baseline的性能对比或运行时间数据。

### 局限性与开放问题
1. 基于LWE的实例化仅为可行性结果，效率较低，实用化需要更高效的基于格的零知识证明系统（如Fiat-Shamir-with-abort方法 [10, 37]）。
2. 特定谓词族（如NC¹电路）虽可由配对构造，但达到电路大小无关性仍依赖q-type假设，需要基于简单假设的HEC实现。
3. 论文提出更强的“非颠覆性匿名性”概念，但仅在随机预言机模型下可证，如何在实际模型下实现是开放问题。
4. 分叉密码学的思想是否可推广至其他密码学原语（如加密、承诺等）值得进一步探索。

### 强关联论文

[27] Katsumata S.等人. Exploring Constructions of Compact NIZKs from Various Assumptions. **CRYPTO 2019** [Google Scholar](https://scholar.google.com/scholar?q=Exploring+Constructions+of+Compact+NIZKs+from+Various+Assumptions)

[14] Boyle E.等人. Fully Leakage-Resilient Signatures. **EUROCRYPT 2011** [Google Scholar](https://scholar.google.com/scholar?q=Fully+Leakage-Resilient+Signatures)

[23] Gorbunov S.等人. Leveled Fully Homomorphic Signatures from Standard Lattices. **STOC 2015** [Google Scholar](https://scholar.google.com/scholar?q=Leveled+Fully+Homomorphic+Signatures+from+Standard+Lattices)

[25] Groth J., Sahai A. Efficient Non-interactive Proof Systems for Bilinear Groups. **EUROCRYPT 2008** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+Non-interactive+Proof+Systems+for+Bilinear+Groups)

[29] Kiayias A., Yung M. Secure Scalable Group Signature with Dynamic Joins and Separable Authorities. **International Journal of Security and Networks 2006** [Google Scholar](https://scholar.google.com/scholar?q=Secure+Scalable+Group+Signature+with+Dynamic+Joins+and+Separable+Authorities)

[34] Libert B.等人. Simulation-Sound Arguments for LWE and Applications to KDM-CCA2 Security. **ASIACRYPT 2020** [Google Scholar](https://scholar.google.com/scholar?q=Simulation-Sound+Arguments+for+LWE+and+Applications+to+KDM-CCA2+Security)

[24] Groth J.等人. Perfect Non-interactive Zero Knowledge for NP. **EUROCRYPT 2006** [Google Scholar](https://scholar.google.com/scholar?q=Perfect+Non-interactive+Zero+Knowledge+for+NP)

[42] Peikert C., Shiehian S. Non-interactive Zero Knowledge for NP from (Plain) Learning with Errors. **CRYPTO 2019** [Google Scholar](https://scholar.google.com/scholar?q=Non-interactive+Zero+Knowledge+for+NP+from+Plain+Learning+with+Errors)

[22] Gentry C.等人. Homomorphic Encryption from Learning with Errors: Conceptually-Simpler, Asymptotically-Faster, Attribute-Based. **CRYPTO 2013** [Google Scholar](https://scholar.google.com/scholar?q=Homomorphic+Encryption+from+Learning+with+Errors+Conceptually+Simpler+Asymptotically+Faster+Attribute+Based)

[44] Regev O. On Lattices, Learning with Errors, Random Linear Codes, and Cryptography. **STOC 2005** [Google Scholar](https://scholar.google.com/scholar?q=On+Lattices+Learning+with+Errors+Random+Linear+Codes+and+Cryptography)


## 关键词

+ 分叉匿名签名
+ 匿名性与问责性
+ 分支隐藏
+ 同态承诺
+ 格与双线性映射