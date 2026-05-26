---
title: "ATRC: An anonymous traceable and revocable credential system using blockchain for VANETs"
标题简称:
论文类型: journal
期刊简称: TVT
发表年份: 2023
created: 2025-05-20 02:27:21
modified: 2025-05-20 02:27:29
---

## ATRC: An anonymous traceable and revocable credential system using blockchain for VANETs

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/10242013)

## 作者

+ Yang Liu
+ Debiao He
+ Min Luo
+ Huaqun Wang
+ Qin Liu

## 笔记

### 背景与动机
车联网环境中，车辆用户的身份隐私泄露可能引发严重事故，因此在身份认证过程中保护隐私至关重要。传统的基于可信第三方的凭证管理系统虽能实现追踪，但存在单点故障和隐私泄露风险。分散式匿名凭证系统虽能由用户自行控制数据，但在车联网场景下面临监管难题：既要保持匿名性，又要在恶意行为发生时实现快速追踪和撤销。现有撤销方法中，验证者本地撤销（如黑/白名单）依赖于可信第三方且效率受限于列表规模，累加器撤销则要求所有用户频繁更新见证者，在车联网环境下车速快、撤销窗口期短，这些方案均不理想。本文旨在填补一种在保持匿名性的同时实现高效、隐私保护的撤销机制的空白，利用区块链作为一致性的公告板，结合群签名和Merkle树，构建一个轻量级且能安全撤销恶意车辆的系统。

### 相关工作

[5] Derler等. A new approach to efficient revocable attribute-based anonymous credentials. **IMACC 2015** [Google Scholar](https://scholar.google.com/scholar?q=A+new+approach+to+efficient+revocable+attribute-based+anonymous+credentials)
> 核心思路：基于累加器构建黑名单实现撤销，验证工作量为常数。
> 局限与区别：该方案撤销时需要更新所有未撤销用户的见证者，且黑名单可能泄露被撤销用户的身份信息。

[6] Camenisch等. An accumulator based on bilinear maps and efficient revocation for anonymous credentials. **PKC 2009** [Google Scholar](https://scholar.google.com/scholar?q=An+accumulator+based+on+bilinear+maps+and+efficient+revocation+for+anonymous+credentials)
> 核心思路：利用双线性映射构建累加器，用户需在累加器更新后自行更新见证者。
> 局限与区别：所有未撤销用户承担见证更新负担，不适用于撤销窗口极短的车联网场景。

[11] Ateniese等. A practical and provably secure coalition-resistant group signature scheme. **CRYPTO 2000** [Google Scholar](https://scholar.google.com/scholar?q=A+practical+and+provably+secure+coalition-resistant+group+signature+scheme)
> 核心思路：提出ACJT群签名方案，成员伪名可本地生成，管理员可追踪签名者。
> 局限与区别：原方案未内置撤销机制，本文在其基础上扩展了Merkle树白名单实现匿名撤销。

[12] Garman等. Decentralized anonymous credentials. **NDSS 2014** [Google Scholar](https://scholar.google.com/scholar?q=Decentralized+anonymous+credentials)
> 核心思路：提出分散式匿名凭证框架，无单一发行方，用户本地生成凭证。
> 局限与区别：该框架未设计撤销功能，本文扩展其流程并加入可撤销的Merkle树白名单。

[13] Chaum. Security without identification: Transaction systems to make big brother obsolete. **Communications of the ACM 1985** [Google Scholar](https://scholar.google.com/scholar?q=Security+without+identification)
> 核心思路：首次提出匿名凭证概念，允许用户在不暴露身份的情况下证明属性。
> 局限与区别：粒度较粗，无法支持细粒度属性和高效撤销。

[14] Camenisch & Lysyanskaya. Signature schemes and anonymous credentials from bilinear maps. **CRYPTO 2004** [Google Scholar](https://scholar.google.com/scholar?q=Signature+schemes+and+anonymous+credentials+from+bilinear+maps)
> 核心思路：提出基于双线性映射的可构造匿名凭证的签名方案。
> 局限与区别：计算开销较大，未针对车联网的高动态性和低延迟需求优化。

### 核心技术与方案

本文提出的ATRC系统包含四个实体：车辆用户、管理权威MA、路侧单元RSU和区块链。MA作为群管理员，负责系统参数设定、成员注册、追踪和撤销；车辆用户本地生成伪名和凭证；RSU负责验证身份并提供道路信息；区块链作为不可篡改的公告板，存储伪名、凭证及撤销白名单的Merkle根。

系统核心分为伪名模块和凭证模块。伪名模块基于ACJT群签名[11]构建：系统参数$params=(n,a,a_0,g,h,y)$由MA生成，其中$n=pq$，$p=2p'+1, q=2q'+1$，$p',q'$为素数；$a,a_0,g,h\in\mathbb{QR}_n$；$y=g^x \mod n$，私钥$secretkey=(p',q',x)$。用户注册后获得私钥$sk=x_i$和证书$cert=(A_i,e_i)$，其中$A_i=(a^{x_i}a_0)^{1/e_i}\mod n$，$e_i$为素数。用户生成伪名$pdn_i=(T_1,T_2,T_3,\pi_p)$：$T_1=A_i y^w$，$T_2=g^w$，$T_3=g^{e_i}h^w$，$w$随机。$\pi_p$是零知识证明，证明用户知道$(w,e_i,A_i,x_i)$满足这些关系，可通过Sigma协议和Fiat-Shamir变换实现为$(c_p,s_1,s_2,s_3,s_4)$。验证者通过计算$R_1'=a_0^{c_p}T_1^{s_1}/(a^{s_2}y^{s_3})$等四式并检查哈希一致性完成验证。MA可通过$A_i=T_1/(T_2^x)$打开伪名。

凭证模块借鉴DAC框架[12]。用户选择属性$attrs=(attr_0,...,attr_{m-1})\in\mathbb{Z}_n^m$，随机选取$w'$，计算凭证$c=h^{w'}g^{e_i}\prod_{j=0}^m g_j^{attr_j}$，并生成签名$\pi_c$证明$c$和伪名$pdn$包含相同的$e_i$。$\pi_c$同样可通过Sigma协议实现。在Show阶段，用户需证明其属性满足RSU要求且未被撤销：提供Merkle树路径和零知识证明$\pi_s$，证明$c$包含所需属性集$\{ra\}$。RSU从区块链获取$c$和伪名，验证路径有效性及$\pi_s$正确性。

撤销机制核心是Merkle树白名单。MA以$leaf_i=Hash(g^{e_i}h^w \| Version)$为叶节点构建Merkle树，根哈希上传至区块链。被撤销用户的叶节点被移除，树更新后MA上传新根。用户Show时必须提供有效路径证明其叶节点仍在树中，这实现了匿名的成员资格验证。与累加器方案不同，未撤销用户无需任何更新操作，撤销的隐私性和效率得到兼顾。

安全性方面，系统满足匿名性（伪名和凭证不泄露身份）、不可伪造性（基于ACJT方案的不可伪造性归约）、可追踪性（MA可通过私钥打开伪名）以及签名知识证的安全性（证明满足完备性、特殊可靠性、诚实验证者零知识）。系统渐进复杂度：伪名生成和验证各需约4次模指数运算，凭证生成和验证各需约2次模指数运算，Show阶段需约$m+2$次模指数运算（$m$为暴露属性数），验证类似。撤销操作仅MA需更新Merkle树，用户端开销为零。

### 核心公式与流程

**[PDN.Gen伪名生成]**
$$T_1 = A_i y^w \mod n,\quad T_2 = g^w \mod n,\quad T_3 = g^{e_i}h^w \mod n$$
$$R_1 = \frac{T_1^{r_1}}{a^{r_2}y^{r_3}},\quad R_2 = \frac{T_2^{r_1}}{g^{r_3}},\quad R_3 = g^{r_4},\quad R_4 = g^{r_1}h^{r_4}$$
$$c_p = \text{hash}(g||h||y||a_0||a||T_1||T_2||T_3||R_1||R_2||R_3||R_4)$$
$$s_1 = r_1 - c_p e_i,\; s_2 = r_2 - c_p x_i,\; s_3 = r_3 - c_p e_i w,\; s_4 = r_4 - c_p w$$
> 作用：车辆用户本地生成伪名$(T_1,T_2,T_3,\pi_p)$，$\pi_p=(c_p,s_1,s_2,s_3,s_4)$是对证书知识的零知识证明。

**[PDN.Verf伪名验证]**
$$R_1' = \frac{a_0^{c_p} T_1^{s_1}}{a^{s_2}y^{s_3}},\quad R_2' = \frac{T_2^{s_1}}{g^{s_3}},\quad R_3' = T_2^{c_p}g^{s_4},\quad R_4' = T_3^{c_p}g^{s_1}h^{s_4}$$
检查 $c_p = \text{hash}(g||h||y||a_0||a||T_1||T_2||T_3||R_1'||R_2'||R_3'||R_4')$ 是否成立。
> 作用：任何人可验证伪名的合法性，无需知道用户真实身份。

**[Cred.Form凭证生成]**
$$c = h^{w'} g^{e_i} \prod_{j=0}^m g_j^{attr_j}$$
$$\pi_c = \text{SoK}[aux]\{(w, e_i, w'): T_3=g^{e_i}h^w \wedge c = h^{w'}g^{e_i}\prod g_j^{attr_j}\}$$
> 作用：用户本地生成凭证$c$和知识签名$\pi_c$，证明凭证与伪名绑定同一$e_i$，并包含属性集$attrs$。

**[Cred.Show凭证展示]**
$$\pi_s = \text{SoK}\{(w, e_i, \{ra\}): c = h^w g^{e_i} \prod_{i\in\{ra\}} g_i^{ra_i} \prod_{j\in\{attr\}\setminus\{ra\}} g_j^{attr_j}\}$$
> 作用：用户向RSU证明所需属性集$\{ra\}$隐藏在凭证$c$中，并附带Merkle路径证明未被撤销。

### 实验结果

实验在配备Intel i7-7700 CPU、8GB内存的Windows 10机器上使用MIRACL库运行，128位安全级别，各运算取1000次执行平均值。使用ns2工具模拟车联网环境，车辆以30km/h速度行驶。实验一固定70辆车，变化RSU数量（2-16个）：平均延迟约0.1秒，波动较小，表明协议处理而非通信拥塞是主要延迟因素；RSU丢包率随数量增加呈下降趋势（约7%-14%），计算压力得到缓解。实验二固定16个RSU，变化车辆数（70-250辆）：平均延迟从约0.11秒升至0.17秒；车辆丢包率从2%飙升至39.23%，RSU丢包率从7.22%升至55.34%。当车辆数超过120时各项指标显著增加，表明系统在该配置下（16 RSU，30km/h）的瓶颈约为120辆车。结果显示本文方案在Show和撤销阶段的用户端计算轻量（伪名生成与验证约4次模指数），撤销操作由MA承担，用户无更新负担，整体在中小规模场景下性能可接受。

### 局限性与开放问题
系统依赖MA作为可信第三方，若MA被攻破则隐私与安全性丧失，未来可探索完全去中心化的群管理方案。Merkle树撤销虽避免了用户更新负担，但每次撤销后MA需重新计算根哈希并上链，在撤销频繁时区块链上存储和验证的延迟可能成为瓶颈。车辆数超过120时性能急剧下降，表明协议扩展性有限，需研究更高效的轻量级群签名或分层网络结构以支持大规模部署。此外，当前实验仅使用仿真环境，真实道路场景中的网络延迟和丢包特性可能使结果偏离。

### 强关联论文

[11] Ateniese G, Camenisch J, Joye M, et al. A practical and provably secure coalition-resistant group signature scheme. **CRYPTO 2000** [Google Scholar](https://scholar.google.com/scholar?q=A+practical+and+provably+secure+coalition-resistant+group+signature+scheme)

[12] Garman C, Green M, Miers I. Decentralized anonymous credentials. **NDSS 2014** [Google Scholar](https://scholar.google.com/scholar?q=Decentralized+anonymous+credentials)

[5] Derler D, Hanser C, Slamanig D. A new approach to efficient revocable attribute-based anonymous credentials. **IMACC 2015** [Google Scholar](https://scholar.google.com/scholar?q=A+new+approach+to+efficient+revocable+attribute-based+anonymous+credentials)

[6] Camenisch J, Kohlweiss M, Soriente C. An accumulator based on bilinear maps and efficient revocation for anonymous credentials. **PKC 2009** [Google Scholar](https://scholar.google.com/scholar?q=An+accumulator+based+on+bilinear+maps+and+efficient+revocation+for+anonymous+credentials)

[14] Camenisch J, Lysyanskaya A. Signature schemes and anonymous credentials from bilinear maps. **CRYPTO 2004** [Google Scholar](https://scholar.google.com/scholar?q=Signature+schemes+and+anonymous+credentials+from+bilinear+maps)

[22] Sonnino A, Al-Bassam M, Bano S, et al. Coconut: Threshold issuance selective disclosure credentials with applications to distributed ledgers. **NDSS 2019** [Google Scholar](https://scholar.google.com/scholar?q=Coconut+Threshold+issuance+selective+disclosure+credentials+with+applications+to+distributed+ledgers)

[4] Yang Y, Cai H, Wei Z, et al. Towards lightweight anonymous entity authentication for IoT applications. **ACISP 2016** [Google Scholar](https://scholar.google.com/scholar?q=Towards+lightweight+anonymous+entity+authentication+for+IoT+applications)

[25] Cui J, Ouyang F, Ying Z, et al. Secure and efficient data sharing among vehicles based on consortium blockchain. **IEEE TITS 2022** [Google Scholar](https://scholar.google.com/scholar?q=Secure+and+efficient+data+sharing+among+vehicles+based+on+consortium+blockchain)


## 关键词

+ ATRC区块链匿名可追踪凭证
+ 去中心化匿名凭证VANETs
+ 广义群签名匿名性追踪性
+ Merkle树白名单撤销机制
+ 车联网隐私身份管理
+ 轻量级用户端凭证展示