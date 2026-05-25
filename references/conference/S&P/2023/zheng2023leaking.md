---
title: "Leaking arbitrarily many secrets: Any-out-of-many proofs and applications to ringct protocols"
标题简称:
论文类型: conference
会议简称: S&P
发表年份: 2023
created: 2025-04-22 11:42:39
modified: 2025-04-22 11:43:57
---

## Leaking arbitrarily many secrets: Any-out-of-many proofs and applications to ringct protocols

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/10179292)

## 作者

+ Tianyu Zheng 
+ Shang Gao 
+ Yubo Song 
+ [Bin Xiao](Bin%20Xiao.md)
## 笔记

Ring Confidential Transaction (RingCT) protocol is an effective cryptographic component for preserving the privacy of cryptocurrencies. However, existing RingCT protocols are instantiated from one-out-of-many proofs with only one secret, leading to low efficiency and weak anonymity when handling transactions with multiple inputs. Additionally, current partial knowledge proofs with multiple secrets are neither secure nor efficient to be applied in a RingCT protocol.In this paper, we propose a novel any-out-of-many proof, a logarithmic-sized zero-knowledge proof scheme for showing the knowledge of arbitrarily many secrets out of a public list. Unlike other partial knowledge proofs that have to reveal the number of secrets [ACF21], our approach proves the knowledge of multiple secrets without leaking the exact number of them. Furthermore, we improve the efficiency of our method with a generic inner-product transformation to adopt the Bulletproofs compression [BBB+18], which reduces the proof size to 2⌈log2(N)⌉+9.Based on our proposed proof scheme, we further construct a compact RingCT protocol for privacy cryptocurrencies, which can provide a logarithmic-sized communication complexity for transactions with multiple inputs. More importantly, as the only known RingCT protocol instantiated from the partial knowledge proofs, our protocol can achieve the highest anonymity level compared with other approaches like Omniring [LRR+19]. For other applications, such as multiple ring signatures, our protocol can also be applied with some modifications. We believe our techniques are also applicable in other privacy-preserving scenarios, such as multiple ring signatures and coin-mixing in the blockchain.

以下是中文翻译：

环形机密交易(Ring Confidential Transaction, RingCT)协议是保护加密货币隐私的有效密码学组件。然而，现有的RingCT协议仅基于单一秘密的一对多证明来实现，这导致在处理多输入交易时效率低下且匿名性较弱。此外，当前具有多个秘密的部分知识证明既不安全也不够高效，无法应用于RingCT协议中。

在本文中，我们提出了一种新颖的任意多对多证明方案，这是一种对公开列表中任意数量秘密知识进行证明的对数大小零知识证明方案。与其他必须揭示秘密数量的部分知识证明[ACF21]不同，我们的方法可以证明多个秘密的知识而不泄露具体数量。此外，我们通过采用子弹证明(Bulletproofs)压缩[BBB+18]的通用内积转换来提高方法效率，将证明大小减少到2⌈log2(N)⌉+9。

基于我们提出的证明方案，我们进一步构建了一个用于隐私加密货币的紧凑型RingCT协议，该协议可以为多输入交易提供对数级的通信复杂度。更重要的是，作为唯一一个基于部分知识证明实现的RingCT协议，我们的协议与其他方法（如Omniring [LRR+19]）相比可以实现最高级别的匿名性。对于其他应用场景，如多重环签名，我们的协议经过适当修改后也可以应用。我们相信我们的技术也适用于其他隐私保护场景，例如多重环签名和区块链中的币混合。

## 关键词

+ 任意多对多零知识证明
+ 环形机密交易RingCT
+ 部分知识证明
+ Bulletproofs压缩
+ 隐私加密货币
+ 多重环签名