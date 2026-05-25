---
title: "Privacy-preserving blueprints"
标题简称:
论文类型: conference
会议简称: EUROCRYPT
发表年份: 2023
modified: 2025-05-13 04:16:09
created: 2025-04-15 11:15:43
---

## Privacy-preserving blueprints

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-30617-4_20)

## 作者

+ [Markulf Kohlweiss](Markulf%20Kohlweiss.md)
+ [Anna Lysyanskaya](Anna%20Lysyanskaya.md)
+ An Nguyen

## 笔记

If everyone were to use anonymous credentials for all access control needs, it would be impossible to trace wrongdoers, by design. This would make legitimate controls, such as tracing illicit trade and terror suspects, impossible to carry out. Here, we propose a privacy-preserving blueprint capability that allows an auditor to publish an encoding $pk_A$ of the function $f(x,\cdot)$ for a publicly known function $f$ and a secret input $x$. For example, $x$ may be a secret watchlist, and $f(x,y)$ may return $y$ if $y \in x$. On input her data $y$ and the auditor's $pk_A$, a user can compute an escrow $Z$ such that anyone can verify that $Z$ was computed correctly from the user's credential attributes, and moreover, the auditor can recover $f(x,y)$ from $Z$. Our contributions are:

+ We define secure f-blueprint systems; our definition is designed to provide a modular extension to anonymous credential systems.
+ We show that secure f-blueprint systems can be contructed for all functions f from fully homomorphic encryption and NIZK proof systems. This result is of theoretical interest but is not efficient enough for practical use.
+ We realize an optimal blueprint system under the DDH assumption in the random-oracle model for the watchlist function.

以下是中文翻译：

如果每个人都使用匿名凭证来满足所有访问控制需求，那么根据设计，将无法追踪不法分子。这将使得合法的控制措施，例如追踪非法交易和恐怖嫌疑人，变得无法实施。在这里，我们提出了一种隐私保护的蓝图能力，允许审计员发布一个已编码的 $pk_A$，用于一个公开已知的函数 $f$ 和一个秘密输入 $x$。例如，$x$ 可能是一个秘密观察名单，而 $f(x,y)$ 可能在 $y \in x$ 时返回 $y$。用户在输入其数据 $y$ 和审计员的 $pk_A$ 后，可以计算出一个托管 $Z$，使得任何人都可以验证 $Z$ 是根据用户的凭证属性正确计算得出的。此外，审计员可以从 $Z$ 中恢复出 $f(x,y)$。我们的贡献包括：

+ 我们定义了安全的 f-蓝图系统；我们的定义旨在为匿名凭证系统提供模块化扩展。
+ 我们展示了可以为所有函数 f 构建安全的 f-蓝图系统，基于完全同态加密和 NIZK 证明系统。这个结果具有理论意义，但在实际应用中效率不足。
+ 我们在随机预言模型下，在 DDH 假设下实现了观察名单函数的最优蓝图系统。

后续工作：

[Updatable Privacy-Preserving Blueprints (**ASIACRYPT 2025**)](david2025updatable)


A High-Level Definition of a Privacy-Preserving Blueprint. We have three types of participants: the users, the verifiers, and the de-anonymization auditor. On input x (for example, a watchlist), the auditor outputs a blueprint pkA that the users and verifiers will need. Next, the user and the verifier engage in an anonymous transaction; we don’t actually care what else happens in this transaction; the user might be proving to the verifier that they are authorized, or it may be an e-cash transaction. What we do care about is that, as a by-product of this transaction, the user and the verifier have agreed on a cryptographic commitment C such that (1) the user is in possession of the opening of C; and (2) the transaction that just occurred guarantees that the opening of C contains user data y that is relevant for the auditor’s needs. For example, imagine that x is a watchlist consisting of names of individuals of interest, and y contains a user’s name; then this user is of interest to the auditor if y ∈ x. To enhance this anonymous transaction with privacy-preserving blueprint capability, the user runs the algorithm Escrow to compute a value Z that is an escrow of the opening of the commitment C; from Z, the auditor will be able to recover the information relevant to him, and no other information about the user. Specifically, in the watchlist scenario, the auditor will recover y if y ∈ x, but will learn nothing about the user if y ∈/ x. More generally, in an f -blueprint scheme, the auditor will recover f (x, y) and no additional information. The verifier’s job is to verify the escrow Z against C using VerEscrow and only let the transaction go through if, indeed, it verifies. It is important that even a malicious auditor cannot create a blueprint that corresponds to an unauthorized input x. To capture this, we also require that there is a publicly available cryptographic commitment CA. Outside of our protocol, we expect a mechanism for arriving at an acceptable (but secret) input x and the commitment CA to x. For example, a judge may publish a commitment to a secret watchlist, and privately reveal the opening to the auditor; or several authorities may be responsible for different components of a watchlist and the auditor aggregates them together in a publicly verifiable fashion; or another distributed protocol can be agreed upon for arriving at the commitment CA such that its opening (i.e., x) is known to the auditor. To ensure that only such an authorized secret input x is blueprinted, a secure blueprint scheme must include an algorithm VerPK that verifies that pkA indeed corresponds to the value to which CA is a commitment.

# 隐私保护蓝图的高级定义

我们有三类参与者：用户、验证者和去匿名化审计员。输入x（例如，监视名单）后，审计员输出用户和验证者所需的蓝图pkA。接下来，用户和验证者进行匿名交易；我们实际上并不关心这个交易中发生的其他事情；用户可能是向验证者证明他们已获授权，或者可能是电子现金交易。我们关心的是，作为这次交易的副产品，用户和验证者已就一个加密承诺（cryptographic commitment）C达成一致，使得(1)用户拥有C的开启信息；以及(2)刚刚发生的交易保证C的开启信息包含与审计员需求相关的用户数据y。例如，假设x是由感兴趣个人姓名组成的监视名单，而y包含用户的姓名；那么如果y∈x，则该用户是审计员感兴趣的对象。为了增强这种匿名交易的隐私保护蓝图功能，用户运行Escrow算法计算一个值Z，该值是承诺C的开启信息的托管；通过Z，审计员将能够恢复与他相关的信息，而不会获取用户的其他信息。具体来说，在监视名单场景中，如果y∈x，审计员将恢复y，但如果y∉x，审计员将不会了解到关于用户的任何信息。更一般地说，在f-蓝图方案中，审计员将恢复f(x,y)而不会获得额外信息。验证者的工作是使用VerEscrow验证托管Z与C的关系，并且只有在确实验证通过时才允许交易进行。

重要的是，即使是恶意的审计员也不能创建对应于未授权输入x的蓝图。为了捕捉这一点，我们还要求有一个公开可用的加密承诺CA。在我们的协议之外，我们期望有一种机制来达成可接受的（但保密的）输入x和对x的承诺CA。例如，法官可能会发布对秘密监视名单的承诺，并私下向审计员揭示开启信息；或者几个权威机构可能负责监视名单的不同组成部分，审计员以公开可验证的方式将它们聚合在一起；或者可以商定另一个分布式协议来达成承诺CA，使得其开启信息（即x）为审计员所知。为确保只有这种授权的秘密输入x被蓝图化，安全蓝图方案必须包括一个算法VerPK，该算法验证pkA确实对应于CA所承诺的值。

## 关键词

+ 隐私保护蓝图
+ 匿名凭证
+ 秘密监视名单
+ DDH假设
+ 访问控制与可追踪性                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   