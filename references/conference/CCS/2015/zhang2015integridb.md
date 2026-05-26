---
title: "IntegriDB: Verifiable SQL for outsourced databases"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2015
---

## IntegriDB: Verifiable SQL for outsourced databases

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/2810103.2813711)

## 作者

+ [Yupeng Zhang](Yupeng%20Zhang.md) 
+ [Jonathan Katz](Jonathan%20Katz.md) 
+ [Charalampos Papamanthou](Charalampos%20Papamanthou.md) 


## 笔记

### 背景与动机
随着云计算普及，将数据库存储和查询外包给不受信任的服务器已成为主流需求，但用户必须能够验证返回结果的正确性。认证数据结构（ADS）允许数据所有者外包数据，并使客户端能够验证服务器回答的查询结果。尽管已有通用方案（如基于电路或RAM的通用可验证计算）理论上支持任意SQL查询，但它们在实践中效率极低，因为电路规模至少与数据库本身一样大，且不支持高效更新；而专用方案（如基于Merkle树或签名的方案）要么仅支持单维范围查询（例如[43][31]），要么不支持高效更新（如[32]），并且几乎所有现有方案都无法为JOIN查询和作用于中间结果的聚合函数提供简短证明。为此，本文旨在设计一个同时具备表达能力（支持多维范围、JOIN、SUM、MAX/MIN、COUNT、AVG及有限嵌套查询）、高效率（证明大小和验证时间对数依赖于数据库大小）、可扩展和可证明安全的ADS系统——IntegriDB。

### 相关工作

[2] Ben-Sasson等. SNARKs for C: Verifying program executions succinctly and in zero knowledge. **Crypto 2013** [Google Scholar](https://scholar.google.com/scholar?q=SNARKs+for+C+Verifying+program+executions+succinctly+and+in+zero+knowledge)
> 核心思路：将任意C程序编译为RAM模型，通过SNARK实现可验证计算。
> 局限与区别：据本文实验，其设置时间和证明时间比IntegriDB慢两个数量级，且无法高效处理数据库更新。

[4] Ben-Sasson等. Succinct non-interactive zero knowledge for a Von Neumann architecture. **USENIX Security 2014** [Google Scholar](https://scholar.google.com/scholar?q=Succinct+non-interactive+zero+knowledge+for+a+Von+Neumann+architecture)
> 核心思路：基于电路的通用可验证计算系统（libsnark）。
> 局限与区别：电路规模随数据库大小线性增长，不支持高效更新，且处理SQL查询时设置时间和证明时间均显著高于IntegriDB。

[32] Papadopoulos等. Taking authenticated range queries to arbitrary dimensions. **CCS 2014** [Google Scholar](https://scholar.google.com/scholar?q=Taking+authenticated+range+queries+to+arbitrary+dimensions)
> 核心思路：首次显式设计支持多维范围查询的ADS，证明大小与表大小无关。
> 局限与区别：不支持高效更新（复杂度为 $O(m\sqrt{n})$），且不支持JOIN查询或作用于中间结果的聚合函数。

[36] Papamanthou等. Optimal verification of operations on dynamic sets. **Crypto 2011** [Google Scholar](https://scholar.google.com/scholar?q=Optimal+verification+of+operations+on+dynamic+sets)
> 核心思路：基于双线性累加器实现动态集合操作（并、交）的最优验证。
> 局限与区别：不直接支持求和查询，也不支持将集合操作作为多维查询或JOIN的构建块。IntegriDB在此基础扩展以支持求和及嵌套查询。

[10] Canetti等. Verifiable set operations over outsourced databases. **PKC 2014** [Google Scholar](https://scholar.google.com/scholar?q=Verifiable+set+operations+over+outsourced+databases)
> 核心思路：基于可提取性假设的集合操作验证方案。
> 局限与区别：未提供对求和查询或与区间树结合以支持完整SQL的功能。

[43] Yang等. Authenticated join processing in outsourced databases. **SIGMOD 2009** [Google Scholar](https://scholar.google.com/scholar?q=Authenticated+join+processing+in+outsourced+databases)
> 核心思路：通过返回某一列的所有值，让客户端对另一个列进行逐一范围查询来实现JOIN。
> 局限与区别：证明大小和验证时间在最坏情况下与最小表的大小呈线性关系，且不支持多维范围查询或作用于中间结果的函数。

[31] Pang等. Scalable verification for outsourced dynamic databases. **VLDB 2009** [Google Scholar](https://scholar.google.com/scholar?q=Scalable+verification+for+outsourced+dynamic+databases)
> 核心思路：基于签名链的方案支持动态数据库上的单维范围查询和JOIN。
> 局限与区别：不支持多维范围查询，且JOIN的证明大小线性于表的大小。

[37] Parno等. Pinocchio: Nearly practical verifiable computation. **IEEE S&P 2013** [Google Scholar](https://scholar.google.com/scholar?q=Pinocchio+Nearly+practical+verifiable+computation)
> 核心思路：基于电路的高效可验证计算系统。
> 局限与区别：与[4]类似，不支持高效更新，且数据库规模导致电路过大而不实用。

[1] Bajaj等. CorrectDB: SQL engine with practical query authentication. **VLDB 2013** [Google Scholar](https://scholar.google.com/scholar?q=CorrectDB+SQL+engine+with+practical+query+authentication)
> 核心思路：依赖可信硬件实现可验证SQL。
> 局限与区别：需要额外的硬件假设，而IntegriDB不依赖任何可信硬件。

### 核心技术与方案
IntegriDB的整体框架围绕两个核心构建块展开：一个支持求和的可验证集合操作ADS和一种认证区间树。系统将数据所有者、服务器和客户端三者分离，数据所有者运行初始化与设置算法，服务器响应查询并生成证明，客户端验证证明。

第一个构建块是支持集合操作与求和的ADS，基于双线性累加器。对于集合 $S = \{x_1, \ldots, x_n\} \subset \mathbb{Z}_p$，其累加值定义为 $\operatorname{acc}(S) = g^{\prod_{i=1}^n (x_i^{-1} + s)}$，其中 $s$ 是秘密陷门。证明一个并集或交集操作的正确性沿用了Papamanthou等人[36]和Canetti等人[10]的方法。对于求和，服务器计算多项式展开系数 $a_1 = \sum_{i=1}^n \prod_{j eq i} x_j^{-1}$ 和 $a_0 = \prod_{i=1}^n x_i^{-1}$，并发送对应的辅助值 $w_1, w_2$。客户端通过两个配对检查来验证 $\operatorname{sum} = a_1 \cdot a_0^{-1} \mod p$ 是否正确。该方案的安全性基于q-SBDH假设[8]和可提取性假设[5]，证明策略在于：如果敌手输出虚假的 $(a_0^*, a_1^*)$ 使得验证通过但和不同，则可以从验证方程中提取出 $g^{1/s}$，从而打破q-SBDH假设。

第二个构建块是认证区间树，基于Merkle树和红黑树构造。对于每对列 $(i, j)$，系统构建一棵区间树，其叶子节点存储键值对 $(x_{ki}, x_{kj})$，内部节点存储键（左子树最大键）和值，该值是一个包含累加值及其加密的元组：$f_{s, sk}(u) = \mathsf{Enc}_{sk}(\prod_{v \in T_u}(v^{-1} + s)) \| g^{\prod_{v \in T_u}(v^{-1} + s)}$。树支持Search和RangeCover查询，以及Insert和Delete更新。证明大小为 $O(\log n)$，验证复杂度为 $O(\log n)$。

在整体方案中，设置算法为每个表的每对列构建一棵认证区间树，并输出所有树根的摘要和每行的哈希。对于JOIN查询，服务器通过RangeCover获取两列的累加值，利用ASO进行求交，再对交集中每个元素进行Search查询以获取匹配行的数量，最后返回行内容及其哈希证明。客户端验证所有证明和行哈希。其安全性由AIT保证累加值的正确性，由ASO保证交集的正确性，由行哈希保证行未被篡改。证明大小和验证时间为 $\tilde{O}(|R|)$，与结果大小成正比。

对于多维范围查询，服务器对每维所在的列与参考列构建的区间树执行RangeCover，获得一组覆盖节点的累加值，然后使用ASO对这些累加值代表的集合进行交集运算。证明大小为 $O(d \log n)$，验证复杂度为 $O(d \log n + |R|)$。SUM函数可直接利用列自身的累加值通过ASO的求和操作验证，COUNT和AVG可规约为SUM，MAX/MIN可规约为单维范围查询。更新操作中，数据所有者通过解密内部节点的加密值，在红黑树旋转时重新计算并加密新的累加值，复杂度为 $\tilde{O}(m^2 \log n)$。嵌套查询的核心在于将中间结果的累加值（而非整个结果）传递给下一层查询，从而保持证明简短。

### 核心公式与流程

**[集合累加值的定义]**
$$ \operatorname{acc}(S) \stackrel{\text{def}}{=} g^{\prod_{i=1}^n (x_i^{-1} + s)} $$
> 作用：将集合 $S$ 压缩为一个群元素，是后续所有集合操作验证的基础。

**[求和验证中的配对检查]**
$$ e(g^s, w_1) \stackrel{?}{=} e(\operatorname{acc}(S) / g^{a_0}, g) $$
$$ e(g^s, w_2) \stackrel{?}{=} e(w_1 / g^{a_1}, g) $$
> 作用：用于验证服务器声称的和 $\operatorname{sum} = a_1 \cdot a_0^{-1} \mod p$ 是否正确。第一个等式保证 $a_0$ 正确，第二个等式保证 $a_1$ 正确。

**[认证区间树内部节点值]**
$$ f_{s, sk}(u) = \mathsf{Enc}_{sk}\left(\prod_{v \in T_u}(v^{-1} + s)\right) \left\|\, g^{\prod_{v \in T_u}(v^{-1} + s)}\right. $$
> 作用：右半部分是子树内所有值的累加，供服务器生成静态查询证明；左半部分是加密的指数，供数据所有者在更新（旋转）时高效计算新的累加值。

**[JOIN查询流程（Prove算法）]**
1. 服务器对 $S^T_{i \times i}$ 执行 RangeCover，获取 $\operatorname{acc}(C_i)$ 及证明。
2. 服务器对 $S^{T'}_{j \times j}$ 执行 RangeCover，获取 $\operatorname{acc}(C'_j)$ 及证明。
3. 服务器利用 ASO 对 $\operatorname{acc}(C_i)$ 和 $\operatorname{acc}(C'_j)$ 执行交集操作，得到 $C^*$ 及证明。
4. 对每个 $x \in C^*$，服务器在 $S^T_{i \times i}$ 上执行 Search，获取 $|R_x|$ 及证明（同样对 $T'$）。
> 作用：客户端最终验证所有证明，并检查返回行是否未被篡改。

### 实验结果
实验在Amazon EC2机器（16GB RAM）上进行，使用C++实现，采用AES-CBC-128加密，SHA-256哈希，254-bit椭圆曲线的Ate配对（128位安全强度），以MySQL作为后端SQL服务器。针对TPC-H查询#19（一个涉及JOIN、多维范围查询和SUM的复杂查询），在lineitem表（6百万行，16列）和part表（20万行，9列）上，设置时间为25272.76秒，证明计算时间为6422.13秒，但验证时间仅232ms，证明大小为184.16KB，插入一行数据的更新时间为150ms。系统支持22个TPC-H查询中的12个，支持TPC-C中94%的查询。在JOIN查询测试中，对于两个各含100,000行、10列的表，证明大小仅为27.97KB，验证时间为45.4ms。对于10维范围查询，在100,000行表上证明大小为251KB，验证约400ms。嵌套SUM查询（对3维范围结果求和）的验证时间约60ms，证明大小45KB。与libsnark [4]和SNARKs for C [2]相比，在相同的10维范围求和查询上，IntegriDB的设置时间（13.878s）比libsnark（157.163s）快10倍，比SNARKs for C（约2000s）快百倍以上，证明时间也显著更优。

### 局限性与开放问题
系统无法支持列间比较（如 $c_1 \geq 2 \cdot c_2 + 3$）和列间聚合（如 $c_1 + 2 \cdot c_2$）的简短证明，处理这类查询需返回大量数据。当嵌套JOIN查询作用于存在重复值的范围查询结果时，无法保持简短证明。此外，当前实现中每个表需为每对列构建区间树，导致设置时间和服务器存储开销为 $O(m^2 n)$，对于列数较多的表可能成为瓶颈。

### 强关联论文

[36] Papamanthou等. Optimal verification of operations on dynamic sets. **Crypto 2011** [Google Scholar](https://scholar.google.com/scholar?q=Optimal+verification+of+operations+on+dynamic+sets)

[10] Canetti等. Verifiable set operations over outsourced databases. **PKC 2014** [Google Scholar](https://scholar.google.com/scholar?q=Verifiable+set+operations+over+outsourced+databases)

[32] Papadopoulos等. Taking authenticated range queries to arbitrary dimensions. **CCS 2014** [Google Scholar](https://scholar.google.com/scholar?q=Taking+authenticated+range+queries+to+arbitrary+dimensions)

[37] Parno等. Pinocchio: Nearly practical verifiable computation. **IEEE S&P 2013** [Google Scholar](https://scholar.google.com/scholar?q=Pinocchio+Nearly+practical+verifiable+computation)

[4] Ben-Sasson等. Succinct non-interactive zero knowledge for a Von Neumann architecture. **USENIX Security 2014** [Google Scholar](https://scholar.google.com/scholar?q=Succinct+non-interactive+zero+knowledge+for+a+Von+Neumann+architecture)

[2] Ben-Sasson等. SNARKs for C: Verifying program executions succinctly and in zero knowledge. **Crypto 2013** [Google Scholar](https://scholar.google.com/scholar?q=SNARKs+for+C+Verifying+program+executions+succinctly+and+in+zero+knowledge)

[43] Yang等. Authenticated join processing in outsourced databases. **SIGMOD 2009** [Google Scholar](https://scholar.google.com/scholar?q=Authenticated+join+processing+in+outsourced+databases)

[31] Pang等. Scalable verification for outsourced dynamic databases. **VLDB 2009** [Google Scholar](https://scholar.google.com/scholar?q=Scalable+verification+for+outsourced+dynamic+databases)

[1] Bajaj等. CorrectDB: SQL engine with practical query authentication. **VLDB 2013** [Google Scholar](https://scholar.google.com/scholar?q=CorrectDB+SQL+engine+with+practical+query+authentication)


## 精准翻译

以下是中文翻译：

本文提出了 IntegriDB 系统，该系统允许数据所有者将数据库存储外包给不可信服务器，然后使任何人都能够对该数据库执行可验证的 SQL 查询。我们的系统处理丰富的 SQL 查询子集，包括多维范围查询、JOIN 连接、SUM 求和、MAX/MIN 最大最小值、COUNT 计数和 AVG 平均值，以及此类查询的（有限）嵌套。即使对于包含 10^5 条记录的表，IntegriDB 也具有小型证明（几 KB），这些证明仅与数据库大小呈对数关系，验证时间短（数十毫秒），服务器计算可行（不到一分钟）。系统还支持高效更新。我们基于已知的密码学假设证明了 IntegriDB 的安全性，并通过性能测量和对 TPC-H 和 TPC-C 基准测试中 SQL 查询的可验证处理来展示其实用性和表达能力。

## 关键词

+ 可验证数据库
+ SQL查询验证
+ 外包数据库
+ 密码学证明
+ 对数级证明