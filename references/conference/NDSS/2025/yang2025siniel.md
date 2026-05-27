---
title: "Siniel: Distributed Privacy-Preserving zkSNARK"
doi: 10.14722/ndss.2025.240152
标题简称: 
论文类型: conference
会议简称: NDSS
发表年份: 2025
modified: 2025-04-13 16:39:23
---
## Siniel: Distributed Privacy-Preserving zkSNARK

## 发表信息

+ [原文链接](https://eprint.iacr.org/2024/1803)

## 作者

+ Yunbo Yang 
+ Yuejia Cheng 
+ Kailun Wang 
+ Xiaoguo Li 
+ Jianfei Sun 
+ Jiachen Shen 
+ Xiaolei Dong 
+ Zhenfu Cao 
+ Guomin Yang 
+ Robert H Deng 

## 笔记

### 背景与动机
零知识简洁非交互知识论证（zk-SNARK）是隐私保护应用的核心原语，但其证明生成的高计算开销（如对大多项式的FFT和MSM操作）严重限制了在资源受限设备（如手机）上的部署。现有私有委托方案中，EOS委托者需在每个PIOP轮次参与一致性检查，导致在线交互延迟；而zkSaaS仅在半诚实安全模型下提供保护。本文旨在设计一个通用的zkSNARK证明生成委托框架，同时满足在线阶段无委托者交互、委托者仅需轻量级离线计算、以及对恶意工人的安全性。提出的Siniel框架基于多项式交互式预言证明（PIOP）和多项式承诺方案（PCS），并利用Shamir秘密共享与认证标签机制实现非交互一致性检查，从而彻底消除委托者的在线参与。

### 相关工作

[CLMZ23] Chiesa等. EOS: Efficient Private Delegation of zkSNARK Provers. **USENIX Security 2023** [Google Scholar](https://scholar.google.com/scholar?q=EOS+Efficient+Private+Delegation+of+zkSNARK+Provers)
> 核心思路：基于PIOP与PCS，通过“一致性检查器”让委托者在每个PIOP轮次验证工人计算的正确性，达到恶意多数安全。
> 局限与区别：委托者必须在线上与工人交互执行一致性检查，增加了延迟与计算开销。Siniel将此检查器完全移至工人端，实现非交互。

[GGJ+23] Garg等. zkSaaS: Zero-Knowledge SNARKs as a Service. **USENIX Security 2023** [Google Scholar](https://scholar.google.com/scholar?q=zkSaaS+Zero-Knowledge+SNARKs+as+a+Service)
> 核心思路：为多项式算术化和MSM设计专用MPC协议，支持委托者离线后无交互，但安全性为半诚实。
> 局限与区别：仅容忍半诚实敌手，无法抵御恶意工人。Siniel在诚实多数假设下提供恶意安全性。

[GGW23] Garg等. How to Prove Statements Obliviously? **Cryptology ePrint Archive 2023** [Google Scholar](https://scholar.google.com/scholar?q=How+to+Prove+Statements+Obliviously)
> 核心思路：基于全同态加密，让委托者将密文直接发送给单服务器，由服务器完成证明生成。
> 局限与区别：同态加密的计算开销极大，实用性差。Siniel使用秘密共享和轻量级认证标签，效率更高。

[OB22] Ozdemir等. Experimenting with Collaborative zk-SNARKs: Zero-Knowledge Proofs for Distributed Secrets. **USENIX Security 2022** [Google Scholar](https://scholar.google.com/scholar?q=Experimenting+with+Collaborative+zk-SNARKs)
> 核心思路：基于SPDZ和GSZ协议，让多个持有见证份额的方联合生成证明，支持恶意安全。
> 局限与区别：依赖昂贵的密码原语保证正确性，通信与计算开销大。Siniel通过非交互一致性检查器简化了在线阶段。

[WZC+18] Wu等. DIZK: A Distributed Zero Knowledge Proof System. **USENIX Security 2018** [Google Scholar](https://scholar.google.com/scholar?q=DIZK+Distributed+Zero+Knowledge+Proof+System)
> 核心思路：将证明任务分发给多个工人，每个工人持有部分明文见证，并行计算。
> 局限与区别：通信开销与电路规模线性正相关，且工人能直接接触部分见证，不提供隐私。Siniel保护委托者见证的隐私性。

[XZC+22] Xie等. deVirgo: Distributed Zero-Knowledge Proof Protocol of Virgo. **CCS 2022** [Google Scholar](https://scholar.google.com/scholar?q=deVirgo+Distributed+Zero-Knowledge+Proof+Protocol+of+Virgo)
> 核心思路：将Virgo协议分布式化，降低每工人的空间复杂度。
> 局限与区别：工人间通信与证明大小仍与工人数相关，且不隐藏工人的局部见证。Siniel可与此类技术互补，进一步提升可扩展性。

[LXZ+24] Liu等. Pianist: Scalable zkRollups via Fully Distributed Zero-Knowledge Proofs. **IEEE S&P 2024** [Google Scholar](https://scholar.google.com/scholar?q=Pianist+Scalable+zkRollups+via+Fully+Distributed+Zero-Knowledge+Proofs)
> 核心思路：将Plonk协议分布式化，优化整体性能。
> 局限与区别：同样不保护隐私。Siniel可作为上层隐私保护框架，与这些分布式ZKP技术结合。

### 核心技术与方案

**整体框架**  
Siniel由离线阶段和在线阶段构成。离线阶段，委托者D通过Shamir秘密共享将见证向量$\vec{w}$分割为份额$[\vec{w}]_i$，并为每个工人$P_i$生成认证标签$\tau_{[w]_i} = \mu^{(i)} \cdot [w]_i + v_{[w]_i}$，同时向其他工人$P_j$分发分段密钥$[\mu^{(i)}]_j$和$[v_{[w]_i}]_j$。在线阶段分为三个模块：见证一致性检查、PIOP计算与一致性检查、证明生成。

**见证一致性检查**  
在PIOP计算开始前，所有工人通过理想功能$F_{wcc}$验证每个工人对其份额的承诺是否正确。协议中，工人广播随机点$\alpha$的份额、恢复$\alpha$，然后打开份额多项式在$\alpha$处的值$\vec{w}'(\alpha)$并附上KZG打开证明，最后恢复$\vec{w}(\alpha)$并检查$\vec{w}'(\alpha)=\vec{w}(\alpha)$且打开证明有效。这保证了工人后续PIOP计算所使用的输入份额与最初承诺一致。

**PIOP一致性检查**  
在每轮PIOP计算后，每个工人$P_i$向其它工人证明其计算正确。其它工人发送随机挑战$\beta$，$P_i$响应多项式$f^{(k)}(\beta)$、对应认证标签$\tau_{f^{(k)}(\beta)}$和KZG打开证明。其它工人更新密钥$[v_{f^{(k)}(\beta)}]_j$，重构$\mu$和$v_{f^{(k)}(\beta)}$，验证$\tau_{f^{(k)}(\beta)} = \mu \cdot f^{(k)}(\beta) + v_{f^{(k)}(\beta)}$且KZG验证通过。由于认证标签的线性同态性，工人可在PIOP计算中本地更新标签与密钥，使得该检查器仅需简单挑战-响应交互，无需委托者参与。

**证明生成**  
若所有一致性检查通过，工人通过Fiat-Shamir变换获得查询点$Q$，计算份额多项式的评估值和打开证明，然后使用OutputF和OutputG恢复最终证明$\pi = (C_{\vec{p}_k}, \vec{p}_k(Q), \pi_{\vec{p}_k})$。工人共同验证$\pi$的有效性，若至少$t+1$个工人认可，则发送给委托者。

**安全性与复杂度**  
Siniel在诚实多数假设（$n=2t+1$）下对恶意工人可撤消安全（secure with abort）。安全证明分为混合论证：通过模拟器$S$在理想世界中模拟诚实工人的行为，利用PIOP的零知识性和KZG的知识可靠性论证现实世界与理想世界不可区分。通信复杂度：离线阶段委托者需向每个工人发送份额及认证材料，总开销$O(n|w|+n^2)$；在线阶段工人间交互主要为一致性检查中的挑战-响应和证明聚合，通信量远小于EOS（后者委托者需全程在线）。计算复杂度：委托者仅执行离线操作（秘密分享、认证标签生成），在线阶段完全由工人承担。

### 核心公式与流程

**[认证标签生成]**
$$\tau_{[w]_i} = \mu^{(i)} \cdot [w]_i + v_{[w]_i}$$
> 作用：工人$P_i$持有份额$[w]_i$和标签$\tau_{[w]_i}$；其他工人$P_j$持有密钥$(\mu^{(i)}, v_{[w]_i})$的分段。线性同态性允许在PIOP计算中本地更新标签与密钥，最终通过挑战验证$\tau = \mu \cdot w + v$来检测份额是否被篡改。

**[见证一致性检查器协议（核心步骤）]**
1. 广播$[\alpha]_i$并恢复$\alpha$。
2. 计算$([\vec{w}]_i(\alpha), \pi_{[\vec{w}]_i}) := \text{KZG.Open}(ck, [\vec{w}]_i, C_{[\vec{w}]_i}, \alpha)$。
3. 聚合：$C_{\vec{w}} := \text{Output}_G(C_{[\vec{w}]_i})$，$\vec{w}'(\alpha) := \text{Output}_F([\vec{w}]_i(\alpha))$，$\pi_{\vec{w}} := \text{Output}_G(\pi_{[\vec{w}]_i})$。
4. 恢复$\vec{w}(\alpha)$并检查$\vec{w}'(\alpha)=\vec{w}(\alpha)$且$\text{KZG.Verify}(ck, \pi_{\vec{w}}, C_{\vec{w}}, \vec{w}(\alpha), \alpha)=1$。
> 作用：保证每个工人使用的输入份额与初始承诺一致，防止恶意工人在PIOP计算前替换份额。

**[PIOP一致性检查器协议（核心步骤）]**
1. 其他工人发送随机挑战$\beta$给$P_i$。
2. $P_i$响应：$(f^{(k)}(\beta), \pi_k) = \text{KZG.Open}(ck, f, com, \beta)$，$\tau_{f^{(k)}(\beta)} = \tau_{f_0^{(k)}} + \tau_{f_1^{(k)}}\cdot\beta + \cdots + \tau_{f_d^{(k)}}\cdot\beta^d$。
3. 其他工人更新$[v_{f^{(k)}(\beta)}]_j$并重构$\mu, v_{f^{(k)}(\beta)}$，验证$\tau_{f^{(k)}(\beta)} = \mu\cdot f^{(k)}(\beta) + v_{f^{(k)}(\beta)}$且$\text{KZG.Verify}(ck, \pi_k, com_{f^{(k)}}, f^{(k)}(\beta), \beta)=1$。
> 作用：同时验证PIOP计算的正确性（通过认证标签）和承诺的一致性（通过KZG打开证明），且无需委托者参与。

**[Siniel离线阶段分发内容]**
发送给$P_i$：$([\alpha]_i, \mathbf{x}, [\vec{w}]_i, [\vec{w}(\alpha)]_i, \{\tau_{[w_k]_i}\}, \{( [a]_i,[b]_i,[c]_i ), (\tau_{[a]_i},\tau_{[b]_i},\tau_{[c]_i})\})$  
发送给$P_j$：$([\mu^{(i)}]_j, \{[v_{[w_k]_i}]_j\}, \{[v_{[a]_i}]_j, [v_{[b]_i}]_j, [v_{[c]_i}]_j\})$
> 作用：委托者一次性地将所有必要份额、认证标签、Beaver三元组及密钥分发给工人，后续在线阶段无需再与委托者通信。

### 实验结果
实验使用AWS c5a实例，1个委托者（16核32GB）和3个工人（32核64GB）。电路规模从$2^{12}$到$2^{20}$，测试三种带宽：10MBps、100MBps、1000MBps。针对SHA256压缩函数（电路约2万门），在10MBps下Siniel委托者耗时6.5秒，比EOS的8.8秒节省约16%；在1000MBps下Siniel委托者仅需0.17秒，较EOS的2.07秒节省约80%。工人侧在低带宽（10MBps）时Siniel耗时约130秒（$2^{20}$），优于EOS的400秒；但在高带宽（1000MBps）时Siniel约79秒，稍慢于EOS的70秒，原因是Siniel多出的内部一致性检查计算开销在网络延迟极低时成为主导。整体而言，Siniel显著降低了委托者的时间开销，尤其在高带宽环境下优势明显。

### 局限性与开放问题
Siniel假设诚实多数（最多$t=\frac{n-1}{2}$个恶意工人），而EOS支持恶意多数场景，因此Siniel的安全模型相对更弱。在需要更强对抗假设（如拜占庭容错中1/3阈值）的应用中，Siniel的假设仍然合理，但对于要求任意数量恶意方的场景则不适用。此外，Siniel的离线阶段需要生成大量认证标签和Beaver三元组，增加了预处理负担。未来工作可探索与分布式ZKP技术（如Pianist）结合，以提升系统可扩展性并降低每工人计算负载。

### 强关联论文

[CLMZ23] Chiesa等. EOS: Efficient Private Delegation of zkSNARK Provers. **USENIX Security 2023** [Google Scholar](https://scholar.google.com/scholar?q=EOS+Efficient+Private+Delegation+of+zkSNARK+Provers)

[GGJ+23] Garg等. zkSaaS: Zero-Knowledge SNARKs as a Service. **USENIX Security 2023** [Google Scholar](https://scholar.google.com/scholar?q=zkSaaS+Zero-Knowledge+SNARKs+as+a+Service)

[GGW23] Garg等. How to Prove Statements Obliviously? **Cryptology ePrint Archive 2023** [Google Scholar](https://scholar.google.com/scholar?q=How+to+Prove+Statements+Obliviously)

[OB22] Ozdemir等. Experimenting with Collaborative zk-SNARKs. **USENIX Security 2022** [Google Scholar](https://scholar.google.com/scholar?q=Experimenting+with+Collaborative+zk-SNARKs)

[WZC+18] Wu等. DIZK: A Distributed Zero Knowledge Proof System. **USENIX Security 2018** [Google Scholar](https://scholar.google.com/scholar?q=DIZK+Distributed+Zero+Knowledge+Proof+System)

[XZC+22] Xie等. deVirgo: Distributed Zero-Knowledge Proof Protocol of Virgo. **CCS 2022** [Google Scholar](https://scholar.google.com/scholar?q=deVirgo+Distributed+Zero-Knowledge+Proof+Protocol+of+Virgo)

[LXZ+24] Liu等. Pianist: Scalable zkRollups via Fully Distributed Zero-Knowledge Proofs. **IEEE S&P 2024** [Google Scholar](https://scholar.google.com/scholar?q=Pianist+Scalable+zkRollups+via+Fully+Distributed+Zero-Knowledge+Proofs)


## 关键词

+ 分布式zkSNARK
+ 证明委托
+ 多项式交互式预言证明（PIOP）
+ 多项式承诺方案
+ 隐私保护证明生成
+ 多方计算