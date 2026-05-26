---
title: "Crowd verifiable zero-knowledge and end-to-end verifiable multiparty computation"
标题简称:
论文类型: conference
会议简称: ASIACRYPT
发表年份: 2020
---

## Crowd verifiable zero-knowledge and end-to-end verifiable multiparty computation

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-030-64840-4_24)

## 作者

+ [Foteini Baldimtsi](Foteini%20Baldimtsi.md) 
+ Aggelos Kiayias 
+ Thomas Zacharias 
+ Bingsheng Zhang 


## 笔记

### 背景与动机
安全多方计算（MPC）已从理论走向实际应用，但现有可审计MPC方案（如Baum等人在SCN 2014提出的方案[4]）仅能对抗服务器腐败，无法应对用户客户端设备被攻破或公共参考字符串（CRS）被篡改的情形。同时，已有的通用可验证MPC[56]依赖随机预言机模型，也未考虑客户端腐败。在电子投票等场景中，终端到端可验证性已成为核心需求，但缺乏统一的理论框架。本文旨在填补这一空白：在完全无信任设置（无CRS、无随机预言机）下，构造即使服务器、客户端和设置参数全部被敌手控制的MPC协议，仍能保证输出可验证。为此，本文引入“人群可验证零知识”（CVZK）原语和“扩展关系”概念，并基于离散对数假设在扩展UC模型（EUC）中实现安全。

### 相关工作

[4] Baum, Damgård, Orlandi. Publicly Auditable Secure Multi-party Computation. **SCN 2014** [Google Scholar](https://scholar.google.com/scholar?q=Publicly+Auditable+Secure+Multi-party+Computation)
> 核心思路：通过修改SPDZ协议实现可审计MPC，允许外部验证者检查正确性，但假设CRS可信。
> 局限与区别：未考虑CRS被颠覆和客户端被腐败的情况；本文在无CRS的plain模型下达到更弱的安全性要求。

[56] Schoenmakers, Veeningen. Universally Verifiable Multiparty Computation from Threshold Homomorphic Cryptosystems. **ACNS 2015** [Google Scholar](https://scholar.google.com/scholar?q=Universally+Verifiable+Multiparty+Computation+from+Threshold+Homomorphic+Cryptosystems)
> 核心思路：利用阈值同态加密实现通用可验证MPC，所有服务器可腐败但客户端必须诚实，安全性依赖随机预言机。
> 局限与区别：客户端不被视为可腐败实体；本文假设客户端也可腐败，且标准模型下实现。

[5] Beaver. Efficient Multiparty Protocols Using Circuit Randomization. **CRYPTO 1991** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+Multiparty+Protocols+Using+Circuit+Randomization)
> 核心思路：提出离线/在线预处理模式，服务器预先计算三元组，在线阶段高效计算。
> 本文使用该范式并基于同态承诺实现可验证性。

[27] Damgård, Pastro, Smart, Zakarias. Multiparty Computation from Somewhat Homomorphic Encryption. **CRYPTO 2012** [Google Scholar](https://scholar.google.com/scholar?q=Multiparty+Computation+from+Somewhat+Homomorphic+Encryption)
> 核心思路：SPDZ协议，基于同态加密和消息认证码实现恶意安全MPC。
> 本文沿用其离线/在线结构，但将零知识证明替换为CVZK，并移除MAC，依赖承诺绑定性和CVZK安全性。

[26] Damgård, Keller, Larraia, Pastro, Scholl, Smart. Practical Covertly Secure MPC for Dishonest Majority – Or: Breaking the SPDZ Limits. **ESORICS 2013** [Google Scholar](https://scholar.google.com/scholar?q=Practical+Covertly+Secure+MPC+for+Dishonest+Majority+%E2%80%93+Or%3A+Breaking+the+SPDZ+Limits)
> 核心思路：SPDZ的优化版本，支持更高效率。
> 本文类似地需要CVZK证明三元组正确性，但需适应人群可验证场景。

[17] Canetti, Lin, Pass. Adaptive Hardness and Composable Security in the Plain Model from Standard Assumptions. **FOCS 2010** [Google Scholar](https://scholar.google.com/scholar?q=Adaptive+Hardness+and+Composable+Security+in+the+Plain+Model+from+Standard+Assumptions)
> 核心思路：扩展UC模型（EUC）允许超多项式时间辅助函数实现标准模型组合安全。
> 本文使用EUC模型来绕过无CRS下UC不可实现的限制。

[46] Lapidot, Shamir. Publicly Verifiable Non-Interactive Zero-Knowledge Proofs. **CRYPTO 1990** [Google Scholar](https://scholar.google.com/scholar?q=Publicly+Verifiable+Non-Interactive+Zero-Knowledge+Proofs)
> 核心思路：给出完全输入延迟的Σ协议（用于哈密顿圈），可用于CVZK编译。
> 本文将其作为底层原语，且证明其可抵抗辅助函数辅助的PPT敌手。

[53] Pandey, Pass, Vaikuntanathan. Adaptive One-Way Functions and Applications. **CRYPTO 2008** [Google Scholar](https://scholar.google.com/scholar?q=Adaptive+One-Way+Functions+and+Applications)
> 核心思路：定义自适应单向函数（AOWF），即使敌手可问其他标签的逆，仍难以求逆。
> 本文基于离散对数构造公开可采样自适应单向函数（PS-AOWF），用于CVZK中模拟硬实例。

[8] Ben-Or, Linial. Collective Coin Flipping, Robust Voting Schemes and Minima of Banzhaf Values. **FOCS 1985** [Google Scholar](https://scholar.google.com/scholar?q=Collective+Coin+Flipping%2C+Robust+Voting+Schemes+and+Minima+of+Banzhaf+Values)
> 核心思路：一轮集体抛硬币（1RCCF）概念和弹性函数。
> 本文利用弹性函数构造凝聚函数，从用户有限随机位中提取高质量随机串。

### 核心技术与方案

#### 整体框架
本文构建端到端可验证MPC（VMPC）的核心工具是“人群可验证零知识”（CVZK）。CVZK允许一个证明者向一群个体验证者（“人群”）证明某个陈述，每个验证者仅贡献少量随机位（对数级），且部分验证者可被腐化。利用CVZK，本文构造的VMPC协议遵循离线/在线模式（类似SPDZ [27]和BDO [4]）：数据被承诺并公布在公告板上，承诺具有线性同态性，验证者可通过重算来验证正确性。所有零知识证明均需转化为CVZK。关键区别在于：离线阶段服务器发布CVZK的第一轮消息；输入阶段用户（人类）协同生成挑战硬币；输出阶段服务器发布输出及CVZK第三轮消息。

#### 凝聚函数（Coalescence Function）
为了从n个用户每人贡献的1比特随机位（总熵仅O(log n)）中产生高质量挑战，本文设计了凝聚函数$F(\cdot)$。输入n比特向量$C$，先划分为$\lambda \log \lambda$个块，每块$\frac{n}{\lambda \log \lambda}$比特；再将每$\lambda$个块分为一组，共$\log \lambda$组。对每组内每个块应用强弹性函数[50]（具有$O(\log^2 m/m)$强弹性），输出1比特；每组得到$\lambda$比特后，通过冯·诺依曼拒绝采样消除偏差，最终每组输出$\frac{\lambda}{\log^2 \lambda}$比特，共$\log \lambda$个字符串。定理1证明：当$n=\lambda^\gamma$，敌手可腐化最多$n^{1-1/\gamma}/\log^3 n$个用户时，至少有一个输出串统计接近均匀，概率$1-\mathsf{negl}(\lambda)$。该函数还满足完备性和高效可采样性。

#### CVZK编译
CVZK编译器将任意完全输入延迟的Σ协议编译成三轮CVZK协议，面向NP语言$\mathcal{L}$和PS-AOWF家族$\mathbf{F}=\{f_{\mathsf{tag}}\}$。编译器使用析取证明范式：证明者必须证明要么知道$\mathcal{L}$中$x$的见证$w$，要么能求逆某个硬实例。具体流程（图2）：
- 首轮：证明者运行$\log \lambda$个Σ协议（语言$\mathcal{L}$）生成$a_i$，并运行$n\log \lambda$个完全输入延迟的模拟器（语言$\mathcal{L}_{\mathsf{tag}_\ell}^*$，即$f_{\mathsf{tag}_\ell}$的像集）生成$a_{\ell,j}^*$，同时选择随机$R$。
- 次轮：各验证者$V_\ell$输出硬币$c_\ell$，组成$C$。
- 终轮：计算$F(C)=(d_1,\dots,d_{\log \lambda})$，设$E=R\oplus C$，对每个$i$用挑战$e_i$完成Σ协议，对每个$(\ell,j)$用$d_j$生成像$\beta_{\ell,j}$并完成模拟。验证者检查所有Σ验证和模拟验证均通过。
安全性（定理2）：若底层Σ协议和输入延迟Σ协议具有特殊健全性和sHVZK，则CVZK满足$(\frac{n^{1-1/\gamma}}{\log^3 n},\mathsf{negl})$-人群可验证健全性和有效性，以及$n$-人群可验证零知识（借助辅助函数）。

#### VMPC构造
单服务器VMPC作为热身：服务器在初始化阶段生成双模承诺密钥并证明其为绑定，随机生成两个随机数$r_\ell^{(0)},r_\ell^{(1)}$并承诺，预计算Beaver三元组并证明正确性。输入阶段，用户$U_\ell$选择随机比特$b_\ell$，计算$\delta_\ell=x_\ell-r_\ell^{(b_\ell)}$，发送$(b_\ell,\delta_\ell)$给客户端，客户端发布至公告板。用户保留$(b_\ell,\delta_\ell,r_\ell^{(1-b_\ell)})$作为审计数据。计算阶段，服务器利用承诺的同态性计算电路，对加法直接同态，对乘法使用Beaver三元组并打开差值。验证阶段，验证者收集各用户审计数据，检查公告板信息一致性、承诺打开正确性、CVZK证明有效性，并重算电路。安全性直觉：若敌手腐化服务器和所有客户端，但最多腐化$n^{1-1/\gamma}/\log^3 n$个用户，则其攻击分为承诺攻击（完美绑定不可行）、声音攻击（CVZK健全性概率可忽略）、客户端攻击（猜测用户硬币概率1/2）。若客户端攻击次数超过$\delta$，则验证者将以至少$1-2^{-\delta}$概率拒绝；若小于$\delta$，则实际输入与敌手输入在$\mathsf{Dcr}_n$距离上$\delta$接近，由$\delta$-扩展关系保证真实输出与敌手输出相关，模拟器可接受。整体误差为$2^{-\delta}+\mathsf{negl}(\lambda)$。多服务器扩展通过秘密共享服务器状态实现，类似BDO/SPDZ但移除MAC，改为CVZK证明，最终得到定理4：在$\{ \mathcal{G}_{\mathsf{BB}}, \mathcal{F}_{\mathsf{sc}}, \mathcal{F}_{\mathsf{auth}}, \mathcal{F}_{\mathsf{V.Offline}} \}$混合模型中，协议$\mathcal{H}$-EUC实现$\mathcal{F}_{\mathsf{vmpc}}^{f,R}(\mathcal{P})$，误差$2^{-\delta}+\mathsf{negl}(\lambda)$，基于自适应DDH假设，最多腐化$\frac{n^{1-1/\gamma}}{\log^3 n}$个用户。

#### 扩展关系（Spreading Relation）
定义7：对于度量空间$(X^n,\mathsf{Dcr}_n)$和$(Y,\mathrm{d}_Y)$，关系$R\subseteq \operatorname{Img}[f]\times\operatorname{Img}[f]$是$\delta$-扩展的，若对于任意$\mathbf{x},\mathbf{x}'\in X^n$，当$\mathsf{Dcr}_n(\mathbf{x},\mathbf{x}')\leq\delta$时，必有$R(f(\mathbf{x}),f(\mathbf{x}'))$成立。定理3证明：若$f$对称且$R$不是$\delta$-扩展的，则任何VMPC方案（用户最小熵$\kappa$）误差至少为$2^{-\kappa\delta}-\mathsf{negl}(\lambda)$，因此VMPC对非扩展关系不可行（当$\kappa=O(\log\lambda)$时）。Lipschitz函数和带距关系是典型特例。

### 核心公式与流程

**[凝聚函数定义]**
$$F: \{0,1\}^n \to \left(\{0,1\}^{\frac{\lambda}{\log^2 \lambda}}\right)^{\log \lambda}, \quad n=\lambda^\gamma$$
> 作用：从$n$个用户的随机位中提取出$\log\lambda$个长度为$\frac{\lambda}{\log^2\lambda}$的字符串，其中至少一个统计接近均匀，即使敌手腐化最多$n^{1-1/\gamma}/\log^3 n$个用户。

**[CVZK编译器（图2）关键步骤]**
$$a_i \leftarrow \Sigma.\mathsf{Prv}_1(x,w),\quad a_{\ell,j}^* \leftarrow \mathsf{InD.Sim}_1(r_\ell, \text{size})$$
$$C = (c_1,\dots,c_n),\quad (d_1,\dots,d_{\log\lambda}) = F(C),\quad E = R \oplus C$$
$$\forall i:\ z_i \leftarrow \Sigma.\mathsf{Prv}_2(\mathsf{st}_i, e_i),\quad \forall \ell,j:\ \beta_{\ell,j} = \mathsf{IM}(\mathsf{tag}_\ell, d_j),\quad z_{\ell,j}^* \leftarrow \mathsf{InD.Sim}_2(\mathsf{st}_{\ell,j}^*, \beta_{\ell,j})$$
> 作用：首轮生成左半部分（真实证明）和右半部分（模拟）；次轮获得用户硬币；终轮用凝聚函数导出的挑战完成左半，镜像映射产生硬实例并完成右半模拟。

**[单服务器VMPC用户输入]**
$$b_\ell \gets \{0,1\},\quad \delta_\ell = x_\ell - r_\ell^{(b_\ell)},\quad \alpha_\ell = (b_\ell, \delta_\ell, r_\ell^{(1-b_\ell)})$$
> 作用：用户利用一次比特选择掩盖输入；审计数据包含另一随机数，用于验证服务器行为。

**[扩展关系定义]**
$$R\text{ 是 }\delta\text{-扩展的} \iff \forall \mathbf{x},\mathbf{x}'\in X^n:\ \mathsf{Dcr}_n(\mathbf{x},\mathbf{x}')\leq\delta \Rightarrow R(f(\mathbf{x}),f(\mathbf{x}'))$$
> 作用：刻画VMPC可行性边界：仅当关系足够“宽松”（能容忍$\delta$个输入被篡改）时，才可能以可忽略误差实现。

**[VMPC理想功能验证阶段关键规则]**
$$\text{若存在诚实服务器且所有诚实用户的客户端诚实，则发送真实输出 }y\text{ 和 }1$$
$$\text{否则，若}(y,\tilde{y})\in R\text{则发送}1,\text{否则发送}0$$
> 作用：当所有服务器或某个诚实用户的客户端被腐化时，功能仅要求输出与正确输出满足关系$R$。

### 实验结果

本文未提供具体的实验评估。作者在论文中仅给出理论构造和安全性证明，未描述任何实现或性能基准测试。因此，无法报告运行时间、通信开销等实验数据。本文主要贡献在于定义新原语、证明可行性，而非工程实现。

### 局限性与开放问题
第一，VMPC协议的误差由$2^{-\delta}+\mathsf{negl}(\lambda)$主导，其中$\delta$是扩展关系参数；为提高安全性，须要求用户数$n$足够大使得$2^{-\delta}$可忽略，这对应用场景有约束。第二，CVZK编译器依赖自适应单向函数（基于离散对数），未来可探索基于后量子假设的实例化。第三，当前构造要求公告板一致、用户与验证者间的认证信道，实际部署中可能增加额外物理假设。第四，对于非对称函数或非扩展关系，VMPC不可行，限制了通用性。

### 强关联论文

[4] Baum, Damgård, Orlandi. Publicly Auditable Secure Multi-party Computation. **SCN 2014**

[56] Schoenmakers, Veeningen. Universally Verifiable Multiparty Computation from Threshold Homomorphic Cryptosystems. **ACNS 2015**

[5] Beaver. Efficient Multiparty Protocols Using Circuit Randomization. **CRYPTO 1991**

[27] Damgård, Pastro, Smart, Zakarias. Multiparty Computation from Somewhat Homomorphic Encryption. **CRYPTO 2012**

[26] Damgård, Keller, Larraia, Pastro, Scholl, Smart. Practical Covertly Secure MPC for Dishonest Majority – Or: Breaking the SPDZ Limits. **ESORICS 2013**

[17] Canetti, Lin, Pass. Adaptive Hardness and Composable Security in the Plain Model from Standard Assumptions. **FOCS 2010**

[46] Lapidot, Shamir. Publicly Verifiable Non-Interactive Zero-Knowledge Proofs. **CRYPTO 1990**

[53] Pandey, Pass, Vaikuntanathan. Adaptive One-Way Functions and Applications. **CRYPTO 2008**

[8] Ben-Or, Linial. Collective Coin Flipping, Robust Voting Schemes and Minima of Banzhaf Values. **FOCS 1985**

[50] Meka. Explicit Resilient Functions Matching Ajtai-Linial. **SODA 2017**


## 关键词

+ 端到端可验证多方计算
+ 群体可验证零知识
+ 离散对数假设
+ 协议审计
+ 可验证关系