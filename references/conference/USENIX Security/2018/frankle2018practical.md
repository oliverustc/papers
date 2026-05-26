---
title: "Practical accountability of secret processes"
标题简称:
论文类型: conference
会议简称: USENIX Security
发表年份: 2018
created: 2025-05-23 01:05:35
modified: 2025-05-23 01:05:55
---

## Practical accountability of secret processes

## 发表信息

+ [原文链接](https://www.usenix.org/conference/usenixsecurity18/presentation/frankie)

## 作者

+ Jonathan Frankle
+ Sunoo Park
+ Daniel Shaar
+ [Shafi Goldwasser](Shafi%20Goldwasser.md)
+ Daniel Weitzner

## 笔记

### 背景与动机
美国联邦法院系统在电子监控的司法实践中面临一个根本性困境：监控程序必须保密以保护调查免受干扰，但公众又需要能够监督权力不被滥用。法官Stephen Smith指出，电子通信隐私法管辖下的监控过程充斥着密封令和封口令，导致三个具体问题：一是密封令被法院遗忘而实际上永久封存；二是被监控目标无法得知被监控，因而没有动力也无机会对命令提出上诉，法院也“没有任何上诉指导”；三是公众和国会无法准确评估监控活动的广度与深度 [37, 38]。Smith法官提出的公开封面页提案尽管有价值，但作为一张纸质文件，它在维持调查秘密性的同时增进公众信任的能力有限。该论文旨在利用现代密码学工具，在保持监控过程必要保密性的同时，提供可配置的、量化的问责性保障，填补现有法律程序中缺乏密码学支撑的透明度和可验证性的空白。

### 相关工作

[12] Bates et al. Accountable Wiretapping--or--I Know They Can Hear You Now. **NDSS 2012** [Google Scholar](https://scholar.google.com/scholar?q=Accountable+Wiretapping+or+I+Know+They+Can+Hear+You+Now)
> 核心思路：为法庭授权的窃听添加问责性，加密所有窃听数据副本并通过日志记录供审计。
> 局限与区别：本文方案允许公众直接、部分实时地验证监控活动的正当性，而Bates等人的系统更侧重于事后审计。

[27] Kroll, Felten, and Boneh. Secure Protocols for Accountable Warrant Execution. **2014** [Google Scholar](https://scholar.google.com/scholar?q=Secure+Protocols+for+Accountable+Warrant+Execution)
> 核心思路：利用密码学确保监控参与者只在合法授权下访问数据，包含审计日志。
> 局限与区别：Kroll等方案侧重于访问控制，本文则专注于公众问责性，并开发了一个用于控制信息释放的精细框架。

[23] Goldwasser and Park. Public Accountability vs. Secret Laws: Can They Coexist?: A Cryptographic Proposal. **WPES 2017** [Google Scholar](https://scholar.google.com/scholar?q=Public+Accountability+vs.+Secret+Laws+Can+They+Coexist)
> 核心思路：使用简洁零知识证明来证明记录在案的行动与秘密司法行动的一致性，应用于FISA法庭。
> 局限与区别：本文关注于ECPA监控，涉及公司等其他参与方，并提供了实现证明实用性的评估以及聚合统计的计算。

[16] Bestavros et al. User-centric distributed solutions for privacy-preserving analytics. **Communications of the ACM 2017** [Google Scholar](https://scholar.google.com/scholar?q=User-centric+distributed+solutions+for+privacy-preserving+analytics)
> 核心思路：一个用于隐私保护分析的JavaScript MPC库WebMPC。
> 局限与区别：作为本文MPC实现的底层库之一，WebMPC功能相对简单，仅支持求和运算。

[5] Jiff. **GitHub** [Google Scholar](https://scholar.google.com/scholar?q=Jiff)
> 核心思路：另一个支持更复杂MPC功能的JavaScript库Jiff，包括阈值求和和乘法。
> 局限与区别：本文使用了Jiff实现并评估了分层MPC协议，以支持更复杂的聚合统计。

[34] SCIPR Lab. libsnark: a C++ library for zkSNARK proofs. **GitHub** [Google Scholar](https://scholar.google.com/scholar?q=libsnark+a+C%2B%2B+library+for+zkSNARK+proofs)
> 核心思路：一个用于创建通用简洁零知识证明的C++库。
> 局限与区别：本文使用LibSNARK实现了三种类型的零知识论证（知识论证、等式论证、存在性等式论证），并评估了其在监控场景下的性能。

### 核心技术与方案
本文设计的系统围绕一个公开可见的仅追加账本展开，法官、执法机构和公司均向该账本发布信息。系统利用四种核心密码学原语。第一，仅追加账本，用于记录带有可信时间戳的监控事件信息，确保数据记录的一致性和不可篡改性。第二，密码学承诺，用于证明某份信息（如法院命令）存在但暂时隐藏其内容，承诺具有隐藏性和绑定性的安全属性，公开承诺的存在即可提供一定程度的问责性，同时保护调查秘密。第三，零知识证明，使各方能向公众证明其行为与既定规则一致（例如，执法机构证明其数据请求与法官的命令兼容），而不泄露承诺内容的任何进一步信息。系统实现了三种论证类型：知识论证、等式论证、以及存在性等式论证。后者允许证明一个承诺的内容与某组承诺中的一个相匹配，从而可以降低披露信息的精度，例如不具体指明是哪个法官的命令。第四，安全多方计算（MPC）用于计算有关整个法院系统监控活动的聚合统计量（例如，“多少个法官向谷歌发出了十次以上的数据请求？”）， MPC通过一个层次化协议实现，该协议模拟了联邦法院系统的层级结构，将计算集中在十二个巡回上诉法院的服务器上。每个下级法院法官计算其个人数据份额并将其分为十二份秘密共享发送给各巡回法院服务器，然后这十二个服务器运行MPC从这些份额中计算出最终的聚合统计量。该层次化结构将MPC的复杂度从与法官数量的二次方关系降低到线性关系，并且下级法院法官可以发送完秘密份额后离线，无需保持在线。协议的安全性基于MPC的正确性和机密性保证，以及承诺方案的完美隐藏性。系统基于一个混合信任模型：法官被建模为诚实但好奇，而执法机构和公司被建模为恶意。机密性目标要求公众除公开信息外不学习其他信息，且其他参与方不能学习超过其已知的信息。

### 核心公式与流程

**秘密共享重建函数**
$$
\begin{array}{c} \text {ReconInputs} \big((\delta_ {1, i^{\prime}}, \ldots , \delta_ {n, i^{\prime}}) \big) _ {i^{\prime} \in [ r ]} = \\ \big (\text {Recon} (\delta_ {j, 1}, \ldots , \delta_ {j, r}) \big) _ {j \in [ n ]} \end{array}
$$
> 作用：定义了在层次化MPC中，由巡回法院服务器从其收到的秘密份额 $\delta_{j,i}$ 中重建出每个法官 $j$ 的原始输入的函数。

**执法机构算法（Algorithm 1）**
接收到法官批准的决策 $(u, s, d)$ 后：
1. 生成承诺 $c = \text{Commit}((s,d), \omega)$ 并存储 $(c,s,d,\omega)$。
2. 生成SNARK证明 $\pi$ 证明 $(s,d)$ 符合规定。
3. 将 $(c, \pi)$ 发布到账本。
4. 将请求 $(s,d,\omega)$ 发送给公司 $u$。
> 作用：定义了执法机构在获得法官授权后如何通过公开承诺和零知识证明来记录其行为并为公众提供可验证的问责性，同时隐藏请求的具体内容。

**法官算法（Algorithm 2）**
接收到执法机构的监控请求 $(u,s)$ 后：
1. 生成决策 $d \gets J_i^{\text{dp1}}(s)$。
2. 向执法机构 $A_j$ 发送响应 $(u,s,d)$。
3. 生成承诺 $c = \text{Commit}((u,s,d), \omega)$ 并存储 $(c,u,s,d,\omega)$。
4. 将封面信息 $\text{CoverSheet}(d)$ 和承诺 $c$ 发布到账本。
> 作用：定义了法官做出决定后如何在账本上留下可追溯的痕迹，承诺隐藏了订单的具体内容，封面信息则提供公开的元数据。

**受托管方算法（Algorithm 4）**
接收到计算聚合统计的事件后：
1. 向所有法官发送计算请求，并接收每个法官发来的秘密份额 $\delta_{j,i}$。
2. 与其他受托管方运行MPC协议计算 $\text{ReconInputs} \circ f$ 的结果 $y$。
3. 将结果 $y$ 发送给所有法官。
> 作用：描述了作为MPC核心的受托管方如何协调来自各级法官的秘密份额，并通过MPC安全地计算出聚合统计量。

### 实验结果
实验在16核CPU、64GB RAM的计算机上进行，通过将每个参与方作为一个独立进程模拟。MPC评估使用了两种JavaScript库：WebMPC（仅支持求和）和Jiff（支持求和、加性阈值、乘性阈值）。层次化MPC协议的性能显著优于平面协议。平面协议将300名法官的求和运算耗时接近8分钟，而层次化求和协议在1000名法官的规模下仅耗时不到20秒，且其运行时间与法官数量呈线性关系（相比之下平面协议呈二次增长）。对于阈值计算，层次化协议在250名法官时的运行时间与平面协议在35名法官时的运行时间相当，虽然绝对时间较长（阈值计算慢于求和），但线性扩展趋势使得其在法庭系统规模下可行。SNARK评估使用了LibSNARK库，测试了16字节到1232字节的消息。论证大小非常紧凑，仅为287字节。验证密钥大小在知识论证和等式论证下为10.6KB和20.83KB，对存在性等式论证随输入集大小线性增长（1.0MB到10.2MB）。论证生成时间从几秒到几分钟不等，而验证时间极快，对于知识论证和等式论证仅需几毫秒，对于存在性等式论证在最大输入规模下也仅需338毫秒。证明密钥较大，在数百MB到1GB左右，但考虑到其一次性生成和存储的性质，这在实践中是可接受的。

### 局限性与开放问题
该系统的核心假设是法官是诚实但好奇的，且执法机构和公司是恶意的，但这种混合信任模型可能无法完全覆盖所有现实场景，例如法官被腐败或恶意行为者渗透，或者不同参与方之间进行完全共谋。系统的安全性依赖于一个安全的公共-密钥基础设施和正确的一次性SNARK密钥生成过程，在法院系统这样一个相对封闭的环境中这或许可行，但其安全模型不如完全去中心化的系统稳健。此外，系统并未解决日志事件与真实世界事件之间的对应问题，例如，执法机构可能承诺提交一个请求但实际发送了另一个请求，这只能通过激励和举报机制来部分缓解，而非依靠密码学保证。

### 强关联论文

[12] Bates et al. Accountable Wiretapping--or--I Know They Can Hear You Now. **NDSS 2012** [Google Scholar](https://scholar.google.com/scholar?q=Accountable+Wiretapping+or+I+Know+They+Can+Hear+You+Now)

[23] Goldwasser and Park. Public Accountability vs. Secret Laws: Can They Coexist?: A Cryptographic Proposal. **WPES 2017** [Google Scholar](https://scholar.google.com/scholar?q=Public+Accountability+vs.+Secret+Laws+Can+They+Coexist)

[27] Kroll et al. Secure Protocols for Accountable Warrant Execution. **2014** [Google Scholar](https://scholar.google.com/scholar?q=Secure+Protocols+for+Accountable+Warrant+Execution)

[16] Bestavros et al. User-centric distributed solutions for privacy-preserving analytics. **Communications of the ACM 2017** [Google Scholar](https://scholar.google.com/scholar?q=User-centric+distributed+solutions+for+privacy-preserving+analytics)

[34] SCIPR Lab. libsnark: a C++ library for zkSNARK proofs. **GitHub** [Google Scholar](https://scholar.google.com/scholar?q=libsnark+a+C%2B%2B+library+for+zkSNARK+proofs)

[5] Jiff. **GitHub** [Google Scholar](https://scholar.google.com/scholar?q=Jiff)


## 关键词

+ 电子监控问责制
+ 零知识证明SNARKs
+ 多方安全计算MPC
+ 秘密信息处理框架
+ 司法保密与问责平衡
+ 分层MPC协议
