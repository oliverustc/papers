---
title: Practical mempool privacy via one-time setup batched threshold encryption
标题简称: 
论文类型: conference
会议简称: USENIX Security
发表年份: 2025
created: 2025-04-28 11:34:05
modified: 2025-04-28 16:05:21
---

## Practical mempool privacy via one-time setup batched threshold encryption

## 发表信息

+ [archive链接](https://eprint.iacr.org/2024/1516)
+ [code](https://github.com/guruvamsi-policharla/batched-threshold-pp)

## 作者

+ [Arka Rai Choudhuri](Arka%20Rai%20Choudhuri.md)
+ [Sanjam Garg](Sanjam%20Garg.md) 
+ [Guru-Vamsi Policharla](Guru-Vamsi%20Policharla.md)
+ [Mingyuan Wang](Mingyuan%20Wang.md) 

## 笔记

An important consideration with the growth of the DeFi ecosystem is the protection of clients who submit transactions to the system. As it currently stands, the public visibility of these transactions in the memory pool (mempool) makes them susceptible to market manipulations such as frontrunning and backrunning. More broadly, for various reasons—ranging from avoiding market manipulation to including time-sensitive information in their transactions—clients may want the contents of their transactions to remain private until they are executed, i.e. they have *pending transaction privacy*. Therefore, *mempool privacy* is becoming an increasingly important feature as DeFi applications continue to spread. We construct the first *practical* mempool privacy scheme that uses a *one-time* DKG setup for n decryption servers. Our scheme ensures the strong privacy requirement by not only hiding the transactions until they are decrypted but also guaranteeing privacy for transactions that were not selected in the epoch (*pending transaction privacy*). For each epoch (or block), clients can encrypt their transactions so that, once B (encrypted) transactions are selected for the epoch, they can be decrypted by each decryption server while communicating only O(1) information. Our result improves upon the best-known prior works, which either: (i) require an expensive initial setup involving a (special purpose) multiparty computation protocol executed by the n decryption servers, along with an additional *per-epoch* setup; (ii) require each decryption server to communicate O(B) information; or (iii) do not guarantee pending transaction privacy. We implement our scheme and find that transactions can be encrypted in approximately 8.5 ms, independent of committee size, and the communication required to decrypt an entire batch of transactions is 48 bytes per party, independent of the number of transactions. If deployed on Ethereum, which processes close to 500 transactions per block, it takes close to 3.2 s for each committee member to compute a partial decryption and 3.0 s to decrypt all transactions for a block in single-threaded mode. Compared to prior work, which had an expensive setup phase per epoch, we incur <2× overhead in the worst case. On some metrics such as partial decryptions size, we actually fare better.

以下是中文翻译：

随着去中心化金融(DeFi)生态系统的发展，保护提交交易的客户端变得越来越重要。目前，这些交易在内存池(mempool)中的公开可见性使其容易受到诸如抢先交易(frontrunning)和尾随交易(backrunning)等市场操纵的影响。更广泛地说，由于各种原因——从避免市场操纵到在交易中包含时间敏感信息——客户端可能希望其交易内容在执行之前保持私密，即他们需要"待处理交易隐私"(pending transaction privacy)。因此，随着DeFi应用的持续扩展，"内存池隐私"(mempool privacy)正在成为一个越来越重要的特性。我们构建了第一个实用的内存池隐私方案，该方案为n个解密服务器使用一次性分布式密钥生成(DKG)设置。我们的方案通过不仅隐藏交易直到它们被解密，而且还为在该轮次中未被选中的交易保证隐私（待处理交易隐私），确保了强隐私要求。对于每个轮次（或区块），客户端可以加密他们的交易，这样一旦选择了B个（加密的）交易用于该轮次，每个解密服务器只需通信$O(1)$的信息就能解密这些交易。我们的结果改进了已知的最佳先前工作，这些工作要么：(i)需要一个昂贵的初始设置，包括由n个解密服务器执行的（特殊用途）多方计算协议，以及额外的每轮次设置；(ii)要求每个解密服务器通信$O(B)$的信息；或(iii)不保证待处理交易隐私。

我们实现了我们的方案，发现交易加密时间约为8.5毫秒，与委员会规模无关，且解密整批交易所需的通信量为每方48字节，与交易数量无关。如果部署在以太坊上（每个区块处理接近500笔交易），在单线程模式下，每个委员会成员计算部分解密需要约3.2秒，解密一个区块的所有交易需要3.0秒。与之前每轮次都需要昂贵设置阶段的工作相比，我们在最坏情况下的开销增加不到2倍。在某些指标上，如部分解密大小，我们实际上表现更好。

## 关键词

+ 内存池隐私保护
+ 一次性DKG批量阈值加密
+ 待处理交易隐私
+ 抗前置交易攻击
+ DeFi隐私保护机制
+ 分布式密钥生成协议