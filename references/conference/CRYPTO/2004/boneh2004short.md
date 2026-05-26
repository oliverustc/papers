---
title: "Short group signatures"

标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 2004
created: 2025-05-20 03:12:28
modified: 2025-05-20 03:14:48
---

## Short group signatures

## 发表信息

+ [原文链接]()

## 作者

+ [Dan Boneh](Dan%20Boneh.md)
+ Xavier Boyen
+ [Hovav Shacham](Hovav%20Shacham.md)
## 笔记

### 背景与动机

群签名允许群体中的任何成员匿名地签署消息，而验证者仅能确认签名来自该群体，却无法识别具体签名者。在需要追溯时，可由一个指定的群管理员利用陷门打开签名、揭示签名者身份。这一特性使其在诸多场景中具有重要价值，例如可信计算中的隐私保护认证，以及美国交通部车辆安全通信（VSC）项目中对车辆广播消息的匿名认证与防篡改。在这些应用中，签名长度是硬性约束——VSC要求每个签名长度不超过250字节。然而，已有的高效群签名方案，如Ateniese等人于Crypto 2000提出的方案[2]和Camenisch等人于Crypto 2002提出的方案[12]，均基于强RSA假设，其签名长度远超此限制，难以满足短签名的应用需求。因此，本文旨在构造一种签名长度极短、能与同等安全级别的标准RSA签名长度相当的群签名方案，以填补实际部署中对短群签名的迫切需求。作者利用双线性群上的强Diffie-Hellman假设和决策线性假设，设计了一套全新的零知识证明协议，并通过Fiat-Shamir启发式将其转化为签名，最终实现了签名长度仅为192字节的群签名系统。

### 相关工作

[2] Ateniese G. et al. A practical and provably secure coalition-resistant group signature scheme. **Crypto 2000** [Google Scholar](https://scholar.google.com/scholar?q=A+practical+and+provably+secure+coalition-resistant+group+signature+scheme)
> 核心思路：基于强RSA假设，构造了第一个实用的、抗合谋攻击的群签名方案，包含用户加入协议（JOIN）以实现强不可诬陷性。
> 局限与区别：该方案的签名长度较长，无法满足VSC等应用对短签名的苛刻要求；此外，其安全证明模型与本文采用的Bellare等人[6]的模型不同。本文基于SDH假设构建的方案在签名长度上具有显著优势。

[5] Baric N. et al. Collision-free accumulators and fail-stop signature schemes without trees. **Eurocrypt 1997** [Google Scholar](https://scholar.google.com/scholar?q=Collision-free+accumulators+and+fail-stop+signature+schemes+without+trees)
> 核心思路：提出了强RSA假设，并利用其构建累加器和失败-停止签名。
> 局限与区别：强RSA假设是此前多数高效群签名的基础，但它导致签名较长。本文采用的新假设（SDH）具有类似性质，但允许构造出更短的签名。

[6] Bellare M. et al. Foundations of group signatures: Formal definitions, simplified requirements, and a construction based on general assumptions. **Eurocrypt 2003** [Google Scholar](https://scholar.google.com/scholar?q=Foundations+of+group+signatures:+Formal+definitions,+simplified+requirements,+and+a+construction+based+on+general+assumptions)
> 核心思路：给出了群签名的形式化安全定义，包括完全匿名性和完全可追溯性，并基于通用假设构造了一个方案。
> 局限与区别：该文定义的安全模型（CCA2完全匿名性）比本文采用的模型更强。本文在证明匿名性时，对模型进行了合理放宽（CPA完全匿名性），认为在实际部署中追踪权限会被严格控制，从而允许更高效的构造。

[8] Boneh D. et al. Short signatures without random oracles. **Eurocrypt 2004** [Google Scholar](https://scholar.google.com/scholar?q=Short+signatures+without+random+oracles)
> 核心思路：提出了基于SDH假设的短签名方案，无需随机预言机即可证明安全性。
> 局限与区别：该文构造的是标准签名，而非群签名。本文利用了相同的SDH假设作为核心密码学原语，但将其用于构造一个零知识证明协议，以证明对SDH问题解的拥有，从而实现了群签名。

[12] Camenisch J. et al. Dynamic accumulators and application to efficient revocation of anonymous credentials. **Crypto 2002** [Google Scholar](https://scholar.google.com/scholar?q=Dynamic+accumulators+and+application+to+efficient+revocation+of+anonymous+credentials)
> 核心思路：提出了动态累加器，并将其应用于匿名凭证的高效撤销。
> 局限与区别：该撤销机制可适用于群签名。本文在第七节展示了如何将这一撤销机制直接应用于自己的SDH群签名方案，使其支持用户撤销。

[13] Camenisch J. et al. Signature schemes and anonymous credentials from bilinear maps. **Crypto 2004** [Google Scholar](https://scholar.google.com/scholar?q=Signature+schemes+and+anonymous+credentials+from+bilinear+maps)
> 核心思路：提出了基于LRSW假设的签名方案，并附带高效的协议，用于获取和证明对已提交值的签名知识，进而派生出群签名方案。
> 局限与区别：该方案基于LRSW假设。作者指出，同样的方法论也可应用于SDH假设，从而得到一个不同的SDH群签名方案。这表明本文的SDH构造并非孤立，而是可以采用类似方法进行实现。

[16] Fiat A. et al. How to prove yourself: Practical solutions to identification and signature problems. **Crypto 1986** [Google Scholar](https://scholar.google.com/scholar?q=How+to+prove+yourself:+Practical+solutions+to+identification+and+signature+problems)
> 核心思路：提出了Fiat-Shamir启发式，可将交互式零知识证明转换为非交互式签名。
> 局限与区别：这是将交互式协议转化为数字签名的一种通用范式。本文正是利用该启发式，将设计的交互式零知识证明协议转化为一个群签名方案，并在随机预言机模型中证明其安全性。

### 核心技术与方案

本文的方案体系建立在两个核心密码学假设之上：强Diffie-Hellman（SDH）假设和决策线性假设。SDH假设保证了在给定一组$q$个SDH问题实例时，无法提取出新的有效对；决策线性假设是DDH的一种变体，它确保即使在一个DDH问题很容易求解的群中（例如双线性群），线性问题仍然困难。

系统的基础构件是一个零知识证明协议，用于证明对SDH问题解的拥有。协议的具体步骤如下。公钥包含$g_1, u, v, h \in G_1$和$g_2, w \in G_2$，其中$w = g_2^\gamma$。证明者希望证明她知道一个SDH对$(A, x)$，满足$A^{x+\gamma} = g_1$，等价于$e(A, w g_2^x) = e(g_1, g_2)$。证明者首先生成一个线性加密，选择随机数$\alpha, \beta \in \mathbb{Z}_p$，计算$T_1 \leftarrow u^\alpha$, $T_2 \leftarrow v^\beta$, $T_3 \leftarrow A h^{\alpha+\beta}$。然后，她需要证明她知道$\alpha, \beta, x, \delta_1 = x\alpha, \delta_2 = x\beta$满足五个约束等式，包括公钥和$T_1, T_2, T_3$的关系。这一证明通过标准的Schnorr类协议完成：选取盲化因子，计算承诺值，接收挑战c，计算响应值。验证者通过五个验证方程来确认证明的有效性。该协议被证明是完备的、诚实验证者零知识的（在决策线性假设下），并且是一个知识证明（存在提取器）。零知识性质允许模拟器在不知道SDH解的情况下生成不可区分的协议副本；知识提取性质允许通过重绕证明者提取出SDH解。

由此，通过Fiat-Shamir启发式，将上述交互式协议转化为一个签名方案。签名者首先执行协议的承诺阶段，然后使用目标消息M和所有承诺值（$T_1, T_2, T_3, R_1, R_2, R_3, R_4, R_5$）调用随机预言机生成挑战c。最后，计算响应值。最终签名为$\sigma \leftarrow (T_1, T_2, T_3, c, s_\alpha, s_\beta, s_x, s_{\delta_1}, s_{\delta_2})$。验证者利用签名中的c和响应值重新计算承诺值，并验证原始挑战是否等于对消息和新承诺值的哈希值。

该签名方案自然地构成了一个群签名方案。群管理员持有私钥$(\xi_1, \xi_2)$，其中$u^{\xi_1} = v^{\xi_2} = h$。当需要追踪时，群管理员可以使用此私钥解密签名中的前三个元素$(T_1, T_2, T_3)$，即计算$A = T_3 / (T_1^{\xi_1} \cdot T_2^{\xi_2})$，从而恢复出用户的身份标识A。方案的安全性在随机预言机模型下得到了证明：核心定理2证明了系统的正确性；定理3证明了CPA完全匿名性，该规约依赖于决策线性假设下线性加密的语义安全性；定理4证明了完全可追溯性，其证明基于SDH假设并使用分叉引理。从效率上看，一个签名由$G_1$中的3个元素和$\mathbb{Z}_p$中的6个元素组成，总长度为1533比特（192字节）。签名和验签的计算量都很低，签名方不需要计算配对，验证方仅需计算一个配对和几个指数运算。

### 核心公式与流程

**[协议 1：SDH零知识证明中的验证方程 (1)-(5)]**

$$u^{s_\alpha} \stackrel{?}{=} T_1^c \cdot R_1; \quad v^{s_\beta} \stackrel{?}{=} T_2^c \cdot R_2; \quad T_1^{s_x} u^{-s_{\delta_1}} \stackrel{?}{=} R_4; \quad T_2^{s_x} v^{-s_{\delta_2}} \stackrel{?}{=} R_5$$

$$e(T_3, g_2)^{s_x} \cdot e(h, w)^{-s_\alpha - s_\beta} \cdot e(h, g_2)^{-s_{\delta_1} - s_{\delta_2}} \stackrel{?}{=} \left( e(g_1, g_2) / e(T_3, w) \right)^c \cdot R_3 $$

> 作用：这五个方程构成了验证者检查证明者知识的核心。它们分别验证了与$\alpha$、$\beta$、$x$、$\delta_1$、$\delta_2$五个秘密值对应的线性约束和双线性映射约束，从而确认证明者确实知道一个满足$A^{x+\gamma}=g_1$的SDH对，而无需泄露$A, x$本身。

**[签名生成流程]**

$$c \leftarrow H(M, T_1, T_2, T_3, R_1, R_2, R_3, R_4, R_5) \in \mathbb{Z}_p$$
$$\sigma \leftarrow (T_1, T_2, T_3, c, s_\alpha, s_\beta, s_x, s_{\delta_1}, s_{\delta_2})$$
其中，$T_1 = u^\alpha$, $T_2 = v^\beta$, $T_3 = A h^{\alpha+\beta}$，$R_1, \dots, R_5$是协议1中的承诺值，$s_\alpha = r_\alpha + c\alpha$, $s_\beta = r_\beta + c\beta$, $s_x = r_x + cx$, $s_{\delta_1} = r_{\delta_1} + c\delta_1$, $s_{\delta_2} = r_{\delta_2} + c\delta_2$。

> 作用：该公式定义了签名的生成过程。它将交互式协议中的证明转换为一个非交互式签名。核心思想是使用哈希函数$H$模拟验证者的随机挑战$c$，从而使签名能够自包含（消息$M$被绑定到挑战中）。签名由线性加密的结果$(T_1, T_2, T_3)$和证明的响应值组成。

**[追踪（打开签名）流程]**

$$A = T_3 / (T_1^{\xi_1} \cdot T_2^{\xi_2})$$

> 作用：这是群管理员打开签名、揭示签名者身份的算法。其正确性依赖于：$T_1^{\xi_1} = (u^\alpha)^{\xi_1} = h^\alpha$ 且 $T_2^{\xi_2} = (v^\beta)^{\xi_2} = h^\beta$，因此 $T_3 / (T_1^{\xi_1} \cdot T_2^{\xi_2}) = A h^{\alpha+\beta} / h^{\alpha+\beta} = A$。管理员通过查找数据库中与$A$对应的用户，即可确定签名者身份。

### 实验结果

本文提出的是理论密码学构造，核心贡献在于提出了一个签名长度极短的群签名方案，因此其“实验结果”主要体现在理论上的参数选择和签名长度对比之上。方案使用由Miyaji、Nakabayashi和Takano [23]定义的特定非超奇异椭圆曲线族，将此族曲线上的群$G_1$大小设定为约$2^{170}$，每个$G_1$元素为171比特字符串。在此参数下，素数$p$为170比特。一个群签名由$G_1$中的3个元素和$\mathbb{Z}_p$中的6个元素组成，总长度为$3 \times 171 + 6 \times 170 = 1533$比特，即约192字节。论文指出，在此安全级别下，安全性与标准1024比特RSA签名（128字节）相当。这直接满足了车辆安全通信（VSC）应用中签名长度需低于250字节的硬性要求。相较于此前基于强RSA假设的方案（如方案[2]），本文在签名长度上实现了数十倍的缩减。系统性能方面，签名生成仅需8次指数运算（或多次指数运算），且不需要计算配对；验签需要6次多次指数运算和1次配对运算。研究人员可以通过预计算固定对（如$e(h,w)$）和固定基指数来进一步提升签名生成速度。

### 局限性与开放问题

尽管本文提出的方案在签名长度上取得了显著突破，但其安全证明依赖于随机预言机模型。虽然在随机预言机模型下被广泛接受，但在标准模型下构造一个同样短的群签名仍然是一个未解决的问题。此外，方案仅实现了CPA完全匿名性，这意味着不能抵抗能够自适应查询追踪预言机的攻击者（CCA2攻击）。虽然作者论证了在实际部署中追踪权限会被严格控制，但从理论上看，实现CCA2完全匿名性的短群签名仍是一个挑战。最后，本文提出的撤销机制要求未被撤销的用户更新自己的私钥，这在实际部署中可能带来同步和管理上的负担。

### 强关联论文

[2] Ateniese G. et al. A practical and provably secure coalition-resistant group signature scheme. **Crypto 2000** [Google Scholar](https://scholar.google.com/scholar?q=A+practical+and+provably+secure+coalition-resistant+group+signature+scheme)

[5] Baric N. et al. Collision-free accumulators and fail-stop signature schemes without trees. **Eurocrypt 1997** [Google Scholar](https://scholar.google.com/scholar?q=Collision-free+accumulators+and+fail-stop+signature+schemes+without+trees)

[6] Bellare M. et al. Foundations of group signatures: Formal definitions, simplified requirements, and a construction based on general assumptions. **Eurocrypt 2003** [Google Scholar](https://scholar.google.com/scholar?q=Foundations+of+group+signatures:+Formal+definitions,+simplified+requirements,+and+a+construction+based+on+general+assumptions)

[8] Boneh D. et al. Short signatures without random oracles. **Eurocrypt 2004** [Google Scholar](https://scholar.google.com/scholar?q=Short+signatures+without+random+oracles)

[12] Camenisch J. et al. Dynamic accumulators and application to efficient revocation of anonymous credentials. **Crypto 2002** [Google Scholar](https://scholar.google.com/scholar?q=Dynamic+accumulators+and+application+to+efficient+revocation+of+anonymous+credentials)

[13] Camenisch J. et al. Signature schemes and anonymous credentials from bilinear maps. **Crypto 2004** [Google Scholar](https://scholar.google.com/scholar?q=Signature+schemes+and+anonymous+credentials+from+bilinear+maps)

[16] Fiat A. et al. How to prove yourself: Practical solutions to identification and signature problems. **Crypto 1986** [Google Scholar](https://scholar.google.com/scholar?q=How+to+prove+yourself:+Practical+solutions+to+identification+and+signature+problems)

[24] Pointcheval D. et al. Security arguments for digital signatures and blind signatures. **J. Cryptology 2000** [Google Scholar](https://scholar.google.com/scholar?q=Security+arguments+for+digital+signatures+and+blind+signatures)


## 关键词

+ 短群签名方案双线性群
+ 强Diffie-Hellman判定线性假设
+ 随机预言机群签名安全证明
+ 可撤销匿名性实用群签名
+ 标准RSA大小签名群签名