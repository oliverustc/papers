---
title: "Vector commitments and their applications"
标题简称:
论文类型: conference
会议简称: PKC
发表年份: 2013
---

## Vector commitments and their applications

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-642-36362-7_5)

## 作者

+ Dario Catalano 
+ [Dario Fiore](Dario%20Fiore.md)
## 笔记

### 背景与动机

在密码学中，承诺方案是构建高级协议的基本工具，但传统的承诺方案仅支持对单个消息的绑定和隐藏，无法高效处理有序序列的多值承诺。许多实际应用，如可验证数据库、零知识集合和动态累加器，都需要对一组数据进行安全且紧凑的承诺，并支持对特定位置的打开和更新。现有方案要么依赖非标准假设（如q-强Diffie-Hellman），要么在效率或功能上存在瓶颈：例如基于Merkle树的零知识集合产生线性长度的证明，可验证数据库方案[4]不支持公开验证，而动态累加器方案[18, 27, 7]在素数阶群中仅支持有界多项式大小集合且依赖较新的假设。Catalano和Fiore提出**向量承诺**（Vector Commitment, VC）这一新原语，旨在以简洁的方式（承诺和打开大小与向量长度无关）实现序列承诺，并支持高效更新，从而解决上述应用中的共性挑战。

### 相关工作

[4] Benabbas等. Verifiable delegation of computation over large datasets. **CRYPTO 2011** [Google Scholar](https://scholar.google.com/scholar?q=Verifiable+delegation+of+computation+over+large+datasets)
> 核心思路：提出可验证数据库（VDB）形式化定义，利用合数阶双线性群中的常数大小假设构造方案，但仅支持私有验证。
> 局限与区别：不支持公开验证，且依赖合数阶群；本文利用VC实现了公开可验证的VDB，且若采用CDH实例可在素数阶群中工作。

[10] Catalano等. Zero-knowledge sets with short proofs. **EUROCRYPT 2008** [Google Scholar](https://scholar.google.com/scholar?q=Zero-knowledge+sets+with+short+proofs)
> 核心思路：通过q元树和q-陷阱门mercurial承诺构造紧凑的零知识集合（ZK-EDB），但具体构造中硬打开长度与q线性相关。
> 局限与区别：硬打开线性增长导致非成员证明远长于成员证明；本文用VC结合标准mercurial承诺得到简洁的q-野性承诺，使两种证明都达到常数大小。

[12] Chase等. Mercurial commitments with applications to zero-knowledge sets. **EUROCRYPT 2005** [Google Scholar](https://scholar.google.com/scholar?q=Mercurial+commitments+with+applications+to+zero-knowledge+sets)
> 核心思路：定义陷阱门mercurial承诺，并利用Merkle树和碰撞抵抗哈希函数构造ZK-EDB，证明长度与树深度成正比。
> 局限与区别：证明长度线性于安全参数；本文通过VC将其推广到q元树，实现了紧凑证明。

[14] Gennaro和Micali. Independent zero-knowledge sets. **ICALP 2006** [Google Scholar](https://scholar.google.com/scholar?q=Independent+zero-knowledge+sets)
> 核心思路：提出独立零知识数据库概念，基于离散对数或强RSA假设构造多陷阱门mercurial承诺。
> 局限与区别：未考虑紧凑性；本文利用VC构造多陷阱门q-mercurial承诺，实现紧凑的独立ZK-EDB。

[20] Libert和Yung. Concise mercurial vector commitments and independent zero-knowledge sets with short proofs. **TCC 2010** [Google Scholar](https://scholar.google.com/scholar?q=Concise+mercurial+vector+commitments+and+independent+zero-knowledge+sets+with+short+proofs)
> 核心思路：直接构造简洁的q-mercurial承诺，基于q-DHE假设，实现短证明的ZK-EDB。
> 局限与区别：依赖非标准q-DHE假设；本文基于标准CDH和RSA假设实现类似功能，且支持可更新。

[21] Liskov. Updatable zero-knowledge databases. **ASIACRYPT 2005** [Google Scholar](https://scholar.google.com/scholar?q=Updatable+zero-knowledge+databases)
> 核心思路：定义可更新零知识数据库，基于离散对数的可更新mercurial承诺构造，证明和更新长度与树深度线性。
> 局限与区别：证明和更新长度随树深度增长；本文利用VC构造可更新q-mercurial承诺，实现了紧凑的可更新ZK-EDB，证明和更新更短。

[7] Camenisch等. An accumulator based on bilinear maps and efficient revocation for anonymous credentials. **PKC 2009** [Google Scholar](https://scholar.google.com/scholar?q=An+accumulator+based+on+bilinear+maps+and+efficient+revocation+for+anonymous+credentials)
> 核心思路：基于双线性映射的累加器，支持动态更新，但假设强度较高。
> 局限与区别：依赖非标准假设；本文展示VC可泛化累加器，基于CDH即可构造通用动态累加器。

[18] Li等. Universal accumulators with efficient nonmembership proofs. **ACNS 2007** [Google Scholar](https://scholar.google.com/scholar?q=Universal+accumulators+with+efficient+nonmembership+proofs)
> 核心思路：提出通用累加器，支持成员和非成员证明，基于q-SDH假设。
> 局限与区别：依赖q型假设；本文基于标准CDH提供了首个素数阶群中的通用动态累加器。

### 核心技术与方案

**1. 向量承诺形式化定义**  
VC包含七个算法：KeyGen生成公参pp（隐式定义消息空间）；Com对向量$(m_1,\dots,m_q)$输出承诺$C$和辅助信息aux；Open针对位置$i$输出证明$\Lambda_i$；Ver验证$\Lambda_i$是否正确打开到$m_i$；Update由承诺者运行，将第$i$个消息更新为$m'$，输出新承诺$C'$和更新信息$U$；ProofUpdate允许持有旧证明的用户根据$U$更新证明。安全性要求**位置绑定**：PPT敌手不能对同一个$C$在同一位置打开出两个不同消息。简洁性要求承诺和证明大小与$q$独立。

**2. 基于CDH的VC构造**  
设$\mathbb{G}$为素数阶$p$的双线性群，$g$为生成元。KeyGen随机选取$z_1,\dots,z_q\in\mathbb{Z}_p$，计算$h_i=g^{z_i}$（$i\in[q]$）以及$h_{i,j}=g^{z_i z_j}$（$i\neq j$）。Com输出$C=\prod_{i=1}^q h_i^{m_i}$。Open输出$\Lambda_i=\prod_{j\neq i} h_{i,j}^{m_j}$。Ver检查$e(C/h_i^{m_i},h_i)=e(\Lambda_i,g)$。Update将$C$乘以$h_i^{m'-m}$，$U=(m,m',i)$。ProofUpdate分$i\neq j$和$i=j$两种情形更新$\Lambda_j$。安全性归结为Square-CDH问题：若敌手在位置$i$打开两个不同消息，则可提取$g^{a^2}$。

**3. 基于RSA的VC构造**  
KeyGen生成RSA模$N$，随机选取$q$个$(\ell+1)$-bit素数$e_1,\dots,e_q$，随机选择$a\in\mathbb{Z}_N^*$，计算$S_i=a^{\prod_{j\neq i}e_j}\bmod N$。Com输出$C=\prod_{i=1}^q S_i^{m_i}\bmod N$。Open输出$\Lambda_i=(\prod_{j\neq i}S_j^{m_j})^{1/e_i}\bmod N$。Ver检查$C=S_i^{m}\Lambda_i^{e_i}\bmod N$。安全性基于RSA假设：若敌手在位置$i$打开出$m\neq m'$，则利用Shamir技巧可计算$a$的$e_i$次根。更新算法类似CDH方案，ProofUpdate涉及$e_j$次根计算。

**4. 常数公参的RSA变体**  
通过使用伪随机函数和Waters-Hohenberger技巧，将公参压缩为$(N,a,s,c)$，其中$s$为PRF种子，$c$为随机串，$e_i$由$F_{s,c}(i)$动态生成。安全性证明结合RSA假设和伪随机性。

**5. 应用之一：可验证数据库（VDB）**  
利用VC构造VDB：Setup对数据库向量$(v_1,\dots,v_q)$计算承诺$C$作为公开密钥PK；Query返回打开$\Lambda_x$；ClientUpdate通过VC.Update更新记录；ServerUpdate存储更新信息。安全性由VC的位置绑定保证：若敌手伪造证明，则可在同一位置产生两个不同打开。该方案支持公开验证，且若采用CDH实例，基于素数阶群的标准假设。公参大小可通过优化使验证者仅存储常数个元素（使用签名验证$h_i$）。

**6. 应用之二：可更新零知识数据库（ZK-EDB）**  
定理10指出：VC与陷阱门mercurial承诺组合可构造简洁的q-陷阱门mercurial承诺（qTMC）。具体地，qTMC的承诺是对$q$个mercurial承诺的向量再做一次VC；证明包含VC打开和对应mercurial打开。安全性证明分两类碰撞：若两个打开的$C_i$相等则破坏mercurial绑定，若不等则破坏VC位置绑定。将该qTMC嵌入Catalano等[10]的q元树构造，即可得到紧凑的ZK-EDB（成员和非成员证明均为常数大小）。进一步，结合可更新mercurial承诺，可得到可更新ZK-EDB，且证明和更新信息长度与树高$\log_q 2^k$成正比，优于Liskov方案[21]的线性大小。

**7. 应用之三：通用动态累加器**  
利用VC构造UDA：将集合$V\subseteq[n]$编码为二进制向量（$m_i=1$若$i\in V$，否则0），承诺值即为累加值；添加/删除元素通过VC.Update修改对应位；成员/非成员证明对应打开值为1或0的证明。安全性直接由位置绑定保证：若敌手对同一元素同时提供成员和非成员证明，则产生位置绑定冲突。该构造基于CDH即可在素数阶群中实现，避免了非标准假设。

### 核心公式与流程

**[基于CDH的VC承诺与验证]**
$$C = \prod_{i=1}^{q} h_i^{m_i}, \quad \Lambda_i = \prod_{j\neq i} h_{i,j}^{m_j}, \quad e(C / h_i^{m_i}, h_i) = e(\Lambda_i, g)$$
> 作用：承诺是对消息的指数乘积，打开验证利用双线性配对确保承诺与打开一致。

**[基于RSA的VC承诺与验证]**
$$C = \prod_{i=1}^{q} S_i^{m_i} \bmod N, \quad \Lambda_i = \Bigl(\prod_{j\neq i} S_j^{m_j}\Bigr)^{1/e_i} \bmod N, \quad C = S_i^{m} \Lambda_i^{e_i} \bmod N$$
> 作用：承诺是RSA累乘，打开是$e_i$次根，验证通过指数运算检查。

**[VC.Update算法（CDH版本）]**
$$C' = C \cdot h_i^{m'-m}, \quad \Lambda_j' = \begin{cases} \Lambda_j \cdot h_{j,i}^{m'-m} & \text{if } i \neq j \\ \Lambda_i & \text{if } i = j \end{cases}$$
> 作用：更新第$i$个消息时，承诺乘以$h_i^{m'-m}$，已有证明在$i\neq j$时需乘以$h_{j,i}^{m'-m}$。

**[qTMC构造（VC+mercurial承诺）]**
$$\text{qHCom}(m_1,\dots,m_q): \forall i, (C_i,\text{aux}_i) \gets \text{HCom}(m_i); \quad (C,\text{aux}_\text{VC}) \gets \text{VC.Com}(C_1,\dots,C_q).$$
$$\varLambda_i \gets \text{VC.Open}(C_i,i,\text{aux}_\text{VC}), \quad \tau_i = (\varLambda_i, C_i, \pi_i).$$
> 作用：将$q$个消息先分别用mercurial承诺提交，再对承诺值向量做VC，证明包含VC打开和mercurial打开。

### 实验结果

本文未提供实验评估，属于纯理论密码学工作。所有构造均以安全定义和归约证明的形式呈现，未涉及真实系统实现或基准测试。文中关于效率的讨论仅限于渐进复杂度比较：例如基于CDH的VC公共参数大小为$O(q^2)$，验证者可优化至$O(q)$；基于RSA的常数公参变体牺牲计算效率换取公参独立性。在VDB应用中，客户端更新和验证时间与数据库大小无关。在ZK-EDB应用中，证明大小与树高$\log_q 2^k$成正比，而以往方案[21]为线性于$k$。在累加器应用中，首次在素数阶群中基于标准CDH假设实现通用动态累加器。

### 局限性与开放问题

本文构造的VC在基于CDH的方案中公参大小为$O(q^2)$，对于大规模$q$可能造成存储瓶颈；虽然给出了优化使验证者仅需$O(q)$，但承诺者仍需完整集合。基于RSA的常数公参变体计算效率较低。另外，本文未涉及隐藏性质的VC形式化定义及其应用，例如匿名凭证场景需要隐藏向量内容。未来工作可探索更高效的VC构造（如线性公参、后量子安全），以及将VC应用于更广泛的密码协议如可验证计算、区块链轻客户端等。

### 强关联论文

[4] Siavosh Benabbas, Rosario Gennaro, and Yevgeniy Vahlis. Verifiable delegation of computation over large datasets. **CRYPTO 2011** [Google Scholar](https://scholar.google.com/scholar?q=Verifiable+delegation+of+computation+over+large+datasets)

[10] Dario Catalano, Dario Fiore, and Mariagrazia Messina. Zero-knowledge sets with short proofs. **EUROCRYPT 2008** [Google Scholar](https://scholar.google.com/scholar?q=Zero-knowledge+sets+with+short+proofs)

[12] Melissa Chase, Alexander Healy, Anna Lysyanskaya, Tal Malkin, and Leonid Reyzin. Mercurial commitments with applications to zero-knowledge sets. **EUROCRYPT 2005** [Google Scholar](https://scholar.google.com/scholar?q=Mercurial+commitments+with+applications+to+zero-knowledge+sets)

[14] Rosario Gennaro and Silvio Micali. Independent zero-knowledge sets. **ICALP 2006** [Google Scholar](https://scholar.google.com/scholar?q=Independent+zero-knowledge+sets)

[20] Benoît Libert and Moti Yung. Concise mercurial vector commitments and independent zero-knowledge sets with short proofs. **TCC 2010** [Google Scholar](https://scholar.google.com/scholar?q=Concise+mercurial+vector+commitments+and+independent+zero-knowledge+sets+with+short+proofs)

[21] Moses Liskov. Updatable zero-knowledge databases. **ASIACRYPT 2005** [Google Scholar](https://scholar.google.com/scholar?q=Updatable+zero-knowledge+databases)

[7] Jan Camenisch, Markulf Kohlweiss, and Claudio Soriente. An accumulator based on bilinear maps and efficient revocation for anonymous credentials. **PKC 2009** [Google Scholar](https://scholar.google.com/scholar?q=An+accumulator+based+on+bilinear+maps+and+efficient+revocation+for+anonymous+credentials)

[18] Jiangtao Li, Ninghui Li, and Rui Xue. Universal accumulators with efficient nonmembership proofs. **ACNS 2007** [Google Scholar](https://scholar.google.com/scholar?q=Universal+accumulators+with+efficient+nonmembership+proofs)

[24] Silvio Micali, Michael O. Rabin, and Joe Kilian. Zero-knowledge sets. **FOCS 2003** [Google Scholar](https://scholar.google.com/scholar?q=Zero-knowledge+sets)

[8] Jan Camenisch and Anna Lysyanskaya. Dynamic accumulators and application to efficient revocation of anonymous credentials. **CRYPTO 2002** [Google Scholar](https://scholar.google.com/scholar?q=Dynamic+accumulators+and+application+to+efficient+revocation+of+anonymous+credentials)


## 关键词

+ 向量承诺
+ 位置绑定
+ 简洁承诺
+ 可验证数据库
+ 动态累加器
+ 零知识数据库