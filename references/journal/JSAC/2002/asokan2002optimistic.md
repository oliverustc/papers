---
title: "Optimistic fair exchange of digital signatures"
标题简称:
论文类型: journal
期刊简称: JSAC
发表年份: 2002
---

## Optimistic fair exchange of digital signatures

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/839935)

## 作者

+ N. Asokan 
+ V. Shoup 
+ M. Waidner

## 笔记

### 背景与动机
随着互联网上商务活动的日益增长，如何公平地交换数字签名（如电子支票与电子机票）成为一个关键问题。公平意味着要么双方都获得对方的签名，要么双方都得不到，避免一方在收到物品后违约。最直接的解决方案是引入一个在线可信第三方作为中介，但这种方法会给第三方带来巨大的负载和成本，并成为潜在的性能瓶颈和单点故障点。本文旨在设计一种“乐观”的公平交换协议，其核心思想是仅在出现欺诈或一方崩溃的情况下才需要第三方介入；在绝大多数正常交易中，双方可直接完成交换。该协议不仅极大地减轻了第三方负担，还解决了以往乐观协议中一个严重但常被忽视的问题：无法保证及时终止。在之前的方案中，一方可能在等待对方响应或向第三方求助时被无限期“挂起”，尤其是在异步网络中。本文通过引入一个非可验证的托管作为关键中间步骤，使得任何一方都能通过单方面联系第三方来强制公平、及时地终止协议，无需依赖同步时钟。

### 相关工作

[1] Asokan, N., Schunter, M., and Waidner, M. Optimistic protocols for fair exchange. **ACM CCS 1997** [Google Scholar](https://scholar.google.com/scholar?q=Optimistic+protocols+for+fair+exchange+Asokan+Schunter+Waidner)
> 核心思路：提出了乐观公平交换的概念，协议中第三方仅在出现问题时介入。
> 局限与区别：该文及后续相关工作[3], [11], [31]均存在“挂起”问题，即一方可能在等待对方响应时被无限期延迟，无法单方面强制终止。本文通过引入非可验证托管和更精细的协议逻辑解决了此问题。

[3] Bao, F., Deng, R. H., and Mao, W. Efficient and practical fair exchange protocols with off-line TTP. **IEEE S&P 1998** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+and+practical+fair+exchange+protocols+with+off-line+TTP+Bao+Deng+Mao)
> 核心思路：使用Stadler的基于“双层幂”的可验证加密方案实现公平交换。
> 局限与区别：本文指出Stadler的方案[41]仅提供弱语义安全（仅保证无法计算离散对数），不足以作为安全托管方案，且要求所有参与者在同一群中工作，缺乏异构性。本文的构造基于更强的安全概念（抗选择密文攻击）。

[5] Bellare, M. and Goldwasser, S. Encapsulated Key Escrow. **1996** [Google Scholar](https://scholar.google.com/scholar?q=Encapsulated+Key+Escrow+Bellare+Goldwasser)
> 核心思路：提出了一种可验证地托管同态原象的方法，与本文使用的“切割-选择”方法相似。
> 局豁与区别：本文的方法独立于该工作，但技术路线类似，都利用了同态性质。

[7] Bellare, M. and Rogaway, P. Optimal asymmetric encryption. **Crypto 1994** [Google Scholar](https://scholar.google.com/scholar?q=Optimal+asymmetric+encryption+Bellare+Rogaway)
> 核心思路：提出了OAEP加密方案，在随机预言机模型下可证明安全。
> 局限与区别：本文将其用作构造安全托管方案（Section V）的基础加密原语。

[16] Cramer, R. and Shoup, V. A practical public key cryptosystem provably secure against adaptive chosen ciphertext attack. **Crypto 1998** [Google Scholar](https://scholar.google.com/scholar?q=A+practical+public+key+cryptosystem+provably+secure+against+adaptive+chosen+ciphertext+attack+Cramer+Shoup)
> 核心思路：提出了一个实用的、无需随机预言机模型即可证明抗选择密文攻击的加密方案。
> 局限与区别：本文指出该方案可作为构建安全托管方案的备选，比OAEP稍低效但无需随机预言机假设。

[31] Micali, S. Certified e-mail with invisible post offices. **1997 RSA Security Conf 1997** [Google Scholar](https://scholar.google.com/scholar?q=Certified+e-mail+with+invisible+post+offices+Micali)
> 核心思路：提出了一个乐观的认证电子邮件协议。
> 局限与区别：本文指出该协议同样未能解决“挂起”问题。

### 核心技术与方案
本文提出的乐观公平交换协议由几个关键模块构成，其核心在于将签名交换问题分解为同态原象的托管和可验证托管。

**1. 签名到同态原象的约简**：首先，协议并非直接交换原始签名，而是将交换的“承诺”约简为对一个同态前像的承诺。例如，对于Schnorr签名$(c, z)$，通过$\theta(z) = g^z = u$，将签名承诺转化为求离散对数$z$的问题。对于其他签名方案如RSA、DSS、Fiat-Shamir等，也设计了具体的约简算法，使得只要从约简输出中恢复了同态前像$s$，就能恢复出原始签名。该约简方案需要满足完备性、可靠性和保密性（即不泄露签名信息）。

**2. 安全托管方案**：协议需要一个普通的（非可验证）托管方案，以及一个可验证的托管方案。普通托管用于玩家A在协议第一步发送其签名的加密。可验证托管用于玩家B在第二步证明其加密中包含正确的同态前像。关键在于，托管方案必须是“安全”的，即抗选择密文攻击（CCA安全）。这是因为对手可能通过向解密预言机提交密文来破坏协议。一个简单的构造是利用CCA安全的加密方案（如OAEP），并将条件$\kappa$的哈希值$H(\kappa)$与消息$m$一同加密：$\psi = E(PK, t, (m, H(\kappa)))$。解密时，若明文中的哈希值与提供的条件匹配，则返回消息$m$；否则返回错误。这确保了条件不可篡改地绑定到密文上。

**3. 可验证托管同态原象**：该模块是协议的核心，允许玩家B向玩家A证明其加密的密文$\psi$中确实包含一个给定同态$\theta$和值$d$的原像$s$，同时不泄露任何关于$s$的信息。构造采用“切割-选择”协议，安全性依赖于随机预言机模型。协议步骤V如下：
- V1: 证明者$P$（B）随机选择$N$个随机串$r_i$，计算$(t_i, s'_i) = H_1(r_i)$，加密$\psi_i = E(PK, t_i, s'_i, \kappa)$，计算$h_i = (\psi_i, \theta(s'_i))$，并发送承诺$h = H_2(h_1, ..., h_N)$给验证者$V$（A）。
- V2: $V$选择随机位$b_1, ..., b_N$（不全为零）发送给$P$。
- V3: $P$根据$b_i$值回复：若$b_i=0$，则回复$r_i$；若$b_i=1$，则回复$(\psi_i, s'_i + s)$。
- V4: $V$检查承诺$h$。若$b_i=0$，解密$\psi_i$并验证；若$b_i=1$，验证$\theta(s'_i + s) = \theta(s'_i) + d$。若全部通过，则接受，并输出一个包含$d$和所有回应$b_i=1$的密文及$s'_i + s$的字符串$\alpha$。

**安全性直觉**：
- **完备性**：若双方诚实，协议成功。
- **可靠性**：对手若在加密中放入“垃圾”，则可能被“切中”，概率为$2^{-N}$。
- **零知识**：利用了“即插即用”的强零知识性质。这通过模拟器控制随机预言机实现：模拟器先发送一个随机承诺，收到挑战$b_i$后，再“反补”预言机$H_2$使其匹配。对于$b_i=1$，模拟器可随机选择$s'_i$（非真实原像）并生成假密文。由于真实的托管密文从未被解密（条件$\kappa$一致），基于底层托管方案的CCA安全性，对手无法区分模拟与现实。

**公平交换主协议**：协议流程（以A先动为例）：
1.  A将他的签名$\sigma_A$用协议-托管（非可验证）加密，加密条件包含他收到的B的公钥等信息和一个一次性密钥$v = f(r)$。他将密文$\alpha$和$v$发送给B。
2.  B验证后，与A运行子协议V，将自己的签名$\sigma_B$的同态原像$s_B$进行可验证托管，条件中包含$\alpha$和$v$。B发送可验证托管结果$\beta$给A。
3.  A验证$\beta$后发送原始签名$\sigma_A$给B。
4.  B验证$\sigma_A$后发送$s_B$给A。若任一步骤失败，玩家需调用中止或解决子协议与第三方T交互。

**计算与通信量**：以离散对数实现为例，假设安全参数$N=40$，通信量约3-4KB。双方各需约40次160位指数运算，利用预处理技术可降至约1000-2000次模乘。

### 核心公式与流程

**[可验证托管协议的核心验证步骤]**
$$ \tilde{h} = H_2(h_1, \ldots, h_N) $$
$$ \text{其中，若 } b_i = 0, h_i = (\psi_i, \theta(s'_i)), \text{且 } \psi_i = E(PK, t_i, s'_i, \kappa), (t_i, s'_i) = H_1(r_i) $$
$$ \text{若 } b_i = 1, h_i = (\psi_i, \theta(s_i'') - d), \text{且 } s_i'' = s_i' + s $$
> 作用：该公式是验证者$V$检查证明者$P$承诺一致性的核心。通过对比计算出的$\tilde{h}$与收到的$h$，验证者确保证明者的回应与其初始承诺一致，从而确保被托管内容的正确性。

**[解决协议A (Resolve-A) ]**
Player A sends $r, \theta_B, d_B$ to T.
T: let $v = f(r)$
if $(v) \in S$ then send "error"
else if $(v, \theta_B, d_B, s_B) \in S$ then send $s_B$ to A
else add $(v)$ to S, send "exchange aborted"
> 作用：为玩家A提供强制终止途径。若A已发送第一次托管但未收到B的响应，可调用此协议。如果交易已被B解决，T会返回$s_B$；否则T记录中止，阻止B后续解决。

**[解决协议B (Resolve-B) ]**
Player B sends $v, \alpha, PK_A, m_A, \theta_B, s_B$ to T.
T: let $d_B = \theta_B(s_B)$
if $(v) \in S$ then send "exchange aborted"
else: Decrypt $\alpha$ under condition $(v, PK_A, m_A, \theta_B, d_B)$
     Check decryption is valid signature $\sigma_A$ on $m_A$.
     If not, send "error". Else, add $(v, \theta_B, d_B, s_B)$ to S, send $\sigma_A$ to B.
> 作用：为玩家B提供强制终止途径。若B已发送可验证托管但未收到A的原始签名，可调用此协议。B直接向T提供其签名的同态原像$s_B$，T验证后从A的托管中解密出$\sigma_A$给B。

### 实验结果
本文未提供实验性数据，但给出了基于典型参数的性能估算。例如，对于可验证托管离散对数的实现（取$N=40$），预期数据传输量为3-4KB。计算方面，双方各需约40次160位模指数运算，结合Lim-Lee的预计算技术，可降至约1000-2000次模乘。若一方基数固定，则可进一步降至约1000次模乘。对于RSA原象的可验证托管（$e=3$），计算量更小，每方所需模乘不超过160次。作者强调协议在通信轮次和数据量上都是实用的。

### 局限性与开放问题
协议的安全性在随机预言机模型下证明，是一种启发式证明，实际中可能存在被攻破的风险。作者提出两个未来方向：一是寻找比“切割-选择”更高效的可验证托管方法，即使不那么通用或安全，但效率更高也有研究价值；二是设计并实现一个实际的分布式、容错的第三方系统以消除单点故障，这需要进一步修改协议，并集成CCA安全的阈值解密和签名方案。

### 强关联论文

[1] Asokan, N., Schunter, M., and Waidner, M. Optimistic protocols for fair exchange. **ACM CCS 1997** [Google Scholar](https://scholar.google.com/scholar?q=Optimistic+protocols+for+fair+exchange+Asokan+Schunter+Waidner)

[3] Bao, F., Deng, R. H., and Mao, W. Efficient and practical fair exchange protocols with off-line TTP. **IEEE S&P 1998** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+and+practical+fair+exchange+protocols+with+off-line+TTP+Bao+Deng+Mao)

[5] Bellare, M. and Goldwasser, S. Encapsulated Key Escrow. **1996** [Google Scholar](https://scholar.google.com/scholar?q=Encapsulated+Key+Escrow+Bellare+Goldwasser)

[7] Bellare, M. and Rogaway, P. Optimal asymmetric encryption. **Crypto 1994** [Google Scholar](https://scholar.google.com/scholar?q=Optimal+asymmetric+encryption+Bellare+Rogaway)

[9] Brands, S. Untraceable off-line cash in wallets with observers. **Crypto 1993** [Google Scholar](https://scholar.google.com/scholar?q=Untraceable+off-line+cash+in+wallets+with+observers+Brands)

[16] Cramer, R. and Shoup, V. A practical public key cryptosystem provably secure against adaptive chosen ciphertext attack. **Crypto 1998** [Google Scholar](https://scholar.google.com/scholar?q=A+practical+public+key+cryptosystem+provably+secure+against+adaptive+chosen+ciphertext+attack+Cramer+Shoup)

[31] Micali, S. Certified e-mail with invisible post offices. **1997 RSA Security Conf 1997** [Google Scholar](https://scholar.google.com/scholar?q=Certified+e-mail+with+invisible+post+offices+Micali)

[40] Shoup, V. and Gennaro, R. Securing threshold cryptosystems against chosen ciphertext attack. **Eurocrypt 1998** [Google Scholar](https://scholar.google.com/scholar?q=Securing+threshold+cryptosystems+against+chosen+ciphertext+attack+Shoup+Gennaro)

[41] Stadler, M. Publicly verifiable secret sharing. **Eurocrypt 1996** [Google Scholar](https://scholar.google.com/scholar?q=Publicly+verifiable+secret+sharing+Stadler)


## 关键词

+ 公平数字签名交换协议
+ 乐观协议设计
+ 可问责可信第三方
+ 完全异步网络公平终止
+ 合同签署协议
+ 密码学公平交换原语