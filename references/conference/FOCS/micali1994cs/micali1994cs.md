---
title: CS proofs
标题简称: 
论文类型: conference
会议简称: FOCS
发表年份: "1994"
modified: 2025-04-08 12:06:23
---

## CS proofs

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/365746)

## 作者

+ Silvio MiCali

## 笔记

### 背景与动机

证明是人类智力活动的核心，但传统数学证明缺乏对验证效率的正式保证，而计算复杂性理论中的 \(\mathcal{NP}\) 证明虽将验证时间限定为多项式，却要求验证者与判定者具有相同的渐进复杂度，无法实现验证比判定“指数级”更快的目标。交互式证明（IP）和概率可检验证明（PCP）虽然降低了验证者的工作，但往往将证明者的计算开销推到难以承受的高度：例如，为证明一个 \(n^{\log n}\) 时间可判定的语言，\(\mathcal{NP}\) 证明者可能需要指数时间寻找见证，IP 证明者在不具备专用协议时也需耗费与判定相当的巨量资源。现有方案的另一短板是缺乏“个体输入”视角——它们以语言类为对象，却无法保证对单个输入，证明者的工作与判定者的实际运行时间成比例。此外，交互式证明的可传递性差、多证明者系统的不可检查前提、以及概率可检验证明中“证明已免费加载到随机访问存储器”的不现实假设，都限制了证明概念在泛计算正确性（如程序检查）中的实用价值。本文旨在提出一种新型证明——计算可靠证明（CS proof），它通过将可靠性从“绝对”放松为“计算不可伪造”，使得证明者能以接近判定的时间生成一个短串，而验证者能在 poly-log 时间内确信定理的正确性，从而在实质上弥合“证明”与“判定”之间的鸿沟。

### 相关工作

[2] Goldwasser, Micali, Rackoff. The Knowledge Complexity of Interactive Proof Systems. **SIAM J. Comput. 1989** [Google Scholar](https://scholar.google.com/scholar?q=The+Knowledge+Complexity+of+Interactive+Proof+Systems)
> 核心思路：引入了交互式证明系统，定义了知识复杂性。
> 局限与区别：验证者与证明者需多轮交互，且验证复杂度并不一定比判定低；CS 证明是非交互的短串，且验证者享有 poly-log 加速。

[5] Lund, Fortnow, Karloff, Nisan. Algebraic Methods for Interactive Proof Systems. **STOC 1990** [Google Scholar](https://scholar.google.com/scholar?q=Algebraic+Methods+for+Interactive+Proof+Systems)
> 核心思路：利用代数技术证明 IP 包含 co-NP，进而 IP = PSPACE。
> 局限与区别：该协议对证明者资源的消耗极大，即使对于 PSPACE 中可有效判定的语句，证明者仍需运行指数级计算，不满足“可行性证明”目标。

[7] Brassard, Chaum, Crépeau. Minimum Disclosure Proofs of Knowledge. **J. Comput. System Sci. 1988** [Google Scholar](https://scholar.google.com/scholar?q=Minimum+Disclosure+Proofs+of+Knowledge)
> 核心思路：提出零知识参数（argument），证明者和验证者均为多项式时间有界，证明者拥有 NP 见证。
> 局限与区别：只适用于 NP 语言，且假设证明者已被赋予见证，未解决“获得见证比判定更难”的问题；CS 证明不预设见证，证明者自行通过判定算法生成证明。

[8] Babai, Fortnow, Levin, Szegedy. Checking Computation in Polylogarithmic Time. **STOC 1991** [Google Scholar](https://scholar.google.com/scholar?q=Checking+Computation+in+Polylogarithmic+Time)
> 核心思路：构造概率可检验证明（PCP），使验证者可在 poly-log 时间检查 NP 证明。
> 局限与区别：要求输入以特殊纠错格式呈现，且验证者仅检查证明而不产生可传递的短证书；CS 证明利用 PCP 内部思想，但将证明压缩为短串，并支持非交互传递。

[9] Feige, Goldwasser, Lovász, Safra, Szegedy. Approximating Clique is Almost NP-complete. **FOCS 1991** [Google Scholar](https://scholar.google.com/scholar?q=Approximating+Clique+is+Almost+NP-complete)
> 核心思路：利用概率可检验证明证明最大团近似问题的难解性。
> 局限与区别：验证者仍运行多项式时间，不追求验证比判定快得多；CS 证明借用了其“可抽样证明”的概念，但实现了验证的 poly-log 加速。

[14] Merkle. A Certified Digital Signature. **Crypto 1989** [Google Scholar](https://scholar.google.com/scholar?q=A+Certified+Digital+Signature)
> 核心思路：提出树哈希（Merkle tree）方案，用于以短根值认证多个一次性公钥。
> 局限与区别：原用途为数字签名中的公钥认证；CS 证明将树哈希用于对 PCP 证明的各个比特进行承诺，并支持按需打开单个比特。

[15] Kilian. A Note on Efficient Zero-Knowledge Proofs and Arguments. **STOC 1992** [Google Scholar](https://scholar.google.com/scholar?q=A+Note+on+Efficient+Zero-Knowledge+Proofs+and+Arguments)
> 核心思路：利用 Merkle 树和 PCP 构造通信量极少的零知识参数。
> 局限与区别：仍需要交互，且局限于 NP；CS 证明去掉了零知识要求，将交互替换为随机谕言机（或公共随机串），且扩展到任意半可判定语言，同时要求证明者自行产生而非外部提供见证。

[18] Goldreich, Goldwasser, Micali. How to Construct Random Functions. **J. ACM 1986** [Google Scholar](https://scholar.google.com/scholar?q=How+to+Construct+Random+Functions)
> 核心思路：基于伪随机生成器构造伪随机函数（GGM 构造），其输出对秘密种子的持有者是伪随机的。
> 局限与区别：秘密种子需保密，函数才具备不可区分性；CS 证明的密码学变体需要公开可评估的伪随机函数，本文基于 GGM 构造并额外假设某些统计性质在公开种子下仍成立。

[23] Fiat, Shamir. How to Prove Yourselves: Practical Solutions of Identification and Signature Problems. **Crypto 1986** [Google Scholar](https://scholar.google.com/scholar?q=How+to+Prove+Yourselves+Practical+Solutions+of+Identification+and+Signature+Problems)
> 核心思路：通过随机谕言机将交互式协议转化为非交互签名方案。
> 局限与区别：该转换启发式地依赖随机谕言机，但未提供可证明安全性；CS 证明中的随机谕言机用法类似，但在“保证型”构造中提供了严格证明，在密码学变体中则依赖于明确的伪随机函数假设。

### 核心技术与方案

本文构造的 CS 证明系统分为两个变体：保证型（guaranteed）和密码学型（cryptographic）。前者依赖共享随机谕言机，后者依赖公共随机串和一个密码学假设。两者的核心构造相同，只是随机谕言机被替换为 GGM 伪随机函数，并附加一个关于公开种子的特殊假设。以下以保证型为例阐述关键技术。

**整体框架与构造思路。**  
系统 \((\mathcal{P},\mathcal{V})\) 的输入是一个三元组 \(\vec{q} = (\bar{M}, x, t)\) 表示机器 \(M\) 在输入 \(x\) 上于 \(t\) 步内接受，以及一个安全参数 \(k\)。证明者 \(\mathcal{P}\) 首先运行 \(M(x)\) 产生接受计算历史 \(\sigma\)（长度为 \(O(t^2)\)），然后利用 PCP 技术将 \(\sigma\) 转化为一个可抽样证明 \(\tau\)，使得抽样验证者 \(SV\) 只需 poly-log 次查询即可验证正确性。然而 \(\tau\) 可能太长（\(\ell(n)\) 比特）不便于直接作为证书，因此 \(\mathcal{P}\) 对 \(\tau\) 的所有比特进行 Merkle 树承诺，仅输出根值 \(R_\epsilon\) 以及 \(k\) 次验证过程中需要打开的叶值和认证路径。验证者 \(\mathcal{V}\) 利用共同随机谕言机生成 \(k\) 个随机种子，运行 \(SV\) 并检查打开的比特是否与承诺一致。

**Merkle 树承诺方案。**  
令 \(\tau_1, \ldots, \tau_N\) 为 \(\tau\) 分割成的 \(N\) 个 \(k\) 比特块（\(N\) 为 2 的幂）。构造深度 \(\log N\) 的完全二叉树，每个叶节点 \(v_{[j]}\) 赋值为 \(\tau_j\)。对每个内部节点 \(v_\alpha\)，将其值定义为 \(R_\alpha = f_1(R_{\alpha 0} \mid R_{\alpha 1})\)，其中 \(f_1\) 是第一个随机谕言机（输出 \(k\) 比特）。根值 \(R_\epsilon\) 即为对整棵树的承诺。当 \(SV\) 需要访问 \(\tau\) 的某个比特时，\(\mathcal{P}\) 提供对应的叶块值、以及从该叶到根路径上所有兄弟节点的值（称为 SIBLINGPATH）。验证者据此重新计算根值并与声称的 ALLEGED-ROOT 比较，从而确认所打开比特的正确性。

**安全参数和 oracle 设置。**  
系统使用两个独立的随机谕言机 \(f_1: \Sigma^{2k} \to \Sigma^k\) 和 \(f_2: \Sigma^{k+n} \to \Sigma^{kL(n)}\)（可通过单一谕言机模拟）。\(f_1\) 用于树哈希，\(f_2\) 用于从根值 \(R_\epsilon\) 生成 \(k\) 个 \(L(n)\) 比特的随机磁带供 \(SV\) 使用。证明者运行时间由 \(O((nkt)^{c_2})\) 控制，证书长度由 \(O((nk \log t)^{c_3})\) 控制，其中 \(c_2, c_3\) 为某个固定常数。

**完备性（feasible completeness）。**  
若 \(\vec{q} \in \mathcal{L}\)，\(\mathcal{P}\) 如实产生 \(\tau\) 和正确的证书，则 \(\mathcal{V}\) 必定接受，因为所有的哈希验证和 \(SV\) 的 \(k\) 次运行均通过。证明者运行时间与 \(M(x)\) 的判定时间加 PCP 转换时间相近，满足“证明不比判定慢太多”的目标。

**可靠性（computational soundness）。**  
可靠性是核心难点。需要证明：对于任何 \(\vec{q}' \notin \mathcal{L}\)，任何作弊证明者 \(\mathcal{P}'\) 在 \(2^{c_5 k}\) 次谕言机调用内，成功让 \(\mathcal{V}\) 接受的概率至多为 \(2^{-c_6 k}\)。证明策略采用反证法和“重排引理”（不断进行概率平均）。主要步骤：

1. 假设存在 \(\mathcal{P}'\) 以概率 \(\ge 2^{-c_6 k'}\) 成功，则可找到一个具体的根值 \(R_\epsilon'\) 和对应的轴位置 \(m\)，使得在特定谕言机回复下输出证书的概率足够高。
2. 通过巧妙的“生长”过程（Lemma 2）固定序列 \(S\) 和部分回复，最后将问题转化为对固定 \(S\) 下的随机单次回复。
3. 构造算法 \(\mathcal{A}_{f_1}\) 通过大量随机采样来搜索一个满足条件的 \(\tilde{\tau}\)（一条 \(2^{\ell(n')}\) 长度的含通配符串），使得 \(SV\) 对 \(\tilde{\tau}\) 的接受概率 \(> 1/2\)。
4. 利用“生日悖论”的扩展（Lemma 1 和 Corollary 1）限制 \(\mathcal{A}\) 找到 \(f_1\)-碰撞的概率；利用 Chernoff 界和计数论证说明存在好的 \(f_1'\) 使得 \(\mathcal{A}\) 以 \(> 1/2\) 概率输出满足条件的 \(\tilde{\tau}\)。
5. 最终得到 \(\tilde{P}_{\tilde{\tau}} \ge 1/2\)，这与 \(SV\) 对 \(\vec{q}'\notin \mathcal{L}\) 的正确性质（任何串被接受的概率 \(< 1/2\)，因可抽样证明系统的可靠性）矛盾。因此假设不成立。

**证书长度与验证复杂度。**  
证书长度 \(|\mathcal{C}| = O(k + k \cdot \log N \cdot k) = O(k^2 \log N) = O(k^2 \log \ell(n)) = (nk \log t)^{O(1)}\)。验证时间：\(\mathcal{V}\) 运行 \(k\) 次 \(SV\)，每次查询 poly-log 个位置，并结合 \(O(\log N)\) 次哈希计算，总时间为 \(O(k \cdot \text{polylog}(t) + k \log N) = \text{poly}(n,k,\log t)\)。与判定时间 \(t\) 相比，验证实现了 poly-log 加速。

**密码学型 CS 证明。**  
构造与保证型相同，但将随机谕言机 \(f_1, f_2\) 替换为 GGM 伪随机函数 \(f_s\)（种子 \(s\) 公开）。证明者与验证者共享短随机串 \(r = s\)。可靠性建立在假设 \(\mathcal{A}\) 上：即使种子公开，作弊者无法高效找到能通过验证的根值 \(R_\epsilon'\)。该假设比离散对数问题更弱，因为可自由选择底层单向函数。

### 核心公式与流程

**[Merkle 树承诺]**
$$R_{[j]} = \tau_j \quad (\text{叶节点}), \qquad R_\alpha = f_1(R_{\alpha 0} \mid R_{\alpha 1}) \quad (\text{内部节点})$$
> 作用：将长字符串 \(\tau\) 压缩为短根值 \(R_\epsilon\)，并支持按需打开单个叶块并验证。

**[验证者路径检查]**
$$R_{\alpha[1\cdots m-1]} = \begin{cases}
f_1(R_{\alpha[1\cdots m]} \mid R_{\alpha[1\cdots \bar{m}]}) & \text{if } \alpha_m = 1 \\
f_1(R_{\alpha[1\cdots \bar{m}]} \mid R_{\alpha[1\cdots m]}) & \text{if } \alpha_m = 0
\end{cases}$$
> 作用：验证者使用从证书中读取的叶值和兄弟路径，重新计算父节点直至根，确认所打开的比特对应于承诺的根。

**[图检查算法 C（NP 完全程序检查）]**
$$
\sigma_0 = \varepsilon; \quad \forall i, \; \text{构造 } G_{\sigma_{i-1}} \text{ 编码 } S_{\sigma_{i-1}}; \quad \sigma_i = \begin{cases}
\sigma_{i-1}0 & \text{if } \mathcal{HP}(G_{\sigma_{i-1}}) = \text{YES} \\
\sigma_{i-1}1 & \text{else}
\end{cases}
$$
> 作用：通过二分搜索（按位确定）构造一个 CS 证书，证明非哈密顿性。若最终证书被接受，则输出证书；否则输出一系列证明 \(\mathcal{HP}\) 错误的反例。

### 实验结果

本文为纯理论论文，未提供实验数据。作者在引言中指出，所有结果与构造均基于数学证明，而非实验验证。论文的重点是提出 CS proof 的概念、构造和正确性证明，并讨论其在程序检查中的应用。因此，本节无法报告实验结果，仅指出：构造的可行性由定理保证，验证者各项复杂度以多项式或 poly-log 形式给出，而实际部署中的效率取决于底层 PCP 系统、Merkle 树参数以及密码学原语的具体选择。

### 局限性与开放问题

CS proof 的保证型依赖共享随机谕言机，在现实中难以实现；密码学型则依赖公开种子仍保持伪随机性的假设 \(\mathcal{A}\)，该假设虽弱于传统假设但缺乏广泛验证。构造中使用的 PCP 系统自身规模较大，影响实际性能。另外，CS proof 的可靠性是计算性的：若敌对者获得超多项式能力，则伪造证书可能变得可行。未来工作应包括：基于标准假设（如仅单向函数）构造密码学型 CS proof；探索更高效的 PCP 和树哈希组合以降低证书长度；将 CS proof 应用于更多计算正确性场景，如可验证外包计算。

### 强关联论文

[2] Goldwasser, Micali, Rackoff. The Knowledge Complexity of Interactive Proof Systems. **SIAM J. Comput. 1989** [Google Scholar](https://scholar.google.com/scholar?q=The+Knowledge+Complexity+of+Interactive+Proof+Systems)

[7] Brassard, Chaum, Crépeau. Minimum Disclosure Proofs of Knowledge. **J. Comput. System Sci. 1988** [Google Scholar](https://scholar.google.com/scholar?q=Minimum+Disclosure+Proofs+of+Knowledge)

[8] Babai, Fortnow, Levin, Szegedy. Checking Computation in Polylogarithmic Time. **STOC 1991** [Google Scholar](https://scholar.google.com/scholar?q=Checking+Computation+in+Polylogarithmic+Time)

[9] Feige, Goldwasser, Lovász, Safra, Szegedy. Approximating Clique is Almost NP-complete. **FOCS 1991** [Google Scholar](https://scholar.google.com/scholar?q=Approximating+Clique+is+Almost+NP-complete)

[14] Merkle. A Certified Digital Signature. **Crypto 1989** [Google Scholar](https://scholar.google.com/scholar?q=A+Certified+Digital+Signature)

[15] Kilian. A Note on Efficient Zero-Knowledge Proofs and Arguments. **STOC 1992** [Google Scholar](https://scholar.google.com/scholar?q=A+Note+on+Efficient+Zero-Knowledge+Proofs+and+Arguments)

[18] Goldreich, Goldwasser, Micali. How to Construct Random Functions. **J. ACM 1986** [Google Scholar](https://scholar.google.com/scholar?q=How+to+Construct+Random+Functions)

[23] Fiat, Shamir. How to Prove Yourselves: Practical Solutions of Identification and Signature Problems. **Crypto 1986** [Google Scholar](https://scholar.google.com/scholar?q=How+to+Prove+Yourselves+Practical+Solutions+of+Identification+and+Signature+Problems)


## 关键词

+ CS证明
+ 简洁证明系统
+ 随机预言机模型
+ NP完全问题验证
+ 计算复杂性理论
+ 多项式时间检验