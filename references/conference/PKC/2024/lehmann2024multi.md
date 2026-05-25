---
title: "Multi-signatures for ad-hoc and privacy-preserving group signing"
标题简称:
论文类型: conference
会议简称: PKC
发表年份: 2024
created: 2025-04-17 10:58:08
modified: 2025-04-17 10:59:13
---

## Multi-signatures for ad-hoc and privacy-preserving group signing

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-57718-5_7)

## 作者

+ Anja Lehmann 
+ Cavit Özbay 

## 笔记

Multi-signatures allow to combine individual signatures from different signers on the same message into a short aggregated signature. Newer schemes further allow to aggregate the individual public keys, such that the combined signature gets verified against a short aggregated key. This makes them a versatile alternative to threshold or distributed signatures: the aggregated key can serve as group key, and signatures under that key can only be computed with the help of all signers. What makes multi-signatures even more attractive is their simple key management, as users can re-use the same secret key in several and ad-hoc formed groups. In that context, it will be desirable to not sacrifice privacy as soon as keys get re-used and ensure that users are not linkable across groups. In fact, when multi-signatures with key aggregation were proposed, it was claimed that aggregated keys hide the signers’ identities or even the fact that it is a combined key at all. In our work, we show that none of the existing multi-signature schemes provide these privacy guarantees when keys get re-used in multiple groups. This is due to the fact that all known schemes deploy deterministic key aggregation. To overcome this limitation, we propose a new variant of _multi-signatures with probabilistic yet verifiable key aggregation_. We formally define the desirable privacy and unforgeability properties in the presence of key re-use. This also requires to adapt the unforgeability model to the group setting, and ensure that key-reuse does not weaken the expected guarantees. We present a simple BLS-based scheme that securely realizes our strong privacy and security guarantees. We also formalize and investigate the privacy that is possible by deterministic schemes, and prove that existing schemes provide the advertised privacy features as long as one public key remains secret.

以下是中文翻译：

多重签名允许将来自不同签署者的单独签名组合成一个简短的聚合签名。更新的方案进一步允许聚合单独的公钥，从而使得组合签名可以通过一个简短的聚合密钥进行验证。这使得多重签名成为阈值签名或分布式签名的多功能替代方案：聚合密钥可以作为组密钥，而在该密钥下的签名只能在所有签署者的帮助下计算。在这种背景下，理想的情况是，在密钥被重用时不牺牲隐私，并确保用户在不同组之间不可链接。实际上，当提出带有密钥聚合的多重签名时，有人声称聚合密钥隐藏了签署者的身份，甚至隐藏了这实际上是一个组合密钥的事实。在我们的研究中，我们表明，现有的多重签名方案在密钥被重用于多个组时并未提供这些隐私保证。这是因为所有已知方案都采用了确定性密钥聚合。为了克服这一限制，我们提出了一种新的多重签名变体，采用概率性但可验证的密钥聚合。我们正式定义了在密钥重用情况下所需的隐私和不可伪造性特性。这还需要将不可伪造性模型调整为组设置，并确保密钥重用不会削弱预期的保证。我们提出了一种基于BLS的简单方案，安全地实现了我们强大的隐私和安全保证。我们还形式化并研究了确定性方案所能提供的隐私，并证明现有方案在一个公钥保持秘密的情况下提供了所宣传的隐私特性。

## 关键词

+ 多重签名
+ 密钥聚合
+ 隐私保护签名
+ 概率密钥聚合
+ BLS签名
+ 跨群组不可链接性