---
title: "An expressive zero-knowledge set accumulator"
标题简称:
论文类型: conference
会议简称: EuroS&P
发表年份: 2017
modified: 2025-04-13 13:51:10
---

## An expressive zero-knowledge set accumulator

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/7961978)

## 作者

+ [Yupeng Zhang](Yupeng%20Zhang.md) 
+ [Jonathan Katz](Jonathan%20Katz.md) 
+ [Charalampos Papamanthou](Charalampos%20Papamanthou.md) 

## 笔记

### 背景与动机
数据外包至云服务器已成为常态，但如何确保外包数据上操作的正确性（如集合查询）是核心挑战。现有加密累加器（如RSA累加器 [7] 和双线性累加器 [34, 38]）仅支持成员资格、非成员资格及基本集合运算，无法高效支持嵌套查询及函数（SUM、COUNT、MIN、MAX、RANGE）；公开更新需线性或准线性时间 [7, 34]；且缺乏零知识性质。本文旨在填补这一空白：构造首个同时具备表达性（支持集合运算、函数、嵌套查询及零知识）、效率（证明大小与查询深度和结果规模成正比、更新常数复杂度）、公开可验证/可更新性的加密累加器。

### 相关工作

[7] Benaloh et al. One-way accumulators: A decentralized alternative to digital signatures. **EUROCRYPT 1993**  
> 核心思路：提出RSA累加器，支持常数大小成员资格证明。  
> 局限与区别：不支持集合运算、函数、嵌套查询且更新需陷门（拥有者才可高效更新）。

[2] Baric et al. Collision-free accumulators and fail-stop signature schemes without trees. **EUROCRYPT 1997**  
> 核心思路：改进RSA累加器，抗碰撞。  
> 局限与区别：同样不支持集合运算和公开高效更新。

[18] Camenisch et al. Dynamic accumulators and application to efficient revocation of anonymous credentials. **CRYPTO 2002**  
> 核心思路：将RSA累加器扩展到动态场景并增加零知识。  
> 局限与区别：仍不支持集合运算和嵌套查询，零知识只限于成员资格。

[34] Nguyen. Accumulators from bilinear pairings and applications. **CT-RSA 2005**  
> 核心思路：提出双线性累加器，支持成员资格证明。  
> 局限与区别：仅支持成员资格，更新需准线性时间，不支持函数和嵌套查询。

[38] Papamanthou et al. Optimal verification of operations on dynamic sets. **CRYPTO 2011**  
> 核心思路：基于双线性累加器，支持交集、并集、差集，证明大小和验证时间与结果规模成正比。  
> 局限与区别：不支持函数（SUM/COUNT/MIN/MAX/RANGE）及嵌套查询，更新仍需准线性时间。

[19] Canetti et al. Verifiable set operations over outsourced databases. **PKC 2014**  
> 核心思路：基于可提取性假设，支持嵌套的集合运算（∩、∪、\）。  
> 局限与区别：不支持函数（SUM等）且更新复杂。

[45] Zhang et al. IntegriDB: Verifiable SQL for outsourced databases. **CCS 2015**  
> 核心思路：将双线性累加器用于SQL查询，支持SUM等，但不支持MIN/MAX/RANGE嵌套。  
> 局限与区别：不能支持嵌套查询中的函数，更新需陷门，复杂度准线性。

[25] Ghosh et al. Zero-knowledge accumulators and set operations. **ePrint 2015**  
> 核心思路：提出零知识集合操作累加器，prover线性时间。  
> 局限与区别：不支持嵌套操作，表达能力不如本文。

[27] Groth. Short pairing-based non-interactive zero-knowledge arguments. **ASIACRYPT 2010**  
> 核心思路：提出向量内积的NIZK参数，可用于集合操作。  
> 局限与区别：不支持嵌套查询和函数，prover时间复杂度高。

[31] Lipmaa. Progression-free sets and sublinear pairing-based non-interactive zero-knowledge arguments. **TCC 2012**  
> 核心思路：改进[27]至准线性时间，支持嵌套查询。  
> 局限与区别：仍不支持SUM/COUNT/MIN/MAX/RANGE函数。

### 核心技术与方案

**整体框架**：本文基于双线性群构造累加器，将集合 $\mathcal{A}$ 映射为两个多项式：$\mathcal{A}(s)=\sum_{i\in\mathcal{A}} s^i$ 及 $\mathcal{A}(r,s)=\sum_{i\in\mathcal{A}} r^i s^{q-i}$（$s,r$ 为秘密随机数）。累加器值包括四个群元素：$\mathcal{A}_s=g^{\mathcal{A}(s)},\ \mathcal{A}_{s,r}=g^{\mathcal{A}(r,s)},\ \mathcal{A}_r=g^{\mathcal{A}(r)},\ \mathcal{A}_{r,s}=g^{\mathcal{A}(s,r)}$。

**关键构造思路**：  
- 交集：利用 $\mathcal{A}_s \times \mathcal{B}_{r,s}$ 展开后 $s^q$ 项的系数恰为 $\sum_{i\in\mathcal{A}\cap\mathcal{B}} r^i$。服务器返回结果 $\mathcal{I}= \mathcal{A}\cap\mathcal{B}$ 及证明 $g^{q(s,r)}$，客户端通过配对检查等式。  
- 其他集合运算（并、差、对称差、补）可通过交集及已有累加值推导。  
- COUNT：多项式求值 $\mathcal{A}(1)$，用 $\mathcal{A}(s)-\mathcal{A}(1)=(s-1)a(s)$ 给出证明。  
- SUM：利用导数 $\mathcal{A}'(1)$，证明基于 $\mathcal{A}(s)-\mathcal{A}(1)-\mathcal{A}'(1)(s-1)=(s-1)^2 b(s)$。  
- MIN：返回最低次项 $s^{\min}$，证明为 $g^{(\mathcal{A}(s)-s^{\min})/s^{\min+1}}$。  
- MAX：对称处理 $\mathcal{A}_{r,s}$。  
- RANGE：将集合分解为小于 $l$、区间、大于 $r$ 三部分，分别证明它们互斥且覆盖原集，再通过MIN/MAX验证边界。  
- 嵌套查询：不直接返回中间结果，而是返回其累加器值，客户端验证该累加器正确性后继续上层操作。

**零知识扩展**：在累加器每一项指数上添加随机化项（如 $r_1 t s^{\min+1}$），并使用额外的秘密参数 $t$ 和随机数 $r_i$ 遮盖真实多项式。证明时引入随机化，保证模拟器可生成与真实分布不可区分的视图。

**安全性**：  
- 正确性通过代数运算直接成立。  
- 可靠性依赖三个假设：q-SBDH（假设1）、双变量可提取性假设（假设2）、BDHE变体（假设3）。证明策略为：假设恶意服务器通过验证但答案错误，则可通过可提取性获得系数，然后利用配对等式导出矛盾，最终归结到已知困难问题。

**复杂度**：  
- 证明大小 $O(d)$（$d$ 为嵌套查询深度）。  
- 验证时间 $O(d+|\mathcal{R}|)$（$|\mathcal{R}|$ 为最终结果规模）。  
- Prover 时间 $O(n^2)$（$n$ 为集合最大规模），主要来自稀疏多项式乘法。  
- 更新（插入/删除）时间 $O(1)$（仅需乘/除群元素）。  
- 公钥大小 $O(q^2)$（$q$ 为全集大小）。

### 核心公式与流程

**[累积值定义]**  
$$ \mathcal{A}_s = g^{\mathcal{A}(s)} = g^{\sum_{i\in\mathcal{A}} s^i},\quad \mathcal{A}_{r,s} = g^{\mathcal{A}(r,s)} = g^{\sum_{i\in\mathcal{A}} r^i s^{q-i}}. $$  
> 作用：定义集合 $\mathcal{A}$ 的累加器，支持后续所有操作。

**[交集验证]**  
$$ e(\mathcal{A}_s, \mathcal{B}_{r,s}) = e(g^{\sum_{i\in\mathcal{I}} r^i}, g^{s^q}) \cdot e(g^{q(s,r)}, g). $$  
> 作用：客户端通过该等式验证交集 $\mathcal{I}=\mathcal{A}\cap\mathcal{B}$ 的正确性。其中 $q(s,r)$ 为不含 $s^q$ 项的证明多项式。

**[COUNT验证]**  
$$ e(\mathcal{A}_s / g^{v}, g) = e(g^{s-1}, \pi), $$  
其中 $v$ 为声称的计数值，$\pi = g^{a(s)}$ 且 $a(s) = (\mathcal{A}(s)-\mathcal{A}(1))/(s-1)$。  
> 作用：验证集合大小的正确性。

**[SUM验证]**  
$$ e(\mathcal{A}_s, g) = e(g^{(s-1)^2}, \pi_1) \cdot e(g^{v(s-1)+\pi_2}, g), $$  
其中 $\pi_1 = g^{b(s)},\ b(s)=(\mathcal{A}(s)-\mathcal{A}(1)-\mathcal{A}'(1)(s-1))/(s-1)^2$，$\pi_2 = \mathcal{A}(1)$。  
> 作用：验证集合元素和。

**[MIN验证]**  
$$ e(\mathcal{A}_s, g) = e(g^{s^{v}}, g) \cdot e(\pi, g^{s^{v+1}}), $$  
其中 $v$ 为声称的最小值，$\pi = g^{(\mathcal{A}(s)-s^{v})/s^{v+1}}$。  
> 作用：验证集合最小值。

### 实验结果

论文在 ate-pairing 库上实现，并在 3.40 GHz Intel Core i7-4770 CPU、32 GB RAM 的机器上对比 ESA 与 RAM-based SNARKs for C [6]。  

测试查询为 SUM( (A∩B) ∪ (C∩D) )，各集合大小 $n$ 分别为 1,000、10,000、5×10⁶。  

- 当 $n=1,000$ 时，ESA 设置时间 0.01s 对比 [6] 的 9,000s；prover 时间 3.6s 对比 4,300s；验证时间 9ms 对比 19ms；证明大小 540B 对比 288B；更新时间 2.4×10⁻⁶s（[6] 不支持高效更新）。  
- 当 $n=10,000$ 时，ESA 设置时间 0.1s；prover 时间 360s（[6] 为 43,000s）；验证时间 9ms；证明大小 540B；更新时间不变。  
- 当 $n=5×10⁶$ 时，ESA 设置时间 5s；prover 时间 9×10⁷s，超过了 [6] 的 2.15×10⁷s。  

可见，当 $n \lesssim 5×10^6$ 时，ESA 在设置、验证、更新方面显著优于通用方案，但 prover 时间最终被超越。论文还指出，ESA 的群乘法操作（0.6μs）和配对操作（0.3ms）极快，且不使用幂运算（指数系数全为1）。

### 局限性与开放问题

1. Prover 时间 $O(n^2)$ 是主要瓶颈，对于超大集合（>5M）不如 RAM-based SNARKs。如何设计线性或准线性时间的 prover 仍是开放问题。  
2. 零知识嵌套查询中的并集操作需要额外协议（通过两个交集验证），增加了复杂度和证明大小。简化该部分值得探索。  
3. 更新公开性虽然 $O(1)$，但需客户端拥有正确的最新累加值，抗恶意客户端攻击的机制未完全讨论（如重放或乱序更新）。

### 强关联论文

[7] Benaloh et al. One-way accumulators: A decentralized alternative to digital signatures. **EUROCRYPT 1993**  
[2] Baric et al. Collision-free accumulators and fail-stop signature schemes without trees. **EUROCRYPT 1997**  
[18] Camenisch et al. Dynamic accumulators and application to efficient revocation of anonymous credentials. **CRYPTO 2002**  
[34] Nguyen. Accumulators from bilinear pairings and applications. **CT-RSA 2005**  
[38] Papamanthou et al. Optimal verification of operations on dynamic sets. **CRYPTO 2011**  
[19] Canetti et al. Verifiable set operations over outsourced databases. **PKC 2014**  
[45] Zhang et al. IntegriDB: Verifiable SQL for outsourced databases. **CCS 2015**  
[25] Ghosh et al. Zero-knowledge accumulators and set operations. **ePrint 2015**  
[27] Groth. Short pairing-based non-interactive zero-knowledge arguments. **ASIACRYPT 2010**  
[31] Lipmaa. Progression-free sets and sublinear pairing-based non-interactive zero-knowledge arguments. **TCC 2012**


## 关键词

+ 零知识集合累加器
+ 集合运算证明
+ 可提取性假设
+ 通用群模型
+ 可验证数据库
+ 简洁证明