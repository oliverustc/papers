---
title: "Mempool privacy via batched threshold encryption: Attacks and defenses"
标题简称:
论文类型: conference
会议简称: USENIX Security
发表年份: 2024
created: 2025-04-29 10:17:53
modified: 2025-04-29 10:19:47
---

## Mempool privacy via batched threshold encryption: Attacks and defenses

## 发表信息

+ [原文链接](https://www.usenix.org/conference/usenixsecurity24/presentation/choudhuri)

## 作者

+ [Arka Rai Choudhuri](Arka%20Rai%20Choudhuri.md)
+ [Sanjam Garg](Sanjam%20Garg.md) 
+ Julien Piet 
+ [Guru-Vamsi Policharla](Guru-Vamsi%20Policharla.md)
## 笔记

With the rising popularity of DeFi applications it is important to implement protections for regular users of these DeFi platforms against large parties with massive amounts of resources allowing them to engage in market manipulation strategies such as frontrunning/backrunning. Moreover, there are many situations (such as recovery of funds from vulnerable smart contracts) where a user may not want to reveal their transaction until it has been executed. As such, it is clear that preserving the privacy of transactions in the mempool is an important goal.

In this work we focus on achieving mempool transaction privacy through a new primitive that we term _batched-threshold encryption_, which is a variant of threshold encryption with strict efficiency requirements to better model the needs of resource constrained environments such as blockchains. Unlike the naive use of threshold encryption, which requires communication proportional to O(nB) to decrypt B transactions with a committee of n parties, our batched-threshold encryption scheme only needs O(n) communication. We additionally discuss pitfalls in prior approaches that use (vanilla) threshold encryption for mempool privacy.

To show that our scheme is concretely efficient, we implement our scheme and find that transactions can be encrypted in under 6 ms, _independent_ of committee size, and the communication required to decrypt an entire batch of B transactions is 80 bytes per party, _independent_ of the number of transactions B, making it an attractive choice when communication is very expensive. If deployed on Ethereum, which processes close to 500 transaction per block, it takes close to 2.8 s for each committee member to compute a partial decryption and under 3.5 s to decrypt all transactions for a block in single-threaded mode.

以下是中文翻译：

随着去中心化金融（DeFi）应用的日益普及，为这些DeFi平台的普通用户实施保护措施变得越来越重要，以防止拥有大量资源的大型参与者利用抢先交易/后随交易（frontrunning/backrunning）等市场操纵策略。此外，在许多情况下（比如从易受攻击的智能合约中恢复资金），用户可能不希望在交易执行之前透露其交易内容。因此，保护交易内存池（mempool）中交易的隐私显然是一个重要目标。

在本研究中，我们通过一种称为批量阈值加密（batched-threshold encryption）的新型原语来实现交易内存池隐私保护，这是阈值加密的一个变体，具有严格的效率要求，以更好地适应区块链等资源受限环境的需求。与普通阈值加密相比，后者需要 $O(nB)$ 的通信量来解密由n个参与方组成的委员会处理的B个交易，而我们的批量阈值加密方案仅需要 $O(n)$ 的通信量。我们还讨论了先前使用（普通）阈值加密来实现交易内存池隐私保护方法中存在的缺陷。

为了证明我们的方案在实际应用中的效率，我们实现了该方案并发现：交易加密时间少于6毫秒，且与委员会规模无关；解密整批B个交易所需的通信量为每个参与方80字节，与交易数量B无关，这使得该方案在通信成本很高的情况下成为一个很有吸引力的选择。如果部署在以太坊（Ethereum）上（每个区块处理接近500个交易），在单线程模式下，每个委员会成员计算部分解密需要接近2.8秒，解密一个区块的所有交易需要不到3.5秒。

## 关键词

+ 批量阈值加密内存池隐私
+ DeFi交易隐私保护
+ 阈值加密效率优化
+ 抗抢先交易协议
+ 区块链交易内存池隐私
+ 委员会解密通信复杂度
