---
title: 门限密码学paper列表
created: 2025-04-17 09:51:00
modified: 2025-05-27 04:19:45
draft: true
---

## 发展历史

+ [Threshold cryptosystems (**EUROCRYPT 1992**)](desmedt1992threshold)
最先提出门限密码学

主要分为两类：

### 隐私门限签名-privacy threshold signature-PTS

> 私有阈值签名（PTS）方案在需要隐藏组织内部运作时使用。例如，一个运行网络服务器的组织可能会选择将服务器的秘密TLS密钥分割到n台机器中，以便至少需要t台机器来生成签名并完成TLS握手。通过使用PTS，组织可以将阈值t对外隐藏，以避免泄露攻击者需要攻陷的机器数量，从而伪造签名。同样，签名不应透露参与生成签名的t台机器的集合，以确保不会暴露当前在线的机器信息。

对消息 $m$ 的签名 $\sigma$ 不会泄露关于门限 $t$ 的任何信息，也不会泄露生成该签名的 $t$ 个参与方的法定人数的信息。即使对手看到一系列其选择的消息上的签名，这一点仍然成立。

+ [Practical threshold signatures (**EUROCRYPT 2000**)](shoup2000practical)
+ [Fully distributed threshold RSA under standard assumptions (**ASIACRYPT 2001**)](fouque2001fully)
+ [Threshold signatures, multisignatures and blind signatures based on the gap-Diffie-Hellman-group signature scheme (**PKC 2002**)](boldyreva2002threshold)
+ 

### 可追责门限签名 accountable threshold signature

> 可追溯阈值签名（ATS）方案通常用于需要问责的金融应用中。例如，如果五位银行高管中需要三位来授权银行转账，那么在批准欺诈性转账的情况下，必须确保完全的问责。当使用ATS方案时，针对欺诈交易的签名将能够识别出授权该交易的三位银行高管。

+ [Short signatures from the Weil pairing (**ASIACRYPT 2001**)](boneh2001short)
+ [Multi-signatures in the plain public-key model and a general forking lemma (**CCS 2006**)](bellare2006multi)
+ [Multisignatures secure under the discrete logarithm assumption and a generalized forking lemma (**CCS 2008**)](bagherzandi2008multisignatures)
+ [Accountable-subgroup multisignatures (**CCS 2001**)](micali2001accountable)
+ [MuSig: Simple two-round Schnorr multi-signatures (**CRYPTO 2021**)](nick2021musig2)

## 草稿

目前收集到的门限密码学在顶会顶刊上的研究进展，有待进一步总结和学习：

+ [UC non-interactive, proactive, threshold ECDSA with identifiable aborts (**CCS 2020**)](canetti2020uc)
+ [Towards scalable threshold cryptosystems (**S&P 2020**)](tomescu2020towards)
+ [Efficient multiplicative-to-additive function from Joye-Libert cryptosystem and its application to threshold ECDSA (**CCS 2023**)](xue2023efficient)
+ [Predicate aggregate signatures and applications (**ASIACRYPT 2023**)](qiu2023predicate)
+ [Multi-signatures for ad-hoc and privacy-preserving group signing (**PKC 2024**)](lehmann2024multi)

## Distributed Key Generation

+ [Aggregatable distributed key generation (**EUROCRYPT 2021**)](gurkan2021aggregatable)
+ [Fast batched asynchronous distributed key generation (**EUROCRYPT 2024**)](groth2024fast)

## threshold encryption

+ [Threshold encryption with silent setup (**CRYPTO 2024**)](garg2024threshold)
+ [Practical mempool privacy via one-time setup batched threshold encryption (**USENIX Security 2024**)](choudhuri2025practical.md)
+ [Secure multiparty computation from threshold encryption based on class groups (**CRYPTO 2023**)](braun2023secure)

## threshold signatures

会议paper

+ [Threshold signatures with private accountability (**CRYPTO 2022**)](boneh2022threshold)
+ [Threshold signatures in the multiverse (**S&P 2023**)](baird2023threshold)
+ [Threshold signatures from inner product argument: Succinct, weighted, and multi-threshold (**CCS 2023**)](das2023threshold)
+ [hints: Threshold signatures with silent setup (**S&P 2024**)](garg2024hints)

期刊paper：

+ [Accountable and secure threshold EdDSA signature and its applications (**TIFS 2024**)](xie2024accountable)
+ [Multi-Signature and Game Based Blockchain Interoperability Oracle (**TDSC 2025**)](wang2025multi)

