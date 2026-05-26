---
title: "ElectionGuard: a Cryptographic Toolkit to Enable Verifiable Elections"
标题简称: 
论文类型: conference
undefined: USENIX Security
发表年份: 2025
created: 2025-05-07 21:51:58
modified: 2025-05-07 21:53:57
---

## ElectionGuard: a Cryptographic Toolkit to Enable Verifiable Elections

## 发表信息

+ [原文链接](https://www.usenix.org/conference/usenixsecurity24/presentation/benaloh)

## 作者

+ Josh Benaloh 
+ Michael Naehrig 
+ Olivier Pereira 
+ Dan S Wallach 

## 笔记

### 背景与动机

端到端（E2E）可验证选举系统允许选民和观察者在无需信任选举软件、硬件或人员的条件下确认选举结果的准确性，这对于抵制有关选举结果的不实信息至关重要。然而，大多数已部署的E2E设计都要求替换整个选举基础设施，导致采纳成本极高。ElectionGuard 由微软于 2018 年发起，其核心创新是将密码学工具与投票系统的核心机制及用户界面分离，从而允许现有的投票设备供应商仅通过添加一个加密模块就能获得可验证性，无需重建整个系统。此外，ElectionGuard 在解密阶段引入了一种新的阈值组合证明方法，将多个监护人的部分解密证明合并为单个 Chaum-Pedersen 证明，从而极大简化了验证器的编写——这是目前最复杂的环节之一。该工具包已在多种真实选举场景中部署，包括美国多个州的现场投票、国会党团选举、邮递投票以及欧洲的网上投票，验证了其灵活性和实用性。

### 相关工作

[1] Adida 等. Electing a university president using open-audit voting: Analysis of real-world use of Helios. **EVT/WOTE 2009** [Google Scholar](https://scholar.google.com/scholar?q=Electing+a+university+president+using+open-audit+voting%3A+Analysis+of+real-world+use+of+Helios)
> 核心思路：Helios 是首个广泛部署的 E2E 网上投票系统，使用 ElGamal 加密和分布式密钥生成（简单产品公钥）。
> 局限与区别：Helios 要求完全替换投票系统，且其密钥生成协议不支持 k < n 的阈值；ElectionGuard 采用更通用的 Pedersen DKG 变体，支持任意阈值，并允许工具包嵌入现有设备。

[4] Benaloh 等. STAR-Vote: A secure, transparent, auditable, and reliable voting system. **EVT/WOTE 2013** [Google Scholar](https://scholar.google.com/scholar?q=STAR-Vote%3A+A+secure%2C+transparent%2C+auditable%2C+and+reliable+voting+system)
> 核心思路：STAR-Vote 是一个面向现场的 E2E 系统，使用同态加密和承诺方案。
> 局限与区别：STAR-Vote 也是作为一个完整的系统设计；ElectionGuard 采用类似的加密技术，但以工具包形式提供，且引入了合并解密证明的创新。

[17] Cohen (Benaloh) 和 Fischer. A robust and verifiable cryptographically secure election scheme. **FOCS 1985** [Google Scholar](https://scholar.google.com/scholar?q=A+robust+and+verifiable+cryptographically+secure+election+scheme)
> 核心思路：最早的同态加密投票方案之一，使用指数 ElGamal 实现加法同态。
> 局限与区别：该方案未考虑分布式密钥生成和现实部署细节；ElectionGuard 基于相同思想，但扩展了完整的工程实现和阈值解密。

[18] Cortier 等. Belenios: A simple private and verifiable electronic voting system. **LNCS 11565 2019** [Google Scholar](https://scholar.google.com/scholar?q=Belenios%3A+A+simple+private+and+verifiable+electronic+voting+system)
> 核心思路：Belenios 是 Helios 的后继系统，增加了非交互式零知识证明和更好的隐私保证。
> 局限与区别：Belenios 仍未脱离“完整系统”模式；ElectionGuard 强调可分离性，并提供确认码链式哈希来增强可检测篡改性。

[20] Cramer, Gennaro 和 Schoenmakers. A secure and optimally efficient multi-authority election scheme. **EUROCRYPT 1997** [Google Scholar](https://scholar.google.com/scholar?q=A+secure+and+optimally+efficient+multi-authority+election+scheme)
> 核心思路：提出了同态计票的通用框架，包括选择加密和范围证明。
> 局限与区别：该协议假设所有权威必须在线；ElectionGuard 采用其潘式证明结构，但支持阈值解密和离线代理人。

[38] Pedersen. A threshold cryptosystem without a trusted party. **EUROCRYPT 1991** [Google Scholar](https://scholar.google.com/scholar?q=A+threshold+cryptosystem+without+a+trusted+party)
> 核心思路：首个分布式密钥生成（DKG）协议，支持门限秘密共享。
> 局限与区别：原协议要求 k < n/2 以保证鲁棒性；ElectionGuard 修改为支持任意 k ≤ n，并增加了 Schnorr 证明和基于公开广播的检查机制，以应对恶意占多数场景。

[39] Sako 和 Kilian. Receipt-free mix-type voting scheme. **EUROCRYPT 1995** [Google Scholar](https://scholar.google.com/scholar?q=Receipt-free+mix-type+voting+scheme)
> 核心思路：基于混合网络的投票方案，支持排序投票等复杂规则。
> 局限与区别：混合网络部署复杂性高；ElectionGuard 当前仅支持同态计票，但路线图中包含混合网络支持。

[8] Benaloh 等. End-to-end verifiability. **arXiv 2015** [Google Scholar](https://scholar.google.com/scholar?q=End-to-end+verifiability)
> 核心思路：定义了 E2E 可验证性的三个核心属性：投出-如意图、已记录-如投出、已计票-如记录。
> 局限与区别：该文是概念性框架；ElectionGuard 是实现该框架的具体工具集。

[9] Benaloh, Stark 和 Teague. VAULT: Verifiable Audits Using Limited Transparency. **E-Vote-ID 2019** [Google Scholar](https://scholar.google.com/scholar?q=VAULT%3A+Verifiable+Audits+Using+Limited+Transparency)
> 核心思路：使用同态加密保护风险限制审计（RLA）中的隐私，避免公布原始选票。
> 局限与区别：VAULT 是一个独立协议；ElectionGuard 将其作为应用场景之一，并提供了完整实现。

### 核心技术与方案

#### 整体架构
ElectionGuard 将选举分为三个阶段：密钥生成与设置、选票加密、计票解密。其核心创新在于工具包模式：密码学模块通过简单 API 嵌入现有投票设备（如扫描仪、标记设备等），不干扰投票流程。所有加密数据（密文、零知识证明、确认码）均由公开的选举记录发布，验证者可独立检查。

#### 密码学基元
使用指数型 ElGamal 加密。设大素数 p，子群阶 q（256 位），生成元 g。明文 m（通常为 0 或 1）编码为 g^m，加密为 (g^ξ, K^ξ · g^m)，其中 K 是选举公钥。加法同态性通过密文分量相乘实现：对应同一候选人的所有密文相乘后，明文乘积对应票数和。解密时需要计算小离散对数（因为票数少）。

为便于验证，加密同时附带 Chaum-Pedersen 零知识证明，证明密文是 {0,1} 的有效加密。证明非交互化采用 Fiat-Shamir 变换，哈希函数用 HMAC-SHA-256，并引入上下文哈希（参数哈希、选举基础哈希、扩展基哈希、选票标识哈希）以防止跨选举和跨选票重放。

#### 密钥生成
采用 Pedersen DKG 变体，支持任意阈值 k ≤ n。每个监护人 G_i 选随机多项式 P_i(x)=∑a_{i,j}x^j (j=0..k-1)，公布 Feldman 承诺 K_{i,j}=g^{a_{i,j}} 和公钥 κ_i=g^{ζ_i}，并附 Schnorr 证明。然后向每个 G_j 加密发送 P_i(j)。G_j 验证份额一致性：g^{P_i(j)} = ∏ (K_{i,ℓ})^{j^ℓ}。最终公钥 K = ∏K_{i,0}，每个监护人私钥份额为 P(i)=∑P_j(i)。该协议对任意 k 均安全，即使 k-1 个监护人被腐蚀，ElGamal 加密仍保持 IND-CPA 安全（定理1的归约证明）。

#### 选票加密与确认码
对每个选项 (i,j)，使用派生随机数 ξ_{i,j}=H_q(H_I; 0x21, i, j, ξ_B)，其中 ξ_B 是选票秘密随机数，H_I 是选票标识哈希。加密为 (α,β)=(g^ξ, K^ξ·g^σ)。附零知识证明：使用选择过的 Pand-Cramer 证明。确认码 H_C 由所有密文的哈希按清单顺序计算得到，并可支持链式哈希（后一张选票的确认码包含前一张的码），增强篡改检测。

#### 计票与解密
有效选票密文相乘得同态密文和。解密时，至少 k 个监护人用份额 P(i) 计算部分解密 M_i = A^{P(i)}；组合得 M = ∏(M_i)^{w_i}，其中 w_i 为 Lagrange 系数。然后计算 K^t = B · M^{-1}，通过小离散对数得到 t。

#### 合并解密证明（核心创新）
传统方案每个监护人发布独立 Chaum-Pedersen 证明，验证者需要累加 Lagrange 系数，复杂易错。ElectionGuard 设计了一个阈值协议：监护人先 commit 到各自的 (a_i,b_i)=(g^{u_i}, A^{u_i})，交换承诺后公开 (a_i,b_i)，计算组合承诺 (a,b) = (∏a_i, ∏b_i)。挑战 c = H_q(H_E; 0x31, A, B, a, b, M)，每个监护人计算调整挑战 c_i = c·w_i 和响应 ν_i = u_i - c_i P(i)，最终响应 ν = ∑ν_i。验证者仅需检查 a = g^ν K^c, b = A^ν M^c。该协议产生单个 Chaum-Pedersen 证明，隐藏参与监护人的身份和数量。定理2证明了模拟器的存在，保证持有部分信息的模拟者（知 M_i, K_{i,j}）能产生与真实交互不可区分的对话，即零知识。

#### 验证
支持“投出-如意图”（选民可挑战选票，获得随机数或解密结果验证加密正确）和“已计票-如记录”（任何人验证同态聚合和合并解密证明）。ElectionGuard 不保证资格性验证，需外部选民名单。

### 核心公式与流程

**指数 ElGamal 加密**
$$(\alpha, \beta) = (g^{\xi}, K^{\xi} \cdot g^{\sigma}), \quad \sigma \in \{0,1\}$$
> 作用：加密选票选择，利用加法同态性：对应同一候选人的密文分量相乘得加密票和。

**派生随机数**
$$\xi_{i,j} = H_q(\mathrm{H}_I; 0x21, i, j, \xi_B)$$
> 作用：从选票秘密随机数 ξ_B 和上下文哈希 H_I 导出每个选项的加密随机数，支持挑战时通过公开 ξ_B 重算。

**合并解密证明**
$$(a_i, b_i) = (g^{u_i}, A^{u_i}), \quad (a,b) = (\prod a_i, \prod b_i)$$
$$c = H_q(\mathrm{H}_E; 0x31, A, B, a, b, M), \quad c_i = c \cdot w_i \pmod{q}, \quad \nu_i = u_i - c_i P(i) \pmod{q}, \quad \nu = \sum \nu_i \pmod{q}$$
验证：$a = g^\nu K^c,\; b = A^\nu M^c$。
> 作用：将多个监护人的部分解密证明合并为单个 Chaum-Pedersen 证明，验证者无需处理 Lagrange 系数。

**确认码（链式）**
$$\mathrm{H}_j = H(\mathrm{H}_I; 0x29, \chi_1, \dots, \chi_{m_B}, i_C \parallel \mathrm{H}_{j-1})$$
> 作用：链式哈希使得修改某张选票后后续所有确认码均需变更，提高篡改检测概率。

### 实验结果

论文未提供传统意义上的基准测试表格，但给出了性能优化数据和部署规模。使用固定基数指数表（预计算 g 的幂）可将加密速度提升 5.1 倍（8 位表）至 8.6 倍（16 位表）；验证操作因变量基数多，仅提升 1.6–1.7 倍。使用 Montgomery 形式存储表项可再额外提速 2.5 倍。采用以 K 为基的加密（将 g^σ 纳入 β 而非独立乘法）节省 13% 的计算量。在 Inyo County 部署中，处理约一百万张选票需要约 1000 个 CPU 核心并行加密；每个加密选票（早期 JSON 格式）约 1MB，总存储需求约 1TB，通过分桶和 Merkle 树实现可扩展验证。实际选举规模：Fulton, Wisconsin 398 张选票（4 张挑战），College Park, Maryland 1468 张选票，Idaho 111 张选票，Utah 514 张选票等。用户调查显示选民和工作人员对结果准确性的信心显著提升。

### 局限性与开放问题

1. **设备信任**：ElectionGuard 不保护选票输入端的隐私（如摄像头、键盘记录器），也不防止摇号机泄露加密随机数或使用弱伪随机生成器。
2. **密钥管理实践**：实际部署中监护人几乎盲目听从选举组织者指示，使用其提供的软硬件，难以实现真正的独立性；论文指出需要更好的方法实现实践中的独立。
3. **资格性验证**：ElectionGuard 本身不验证选民资格，依赖外部名单，若名单未公开则难以防止内部人员添加虚假选票。
4. **性能瓶颈**：虽然加密可并行化，但验证（特别是百万量级选票）仍需大量计算和存储资源，链式哈希和 Merkle 树等优化尚未充分标准化。

### 强关联论文

[1] Ben Adida, Olivier de Marneffe, Olivier Pereira, and Jean-Jacques Quisquater. Electing a university president using open-audit voting: Analysis of real-world use of Helios. **EVT/WOTE 2009**

[4] Josh Benaloh, Michael D. Byrne, Bryce Eakin, Philip T. Kortum, Neal McBurnett, Olivier Pereira, Philip B. Stark, Dan S. Wallach, Gail Fisher, Julian Montoya, Michelle Parker, and Michael Winn. STAR-Vote: A secure, transparent, auditable, and reliable voting system. **EVT/WOTE 2013**

[17] Josh D. (Benaloh) Cohen and Michael J. Fischer. A robust and verifiable cryptographically secure election scheme. **FOCS 1985**

[18] Véronique Cortier, Pierrick Gaudry, and Stéphane Glondu. Belenios: A simple private and verifiable electronic voting system. **LNCS 11565 2019**

[20] Ronald Cramer, Rosario Gennaro, and Berry Schoenmakers. A secure and optimally efficient multi-authority election scheme. **EUROCRYPT 1997**

[38] Torben P. Pedersen. A threshold cryptosystem without a trusted party. **EUROCRYPT 1991**

[39] Kazue Sako and Joe Kilian. Receipt-free mix-type voting scheme. **EUROCRYPT 1995**

[8] Josh Benaloh, Ronald Rivest, Peter Y.A. Ryan, Philip Stark, Vanessa Teague, and Poorvi Vora. End-to-end verifiability. **arXiv 2015**

[9] Josh Benaloh, Philip Stark, and Vanessa Teague. VAULT: Verifiable Audits Using Limited Transparency. **E-Vote-ID 2019**

[21] Elizabeth C. Crites, Chelsea Komlo, and Mary Maller. Fully adaptive Schnorr threshold signatures. **CRYPTO 2023**


## 关键词

+ ElectionGuard可验证选举工具包
+ 端到端选举可验证性
+ 密码学投票系统设计
+ 选举完整性与隐私保护
+ 开源选举基础设施
+ 实际选举部署经验