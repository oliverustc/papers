---
title: "NIZKs with an Untrusted CRS: Security in the Face of Parameter Subversion"
标题简称:
论文类型: conference
会议简称: ASIACRYPT
发表年份: 2016
modified: 2025-04-21 13:52:42
created: 2025-04-08 17:20:21
---

## NIZKs with an Untrusted CRS: Security in the Face of Parameter Subversion

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-662-53890-6_26)

## 作者

+ [Mihir Bellare](Mihir%20Bellare.md)
+ [Georg Fuchsbauer](Georg%20Fuchsbauer.md)
+ Alessandra Scafuro

## 笔记

### 背景与动机
2013年斯诺登事件揭露了大规模监控活动中对“可信”公共参数的系统性颠覆，最典型的案例是NSA设计的Dual EC随机数生成器，其公开参数P、Q被怀疑由NSA故意选择使得知晓离散对数s满足$P = s Q$者能预测输出，且该标准被强制推广至TLS等广泛使用的协议中[24]。这一现实攻击表明，密码系统依赖“由可信方诚实生成”的公共参考串（CRS）具有巨大安全隐患，因为实际中CRS可能被恶意生成并植入后门。非交互式零知识证明（NIZK）作为大量密码应用的核心组件，其安全性恰好建立在CRS必须诚实生成的假设之上，然而这一假设在参数颠覆面前完全失效。现有NIZK系统的模拟器本身就可以生成与诚实CRS不可区分的“被颠覆的”CRS并掌握陷门，这使得颠覆者可以自然地利用此特性破坏可靠性或零知识性。本文旨在填补这一空白，为NIZK在恶意CRS下的安全性建立系统的形式化定义，并全面刻画哪些安全目标的组合是可实现的，哪些是理论不可能的。

### 相关工作

[36] Goldreich, O., Oren, Y.: Definitions and properties of zero-knowledge proof systems. **J. Cryptology 1994** [Google Scholar](https://scholar.google.com/scholar?q=Definitions+and+Properties+of+Zero-Knowledge+Proof+Systems)
> 核心思路：证明了交互式零知识证明中模拟器不能存在于非平凡语言中。
> 局限与区别：该工作针对交互式系统，且其不可能性定理基于非均匀复杂性。本文将该范式扩展到NIZK的CRS颠覆场景，证明了ZK与S-SND不可兼容。

[42] Groth, J., Ostrovsky, R., Sahai, A.: Non-interactive zaps and new techniques for NIZK. **CRYPTO 2006** [Google Scholar](https://scholar.google.com/scholar?q=Non-interactive+zaps+and+new+techniques+for+NIZK)
> 核心思路：提出基于决策线性假设（DLin）的无CRS非交互式zap系统，实现完美可靠性和证人不可区分性。
> 局限与区别：该系统本身是SND和WI的，但不能满足ZK。本文利用该系统的“trivial CRS”特性证明了它自动具备S-SND和S-WI，从而以标准假设实现P2。

[32] Feige, U., Lapidot, D., Shamir, A.: Multiple non-interactive zero knowledge proofs based on a single random string. **FOCS 1990** [Google Scholar](https://scholar.google.com/scholar?q=Multiple+non-interactive+zero+knowledge+proofs+based+on+a+single+random+string)
> 核心思路：第一个在公共随机串模型下构造NIZK的系统。
> 局限与区别：该构造假设CRS诚实生成。本文在P3构造中利用其“zap可从任何NIZK构造”的结论，将PRG和zap组合，从最小假设获得SND+ZK+S-WI。

[30] Dwork, C., Naor, M.: Zaps and their applications. **FOCS 2000** [Google Scholar](https://scholar.google.com/scholar?q=Zaps+and+their+applications)
> 核心思路：提出zap这一2-move WI交互协议，其中第一轮消息不依赖待证明语句。
> 局限与区别：zap本身是交互式的且不满足ZK。本文在P3中将zap的第一轮消息作为CRS的一部分，使得在CRS被颠覆时系统仍保留S-WI。

[15] Bitansky, N., Canetti, R., Paneth, O., Rosen, A.: On the existence of extractable one-way functions. **STOC 2014** [Google Scholar](https://scholar.google.com/scholar?q=On+the+existence+of+extractable+one-way+functions)
> 核心思路：证明了在特定假设下存在可提取单向函数，从而构造2-move ZK。
> 局限与区别：该ZK构造的模拟要求在第一轮之前不能知道实例，而本文的S-ZK需要CRS提前产生、模拟器随后适应性地生成多实例证明。本文指出该构造可能被改造为S-ZK，但本文选择用KEA给出一个更简洁的自包含构造。

[39] Groth, J.: Short pairing-based non-interactive zero-knowledge arguments. **ASIACRYPT 2010** [Google Scholar](https://scholar.google.com/scholar?q=Short+pairing-based+non-interactive+zero-knowledge+arguments)
> 核心思路：在双线性群中使用知识假设构造短NIZK参数。
> 局限与区别：该系统的可靠性依赖于CRS诚实生成。本文P1中的S-ZK构造同样使用了知识假设（DH-KEA），但通过让CRS包含Diffie-Hellman元组并从颠覆者中提取其一指数作为陷门，实现了在恶意CRS下的零知识性。

[4] Barak, B., Lindell, Y., Vadhan, S.P.: Lower bounds for non-black-box zero knowledge. **FOCS 2003** [Google Scholar](https://scholar.google.com/scholar?q=Lower+bounds+for+non-black-box+zero+knowledge)
> 核心思路：证明了非黑盒零知识的下界，并讨论了2-move ZK的可能性。
> 局限与区别：该工作的2-move ZK构造依赖于Micali猜想（CS证明或两轮通用参数）。本文P1的构造独立性更强，只需群上的KEA和DLin假设，且指出即使从该工作出发，也需要额外论证才能达到S-ZK。

[42]（同前，作为zap系统引用）  
此处不再重复。

### 核心技术与方案
**1. 定义框架与不可能性结果（N）**  
论文首先形式化了六个安全概念：标准可靠性SND、证人不可区分性WI、零知识ZK，以及它们在CRS可被颠覆下的对应版本S-SND、S-WI、S-ZK。在颠覆模型中，对手A直接输出CRS（与硬币$r$关联），可存在后门。  
核心否定结果是定理1：任何同时满足ZK和S-SND的NI系统只能对应平凡NP关系。证明继承Goldreich-Oren范式：利用ZK模拟器构建一个决策程序M，该程序通过生成模拟CRS和假证明来判定实例$x$是否在语言中；若R是非平凡的，则M可以区分正负实例，这同时侵犯了S-SND（因为模拟证明是有效的假证明）。该论证的关键在于S-SND确保模拟CRS下的可靠性，使得模拟证明必须几乎总是有效，从而拒绝一个$x\in L(R)$的假证明意味着区分了模拟与真实世界，与ZK矛盾。

**2. 正面结果P1：SND + S-ZK**  
构造基于双线性群上的新假设DH-KEA：若对手输出Diffie-Hellman元组$(S_0, S_1, S_2)$满足$S_2 = S_0^{s_0} = S_1^{s_1} = g^{s_0 s_1}$，则存在提取器可从其硬币中提取$s_0$或$s_1$。CRS设为$(S_0, S_1, S_2, h)$，其中$h = g^t$。证明系统$\Pi$中，证明者针对实例x和CRS产生证明$\pi = (\boldsymbol{C}_0, \boldsymbol{C}_1, \boldsymbol{D}_0, \boldsymbol{D}_1, \zeta)$，其中$\boldsymbol{C}_0,\boldsymbol{C}_1$是$h^{\log S_0}$或$h^{\log S_1}$的线性加密（在DLin下保持隐藏），$\boldsymbol{D}_{i,j}$是与密钥一致性验证相关的交叉乘积，$\zeta$是GOS的非交互zap证明（无CRS, 完美可靠, WI）证明“要么存在w使得R(x,w)真，要么$\boldsymbol{C}_0,\boldsymbol{C}_1$加密了$h^{s_0}$或$h^{s_1}$”。  
**S-ZK论证**：给定任意CRS颠覆者X，由DH-KEA存在提取器E从X的硬币中提取一个指数$s$（$s = s_0$或$s = s_1$）。模拟器S.crs先用E提取s，然后输出CRS和伪造的硬币；S.pf用s作为陷门，直接加密$h^{s}$并用GOS的witness构造$\zeta$。模拟证明与真实证明在DLin下面不可区分：因为线性加密的隐藏性保证了$\boldsymbol{C}_0,\boldsymbol{C}_1$中的消息变化不可察觉，且GOS的WI隐藏了用的是哪一种witness。  
**SND论证**：若对手对假语句$x\notin L$输出有效证明，则由GOS的完美可靠性知$\zeta$必须保证$\boldsymbol{C}_0,\boldsymbol{C}_1$加密了$h^{\log S_0}$或$h^{\log S_1}$。构造CDH规约：随机猜测b，将CDH挑战嵌入$S_b$，利用DH-KEA的四个提取器从证明中提取$(u_{0,i}, u_{1,j})$以解密得到$h^{\log S_b}$，即CDH解。规约的成功概率约1/2。

**3. 正面结果P2：S-SND + S-WI**  
引理4指出：任何具有平凡CRS（即证明者和验证者忽略CRS输入）的NI系统，如果满足SND和WI，则自动满足S-SND和S-WI。因为颠覆者提供的CRS不被系统使用，任何针对S-SND的攻击可以直接转换成针对SND的攻击。GOS系统[42]恰好满足平凡CRS、SND和WI（在DLin假设下），因此直接得到P2。

**4. 正面结果P3：SND + ZK + S-WI**  
构造：CRS包含$\sigma \in \{0,1\}^{2\lambda}$和zap的第一轮消息$m_1$。证明为zap的第二轮消息，证明“存在$s$使得$\sigma = G(s)$或$w$使得R(x,w)真”（$G$是伪随机生成器）。  
- **SND**：由zap的可靠性和PRG值域稀疏性保证。  
- **ZK**：模拟器选择随机$s$，设$\sigma = G(s)$，从而拥有witness（PRG的前像）产生模拟证明，该过程与真实证明在PRG伪随机性和zap的WI下不可区分。  
- **S-WI**：若CRS被颠覆，无论$\sigma$的值如何，zap的WI性质依然保持。构造规约：S-WI对手A转换为zap的WI对手B；B将A输出的$(\sigma, m_1)$作为zap的第一轮消息，并用其WIProve模拟A的Prove查询，故A对$\Pi$的优势等于B对zap的优势。

**渐进复杂度**：P1的证明包含约14个群元素加上GOS的证明（大小与NP关系电路的尺寸线性）。P2与GOS相同。P3中，证明长度等于zap的证明长度（与电路的尺寸线性）。

### 核心公式与流程

**DH-KEA假设**
$$ \begin{array}{l}
\text{Game KE}_{dGG,M,E}(\lambda) \\
(p,\mathbb{G},\mathbb{G}_T,\mathbf{e},g)\leftarrow dGG(1^\lambda);\; h_0,h_1\leftarrow \$\mathbb{G};\\
r\leftarrow\$\{0,1\}^{M.rl(\lambda)};\; (S_0,S_1,S_2)\leftarrow M(1^\lambda,h_0,h_1;r);\; s\leftarrow\$ E(1^\lambda,h_0,h_1,r)\\
\text{Return }(\mathbf{e}(S_0,S_1)=\mathbf{e}(g,S_2) \land g^s\neq S_0 \land g^s\neq S_1)
\end{array} $$
> 作用：定义在双线性群上的知识假设，保证输出合法DH元组者必须知道其中一个指数。

**P1构造核心算法**
$$ \begin{array}{l}
\Pi.\text{Pg}(1^\lambda):\\
(p,\mathbb{G},\mathbb{G}_T,\mathbf{e},g)\leftarrow dGG(1^\lambda);\; t,s_0,s_1\leftarrow\$\mathbb{Z}_p;\\
h\leftarrow g^t;\; S_0\leftarrow g^{s_0};\; S_1\leftarrow g^{s_1};\; S_2\leftarrow g^{s_0 s_1};\; \text{Return } crs=(S_0,S_1,S_2,h)
\end{array} $$
> 作用：CRS包含一个DH元组$(S_0,S_1,S_2)$和随机元素$h$，用于嵌入陷门。

$$ \begin{array}{l}
\Pi.\text{P}(1^\lambda,(S_0,S_1,S_2,h),x,w):\\
\text{若}R(x,w)=\text{false}\text{则返}\bot;\;\text{若}e(S_0,S_1)\neq e(g,S_2)\text{则返}\bot;\\
C_{0,0},\ldots,C_{0,4},C_{1,2},C_{1,3},C_{1,4}\leftarrow\$\mathbb{G};\; u_0,u_1\leftarrow\$\mathbb{Z}_p;\; C_{1,0}\leftarrow g^{u_0};\; C_{1,1}\leftarrow g^{u_1};\\
\text{对于}i,j=0,1\text{做}\; D_{i,j}\leftarrow C_{0,i}^{u_j};\\
\zeta\leftarrow\$ Z.P((x,S_0,S_1,h,\boldsymbol{C}_0,\boldsymbol{C}_1),(w,\bot));\; \pi\leftarrow(\boldsymbol{C}_0,\boldsymbol{C}_1,\boldsymbol{D}_0,\boldsymbol{D}_1,\zeta);\text{ 返}\pi
\end{array} $$
> 作用：证明者使用线性加密密钥$C_{0,0}=g^{?}, C_{0,1}=g^{?}$和统一随机化的其他分量，保证密文隐藏，并计算交叉验证值$\boldsymbol{D}_{i,j}$；zap证明$\zeta$展示实例要么有witness要么密文包含陷门。

**P3构造核心算法**
$$ \begin{array}{l}
\Pi.\text{Pg}(1^\lambda):\\
\sigma\leftarrow\$\{0,1\}^{2\lambda};\; m_1\leftarrow\$ Z.V(1^\lambda);\; \text{Return } crs\leftarrow(\sigma,m_1)
\end{array} $$
$$ \begin{array}{l}
\Pi.\text{P}(1^\lambda,(\sigma,m_1),x,w):\\
m_2\leftarrow\$ Z.P(1^\lambda,(\sigma,x),(\bot,w),m_1);\; \pi\leftarrow m_2;\;\text{返}\pi
\end{array} $$
> 作用：CRS包含一个随机串$\sigma$和zap的第一轮消息$m_1$；证明为zap的第二轮消息，证明“要么$\sigma$是PRG输出，要么$x\in L(R)$”。

### 实验结果
本文是纯理论工作，不包含实验。所有结果都是定理形式（Theorems 1, 2, 3, 5, 6）和形式化构造，没有性能评测或实现数据。

### 局限性与开放问题
所有正面构造都基于非标准或较强的假设：P1需要双线性群上的新知识假设DH-KEA，该假设的复杂性尚未被充分研究；P2和P3虽然基于DLin或PRG+zap，但P2的安全级别仅保持WI而非ZK，实用性受限。此外，S-ZK定义要求模拟器能提取颠覆者的陷门，使得构造无法规避知识假设。开放问题包括：是否能从更标准的假设（如DLin alone）实现S-ZK+SND？能否构造对多个CRS同时抵抗颠覆的方案？能否将本框架扩展到更复杂的证明系统（如可提取性、模拟健全性）？

### 强关联论文

[36] Goldreich, O., Oren, Y.: Definitions and properties of zero-knowledge proof systems. **J. Cryptology 1994** [Google Scholar](https://scholar.google.com/scholar?q=Definitions+and+Properties+of+Zero-Knowledge+Proof+Systems)

[42] Groth, J., Ostrovsky, R., Sahai, A.: Non-interactive zaps and new techniques for NIZK. **CRYPTO 2006** [Google Scholar](https://scholar.google.com/scholar?q=Non-interactive+zaps+and+new+techniques+for+NIZK)

[32] Feige, U., Lapidot, D., Shamir, A.: Multiple non-interactive zero knowledge proofs based on a single random string. **FOCS 1990** [Google Scholar](https://scholar.google.com/scholar?q=Multiple+non-interactive+zero+knowledge+proofs+based+on+a+single+random+string)

[30] Dwork, C., Naor, M.: Zaps and their applications. **FOCS 2000** [Google Scholar](https://scholar.google.com/scholar?q=Zaps+and+their+applications)

[15] Bitansky, N., Canetti, R., Paneth, O., Rosen, A.: On the existence of extractable one-way functions. **STOC 2014** [Google Scholar](https://scholar.google.com/scholar?q=On+the+existence+of+extractable+one-way+functions)

[39] Groth, J.: Short pairing-based non-interactive zero-knowledge arguments. **ASIACRYPT 2010** [Google Scholar](https://scholar.google.com/scholar?q=Short+pairing-based+non-interactive+zero-knowledge+arguments)

[4] Barak, B., Lindell, Y., Vadhan, S.P.: Lower bounds for non-black-box zero knowledge. **FOCS 2003** [Google Scholar](https://scholar.google.com/scholar?q=Lower+bounds+for+non-black-box+zero+knowledge)

[26] Santis, A., Crescenzo, G., Ostrovsky, R., Persiano, G., Sahai, A.: Robust non-interactive zero knowledge. **CRYPTO 2001** [Google Scholar](https://scholar.google.com/scholar?q=Robust+non-interactive+zero+knowledge)

[44] Groth, J., Sahai, A.: Efficient non-interactive proof systems for bilinear groups. **EUROCRYPT 2008** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+non-interactive+proof+systems+for+bilinear+groups)


## 关键词

+ 非交互式零知识证明
+ 公共参考串
+ 参数破坏攻击
+ 证人不可区分性
+ 不可信CRS