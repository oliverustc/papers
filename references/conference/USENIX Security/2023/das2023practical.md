---
title: "Practical asynchronous high-threshold distributed key generation and distributed polynomial sampling"
标题简称:
论文类型: conference
会议简称: USENIX Security
发表年份: 2023
modified: 2025-04-13 16:44:05
---

## Practical asynchronous high-threshold distributed key generation and distributed polynomial sampling

## 发表信息

+ [原文链接](https://www.usenix.org/conference/usenixsecurity23/presentation/das)

## 作者

+ [Sourav Das](Sourav%20Das.md)
+ [Zhuolun Xiang](Zhuolun%20Xiang.md)
+ Lefteris Kokoris-Kogias 
+ [Ling Ren](Ling%20Ren.md)
## 笔记

### 背景与动机

分布式密钥生成（DKG）是启动门限密码系统（如门限签名、门限加密、公共硬币）的核心构建模块，其目标是在互不信任的节点间分布式地生成公私钥对，使得每个节点持有私钥的一份秘密分享，并公开公钥。在异步网络环境中，现有异步 DKG（ADKG）协议在高重建门限（即重建秘密所需的节点数远大于容忍的恶意节点数）时效率极低。例如，Das 等人 [22] 的高门限 ADKG 比其低门限版本慢 500 倍以上，通信量高 6 倍，瓶颈在于高门限异步完全秘密共享（ACSS）的计算开销比低门限 ACSS 高两到三个数量级。此外，许多应用（如 BFT 共识协议 [4,28,33,41,57] 和异步协议中的共享随机性 [12,17,18]）天然需要高重建门限，因此迫切需要一种高效、实用的异步高门限 DKG 方案。本文旨在通过一种全新的分布式多项式采样思路，绕过昂贵的高门限 ACSS，仅使用低门限 ACSS 来采样一个随机的高次多项式，从而将高门限 ADKG 的效率提升到接近于低门限 ADKG 的水平。

### 相关工作

[3] Abraham 等. Reaching consensus for asynchronous distributed key generation. **PODC 2021** [Google Scholar](https://scholar.google.com/scholar?q=Reaching+consensus+for+asynchronous+distributed+key+generation)
> 核心思路：提出首个异步 DKG 协议，基于 PVSS 方案，通信复杂度 O(κn³logn)。
> 局限与区别：其协议将秘密钥作为群元素输出，与现成的门限加密/签名方案不兼容；且未明确支持高重建门限。

[21] Das 等. Asynchronous data dissemination and its applications. **CCS 2021** [Google Scholar](https://scholar.google.com/scholar?q=Asynchronous+data+dissemination+and+its+applications)
> 核心思路：改进了低门限 ACSS 方案，并将其应用于异步数据处理。
> 局限与区别：本文直接使用该低门限 ACSS 作为底层原语，结合分布式多项式采样构建高门限 ADKG，避免了使用高门限 ACSS。

[22] Das 等. Practical asynchronous distributed key generation. **S&P 2022** [Google Scholar](https://scholar.google.com/scholar?q=Practical+asynchronous+distributed+key+generation)
> 核心思路：首个实用的异步 DKG 实现，包括低门限和高门限版本；高门限版本依赖于高门限 ACSS。
> 局限与区别：其高门限 ACSS 计算开销极大（比低门限版本高 500 倍以上），通信开销高 6 倍；本文通过分布式多项式采样彻底规避了高门限 ACSS，使高门限 ADKG 开销与低门限版本几乎相同。

[27] Gao 等. Efficient asynchronous Byzantine agreement without private setups. **ePrint 2021** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+asynchronous+Byzantine+agreement+without+private+setups)
> 核心思路：将 Abraham 等人 [3] 的 ADKG 通信复杂度改进到 O(κn³)。
> 局限与区别：与 [3] 类似，秘密钥是群元素，不支持标准门限密码系统，且未讨论高门限支持。

[39] Kokoris-Kogias 等. Asynchronous distributed key generation for computationally-secure randomness, consensus, and threshold signatures. **CCS 2020** [Google Scholar](https://scholar.google.com/scholar?q=Asynchronous+distributed+key+generation+for+computationally-secure+randomness,+consensus,+and+threshold+signatures)
> 核心思路：第一个异步 DKG 方案，总通信量 O(κn⁴)，轮复杂度 O(n)。
> 局限与区别：通信开销高，轮数线性，且未优化高门限场景。

[58] Yurek 等. hbacss: How to robustly share many secrets. **NDSS 2022** [Google Scholar](https://scholar.google.com/scholar?q=hbacss:+How+to+robustly+share+many+secrets)
> 核心思路：提出一种低门限 ACSS 方案，支持批量秘密共享。
> 局限与区别：本文使用的低门限 ACSS 是基于 [21] 的改进版本，比 [58] 更高效。

### 核心技术与方案

本文的核心洞见在于：高重建门限的 DKG 问题本质上等价于分布式地采样一个随机 $l$ 次多项式（$l$ 为重建门限），使得每个节点只得到该多项式的一个求值点，而秘密钥为 $z(0)$。因此，不需要通过高门限 ACSS 来分享高次多项式，而是可以通过低门限 ACSS（分享 $t$ 次多项式）来秘密分享 $l+1$ 个系数，然后利用这些系数的秘密分享为每个节点计算其在 $l$ 次多项式上的求值点。整个方案分为四个阶段：共享阶段、协议阶段、随机提取阶段和密钥推导阶段。

**共享阶段**：每个节点 $i$ 采样两个随机秘密 $a_i, b_i \in \mathbb{Z}_q$，并使用低门限 ACSS 方案（来自 [21]）将它们秘密分享给所有节点。低门限 ACSS 的 $t$ 次多项式保证即使有 $t$ 个恶意节点，秘密仍保密。节点 $i$ 还输出 Pedersen 承诺 $u_i = g^{a_i}h^{\hat{a}_i}$ 和 $v_i = g^{b_i}h^{\hat{b}_i}$，其中 $\hat{a}_i, \hat{b}_i$ 是承诺随机性。

**协议阶段**：每个节点等待 $n-t$ 个 ACSS 实例本地完成，获得集合 $S_i$，并作为输入运行 Multi-valued Validated Byzantine Agreement（MVBA）协议，最终所有节点输出一个一致的 $T$，$|T| \ge n-t$。$T$ 包含了至少 $n-2t$ 个诚实节点。对于不在 $T$ 中的节点，将其 $a_j, b_j$ 视为 0。

**随机提取阶段**：每个节点 $i$ 持有向量 $\mathbf{a}=[a_1,\dots,a_n]$ 和 $\mathbf{b}=[b_1,\dots,b_n]$ 的 $(n, t+1)$ 阈下秘密分享。利用超可逆矩阵（Vandermonde 矩阵），各节点本地计算 $l+1$ 个系数 $z_0,\dots,z_l$ 的阈下秘密分享。具体地，用 $a$ 向量通过矩阵 $M \in \mathbb{Z}_q^{(t+1)\times n}$（即 $M_{k,j} = \omega_k^{j-1}$，$\omega_k$ 为不同元素）计算 $z_0,\dots,z_t$；用 $b$ 向量通过矩阵 $\tilde{M} \in \mathbb{Z}_q^{(l-t)\times n}$ 计算 $z_{t+1},\dots,z_l$。由于超可逆矩阵的性质，只要输入中有至少 $n-t$ 个均匀随机秘密（来自诚实节点），输出 $l+1$ 个系数就是均匀随机且独立的。然后，每个节点 $i$ 利用其手中的系数秘密分享，本地计算每个节点 $j$ 对应的多项式求值点 $z(j)$ 的秘密分享 $[[z(j)]]_i$（以及对应的 Pedersen 随机性 $\hat{z}(j)$），并将这些值通过私密通道发送给节点 $j$。节点 $j$ 收到至少 $2t+1$ 个分享后，使用在线纠错（OEC）算法恢复出 $z(j)$ 和 $\hat{z}(j)$。OEC 算法是信息论安全的，最多容忍 $t$ 个错误。

**密钥推导阶段**：每个节点 $i$ 广播其 $g^{z(i)}$ 和 $h^{\hat{z}(i)}$，并附上非交互零知识证明（Schnorr 协议）证明其知道 $z(i)$ 和 $\hat{z}(i)$。同时，节点可以利用 ACSS 中公开的承诺 $u_j, v_j$，通过指数上的内积运算得到 $c(j) = g^{z(j)}h^{\hat{z}(j)}$。收到 $\ell+1$ 个通过验证的 KEY 消息后，节点通过指数上的拉格朗日插值计算出公钥 $g^{z(0)}$ 以及所有缺失的阈下公钥 $g^{z(k)}$。

**安全性直觉**：由于随机提取阶段输出的 $l+1$ 个系数是均匀随机的，且每个节点只知道 $l$ 次多项式上的一个点，因此学习到最多 $\ell$ 个节点分享的敌手无法恢复秘密 $z(0)$。安全性证明通过仿真器实现：仿真器从理想功能 $\mathcal{F}_{\mathsf{ADKG}}$ 获得 $g^z$、$g^{[[z]]}$ 以及 $C_1 \cup C_2$ 中节点的份额，然后利用 Pedersen 承诺的完美隐藏特性和 Shamir 秘密共享的完美保密性，将实际协议中的份额和承诺替换为与理想输出一致的模拟值，从而使真实世界与理想世界不可区分。该仿真是直线的（straight-line），不涉及倒带，因此可扩展至 UC 框架。

**复杂度**：期望通信总量 $O(\kappa n^3)$，期望每节点计算量 $O(n^2)$ 群指数运算（最坏情况也是 $O(n^2)$，得益于 §4.6 对 MVBA 的优化），期望轮复杂度 $O(\log n)$。

### 核心公式与流程

**[低门限 ACSS 的 Pedersen 多项式承诺]**
$$
\mathbf{v} = \left[ g^{a_0} h^{\hat{a}_0}, g^{a_1} h^{\hat{a}_1}, \ldots, g^{a_t} h^{\hat{a}_t} \right]
$$
> 作用：用于对 $t$ 次多项式 $a(x)$ 进行可验证的、信息论隐藏的承诺。节点通过检查 $g^{\alpha_i} h^{\beta_i} = \prod_{k=0}^t (\mathbf{v}[k])^{i^k}$ 验证收到的份额 $\alpha_i, \beta_i$ 是否正确。

**[超可逆矩阵随机提取]**
$$
\begin{bmatrix} z_0 \\ z_1 \\ \vdots \\ z_t \end{bmatrix} = 
\begin{bmatrix}
1 & \omega_1 & \dots & \omega_1^{n-1} \\
1 & \omega_2 & \dots & \omega_2^{n-1} \\
\vdots & \vdots & \ddots & \vdots \\
1 & \omega_{t+1} & \dots & \omega_{t+1}^{n-1}
\end{bmatrix}
\begin{bmatrix} a_1 \\ a_2 \\ \vdots \\ a_n \end{bmatrix}
$$
$$
\begin{bmatrix} z_{t+1} \\ z_{t+2} \\ \vdots \\ z_{\ell} \end{bmatrix} = 
\begin{bmatrix}
1 & \omega_1 & \dots & \omega_1^{n-1} \\
1 & \omega_2 & \dots & \omega_2^{n-1} \\
\vdots & \vdots & \ddots & \vdots \\
1 & \omega_{\ell-t} & \dots & \omega_{\ell-t}^{n-1}
\end{bmatrix}
\begin{bmatrix} b_1 \\ b_2 \\ \vdots \\ b_n \end{bmatrix}
$$
> 作用：节点利用各自持有的 $(n, t+1)$ 秘密分享，通过矩阵乘法（在份额上线性运算）得到 $l+1$ 个随机系数的秘密分享。矩阵的超可逆性保证输出均匀随机，只要输入中有至少 $n-t$ 个均匀随机的秘密。

**[多项式求值点的秘密分享传递]**
每个节点 $i$ 计算 $[[z(j)]]_i = \sum_{k=0}^{l} [[z_k]]_i \cdot j^k$，并通过私密信道发送给节点 $j$。
> 作用：节点 $i$ 利用自己手中的系数秘密分享，为每个其他节点 $j$ 计算 $z(j)$ 的秘密分享。节点 $j$ 收集足够多的分享后通过 OEC 恢复 $z(j)$。

**[指数插值计算公钥]**
$$
g^{z(0)} = \prod_{i \in H} g^{z(i)} \cdot \Lambda_i(0) \quad \text{(指数上的拉格朗日插值)}
$$
> 作用：节点从至少 $l+1$ 个经过验证的 KEY 消息中恢复出阈下公钥 $g^{z(0)}$ 以及缺失的其他节点公钥。其中 $H$ 是大小为 $l+1$ 的验证通过集合，$\Lambda_i$ 是拉格朗日基多项式。

### 实验结果

实验在 Amazon EC2 t3a.medium 实例（2 vCPU, 4GB RAM）上进行，节点分布在 8 个全球 AWS 区域，网络拓扑为完全连接图。评估了 16、32、64、128 个节点，重建门限 $l = 2t$（即 $t = \lfloor n/3 \rfloor$）。对比基线为 Das 等人 [22] 的 ADKG 实现（包含低门限和高门限版本）。主要结果：对于 $n=64$，curve25519 曲线，本文高门限 ADKG 平均运行时间 12.48 秒，仅为 [22] 高门限版本（152.56 秒）的 8.2%，同时比 [22] 低门限版本（9.56 秒）仅高 30%；每节点带宽 3.32 MB，仅为 [22] 高门限版本（18.97 MB）的 18%。对于 bls12381 曲线，趋势类似。实验表明，本文方案的计算和通信开销随节点数二次增长，与理论分析一致，且无论 $l$ 取何值（在 $[t, n-t-1]$ 范围内），带宽相同，计算开销影响可忽略。

### 局限性与开放问题

本文的安全证明在独立模型（stand-alone）中完成，但仿真器是直线的（straight-line），作者认为可扩展至 UC 框架，但未给出完整证明。此外，底层低门限 ACSS 和 MVBA 的进一步改进可直接提升 ADKG 性能。分布式多项式采样原语在异步环境下的其他应用（如主动秘密刷新、MPC 预处理）仅作了简要讨论，尚未深入分析安全性或性能权衡。最后，虽然文中提到可支持 $l > n - t$ 的多项式采样，但未详细说明相应的额外开销和安全性保证。

### 强关联论文

[3] Abraham I, Jovanovic P, Maller M, et al. Reaching consensus for asynchronous distributed key generation. **PODC 2021** [Google Scholar](https://scholar.google.com/scholar?q=Reaching+consensus+for+asynchronous+distributed+key+generation)

[21] Das S, Xiang Z, Ren L. Asynchronous data dissemination and its applications. **CCS 2021** [Google Scholar](https://scholar.google.com/scholar?q=Asynchronous+data+dissemination+and+its+applications)

[22] Das S, Yurek T, Xiang Z, et al. Practical asynchronous distributed key generation. **S&P 2022** [Google Scholar](https://scholar.google.com/scholar?q=Practical+asynchronous+distributed+key+generation)

[27] Gao Y, Lu Y, Lu Z, et al. Efficient asynchronous Byzantine agreement without private setups. **ePrint 2021** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+asynchronous+Byzantine+agreement+without+private+setups)

[39] Kokoris-Kogias E, Malkhi D, Spiegelman A. Asynchronous distributed key generation for computationally-secure randomness, consensus, and threshold signatures. **CCS 2020** [Google Scholar](https://scholar.google.com/scholar?q=Asynchronous+distributed+key+generation+for+computationally-secure+randomness,+consensus,+and+threshold+signatures)

[58] Yurek T, Luo L, Fairoze J, et al. hbacss: How to robustly share many secrets. **NDSS 2022** [Google Scholar](https://scholar.google.com/scholar?q=hbacss:+How+to+robustly+share+many+secrets)

[6] Beerliová-Trubíniová Z, Hirt M. Perfectly-secure MPC with linear communication complexity. **TCC 2008** [Google Scholar](https://scholar.google.com/scholar?q=Perfectly-secure+MPC+with+linear+communication+complexity)

[11] Cachin C, Kursawe K, Petzold F, et al. Secure and efficient asynchronous broadcast protocols. **CRYPTO 2001** [Google Scholar](https://scholar.google.com/scholar?q=Secure+and+efficient+asynchronous+broadcast+protocols)

[29] Gennaro R, Jarecki S, Krawczyk H, et al. Secure distributed key generation for discrete-log based cryptosystems. **Journal of Cryptology 2007** [Google Scholar](https://scholar.google.com/scholar?q=Secure+distributed+key+generation+for+discrete-log+based+cryptosystems)


## 关键词

+ 异步分布式密钥生成ADKG
+ 高门限密码系统
+ 秘密多项式采样
+ 拜占庭容错密钥生成
+ 随机信标门限签名
+ 异步多方计算
