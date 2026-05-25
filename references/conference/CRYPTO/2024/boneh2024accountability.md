---
title: "Accountability for misbehavior in threshold decryption via threshold traitor tracing"
标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 2024
---

## Accountability for misbehavior in threshold decryption via threshold traitor tracing

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-68394-7_11)

## 作者

+ [Dan Boneh](Dan%20Boneh.md) 
+ Aditi Partap 
+ Lior Rotem 


## 笔记

A t-out-of-n threshold decryption system assigns key shares to n parties so that any t of them can decrypt a well-formed ciphertext. Existing threshold decryption systems are not secure when these parties are rational actors: an adversary can offer to pay the parties for their key shares. The problem is that a quorum of t parties, working together, can sell the adversary a decryption key that reveals nothing about the identity of the traitor parties. This provides a risk-free profit for the parties since there is no accountability for their misbehavior --- the information they sell to the adversary reveals nothing about their identity. This behavior can result in a complete break in many applications of threshold decryption, such as encrypted mempools, private voting, and sealed-bid auctions. In this work we show how to add accountability to threshold decryption systems to deter this type of risk-free misbehavior. Suppose a quorum of t or more parties construct a decoder algorithm D(⋅) that takes as input a ciphertext and outputs the corresponding plaintext or ⊥. They sell D to the adversary. Our threshold decryption systems are equipped with a tracing algorithm that can trace D to members of the quorum that created it. The tracing algorithm is only given blackbox access to D and will identify some members of the misbehaving quorum. The parties can then be held accountable, which may discourage them from selling the decoder D in the first place. Our starting point is standard (non-threshold) traitor tracing, where n parties each holds a secret key. Every party can decrypt a well-formed ciphertext on its own. However, if a subset of parties J⊆[n] collude to create a pirate decoder D(⋅) that can decrypt well-formed ciphertexts, then it is possible to trace D to at least one member of J using only blackbox access to the decoder D. Traitor tracing received much attention over the years and multiple schemes have been developed. In this work we develop the theory of traitor tracing for threshold decryption, where now only a subset J⊆[n] of t or more parties can collude to create a pirate decoder D(⋅). This problem has recently become quite important due to the real-world deployment of threshold decryption in encrypted mempools, as we explain in the paper. While there are several non-threshold traitor tracing schemes that we can leverage, adapting these constructions to the threshold decryption settings requires new cryptographic techniques. We present a number of constructions for traitor tracing for threshold decryption, and note that much work remains to explore the large design space.

这是一篇关于门限解密系统的学术论文摘要，以下是中文翻译：

门限解密系统(t-out-of-n threshold decryption system)将密钥份额分配给n个参与方，其中任意t个参与方可以解密格式正确的密文。现有的门限解密系统在参与方是理性行为者时并不安全：攻击者可以出价购买参与方的密钥份额。问题在于，当t个参与方形成法定人数并合作时，他们可以向攻击者出售一个解密密钥，而这个密钥不会泄露任何叛徒方的身份信息。由于他们的不当行为无需承担责任——他们出售给攻击者的信息不会暴露他们的身份，这为参与方提供了无风险的利益。这种行为可能导致门限解密在许多应用场景中完全失效，如加密内存池(encrypted mempools)、私密投票和密封竞价拍卖。

在本研究中，我们展示了如何为门限解密系统添加问责机制，以遏制这种无风险的不当行为。假设t个或更多参与方构建了一个解码器算法D(⋅)，该算法接收密文作为输入，输出相应的明文或⊥。他们将D出售给攻击者。我们的门限解密系统配备了一个追踪算法，可以将D追踪到创建它的法定人数成员。追踪算法仅需要对D的黑盒访问就能识别出部分不当行为的法定人数成员。这样参与方就可以被追究责任，这可能会阻止他们一开始就出售解码器D。

我们的起点是标准的（非门限）叛徒追踪(traitor tracing)，其中n个参与方各自持有一个密钥。每个参与方都可以独立解密格式正确的密文。然而，如果一个参与方子集J⊆[n]串谋创建了一个能够解密格式正确密文的盗版解码器D(⋅)，那么仅通过对解码器D的黑盒访问，就可以将D追踪到J中的至少一个成员。叛徒追踪多年来受到广泛关注，并已开发出多种方案。

在本研究中，我们发展了门限解密的叛徒追踪理论，现在只有t个或更多参与方的子集J⊆[n]能够串谋创建盗版解码器D(⋅)。正如我们在论文中解释的，由于加密内存池在现实世界中的部署，这个问题最近变得非常重要。虽然我们可以利用几个非门限叛徒追踪方案，但将这些构造适配到门限解密设置需要新的密码学技术。我们提出了几种门限解密叛徒追踪的构造方案，并指出在这个广阔的设计空间中仍有许多工作待完成。

## 关键词

+ 密码学
+ 零知识
+ 协议