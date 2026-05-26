---
title: "Zerocash: Decentralized anonymous payments from bitcoin"
标题简称:
论文类型: conference
会议简称: S&P
发表年份: 2014
created: 2025-04-21 10:23:14
modified: 2025-04-21 10:24:07
---

## Zerocash: Decentralized anonymous payments from bitcoin

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/6956581)

## 作者

+ Eli Ben Sasson 
+ [Alessandro Chiesa](Alessandro%20Chiesa.md)
+ [Christina Garman](Christina%20Garman.md)
+ [Matthew Green](Matthew%20Green.md)
+ [Ian Miers](Ian%20Miers.md)
+ [Eran Tromer](Eran%20Tromer.md) 
+ Madars Virza 

## 笔记

### 背景与动机
比特币作为首个广泛采用的分布式数字货币，其交易记录全部存储于公开的区块链上。研究表明，通过分析交易图的结构和金额等信息，任何人都可以对用户进行去匿名化 [4, 5, 6]。虽然混币服务等方案可以提供一定程度的隐私保护，但它们存在延迟大、可追踪以及存在中心化信任风险等问题。现有的Zerocoin协议 [8] 通过零知识证明将交易与来源解耦，但该方案仅支持固定面额的硬币，无法隐藏交易金额和接收方，并且其证明尺寸大（超过45 kB）、验证速度慢（约450 ms），性能远逊于比特币。本文旨在填补这一空白，构建一个功能完整、性能可比的去中心化匿名支付系统，该系统能够隐藏交易的发起方、接收方和转移金额。

### 相关工作

[8] Miers 等. Zerocoin: Anonymous distributed e-cash from bitcoin. **IEEE S&P 2013** [Google Scholar](https://scholar.google.com/scholar?q=Zerocoin%3A%20Anonymous%20distributed%20e-cash%20from%20bitcoin)
> 核心思路：使用基于双离散对数证明的零知识证明，实现可交易的匿名硬币。
> 局限与区别：仅支持固定面额，无法隐藏金额和接收方，证明尺寸大且验证速度慢，本质是一个去中心化的混币器而非完整的支付方案。

[19] Danezis 等. Pinocchio Coin: building Zerocoin from a succinct pairing-based proof system. **PETShop 2013** [Google Scholar](https://scholar.google.com/scholar?q=Pinocchio%20Coin%3A%20building%20Zerocoin%20from%20a%20succinct%20pairing-based%20proof%20system)
> 核心思路：使用zk-SNARK来减少Zerocoin中证明的尺寸和验证时间。
> 局限与区别：该方案仍然只支持固定面额，且其算术电路复杂度随硬币数量超线性增长，限制了可混合的硬币数量。

[13] Parno 等. Pinocchio: nearly practical verifiable computation. **IEEE S&P 2013** [Google Scholar](https://scholar.google.com/scholar?q=Pinocchio%3A%20nearly%20practical%20verifiable%20computation)
> 核心思路：提出了一个高效的zk-SNARK协议，用于验证通用算术电路的可满足性。
> 局限与区别：本文在其协议基础上构建，并为支付系统特定的NP声明设计了手工优化的算术电路以提升性能。

[16] Ben-Sasson 等. Succinct non-interactive arguments for a von Neumann architecture. **ePrint 2013** [Google Scholar](https://scholar.google.com/scholar?q=Succinct%20non-interactive%20arguments%20for%20a%20von%20Neumann%20architecture)
> 核心思路：实现了支持自修改代码的通用计算验证的zk-SNARK，并在大型电路上降低了成本。
> 局限与区别：本文利用了该实现作为底层zk-SNARK引擎，并针对支付系统的特定算术电路进行了实例化。

### 核心技术与方案
本文的核心解决方案是构建一个**去中心化匿名支付（DAP）方案**，并给出了一个名为Zerocash的具体实例化方案。该方案基于zk-SNARK技术，将系统的匿名性与安全性形式化定义并证明。

首先，作者形式化定义了DAP方案，它包含六个算法：Setup（系统设置）、CreateAddress（创建地址）、Mint（铸造硬币）、Pour（转移/拆分/合并硬币）、VerifyTransaction（验证交易）和Receive（接收硬币）。安全性由三个属性定义：账本不可区分性（保证账本不泄露交易细节）、交易不可延展性（防止交易被篡改）和余额平衡性（防止超发货币）。构造的核心是使用**zk-SNARK证明一个特定的NP声明——POUR**。

在构造中，硬币的**硬币承诺cm**不再仅仅是序列号的承诺，而是通过两层承诺结构：$k := \text{COMM}_r(a_{pk} \| \rho)$，然后$\text{cm} := \text{COMM}_s(v \| k)$。这隐藏了所有者地址$a_{pk}$和用于派生序列号的随机数$\rho$。**POUR操作**是将一组输入硬币的价值“倒入”一组输出硬币中，同时支持公共输出。其对应的NP声明POUR验证：(1) 输入硬币的承诺存在于Merkle树中；(2) 序列号由地址密钥和随机数正确计算；(3) 新旧硬币结构和价值守恒（$v_1^{new} + v_2^{new} + v_{pub} = v^{old}$）；(4) 用于实现隐私的伪随机函数计算正确。为抵御交易延展性攻击，方案还引入了一次性签名来绑定交易的所有字段，并使用密钥隐私加密方案在账本上传递新硬币的秘密值，从而实现无需额外通信通道的直接支付。

Zerocash实例化基于SHA256实现所有密码学原语，并将POUR声明编译成一个手工优化的算术电路$C_{\text{POUR}}$（包含64层Merkle树验证）。整个方案依赖于一次可信设置来生成公共参数，但安全性证明表明，即使设置被攻破，匿名性仍能保持。

### 核心公式与流程

**[硬币承诺构造]**
$$k := \text{COMM}_r(a_{\text{pk}} \| \rho)$$
$$\text{cm} := \text{COMM}_s(v \| k)$$
> 作用：将用户地址、序列号随机数和价值通过两层承诺隐藏。外层怀疑者可以验证硬币价值$v$与承诺$\text{cm}$的关系，但无法知道所有者$a_{pk}$和序列号衍生随机数$\rho$。

**[硬币序列号计算]**
$$\text{sn} := \text{PRF}_{a_{\text{sk}}}^{\text{sn}}(\rho)$$
> 作用：使用用户的地址密钥和硬币特有的随机数$\rho$（而非承诺本身）来确定序列号。这确保了只有知道地址密钥的用户才能正确花费硬币，且花费前序列号对所有人（包括原所有者）都是不可预测的。

**[POUR声明核心验证]**
$$v_1^{\text{new}} + v_2^{\text{new}} + v_{\text{pub}} = v^{\text{old}}$$
> 作用：保证在匿名转移过程中，输入硬币的总价值与输出硬币的总价值（包括公共输出）相等，防止凭空创造货币。

**[Pour交易的NP声明实例]**
$$\vec{x} = (\text{rt}, \text{sn}_1^{\text{old}}, \text{sn}_2^{\text{old}}, \text{cm}_1^{\text{new}}, \text{cm}_2^{\text{new}}, v_{\text{pub}}, h_{\text{Sig}}, h_1, h_2)$$
> 作用：定义了zk-SNARK证明的公开输入，包括Merkle树根、输入序列号、输出承诺、公开金额和用于防止延展性的哈希值。

### 实验结果
论文在Intel Core i7-4770处理器（8线程）上对Zerocash的核心组件进行了基准测试。对于关键的POUR操作的zk-SNARK，**生成证明**（Prove）需要约2分2秒（单线程）或1分3秒（8线程），**验证证明**（Verify）仅需5.4毫秒，证明大小为288字节。作为对比，整个**Pour算法**的执行时间为2分2秒，输出的Pour交易大小为996字节。在验证环节，验证一条Pour交易（不包括账本扫描）需要5.7毫秒，验证一条Mint交易仅需8.3微秒。这些性能数据表明，Pour交易的验证成本比Zerocoin低98.6%，交易大小减少了97.7%。网络仿真实验（1000节点，平均每秒产生1笔交易，平均150秒生成一个区块）表明，由于交易验证缓存机制非常有效，即使在100%的交易均为Pour交易的情况下，区块的**平均验证时间仅为78毫秒**，对区块传播速度的影响几乎可以忽略不计。交易从创建到被包含进区块的延迟约为195秒（在更快的区块生成速率下），用户可以等待一个区块后再花费接收到的硬币。

### 局限性与开放问题
Zerocash的隐私保护主要体现在交易账本层面，但网络层的流量分析（例如IP地址泄露）仍需借助Tor等匿名网络来缓解。系统依赖一次可信设置来生成公共参数，虽然匿名性在设置被攻破时仍能保持，但系统的健壮性（如防止双花）会受到影响，未来可以通过安全多方计算来分散信任。论文指出，其底层的zk-SNARK技术足够灵活，能在保护隐私的同时嵌入合规性检查（如税收验证），这提出了关于“哪些政策是理想的且可实现的”这一新的研究、政策和工程问题。

### 强关联论文

[8] Miers 等. Zerocoin: Anonymous distributed e-cash from bitcoin. **IEEE S&P 2013** [Google Scholar](https://scholar.google.com/scholar?q=Zerocoin%3A%20Anonymous%20distributed%20e-cash%20from%20bitcoin)

[13] Parno 等. Pinocchio: nearly practical verifiable computation. **IEEE S&P 2013** [Google Scholar](https://scholar.google.com/scholar?q=Pinocchio%3A%20nearly%20practical%20verifiable%20computation)

[14] Ben-Sasson 等. SNARKs for C: verifying program executions succinctly and in zero knowledge. **CRYPTO 2013** [Google Scholar](https://scholar.google.com/scholar?q=SNARKs%20for%20C%3A%20verifying%20program%20executions%20succinctly%20and%20in%20zero%20knowledge)

[16] Ben-Sasson 等. Succinct non-interactive arguments for a von Neumann architecture. **ePrint 2013** [Google Scholar](https://scholar.google.com/scholar?q=Succinct%20non-interactive%20arguments%20for%20a%20von%20Neumann%20architecture)

[19] Danezis 等. Pinocchio Coin: building Zerocoin from a succinct pairing-based proof system. **PETShop 2013** [Google Scholar](https://scholar.google.com/scholar?q=Pinocchio%20Coin%3A%20building%20Zerocoin%20from%20a%20succinct%20pairing-based%20proof%20system)

[9] Groth. Short pairing-based non-interactive zero-knowledge arguments. **ASIACRYPT 2010** [Google Scholar](https://scholar.google.com/scholar?q=Short%20pairing-based%20non-interactive%20zero-knowledge%20arguments)

[12] Gennaro 等. Quadratic span programs and succinct NIZKs without PCPs. **EUROCRYPT 2013** [Google Scholar](https://scholar.google.com/scholar?q=Quadratic%20span%20programs%20and%20succinct%20NIZKs%20without%20PCPs)


## 关键词

+ Zerocash
+ 去中心化匿名支付
+ zk-SNARK
+ 隐私保护数字货币
+ 匿名交易
+ DAP方案