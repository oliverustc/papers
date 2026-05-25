---
title: "One-out-of-many proofs: Or how to leak a secret and spend a coin"
标题简称:
论文类型: conference
会议简称: EUROCRYPT
发表年份: 2015
created: 2025-05-12 08:48:43
modified: 2025-05-12 08:57:09
---

## One-out-of-many proofs: Or how to leak a secret and spend a coin

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-662-46803-6_9)

## 作者

+ [Jens Groth](Jens%20Groth.md)
+ [Markulf Kohlweiss](Markulf%20Kohlweiss.md)

## 笔记

We construct a 3-move public coin special honest verifier zero-knowledge proof, a so-called Sigma-protocol, for a list of commitments having at least one commitment that opens to 0. It is not required for the prover to know openings of the other commitments. The proof system is efficient, in particular in terms of communication requiring only the transmission of a logarithmic number of commitments.

We use our proof system to instantiate both ring signatures and zerocoin, a novel mechanism for bitcoin privacy. We use our Sigma-protocol as a (linkable) ad-hoc group identification scheme where the users have public keys that are commitments and demonstrate knowledge of an opening for one of the commitments to unlinkably identify themselves (once) as belonging to the group. Applying the Fiat-Shamir transform on the group identification scheme gives rise to ring signatures, applying it to the linkable group identification scheme gives rise to zerocoin.

Our ring signatures are very small compared to other ring signature schemes and we only assume the users’ secret keys to be the discrete logarithms of single group elements so the setup is quite realistic. Similarly, compared with the original zerocoin protocol we only rely on a weak cryptographic assumption and do not require a trusted setup.

A third application of our Sigma protocol is an efficient proof of membership of a secret committed value belonging to a public list of values.

以下是中文翻译：

我们构建了一个3步公开随机特殊诚实验证者零知识证明（也称为Sigma协议），用于证明一组承诺中至少有一个承诺能打开为0。证明者不需要知道其他承诺的开启值。该证明系统非常高效，特别是在通信方面，只需传输对数级数量的承诺。

我们使用这个证明系统来实现环签名（ring signatures）和零币（zerocoin）- 一种新型的比特币隐私机制。我们将Sigma协议用作（可链接的）临时组身份识别方案，其中用户的公钥是承诺，通过证明知道其中一个承诺的开启值来不可链接地证明自己（一次）属于该组。对组身份识别方案应用Fiat-Shamir变换可以得到环签名，而对可链接的组身份识别方案应用该变换则可以得到零币。

与其他环签名方案相比，我们的环签名非常简短，并且我们只假设用户的私钥是单个群元素的离散对数，因此这种设置相当实用。同样，与原始的零币协议相比，我们只依赖于较弱的密码学假设，且不需要可信设置。

我们的Sigma协议的第三个应用是为秘密承诺值属于公开值列表提供高效的成员资格证明。

## 关键词

+ 一取多证明
+ Sigma协议
+ 环签名
+ 零币
+ Pedersen承诺