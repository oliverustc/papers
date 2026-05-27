---
title: "Membership privacy for fully dynamic group signatures"
doi: 10.1145/3319535.3354257
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2019
created: 2025-05-09 14:51:29
modified: 2025-05-09 14:52:26
---
## Membership privacy for fully dynamic group signatures

## 发表信息

+ [原文链接](https://dl.acm.org/doi/10.1145/3319535.3354257)

## 作者

+ Michael Backes
+ [Lucjan Hanzlik](Lucjan%20Hanzlik.md)
+ Jonas Schneider-Bensch

## 笔记

好的，作为一名密码学领域的研究助手，我将严格根据您提供的论文全文，按照指定格式输出详尽的结构化笔记。

### 背景与动机
群签名允许群成员代表整个群签名，同时隐藏具体签名者的身份，仅在必要时可由指定打开者追踪。现有最具有表现力的安全模型，即完全动态群签名模型，支持成员的动态加入与撤销，并通过发布 epoch 信息来更新群组状态。然而，现有模型及构造（如 [17, 18]）存在一个关键隐私缺陷：epoch 信息（如活跃成员列表）是公开验证签名所必需的，这直接泄露了哪些用户是当前群组成员。在许多应用中，如基于居住地的资源访问控制、企业部门间的匿名访问控制或私人俱乐部成员认证，成员身份本身就是极高敏感的信息，其泄露可能导致针对性攻击、身份追踪或社会性迫害。因此，完全动态群签名需要一种形式化的成员隐私保护机制，确保外部观察者无法得知在某个 epoch 谁加入或离开了群组，即使该观察者控制了部分群成员。

### 相关工作

[1] Bootle, J. et al. Foundations of Fully Dynamic Group Signatures. **ACNS 2016** [Google Scholar](https://scholar.google.com/scholar?q=Foundations+of+Fully+Dynamic+Group+Signatures)
> 核心思路：建立了完全动态群签名的形式化安全模型，支持成员添加、撤销以及恶意密钥攻击。
> 局限与区别：其模型及基于问责环签名的实例化中，epoch 信息包含活跃成员列表，这是本文所定义的成员隐私问题的直接根源。本文在其模型基础之上，扩展了成员隐私的新安全属性。

[2] Backes, M. et al. Signatures with Flexible Public Key: Introducing Equivalence Classes for Public Keys. **ASIACRYPT 2018** [Google Scholar](https://scholar.google.com/scholar?q=Signatures+with+Flexible+Public+Key+Introducing+Equivalence+Classes+for+Public+Keys)
> 核心思路：引入 SFPK，允许签名者在不泄露原始密钥类的情况下随机化自己的密钥对，并基于该原语构建了静态群签名。
> 局限与区别：该构造仅适用于静态模型，且其定义中识别等价类需要陷门。本文为了支持动态环境和公开的身份识别（打开签名），提出了“典范代表”的概念，并改进了 SFPK 的类隐藏定义以适应更弱的攻击模型（仅泄露密钥而非随机数）。

[3] Hanser, C. and Slamanig, D. Structure-Preserving Signatures on Equivalence Classes and Their Application to Anonymous Credentials. **ASIACRYPT 2014** [Google Scholar](https://scholar.google.com/scholar?q=Structure-Preserving+Signatures+on+Equivalence+Classes+and+Their+Application+to+Anonymous+Credentials)
> 核心思路：引入 SPS-EQ，允许签名者签署整个等价类，并可将签名公开地随机化为该类的其他代表。
> 局限与区别：本文利用 SPS-EQ 为每个 epoch 颁发可随机化的成员证书，并结合 SFPK，使得成员既可以对证书进行随机化，也可以对其密钥对进行随机化，从而在不泄露身份的前提下生成可验证签名。

[4] Libert, B. et al. Short Group Signatures via Structure-Preserving Signatures: Standard Model Security from Simple Assumptions. **CRYPTO 2015** [Google Scholar](https://scholar.google.com/scholar?q=Short+Group+Signatures+via+Structure-Preserving+Signatures+Standard+Model+Security+from+Simple+Assumptions)
> 核心思路：提出了在标准模型下基于简单假设的短群签名方案，安全性仅达静态或部分动态模型。
> 局限与区别：本文目标是构建具有成员隐私的完全动态群签名。实验部分对比显示，本文的优化实例化即使在添加了更强的隐私属性后，签名长度仍短于该工作，证明了本文的隐私定义在现代标准模型下无需额外开销。

[5] Boneh, D. et al. Short Group Signatures. **CRYPTO 2004** [Google Scholar](https://scholar.google.com/scholar?q=Short+Group+Signatures)
> 核心思路：提出了基于 q-type 假设的短群签名方案，效率高但安全性基于随机谕言模型。
> 局限与区别：本文的目标是标准模型下的构造，且支持完全动态和成员隐私，避免了随机谕言模型。

[6] Derler, D. and Slamanig, D. Highly-Efficient Fully-Anonymous Dynamic Group Signatures. **AsiaCCS 2018** [Google Scholar](https://scholar.google.com/scholar?q=Highly-Efficient+Fully-Anonymous+Dynamic+Group+Signatures)
> 核心思路：利用 SPS-EQ 和知识签名构造高效动态群签名，但安全性依赖随机谕言模型。
> 局限与区别：其构造依赖随机谕言模型中的知识签名来实现追踪，而本文通过引入“典范代表”和 NIWI 证明系统，实现了标准模型下的高效实例化。

[7] Fuchsbauer, G. and Gay, R. Weakly Secure Equivalence-Class Signatures from Standard Assumptions. **PKC 2018** [Google Scholar](https://scholar.google.com/scholar?q=Weakly+Secure+Equivalence-Class+Signatures+from+Standard+Assumptions)
> 核心思路：提出了在标准假设下具有较弱安全性的 SPS-EQ 方案（EUF-CoMA）。
> 局限与区别：本文直接采用该 SPS-EQ 方案作为其构造的基础构建块之一，并利用其“完美适配签名”的性质来证明匿名性。

### 核心技术与方案

本文的核心贡献在于形式化定义了完全动态群签名的成员隐私概念，并提出了一个通用构造和高效的优化实例化。

**形式化定义。** 论文在 Bootle 等 [17] 的完全动态模型基础上，新增了两个安全实验：加入隐私，描述了一个外部观察者无法区分两个非成员中哪一个加入了下一个 epoch；离开隐私，描述了该观察者无法区分两个当前成员中哪一个在下一个 epoch 被移除。这两个实验保证了 epoch 信息的变更不泄露具体哪个成员的进出。

**通用构造思路。** 构造的核心思想是结合 SFPK 和 SPS-EQ。群管理员在每个 epoch 生成一对新的 SPS-EQ 密钥，并用该密钥为所有活跃成员的 SFPK 公钥颁发签名证书。为了保护成员身份，管理员不直接发布证书，而是先通过 SFPK.ChgPK 算法随机化每个成员的 SFPK 公钥到新的代表，对随机化后的公钥签名，并将该签名和用于随机化的随机数（用成员的加密公钥加密后）一并放入 epoch 信息。为了打开签名，追踪权威使用成员的 SFPK 典范代表。每个成员在签名时，从 epoch 信息中解密得到随机数，恢复出正确的 SPS-EQ 证书，并再次随机化自己的 SFPK 密钥对和 SPS-EQ 证书，最后用随机化后的 SFPK 密钥签署消息及整个签名组件。签名中包含一个证明，证明随机化后的 SFPK 公钥与加密在追踪者公钥下的典范代表同属一个等价类。追踪者解密典范代表，即可与注册表匹配。

**安全性直觉。** 加入和离开隐私的核心依赖于 epoch 信息中加密的随机性，由 SFPK 的类隐藏性、加密方案的 IND-CPA 安全性以及关键隐私性保证。匿名性依赖于 SPS-EQ 的完美适配签名性和 SFPK 的类隐藏性。追踪性依赖于 SPS-EQ 和 SFPK 的不可伪造性。不可诬陷性依赖于 SFPK 的不可伪造性和证明系统的可靠性。

**高效实例化。** 论文提出了一种新的 SFPK 方案（Scheme 5），其公钥仅包含 2 个 $\mathbb{G}_1$ 元组，并引入了“典范代表”（例如，公钥第一个元素设为 $g_1$）。这使得追踪者可以在不依赖陷门的情况下识别等价类，因为典范代表是唯一的。该 SFPK 方案的安全性基于双线性配对群上的判定性 Diffie-Hellman 假设。通过进一步优化证明系统，将 Groth-Sahai 证明与陷门见证（基于 DDH 假设）结合，签名大小被缩减至 28 个 $\mathbb{G}_1$ 元素、15 个 $\mathbb{G}_2$ 元素和 1 个 $\mathbb{Z}_p^*$ 元素，比仅达到部分动态模型的标准模型方案 [45] 更短。

**渐进复杂度。** 群管理员的更新复杂度线性于活跃成员数，但可并行化，且适用于批处理。签名者只需在首次进入新 epoch 时进行一次线性搜索（可优化为对数级）以找到自己的证书。

### 核心公式与流程

**[SFPK.ChgPK 与 SPS.ChgRep 操作]**
成员收到 epoch 信息中的随机数 $k \in \mathbb{Z}_p^*$ 和 SPS-EQ 签名 $\sigma_{SPS}$。在签名时，成员选取新的随机数 $r \in \mathbb{Z}_p^*$，计算：
$$(\text{sk}_{\text{SFPK}}', \text{pk}_{\text{SFPK}}') \leftarrow \text{SFPK.ChgKeys}(\text{sk}_{\text{SFPK}}, \text{pk}_{\text{SFPK}}, r)$$
$$\sigma_{\text{SPS}}' \leftarrow \text{SPS.ChgRep}(\text{pk}_{\text{SPS}}', \sigma_{\text{SPS}}, r \cdot k^{-1}, \text{pk}_{\text{SPS}})$$
> 作用：成员使用自身的随机数 $r$ 随机化自己的密钥对，同时利用 epoch 信息中的随机数 $k$ 适配 SPS-EQ 证书，确保证书与随机化后的公钥对齐。

**[在优化的实例化方案中，签名者证明的语句]**
签名者在签名中包含一个非交互式证明，其核心语句为：
$$\exists (\text{pk}_{\text{SFPK}}, r, w_1, w_2) \text{ s.t. }$$
$$\text{SFPK.ChgPK}(\text{pk}_{\text{SFPK}}, r) = \text{pk}_{\text{SFPK}}' \land \text{IsCanonical}(\text{pk}_{\text{SFPK}})$$
$$\lor e(w_1, K_2) = e(w_2, g_2)$$
> 作用：该证明声明签名用户的密钥 $\text{pk}_{\text{SFPK}}$ 是一个典范代表，且被随机化为签名中出现的 $\text{pk}_{\text{SFPK}}'$。证明中包含一个“或”分支，这是用于安全性证明的陷门，用于模拟签名，使证明系统能够安全地实例化为标准模型下的 NIWI。

**[基于 SFPK Scheme 5 的验证方程]**
验证者检查 SFPK 签名的有效性，其核心验证方程为：
$$e(\text{Sig}_{\text{SFPK}}^1, g_2) = e(X, Y_2) \cdot e(\text{PHF.Eval}(K_{\text{PHF}}, M), g_2^r)$$
其中 $M = g_1^h \cdot \hat{g}^s$，$h = H(m||\text{Sig}^2||\text{Sig}^3||\text{pk}')$。
> 作用：该方程是 SFPK 方案（Scheme 5）的验证核心。它利用程序化哈希函数和双线性配对，确保了签名在随机化后的公钥（$X$）下是有效的，且与消息 $m$ 绑定。这个构造允许在安全性证明中利用程序化哈希函数进行模拟。

### 实验结果
论文在比较表格中给出了与现有方案的签名大小对比，所有数值均基于 256 位 $\mathbb{G}_1$、512 位 $\mathbb{G}_2$ 和 3072 位 RSA/DL 模数进行估计。本文的通用构造保持常数级签名大小。当使用提出的高效实例化（Scheme 5）和 Groth-Sahai 证明时，签名大小为 13,056 位，其中包含 28 个 $\mathbb{G}_1$ 元素、15 个 $\mathbb{G}_2$ 元素和 1 个 $\mathbb{Z}_p^*$ 元素。作为对比，Libert-Peters-Yung [45] 在部分动态模型下的方案签名大小为 14,848 位。这直接表明，在添加完全动态和成员隐私的更强安全属性后，本方案的签名长度反而更短，证明了隐私在现代标准模型下无需额外性能开销。与 Boyen-Waters [20] 的 6,656 位相比虽更长，但其安全性仅达静态模型且基于 q-type 假设。与 Groth [35] 的 13,056 位相比，本方案在部分动态模型下的签名长度相当，但本方案提供了更强的功能和安全性。

### 局限性与开放问题
本文提出的构造不隐藏群组的大小，因为 epoch 信息的大小线性于活跃成员数。论文讨论了通过添加“哑元成员”来隐藏群组大小的可能性，但这会引入更新复杂度的权衡，并泄露群组的最大容量上界。一个更理想的解决方案是利用常数大小的密码学累加器，但现有累加器在成员加入/离开时要求公开更新证据，这直接破坏了成员隐私。因此，如何设计一个能够隐藏群组大小的同时保持成员隐私和高效更新的完全动态群签名方案，是一个遗留的开放问题。

### 强关联论文

[5] Michael Backes, Lucjan Hanzlik, Kamil Kluczniak, and Jonas Schneider. Signatures with Flexible Public Key: Introducing Equivalence Classes for Public Keys. In ASIACRYPT 2018.
[17] Jonathan Bootle, Andrea Cerulli, Pyrros Chaidos, Essam Ghadafi, and Jens Groth. Foundations of Fully Dynamic Group Signatures. In ACNS 2016.
[18] Jonathan Bootle, Andrea Cerulli, Pyrros Chaidos, Essam Ghadafi, Jens Groth, and Christophe Petit. Short Accountable Ring Signatures Based on DDH. In ESORICS 2015.
[20] Xavier Boyen and Brent Waters. Full-Domain Subgroup Hiding and Constant-Size Group Signatures. In PKC 2007.
[31] Georg Fuchsbauer and Romain Gay. Weakly Secure Equivalence-Class Signatures from Standard Assumptions. In PKC 2018.
[37] Christian Hanser and Daniel Slamanig. Structure-Preserving Signatures on Equivalence Classes and Their Application to Anonymous Credentials. In ASIACRYPT 2014.
[45] Benoît Libert, Thomas Peters, and Moti Yung. Short Group Signatures via Structure-Preserving Signatures: Standard Model Security from Simple Assumptions. In CRYPTO 2015.
[46] San Ling, Khoa Nguyen, Huaxiong Wang, and Yanhong Xu. Constant-Size Group Signatures from Lattices. In PKC 2018.


## 关键词

+ 群签名
+ 成员隐私
+ 动态群
+ 灵活公钥签名
+ 隐私保护