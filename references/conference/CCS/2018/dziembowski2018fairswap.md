---
title: "Fairswap: How to fairly exchange digital goods"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2018
---

## Fairswap: How to fairly exchange digital goods

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3243734.3243857)

## 作者

+ Stefan Dziembowski 
+ Lisa Eckey 
+ Sebastian Faust 


## 笔记

### 背景与动机
公平交换数字商品是互联网中的一个基本问题：发送方 S 希望以固定价格出售数字商品 x 给接收方 R，要求 R 只有在收到满足谓词 φ(x)=1 的正确商品时才付款，S 只有在确实发送了正确商品时才获得付款。已有理论结果表明，在没有额外假设的情况下不可能实现强公平性 [40]。传统方案引入可信第三方（托管服务）[33]，但完全可信的中间人往往不可得或成本高昂。基于加密货币的智能合约提供了一种去中心化的替代方案，但若商品 x 很大（例如数 GB 的文件），直接在链上存储和验证 φ(x) 会导致极高的交易费用。零知识条件支付（ZKCP）[46] 通过零知识证明避免了链上大数据的处理，却给参与方带来了巨大的计算负担，尤其当电路 φ 复杂或证据 x 很大时，零知识证明的生成和验证仍非常低效。本文旨在设计一种既能保持低链上费用又能避免零知识证明重计算开销的公平交换协议，同时支持任意谓词函数 φ 和大尺寸证据 x。

### 相关工作

[10] Bentov 等. How to Use Bitcoin to Design Fair Protocols. **CRYPTO 2014** [Google Scholar](https://scholar.google.com/scholar?q=How+to+Use+Bitcoin+to+Design+Fair+Protocols)
> 核心思路：利用比特币实现公平的密码学协议，引入“claim-or-refund”功能作为基本构件。  
> 局限与区别：其 claim-or-refund 的朴素实现需要智能合约处理复杂电路或大数据，导致高费用；本文通过“行为不当证明”大幅降低链上复杂度。

[46] Bitcoin Wiki. Zero Knowledge Contingent Payment. **2018** [Google Scholar](https://scholar.google.com/scholar?q=Zero+Knowledge+Contingent+Payment)
> 核心思路：使用零知识证明实现公平交换，仅需在链上验证哈希。  
> 局限与区别：零知识证明生成和验证计算开销大，不适合大电路或大证据；本文避免使用零知识证明。

[12] Bowe. Pay-to-sudoku. **2016** [Google Scholar](https://scholar.google.com/scholar?q=Pay-to-sudoku)
> 核心思路：ZKCP 的首个实现。  
> 局限与区别：被 Campanelli 等 [15] 发现安全漏洞；本文无需 ZKCP，不受此类攻击影响。

[15] Campanelli 等. Zero-Knowledge Contingent Payments Revisited: Attacks and Payments for Services. **CCS 2017** [Google Scholar](https://scholar.google.com/scholar?q=Zero-Knowledge+Contingent+Payments+Revisited)
> 核心思路：指出 ZKCP 中若使用 NIZK 且验证者生成 CRS 则存在子版本攻击，并提出修复方案。  
> 局限与区别：修复仍需零知识证明；本文方案与此攻击无关。

[44] Teutsch 等. TrueBit – a scalable verification solution for blockchains. **2018** [Google Scholar](https://scholar.google.com/scholar?q=TrueBit+%E2%80%93+a+scalable+verification+solution+for+blockchains)
> 核心思路：使用“行为不当证明”解决链上可验证计算问题，系统包含证明者、验证者和法官。  
> 局限与区别：TrueBit 要求证明者公开解并交互，本文需要非交互且计算结果对他人保密；本文提供了具体的 Encode/Extract/Judge 子程序并给出形式化安全分析。

[5] Asokan 等. Optimistic Fair Exchange of Digital Signatures. **EUROCRYPT 1998** [Google Scholar](https://scholar.google.com/scholar?q=Optimistic+Fair+Exchange+of+Digital+Signatures)
> 核心思路：乐观公平交换，仅在争议时咨询第三方（TTP）。  
> 局限与区别：依赖传统 TTP；本文使用区块链智能合约替代 TTP，且通过行为不当证明降低链上开销。

[13] Cachin 等. Optimistic Fair Secure Computation. **CRYPTO 2000** [Google Scholar](https://scholar.google.com/scholar?q=Optimistic+Fair+Secure+Computation)
> 核心思路：乐观公平安全计算。  
> 局限与区别：同样依赖 TTP；本文针对数字商品交换而非通用安全计算。

[33] Küpçü 等. Usable optimistic fair exchange. **Computer Networks 2012** [Google Scholar](https://scholar.google.com/scholar?q=Usable+optimistic+fair+exchange)
> 核心思路：使用仲裁者通过 cut-and-choose 实现文件交换的乐观公平交换。  
> 局限与区别：cut-and-choose 导致非可忽略的错误概率且仲裁者负担重；本文错误概率可忽略且链上成本低。

[7] Banasik 等. Efficient Zero-Knowledge Contingent Payments in Cryptocurrencies Without Scripts. **ESORICS 2016** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+Zero-Knowledge+Contingent+Payments+in+Cryptocurrencies+Without+Scripts)
> 核心思路：在不支持合约的加密货币上实现 ZKCP。  
> 局限与区别：仍需零知识证明；本文环境为支持智能合约的加密货币并利用合约进行高效验证。

### 核心技术与方案
本文整体框架：利用智能合约作为法官，通过“行为不当证明”实现公平交换，避免链上执行复杂电路 φ。核心思路是：检查整个计算中某一步的错误比验证整个计算要容易得多。协议分为三个阶段：初始化、密钥揭示、支付。发送方 S 用密钥 k 加密证据 x 及 φ(x) 的中间计算结果，得到编码 z，并将承诺 c = H(k) 和 Merkle 树根 r_z、r_φ 发送给合约。接收方 R 收到 z 后，将 p 枚硬币冻结在合约中。随后 S 揭示密钥 k，R 运行 Extract 算法解密并重新计算 φ(x)，若 φ(x) ≠ 1 则 R 可生成一个简洁的“行为不当证明”π，发送给合约；合约运行 Judge 算法验证 π，若接受则退款给 R，否则将硬币支付给 S。若 R 在揭示后无反应，S 可在第5轮调用合约获得支付。

协议的核心算法 Encode、Extract、Judge 描述如下：

- **Encode(k, x, φ)**：对每个输入门 i ∈ [n]，out_i = x_i，z_i = Enc(k, out_i)；对每个中间门 i ∈ {n+1,…,m}，解析 φ_i = (i, op_i, I_i)，计算 out_i = op_i(out_{I_i[1]}, …, out_{I_i[ℓ]})，z_i = Enc(k, out_i)。输出 z = (z_1,…,z_m)。
- **Extract(z, φ, k)**：解密得到 out_1,…,out_n 为 x_i，重建 Merkle 树 M_z 和 M_φ，然后按顺序计算每个门的输出 out_i，与解密得到的 Dec(k, z_i) 比较；若发现不一致（或输出门 out_m ≠ 1），则生成π：对 φ_i 的 Merkle 证明、对 z_i 的 Merkle 证明、对每个输入值 z_j 的 Merkle 证明。输出 (x, π) 或 (x, ⊥)。
- **Judge(k, r_z, r_φ, π)**：解析π包含 (π_φ, π_out, π_in^1,…,π_in^ℓ)，验证 Merkle 证明与根 r_z, r_φ 匹配，然后解密得到 out_i 和输入值，计算 op_i(输入) 并与 out_i 比较，若不相等则接受投诉（输出1），否则拒绝（输出0）。

安全性直觉：发送方无法伪造编码使得 R 生成被拒绝的证明，因为需要找到哈希碰撞；接收方在 S 揭示密钥前无法获知 x，因为加密是 IND-CPA 的；协议在至多5轮内终止，公平性来源于行为不当证明的绑定性及合约的冻结机制。渐近复杂度：合约验证一个行为不当证明需要 O(log m) 个 Merkle 验证操作，其中 m 为电路门数；发送方和接收方各需 O(m) 次哈希计算。

### 核心公式与流程

**[Encode 算法]**
$$
\begin{aligned}
&\text{for each } i\in[n]: out_i = x_i,\; z_i = \text{Enc}(k, out_i)\\
&\text{for each } i\in\{n+1,\dots,m\}:\\
&\quad \text{parse } \phi_i = (i, op_i, I_i)\\
&\quad out_i = op_i(out_{I_i[1]},\dots,out_{I_i[\ell]})\\
&\quad z_i = \text{Enc}(k, out_i)\\
&\text{Output } z = (z_1,\dots,z_m)
\end{aligned}
$$
> 作用：生成加密证据和中间值。

**[Extract 算法核心部分]**
$$
\begin{aligned}
&\text{for each } i\in[n]: out_i = \text{Dec}(k, z_i),\; x_i = out_i\\
&\text{for each } i\in\{n+1,\dots,m\}:\\
&\quad out_i = op_i(out_{I_i[1]},\dots,out_{I_i[\ell]})\\
&\quad \text{if } \text{Dec}(k, z_i) \neq out_i \text{ or } (i=m \text{ and } out_i \neq 1):\\
&\qquad \text{build } \pi \text{ with Merkle proofs}\\
&\text{Output } (x, \pi) \text{ or } (x, \bot)
\end{aligned}
$$
> 作用：解密并验证计算正确性，生成行为不当证明。

**[Judge 算法]**
$$
\begin{aligned}
&\text{Verify } \pi_{\phi},\pi_{out},\pi_{in}^j \text{ against } r_{\phi}, r_z\\
&out_i = \text{Dec}(k, z_i)\\
&\text{if } i=m \text{ and } out_i \neq 1: \text{ accept}\\
&\text{for each } j\in[\ell]: out_{I_i[j]} = \text{Dec}(k, z_j)\\
&\text{if } op_i(out_{I_i[1]},\dots,out_{I_i[\ell]}) \neq out_i: \text{ accept}\\
&\text{else reject}
\end{aligned}
$$
> 作用：验证单个门计算是否错误，决定投诉是否成立。

### 实验结果
本文为文件销售应用实现了原型（基于以太坊 Solidity）。电路采用 Merkle 树哈希验证，指令集仅包含哈希和比较，fan-in=2，因此可实现极高效的合约。部署合约成本约 1,050,000 gas（约 1.57 USD，假设 gas 价格 3 GWei，ETH 500 USD）。乐观场景（R 接受文件不投诉）成本约 1.73 USD，接近常数；悲观场景（R 投诉）成本随文件块长度线性增长，因为行为不当证明大小与块大小和 Merkle 深度相关。对于 1 GB 文件，通过调整文件块大小可权衡编码开销与链上成本。编码吞吐量约 2 MB/s（单核 2.67 GHz i7，8 GB RAM）。协议需要 4 轮区块链交互，每轮时间取决于网络拥堵（以太坊上通常几分钟完成）。通过状态通道可将重复执行的成本分摊，首次部署后每次只需约 1.60 USD。

### 局限性与开放问题
协议无法阻止发送方发起拒绝服务攻击（S 可初始化合约但不揭示密钥，使 R 资金被冻结），虽可通过惩罚金缓解但无法完全消除。接收方也可恶意多次请求文件而不接受合约执行，给发送方带来计算和费用负担。状态通道网络尚不成熟，将 FairSwap 集成到状态通道网络中是未来工作。此外，即使在悲观场景下，投诉成本仍可能较高，进一步优化证明大小和 gas 消耗值得探索。

### 强关联论文

[46] Bitcoin Wiki. Zero Knowledge Contingent Payment. **2018** [Google Scholar](https://scholar.google.com/scholar?q=Zero+Knowledge+Contingent+Payment)

[10] Iddo Bentov and Ranjit Kumaresan. How to Use Bitcoin to Design Fair Protocols. **CRYPTO 2014** [Google Scholar](https://scholar.google.com/scholar?q=How+to+Use+Bitcoin+to+Design+Fair+Protocols)

[44] Jason Teutsch and Christian Reitwießner. TrueBit – a scalable verification solution for blockchains. **2018** [Google Scholar](https://scholar.google.com/scholar?q=TrueBit+%E2%80%93+a+scalable+verification+solution+for+blockchains)

[12] Sean Bowe. Pay-to-sudoku. **2016** [Google Scholar](https://scholar.google.com/scholar?q=Pay-to-sudoku)

[15] Matteo Campanelli, Rosario Gennaro, Steven Goldfeder, and Luca Nizzardo. Zero-Knowledge Contingent Payments Revisited: Attacks and Payments for Services. **CCS 2017** [Google Scholar](https://scholar.google.com/scholar?q=Zero-Knowledge+Contingent+Payments+Revisited)

[5] N. Asokan, Victor Shoup, and Michael Waidner. Optimistic Fair Exchange of Digital Signatures. **EUROCRYPT 1998** [Google Scholar](https://scholar.google.com/scholar?q=Optimistic+Fair+Exchange+of+Digital+Signatures)

[33] Alptekin Küpçü and Anna Lysyanskaya. Usable optimistic fair exchange. **Computer Networks 2012** [Google Scholar](https://scholar.google.com/scholar?q=Usable+optimistic+fair+exchange)

[7] Waclaw Banasik, Stefan Dziembowski, and Daniel Malinowski. Efficient Zero-Knowledge Contingent Payments in Cryptocurrencies Without Scripts. **ESORICS 2016** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+Zero-Knowledge+Contingent+Payments+in+Cryptocurrencies+Without+Scripts)

[18] Ran Canetti, Ben Riva, and Guy N. Rothblum. Practical delegation of computation using multiple servers. **CCS 2011** [Google Scholar](https://scholar.google.com/scholar?q=Practical+delegation+of+computation+using+multiple+servers)


## 关键词

+ 公平交换
+ 智能合约
+ 区块链
+ 数字商品
+ 成本优化