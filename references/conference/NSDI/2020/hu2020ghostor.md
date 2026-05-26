---
title: "Ghostor: Toward a Secure Data-Sharing System from Decentralized Trust"
标题简称:
论文类型: conference
会议简称: NSDI
发表年份: 2020
created: 2025-04-27 09:14:53
modified: 2025-04-27 09:20:04
---

## Ghostor: Toward a Secure Data-Sharing System from Decentralized Trust

## 发表信息

+ [原文链接](https://www.usenix.org/conference/nsdi20/presentation/hu-yuncong)

## 作者

+ [Yuncong Hu](Yuncong%20Hu.md) 
+ Sam Kumar 
+ [Raluca Ada Popa](Raluca%20Ada%20Popa.md)

## 笔记

### 背景与动机

数据共享系统广泛应用于敏感数据存储，但现有方案在抵御恶意服务器攻击时存在严重不足。即使在加密和签名的保护下，一个攻陷了服务器的攻击者仍然能够利用用户的元数据，例如哪些用户共享了文件、何时访问，从而推断出用户的敏感信息（如图1中利用访问医疗记录推断癌症）[81, 89]。此外，攻击者还可以通过回滚攻击重放文件旧版本，或通过分叉攻击隐藏用户更新，导致用户无法察觉数据篡改，这在高安全要求的场景（如医疗）中尤为危险。为解决此类威胁，学术界和工业界提出了多种技术：匿名性技术用于隐藏用户身份，可验证一致性技术用于抵御回滚和分叉攻击。然而，现有最先进的系统在实现这些更强的安全保证时，通常依赖集中化信任，例如假设一个受信任的辅助方[66, 90]、将服务器拆分成两个组件并假设其中之一是诚实的[49, 54, 74]，或假设攻击者是被动的“半诚实”模型[7, 16, 65, 104]。这些假设与日益频繁的针对性攻击相矛盾，攻击者能够通过恶意软件修改软件或数据来攻陷任何中央机器[62, 106, 107]。Mazières 和 Shasha [69] 证明了如果不假设客户端可靠在线，在不信任服务器的情况下检测分叉攻击是不可能的。因此，本文致力于回答一个核心问题：能否在不依赖集中化信任的前提下，在一个数据共享系统中同时实现强隐私和强完整性保证？

### 相关工作

[64] Li et al. Secure Untrusted Data Repository (SUNDR). **OSDI 2004** [Google Scholar](https://scholar.google.com/scholar?q=Secure+Untrusted+Data+Repository+%28SUNDR%29)
> 核心思路：使用哈希链和版本向量实现分叉一致性，允许用户检测服务器的分叉攻击。
> 局限与区别：SUNDR 要求用户用个人密钥签名，泄露了用户身份；其版本向量机制会暴露每个对象的版本号，与 Ghostor 追求的匿名性（隐藏用户身份）相悖。Ghostor 改用共享能力（capabilities）签名，并重设计并发处理来解决匿名性问题。

[35] Goh et al. SiRiUS: Securing Remote Untrusted Storage. **NDSS 2003** [Google Scholar](https://scholar.google.com/scholar?q=SiRiUS%3A+Securing+Remote+Untrusted+Storage)
> 核心思路：端到端加密（E2EE）系统，服务器仅存储密文，用户通过密钥列表（KeyList）分发解密密钥。
> 局限与区别：SiRiUS 的密钥列表绑定用户公钥，服务器可观察到用户的公钥和 ACL 关系，泄露了用户身份信息。Ghostor 使用密钥隐私加密和共享能力来隐藏此类信息。

[7] Backes et al. Anonymous RAM. **ESORICS 2016** [Google Scholar](https://scholar.google.com/scholar?q=Anonymous+RAM)
> 核心思路：提出 AnonRAM，通过 ORAM 和假访问实现全局 obliviousness，隐藏哪个对象被访问。
> 局限与区别：AnonRAM 假设“诚实但好奇”的服务器（不发起主动攻击），且不提供对象共享能力；它也不处理资源滥用问题。Ghostor 的匿名性技术可以应用于此类方案（构建 Ghostor-MH），使其能抵抗恶意攻击并提供共享功能，但 Ghostor 本身专注于更实际的数据共享应用，不追求全局 obliviousness 的高昂开销。

[66] Maffei et al. Maliciously Secure Multi-Client ORAM. **ACNS 2017** [Google Scholar](https://scholar.google.com/scholar?q=Maliciously+Secure+Multi-Client+ORAM)
> 核心思路：提出一个恶意安全的多客户端 ORAM 方案，保护访问模式。
> 局限与区别：该方案依赖一个不可腐蚀的服务器或可信第三方来分发密钥和维持系统状态，即集中化信任。Ghostor 的信任模型是去中心化的，不依赖任何单一诚实方。

[49] Karapanos et al. Verena: End-to-end integrity protection for web applications. **S&P 2016** [Google Scholar](https://scholar.google.com/scholar?q=Verena%3A+End-to-end+integrity+protection+for+web+applications)
> 核心思路：使用一个独立的哈希服务器（Hash Server）来存储和验证操作的哈希值，该哈希服务器被假设为诚实且不与存储服务器合谋。
> 局限与区别：哈希服务器是一个集中化信任点，攻击者只需攻破该服务器即可破坏完整性保证。Ghostor 使用区块链替代哈希服务器，避免了这一单点故障和信任假设。

[55] Kim et al. Caelus: Verifying the consistency of cloud services with battery-powered devices. **S&P 2015** [Google Scholar](https://scholar.google.com/scholar?q=Caelus%3A+Verifying+the+consistency+of+cloud+services+with+battery-powered+devices)
> 核心思路：利用电池供电的低功耗设备验证云存储服务的 fork 一致性，设备需要记录服务的历史哈希值。
> 局限与区别：Caelus 假设部分客户端必须经常在线以参与验证，并无法抵抗恶意客户端与服务器的共谋。Ghostor 的验证过程不需要所有客户端持续在线，只需在每个纪元结束时验证一次。

### 核心技术与方案

Ghostor 的核心目标是实现两个安全属性：匿名性（Anonymity）和可验证线性一致性（Verifiable Linearizability, VerLinear）。它通过重新设计系统以摒弃常见的、依赖集中化信任的范式来实现这些目标，其整体架构如图 3 所示。

**匿名性（Hiding User Identities）**。Ghostor 通过“匿名分布式共享能力”这一核心技术来实现匿名性。这需要解决三个子问题。第一，**消除服务器可见的 ACL**：传统的基于 ACL 的访问控制会暴露哪些用户有权访问哪个对象。Ghostor 的替代方案是，每个对象拥有三个签名密钥对：PVK (权限验证公钥)、RVK (读取验证公钥)、WVK (写入验证公钥)。所有授权用户共享同一组签名私钥（作为能力凭证），使用这些私钥签名操作。服务器只需验证操作是否使用正确的密钥签名，而无需知道签名者是谁。关键列表（KeyList）位于对象头中，该列表包含每个授权用户对应的能力，并加密存储。由于使用密钥隐私加密（Key-Private Encryption）[10]，密文不会泄露用于加密的公钥。第二，**消除用户账户和用户特定邮箱**：为避免服务器通过跟踪账户访问来关联用户操作，Ghostor 不做任何用户特定的存储。对象头充当“对象特定邮箱”，所有访问同一对象的用户都读取同一个头文件，从而在服务器视角上无法区分不同用户。第三，**消除客户端缓存**：由于客户端缓存会泄露用户访问同一对象的连续性（即“同一用户重复访问”），Ghostor 禁止客户端缓存密钥或头文件。

**可验证线性一致性（Verifiable Linearizability）**。Ghostor 通过“可验证匿名历史”来实现，包括三个组件：哈希链摘要、周期性检查点、以及匿名验证过程。
1.  **哈希链摘要**：每个对象都有一个独立的摘要链。每次 GET 或 PUT 操作都会生成一个名为“摘要”的记录（Table 3）。摘要包含纪元号、对象公钥（PVK, WVK, RVK）、前向哈希 Hashprev、数据哈希 Hashdata、客户端签名（使用能力密钥）、服务器签名 Sigs\(_{server}\) 以及一个随机数。客户端的签名使用对象的共享能力密钥（如 WSK），而非个人签名密钥，因此服务器无法得知签名者身份。服务器的签名使摘要成为不可否认的证据。
2.  **周期性检查点**：为了检测并阻止分叉攻击，Ghostor 将纪元结束时每个对象最新摘要的哈希值组合成一个 Merkle 树，并将树根哈希发布到区块链上。区块链的不可篡改性和一致性保证所有用户看到相同的根哈希，从而固定了每个纪元所有对象的历史状态。这避免了使用中心化的哈希服务器。
3.  **并发操作处理**：由于客户端需要读取最新摘要才能构造下一个摘要，这会产生并发冲突。Ghostor 优化了 GET 操作，允许服务器代为填充哈希值。对于 PUT 操作，Ghostor 采用两阶段协议：先执行 PREPARE 阶段，客户端发送一个无数据哈希的摘要，服务器签名后返回；然后执行 COMMIT 阶段，客户端发送包含新数据哈希和 PREPARE 摘要哈希（Hash\(_{prep}\)）的最终摘要。Ghostor 通过冲突解决策略（选择 PREPARE 哈希最新的写入作为胜者）来确保线性一致性，因为服务器无法篡改由客户端签名的 Hash\(_{prep}\) 字段，有效防止了时间拉伸攻击和重放攻击。对于并发的 GET 和 PUT，线性化顺序将 GET 安排在 PUT 之前。

### 核心公式与流程

**[摘要 (Digest) 结构]**
$$\text{Digest} = \left( \text{Epoch}, \text{PVK}, \text{WVK}, \text{RVK}, \text{Hash}_{\text{prev}}, \text{Hash}_{\text{keylist}}, \text{Hash}_{\text{data}}, \text{Sig}_{\text{client}}, \text{Sig}_{\text{server}}, \text{nonce} \right)$$
> 作用：每一笔 GET 或 PUT 操作都由一个摘要表示，该摘要记录了操作发生的时间（纪元）、涉及的权限密钥、前一个操作的历史链接、数据哈希，并由客户端和服务器双重签名，以提供不可否认性。该结构是进行可验证一致性的基础。

**[Merkle 树检查点]**
$$h_{\text{root}} = \text{MerkleRoot} \left( \left\{ \text{Hash}_{D_i} \right\}_{i=1}^{N} \right)$$
> 作用：在每个纪元结束时，服务器将所有对象的历史链的最新摘要哈希值 $\text{Hash}_{D_i}$ 作为叶子节点，构建一棵 Merkle 树，并将树根 $h_{\text{root}}$ 发布到区块链上。这将以太坊或 Zcash 等区块链的一致性保证扩展到整个系统，防止服务器对任意对象进行分叉攻击。

**[两阶段 PUT 协议]**
1.  **PREPARE 阶段**：客户端生成摘要 $D_{\text{prep}}$，包含 $\text{epoch}$、$\text{PVK}$、$\text{RVK}$、$\text{WVK}$、$\text{nonce}$，并用 $\text{WSK}$ 签名。服务器收到后，填充 $\text{Hash}_{\text{prev}}$、$\text{Hash}_{\text{keylist}}$、$\text{Hash}_{\text{data}}$，用 $\text{SSK}$ 签名并追加到对象的摘要链中，将签名后的 $D_{\text{prep}}$ 返回给客户端。
2.  **COMMIT 阶段**：客户端组装最终摘要 $D_{\text{commit}} = \left( \text{epoch}, \text{PVK}, \text{WVK}, \text{RVK}, \text{Hash}_{\text{prep}}, \text{Hash}_{\text{data\_new}}, \text{nonce} \right)$，其中 $\text{Hash}_{\text{prep}} = \text{Hash}(D_{\text{prep}})$。客户端用 $\text{WSK}$ 签名后，将 $D_{\text{commit}}$ 和新数据发送给服务器。服务器根据冲突解决策略决定写入结果（若为胜出写入，则更新数据；若为失败写入，则记录为“附录”），并用 $\text{SSK}$ 签名后追加到摘要链。
> 作用：由于 $D_{\text{commit}}$ 包含了 $D_{\text{prep}}$ 的哈希，服务器无法对同一 PREPARE 生成不同的 COMMIT 结果来进行时间拉伸攻击（例如，将写入延迟到另一个写入之后）。冲突解决策略保证了所有客户端看到一致的线性化顺序。

### 实验结果

Ghostor 在 Amazon EC2 上使用三个 i3en.xlarge 服务器作为 Ceph RADOS 集群进行了评估。实验设置了六种系统对比：Insec（不安全基线）、E2EE（端到端加密）、Anon（仅匿名）、ForkC（仅分叉一致性）、VLinear（仅可验证线性一致性）和 Ghostor（完整版）。

在单对象吞吐量测试中，对于 1 KiB 对象的读写，Ghostor 的吞吐量比 Insec 基线低了两个数量级（约 50 op/s 对比 7000 op/s）。在多对象基准测试中，瓶颈消失，Ghostor 的 1 KiB 对象的读写吞吐量约为 4000-5000 op/s。在 YCSB 基准测试中，与 Insec 基线相比，仅匿名性（Anon）引入了高达 25% 的开销，而分叉一致性（ForkC）引入了 3-4 倍的开销。结合匿名性和可验证一致性的 Ghostor 整体吞吐量下降约为 4-5 倍，例如在 YCSB 工作负载 A 下，Insec 为 9500 op/s，而 Ghostor 约为 2000 op/s。

端到端延迟方面，使用 Tor 匿名网络和难度适中的 PoW（客户端平均求解时间约 3.2 秒）后，客户端的主导延迟来自 PoW 和 Tor。例如，对于 10 KiB 对象的 PUT 操作，70% 的请求在约 40 秒内完成，1 MiB 对象的 PUT 操作更高。相比之下，对于 1 MB 对象，Insec 的服务器端延迟仅为约 2 毫秒。验证过程的成本是线性的，验证 10000 个操作每个约 360 微秒，而服务器计算包含 10,000 个对象的 Merkle 根约需 2.5 秒。

### 局限性与开放问题

尽管 Ghostor 在不依赖集中化信任方面取得了进展，但其性能开销显著，特别是对于频繁的小对象操作，这限制了其在延迟敏感型场景中的应用。系统的匿名性依赖于用户不使用客户端缓存，但这会强制增加网络往返并降低性能。此外，当前实现假设用户不会对特定对象启动并发 ACL 更改，这限制了一部分应用场景的灵活性。针对恶意用户的攻击（例如窃取密钥导致数据泄露），Ghostor 依赖传统方案（如秘密共享）来备份密钥，但系统的核心机制并未设计容错或密钥轮换策略。未来工作可以探索更高效的并发存协议，以及研究如何在保持匿名性的同时提供更精细化的资源控制策略，或许可以结合更轻量级的匿名支付方案或访问模式混淆技术。

### 强关联论文

[7] Backes et al. Anonymous RAM. **ESORICS 2016** 
[35] Goh et al. SiRiUS: Securing Remote Untrusted Storage. **NDSS 2003** 
[49] Karapanos et al. Verena: End-to-end integrity protection for web applications. **S&P 2016** 
[55] Kim et al. Caelus: Verifying the consistency of cloud services with battery-powered devices. **S&P 2015** 
[64] Li et al. Secure Untrusted Data Repository (SUNDR). **OSDI 2004** 
[66] Maffei et al. Maliciously Secure Multi-Client ORAM. **ACNS 2017** 
[69] Mazières et al. Building secure file systems out of Byzantine storage. **PODC 2002** 
[75] Popa et al. Building web applications on top of encrypted data using Mylar. **NSDI 2014** 
[93] Tomescu et al. Catena: Efficient non-equivocation via Bitcoin. **S&P 2017** 
[105] Zcash. **2016**


## 关键词

+ 去中心化信任
+ 数据共享系统
+ 用户身份隐藏
+ 可验证匿名历史
+ 完整性验证
+ 区块链轻量应用