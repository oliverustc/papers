---
title: "Oblivious message retrieval"
doi: 10.1007/978-3-031-15802-5_26
标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 2022
modified: 2025-04-09 12:10:23
---
## Oblivious message retrieval

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-15802-5_26)

## 作者

+ [Zeyu Liu](Zeyu%20Liu.md)
+ [Eran Tromer](Eran%20Tromer.md)

## 笔记

### 背景与动机
匿名消息传递系统（如隐私支付加密货币Zcash [8,30] 和Monero [48]）需要接收方从公开的公告板（如区块链）上识别属于自己的消息，同时不泄露关于接收方的元数据。最直接的“全扫描”方式要求接收方下载并处理整个公告板，这对资源受限的移动设备而言通信和计算开销过高。现有方案Zcash的“轻客户端”协议ZIP-307 [27] 虽然通过压缩消息减小了传输量，但处理仍需数小时，成为严重的可用性瓶颈。Fuzzy Message Detection (FMD) [7] 通过引入假阳性提供了一定隐私保护，但这需要在隐私（高假阳性密度）与效率（处理大量假消息的开销）之间进行艰难的权衡。Private Signaling (PS) [44] 方案要么依赖可信硬件（如Intel SGX）这一强信任假设，要么需要一对不共谋的服务器，且两个方案在存在恶意参与者时都易受放大式拒绝服务攻击。本文旨在填补这一空白：实现一种同时满足完全隐私、抗DoS攻击、密钥不可链接、无需信任假设且实际可行的遗忘消息检索方案。

### 相关工作
[7] Beck 等. Fuzzy Message Detection. **CCS 2021** [Google Scholar](https://scholar.google.com/scholar?q=Fuzzy+Message+Detection)
> 核心思路：检测器为每个接收方标记假阳性消息，使真实消息隐藏其中，隐私程度由假阳性率p控制。
> 局限与区别：提供的是基于假阳性的弱匿名性，难以抵御主动攻击或长期流量分析；易受恶意生成的“通配符”密文攻击导致DoS；检测密钥与公钥可链接。

[44] Madathil 等. Private Signaling. **ePrint 2021** [Google Scholar](https://scholar.google.com/scholar?q=Private+Signaling)
> 核心思路：单服务器方案（PS1）依赖Intel SGX进行隐私计算；双服务器方案（PS2）依赖两个不共谋服务器运行混淆电路。
> 局限与区别：PS1在SGX被攻破时完全失效，PS2的隐私仅在被分到同一检测器的接收方集合内有效；二者均假设发送方和接收方诚实才能保证正确性，易受DoS攻击。

[4] Ali 等. Communication-Computation Trade-offs in PIR. **USENIX Security 2021** [Google Scholar](https://scholar.google.com/scholar?q=Communication-Computation+Trade-offs+in+PIR)
> 核心思路：利用FHE和线性编码实现批量私有信息检索，通过累加消息降低通信开销。
> 局限与区别：该方法假设检索索引已知，而本文的OMR需在不知索引的情况下从线索中推导。

[5] Angel 等. PIR with Compressed Queries and Amortized Query Processing. **IEEE S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=PIR+with+Compressed+Queries+and+Amortized+Query+Processing)
> 核心思路：与[4]类似，通过同态累加和编码实现高效PIR。
> 局限与区别：同样假设索引已知，本文将其思想扩展至未知索引的检测与检索问题。

[51] Ostrovsky 等. Private Searching on Streaming Data. **CRYPTO 2005** [Google Scholar](https://scholar.google.com/scholar?q=Private+Searching+on+Streaming+Data)
> 核心思路：允许客户端在加密数据流中搜索关键字，通过同态累加返回匹配文档。
> 局限与区别：搜索基于明文字符串，而本文需处理加密的、不可链接的“线索”以隐藏接收方身份，因此同态运算电路更复杂。

[54] Peikert 等. A Framework for Efficient and Composable Oblivious Transfer. **CRYPTO 2008** [Google Scholar](https://scholar.google.com/scholar?q=A+Framework+for+Efficient+and+Composable+Oblivious+Transfer)
> 核心思路：提出PVW加密方案，一种高效的LWE变体，支持多比特加密且密文尺寸增长慢。
> 局限与区别：本文将其作为生成轻量级线索的加密原语，并利用其可被BFV同态解密的性质。

[13,24] Brakerski; Fan 等. Fully Homomorphic Encryption without Modulus Switching; Somewhat Practical Fully Homomorphic Encryption. **CRYPTO 2012; ePrint 2012** [Google Scholar](https://scholar.google.com/scholar?q=Fully+Homomorphic+Encryption+without+Modulus+Switching;+Somewhat+Practical+Fully+Homomorphic+Encryption)
> 核心思路：提出BFV方案，一种支持SIMD运算的层状全同态加密方案。
> 局限与区别：本文利用BFV的SIMD特性和低成本进行同态解密线索和消息累积，避免使用昂贵的自举操作。

### 核心技术与方案
本文方案的整体框架分为两个主要阶段：首先是一个理论证明可行的通用构造（第5章），其次是一系列面向实际性能的优化（第6章），最终形成两个实用方案OMRp1和OMRp2。

**通用构造（第5章）**。该构造使用任意FHE方案，将所有消息的线索设计为$\ell$个FHE密文，每个密文加密1，指向接收方公钥。检测器（服务器）对每个线索进行重加密（Recrypt），得到扰动后的密文。若消息确实指向该接收方，重加密密文解密后为1；否则根据FHE的“错误密钥解密”性质，解密为1的概率仅为1/2 + negl(λ)。通过对$\ell$个结果执行逻辑与，可显著降低假阳性率。为实现紧凑的摘要（大小与相关消息数$\bar{k}$成正比而非总消息数N），检测器将每个消息随机分配到$m$个桶中，同态地将相关指示位累加到桶的计数器和内容累加器中。若所有桶计数均不超过1，接收方可直接解码获取相关消息索引；若存在碰撞，则通过多次独立重复采样（参数$C$）降低失败概率。对于检索（OMR），检测器在获取相关性向量PV后，利用稀疏随机线性编码（SRLC）对相关消息的负载进行加权线性组合，其中每个消息仅参与少量组合（权重非零概率为$\gamma/m$），接收方通过高斯消元解码。

**面向实际的优化（第6章）**。针对通用构造中重加密开销过大、线索尺寸过大的问题，本文进行了根本性改造。线索层采用更轻量的PVW加密方案[54]（一个LWE变体），其密文尺寸为$O(n+\ell)$。检测器端采用BFV层状同态加密[13,24]代替全同态加密，利用其在分组运算上的SIMD特性。检测过程的核心步骤是：（1）**InnerProd**：在BFV密文空间内，计算PVW线索与秘密密钥$sk_{PVW}$的同态内积$d = b - sk^T a$；（2）**RangeCheck**：通过预计算的纠错多项式$RC_r(X)$，判断内积值是否落在区间$[-r, r]$内，若是则输出0（表示相关），否则输出1。该多项式在有限域$\mathbb{Z}_t$上求值，深度可控。然后使用一个简单的单比特指示符翻转。最后，通过“确定性摘要压缩”或“随机性摘要压缩”将结果打包。确定性方法适合较小的N；随机性方法利用桶结构和SIMD打包，可使摘要尺寸摊销至小于1比特/消息。在DoS抵抗方面，本文证明，在“蛇眼抵抗”猜想的支持下，PVW加密的线索难以在同态解密下同时“欺骗”两个不同的接收方密钥，从而天然抵抗恶意生成的线索。在密钥不可链接方面，通过语义安全的BFV重新加密PVW密钥对，以及PVW密钥本身的重新采样，可实现完整的密钥不可链接性。

系统的渐进复杂度为：检测器计算量$O(N)$（每消息需进行PVW解密和范围检查），通信量（摘要尺寸）对于OMRp1为$O(N)$，对于OMRp2为$O(\log N \cdot \log(1/\epsilon_p) \cdot (\bar{k} + \epsilon_p N))$，接收方解码时间$O(\bar{k}^2)$（通过高斯消元）。本文方案的安全性基于标准格假设（Ring-LWE）。

### 核心公式与流程

**[PVW解密内积]**
$$
\vec{d} = \vec{b} - \mathsf{sk}^T\vec{a} \in \mathbb{Z}_q^\ell
$$
> 作用：检测器在BFV密文空间下同态计算PVW线索与接收方秘密密钥的内积。

**[范围检查多项式]**
$$
RC_r(X) = f_r(0) - \sum_{i=0}^{t-1} X^i \sum_{a=0}^{t-1} f_r(a)a^{t-1-i}
$$
其中$f_r(x)=0$当且仅当$x\in[-r,r]$（在模$t$意义下），否则为1。该多项式在$\mathbb{Z}_t$上求值，将内积结果$u$映射为0（相关）或1（不相关）。
> 作用：将同态PVW解密的内积结果转换为一个单比特的相关性指示符。

**[稀疏随机线性编码（SRLC）]**
$$
\mathsf{Cmb}_j = \bigg\langle \sum_{i\in\mathsf{PS}} w_{i,j} \cdot x_i \bigg\rangle_{\mathsf{sk}}, \quad j\in[m]
$$
其中$w_{i,j}$为随机权重，大多数为零（$\text{Pr}[w_{i,j} \neq 0] = \gamma/m$），$\mathsf{PS}$为相关消息索引集合，$x_i$为负载。
> 作用：检测器同态计算多个稀疏加权和，作为摘要的一部分，接收方通过解线性方程组恢复各个负载。

**[每组失败概率（无碰撞）]**
$$
\rho = \prod_{i=1}^{\bar{k}-1} \frac{(m-i)}{m}
$$
> 作用：当使用$m$个桶时，恰好每个相关消息被分到不同桶的概率，用于指导重复次数$C$以降低失败率。

### 实验结果
实验使用Google Compute Cloud c2-standard-4实例（4核Intel Xeon 3.10 GHz，16 GB RAM），针对包含N=500,000条消息的公告板（近似比特币日交易量），设置相关消息上限$\bar{k}=50$，假阳性率$\epsilon_p=2^{-21}$，假阴性率$\epsilon_n=2^{-30}$，负载大小为612字节（Zcash标准）。核心性能数值（见表2）：对于仅检测的OMDp1方案，检测器计算时间为0.021秒/消息（1线程），摘要通信开销为0.56字节/消息；对于完整检索的OMRp1方案，检测器计算时间为0.145秒/消息（1线程），使用4线程时可降至0.065秒/消息（约$1.02/百万消息），接收方解码总时间仅20毫秒，摘要通信开销为1.13字节/消息。相比之下，FMD检索方案（假阳性率$2^{-5}$或$2^{-8}$）的接收方解码时间为0.29-2.1秒，摘要通信开销为5.3-42字节/消息；PS方案受限于SGX或不共谋服务器假设。在扩展性测试中（图2），当N从$10^3$增长至$10^8$，OMRp1的摘要和接收方计算时间增长缓慢，在$N\approx 8\times10^6$后，紧凑型OMRp2方案的摘要尺寸甚至低于1比特/消息，显示出优越的扩展性。检测密钥尺寸为129 MB（经优化后），可一次性发送给检测器后重复使用。

### 局限性与开放问题
检测密钥尺寸（129 MB）仍是一个实际部署障碍，虽然可一次传输，但对网络环境差的客户端不够友好。PVW线索密钥（133 KB）分发到发送方尚需基础设施支持（如Zcash的统一地址机制）。检测器的计算成本虽然绝对数值较低，但线性依赖于N，在超大规模应用（如每天数千万消息）中仍需GPU或专用硬件来进一步降低成本。方案的DoS抵抗依赖于一个未经标准规约证明的猜想（蛇眼抵抗），虽可通过添加zk-SNARK来规避，但这会引入额外的计算和通信开销。最后，检索失败时需通过另一条匿名通道发送新的检索请求，这涉及与第8章密钥不可链接性的协同设计，实际协议复杂性较高。

### 强关联论文
[4] Ali, A., et al. Communication-Computation Trade-offs in PIR. **USENIX Security 2021**

[5] Angel, S., Chen, H., Laine, K., Setty, S.T.V. PIR with Compressed Queries and Amortized Query Processing. **IEEE S&P 2018**

[7] Beck, G., Len, J., Miers, I., Green, M. Fuzzy Message Detection. **CCS 2021**

[13] Brakerski, Z. Fully Homomorphic Encryption without Modulus Switching from Classical GapSVP. **CRYPTO 2012**

[24] Fan, J., Vercauteren, F. Somewhat Practical Fully Homomorphic Encryption. **ePrint 2012/144**

[27] Grigg, J., Hopwood, D. Zcash Improvement Proposal 307: Light Client Protocol for Payment Detection. **2018**

[30] Hopwood, D., Bowe, S., Hornby, T., Wilcox, N. Zcash Protocol Specification. **2021**

[44] Madathil, V., Scafuro, A., Seres, I.A., Shlomovits, O., Varlakov, D. Private Signaling. **ePrint 2021/853**

[48] Noether, S. Ring Signature Confidential Transactions for Monero. **ePrint 2015/1098**

[54] Peikert, C., Vaikuntanathan, V., Waters, B. A Framework for Efficient and Composable Oblivious Transfer. **CRYPTO 2008**


## 关键词

+ 密码学
+ 零知识
+ 协议