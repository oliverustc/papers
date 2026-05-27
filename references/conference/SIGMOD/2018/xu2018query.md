---
title: "When query authentication meets fine-grained access control: A zero-knowledge approach"
doi: 10.1145/3183713.3183741
标题简称:
论文类型: conference
会议简称: SIGMOD
发表年份: 2018
modified: 2025-04-11 14:03:02
---
## When query authentication meets fine-grained access control: A zero-knowledge approach

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3183713.3183741)

## 作者

+ [Cheng Xu](Cheng%20Xu.md)
+ [Jianliang Xu](Jianliang%20Xu.md)
+ Haibo Hu 
+ [Man Ho Au](Man%20Ho%20Au.md)
## 笔记

### 背景与动机
在数据即服务（DaaS）和云计算的背景下，企业将数据库外包给第三方云引擎（如Amazon SimpleDB、Microsoft Azure），以获得高性能和高可用性。然而，由于服务中断、程序故障和安全漏洞等原因，外包数据库返回的查询结果完整性无法得到保证。为此，学术界已提出大量基于认证数据结构（ADS）的查询认证方案 [14, 15, 24, 36]。另一方面，访问控制是保护数据安全的关键，往往与完整性需求共存。基于属性加密（ABE）[2, 9]等技术已被用于实现细粒度访问控制 [10, 29–31]。现有研究 [3, 12, 22] 尝试在查询认证中融合访问控制，但存在三个主要局限：仅支持粗粒度规则，例如 [22] 仅禁止泄露查询范围外的数据；访问控制并非密码学强制实施，易被绕过或遭受SQL注入攻击；此外，这些技术会区分不可访问数据与不存在数据，从而向用户泄露敏感信息，如通过枚举攻击推断数据分布。因此，本文旨在解决在细粒度访问控制下进行查询认证的核心挑战——如何在认证过程中保护信息机密性，确保证明是零知识的，即不泄露可访问记录之外的任何信息。

### 相关工作

[2] Bethencourt等人. Ciphertext-Policy Attribute-Based Encryption. **IEEE S&P 2007** [Google Scholar](https://scholar.google.com/scholar?q=Ciphertext-Policy+Attribute-Based+Encryption)
> 核心思路：提出CP-ABE方案，将访问策略嵌入密文，解密密钥与用户属性集关联。
> 局限与区别：CP-ABE只能用于加密，无法提供数据完整性认证或身份证明。本文基于ABE的思想，但改用了ABS来实现认证。

[9] Goyal等人. Attribute-based encryption for fine-grained access control of encrypted data. **CCS 2006** [Google Scholar](https://scholar.google.com/scholar?q=Attribute-based+encryption+for+fine-grained+access+control+of+encrypted+data)
> 核心思路：提出KP-ABE方案，用户密钥绑定访问策略，密文关联属性集。
> 局限与区别：同CP-ABE，该方案仅关注数据机密性，未考虑用户对查询结果的认证需求。

[3] Chen等人. Access Control Friendly Query Verification for Outsourced Data Publishing. **ESORICS 2008** [Google Scholar](https://scholar.google.com/scholar?q=Access+Control+Friendly+Query+Verification+for+Outsourced+Data+Publishing)
> 核心思路：提出一种支持基本访问控制的可验证范围查询算法，基于“可访问空间”概念。
> 局限与区别：该方案仅支持粗粒度的基于身份的空间划分，且不提供零知识隐私保护。本文则面向细粒度的基于属性的策略，并实现了零知识机密性。

[19] Maji等人. Attribute-Based Signatures. **Topics in Cryptology 2011** [Google Scholar](https://scholar.google.com/scholar?q=Attribute-Based+Signatures)
> 核心思路：提出ABS方案，允许用户使用满足特定谓词的属性集对消息进行签名，同时隐藏签名者身份。
> 局限与区别：本文修改了ABS方案，使其支持谓词松弛（predicate relaxation），从而使服务提供者能为未授权用户生成定制化的“剥除策略”签名，以实现零知识证明。

[22] Pang等人. Verifying Completeness of Relational Query Results in Data Publishing. **SIGMOD 2005** [Google Scholar](https://scholar.google.com/scholar?q=Verifying+Completeness+of+Relational+Query+Results+in+Data+Publishing)
> 核心思路：利用签名链（signature chaining）技术，验证关系查询结果的完整性和正确性。
> 局限与区别：该方案完全不支持访问控制，任何用户都能验证所有返回结果。本文在此类认证技术上融入了细粒度访问控制机制。

[15] Li等人. Dynamic Authenticated Index Structures for Outsourced Databases. **SIGMOD 2006** [Google Scholar](https://scholar.google.com/scholar?q=Dynamic+Authenticated+Index+Structures+for+Outsourced+Databases)
> 核心思路：提出Merkle B-tree，支持动态数据库上的高效查询认证。
> 局限与区别：Merkle树结构会泄露数据分布信息，不符合零知识要求。本文采用全满的网格树（AP²G-tree），防止通过树结构推断数据分布。

[8] Ghosh等人. Efficient Verifiable Range and Closest Point Queries in Zero-Knowledge. **PETS 2016** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+Verifiable+Range+and+Closest+Point+Queries+in+Zero-Knowledge)
> 核心思路：提出一维数据上支持零知识认证的范围和最近点查询方案。
> 局限与区别：该方案假设用户只提交单次查询，无法抵御连续查询攻击。本文的方案设计考虑了重复查询下的安全性，且支持更复杂的细粒度访问控制。

### 核心技术与方案

**系统模型与威胁模型**：系统包含三方：数据所有者（DO）、服务提供者（SP）和用户。DO 使用 CP-ABE 加密数据内容，并基于一种新的访问策略保留（APP）签名构建 ADS，然后将所有内容外包给 SP。SP 响应用户查询，返回结果及其验证对象（VO）。威胁模型假设 SP 不完全可信，可能篡改或遗漏结果；用户是好奇的，试图获取越权信息。目标是实现存证性（返回结果真实且可访问）和完备性（所有符合条件的记录都被返回），同时满足零知识机密性（不泄露不可访问记录的任何信息）。

**APP 签名与 APS 签名**：核心基础是本文提出的 APP 签名，它是基于 ABS 变体的数字签名。对一条记录 $(o_i, v_i, \Upsilon_i)$，其 APP 签名定义为 $\sigma_i = \text{ABS.Sign}(sk_{\text{DO}}, hash(o_i) | hash(v_i), \Upsilon_i)$，它将查询属性、数据内容和访问策略绑定在一起。关键创新在于鉴权不可访问记录时，SP 通过 ABS.Relax 操作，将原 APP 签名转变为**访问策略剥离（APS）签名**。APS 签名的谓词是用户角色全集 $\mathbb{A}$ 中去除用户所拥角色集 $\mathcal{A}$ 后剩余角色的析取，即 $\hat{\Upsilon}_{\mathcal{A}} = \vee_{a \in \mathbb{A} \backslash \mathcal{A}} a$。这个谓词是用户无法满足的最弱策略，APS 签名足以证明用户无法访问该记录，但又不泄露具体缺少哪个角色，从而实现了零知识。

**ABS 方案及其谓词松弛**：ABS 方案基于双线性对和单调跨距程序（MSP）。ABS.Sign 算法根据用户的属性集和谓词签名。ABS.Relax 算法接受原 APP 签名和一个属性集 $\mathcal{A}'$，通过四个步骤生成新签名：清除(剔除原谓词树中不能被 $\mathcal{A}'$ 满足的分支)；合并重复属性；追加缺失属性；重随机化签名。该算法成功的条件是 $\Upsilon(\mathbb{A} \backslash \mathcal{A}') = 0$，即原谓词不能被用户的全集互补角色满足。该设计确保了所有变换在计算上不可区分，满足完美隐私性，是零知识性质的前提。

**AP²G-tree 索引**：为高效处理范围查询和连接查询，提出了**访问策略保留网格树**（AP²G-tree）。该树将数据空间递归划分为网格，形成一个全满树。非叶子节点的访问策略是其所有子节点策略的**析取**，签名是对网格盒子 $gb_i$ 和聚合策略的 ABS 签名。这一设计的要点在于：若一个节点不可访问，其所有子节点必然都不可访问，因此可以用一个 APS 签名证明整个子树区域的不可访问性，实现高效剪枝。

**查询处理**：处理范围查询时，SP 基于 BFS 遍历 AP²G-tree。若节点与查询范围部分相交，则展开其子节点。若节点被完全覆盖且可访问，则继续展开；若被完全覆盖但不可访问，则直接为该节点生成 APS 签名加入VO。用户验证时，检查所有 VO 中签名，并确保 VO 中所有区域的并集覆盖整个查询范围，以此保证完备性。连接查询的处理类似，通过对两张表的树进行同步遍历，确认可访问匹配对，对不可访问的空间添加 APS 签名。

**安全性证明**：论文在通用群模型下证明了 ABS 方案的完美隐私性和不可伪造性。基于此，论证了查询认证算法的不可伪造性（若 VO 通过验证，则结果集必定是真实且完备的）和零知识性（真实游戏和理想游戏输出分布相同，理想游戏中不可访问记录被替换为随机数据并关联仅有伪角色的策略）。

**复杂度**：AP²G-tree 的空间复杂度为 $O((n + \log(n))m)$，其中 $n$ 是索引空间大小，$m$ 是访问策略的单调跨距程序大小。计算开销主要来自 ABS.Relax 操作，其性能与谓词长度成正比。

### 核心公式与流程

**[APP 签名定义]**
$$
\sigma_i = \text{ABS.Sign}(sk_{\text{DO}}, hash(o_i) | hash(v_i), \Upsilon_i)
$$
> 作用：将查询属性 $o_i$、数据内容 $v_i$ 和访问策略 $\Upsilon_i$ 绑定，作为记录的完整性证明。

**[APS 签名定义]**
$$
\hat{\sigma}_{i,\mathcal{A}} = \text{ABS.Sign}(sk_{\text{DO}}, hash(o_i) | hash(v_i), \hat{\Upsilon}_{\mathcal{A}}), \; \hat{\Upsilon}_{\mathcal{A}} = \vee_{a \in \mathbb{A} \backslash \mathcal{A}} a
$$
> 作用：为用户生成不可访问记录的“剥除策略”签名，该谓词是用户无法满足的最弱策略，确保零知识。

**[AP²G-tree 非叶子节点定义]**
$$
p_i = p_{c_1} \vee p_{c_2} \vee \dots \vee p_{c_C}, \quad sig_i = \text{ABS.Sign}(sk_{\text{DO}}, gb_i, p_i)
$$
> 作用：定义非叶子节点的聚合访问策略（子节点策略的析取）及其签名，实现高剪枝效率。

**[ABS.Relax 算法关键步骤]**
$$
\sigma_{m,\Upsilon'} = (\tau, \hat{Y}^r, \hat{W}^r, \{\hat{S}_i^r\}, \hat{P}_1^r)
$$
> 作用：对原 APP 签名进行清除、合并、追加和重随机化，生成新谓词下的 APS 签名，确保新旧签名分布相同。

### 实验结果

实验使用 TPC-H 标准基准测试的 Lineitem 表，共 12 个属性，前三个作为查询属性。默认数据库规模为 0.3（180万条记录），访问策略为 DNF 形式，默认包含 10 个不同策略，最多 10 个角色，最大策略长度为 6。数据所有者（DO）和服务提供者（SP）部署在双 Intel Xeon 2.67GHz X5650 CPU、32GB RAM 的服务器上，用户端为 Intel Core i5 CPU、4GB RAM 的笔记本。在所有实验中，AP²G-tree 方法在 SP CPU 时间、用户 CPU 时间和 VO 大小上全面优于重复执行相等查询的简单方法。以范围查询为例，当查询范围从 0.03% 增长到 1% 时，AP²G-tree 的 SP CPU 时间从约 1 秒增长到 42 秒，而简单方法从 2 秒增长到 60 秒。数据库规模从 0.1 增加到 3 时，AP²G-tree 的各项开销增长平稳。增加角色总数和策略长度会显著增加开销。并行优化（多线程）可有效降低 SP 和用户端 CPU 时间，在 16 线程时性能提升趋于饱和。层次角色分配优化可减少不可访问谓词长度，从而降低 SP 和用户端开销。k-d 树索引（访问策略保留下，非零知识）的性能显著优于网格树索引，SP CPU 时间在查询范围 1% 时可降低近 40%。

### 局限性与开放问题
本文主要关注范围查询和连接查询，未能处理聚合查询（如 SUM、AVG）或多源数据在分布式环境下的查询认证。如何处理这些更复杂的查询类型是未来工作一个重要方向。此外，当前方案在角色数和策略长度较大时计算开销仍较高，进一步优化 ABS 操作或引入更高效的密码学原语是值得探索的方向。

### 强关联论文

[19] Maji等人. Attribute-Based Signatures. **Topics in Cryptology 2011** [Google Scholar](https://scholar.google.com/scholar?q=Attribute-Based+Signatures)

[9] Goyal等人. Attribute-based encryption for fine-grained access control of encrypted data. **CCS 2006** [Google Scholar](https://scholar.google.com/scholar?q=Attribute-based+encryption+for+fine-grained+access+control+of+encrypted+data)

[2] Bethencourt等人. Ciphertext-Policy Attribute-Based Encryption. **IEEE S&P 2007** [Google Scholar](https://scholar.google.com/scholar?q=Ciphertext-Policy+Attribute-Based+Encryption)

[15] Li等人. Dynamic Authenticated Index Structures for Outsourced Databases. **SIGMOD 2006** [Google Scholar](https://scholar.google.com/scholar?q=Dynamic+Authenticated+Index+Structures+for+Outsourced+Databases)

[24] Pang等人. Authenticating query results in edge computing. **ICDE 2004** [Google Scholar](https://scholar.google.com/scholar?q=Authenticating+query+results+in+edge+computing)

[3] Chen等人. Access Control Friendly Query Verification for Outsourced Data Publishing. **ESORICS 2008** [Google Scholar](https://scholar.google.com/scholar?q=Access+Control+Friendly+Query+Verification+for+Outsourced+Data+Publishing)

[22] Pang等人. Verifying Completeness of Relational Query Results in Data Publishing. **SIGMOD 2005** [Google Scholar](https://scholar.google.com/scholar?q=Verifying+Completeness+of+Relational+Query+Results+in+Data+Publishing)

[36] Yang等人. Authenticated indexing for outsourced spatial databases. **VLDBJ 2009** [Google Scholar](https://scholar.google.com/scholar?q=Authenticated+indexing+for+outsourced+spatial+databases)


## 关键词

+ 查询认证细粒度访问控制
+ 访问策略保留签名
+ 零知识机密性
+ 外包数据库完整性
+ 网格索引认证数据结构
+ 范围查询连接查询认证