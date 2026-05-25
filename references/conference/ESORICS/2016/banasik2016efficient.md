---
title: "Efficient zero-knowledge contingent payments in cryptocurrencies without scripts"
标题简称:
论文类型: conference
会议简称: ESORICS
发表年份: 2016
---

## Efficient zero-knowledge contingent payments in cryptocurrencies without scripts

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-319-45741-3_14)

## 作者

+ Wacław Banasik 
+ Stefan Dziembowski 
+ Daniel Malinowski 


## 笔记

One of the most promising innovations offered by the cryptographic currencies (like Bitcoin) are the so-called _smart contracts_, which can be viewed as financial agreements between mutually distrusting participants. Their execution is enforced by the mechanics of the currency, and typically has monetary consequences for the parties. The rules of these contracts are written in the form of so-called “scripts”, which are pieces of code in some “scripting language”. Although smart contracts are believed to have a huge potential, for the moment they are not widely used in practice. In particular, most of Bitcoin miners allow only to post standard transactions (i.e.: those without the non-trivial scripts) on the blockchain. As a result, it is currently very hard to create non-trivial smart contracts in Bitcoin.

Motivated by this, we address the following question: “is it possible to create non-trivial efficient smart contracts using the standard transactions only?” We answer this question affirmatively, by constructing efficient Zero-Knowledge Contingent Payment protocol for a large class of NP-relations. This includes the relations for which efficient sigma protocols exist. In particular, our protocol can be used to sell a factorization (_p_, _q_) of an RSA modulus , which is an example that we implemented and tested its efficiency in practice.

As another example of the “smart contract without scripts” we show how our techniques can be used to implement the contract called “trading across chains”.

以下是中文翻译：

加密货币（cryptographic currencies，如比特币）所提供的最具前景的创新之一是所谓的智能合约（smart contracts），这类合约可被视为互不信任参与者之间的金融协议。其执行由加密货币自身的机制强制保障，通常会对各方产生货币层面的后果。这些合约的规则以所谓“脚本”（scripts）的形式编写，即采用某种“脚本语言”（scripting language）编写的代码片段。尽管智能合约被认为具有巨大潜力，但目前在实践中尚未被广泛采用。特别是，大多数比特币矿工仅允许将标准交易（standard transactions，即不含非平凡脚本的交易）发布到区块链上。因此，目前在比特币中构建非平凡的智能合约极为困难。

受此现状启发，我们探讨以下问题：“是否仅使用标准交易即可构建非平凡且高效的智能合约？”我们对此给出了肯定的回答：通过构造一种高效的零知识条件支付（Zero-Knowledge Contingent Payment, ZKCP）协议，适用于一大类 NP 关系（NP-relations）。该类关系包括那些存在高效 Sigma 协议（sigma protocols）的关系。特别地，我们的协议可用于出售 RSA 模数（RSA modulus）的因式分解结果（p, q）——我们已实现并实际测试了该示例的效率。

作为“无脚本智能合约”的另一实例，我们进一步展示了如何利用所提出的技术实现一种名为“跨链交易”（trading across chains）的合约。

## 关键词

+ 零知识条件支付
+ 无脚本智能合约
+ 比特币标准交易
+ NP关系与Sigma协议
+ 跨链交易