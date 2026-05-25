---
title: "Derecho: privacy pools with proof-carrying disclosures"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2024
created: 2025-04-21 11:09:48
modified: 2025-04-21 11:10:01
---

## Derecho: privacy pools with proof-carrying disclosures

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3658644.3670270)

## 作者

+ Josh Beal 
+ [Ben Fisch](Ben%20Fisch.md)
## 笔记

A _privacy pool_ enables clients to deposit units of a cryptocurrency into a shared pool where ownership of deposited currency is tracked via a system of cryptographically hidden records. Clients may later withdraw from the pool without linkage to previous deposits. Some privacy pools also support hidden transfer of currency ownership within the pool. In August 2022, the U.S. Department of Treasury sanctioned Tornado Cash, the largest Ethereum privacy pool, on the premise that it enables illicit actors to hide the origin of funds, citing its usage by the DPRK-sponsored Lazarus Group to launder over $455 million dollars worth of stolen cryptocurrency. This ruling effectively made it illegal for U.S. persons/institutions to use or accept funds that went through Tornado Cash, sparking a global debate among privacy rights activists and lawmakers. Against this backdrop, we present _Derecho,_ a system that institutions could use to request cryptographic attestations of fund origins rather than naively rejecting all funds coming from privacy pools. Derecho is a novel application of _proof-carrying data,_ which allows users to propagate allowlist membership proofs through a privacy pool's transaction graph. Derecho is backwards-compatible with existing Ethereum privacy pool designs, adds no overhead in gas costs, and costs users only a few seconds to produce attestations.

以下是中文翻译：

隐私池允许用户将加密货币存入一个共享池中，通过加密隐藏记录系统追踪存入货币的所有权。用户随后可从该池中提取资金，而无需与之前的存款相关联。部分隐私池还支持在池内进行货币所有权的隐蔽转移。2022年8月，美国财政部以朝鲜支持的拉撒路集团利用其清洗价值超过4.55亿美元的盗窃加密货币为由，对最大的以太坊隐私池Tornado Cash实施制裁，认为其帮助非法行为者隐藏资金来源。这一裁决实际上禁止了美国个人/机构使用或接受通过Tornado Cash流转的资金，引发了全球隐私权活动人士与立法者的激烈辩论。在此背景下，我们推出Derecho系统——金融机构可借此要求对资金来源进行加密验证，而非简单拒绝所有来自隐私池的资金。Derecho是"携带证明数据"技术的新颖应用，允许用户通过隐私池交易图传播白名单成员资格证明。该系统与现有以太坊隐私池设计向后兼容，不增加Gas费用开销，用户仅需数秒即可生成验证凭证。

## 关键词

+ 隐私池
+ 证明携带数据
+ 以太坊
+ 加密货币
+ 合规性
+ Tornado Cash