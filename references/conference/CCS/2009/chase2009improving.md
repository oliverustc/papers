---
title: Improving privacy and security in multi-authority attribute-based encryption
标题简称: 
论文类型: conference
会议简称: CCS
发表年份: 2009
tags:
  - 需要调研引用文献
created: 2025-05-23 01:28:00
modified: 2025-05-23 01:28:06
---

## Improving privacy and security in multi-authority attribute-based encryption

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/1653662.1653678)

## 作者

+ [Melissa Chase](Melissa%20Chase.md)
+ [Sherman SM Chow](Sherman%20SM%20Chow.md)
## 笔记

### 背景与动机

传统属性基加密（ABE）由Sahai和Waters于2005年提出[13]，但假设单一权威机构管理所有属性，这在现实中并不合理。Chase于2007年提出多权威ABE方案[5]，引入全局标识符（GID）和可信中央权威（CA）来抵抗用户合谋。然而该方案存在两个根本性缺陷：第一，CA掌握系统主密钥并能解密所有密文，与分布式控制的初衷矛盾；第二，用户必须向每个权威机构出示相同GID，使得合谋的权威机构能够汇总所有属性信息，构建用户的完整画像，严重侵犯用户隐私。此外，Lin等人于2008年提出的方案[10]虽去除了CA，但仅能抵抗最多m个用户的合谋攻击（m需在系统初始化时固定），安全强度随用户规模线性下降。本文旨在同时解决上述两个问题——去除可信CA并保护用户隐私，同时保持对任意数量用户合谋的抵抗力。

### 相关工作

[5] Melissa Chase. Multi-authority Attribute Based Encryption. **TCC 2007** [Google Scholar](https://scholar.google.com/scholar?q=Multi-authority+Attribute+Based+Encryption)
> 核心思路：首次提出多权威ABE，利用CA和GID实现抗合谋，每个权威机构使用PRF生成用户特定份额。
> 局限与区别：CA拥有解密所有密文的能力，且GID导致用户隐私完全暴露；本文去除了CA并实现了匿名密钥颁发。

[10] Huang Lin, Zhenfu Cao, Xiaohui Liang, Jun Shao. Secure Threshold Multi Authority Attribute Based Encryption without a Central Authority. **INDOCRYPT 2008** [Google Scholar](https://scholar.google.com/scholar?q=Secure+Threshold+Multi+Authority+Attribute+Based+Encryption+without+a+Central+Authority)
> 核心思路：通过分布式密钥生成协议去除CA，但仅实现m-resilient安全性（最多抵抗m个用户合谋）。
> 局限与区别：安全性与系统参数m绑定，且m需较大才能抵抗实际攻击；本文实现的是强安全性（任意数量用户合谋仍安全）。

[11] Moni Naor, Benny Pinkas, Omer Reingold. Distributed Pseudo-random Functions and KDCs. **EUROCRYPT 1999** [Google Scholar](https://scholar.google.com/scholar?q=Distributed+Pseudo-random+Functions+and+KDCs)
> 核心思路：提出分布式PRF构造，使多个服务器能协作计算伪随机函数而无需暴露种子。
> 局限与区别：本文利用其“求和为0”的PRF构造来替代CA的功能。

[9] Stanislaw Jarecki, Xiaomin Liu. Efficient Oblivious Pseudorandom Function with Applications to Adaptive OT and Secure Computation of Set Intersection. **TCC 2009** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+Oblivious+Pseudorandom+Function+with+Applications+to+Adaptive+OT+and+Secure+Computation+of+Set+Intersection)
> 核心思路：设计高效的 oblivious PRF 协议，允许一方以隐藏输入的方式获得PRF值。
> 局限与区别：本文将其推广，构造了适用于ABE密钥的 oblivious 计算协议。

[13] Amit Sahai, Brent Waters. Fuzzy Identity-Based Encryption. **EUROCRYPT 2005** [Google Scholar](https://scholar.google.com/scholar?q=Fuzzy+Identity-Based+Encryption)
> 核心思路：提出阈值策略的ABE（即模糊IBE），使用双线性映射，安全性基于DBDH假设。
> 局限与区别：仅支持单权威阈值策略；本文将其扩展为多权威，并加入抗合谋和隐私保护。

[8] Vipul Goyal, Omkant Pandey, Amit Sahai, Brent Waters. Attribute-Based Encryption for Fine-Grained Access Control of Encrypted Data. **ACM CCS 2006** [Google Scholar](https://scholar.google.com/scholar?q=Attribute-Based+Encryption+for+Fine-Grained+Access+Control+of+Encrypted+Data)
> 核心思路：提出支持任意单调访问结构（树形）的KP-ABE。
> 局限与区别：仍为单权威；本文在扩展部分指出其树结构可移植到多权威方案中。

### 核心技术与方案

本文提出一个完整的多权威ABE系统，包含两大创新：去中心化主密钥生成和匿名密钥颁发协议。

**1. 去除可信CA：基于分布式PRF的密钥共享**

Chase方案[5]的核心问题是CA掌握所有权威机构的PRF种子和系统主密钥，从而能够解密。Waters建议的替代思路是：每对权威机构$(j,k)$预先共享一个PRF种子$s_{jk}$，并定义每个权威$k$的最终伪随机函数为
$$F_k(\text{GID}) = \sum_{j<k} \text{PRF}_{jk}(\text{GID}) - \sum_{j>k} \text{PRF}_{jk}(\text{GID})$$
其中$\text{PRF}_{jk}(u)=g_1^{x_j x_k/(s_{jk}+u)}$基于Dodis-Yampolskiy PRF [7]构造。当所有$F_k(u)$相加时，正负项互相抵消，总和为0。这样每个权威$k$不再需要CA提供的抵消值，而是独立地为用户生成密钥。只要至少有2个权威是诚实的（即攻击者控制不超过$N-2$个权威），PRF的伪随机性就能保证合谋用户无法恢复主密钥。由于PRF种子仅由一对权威共享，任何控制少于$N-2$个权威的敌手都无法区分$F_k$与随机函数。安全性证明依赖于DBDH假设和q-DDHI假设。

**2. 匿名密钥颁发协议**

为保护用户隐私，用户不应向权威暴露其GID。本文设计了一个通用的两方安全计算协议，使得用户（持有私密值$u$）和权威（持有秘密$\alpha,\beta,\gamma$）能联合计算值$(h^\alpha g^{1/(\beta+u)})^\gamma$，只有用户得到输出，权威得不到$u$，用户也得不到$\alpha,\beta,\gamma$。协议步骤如图1所示：首先通过一个算术2PC让用户和权威共同计算$x = (\beta+u)\rho_1$（$\rho_1$为用户随机数），权威得到$x$；然后权威发送$X_1 = g^{\tau/x}, X_2 = h^{\alpha\tau}$并证明知识；用户计算$Y = (X_1^{\rho_1} X_2)^{\rho_2}$并返回；最后由权威发送$Z = Y^{\gamma/\tau}$，用户恢复$D = Z^{1/\rho_2} = (h^\alpha g^{1/(\beta+u)})^\gamma$。安全性证明：对恶意权威，模拟器利用2PC模拟和零知识提取器提取$\alpha,\beta,\gamma$；对恶意用户，模拟器依赖DDH假设（因为需要隐藏权威的$x$值）来模拟交互。协议保证了输入隐私和输出正确性。

**3. 完整构造（以KP-ABE阈值策略为例）**

- **Setup**：各权威$k$选择$v_k \in \mathbb{Z}_q$，公开$Y_k = \hat{e}(g_1,g_2)^{v_k}$，共同计算$Y = \prod Y_k$。每对权威$(k,j)$共享种子$s_{kj}$，并各自选择$x_k$公开$y_k = g_1^{x_k}$。每个权威为每个属性$i$选择$t_{k,i}$，公开$T_{k,i}=g_2^{t_{k,i}}$。
- **Key Issuing**：用户与每个权威$k$执行$N-1$次匿名协议，得到$D_{kj} = g_1^{R_{kj}} \cdot \text{PRF}_{kj}(u)$或$g_1^{R_{kj}} / \text{PRF}_{kj}(u)$（取决于$k>j$或$k<j$）。权威$k$随机选择$d_k$次多项式$p_k$满足$p_k(0) = v_k - \sum_{j\neq k} R_{kj}$，并为用户属性$i$颁发$S_{k,i} = g_1^{p_k(i)/t_{k,i}}$。用户计算$D_u = \prod D_{kj} = g_1^{R_u}$（PRF项全部抵消）。
- **Encryption**：选择$s \in \mathbb{Z}_q$，输出$E_0 = m \cdot Y^s, E_1 = g_2^s, C_{k,i} = T_{k,i}^s$。
- **Decryption**：对每个权威$k$，利用$d_k$个属性配对$\hat{e}(S_{k,i}, C_{k,i}) = \hat{e}(g_1,g_2)^{s p_k(i)}$，插值得$P_k = \hat{e}(g_1,g_2)^{s(v_k - \sum_{j\neq k} R_{kj})}$。乘所有$P_k$得$Q = Y^s / \hat{e}(g_1^{R_u}, g_2^s)$，再乘$\hat{e}(D_u, E_1)$恢复$Y^s$，最后解出$m$。

**复杂度**：每个权威需存储$N-1$个种子，为用户执行$N-1$次匿名协议。用户存储$\sum_k (|\mathbb{A}_k^u|+1)$个密钥。密文大小为$O(|\mathbb{A}^C|+1)$。初始设置需$O(N^2)$通信用于PRF种子协商，但无需分布式密钥生成协议，比Lin方案[10]更具可扩展性。

### 核心公式与流程

**[分布式PRF构造]**
$$F_k(u) = \sum_{j<k} \text{PRF}_{jk}(u) - \sum_{j>k} \text{PRF}_{jk}(u)$$
其中$\text{PRF}_{jk}(u) = g_1^{x_j x_k/(s_{jk}+u)}$
> 作用：确保$\sum_{k=1}^N F_k(u)=0$，从而去除对CA的需求；只要至少2个权威诚实，$F_k$对敌手具有伪随机性。

**[匿名密钥颁发协议（图1）]**
- 步骤1：用户随机$\rho_1$，通过2PC与权威计算$x = (\beta+u)\rho_1$，权威得到$x$。
- 步骤2：权威随机$\tau$，发送$X_1 = g^{\tau/x}, X_2 = h^{\alpha\tau}$及知识证明（PoK）。
- 步骤3：用户随机$\rho_2$，计算$Y = (X_1^{\rho_1} X_2)^{\rho_2}$，发送$Y$及PoK。
- 步骤4：权威发送$Z = Y^{\gamma/\tau}$及PoK。
- 用户计算$D = Z^{1/\rho_2} = (h^\alpha g^{1/(\beta+u)})^\gamma$。
> 作用：用户获得$(h^\alpha g^{1/(\beta+u)})^\gamma$，权威不知$u$，用户不知$\alpha,\beta,\gamma$；安全性依赖DDH和零知识证明。

**[完整加密/解密关系]**
$$E_0 = m \cdot Y^s, \quad Y = \prod_k \hat{e}(g_1,g_2)^{v_k} = \hat{e}(g_1,g_2)^{\sum v_k}$$
$$P_k = \hat{e}(g_1,g_2)^{s p_k(0)} = \hat{e}(g_1,g_2)^{s(v_k - \sum_{j\neq k} R_{kj})}$$
$$Q = \prod_k P_k = Y^s / \hat{e}(g_1^{R_u}, g_2^s), \quad D_u = g_1^{R_u}$$
$$\hat{e}(D_u, E_1) \cdot Q = \hat{e}(g_1^{R_u}, g_2^s) \cdot (Y^s / \hat{e}(g_1^{R_u}, g_2^s)) = Y^s$$
$$m = E_0 / Y^s$$
> 作用：解密时用户的$D_u$（来自所有权威的匿名协议输出）恰好抵消掉密钥中的$R$盲化项，恢复出$Y^s$。

### 实验结果

本文为理论性工作，未提供实验数据，仅给出了渐进复杂度分析和与其他方案的理论对比（表1）。与Chase方案[5]相比，本文的权威密钥大小从$|\mathbb{A}_k|+1$增至$|\mathbb{A}_k|+N$（多出$N$个种子），用户密钥大小相同（$|\mathbb{A}^u|+1$），密文大小相同（$|\mathbb{A}^C|+1$）。与Lin方案[10]相比，本文无需分布式密钥生成（0次DKG实例），而Lin方案需要$m+2$次；安全容限方面，本文可容忍至多$N-2$个腐败权威，Lin方案仅$m$个腐败用户。由于$m$通常需大于$N$才能与本文的安全强度匹配，本文在较大$N$下效率更优。匿名密钥颁发协议引入$O(N^2)$次2PC调用（每个用户每个权威需$N-1$次），但通过将属性相关的密钥生成与用户秘密解耦，使得交互次数与属性数量无关，实际效率可接受。

### 局限性与开放问题

本文方案要求每对权威机构之间预先共享PRF种子，导致初始设置阶段需要$O(N^2)$次安全交互和存储，当权威数量N很大时通信开销和存储需求较高。匿名密钥颁发协议依赖通用2PC和零知识证明，实际实现中可能计算负担较大，尤其是每个用户每次密钥请求需执行$N-1$次协议。此外，方案仅支持KP-ABE的阈值策略和树形策略，未扩展到CP-ABE或非单调访问结构，这些场景需要更强的数学假设和不同的技术路线。寻找更高效的分布式PRF构造（如线性交互量）或更简洁的匿名密钥颁发协议是未来的开放方向。

### 强关联论文

[5] Melissa Chase. Multi-authority Attribute Based Encryption. **TCC 2007** [Google Scholar](https://scholar.google.com/scholar?q=Multi-authority+Attribute+Based+Encryption)

[10] Huang Lin, Zhenfu Cao, Xiaohui Liang, Jun Shao. Secure Threshold Multi Authority Attribute Based Encryption without a Central Authority. **INDOCRYPT 2008** [Google Scholar](https://scholar.google.com/scholar?q=Secure+Threshold+Multi+Authority+Attribute+Based+Encryption+without+a+Central+Authority)

[11] Moni Naor, Benny Pinkas, Omer Reingold. Distributed Pseudo-random Functions and KDCs. **EUROCRYPT 1999** [Google Scholar](https://scholar.google.com/scholar?q=Distributed+Pseudo-random+Functions+and+KDCs)

[9] Stanislaw Jarecki, Xiaomin Liu. Efficient Oblivious Pseudorandom Function with Applications to Adaptive OT and Secure Computation of Set Intersection. **TCC 2009** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+Oblivious+Pseudorandom+Function+with+Applications+to+Adaptive+OT+and+Secure+Computation+of+Set+Intersection)

[13] Amit Sahai, Brent Waters. Fuzzy Identity-Based Encryption. **EUROCRYPT 2005** [Google Scholar](https://scholar.google.com/scholar?q=Fuzzy+Identity-Based+Encryption)

[8] Vipul Goyal, Omkant Pandey, Amit Sahai, Brent Waters. Attribute-Based Encryption for Fine-Grained Access Control of Encrypted Data. **ACM CCS 2006** [Google Scholar](https://scholar.google.com/scholar?q=Attribute-Based+Encryption+for+Fine-Grained+Access+Control+of+Encrypted+Data)

[7] Yevgeniy Dodis, Aleksandr Yampolskiy. A Verifiable Random Function with Short Proofs and Keys. **Public Key Cryptography 2005** [Google Scholar](https://scholar.google.com/scholar?q=A+Verifiable+Random+Function+with+Short+Proofs+and+Keys)


## 关键词

+ 多权威属性基加密
+ 隐私保护
+ 属性加密
+ 访问控制
+ 密码学原语