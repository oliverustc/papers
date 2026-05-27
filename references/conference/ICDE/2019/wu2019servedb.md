---
title: "ServeDB: Secure, verifiable, and efficient range queries on outsourced database"
doi: 10.1109/icde.2019.00062
标题简称:
论文类型: conference
会议简称: ICDE
发表年份: 2019
---
## ServeDB: Secure, verifiable, and efficient range queries on outsourced database

## 发表信息

+ [原文链接]()

## 作者

+ Songrui Wu 
+ [Qi Li](Qi%20Li.md)
+ Guoliang Li 
+ Dong Yuan 
+ Xingliang Yuan 
+ Cong Wang 


## 笔记

### 背景与动机
随着云服务的普及，数据外包已成为常见做法，但数据安全和隐私问题成为重要障碍。虽然数据加密可以缓解安全担忧，但它降低了查询处理的功能性，例如无法在加密数据上执行SQL查询。多维度范围查询在数据库应用中非常普遍（如电子病历中的年龄和位置组合查询），但现有方案存在明显瓶颈。基于顺序保留加密（OPE）的方案（如CryptDB）会泄露数据的顺序和分布信息，安全性较弱。现有的可搜索对称加密（SSE）方案主要支持关键词搜索或单维度范围查询，扩展到多维时需要对每个维度独立搜索再取交集，这会产生显著延迟并可能泄露比预期更多的匹配记录。此外，大多数先前方案假设云服务器是半诚实的，但实践中服务器可能行为恶意，例如仅执行部分查询操作以节省计算成本或故意篡改结果。因此，在保证隐私和效率的同时实现可验证性，是多维范围查询领域一个未被充分解决的挑战。ServeDB旨在填补这一空白，首次同时实现了隐私保护、亚线性查询效率和对恶意服务器的结果可验证性。

### 相关工作

[2] Agrawal et al. Order preserving encryption for numeric data. **SIGMOD 2004** [Google Scholar](https://scholar.google.com/scholar?q=Order+preserving+encryption+for+numeric+data)
> 核心思路：提出顺序保留加密，使得在密文上可以直接比较大小，从而支持范围查询。
> 局限与区别：其安全定义较弱，会泄露数据的顺序和分布信息，易受推断攻击。ServeDB通过哈希和布隆过滤器混淆节点内容，不泄露任何顺序或分布信息。

[5] Stefanov et al. Practical dynamic searchable encryption with small leakage. **NDSS 2014** [Google Scholar](https://scholar.google.com/scholar?q=Practical+dynamic+searchable+encryption+with+small+leakage)
> 核心思路：提出动态可搜索对称加密方案，支持高效的关键词搜索，并控制泄露量。
> 局限与区别：主要针对单关键词搜索，无法直接处理多维范围查询。ServeDB在此基础上进行扩展，支持多维查询并增加了可验证性。

[7] Popa et al. CryptDB: protecting confidentiality with encrypted query processing. **SOSP 2011** [Google Scholar](https://scholar.google.com/scholar?q=CryptDB+protecting+confidentiality+with+encrypted+query+processing)
> 核心思路：提出在数据库系统内部对SQL操作进行洋葱式加密，以支持多种查询。
> 局限与区别：其核心依赖OPE，安全性较弱。ServeDB不依赖于OPE，而是设计了全新的安全索引结构SVETree。

[8] Wang et al. Secure and efficient range queries on outsourced databases using RP-trees. **ICDE 2013** [Google Scholar](https://scholar.google.com/scholar?q=Secure+and+efficient+range+queries+on+outsourced+databases+using+RP-trees)
> 核心思路：提出RP-tree，在R-tree基础上利用OPE加密索引，以支持加密范围查询。
> 局限与区别：RP-tree会泄露数据的分布信息，且同样依赖弱安全性的OPE，不提供结果可验证性。

[10] Li et al. Fast and scalable range query processing with strong privacy protection for cloud computing. **IEEE/ACM ToN 2016** [Google Scholar](https://scholar.google.com/scholar?q=Fast+and+scalable+range+query+processing+with+strong+privacy+protection+for+cloud+computing)
> 核心思路：提出PBtree，使用布隆过滤器和SSE技术实现单维范围查询。
> 局限与区别：该方法仅为单维设计，扩展至多维需独立查询各维再取交集，性能和隐私均有损失。ServeDB通过层次化立方体编码将多维问题转化为单维匹配问题。

[11] Demertzis et al. Practical private range search revisited. **SIGMOD 2016** [Google Scholar](https://scholar.google.com/scholar?q=Practical+private+range+search+revisited)
> 核心思路：提出Log-SRC-i方案，使用范围覆盖技术和SSE实现隐私范围查询。 
> 局限与区别：主要针对一维，扩展至多维同样需要取交集且引入较高假阳性率。ServeDB在查询效率和假阳性率方面均优于该方法。

[23] Szydlo. Merkle tree traversal in log space and time. **Eurocrypt 2004** [Google Scholar](https://scholar.google.com/scholar?q=Merkle+tree+traversal+in+log+space+and+time)
> 核心思路：提出Merkle树的遍历算法，用于验证大型数据集中的成员关系。
> 局限与区别：经典Merkle树仅用于验证数据完整性，未结合查询和隐私保护。ServeDB将Merkle树验证思想融入其安全查询索引SVETree中。

[26] Papadopoulos et al. Taking authenticated range queries to arbitrary dimensions. **CCS 2014** [Google Scholar](https://scholar.google.com/scholar?q=Taking+authenticated+range+queries+to+arbitrary+dimensions)
> 核心思路：提出针对任意维度范围查询的可验证方案，但验证开销与维度数成线性关系。
> 局限与区别：其验证复杂度随维度增加而线性增长。ServeDB的验证开销与维度无关，仅取决于查询结果集大小和树的高度，效率更高。

[28] Curtmola et al. Searchable symmetric encryption: improved definitions and efficient constructions. **Journal of Computer Security 2011** [Google Scholar](https://scholar.google.com/scholar?q=Searchable+symmetric+encryption+improved+definitions+and+efficient+constructions)
> 核心思路：为可搜索对称加密（SSE）提出改进的安全定义和高效构造，是后续SSE工作的理论基础。
> 局限与区别：本文引用了其安全定义框架（理想-现实模拟范式）来形式化定义安全模型，但需要针对多维查询和可验证性进行扩展。

### 核心技术与方案
ServeDB的整体框架包含数据所有者、云服务器和数据用户三方，核心在于一个称为SVETree的安全、可验证、高效索引树。方案首先通过**分层立方体编码**将多维数值数据转换为一组离散的立方体编码，从而将多维范围匹配问题转化为单维编码集合交集判定问题。具体地，数据所有者根据所有属性的值域定义一个d维超级立方体，并递归地将其划分为 $2^{d}$ 个子立方体，直到层数k满足精度要求。每个立方体通过HMAC（带密钥K）对其中点坐标和层级进行哈希，得到唯一编码 $c_{i} = \text{HMAC}(K, (g_{i}.x + g_{i}.y + L_{i}))$。每个数据记录 $D_{i}$ 对应其所在的所有层级立方体编码集合 $C_{i} = \{c_{1}, ..., c_{k}\}$。对于查询范围Q，从根立方体开始，自上而下地查找被Q完全覆盖的立方体，将其编码加入查询编码集 $C_{Q}$；若部分覆盖则递归进入子立方体，直到叶子层级，从而以最少编码覆盖查询范围。

为了索引这些编码并支持查询和验证，论文设计了SVETree。其构建包含三个步骤：
1. **构建平衡二叉树**：递归将数据集随机均分到左右子节点，每个叶子节点包含一个数据记录及其加密结果。
2. **编码树节点**：每个节点v用一个布隆过滤器 $BL(v)$ 存储其所有后代记录的编码集合 $C(v)$。为消除节点间的关联，使用节点独有的随机数 $rand_{v}$ 对每个hash值再次哈希：$\text{HMAC}(rand_{v}, \text{HMAC}(key_{i}, c))$，然后将最终值映射到 $BL(v)$。
3. **添加验证信息**：每个节点v存储验证信息 $Ver(v)$，包含：
   - **哈希标签 $HL(v)$**：类似Merkle树。叶子节点 $HL(v_l) = hash(E_i)$，内部节点 $HL(v_n) = hash(HL(v_n.left) || HL(v_n.right))$，根哈希由数据用户持有。
   - **布隆过滤器的HMAC值 $HB(v)$**：用于验证布隆过滤器完整性。为减少通信，布隆过滤器被分为若干段，每段有独立的HMAC，仅返回被查询命中的段。

**查询处理**过程如下：数据用户将查询Q编码为矩阵 $M(Q)$，其中每个元素 $T_i$ 包含对编码 $c_i$ 的r次HMAC哈希值。云服务器从根节点开始自上而下搜索：对节点v，将 $M(Q)$ 中的每个 $T_i$ 用 $rand_v$ 重哈希后映射到 $BL(v)$。若 $T_i$ 所有位均命中，则 $v$ 下可能有匹配记录，继续搜索其子节点，并将 $T_i$ 保留；若某位未命中，则 $T_i$ 不匹配，将其从 $M(Q)$ 移除。搜索在 $M(Q)$ 为空或到达叶子节点时终止。同时，服务器生成验证证明 $\pi$，包括所有“关键节点”（匹配的叶子节点和有一项或多项不匹配的内部节点）及其哈希标签、布隆过滤器（相关段）、随机数 $rand_v$，以及不匹配陷阱门集 $UMT(v)$ 和匹配陷阱门集 $MT(v)$。

**验证机制**包括正确性和完备性验证：
- **正确性**：用户首先解密结果并检查其是否在查询范围内。然后，利用证明中的哈希标签从叶子向上计算根哈希，若与已知根哈希一致，则证明结果集和关键节点均未被篡改且属于原数据集。
- **完备性**：对于每条搜索路径，用户用证明信息重现查询过程。若每条路径上所有不匹配陷阱门和匹配叶子陷阱门的并集恰好等于原始陷阱门集 $M(Q)$，则证明服务器没有遗漏任何分支，结果是完备的。

**安全性分析**遵循理想-现实模拟范式。定义泄露函数 $L_1$（泄露数据规模、布隆过滤器长度和树结构）和 $L_2$（泄露访问模式、搜索模式和路径模式）。定理1指出，若两个数据集规模相同，其SVETree索引是计算上不可区分的，因为树结构仅由数据量决定，且数据被随机划分。定理2指出，若HMAC是伪随机函数，则ServeDB是L-自适应的安全（L-secure against adaptive attacks）。这保证了即使云服务器能看到查询和访问模式，也无法获取数据内容和查询内容的明文。

**性能复杂度**：查询时间复杂度为 $O(\log|D|)$，验证时间与关键节点数量相关，通信开销约为结果数据量的15%。

### 核心公式与流程

**[分层立方体编码]**
$$c_{i} = \text{HMAC}(K, (g_{i}.x + g_{i}.y + L_{i}))$$
> 作用：将多维空间中的一个立方体（由其中心点和层级标识）映射为一个唯一的、不可逆的编码，用于在布隆过滤器中进行匹配。

**[布隆过滤器节点构建]**
对于节点 $v$ 中的每个编码 $c$，执行以下操作将其插入布隆过滤器 $BL(v)$：
$$\text{For each } key_j \in HK: h_{j} = \text{HMAC}(key_j, c)$$
$$\text{Final position } p_{j} = \text{HMAC}(rand_v, h_{j}) \mod \text{Len}(BL(v))$$
> 作用：使用节点独有的随机数 $rand_v$ 对编码的哈希结果进行重哈希，确保不同节点中相同编码的哈希值不同，从而消除节点间的关联性，保护数据隐私。

**[SVETree节点哈希标签生成（Merkle验证）]**
叶子节点 $v_l$： $HL(v_l) = hash(E_i)$
内部节点 $v_n$：  $HL(v_n) = hash(HL(v_n.left) || HL(v_n.right))$
> 作用：构建从数据到根哈希的Merkle树结构，用于验证查询结果和中间节点的数据完整性和来源，防止服务器伪造或替换数据。

**[查询匹配与不匹配验证]**
在节点 $v$ 处，对于陷阱门 $T_i$：
$$\text{For each } t_{ij} \in T_i: \text{ check } BL(v)[\text{HMAC}(rand_v, t_{ij}) \mod \text{Len}] \stackrel{?}{=} 1$$
若所有位置均为1，则 $T_i$ 匹配；否则 $T_i$ 不匹配。
> 作用：在查询过程中判断一个查询编码是否可能落在一个节点所包含的数据范围内，若所有检查位都为1则为“可能匹配”，否则为“必然不匹配”。该判定方法决定了搜索路径的走向和验证信息的生成。

### 实验结果
实验在Windows 7 Professional机器（3.5GHz i7-4770k处理器，32GB内存）上进行，使用C++实现。使用了包含500万条推文的Twitter数据集和包含50万条记录的Foursquare数据集，基线方法包括PBtree、Log-SRC-i、R-tree和Scan。在查询延迟方面，当维数大于1时，PBtree和Log-SRC-i因需做交集运算导致延迟快速增长，而ServeDB的延迟几乎不受维数影响。在数据集为100万、维度为3时，ServeDB的平均查询延迟约为30毫秒，比PBtree和Log-SRC-i快至少19倍。在验证延迟方面，对包含1百万条记录的数据集，验证过程平均仅需约12毫秒，且基本不受查询范围大小影响。通信开销方面，验证所需的额外数据（证明信息）约为返回结果数据量的15%，部分源自布隆过滤器段的传输。在查询精度方面，由于使用分层立方体编码，ServeDB会产生约10-15%的假阳性率，而PBtree约为5%，Log-SRC-i约为30%。虽然ServeDB的假阳性率比PBtree稍高，但用户可在本地通过解密结果并过滤轻松解决。实验还评估了多维查询扩展（多树、查询扩展、混合方法）的性能，表明多树方法延迟最低但存储开销大，查询扩展方法延迟稍高但存储开销小。总体而言，ServeDB在实现亚线性查询和验证时间的同时，具备了良好的可扩展性和实际部署潜力。

### 局限性与开放问题
论文主要针对数值属性数据进行设计，虽然提及可扩展至非数值数据，但未给出具体处理方案。实验评估了假阳性问题，但未深入探讨布隆过滤器参数（如长度、哈希函数数量）对假阳性率和查询性能之间权衡的系统性影响。提出的安全性模型主要防范服务器从索引和查询中学习数据信息，但明确不防御侧信道攻击（如访问模式分析），因此在实际部署中可能需要配合Padding等技术，这会增加额外的存储和计算开销。动态更新操作虽然被提及，但论文未详细评估更新操作的性能开销及其对索引结构平衡性和隐私性的长期影响。

### 强关联论文

[2] Agrawal et al. Order preserving encryption for numeric data. **SIGMOD 2004** [Google Scholar](https://scholar.google.com/scholar?q=Order+preserving+encryption+for+numeric+data)

[5] Stefanov et al. Practical dynamic searchable encryption with small leakage. **NDSS 2014** [Google Scholar](https://scholar.google.com/scholar?q=Practical+dynamic+searchable+encryption+with+small+leakage)

[7] Popa et al. CryptDB: protecting confidentiality with encrypted query processing. **SOSP 2011** [Google Scholar](https://scholar.google.com/scholar?q=CryptDB+protecting+confidentiality+with+encrypted+query+processing)

[8] Wang et al. Secure and efficient range queries on outsourced databases using RP-trees. **ICDE 2013** [Google Scholar](https://scholar.google.com/scholar?q=Secure+and+efficient+range+queries+on+outsourced+databases+using+RP-trees)

[10] Li et al. Fast and scalable range query processing with strong privacy protection for cloud computing. **IEEE/ACM ToN 2016** [Google Scholar](https://scholar.google.com/scholar?q=Fast+and+scalable+range+query+processing+with+strong+privacy+protection+for+cloud+computing)

[11] Demertzis et al. Practical private range search revisited. **SIGMOD 2016** [Google Scholar](https://scholar.google.com/scholar?q=Practical+private+range+search+revisited)

[23] Szydlo. Merkle tree traversal in log space and time. **Eurocrypt 2004** [Google Scholar](https://scholar.google.com/scholar?q=Merkle+tree+traversal+in+log+space+and+time)

[26] Papadopoulos et al. Taking authenticated range queries to arbitrary dimensions. **CCS 2014** [Google Scholar](https://scholar.google.com/scholar?q=Taking+authenticated+range+queries+to+arbitrary+dimensions)

[28] Curtmola et al. Searchable symmetric encryption: improved definitions and efficient constructions. **Journal of Computer Security 2011** [Google Scholar](https://scholar.google.com/scholar?q=Searchable+symmetric+encryption+improved+definitions+and+efficient+constructions)


## 关键词

+ 多维范围查询
+ 加密数据查询
+ 分层立方体编码
+ 安全树索引
+ 可验证性
+ 隐私保护