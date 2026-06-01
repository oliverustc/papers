---
title: "CHURP: Dynamic-committee proactive secret sharing"
doi: 10.1145/3319535.3363203
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2019
modified: 2025-04-13 13:54:13
---
## CHURP: Dynamic-committee proactive secret sharing

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3319535.3363203)

## 作者

+ Sai Krishna Deepak Maram 
+ Fan Zhang 
+ Lun Wang 
+ Andrew Low 
+ [Yupeng Zhang](Yupeng%20Zhang.md) 
+ Ari Juels 
+ [Dawn Song](Dawn%20Song.md) 

## 笔记

### 背景与动机

用户密钥的安全存储是密码系统，尤其是区块链等去中心化系统中的普遍难题。据估计约四百万比特币因密钥丢失而永久消失 [63]。许多用户因此依赖中心化交易所托管密钥，但这侵蚀了区块链的去中心化本质。秘密共享，特别是主动秘密共享（PSS），通过定期刷新份额防止对手逐步攻陷节点，提供了更强的安全性。然而，现有 PSS 方案要么只支持静态委员会 [17, 44]，要么假设弱被动对手 [26, 64]，要么通信成本过高 [12, 54, 66, 71, 73]。在区块链环境中，节点可以随时加入或离开（即节点更替），而现有的动态委员会 PSS 方案无法同时满足低通信开销和强安全假设。本文提出的 CHURP 是第一个支持动态委员会、容忍主动对手且通信复杂度低的实用 PSS 方案，其乐观情况下每轮仅需 O(n) 链上通信和 O(n²) 点对点通信。

### 相关工作

[17] Cachin 等. Asynchronous verifiable secret sharing and proactive cryptosystems. **ACM CCS 2002** [Google Scholar](https://scholar.google.com/scholar?q=Asynchronous+verifiable+secret+sharing+and+proactive+cryptosystems)
> 核心思路：提出异步环境下的可验证秘密共享和主动密码系统。
> 局限与区别：仅支持静态委员会，且通信复杂度为 O(n⁴)（与本文动态委员会且 O(n²) 不同）。

[44] Herzberg 等. Proactive secret sharing or: How to cope with perpetual leakage. **CRYPTO 1995** [Google Scholar](https://scholar.google.com/scholar?q=Proactive+secret+sharing+or:+How+to+cope+with+perpetual+leakage)
> 核心思路：首次提出主动秘密共享（PSS），通过定期刷新份额防御持续性泄露。
> 局限与区别：仅支持静态委员会，且主动化过程通信复杂度为 O(n³)（本文的 bivariate 0-sharing 将其降至 O(n²)）。

[66] Schultz 等. Mobile proactive secret sharing. **ACM PODC 2008** [Google Scholar](https://scholar.google.com/scholar?q=Mobile+proactive+secret+sharing)
> 核心思路：首个支持动态委员会的实用主动秘密共享方案，针对异步网络假设 t < n/3。
> 局限与区别：通信复杂度高达 O(n⁴)（本文乐观路径为 O(n²)，且支持更高阈值 t < n/2）。

[12] Baron 等. Communication-optimal proactive secret sharing for dynamic groups. **ACNS 2015** [Google Scholar](https://scholar.google.com/scholar?q=Communication-optimal+proactive+secret+sharing+for+dynamic+groups)
> 核心思路：提出通信最优的动态组主动秘密共享，可批量传输秘密。
> 局限与区别：依赖虚拟化技术和恶意安全 MPC，实际委员会规模需极大（例如 576 组每组 576 节点），实用性差（本文对任意规模均适用）。

[45] Kate 等. Constant-size commitments to polynomials and their applications. **ASIACRYPT 2010** [Google Scholar](https://scholar.google.com/scholar?q=Constant-size+commitments+to+polynomials+and+their+applications)
> 核心思路：提出常数大小的多项式承诺（KZG），支持高效验证。
> 局限与区别：需要可信设置和 t-SDH 假设；本文引入 hedged 机制在假设失效时降级至 t < n/3。

[24] Desmedt 和 Jajodia. Redistributing secret shares to new access structures and its applications. **Technical Report 1997** [Google Scholar](https://scholar.google.com/scholar?q=Redistributing+secret+shares+to+new+access+structures+and+its+applications)
> 核心思路：提出秘密共享的份额重新分配，支持委员会和阈值变化。
> 局限与区别：方案不可验证，且对手模型较弱；本文的可验证维度切换基于此技术但加入了安全性证明。

[32] Frankel 等. Optimal-resilience proactive public-key cryptosystems. **FOCS 1997** [Google Scholar](https://scholar.google.com/scholar?q=Optimal-resilience+proactive+public-key+cryptosystems)
> 核心思路：提出最优弹性主动公钥密码系统。
> 局限与区别：主要针对公钥系统，本文将其中的 resharing 技术用于 bivariate 0-sharing 以降低通信。

### 核心技术与方案

CHURP 采用三层协议架构：乐观路径 Opt-CHURP、悲观路径 Exp-CHURP-A 和 Exp-CHURP-B。系统默认运行 Opt-CHURP，仅当检测到节点作弊或 KZG 假设失效时才切换至更昂贵的路径。

底层核心是两个创新技术：双变量 0-分享和维度切换。**双变量 0-分享**用于主动化阶段，目的是生成一个随机双变量多项式 $Q(x,y)$ 满足 $Q(0,0)=0$，使得秘密 $s = B(0,0)$ 保持不变，但份额被刷新。传统方案中每个节点生成自己的 0-洞多项式并分发 $O(n)$ 个点，总通信 $O(n^3)$。CHURP 的 BivariateZeroShare 协议先令一个大小为 $2t+1$ 的子集执行 UnivariateZeroShare 生成单变量零多项式 $P(x)$ 的份额 $s_j$，然后每个节点将其 $s_j$ 通过随机多项式 $R_j(x)$ 重新分享给整个委员会。最终每个节点得到 $Q(i,y)$。该过程总通信为 $O(tn)$，在乐观情况下为 $O(n^2)$。协议支持主动对手，通过承诺和 Lagrange 系数检查确保正确性：$\prod_{j=1}^{2t+1} (g^{s_j})^{\lambda_j^{2t}} = 1$。

**维度切换**用于应对握手期间对手可能同时控制旧委员会和新委员会共 $2t$ 个节点的问题。CHURP 使用不对称双变量多项式 $B(x,y)$，其中 $x$ 方次为 $t$，$y$ 方次为 $2t$。稳定状态下节点持有全份额 $B(i,y)$（即 $i$ 方向上 $2t$ 次多项式），此时为 $(t,n)$-门限分享。握手时，新委员会子集 $\mathcal{U}'$ 中的节点收到旧委员会成员发送的点 $B(i,j)$，插值得出缩减份额 $B(x,j)$（即 $j$ 方向上 $t$ 次多项式），此时变为 $(2t,n)$-门限分享，因此对手控制 $2t$ 个节点也无法重构秘密。主动化阶段新增随机 $Q(x,y)$ 后，再通过全份额分发（再次维度切换）恢复 $(t,n)$-门限，并确保新份额独立于旧份额。

Opt-CHURP 的协议流程：Opt-ShareReduce（降低维度）、Opt-Proactivize（主动化）、Opt-ShareDist（恢复全份额）。每个节点在乐观路径中仅需 O(1) 次链上交易和 O(n) 次点对点通信，总复杂度 O(n) 链上、O(n²) 点对点。安全证明依赖于 KZG 承诺的隐藏性和绑定性（基于离散对数假设）以及双变量多项式的随机性。当检测到作弊时，切换至 Exp-CHURP-A（全部通过链上通信，$O(n^2)$ 链上成本，需 $t<n/2$）。若 KZG 假设失效，则切换至 Exp-CHURP-B（也使用链上通信，但需 $t<n/3$）。Hedge机制 StateVerif 仅需 $O(n)$ 链上成本即可检测 KZG 失败。

### 核心公式与流程

**双变量多项式与维度切换**
$$B(x,y) \text{ 满足 } B(0,0)=s,\quad \deg_x B = t,\ \deg_y B = 2t.$$
全份额：$FS_i(y)=B(i,y)$（$2t$ 次多项式）；缩减份额：$RS_j(x)=B(x,j)$（$t$ 次多项式）。

> 作用：定义秘密分享方案的基本对象，维度切换通过改变使用的维度来调整门限值。

**0-分享验证**
$$\prod_{j=1}^{2t+1} (g^{s_j})^{\lambda_j^{2t}} = 1,$$
其中 $\lambda_j^{2t}$ 是 Lagrange 系数，$s_j$ 是 UnivariateZeroShare 的输出。

> 作用：确保所有 $s_j$ 对应一个 0-洞多项式 $P(x)$，即 $\sum_{j} \lambda_j s_j = 0$，保证 $Q(0,0)=0$。

**BivariateZeroShare 生成 $Q(x,y)$**
节点 $\mathcal{U}_j$ 生成 $R_j(x)$ 满足 $R_j(0)=s_j$，并发送 $R_j(i)=Q(i,j)$ 给节点 $C_i$。节点 $C_i$ 收到 $2t+1$ 个点后插值得 $Q(i,y)$（$2t$ 次多项式）。

> 作用：从单变量 0-分享秘密出发，通过 resharing 高效构造双变量 0-洞多项式，总通信 $O(tn)$。

**Opt-CHURP 三个阶段的关键操作**
- Opt-ShareReduce：$C_i$ 发送 $(B(i,j), W_{B(i,j)})$ 给 $\mathcal{U}'_j$，$\mathcal{U}'_j$ 验证并插值得 $B(x,j)$。
- Opt-Proactivize：$\mathcal{U}'_j$ 生成 $g^{s_j}, C_{Z_j}, W_{Z_j(0)}, C_{B'(x,j)}$，并发布哈希上链。验证 $C_{B'(x,j)} = C_{B(x,j)} \times C_{Z_j} \times g^{s_j}$ 和 $\prod (g^{s_j})^{\lambda_j}=1$。
- Opt-ShareDist：$\mathcal{U}'_j$ 发送 $(B'(i,j), W'_{B(i,j)})$ 给 $C_i'$，$C_i'$ 验证并插值得全份额 $B'(i,y)$。

> 作用：三个阶段分别完成维度降低、主动化、维度恢复，确保秘密不变且新旧份额独立。

### 实验结果

实验在最多 1000 个 EC2 c5.large 实例上进行，每个实例作为委员会节点，执行 1000 轮 Opt-CHURP 取平均。**局域网 (LAN) 设置**下，1001 个节点时总执行时间约 3 分钟，其中 Opt-ShareDist 阶段占主导（因 KZG CreateWitness 需 $O(n^2)$ 指数运算）。**广域网 (WAN) 设置**下（跨多区域），100 节点时协议延迟约 4.54 秒，比 LAN 的 2.92 秒多约 1.6 秒，该额外延迟与节点数无关。**链上通信**：每轮每个节点仅写入 1 个哈希（32 字节），总复杂度 $O(n)$。**点对点通信**：对于 $t=50, n=101$，点对点数据量约 2.3 MB。与 Schultz-MPSS [66] 的乐观路径相比，相同委员会规模下（例如 n=100），Opt-CHURP 的点对点通信量为 2.3 MB，而 Opt-Schultz-MPSS 约为 53.7 GB（因为其复杂度为 $O(n^4)$），即 CHURP 降低了约 2300 倍。对于 $n \ge 65$，改进至少三个数量级。由于 Schultz-MPSS 开销巨大，实验未运行超过 100 节点。Transaction Ghosting 技术实验显示，在以太坊主网上，平均带宽 32.3 KB/s，成本约 $0.06/MB，延迟 1.09 秒，比链上通信便宜两个数量级以上。

### 局限性与开放问题

CHURP 的乐观路径依赖同步网络假设，需要短暂的同步期（分钟级）以完成握手；若消息延迟，则切换至昂贵的链上悲观路径。KZG 承诺的可信设置是协议唯一信任假设，StateVerif 可在假设失效时降级，但降级后阈值降至 $t < n/3$。阈值变化（增大或减小）虽已支持，但需要额外假设（如 q-PKE）且仅支持有限变化范围。点对点通信技术 Transaction Ghosting 可能被视为对区块链网络的滥用，且存在约 8% 的丢包率，需要工程优化以提高可靠性。本文未讨论完整的轻客户端验证或分布式密钥生成的具体集成。

### 强关联论文

[44] Herzberg 等. Proactive secret sharing or: How to cope with perpetual leakage. **CRYPTO 1995** [Google Scholar](https://scholar.google.com/scholar?q=Proactive+secret+sharing+or:+How+to+cope+with+perpetual+leakage)

[66] Schultz 等. Mobile proactive secret sharing. **ACM PODC 2008** [Google Scholar](https://scholar.google.com/scholar?q=Mobile+proactive+secret+sharing)

[12] Baron 等. Communication-optimal proactive secret sharing for dynamic groups. **ACNS 2015** [Google Scholar](https://scholar.google.com/scholar?q=Communication-optimal+proactive+secret+sharing+for+dynamic+groups)

[45] Kate 等. Constant-size commitments to polynomials and their applications. **ASIACRYPT 2010** [Google Scholar](https://scholar.google.com/scholar?q=Constant-size+commitments+to+polynomials+and+their+applications)

[24] Desmedt 和 Jajodia. Redistributing secret shares to new access structures and its applications. **Technical Report 1997** [Google Scholar](https://scholar.google.com/scholar?q=Redistributing+secret+shares+to+new+access+structures+and+its+applications)

[32] Frankel 等. Optimal-resilience proactive public-key cryptosystems. **FOCS 1997** [Google Scholar](https://scholar.google.com/scholar?q=Optimal-resilience+proactive+public-key+cryptosystems)

[17] Cachin 等. Asynchronous verifiable secret sharing and proactive cryptosystems. **ACM CCS 2002** [Google Scholar](https://scholar.google.com/scholar?q=Asynchronous+verifiable+secret+sharing+and+proactive+cryptosystems)

[71] Wong 等. Verifiable secret redistribution for archive systems. **1st Security in Storage Workshop 2002** [Google Scholar](https://scholar.google.com/scholar?q=Verifiable+secret+redistribution+for+archive+systems)

[73] Zhou 等. APSS: Proactive secret sharing in asynchronous systems. **ACM TISSEC 2005** [Google Scholar](https://scholar.google.com/scholar?q=APSS:+Proactive+secret+sharing+in+asynchronous+systems)

[26] Dolev 等. Swarming secrets. **2009** [Google Scholar](https://scholar.google.com/scholar?q=Swarming+secrets)


## 关键词

+ 秘密共享
+ 动态委员会
+ 主动安全
+ 区块链
+ 密钥共享