---
title: "Drynx: Decentralized, Secure, Verifiable System for Statistical Queries and Machine Learning on Distributed Datasets"
标题简称: Drynx
论文类型: journal
期刊简称: TIFS
发表年份: 2020
modified: 2025-04-09 09:20:27
---

## Drynx: Decentralized, Secure, Verifiable System for Statistical Queries and Machine Learning on Distributed Datasets

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/document/9019831)

## 作者

+ David Froelicher; 
+ Juan Ramón Troncoso-Pastoriza; 
+ Joao Sa Sousa; 
+ [Jean-Pierre Hubaux](Jean-Pierre%20Hubaux.md)
## 笔记

### 背景与动机
在医疗、金融等涉及敏感数据的领域，对分布式数据集进行统计分析和机器学习模型训练的需求日益迫切，但隐私保护法规（如GDPR）和伦理约束大大制约了数据的直接共享与集中化处理。中心化的数据仓库（如CryptDB [8]）虽然能提供一定程度的加密查询，却引入了单点故障风险，一旦被攻破将导致大规模数据泄露（如Equifax事件 [4]）。现有的去中心化数据共享系统（如Sharemind [22]）大多假设计算节点是诚实但好奇的，无法抵御恶意敌手，且通常只支持简单的求和操作，缺乏对输入数据正确性和计算过程完整性的可审计性保证。Drynx旨在填补这一空白：在无需信任任何单一实体的强敌手模型下，首次实现了一个支持多种统计查询与机器学习回归模型训练的去中心化系统，同时保证了数据机密性、数据提供者隐私、结果鲁棒性以及计算正确性。

### 相关工作

[16] Froelicher et al. **UnLynx: A decentralized system for privacy-conscious data sharing.** *PoPETs 2017* [Google Scholar](https://scholar.google.com/scholar?q=UnLynx%3A+A+decentralized+system+for+privacy-conscious+data+sharing)
> 核心思路：提出了一个基于同态加密和交互式协议的去中心化系统，支持分布式数据集上的安全求和操作。
> 局限与区别：仅支持求和运算；假设数据提供者是诚实但好奇的，不提供结果鲁棒性；缺乏实用的可审计性方案。Drynx在此基础上扩展了多种操作，并引入了恶意数据提供者模型和分布式认证机制。

[26] Corrigan-Gibbs & Boneh. **Prio: Private, Robust, and Computation of Aggregate Statistics.** *NSDI 2017* [Google Scholar](https://scholar.google.com/scholar?q=Prio%3A+Private%2C+Robust%2C+and+Computation+of+Aggregate+Statistics)
> 核心思路：使用秘密共享和非交互式证明，让数据提供者证明输入值在合法范围内，从而实现鲁棒的聚合统计。
> 局限与区别：Prio的鲁棒性仅在所有计算节点均为诚实但好奇时才成立；不保护数据提供者之间的隐私（例如，可以推断某个提供者是否参与查询）。Drynx的Anytrust模型允许大多数节点恶意，且额外提供了数据提供者隐私（如中立响应、差分隐私）。

[10] Bater et al. **SMCQL: Secure querying for federated databases.** *VLDB 2017* [Google Scholar](https://scholar.google.com/scholar?q=SMCQL%3A+Secure+querying+for+federated+databases)
> 核心思路：利用安全多方计算（MPC）技术，在分布式数据库上执行SQL查询。
> 局限与区别：SMCQL假设数据提供者和计算节点都是诚实的；不提供对计算正确性的可验证性（零知识证明）。Drynx对所有计算步骤都提供公开可验证的零知识证明，并假设潜在恶意参与方。

[33] Aono et al. **Scalable and secure logistic regression via homomorphic encryption.** *CODASPY 2016* [Google Scholar](https://scholar.google.com/scholar?q=Scalable+and+secure+logistic+regression+via+homomorphic+encryption)
> 核心思路：利用同态加密实现两方或三方场景下的逻辑回归训练，假设服务器是诚实但好奇的。
> 局限与区别：该方案需要数据集中化到单个服务器；不提供计算结果正确性的证明，也不考虑恶意数据提供者。Drynx通过可编码操作的框架实现了去中心化的逻辑回归，并提供了完整的安全性保证。

### 核心技术与方案

Drynx的系统模型包含四类实体：数据提供者（DPs）持有本地数据集；计算节点（CNs）集体执行同态操作；验证节点（VNs）并行验证正确性并存储至区块链；查询者（Q）发起查询并接收最终结果。系统采用Anytrust威胁模型：只要至少一个CN是诚实的，即可保证安全；DPs和Q被认为是恶意的。

核心技术栈包括：基于椭圆曲线ElGamal（ECEG）的加法同态加密，分散密钥（集体公钥 K，私钥碎片 k_i）；Camensch-Stadler型零知识证明（ZKP）用于证明离散对数关系（如密钥切换的正确性）；Camenisch-Chaabouni范围证明（改进至Anytrust模型）用于验证DP输入值在 [b_l, b_u) 内；以及分布式的Neff可验证洗牌用于差分隐私噪声添加。系统使用基于skipchain的许可区块链来不可篡改地存储验证映射，公众审计时仅需检查区块头。

核心安全架构建立在三个层次上：(1) 数据机密性通过端到端加密和集体密钥切换保护，CTKS协议（协议1）将解密能力和聚合结果一并从C1传递到Q，密文始终对除Q外的各方保密。(2) 数据提供者（DP）隐私通过三个子机制实现：中立响应使DP可以选择发送一个不影响聚合结果的零元；集体树混淆（CTO，协议2）用于位运算，将二进制结果乘随机数再解密；分布式差分隐私（CDP，协议3）在聚合结果上添加来自Laplace分布的噪声，该噪声由CNs集体洗牌以避免任何单一实体知晓其真实值。(3) 查询执行正确性通过并行审计框架保障：DP生成范围证明（算法1），每个CN在执行CTA、CTO、CTKS或CDP时都生成对应的ZKP；所有证明送交VNs，VNs以可配置概率(T, T_sub)验证后将结果写入区块链，审计者只需检查区块链即可。

所有协议的计算复杂度和通信开销已由论文给出。对于单条密文的操作：CTA的计算开销为(CN-1)次同态加法，通信量为CN·4p字节（约0.768KB）；CTKS的计算开销为(CN-1)次加法加上3·CN次标量乘法，通信量为CN·6p字节（约1.344KB）；包含范围证明的DP响应通信量为DP·(1.28KB)，但验证带宽膨胀至约2.43MB，主要由大配对点（384B）引起。

### 核心公式与流程

**[ElGamal加密与同态性]**
$$E_{\Omega}(m) = (rB, mB + r\Omega)$$
$$E_{\Omega}(\alpha m_1 + \beta m_2) = \alpha E_{\Omega}(m_1) + \beta E_{\Omega}(m_2)$$
> 作用：提供加法同态加密基础，用于安全聚合。

**[集体树密钥切换（CTKS）核心公式]**
$$\text{Input: } E_K(m) = (C_1, C_2), \quad \text{Output: } E_{K'}(m) = (C'_1, C'_2)$$
$$C'_1 = \sum a_i B, \quad C'_2 = C_2 + \sum (- (C_1)k_i + a_i K')$$
> 作用：将聚合结果从集体公钥K下转换到查询者公钥K'下，而无需解密，且只需一次聚合即可完成。

**[集体树混淆（CTO）核心公式]**
$$\text{Output: } E_K(sm) = s \cdot (C_1, C_2), \quad s = \sum s_i$$
> 作用：将1混淆为随机值，0保持不变，从而隐藏参与位运算的DP个数。

**[范围证明（Anytrust模型）验证方程]**
$$D = C_2 c + \Omega z_r + \sum_j B u^j z_{m_j}$$
$$a_{i,j} = e(V_{i,j}, Z_i)c - z_{m_j} \cdot e(V_{i,j}, B) + z_{v_j} \cdot e(B, B)$$
> 作用：允许任何验证者检查DP的秘密值m是否在[0, u^l)范围内，而无需泄露m。通过合并所有CN的公钥使得只要一个CN诚实，DP就无法伪造证明。

**[查询验证的证明区块链结构]**
> 作用：每个VNs验证并存储所有DPs和CNs产生的证明，经Byzantine容错共识后形成不可篡改的区块，审计者只需检查区块头即可完成审计。

### 实验结果

实验在Mininet模拟的虚拟网络（100Mbps带宽，20ms延迟）上进行，共使用13台Intel Xeon E5-2680 v3机器，默认配置6个CN和7个VN。对于逻辑回归训练任务（12个特征，60万条记录，12个DP，100次迭代），查询执行时间约 1.5 秒，而并行运行的证明验证时间约 21.9 秒，区块链区块插入时间约 0.4 秒。系统扩展性测试显示，当记录数从600增加到600,000且DP数固定为10时，总时间（执行+验证）约从2.2秒增长至4.4秒；而当DP数等于记录数时，总时间在60万条记录下达到约3,287秒。与Prio [26]的直接对比显示，在相同的诚实但好奇模型下，Drynx的min操作（无CTO、无范围证明）在48个DP时（15秒）比Prio（244秒）快一个数量级以上；即便启用了完整安全功能（CTO + 范围证明），Drynx的扩展性仍与Prio相当，但提供了更强的安全模型。通信带宽分析表明，CTKS步骤中每个CN的通信量约1.344 kB；范围证明验证的带宽增至2.4 MB，主要由配对点大小（384B）导致。

### 局限性与开放问题

Drynx的位运算方案在未启用CTO时存在概率性错误（约1/(#G-1)），该错误虽小但理论上非零；迭代查询（如最大值搜索）会泄露中间结果的区间范围，系统虽通过熵限制（EL）控制泄露量，但未采用差分隐私来隐藏中间值。此外，Drynx假设CNs必须全部在线才能成功完成CTA和CTKS步骤，这在节点易故障的环境中构成单一故障点。系统未支持神经网络训练，且对于预处理加密数据（数据静态加密）灵活性有限，因为DP必须预置所有可能的输入表示。最后，论文的威胁模型未考虑针对隐私审计者的拒绝服务攻击（如攻击VNs）以及激励兼容性问题（如何确保CNs有动机诚实地执行验证）。

### 强关联论文

[16] Froelicher et al. **UnLynx: A decentralized system for privacy-conscious data sharing.** *PoPETs 2017* [Google Scholar](https://scholar.google.com/scholar?q=UnLynx%3A+A+decentralized+system+for+privacy-conscious+data+sharing)

[26] Corrigan-Gibbs & Boneh. **Prio: Private, Robust, and Computation of Aggregate Statistics.** *NSDI 2017* [Google Scholar](https://scholar.google.com/scholar?q=Prio%3A+Private%2C+Robust%2C+and+Computation+of+Aggregate+Statistics)

[8] Popa et al. **CryptDB: Protecting confidentiality with encrypted query processing.** *SOSP 2011* [Google Scholar](https://scholar.google.com/scholar?q=CryptDB%3A+Protecting+confidentiality+with+encrypted+query+processing)

[5] Bindschaedler et al. **Plausible deniability for privacy-preserving data synthesis.** *VLDB 2017* [Google Scholar](https://scholar.google.com/scholar?q=Plausible+deniability+for+privacy-preserving+data+synthesis)

[33] Aono et al. **Scalable and secure logistic regression via homomorphic encryption.** *CODASPY 2016* [Google Scholar](https://scholar.google.com/scholar?q=Scalable+and+secure+logistic+regression+via+homomorphic+encryption)

[27] Nikolaenko et al. **Privacy-preserving ridge regression on hundreds of millions of records.** *IEEE S&P 2013* [Google Scholar](https://scholar.google.com/scholar?q=Privacy-preserving+ridge+regression+on+hundreds+of+millions+of+records)

[32] Juvekar et al. **Gazelle: A low latency framework for secure neural network inference.** *USENIX Security 2018* [Google Scholar](https://scholar.google.com/scholar?q=Gazelle%3A+A+low+latency+framework+for+secure+neural+network+inference)

[30] Mohassel & Zhang. **SecureML: A system for scalable privacy-preserving machine learning.** *IEEE S&P 2017* [Google Scholar](https://scholar.google.com/scholar?q=SecureML%3A+A+system+for+scalable+privacy-preserving+machine+learning)

[69] Neff. **Verifiable mixing (shuffling) of ElGamal pairs.** *VHTi Technical Document 2003* [Google Scholar](https://scholar.google.com/scholar?q=Verifiable+mixing+%28shuffling%29+of+ElGamal+pairs)

[56] Camenisch & Chaabouni. **Efficient protocols for set membership and range proofs.** *ASIACRYPT 2008* [Google Scholar](https://scholar.google.com/scholar?q=Efficient+protocols+for+set+membership+and+range+proofs)


## 关键词

+ Drynx去中心化隐私统计分析
+ 同态加密分布式数据计算
+ 零知识正确性证明
+ 差分隐私机器学习训练
+ 去中心化可验证查询
+ 多方安全计算审计性