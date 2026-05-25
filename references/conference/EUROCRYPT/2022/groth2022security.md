---
title: "On the security of ECDSA with additive key derivation and presignatures"
标题简称:
论文类型: conference
会议简称: EUROCRYPT
发表年份: 2022
created: 2025-05-12 09:11:47
modified: 2025-05-12 09:13:24
---

## On the security of ECDSA with additive key derivation and presignatures

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-06944-4_13)
+ [archive](https://eprint.iacr.org/2021/1330)

## 作者

+ [Jens Groth](Jens%20Groth.md)
+ [Victor Shoup](Victor%20Shoup.md)
## 笔记

Two common variations of ECDSA signatures are additive key derivation and presignatures. Additive key derivation is a simple mechanism for deriving many subkeys from a single master key, and is already widely used in cryptocurrency applications with the Hierarchical Deterministic Wallet mechanism standardized in Bitcoin Improvement Proposal 32 (BIP32). Because of its linear nature, additive key derivation is also amenable to efficient implementation in the threshold setting. With presignatures, the secret and public nonces used in the ECDSA signing algorithm are precomputed. In the threshold setting, using presignatures along with other precomputed data allows for an extremely efficient “online phase” of the protocol. Recent works have advocated for both of these variations, sometimes combined together. However, somewhat surprisingly, we are aware of no prior security proof for additive key derivation, let alone for additive key derivation in combination with presignatures.

In this paper, we provide a thorough analysis of these variations, both in isolation and in combination. Our analysis is in the generic group model (GGM). Importantly, we do not modify ECDSA or weaken the standard notion of security in any way. Of independent interest, we also present a version of the GGM that is specific to elliptic curves. This EC-GGM better models some of the idiosyncrasies (such as the conversion function and malleability) of ECDSA. In addition to this analysis, we report security weaknesses in these variations that apparently have not been previously reported. For example, we show that when both variations are combined, there is a cube-root attack on ECDSA, which is much faster than the best known, square-root attack on plain ECDSA. We also present two mitigations against these weaknesses: re-randomized presignatures and homogeneous key derivation. Each of these mitigations is very lightweight, and when used in combination, the security is essentially the same as that of plain ECDSA (in the EC-GGM).

以下是中文翻译：

ECDSA签名有两种常见变体：加法密钥派生（additive key derivation）和预签名（presignatures）。加法密钥派生是一种从单个主密钥派生多个子密钥的简单机制，已在比特币改进提案32（BIP32）标准化的分层确定性钱包机制中广泛应用于加密货币领域。由于其线性特性，加法密钥派生也适合在门限设置中高效实现。预签名则是预先计算ECDSA签名算法中使用的秘密和公开随机数（nonces）。在门限设置中，使用预签名及其他预计算数据可以实现极高效率的协议"在线阶段"。近期研究提倡使用这两种变体，有时将其结合使用。然而令人意外的是，目前尚无针对加法密钥派生的安全证明，更遑论将加法密钥派生与预签名结合使用的安全性分析。

本文对这些变体进行了全面分析，包括单独分析和组合分析。分析在通用群模型（generic group model，GGM）下进行。重要的是，我们不对ECDSA进行任何修改，也不以任何方式削弱标准安全性定义。作为独立贡献，我们还提出了专门针对椭圆曲线的GGM版本（EC-GGM），能更好地模拟ECDSA的特性（如转换函数和可塑性）。除上述分析外，我们报告了这些变体中此前未被发现的安全弱点。例如，当两种变体结合使用时，ECDSA存在一种立方根攻击，其效率远超已知最优的平方根攻击。我们还提出了两种缓解措施：重随机化预签名（re-randomized presignatures）和同质密钥派生（homogeneous key derivation）。这两种措施均非常轻量，组合使用时安全性与普通ECDSA（在EC-GGM中）本质上相同。

## 关键词

+ ECDSA安全性分析
+ 加法密钥派生
+ 预签名
+ 通用群模型
+ 门限签名
