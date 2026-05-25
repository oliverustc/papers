---
title: "zklogin: Privacy-preserving blockchain authentication with existing credentials"
标题简称: 
论文类型: conference
会议简称: CCS
发表年份: 2024
modified: 2025-05-09 10:51:30
created: 2025-04-13 17:52:56
---

## zklogin: Privacy-preserving blockchain authentication with existing credentials

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3658644.3690356)

## 作者

+ [Foteini Baldimtsi](Foteini%20Baldimtsi.md)
+ Konstantinos Kryptos Chalkias
+ Yan Ji
+ Jonas Lindstrøm
+ [Deepak Maram](Deepak%20Maram.md)
+ Ben Riva
+ [Arnab Roy](Arnab%20Roy.md)
+ Mahdi Sedaghat
+ Joy Wang

## 笔记

For many users, a private key based wallet serves as the primary entry point to blockchains. Commonly recommended wallet authentication methods, such as mnemonics or hardware wallets, can be cumbersome. This difficulty in user onboarding has significantly hindered the adoption of blockchain-based applications.

We develop zkLogin, a novel technique that leverages identity tokens issued by popular platforms (any OpenID Connect enabled platform e.g., Google, Facebook, etc.) to authenticate transactions. At the heart of zkLogin lies a signature scheme allowing the signer to sign using their existing OpenID accounts and nothing else. This improves the user experience significantly as users do not need to remember a new secret and can reuse their existing accounts.

zkLogin provides strong security and privacy guarantees. Unlike prior works, zkLogin's security relies solely on the underlying platform's authentication mechanism without the need for any additional trusted parties (e.g., trusted hardware or oracles). As the name suggests, zkLogin leverages zero-knowledge proofs (ZKP) to ensure that the sensitive link between a user's off-chain and on-chain identities is hidden, even from the platform itself.

zkLogin enables a number of important applications outside blockchains. It allows billions of users to produce verifiable digital content leveraging their existing digital identities, e.g., email address. For example, a journalist can use zkLogin to sign a news article with their email address, allowing verification of the article's authorship by any party.

We have implemented and deployed zkLogin on the Sui blockchain as an additional alternative to traditional digital signature-based addresses. Due to the ease of web3 on-boarding just with social login, many hundreds of thousands of zkLogin accounts have already been generated in various industries such as gaming, DeFi, direct payments, NFT collections, sports racing, cultural heritage, and many more.

以下是中文翻译：

对许多用户而言，基于私钥的钱包是进入区块链世界的主要门户。然而，常见的钱包认证方式，如助记词或硬件钱包，往往操作繁琐。这种用户入门的高门槛极大地阻碍了基于区块链应用的普及。

我们开发了zkLogin这一创新技术，它利用由主流平台（任何支持OpenID Connect的平台，如谷歌、脸书等）颁发的身份令牌来验证交易。zkLogin的核心在于一种签名方案，该方案允许签名者仅使用其现有的OpenID账户进行签名，无需其他任何条件。这极大地提升了用户体验，因为用户无需记忆新的密钥，可以直接复用他们已有的账户。

zkLogin提供了强大的安全性和隐私保障。与以往的研究不同，zkLogin的安全性仅依赖于底层平台的认证机制，无需任何额外的可信第三方（如可信硬件或预言机）。正如其名所示，zkLogin利用零知识证明（ZKP）技术，确保用户链下与链上身份间的敏感关联得以隐藏，即便是平台自身也无法窥探。

zkLogin技术不仅限于区块链领域，还支持众多重要应用场景。它让数十亿用户能够利用现有数字身份（如电子邮箱地址）生成可验证的数字内容。举例来说，记者可通过zkLogin使用个人邮箱对新闻稿件进行签名，使得任何一方都能核实文章的真实作者身份。

我们已在Sui区块链上实现并部署了zkLogin，作为传统基于数字签名地址的额外选择。由于仅需社交登录即可轻松接入web3，zkLogin账户已在游戏、DeFi、直接支付、NFT收藏、体育竞速、文化遗产等多个行业中迅速普及，生成账户数量已达数十万之多。

## 关键词

+ 零知识证明
+ 区块链认证
+ 隐私保护
+ OpenID Connect
+ 数字身份
+ Sui区块链