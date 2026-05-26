---
title: "Everlasting Anonymous Rate-Limited Tokens"
标题简称:
论文类型: preprint
预印本简称: archive
发表年份: 2025
created: 2025-06-09 09:20:55
modified: 2025-06-09 10:24:31
---

## Everlasting Anonymous Rate-Limited Tokens

## 发表信息

+ [原文链接](https://eprint.iacr.org/2025/1030)

## 作者

+ Rutchathon Chairattana-Apirom
+ [Nico Döttling](Nico%20D%C3%B6ttling.md)
+ [Anna Lysyanskaya](Anna%20Lysyanskaya.md)
+ Stefano Tessaro

## 笔记

### 背景与动机

匿名限速令牌是一类特殊的凭证，允许用户通过一次签发获得一个“令牌分发器”，并从中生成至多 \(k\) 个不可关联且公开可验证的令牌。每个令牌与一个上下文（如服务名称）绑定，且同一上下文下最多可生成 \(N\) 个令牌；若超过该数量，用户身份会被暴露。这类令牌在隐私保护认证系统（如 Privacy Pass [22]）和电子现金中具有重要应用。Camenisch 等人 [14,12] 首次给出了基于 PRF、签名和零知识证明的构造，但其匿名性仅对计算有界敌手成立。随着量子计算的发展，“先存储、后破解”的存储-现在-解密-后来攻击对已生成的令牌的隐私构成威胁：即使当前无法破解，量子计算机在未来可能通过逆向 PRF 等手段关联不同令牌或将其与签发会话联系起来。本文旨在实现**永恒匿名性**（everlasting anonymity），即令牌的不可关联性对计算无界敌手也成立，同时保持其他安全性质（如不可伪造性）的计算安全性。这样，即使未来量子计算机出现，之前存储的令牌的隐私仍无法被攻破。文章采用双线性配对群，利用现有代数工具保证效率，同时避免完全依赖后量子假设带来的高昂开销。

### 相关工作

[12] Camenisch 等. How to win the clonewars: efficient periodic n-times anonymous authentication. **CCS 2006** [Google Scholar](https://scholar.google.com/scholar?q=How+to+win+the+clonewars%3A+efficient+periodic+n-times+anonymous+authentication)  
> 核心思路：提出基于 PRF、签名和零知识证明的限速令牌构造（CHKLM），令牌序列号通过 PRF 计算，双花检测通过线性方程恢复用户公钥。  
> 局限与区别：匿名性仅计算安全，无法抵抗无界敌手；本文通过替换 PRF 为统计伪随机函数族实现永恒匿名性。

[14] Camenisch 等. Balancing accountability and privacy using E-cash. **SCN 2006** [Google Scholar](https://scholar.google.com/scholar?q=Balancing+accountability+and+privacy+using+E-cash)  
> 核心思路：基于上下文限制的电子现金系统，引入伪随机函数种子 \(s\)，序列号 \(sn = F_s(\text{ctxt}, i)\) 限制每商户最多 \(N\) 个硬币。  
> 局限与区别：使用计算安全的 PRF；本文采用 Pagh-Pagh 函数族，利用 KZG 承诺和 Groth-Sahai 证明实现统计隐藏。

[32] Kate 等. Constant-size commitments to polynomials and their applications. **ASIACRYPT 2010** [Google Scholar](https://scholar.google.com/scholar?q=Constant-size+commitments+to+polynomials+and+their+applications)  
> 核心思路：提出 KZG 多项式承诺方案，支持对多项式求值的常量大小证明。  
> 本文用它承诺函数键中的多项式（如 \(f_1, f_2, g\)）和向量（通过插值），$O(1)$ 大小打开证明。

[2] Abe 等. Structure-preserving signatures and commitments to group elements. **CRYPTO 2010** [Google Scholar](https://scholar.google.com/scholar?q=Structure-preserving+signatures+and+commitments+to+group+elements)  
> 核心思路：定义结构保持签名（SPS），公钥、消息和签名均为源群元素，验证可表达为双线性方程。  
> 本文用 SPS 签发用户承诺的令牌分发器，与 Groth-Sahai 证明结合实现知识证明。

[29] Groth, Sahai. Efficient non-interactive proof systems for bilinear groups. **EUROCRYPT 2008** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+non-interactive+proof+systems+for+bilinear+groups)  
> 核心思路：给出针对双线性群中方程（配对积、多标量乘、二次）的 NIZK 证明系统，可绑定或隐藏。  
> 本文用它证明令牌展示中的正确性方程（R.2-R.8），并在隐藏模式下实现统计零知识。

[7] Berman 等. Hardness-preserving reductions via cuckoo hashing. **J. Cryptol. 2019** [Google Scholar](https://scholar.google.com/scholar?q=Hardness-preserving+reductions+via+cuckoo+hashing)  
> 核心思路：利用布谷哈希构造统计伪随机函数族。  
> 本文采用 Pagh-Pagh [34] 函数族（二阶独立哈希 + 表），在 \(S = 8k\) 下对 \(k\) 个查询不可与随机函数区分。

[10] Bünz 等. Bulletproofs: short proofs for confidential transactions and more. **S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Bulletproofs%3A+short+proofs+for+confidential+transactions+and+more)  
> 核心思路：给出简洁的非交互范围证明。  
> 本文的截断证明 \(\Pi_{\text{trunc}}\) 采用类似技术，结合压缩 Σ-协议 [4] 证明比特分解和取模的正确性。

[4] Attema, Cramer. Compressed Σ-protocol theory and practical application to plug & play secure algorithmics. **CRYPTO 2020** [Google Scholar](https://scholar.google.com/scholar?q=Compressed+%CE%A3-protocol+theory+and+practical+application+to+plug+%26+play+secure+algorithmics)  
> 核心思路：提出压缩 Σ-协议框架，可将算术电路证明转化为仅含线性方程的交互证明。  
> 本文用它高效实现 \(O(\lambda)\) 大小的范围证明和截断证明。

### 核心技术与方案

**整体框架**：EARLT 由 Setup、IKGen、UKGen、发行协议（User1, I, User2）、展示协议（Show）、验证（V）和识别（Identify）组成。Setup 生成双线性配对群参数和多个 CRS：KZG（含无界隐藏变体）、向量承诺 VCKZG、Groth-Sahai（隐藏模式）、以及两个辅助证明系统 \(\Pi_{\text{lin}}\) 和 \(\Pi_{\text{trunc}}\)。发行者密钥为 SPS 的密钥对，用户密钥为 \(sk_U \in \mathbb{Z}_p, pk_U = sk_U G_1\)。

**发行协议**：用户首先生成一个 Pagh-Pagh 函数族密钥 key，包含两个度 \(d=\Theta(\lambda)\) 的多项式 \(f_1, f_2\)、三个多项式 \(g_1,g_2,g_3\) 以及两个表 \(T_1,T_2 \in (\mathbb{Z}_p^3)^{8k}\)。用户用 KZGPed 承诺多项式 \(f_j, g_i\)，用 VCKZG 承诺两个表（每个表 \(3 \times 8k\) 个元素），然后将所有承诺 \(C\) 发送给发行者。发行者随机选取两个二维重随机化因子 \(\gamma_0, \gamma_1 \in \mathbb{Z}_p^2\)，计算承诺 \(C_\gamma = \sum_{i=1}^2 \gamma_{0,i} H_i + \gamma_{1,i} H_{2+i}\)，并用 SPS 签署 \((pk_U, C, C_\gamma)\)。用户验证签名后存储令牌分发器 \(D\)，包含密钥、所有承诺、签名、\(\gamma_0,\gamma_1\) 及上下文计数器。

**展示与验证**：用户对上下文 ctxt 维护计数器 cnt（初始 0），计算 \(x = \text{ctxt} \cdot N + \text{cnt}\)。然后评估函数：\(y_j = f_j(x), \bar y_j = y_j \pmod{8k}\)，查表得 \(t_{j,i} = T_{j,i}[\bar y_j]\)，计算 \(z_i = g_i(x)\)。序列号和双花方程定义为
\[
sn = (t_{1,1}+t_{2,1}+z_1, t_{1,2}+t_{2,2}+z_2) + cnt \cdot \gamma_0 + \gamma_1 \in \mathbb{Z}_p^2, \quad dbsp = sk_U + r \cdot (t_{1,3}+t_{2,3}+z_3),
\]
其中 \(r\) 是验证者提供的随机 nonce。用户用 Groth-Sahai 承诺所有中间值、承诺 \(C, C_\gamma\) 和签名 \(\sigma\)，然后生成三个证明：\(\pi_{GS}\) 证明方程 (R.2)-(R.8)（即 \(sn, dbsp\) 计算正确、SPS 验证通过、KZG 和 VC 打开正确、\(C_\gamma\) 正确构成）；\(\pi_{\text{lin}}\) 证明知识 of 标量 openings（利用随机预言机）；\(\pi_{\text{trunc}}\) 证明 cnt 在 \([0, N-1]\) 且 \(\bar y_j = y_j \pmod{8k}\)（通过比特分解和 Bulletproof 风格范围证明）。验证者检查三个证明。

**识别**：给定两个相同序列号 \(sn_0=sn_1\) 但不同 nonce \(r_0 \neq r_1\) 的令牌，计算 \(pk_U' = (dbsp_0 - dbsp_1)/(r_0 - r_1) \cdot G_1\) 恢复用户公钥。

**安全性**：永恒匿名性基于 Pagh-Pagh 函数的统计伪随机性（查询数 ≤ k，优势 ≤ \(k/2^{d/2-6}\)），KZGPed 和 VCKZG 的统计隐藏性，以及 Groth-Sahai、\(\Pi_{\text{lin}}\)、\(\Pi_{\text{trunc}}\) 的统计零知识。不可伪造性依赖于 SPS（EUF-CMA）、KZG 的评价绑定和位置绑定（基于 q-SDH 和 ARSDH 假设）、Groth-Sahai 的可靠性、\(\Pi_{\text{trunc}}\) 的可靠性（基于 DLOG），需随机预言机模型提取证据。可链接性通过重随机化因子 \(\gamma_0,\gamma_1\) 防止函数碰撞，并利用度绑定（ARSDH）处理跨会话冲突。免罪性由匿名性和 DLOG 假设保证。

**渐进复杂度**：Setup 和 Issuer 运行时间 \(t_I = \text{poly}(\lambda)\)（不依赖于 \(k\)）；用户发行时间 \(t_{User} = O(k \log^2 k \cdot \text{poly}(\lambda))\)（主要预计算 VC 打开）；展示时间 \(t_{Show} = O(\log N \cdot \text{poly}(\lambda))\)（独立于 \(k\)）；验证时间 \(t_V = O(\log N \cdot \text{poly}(\lambda))\)；令牌大小 \(s_\tau = O(\log \lambda)\) 群元素和标量；分发器大小 \(O(k)\)。

### 核心公式与流程

**Pagh-Pagh 函数计算**
\[
F_{\text{key}}(x) = T_1[\bar y_1] + T_2[\bar y_2] + (z_1, z_2, z_3), \quad \bar y_j = f_j(x) \pmod{8k}, \; z_i = g_i(x)
\]
> 作用：定义统计伪随机函数，其中 \(f_j, g_i\) 为度 \(d\) 多项式，\(T_j\) 为大小 \(S=8k\) 的表，输出 \(\mathbb{Z}_p^3\)。

**序列号和双花方程**
\[
sn = (t_{1,1}+t_{2,1}+z_1, t_{1,2}+t_{2,2}+z_2) + cnt \cdot \gamma_0 + \gamma_1,\quad dbsp = sk_U + r \cdot (t_{1,3}+t_{2,3}+z_3)
\]
> 作用：令牌的公开输出，\(sn\) 用于检测是否重复，\(dbsp\) 配合 nonce \(r\) 可恢复 \(sk_U\)。

**KZG 承诺验证（例如对多项式 \(f_j\)）**
\[
e(Q_{f,j}, X_{2,1} - x G_2) = e(C_{f,j} - y_j G_1 - \beta'_{f,j} H, G_2)
\]
> 作用：证明承诺 \(C_{f,j}\) 在点 \(x\) 处打开到 \(y_j\)，\(\beta'_{f,j}\) 为隐藏随机性得到的标量。

**Groth-Sahai 证明的配对积方程（简化）**
\[
e(sn \cdot G_T, ?) = e(T_{1,1}+T_{2,1}+Z_1, ?) + e(\widehat{cnt}_1, \Gamma_0) + e(G_1, \Gamma_1)
\]
> 作用：确保 \(sn\) 由正确的中间值组合而成，且 cnt 与 \(\gamma\) 正确参与运算。

### 实验结果

论文未提供实际实现运行时间或硬件测试，但给出了详细的理论效率对比（图 1）和具体尺寸估算。令牌大小约为 23 KB（使用 BLS12-381 曲线，含 196 个 \(\mathbb{G}_1\)、110 个 \(\mathbb{G}_2\)、101 个 \(\mathbb{Z}_p\) 标量），包括 Groth-Sahai 承诺（86 \(\mathbb{G}_1\) + 26 \(\mathbb{G}_2\)）、\(\pi_{GS}\) 证明（84 \(\mathbb{G}_1\) + 84 \(\mathbb{G}_2\)）、\(\pi_{\text{lin}}\)（63 标量）、\(\pi_{\text{trunc}}\)（26 \(\mathbb{G}_1\) + 35 标量以及 \(O(\log \lambda)\) 额外元素）。分发器大小约 \(O(k)\) 群元素（主要来自表 \(T_{j,i}\) 及其 VC 打开，约 \(48k\) 个 \(\mathbb{G}_1\)）。与格基替代方案对比：格基盲签名 [30] 令牌约 40 KB、发行带宽约 60 KB；格基匿名凭证 [3] 令牌约 80 KB、发行带宽约 45 KB；本文在令牌和带宽上更优，且实现统计匿名。参数范围：\(d = \Theta(\lambda)\)（如 32-128），\(S = 8k\)，\(k\) 可取到 \(2^{20}\) 量级，\(N\) 可取到 \(2^{20}\)。

### 局限性与开放问题

尽管本文的理论渐进效率优于 CHKLM 和格基方案，但实际令牌尺寸（约 23 KB）仍较大，难以用于带宽受限场景（如移动端高频认证）。证明过程大量使用随机预言机模型（\(\Pi_{\text{lin}}\) 和 \(\Pi_{\text{trunc}}\) 的 Fiat-Shamir 变换）和代数假设（SXDH, q-SDH, ARSDH），安全性归约不够紧。未来工作可探索在理想化群模型下获得更紧安全性和更小证明尺寸；亦可尝试将构造移植到标准模型，消除随机预言机依赖。用户发行阶段预计算 VC 打开需 \(O(k \log^2 k)\) 指数运算，对大规模 \(k\) 仍显昂贵，能否优化至 \(O(k \log k)\) 或 \(O(k)\) 值得研究。

### 强关联论文

[12] Camenisch, J., Hohenberger, S., Kohlweiss, M., Lysyanskaya, A., Meyerovich, M. How to win the clonewars: efficient periodic n-times anonymous authentication. **CCS 2006** [Google Scholar](https://scholar.google.com/scholar?q=How+to+win+the+clonewars%3A+efficient+periodic+n-times+anonymous+authentication)

[14] Camenisch, J., Hohenberger, S., Lysyanskaya, A. Balancing accountability and privacy using E-cash. **SCN 2006** [Google Scholar](https://scholar.google.com/scholar?q=Balancing+accountability+and+privacy+using+E-cash)

[32] Kate, A., Zaverucha, G.M., Goldberg, I. Constant-size commitments to polynomials and their applications. **ASIACRYPT 2010** [Google Scholar](https://scholar.google.com/scholar?q=Constant-size+commitments+to+polynomials+and+their+applications)

[2] Abe, M., Fuchsbauer, G., Groth, J., Haralambiev, K., Ohkubo, M. Structure-preserving signatures and commitments to group elements. **CRYPTO 2010** [Google Scholar](https://scholar.google.com/scholar?q=Structure-preserving+signatures+and+commitments+to+group+elements)

[29] Groth, J., Sahai, A. Efficient non-interactive proof systems for bilinear groups. **EUROCRYPT 2008** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+non-interactive+proof+systems+for+bilinear+groups)

[7] Berman, I., Haitner, I., Komargodski, I., Naor, M. Hardness-preserving reductions via cuckoo hashing. **J. Cryptol. 2019** [Google Scholar](https://scholar.google.com/scholar?q=Hardness-preserving+reductions+via+cuckoo+hashed)

[34] Pagh, A., Pagh, R. Uniform hashing in constant time and optimal space. **SIAM J. Comput. 2008** [Google Scholar](https://scholar.google.com/scholar?q=Uniform+hashing+in+constant+time+and+optimal+space)

[10] Bünz, B., Bootle, J., Boneh, D., Poelstra, A., Wuille, P., Maxwell, G. Bulletproofs: short proofs for confidential transactions and more. **S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Bulletproofs%3A+short+proofs+for+confidential+transactions+and+more)

[4] Attema, T., Cramer, R. Compressed Σ-protocol theory and practical application to plug & play secure algorithmics. **CRYPTO 2020** [Google Scholar](https://scholar.google.com/scholar?q=Compressed+%CE%A3-protocol+theory+and+practical+application+to+plug+%26+play+secure+algorithmics)

[30] Jeudy, C., Sanders, O. Improved lattice blind signatures from recycled entropy. **CRYPTO 2025** [Google Scholar](https://scholar.google.com/scholar?q=Improved+lattice+blind+signatures+from+recycled+entropy)


## 关键词

+ 永久性匿名限次令牌不可关联性
+ Privacy Pass匿名认证令牌分发器
+ 配对运算永久性匿名安全
+ 后量子鲁棒隐私保护凭证
+ 无界计算攻击者匿名性安全