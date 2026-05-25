---
title: "Efficient zero-knowledge proof of algebraic and non-algebraic statements with applications to privacy preserving credentials"

标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 2016
modified: 2025-04-14 09:56:54
---

## Efficient zero-knowledge proof of algebraic and non-algebraic statements with applications to privacy preserving credentials

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-662-53015-3_18)

## 作者

+ [Melissa Chase](Melissa%20Chase.md)
+ [Chaya Ganesh](Chaya%20Ganesh.md)
+ [Payman Mohassel](Payman%20Mohassel.md)
## 笔记

Practical anonymous credential systems are generally built around sigma-protocol ZK proofs. This requires that credentials be based on specially formed signatures. Here we ask whether we can instead use a standard (say, RSA, or (EC)DSA) signature that includes formatting and hashing messages, as a credential, and still provide privacy. Existing techniques do not provide efficient solutions for proving knowledge of such a signature: On the one hand, ZK proofs based on garbled circuits (Jawurek et al. 2013) give efficient proofs for checking formatting of messages and evaluating hash functions. On the other hand they are expensive for checking algebraic relations such as RSA or discrete-log, which can be done efficiently with sigma protocols.

We design new constructions obtaining the best of both worlds: combining the efficiency of the garbled circuit approach for non-algebraic statements and that of sigma protocols for algebraic ones. We then discuss how to use these as building-blocks to construct privacy-preserving credential systems based on standard RSA and (EC)DSA signatures.

Other applications of our techniques include anonymous credentials with more complex policies, the ability to efficiently switch between commitments (and signatures) in different groups, and secure two-party computation on committed/signed inputs.

以下是中文翻译：

实用的匿名凭证系统通常围绕sigma协议零知识证明构建。这要求凭证基于特殊构造的签名。本文探讨是否能用包含消息格式化和哈希处理的标准签名（如RSA或(EC)DSA）作为凭证，同时仍保障隐私。现有技术对此类签名的知识证明缺乏高效解决方案：一方面，基于混淆电路的零知识证明（Jawurek等人，2013年）能高效验证消息格式和哈希函数；另一方面，这些方法在验证RSA或离散对数等代数关系时效率低下，而这些恰是sigma协议能高效处理的。

我们设计的新型构造方案集两者之长：既融合了混淆电路方法在处理非代数陈述时的高效性，又结合了西格玛协议在代数陈述上的优势。随后，我们探讨了如何将这些方案作为基础模块，构建基于标准RSA及(EC)DSA签名的隐私保护凭证系统。

我们技术的其他应用包括支持更复杂策略的匿名凭证、在不同群组间高效切换承诺（及签名）的能力，以及对已承诺/签名输入的安全两方计算。

## 关键词

+ 代数非代数陈述零知识证明
+ 混淆电路sigma协议结合框架
+ 隐私保护凭证标准签名RSA ECDSA
+ 非代数关系证明高效组合构造
+ 安全两方计算承诺签名输入