---
title: "Fast batched asynchronous distributed key generation"
标题简称:
论文类型: conference
会议简称: EUROCRYPT
发表年份: 2024
created: 2025-05-12 09:08:01
modified: 2025-05-12 09:09:40
---

## Fast batched asynchronous distributed key generation

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-58740-5_13)
+ [archive](https://eprint.iacr.org/2023/1175)

## 作者

+ [Jens Groth](Jens%20Groth.md)
+ [Victor Shoup](Victor%20Shoup.md)
## 笔记

We present new protocols for threshold Schnorr signatures that work in an asynchronous communication setting, providing robustness and optimal resilience. These protocols provide unprecedented performance in terms of communication and computational complexity. In terms of communication complexity, for each signature, a single party must transmit a few dozen group elements and scalars across the network (independent of the size of the signing committee). In terms of computational complexity, the amortized cost for one party to generate a signature is actually less than that of just running the standard Schnorr signing or verification algorithm (at least for moderately sized signing committees, say, up to 100).

For example, we estimate that with a signing committee of 49 parties, at most 16 of which are corrupt, we can generate 50,000 Schnorr signatures per second (assuming each party can dedicate one standard CPU core and 500 Mbs of network bandwidth to signing). Importantly, this estimate includes both the cost of an offline precomputation phase (which just churns out message independent “presignatures”) and an online signature generation phase. Also, the online signing phase can generate a signature with very little network latency (just one to three rounds, depending on how throughput and latency are balanced).

To achieve this result, we provide two new innovations. One is a new secret sharing protocol (again, asynchronous, robust, optimally resilient) that allows the dealer to securely distribute shares of a large batch of ephemeral secret keys, and to publish the corresponding ephemeral public keys. To achieve better performance, our protocol minimizes public-key operations, and in particular, is based on a novel technique that does not use the traditional technique based on “polynomial commitments”. The second innovation is a new algorithm to efficiently combine ephemeral public keys contributed by different parties (some possibly corrupt) into a smaller number of secure ephemeral public keys. This new algorithm is based on a novel construction of a so-called “super-invertible matrix” along with a corresponding highly-efficient algorithm for multiplying this matrix by a vector of group elements.

As protocols for verifiably sharing a secret key with an associated public key and the technology of super-invertible matrices both play a major role in threshold cryptography and multi-party computation, our two new innovations should have applicability well beyond that of threshold Schnorr signatures.

以下是中文翻译：

我们提出了新的门限Schnorr签名(threshold Schnorr signatures)协议，该协议在异步通信环境下工作，提供了鲁棒性和最优的容错能力。这些协议在通信复杂度和计算复杂度方面都实现了前所未有的性能。就通信复杂度而言，对于每个签名，单个参与方只需在网络中传输几十个群元素和标量（与签名委员会的规模无关）。就计算复杂度而言，一个参与方生成签名的摊销成本实际上比仅运行标准Schnorr签名或验证算法还要低（至少对于中等规模的签名委员会，比如不超过100个成员时）。

例如，我们估计在一个由49个参与方组成的签名委员会中（其中最多16个可能是恶意的），每秒可以生成50,000个Schnorr签名（假设每个参与方可以dedicat一个标准CPU核心和500 Mbs的网络带宽用于签名）。重要的是，这个估计包括了离线预计算阶段（该阶段持续产生与消息无关的"预签名"）和在线签名生成阶段的成本。此外，在线签名阶段可以以很低的网络延迟（根据吞吐量和延迟的平衡方式，仅需一到三轮）生成签名。

为实现这一结果，我们提供了两项新的创新。第一项是一个新的秘密共享协议（同样是异步的、鲁棒的、具有最优容错性的），允许分发者安全地分发大批量临时密钥的份额，并发布相应的临时公钥。为了获得更好的性能，我们的协议最小化了公钥操作，特别是基于一种新颖的技术，不使用传统的"多项式承诺"(polynomial commitments)技术。第二项创新是一种新算法，可以高效地将不同参与方（其中一些可能是恶意的）贡献的临时公钥组合成更少数量的安全临时公钥。这个新算法基于一种新颖的"超可逆矩阵"(super-invertible matrix)构造，以及相应的高效矩阵-向量乘法算法，其中向量元素为群元素。

由于可验证地共享具有关联公钥的密钥的协议以及超可逆矩阵技术在门限密码学和多方计算中都发挥着重要作用，我们的这两项新创新应该具有超出门限Schnorr签名范畴的广泛应用价值。

## 关键词

+ 门限Schnorr签名
+ 异步分布式密钥生成
+ 超可逆矩阵
+ 批量预签名
+ 多方计算
+ 最优容错性