---
title: "Non-interactive Blind Signatures from RSA Assumption and More"
标题简称:
论文类型: conference
会议简称: EUROCRYPT
发表年份: 2025
created: 2025-05-09 14:34:37
modified: 2025-05-09 14:35:38
---

## Non-interactive Blind Signatures from RSA Assumption and More

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-91124-8_13)

## 作者

+ [Lucjan Hanzlik](Lucjan%20Hanzlik.md)
+ Eugenio Paracucchi
+ Riccardo Zanotto

## 笔记

Blind signatures have received increased attention from researchers and practitioners. They allow users to obtain a signature under a message without revealing it to the signer. One of the most popular applications of blind signatures is to use them as one-time tokens, where the issuing is not linkable to the redeeming phase, and the signature under a random identifier forms a valid token. This concept is the backbone of the Privacy Pass system, which uses it to identify honest but anonymous users and protect content delivery networks from botnets.

Non-interactive blind signatures for random messages were introduced by Hanzlik (Eurocrypt’23). They allow a signer to create a pre-signature with respect to a particular public key, while the corresponding secret key can later be used to finalize the signature. This non-interaction allows for more applications than in the case of blind signatures. In particular, the author suggested using regular PKI keys as the recipient public key, allowing for a distribution of one-time tokens to users outside the system, e.g., to public keys of GitHub users, similar to airdropping of cryptocurrencies. Unfortunately, despite introducing this concept, the paper fails to provide schemes that work with keys used in the wild.

We solve this open problem. We introduce a generic construction of non-interactive blind signatures that relies on Yao’s garbled circuit techniques and provide particular improvements to this generic setting. We replace oblivious transfer with their non-interactive variant and show how to construct them so that the recipient’s public key, encoding the OT choice, is a standard RSA public key (_e_, _N_). To improve the efficiency of the garbling, we show how to garble the signing algorithm of the pairing-based Pointcheval-Sanders (PS) signatures and the RSA-based signature scheme with efficient protocols by Camenisch and Lysyanskaya. Our technique also apply to the well-known BBS signatures. All our improvements are of independent interest and are central to our contribution.

以下是中文翻译：

盲签名（Blind signatures）已经受到研究人员和实践者越来越多的关注。它允许用户在不向签名者透露消息内容的情况下获得该消息的签名。盲签名最流行的应用之一是将其用作一次性令牌（one-time tokens），其中令牌的发行阶段与兑换阶段不可关联，且对随机标识符的签名构成有效令牌。这一概念是隐私传递系统（Privacy Pass system）的核心，该系统使用它来识别诚实但匿名的用户，并保护内容分发网络免受僵尸网络的攻击。

针对随机消息的非交互式盲签名（Non-interactive blind signatures）由Hanzlik（Eurocrypt'23）首次提出。它允许签名者针对特定公钥创建预签名，而相应的私钥可以在之后用于完成签名。这种非交互性使其比普通盲签名具有更多的应用场景。特别是，作者建议使用常规PKI密钥作为接收方公钥，这样可以向系统外的用户分发一次性令牌，例如向GitHub用户的公钥分发，类似于加密货币的空投。遗憾的是，尽管引入了这一概念，但该论文未能提供适用于实际环境中使用的密钥的方案。

我们解决了这个开放性问题。我们提出了一个基于姚氏混淆电路（Yao's garbled circuit）技术的非交互式盲签名通用构造方案，并对这个通用设置进行了特定改进。我们用非交互式变体替代了不经意传输（oblivious transfer），并展示了如何构造它们，使得接收方的公钥（用于编码选择）可以是标准的RSA公钥(e, N)。为了提高混淆的效率，我们展示了如何对基于配对的Pointcheval-Sanders（PS）签名和基于RSA的Camenisch-Lysyanskaya高效协议签名方案的签名算法进行混淆。我们的技术同样适用于著名的BBS签名。我们所有的改进都具有独立的研究价值，并且是我们贡献的核心。

## 关键词

+ 非交互式盲签名
+ RSA假设
+ 混淆电路技术
+ 不经意传输
+ 隐私传递系统
+ BBS签名