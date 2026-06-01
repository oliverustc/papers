---
title: "VeRSA: Verifiable registries with efficient client audits from RSA authenticated dictionaries"
doi: 10.1145/3548606.3560605
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2022
created: 2025-04-21 11:14:58
modified: 2025-04-21 11:15:27
---
## VeRSA: Verifiable registries with efficient client audits from RSA authenticated dictionaries

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3548606.3560605)
+ [code](https://github.com/nirvantyagi/versa)

## 作者

+ [[Nirvan Tyagi]] 
+ [Ben Fisch](Ben%20Fisch.md)
+ Andrew Zitek 
+ [[Joseph Bonneau]] 
+ Stefano Tessaro 

## 笔记

### 背景与动机

透明度系统要求注册表服务器提供不可否认的承诺和可审计的历史记录。现有可验证注册表 [26, 54, 55] 主要依赖 Merkle 树实现认证字典，但为了确保全局不变性（如版本号单调递增）在各 epoch 之间被保持，必须由第三方审计者进行线性于 epoch 次数的昂贵审计工作。为降低客户端审计开销，已有方案采用增量可验证计算（IVC）[28, 74]，通过递归 SNARK 生成随 epoch 数增长的简洁证明。然而，将 Merkle 路径验证编码为 SNARK 电路导致电路规模与更新次数成线性，实际吞吐量低于每秒 5 次密钥更新，远不能满足证书透明度（约 60 次/秒）[32] 等应用的需求。本文旨在构建客户端可直接审计的高吞吐量可验证注册表，填补现有方案在更新吞吐与审计效率之间的空白。

### 相关工作

[55] Melara 等. CONIKS: Bringing Key Transparency to End Users. **USENIX Security 2015** [Google Scholar](https://scholar.google.com/scholar?q=CONIKS%3A+Bringing+Key+Transparency+to+End+Users)
> 核心思路：基于 Merkle 树构建可验证注册表，提供密钥查找和监控。
> 局限与区别：审计需要线性于 epoch 次数的工作，客户端不能自行高效审计；本文通过 RSA 累加器实现不变性证明的常规模拟电路，大幅降低 SNARK 证明成本。

[26] Chase 等. SEEMless: Secure End-to-End Encrypted Messaging with less Trust. **CCS 2019** [Google Scholar](https://scholar.google.com/scholar?q=SEEMless%3A+Secure+End-to-End+Encrypted+Messaging+with+less+Trust)
> 核心思路：同样基于 Merkle 树，引入外包审计以减少客户端负担。
> 局限与区别：仍假设存在可信第三方审计者，本文追求完全由客户端完成审计。

[54] Meiklejohn 等. Think Global, Act Local: Gossip and Client Audits in Verifiable Data Structures. **2020** (arXiv) [Google Scholar](https://scholar.google.com/scholar?q=Think+Global%2C+Act+Local%3A+Gossip+and+Client+Audits+in+Verifiable+Data+Structures)
> 核心思路：提出紧致范围和 gossip 协议用于注册表审计。
> 局限与区别：审计仍依赖第三方或线性成本，本文将其检查点思想与摊销证明结合实现无 SNARK 的客户端审计。

[28] Chen 等. Reducing Participation Costs via Incremental Verification for Ledger Systems. **ePrint 2020** [Google Scholar](https://scholar.google.com/scholar?q=Reducing+Participation+Costs+via+Incremental+Verification+for+Ledger+Systems)
> 核心思路：提出 IVC 用于注册表审计，递归 SNARK 证明 epoch 间不变性。
> 局限与区别：使用 Merkle 树导致电路随更新数线性增长，证明成本高；本文用 RSA 累加器将电路规模降为常数。

[43] Hu 等. Merkle²: A Low-Latency Transparency Log System. **IEEE S&P 2021** [Google Scholar](https://scholar.google.com/scholar?q=Merkle%C2%B2%3A+A+Low-Latency+Transparency+Log+System)
> 核心思路：利用签名链和 Merkle 扩展证明减少审计成本为对数。
> 局限与区别：依赖签名链（密钥更新必须由授权密钥签名），不适用于账户恢复等场景；本文的构造适用于更一般的密钥更新策略。

[51] Leung 等. Aardvark: A Concurrent Authenticated Dictionary with Short Proofs. **ePrint 2020** [Google Scholar](https://scholar.google.com/scholar?q=Aardvark%3A+A+Concurrent+Authenticated+Dictionary+with+Short+Proofs)
> 核心思路：使用双线性对累加器构建认证字典，支持并行更新。
> 局限与区别：不变性证明为线性大小，且更新提示计算代价高；本文的 RSA 累加器无需更新提示，且不变性证明为常数大小。

[70] Tomescu 等. Transparency Logs via Append-Only Authenticated Dictionaries. **CCS 2019** [Google Scholar](https://scholar.google.com/scholar?q=Transparency+Logs+via+Append-Only+Authenticated+Dictionaries)
> 核心思路：使用双线性对累加器实现只追加字典，支持对数大小的不变性证明。
> 局限与区别：渐近效率好但具体代价高，且本文的 RSA 构造在相同渐近下实现更具体高效。

[74] Tzialla 等. Transparency Dictionaries with Succinct Proofs of Correct Operation. **ePrint 2021** [Google Scholar](https://scholar.google.com/scholar?q=Transparency+Dictionaries+with+Succinct+Proofs+of+Correct+Operation)
> 核心思路：利用折叠方案（Nova）替代递归 SNARK，实现每 epoch 仅需一个折叠证明加一个 SNARK 证明，客户端审计代价线性于 epoch 次数。
> 局限与区别：客户端审计线性成本在长时间离线时远高于本文的对数级审计；本文的 VeRSA-Amtz 通过摊销证明和检查点审计实现对数级审计成本。

[72] Tomescu 等. Authenticated Dictionaries with Cross-Incremental Proof (Dis)aggregation. **ePrint 2020** [Google Scholar](https://scholar.google.com/scholar?q=Authenticated+Dictionaries+with+Cross-Incremental+Proof+%28Dis%29aggregation)
> 核心思路：提出 RSA 累加器用于字典，但不支持关于值变化的版本不变性证明。
> 局限与区别：缺少本文关注的值映射变化证明，无法直接用于可验证注册表。

### 核心技术与方案

本文整体框架如图 1 所示，分为三个层次：底层认证字典（AD）支持版本不变性证明；中间层通过 IVC 或摊销证明将 AD 提升为认证历史字典（AHD）；顶层结合公告板与检查点审计机制构建可验证注册表。

**1. RSA 认证字典与版本不变性证明**  
本文基于 KVaC 构造 [2] 扩展。KVaC 的摘要为：
$$
d \leftarrow \left(g^{\left(\prod_i \mathsf{H}(k_i)^{u_i}\right) \cdot \left(\sum_i v_i / \mathsf{H}(k_i)\right)},\; g^{\prod_i \mathsf{H}(k_i)^{u_i}}\right),
$$
其中 $\mathsf{H}$ 将密钥映射到素数，$u_i$ 为版本号。批更新时，对多个 $(k_i, \delta_i)$ 计算 $Z = \prod_i \mathsf{H}(k_i)$ 和 $\Delta = Z \cdot \sum_i \delta_i / \mathsf{H}(k_i)$，新摘要为 $(d_1^Z d_2^\Delta, d_2^Z)$。  
核心贡献是构造了版本不变性的简洁证明：证明者生成知识证明满足关系
$$
\mathcal{R}_{\mathsf{KVaC}} = \{((X_1,X_2,Y_1,Y_2);(\alpha,\beta)): Y_1 = X_1^\alpha X_2^\beta \wedge Y_2 = X_2^\alpha \}.
$$
直觉上，若版本不变性被违反（如相同版本号不同值），则存在算法可从中分解 RSA 模数，从而归约到 Strong-RSA 假设。该证明使用 [11] 的整数离散对数知识证明系统，常规模拟电路大小（约 20M 约束），且证明大小为常数。

**2. 认证历史字典（AHD）**  
AHD 承诺当前状态及所有历史状态，支持高效的不变性证明。本文给出两种构造：

- **AHD-IVC**（第 5.3 节）：每 epoch 计算递归 SNARK 证明，其中 SNARK 电路验证：① AD 的不变性证明 $\pi_\Phi$，② 历史向量承诺（VC）的更新证明 $\pi_{\mathrm{hist}}$，③ 递归验证上一 epoch 的 SNARK。该构造适用于任何支持不变性证明的 AD。由于 RSA AD 的 $\pi_\Phi$ 验证电路为常数大小（而 Merkle 树的验证电路随更新数线性增长），VeRSA-IVC 的 SNARK 证明时间远低于 MT-VR-IVC。

- **AHD-Amtz**（第 5.4 节）：利用紧致范围（compact range）性质，预计算所有形如 $[a \cdot 2^b, a \cdot 2^b + 2^b)$ 子区间的不变性证明。紧致范围的数目为 $O(N \log N)$，但可通过经典摊销将每 epoch 的预计算代价控制在 $O(\log N)$。对于任意查询区间 $[c_j, c_{j+1})$，可拼接 $O(\log N)$ 个预计算证明即可得到整体不变性证明。该构造无需 SNARK，但要求底层 AD 支持简洁的不变性证明（RSA AD 满足，Merkle AD 不满足）。

**3. 客户端检查点审计**  
客户端在每次操作（查询、监控、更新）时，对从上次上线到当前 epoch 的区间进行审计。客户端计算该区间的紧致范围表示，得到 $O(\log N)$ 个检查点 epoch，然后请求服务器提供这些检查点之间的不变性证明（对于 AHD-Amtz 即为预计算的子区间证明）。  
关键性质（定理 1）：任意两个重叠区间共享至少一个检查点。因此，两个客户端各自审计的 epoch 序列通过共享检查点隐式保证了一致性，有效防止振荡攻击（oscillation attack）。该模型允许客户端暂时接受不一致状态（直至下一个共享检查点），但保证最终检测到不一致。该安全性质可形式化定义为“最终检测”（eventual detection）。

渐进复杂度：客户端审计证明大小 $O(\log N)$，验证时间 $O(\log N)$（对于 AHD-IVC 中含递归 SNARK 可进一步优化为常数，但本文中仍需对数个历史承诺证明）；服务器更新 epoch 时，VeRSA-IVC 代价为常规模拟时间 + 批更新 RSA 求幂，VeRSA-Amtz 每 epoch 摊销 $O(\log N)$ 次预计算。

### 核心公式与流程

**[KVaC 批更新公式]**
$$
Z \leftarrow \prod_i \mathsf{H}(k_i),\quad \Delta \leftarrow Z \cdot \sum_i \delta_i / \mathsf{H}(k_i), \quad d' = (d_1^Z d_2^\Delta,\; d_2^Z).
$$
> 作用：将多个密钥的增量 $\delta_i$ 合并为单个指数运算，实现批更新，为简洁不变性证明奠定基础。

**[版本不变性知识证明关系]**
$$
\mathcal{R}_{\mathsf{KVaC}} = \{((X_1,X_2,Y_1,Y_2);(\alpha,\beta)): Y_1 = X_1^\alpha X_2^\beta \wedge Y_2 = X_2^\alpha \}.
$$
> 作用：证明者只需证明存在 $\alpha, \beta$ 使上述等式成立，而不需证明 $\alpha,\beta$ 具有特定结构（如由哈希到素数的乘积构成），即可确保版本不变性。安全证明基于 Strong-RSA 假设：若可伪造证明违反版本不变性，则可提取非平凡因子。

**[紧致区间定义]**
令 $[L,R)$ 为 epoch 区间。其紧致表示为满足 $L_1=L$, $R_m=R$, $R_i = L_{i+1}$，且每个子区间形如 $[a\cdot 2^b,\; a\cdot 2^b+2^b)$ 的最小集合 $\{(L_i,R_i)\}_{i=1}^m$，其中 $m = O(\log(R-L))$。
> 作用：用于客户端选择检查点 epoch 以及 AHD-Amtz 预计算单位区间的不变性证明。

### 实验结果

实验在 Amazon EC2 r5.16xlarge（32 核，512 GB RAM）上进行。对比基线包括 MT-VR（Merkle 树无审计优化）、MT-VR-IVC（Merkle + IVC）、VeRSA-IVC 和 VeRSA-Amtz。  
- **客户端审计成本**（图 4）：对于 epoch 区间长度从 32 到 1000，VeRSA-IVC 和 VeRSA-Amtz 的证明大小在 1–20 KB 之间，验证时间在 5–100 ms 之间，而 MT-VR 的审计成本线性增长，区间长度 1000 时带宽和验证时间分别为 $10^5$ 倍和 $10^3$ 倍差距。  
- **服务器更新吞吐量**（图 5）：MT-VR 达到 40,000 updates/s，但不产生可审计简洁证明。VeRSA-IVC 在批处理 20000 个密钥更新时可实现约 60 updates/s（延迟约 30 分钟），VeRSA-Amtz 达到约 90 updates/s（延迟与密钥数成比例）。MT-VR-IVC 仅约 1 update/s（受限于 Merkle 路径验证的 SNARK 电路规模）。  
- **SNARK 电路规模**（图 6 左）：对于 0–4000 个密钥更新，RSA AD 的电路约束恒约 20M，而 Merkle AD 的约束随更新数线性增长（每个更新约 20K 约束）。  
- **并行化**（图 6 右）：SNARK 证明时间可近似线性扩展到 16–32 核。  
- **查找证明成本**（图 7）：RSA 查找证明计算代价高：对于 100 万条目的注册表，全部成员证明的重计算需要约 3 小时（单线程）；单个证明的更新代价随中间密钥更新数线性增长（60 updates/s 下 213 个更新需约 10 秒）。验证时间随版本号线性增长（版本号 1000 时约 0.8 秒）。  
- **适用规模**：RSA 方案适合百万级条目（如应用商店 app 或 Signal 用户），不适合证书透明度（3.4 亿域名）或 WhatsApp（20 亿用户）。

### 局限性与开放问题

RSA 查找证明的计算和验证成本远高于 Merkle 树方案，限制了其在超大规模注册表中的应用；RSA 群需要可信设置（虽然可用多方协议生成，但仍增加部署复杂度）；版本号线性增长的验证时间要求版本号不超过数千，对于频繁更新的应用可能需要引入变体（如树形划分降低验证复杂度）；目前客户端检查点审计的安全性定义为最终检测，未涉及检测延迟的上界，需要针对具体应用场景评估。

### 强关联论文

[2] Agrawal et al. KVaC: Key-Value Commitments for Blockchains and Beyond. **ASIACRYPT 2020** [Google Scholar](https://scholar.google.com/scholar?q=KVaC%3A+Key-Value+Commitments+for+Blockchains+and+Beyond)

[55] Melara et al. CONIKS: Bringing Key Transparency to End Users. **USENIX Security 2015** [Google Scholar](https://scholar.google.com/scholar?q=CONIKS%3A+Bringing+Key+Transparency+to+End+Users)

[54] Meiklejohn et al. Think Global, Act Local: Gossip and Client Audits in Verifiable Data Structures. **2020** (arXiv) [Google Scholar](https://scholar.google.com/scholar?q=Think+Global%2C+Act+Local%3A+Gossip+and+Client+Audits+in+Verifiable+Data+Structures)

[26] Chase et al. SEEMless: Secure End-to-End Encrypted Messaging with less Trust. **CCS 2019** [Google Scholar](https://scholar.google.com/scholar?q=SEEMless%3A+Secure+End-to-End+Encrypted+Messaging+with+less+Trust)

[28] Chen et al. Reducing Participation Costs via Incremental Verification for Ledger Systems. **ePrint 2020** [Google Scholar](https://scholar.google.com/scholar?q=Reducing+Participation+Costs+via+Incremental+Verification+for+Ledger+Systems)

[74] Tzialla et al. Transparency Dictionaries with Succinct Proofs of Correct Operation. **ePrint 2021** [Google Scholar](https://scholar.google.com/scholar?q=Transparency+Dictionaries+with+Succinct+Proofs+of+Correct+Operation)

[70] Tomescu et al. Transparency Logs via Append-Only Authenticated Dictionaries. **CCS 2019** [Google Scholar](https://scholar.google.com/scholar?q=Transparency+Logs+via+Append-Only+Authenticated+Dictionaries)

[51] Leung et al. Aardvark: A Concurrent Authenticated Dictionary with Short Proofs. **ePrint 2020** [Google Scholar](https://scholar.google.com/scholar?q=Aardvark%3A+A+Concurrent+Authenticated+Dictionary+with+Short+Proofs)

[43] Hu et al. Merkle²: A Low-Latency Transparency Log System. **IEEE S&P 2021** [Google Scholar](https://scholar.google.com/scholar?q=Merkle%C2%B2%3A+A+Low-Latency+Transparency+Log+System)

[72] Tomescu et al. Authenticated Dictionaries with Cross-Incremental Proof (Dis)aggregation. **ePrint 2020** [Google Scholar](https://scholar.google.com/scholar?q=Authenticated+Dictionaries+with+Cross-Incremental+Proof+%28Dis%29aggregation)


## 关键词

+ 可验证注册表
+ RSA累加器
+ 可审计
+ 认证字典
+ 区块链