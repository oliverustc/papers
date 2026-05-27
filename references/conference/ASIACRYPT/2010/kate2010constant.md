---
title: "Constant-size commitments to polynomials and their applications"
doi: 10.1007/978-3-642-17373-8_11
标题简称:
论文类型: conference
会议简称: ASIACRYPT
发表年份: 2010
modified: 2025-04-13 17:44:41
---
## Constant-size commitments to polynomials and their applications

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-642-17373-8_11)

## 作者

+ [Aniket Kate](Aniket%20Kate.md)
+ Gregory M Zaverucha 
+ Ian Goldberg 

## 笔记

### 背景与动机
承诺方案是密码协议的基础组件，但传统承诺方案在承诺多项式时存在效率瓶颈：若直接承诺多项式系数，则承诺规模与多项式次数t呈线性关系（即t+1个群元素），这在需要打开单个求值而非整个多项式的场景（如可验证秘密共享）中造成巨大的通信开销。本文试图填补多项式承诺方案的形式化定义空白，并构造出承诺与打开均为常数规模（单个群元素）的高效方案，从而将可验证秘密共享、零知识集合、凭证系统等协议中的广播/通信复杂度从线性降低到常数。区别于Merkle哈希树（打开代价O(log n)）和现有向量承诺方案（如Catalano等[12]和Libert-Yung[25]依赖固定索引或需全部打开），本文方案支持任意索引且可通过批量打开进一步降低通信。

### 相关工作

[3] Benaloh等. One-way accumulators: A decentralized alternative to digital signatures. **EUROCRYPT 1993** [Google Scholar](https://scholar.google.com/scholar?q=One-way+accumulators+A+decentralized+alternative+to+digital+signatures)
> 核心思路：聚合大量集合元素为单个值，提供成员关系证据。
> 局限与区别：不支持非成员证明，且元素无序，无法直接用于多项式承诺；本文方案支持有序多项式的承诺与批量求值打开。

[12] Catalano等. Zero-knowledge sets with short proofs. **EUROCRYPT 2008** [Google Scholar](https://scholar.google.com/scholar?q=Zero-knowledge+sets+with+short+proofs)
> 核心思路：构造陷门t-水银承诺实现零知识集合。
> 局限与区别：打开时必须揭示所有消息，不支持按索引打开单个值；本文方案支持任意索引的单个求值打开且承诺规模常数。

[25] Libert, Yung. Concise Mercurial Vector Commitments and Independent Zero-Knowledge Sets with Short Proofs. **TCC 2010** [Google Scholar](https://scholar.google.com/scholar?q=Concise+Mercurial+Vector+Commitments+and+Independent+Zero-Knowledge+Sets+with+Short+Proofs)
> 核心思路：允许打开单个消息，但索引固定为系统参数中g^{α^j}的j∈[1,t]。
> 局限与区别：索引域受限，本文方案索引可为任意Z_p中的元素，灵活性更高。

[26] Menezes等. Handbook of Applied Cryptography. **CRC Press 1997** [Google Scholar](https://scholar.google.com/scholar?q=Handbook+of+Applied+Cryptography)
> 核心思路：离散对数假设与Merkle树。
> 局限与区别：Merkle树打开大小为O(log n)，本文方案为O(1)。

[29] Nguyen. Accumulators from bilinear pairings and applications. **CT-RSA 2005** [Google Scholar](https://scholar.google.com/scholar?q=Accumulators+from+bilinear+pairings+and+applications)
> 核心思路：基于双线性配对的累加器，支持成员证明。
> 局限与区别：不提供隐藏性和批量打开；本文方案提供隐藏性且支持批量打开。

[31] Pedersen. Non-Interactive and Information-Theoretic Secure Verifiable Secret Sharing. **CRYPTO 1991** [Google Scholar](https://scholar.google.com/scholar?q=Non-Interactive+and+Information-Theoretic+Secure+Verifiable+Secret+Sharing)
> 核心思路：Pedersen承诺，实现无条件隐藏和计算绑定。
> 局限与区别：承诺多项式时需t+1个元素；本文方案承诺规模为常数。

[35] Steinfeld等. Content extraction signatures. **ICISC 2001** [Google Scholar](https://scholar.google.com/scholar?q=Content+extraction+signatures)
> 核心思路：内容提取签名通用构造，依赖标准承诺。
> 局限与区别：现有构造需为每个子消息分别承诺，通信复杂度为O(t)；本文方案通过多项式承诺实现O(1)或O(k)的开销。

### 核心技术与方案

本文提出多项式承诺方案的形式化定义，包括Setup、Commit、Open、VerifyPoly、CreateWitness、VerifyEval六个算法，并定义正确性、多项式绑定、求值绑定和隐藏性。核心构造基于代数性质：对于多项式φ(x)∈Z_p[x]和任意i，有(x−i)整除φ(x)−φ(i)。基于该性质，两个具体方案如下。

**PolyCommit_DL方案**：Setup生成双线性群G、GT，选择随机α∈Z_p^∗，输出PK = ⟨G, g, g^α, …, g^{α^t}⟩。Commit计算C = g^{φ(α)}，即常数规模的单元素承诺。CreateWitness计算ψ_i(x) = (φ(x)−φ(i))/(x−i)，输出w_i = g^{ψ_i(α)}。VerifyEval验证e(C, g) = e(w_i, g^α/g^i)·e(g, g)^{φ(i)}。正确性由双线性性及φ(α)=ψ_i(α)(α−i)+φ(i)保证。安全证明：绑定性基于t-SDH假设，隐藏性基于DL假设。当t′ < deg(φ)个求值已打开时，方案无条件隐藏未打开值（因⟨α, φ(α)⟩以指数形式存在，不足以插值）。

**PolyCommit_Ped方案**：添加随机多项式φ̂(x)实现无条件隐藏。PK额外包含h, h^α, …, h^{α^t}。Commit计算C = g^{φ(α)}h^{φ̂(α)}。CreateWitness计算w_i = g^{ψ_i(α)}h^{ψ̂_i(α)}，其中ψ̂_i(x)=(φ̂(x)−φ̂(i))/(x−i)。VerifyEval验证e(C, g) = e(w_i, g^α/g^i)·e(g^{φ(i)}h^{φ̂(i)}, g)。绑定性仍基于t-SDH，隐藏性无条件。

**批量打开**：对于集合B⊂Z_p，计算w_B = g^{ψ_B(α)}，其中ψ_B(x) = (φ(x)−r(x))/∏_{i∈B}(x−i)，r(x)为余式满足φ(i)=r(i)。验证e(C, g) = e(g^{∏_{i∈B}(α−i)}, w_B)·e(g, g^{r(α)})且deg r(x)=|B|。批量打开的绑定性基于t-BSDH假设。

**强正确性**：要求无法承诺次数大于t的多项式，依赖t-polyDH假设。

渐进复杂度：承诺为单元素（常数），单个求值打开传输一个群元素（常数），批量打开|B|个求值时通信仅为单元素加余式（|B|个值），计算量通过多指数加速为O(t)次幂。

### 核心公式与流程

**PolyCommit_DL的验证公式**
$$e(\mathcal{C}, g) = e(w_i, g^{\alpha}/g^{i}) \cdot e(g, g)^{\phi(i)}$$
> 作用：验证求值φ(i)与承诺C的一致性。正确性由双线性性及φ(α)=ψ_i(α)(α−i)+φ(i)导出。

**PolyCommit_Ped的验证公式**
$$e(\mathcal{C}, g) = e(w_i, g^{\alpha}/g^{i}) \cdot e(g^{\phi(i)} h^{\hat{\phi}(i)}, g)$$
> 作用：验证带随机化多项式的承诺求值，实现无条件隐藏。

**批量打开验证公式**
$$e(\mathcal{C}, g) = e(g^{\prod_{i\in B}(\alpha - i)}, w_B) \cdot e(g, g^{r(\alpha)})$$
> 作用：一次性验证多个求值，要求deg r(x)=|B|且r(i)=φ(i) for all i∈B，通信开销常数加余式。

**强正确性游戏**
对手创建承诺C后，挑战者发送t′+1个索引，对手返回对应求值及证据。若插值得到的多项式次数小于t，则对手获胜。该性质依赖t-polyDH假设。

### 实验结果
本文未提供具体实验数据（理论性论文），但给出了通信复杂度的理论对比：与Merkle树（打开O(log n)）和矢量承诺（Catalano等[12]打开O(t)，Libert-Yung[25]打开单元素但索引受限）相比，PolyCommit_DL的承诺和打开均为常数（单群元素），批量打开时传输常数加余式。在参数选择上，系统参数规模为O(t)（t+1个群元素），与t-SDH假设中的t一致。在计算开销方面，Commit和CreateWitness需O(t)次指数运算（可通过多指数加速），VerifyEval需2个配对运算（其中e(g,g)可预计算）。在应用中，eVSS方案将广播通信从O(n)降为O(1)；近零知识集合的成员/非成员证明大小分别为2个群元素和约5个群元素，较Libert-Yung[25]的80–220个群元素降低至少16倍。

### 局限性与开放问题
本文方案依赖t-SDH等强假设，能否在更弱假设下构造是开放问题。系统参数规模为O(t)，虽不影响通信但会增加存储和首次计算开销。目前主要关注通信成本，计算成本虽可并行化但仍为O(t)次指数运算，进一步降低计算量是未来方向。另外，本文未涉及异步网络环境下的VSS协议优化，以及可验证混洗等其他应用的适用性。

### 强关联论文

[6] Boneh, Boyen. Short Signatures Without Random Oracles. **EUROCRYPT 2004** [Google Scholar](https://scholar.google.com/scholar?q=Short+Signatures+Without+Random+Oracles)

[12] Catalano, Fiore, Messina. Zero-knowledge sets with short proofs. **EUROCRYPT 2008** [Google Scholar](https://scholar.google.com/scholar?q=Zero-knowledge+sets+with+short+proofs)

[25] Libert, Yung. Concise Mercurial Vector Commitments and Independent Zero-Knowledge Sets with Short Proofs. **TCC 2010** [Google Scholar](https://scholar.google.com/scholar?q=Concise+Mercurial+Vector+Commitments+and+Independent+Zero-Knowledge+Sets+with+Short+Proofs)

[18] Feldman. A Practical Scheme for Non-interactive Verifiable Secret Sharing. **FOCS 1987** [Google Scholar](https://scholar.google.com/scholar?q=A+Practical+Scheme+for+Non-interactive+Verifiable+Secret+Sharing)

[31] Pedersen. Non-Interactive and Information-Theoretic Secure Verifiable Secret Sharing. **CRYPTO 1991** [Google Scholar](https://scholar.google.com/scholar?q=Non-Interactive+and+Information-Theoretic+Secure+Verifiable+Secret+Sharing)

[27] Micali, Rabin, Kilian. Zero-knowledge sets. **FOCS 2003** [Google Scholar](https://scholar.google.com/scholar?q=Zero-knowledge+sets)

[35] Steinfeld, Bull, Zheng. Content extraction signatures. **ICISC 2001** [Google Scholar](https://scholar.google.com/scholar?q=Content+extraction+signatures)

[26] Menezes, Van Oorschot, Vanstone. Handbook of Applied Cryptography. **CRC Press 1997** [Google Scholar](https://scholar.google.com/scholar?q=Handbook+of+Applied+Cryptography)

[29] Nguyen. Accumulators from bilinear pairings and applications. **CT-RSA 2005** [Google Scholar](https://scholar.google.com/scholar?q=Accumulators+from+bilinear+pairings+and+applications)

[3] Benaloh, de Mare. One-way accumulators: A decentralized alternative to digital signatures. **EUROCRYPT 1993** [Google Scholar](https://scholar.google.com/scholar?q=One-way+accumulators+A+decentralized+alternative+to+digital+signatures)


## 关键词提炼

1. **多项式承诺方案** - 核心技术创新
2. **常数大小承诺** - 主要性能优势
3. **通信开销优化** - 实际应用价值
4. **可验证秘密共享** - 重要应用领域
5. **零知识密码学** - 技术应用范畴

An extended version of this paper is available [24]. This research