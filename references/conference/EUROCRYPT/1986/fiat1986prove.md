---
title: "How to prove yourself: Practical solutions to identification and signature problems"
标题简称:
论文类型: conference
会议简称: EUROCRYPT
发表年份: 1986
modified: 2025-04-14 09:54:24
---

## How to prove yourself: Practical solutions to identification and signature problems

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/3-540-47721-7_12)

## 作者

+ Amos Fiat 
+ Adi Shamir 

## 笔记

### 背景与动机
在大规模商用和军事应用中，创建不可伪造的智能卡身份凭证是一个关键挑战。当验证方和证明方互为对手时，问题尤为严峻——必须确保验证方即使完整见证并验证了证明方生成的任意多次身份证明，也无法冒充证明方。该论文将保护机制分为三个层次：认证方案（仅对外部威胁有效）、识别方案（防止验证者冒充证明方）以及签名方案（防止验证者哪怕是向自己也无法伪造证据）。此前的密码学方案，如 RSA，虽能提供签名和认证机制，但其计算开销过大（典型实现需要 768 次模乘），难以应用于资源受限的微处理器设备（如智能卡、个人计算机）。因此，该论文旨在设计一种证明上安全、且计算和通信复杂度远低于 RSA 的实用方案。

### 相关工作

[2] Goldreich, Goldwasser and Micali. How to Construct Random Functions. **FOCS 1984** [Google Scholar](https://scholar.google.com/scholar?q=How+to+Construct+Random+Functions)
> 核心思路：提出一种在密码学意义上与真随机函数不可区分的伪随机函数构造方法。
> 局限与区别：该论文指出实践中可选用更高效的函数（如多重DES），而不必采用该构造以实现完全可证明的安全性。

[4] Goldwasser, Micali and Rackoff. The Knowledge Complexity of Interactive Proof Systems. **STOC 1985** [Google Scholar](https://scholar.google.com/scholar?q=The+Knowledge+Complexity+of+Interactive+Proof+Systems)
> 核心思路：提出零知识交互式证明的理论框架，定义知识复杂性。
> 局限与区别：该理论框架缺乏实际的、高效的识别应用。该论文将此类零知识证明与基于身份的方案结合，转化为实用的识别与签名协议。

[5] Shamir. Identity-Based Cryptosystems and Signature Schemes. **Crypto 1984** [Google Scholar](https://scholar.google.com/scholar?q=Identity-Based+Cryptosystems+and+Signature+Schemes)
> 核心思路：提出基于用户身份信息而非公钥证书的密码系统。
> 局限与区别：该论文直接使用身份信息 $I$ 来生成可验证的凭证 $v_j$，从而消除了公钥目录的需求，并结合零知识证明设计了比原方案更高效的协议。

[1] Fischer, Micali and Rackoff. A Secure Protocol for the Oblivious Transfer. **Eurocrypt 1984** [Google Scholar](https://scholar.google.com/scholar?q=A+Secure+Protocol+for+the+Oblivious+Transfer)
> 核心思路：提出了一个用于证明数二次剩余性的相关协议。
> 局限与区别：该论文的协议是该工作中 $k=1$ 的特例，而该文通过引入 $k>1$ 的多秘密参数，在相同安全级别下将迭代次数从 $t$ 降低到约 $\sqrt{t}$，大幅提升了速度和通信效率。

[3] Goldreich, Micali and Wigderson. Proofs that Yield Nothing But the Validity of the Assertion and the Methodology of Cryptographic Protocol Design. **FOCS 1986** [Google Scholar](https://scholar.google.com/scholar?q=Proofs+that+Yield+Nothing+But+the+Validity+of+the+Assertion+and+the+Methodology+of+Cryptographic+Protocol+Design)
> 核心思路：为任何 NP 完全问题的实例构建零知识证明。
> 局限与区别：该论文指出这类通用构造的时通信复杂度虽有改进，但实际应用性仍不明确。与此相对，该文基于模平方根难题的专用方案在实用指标上远优于通用方法。

### 核心技术与方案

该论文提出了两个相互关联的方案：交互式识别方案和非交互式签名方案，二者均基于相同的密码学假设，即合数模 $n=pq$ 下计算模平方根的困难性。

**1. 交互式识别方案**
方案设置了一个可信中心，中心选择并公开一个公共模数 $n$（两个大素数的乘积）和伪随机函数 $f$。当用户申请智能卡时，中心生成用户的身份字符串 $I$，对于 $j=1,\dots,k$ 计算 $v_j = f(I,j)$，从中选取 $v_j$ 为二次剩余的 $k$ 个索引，并计算其最小时根 $s_j$（即 $s_j^2 \equiv v_j^{-1} \pmod{n}$）。这些 $s_j$ 作为秘密密钥存放在卡内，而 $n$ 和 $f$ 是所有验证设备共享的公共信息。

交互证明协议通过 $t$ 轮迭代完成。每轮中，证明方A生成随机数 $r_i$ 并发送承诺 $x_i = r_i^2 \pmod{n}$；验证方B返回随机的挑战向量 $(e_{i1},\dots,e_{ik})$，其中 $e_{ij} \in \{0,1\}$；A计算并发送响应 $y_i = r_i \prod_{e_{ij}=1} s_j \pmod{n}$；B验证 $x_i \equiv y_i^2 \prod_{e_{ij}=1} v_j \pmod{n}$。若所有 $t$ 轮均通过，则身份被接受。
该协议的正确性由等式 $y_i^2 \prod v_j \equiv r_i^2 \prod (s_j^2 v_j) \equiv r_i^2 \equiv x_i \pmod{n}$ 保证。安全性方面，方案可分为三个层面：可靠性保证探知不到秘密的概率为 $2^{-kt}$，零知识性通过存在一个模拟器（期望运行时间为 $t \cdot 2^k$）产生与真实交互不可区分的对话来证明。该方案计算量极低，平均模乘次数为 $t(k+2)/2$，约为 RSA 的 $1\%$ 到 $4\%$。

**2. 非交互式签名方案**
要获得真正的数字签名，需要消除交互性。该方案用伪随机函数 $f$ 代替验证者的角色。签名者A首先选取随机数 $r_1,\dots,r_t$，计算 $x_i = r_i^2 \pmod{n}$，然后生成挑战矩阵 $e_{ij}$ 为 $f(m,x_1,\dots,x_t)$ 的前 $kt$ 位。随后A计算 $y_i = r_i \prod_{e_{ij}=1} s_j \pmod{n}$，并将签名 $(\text{签名},m, e_{ij}, y_i)$ 发送给B。
验证时，B计算 $v_j = f(I,j)$，然后计算 $z_i = y_i^2 \prod_{e_{ij}=1} v_j \pmod{n}$，最后检验 $f(m,z_1,\dots,z_t)$ 的前 $kt$ 位是否等于 $e_{ij}$。正确性源自 $z_i \equiv x_i$。安全性证明基于假定 $f$ 为真随机函数，并将攻击者 $AL$ 转化为模 $n$ 的因子分解算法：若 $AL$ 能成功伪造签名，则可构造 $AL'$ 计算 $\prod v_j^{c_j}$ 的平方根，进而以概率 $1/2$ 分解 $n$。该方案中 $kt$ 需提升至至少 $72$ 以抵御离线字典攻击。

### 核心公式与流程

**[身份识别协议一轮流程（第 $i$ 轮）]**
$$
\begin{aligned}
&\text{A} \rightarrow \text{B}: \quad x_i = r_i^2 \pmod{n} \\
&\text{B} \rightarrow \text{A}: \quad \text{随机挑战向量 } (e_{i1},\dots,e_{ik}) \\
&\text{A} \rightarrow \text{B}: \quad y_i = r_i \prod_{\{j:e_{ij}=1\}} s_j \pmod{n} \\
&\text{B 验证}: \quad x_i \equiv y_i^2 \prod_{\{j:e_{ij}=1\}} v_j \pmod{n}
\end{aligned}
$$
> 作用：实现证明方对秘密 $s_j$ 的零知识证明。

**[签名生成与验证流程]**
$$
\begin{aligned}
&\text{签名生成} \\
&x_i \leftarrow r_i^2 \pmod{n}, \quad 1 \le i \le t \\
&e_{ij} \leftarrow f(m, x_1,\dots,x_t) \text{ 的前 } kt \text{ 位} \\
&y_i \leftarrow r_i \prod_{\{j:e_{ij}=1\}} s_j \pmod{n}, \quad 1 \le i \le t \\
&\text{签名} \leftarrow (m, e_{ij}, y_i) \\
&\text{签名验证} \\
&z_i \leftarrow y_i^2 \prod_{\{j:e_{ij}=1\}} v_j \pmod{n}, \quad 1 \le i \le t \\
&\text{检验: } f(m, z_1,\dots,z_t) \text{ 的前 } kt \text{ 位} \stackrel{?}{=} e_{ij}
\end{aligned}
$$
> 作用：将交互式识别转化为非交互式签名，挑战由消息和承诺的哈希值伪随机生成。

**[安全性归约核心关系]**
$$
y_i' / y_i'' \equiv \prod_{j=1}^{k} s_j^{c_j} \pmod{n}
$$
> 作用：攻击者若能为同一 $x_i$ 响应两个不同挑战，则可计算出秘密的乘积，从而导出矛盾的证明或用于分解 $n$。

### 实验结果

实验设置方面，论文以理论分析和参数权衡为主，未提供具体的硬件实现结果。核心性能数值如下：针对 $2^{-20}$ 的识别方案，取参数 $k=5, t=4$ 即可实现，平均模乘次数为 $t(k+2)/2 = 14$，通信字节数为 $323$ 字节，秘密密钥存储为 $320$ 字节（$k=18, t=4$ 时，$2^{-72}$ 级别签名方案仅需 $7.6$ 次模乘，低于 RSA 的 $768$ 次）。当 $k=18$ 且限制 $e_{ij}$ 中至多 $3$ 个 $1$ 时，通信量降至 $165$ 字节，模乘次数降至 $7.6$。签名方案中（$2^{-72}$ 级别），若取 $k=9, t=8$，密钥为 $576$ 字节，签名大小 $521$ 字节，平均 $44$ 次模乘；若取 $k=18, t=4$，密钥增至 $1152$ 字节，签名大小降至 $265$ 字节，优化后仅需 $32$ 次模乘，为 RSA 的 $4\%$。表 1 展示了 $k$ 和 $t$ 从 $1$ 到 $72$ 的多种权衡，总迭代次数 $kt$ 固定为 $72$ 时，密钥大小从 $64$ 到 $4608$ 字节变化，签名大小从 $4608+9$ 下降到 $64+9$ 字节，平均模乘次数在 $37$ 到 $108$ 之间。该方案的适用参数范围极广，能在时间、空间和通信之间灵活折中。

### 局限性与开放问题

该论文的签名方案虽然可证明安全，但并非零知识，因此验证者能从签名获取关于秘密的隐式信息，尽管归约证明保证了从该信息中无法高效提取出完整秘密。实际实现中，$f$ 函数必须选择得足够强（论文建议采用多重 DES），否则若 $f$ 存在偏向，则安全性会退化。所有方案均依赖可信中心，中心持有 $n$ 的分解信息，在任何应用中都是一个单点故障和高价值攻击目标。此外，方案的核心是模平方根难题，尚未探索将其推广到基于其他密码学困难问题（如格或编码理论）的变体。

### 强关联论文

[1] Fischer, Micali and Rackoff. A Secure Protocol for the Oblivious Transfer. **Eurocrypt 1984** [Google Scholar](https://scholar.google.com/scholar?q=A+Secure+Protocol+for+the+Oblivious+Transfer)

[2] Goldreich, Goldwasser and Micali. How to Construct Random Functions. **FOCS 1984** [Google Scholar](https://scholar.google.com/scholar?q=How+to+Construct+Random+Functions)

[3] Goldreich, Micali and Wigderson. Proofs that Yield Nothing But the Validity of the Assertion and the Methodology of Cryptographic Protocol Design. **FOCS 1986** [Google Scholar](https://scholar.google.com/scholar?q=Proofs+that+Yield+Nothing+But+the+Validity+of+the+Assertion+and+the+Methodology+of+Cryptographic+Protocol+Design)

[4] Goldwasser, Micali and Rackoff. The Knowledge Complexity of Interactive Proof Systems. **STOC 1985** [Google Scholar](https://scholar.google.com/scholar?q=The+Knowledge+Complexity+of+Interactive+Proof+Systems)

[5] Shamir. Identity-Based Cryptosystems and Signature Schemes. **Crypto 1984** [Google Scholar](https://scholar.google.com/scholar?q=Identity-Based+Cryptosystems+and+Signature+Schemes)


## 关键词

+ 身份识别协议
+ 数字签名
+ 零知识证明
+ 模乘法优化
+ 智能卡