---
title: "Oblivious accumulators"
标题简称:
论文类型: conference
会议简称: PKC
发表年份: 2024
created: 2025-04-16 10:08:43
modified: 2025-04-16 10:11:47
---

## Oblivious accumulators

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-57722-2_4)

## 作者

+ [Foteini Baldimtsi](Foteini%20Baldimtsi.md)
+ [Ioanna Karantaidou](Ioanna%20Karantaidou.md)
+ Srinivasan Raghuraman 

## 笔记

### 背景与动机
动态密码学累积器提供集合的紧凑摘要，并支持高效的成员关系证明。然而，在标准定义下，累积器并不提供隐私保护：累积器摘要、成员关系证明，尤其是一系列更新消息，会泄露累积集合中的元素信息乃至集合的大小。在匿名凭证撤销、智能合约等应用中，参与者希望隐藏凭证的具体内容及客户群规模。现有工作通过零知识证明或模块化构造实现了元素隐藏或加入-撤销不可链接性，但尚未有方案能同时隐藏集合的元素和大小，即实现完全的无感知（oblivious）特性。本文旨在填补这一空白，首次定义并构造了“无感知累积器”，使得外部观察者、验证者，甚至其他元素持有者都无法从公开信息中获取累积集合的元素和大小。

### 相关工作

[5] Baldimtsi et al. Accumulators with Applications to Anonymity-Preserving Revocation. **IEEE EuroS&P 2017** [Google Scholar](https://scholar.google.com/scholar?q=Accumulators+with+Applications+to+Anonymity-Preserving+Revocation)
> 核心思路：在管理者参与的匿名撤销场景中引入了“加入-撤销不可链接性”。
> 局限与区别：该工作未将不可链接性定义为累积器本身的性质，也未考虑隐藏集合大小；本文将其推广为 trapdoorless 累积器下的“加入-删除不可链接性”并作为中间隐私目标。

[29] Miers et al. Zerocoin: Anonymous Distributed E-Cash from Bitcoin. **IEEE S&P 2013** [Google Scholar](https://scholar.google.com/scholar?q=Zerocoin:+Anonymous+Distributed+E-Cash+from+Bitcoin)
> 核心思路：使用两个集合（有效币集和已花费币集）实现隐私保护加密货币。
> 局限与区别：该方案本质上是一个 almost-oblivious 累积器，无法隐藏集合大小，且更新消息泄露操作类型；本文追求更强的“加入-删除不可区分性”以隐藏大小。

[2] Agrawal and Raghuraman. KVaC: Key-Value Commitments for Blockchains and Beyond. **ASIACRYPT 2020** [Google Scholar](https://scholar.google.com/scholar?q=KVaC:+Key-Value+Commitments+for+Blockchains+and+Beyond)
> 核心思路：构造了基于 RSA 假设的键值承诺（KVC），支持键的成员关系和非成员关系证明。
> 局限与区别：该文未考虑将 KVC 用于构造隐藏操作类型的累积器；本文将 KVC 作为核心原语来构造 oblivious accumulator。

[10] Camacho and Hevia. On the Impossibility of Batch Update for Cryptographic Accumulators. **LATINCRYPT 2010** [Google Scholar](https://scholar.google.com/scholar?q=On+the+Impossibility+of+Batch+Update+for+Cryptographic+Accumulators)
> 核心思路：证明了动态累积器中更新消息大小必须随删除次数线性增长的下界。
> 局限与区别：该下界仅针对删除操作；本文利用 obliviousness 性质将该下界推广到所有操作，并证明 almost-oblivious 累积器的下界取决于删除空间的对数。

[19] Christ and Bonneau. Limits on Revocable Proof Systems, with Applications to Stateless Blockchains. **ePrint 2022** [Google Scholar](https://scholar.google.com/scholar?q=Limits+on+Revocable+Proof+Systems,+with+Applications+to+Stateless+Blockchains)
> 核心思路：证明了可撤销证明系统中通信开销的下界。
> 局限与区别：本文采用类似信息论论证，但专门针对 oblivious 累积器的隐私性质进行适配和推广。

[6] Barić and Pfitzmann. Collision-Free Accumulators and Fail-Stop Signature Schemes without Trees. **EUROCRYPT 1997** [Google Scholar](https://scholar.google.com/scholar?q=Collision-Free+Accumulators+and+Fail-Stop+Signature+Schemes+without+Trees)
> 核心思路：首次形式化定义了密码学累积器。
> 局限与区别：该方案无隐私保护性质；本文在其定义基础上引入 obliviousness 性质。

[16] Catalano and Fiore. Vector Commitments and Their Applications. **PKC 2013** [Google Scholar](https://scholar.google.com/scholar?q=Vector+Commitments+and+Their+Applications)
> 核心思路：定义了向量承诺（VC）并给出构造，支持对指定位置的打开。
> 局限与区别：VC 需要初始化时确定向量长度；本文在构造 KVC 时利用了支持 Extend 操作的 VC 以动态增长长度。

### 核心技术与方案

本文的核心是构建一个 trapdoorless、positive、dynamic 的 oblivious accumulator，其关键思想是使用单一的键值承诺（KVC）数据结构，将添加和删除操作均编码为 KVC 的插入操作，但使用由不同哈希函数导出的不同键，从而隐藏操作类型。

具体构造如下：公共参数包含两个随机预言机 $H_1, H_2: \{0,1\}^\lambda \times \mathcal{D} \to \mathcal{K}$。累积器摘要即为 KVC 的承诺 $C$。当用户添加元素 $x$ 时，随机选取 $r \in \{0,1\}^\lambda$，计算键 $k_1 = H_1(r,x)$ 和 $k_2 = H_2(r,x)$。然后，执行 KVC.Insert 在键 $k_1$ 处插入值 $1$，并生成一个 KVC 的非成员关系证明，证明键 $k_2$ 尚未被插入。成员关系证明 $w_x$ 由 $k_1$ 的打开证明和 $k_2$ 的非成员关系证明组成，辅助信息 $\text{aux} = r$。当用户删除 $x$ 时，使用 $\text{aux} = r$ 重新计算 $k_2 = H_2(r,x)$，并执行 KVC.Insert 在键 $k_2$ 处插入值 $1$。验证时，对于元素 $x$，验证者使用 $r$ 计算 $k_1, k_2$，然后验证 $k_1$ 处存在值 $1$ 且 $k_2$ 处未被插入。

安全性论证方面：正确性直接由 KVC 正确性保证。弱（强）可靠性归约到 KVC 的弱（强）密钥绑定性质，同时依赖随机预言机无碰撞的性质。元素隐藏性成立，因为 $r$ 随机且 $H_1, H_2$ 为随机预言机，故攻击者无法区分 $(k_1, k_2)$ 对应的元素。加入-删除不可区分性成立，因为添加操作在 $H_1(r,x)$ 处插入，删除操作在 $H_2(r,x)$ 处插入，而 $H_1(r,x)$ 和 $H_2(r,x)$ 在随机预言机模型下分布完全相同，因此两个操作的公开信息（KVC 的更新消息）在计算上不可区分。

复杂度方面：摘要大小 $|C|$ 和更新消息大小 $|u|$ 均与 KVC 实现相关，通常为常数或对数大小。成员关系证明大小也为常数或对数大小。下界分析（Sect. 6）表明，对于任意 oblivious accumulator，$|C| + |U| = \Omega(n)$，其中 $n$ 是操作序列长度，因此本文构造在该意义下达到最优。

### 核心公式与流程

**[Setup]**
$$(\mathsf{pp}, C) \leftarrow_{\!\!\!\$} \mathsf{Setup}(1^\lambda)$$
运行 $(\mathsf{pp}_\text{KVC}, C_\text{KVC}) \leftarrow_{\!\!\!\$} \mathsf{KVC.Setup}(1^\lambda)$，输出 $\mathsf{pp} = (\mathsf{pp}_\text{KVC}, H_1, H_2)$，$C = C_\text{KVC}$。
> 作用：生成系统公共参数和初始空累积器摘要。

**[Add]**
$$(C', w_x, u, \mathsf{aux}) \leftarrow_{\!\!\!\$} \mathsf{Add}(C, x, U)$$
1. 采样 $r \leftarrow_{\!\!\!\$} \{0,1\}^\lambda$。
2. 计算 $k_1 = H_1(r,x)$, $k_2 = H_2(r,x)$。
3. 运行 $(C_\text{KVC}, \Lambda_{k_1}, u_\text{KVC}) \leftarrow \mathsf{KVC.Insert}(C, (k_1, 1))$。
4. 运行 $\overline{\Lambda}_{k_2} \leftarrow \mathsf{KVC.NonMemProofCreate}(k_2, U \cup \{u_\text{KVC}\})$。
5. 输出 $C' = C_\text{KVC}$，$w_x = (\Lambda_{k_1}, \overline{\Lambda}_{k_2})$，$u = u_\text{KVC}$，$\mathsf{aux} = r$。
> 作用：添加元素 $x$，生成成员证明和辅助信息。添加操作在由 $H_1$ 导出的键处插入值 $1$，并证明由 $H_2$ 导出的键未被插入。

**[Del]**
$$(C', u) \leftarrow \mathsf{Del}(C, x, U, \mathsf{aux})$$
1. 解析 $\mathsf{aux} = r$，计算 $k_2 = H_2(r,x)$。
2. 运行 $(C_\text{KVC}, \Lambda_{k_2}, u_\text{KVC}) \leftarrow \mathsf{KVC.Insert}(C, (k_2, 1))$。
3. 输出 $C' = C_\text{KVC}$，$u = u_\text{KVC}$。
> 作用：删除元素 $x$。删除操作在由 $H_2$ 导出的键处插入值 $1$，使得之前的 $k_2$ 非成员证明失效。

**[MemVer]**
$$b \leftarrow \mathsf{MemVer}(C, x, w_x, \mathsf{aux})$$
1. 解析 $\mathsf{aux}=r$，计算 $k_1 = H_1(r,x), k_2 = H_2(r,x)$。
2. 解析 $w_x = (\Lambda_{k_1}, \overline{\Lambda}_{k_2})$。
3. 运行 $b_1 \leftarrow \mathsf{KVC.Ver}(C, (k_1, 1), \Lambda_{k_1})$。
4. 运行 $b_2 \leftarrow \mathsf{KVC.NonMemVer}(C, k_2, \overline{\Lambda}_{k_2})$。
5. 输出 $b = b_1 \wedge b_2$。
> 作用：验证 $x$ 是否在累积集中。必须同时满足：$H_1(r,x)$ 处有值，且 $H_2(r,x)$ 处未被插入。

**[下界]**
$$|C| + |U| = \Omega(n)$$
> 作用：对于任何 oblivious accumulator，累积器摘要大小与所有更新消息的总大小之和必须随操作数量 $n$ 线性增长，证明通过信息论编码论证。

### 实验结果
本文未提供具体的实验评估，属于理论性工作。文中证明了构造的正确性、可靠性和 obliviousness 性质，并给出了信息论下界。下界结果表明本文基于 KVC 的构造在通信开销方面达到最优。以及作者在 Sect. 5.5 简要讨论了支持唯一元素积累的扩展，但未进行性能基准测试。

### 局限性与开放问题
本文的构造依赖随机预言机模型（$H_1, H_2$ 作为随机预言机），在标准模型下能否构造 oblivious accumulator 是一个开放问题。此外，当前的 oblivious accumulator 构造需要辅助信息 $\text{aux} = r$ 来生成和验证证明，这带来了状态管理的负担；设计无需辅助信息（或无状态验证）的 oblivious accumulator 是一个潜在方向。

### 强关联论文

[5] Baldimtsi et al. Accumulators with Applications to Anonymity-Preserving Revocation. **IEEE EuroS&P 2017** [Google Scholar](https://scholar.google.com/scholar?q=Accumulators+with+Applications+to+Anonymity-Preserving+Revocation)

[2] Agrawal and Raghuraman. KVaC: Key-Value Commitments for Blockchains and Beyond. **ASIACRYPT 2020** [Google Scholar](https://scholar.google.com/scholar?q=KVaC:+Key-Value+Commitments+for+Blockchains+and+Beyond)

[10] Camacho and Hevia. On the Impossibility of Batch Update for Cryptographic Accumulators. **LATINCRYPT 2010** [Google Scholar](https://scholar.google.com/scholar?q=On+the+Impossibility+of+Batch+Update+for+Cryptographic+Accumulators)

[19] Christ and Bonneau. Limits on Revocable Proof Systems, with Applications to Stateless Blockchains. **ePrint 2022** [Google Scholar](https://scholar.google.com/scholar?q=Limits+on+Revocable+Proof+Systems,+with+Applications+to+Stateless+Blockchains)

[29] Miers et al. Zerocoin: Anonymous Distributed E-Cash from Bitcoin. **IEEE S&P 2013** [Google Scholar](https://scholar.google.com/scholar?q=Zerocoin:+Anonymous+Distributed+E-Cash+from+Bitcoin)

[6] Barić and Pfitzmann. Collision-Free Accumulators and Fail-Stop Signature Schemes without Trees. **EUROCRYPT 1997** [Google Scholar](https://scholar.google.com/scholar?q=Collision-Free+Accumulators+and+Fail-Stop+Signature+Schemes+without+Trees)

[16] Catalano and Fiore. Vector Commitments and Their Applications. **PKC 2013** [Google Scholar](https://scholar.google.com/scholar?q=Vector+Commitments+and+Their+Applications)


## 关键词

+ 无知累加器
+ 集合承诺
+ 元素隐藏
+ 键值承诺
+ 去中心化累加器
+ 隐私保护集合操作