---
title: Signature-based witness encryption with compact ciphertext
doi: 10.1007/978-981-96-0875-1_1
标题简称: 
论文类型: conference
会议简称: ASIACRYPT
发表年份: 2024
modified: 2025-04-29 10:39:02
created: 2025-04-15 14:12:27
---
## Signature-based witness encryption with compact ciphertext

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-981-96-0875-1_1)

## 作者

+ Gennaro Avitabile 
+ [Nico Döttling](Nico%20D%C3%B6ttling.md)
+ Bernardo Magri 
+ Christos Sakkas 
+ Stella Wohnig 

## 笔记

### 背景与动机
在分布式系统（如区块链）中，多参与方对可预测消息（如区块号或随机信标）进行签名是常见操作。在此基础上，签名基础见证加密（SWE）允许加密者针对一个标签T和一组签名验证密钥集V进行加密，密文只能被持有关于该标签T的足够数量（阈值t）有效签名的一方解密。这种原语在时间释放加密和基于预言机的条件支付中具有自然应用 [9, 29]。然而，现有的无需可信设置的SWE方案，其密文大小与验证密钥的数量n呈线性关系 [9, 29]。在去中心化系统的参与方规模不断增长的背景下，这一线性瓶颈严重限制了方案的可扩展性。本文旨在填补这一空白：在不依赖长期可信设置或强理想模型（如可编程通用群模型）的前提下，构建首个密文大小在验证密钥数量上呈亚线性（具体为多项式对数级别）增长的签名基础见证加密方案，即紧凑型SWE（cSWE）。

### 相关工作

[8] Desmedt等. Threshold cryptosystems. **CRYPTO 1989** [Google Scholar](https://scholar.google.com/scholar?q=Threshold+cryptosystems)
> 核心思路：提出阈值加密概念，通过分布式密钥生成和秘密分享实现阈值解密。
> 局限与区别：需要通信开销大且需参与方之间进行交互以完成解密，且依赖一个生成相关密钥的初始化阶段。SWE无需交互式解密过程，且适合无需通信的区块链场景。

[9] Döttling等. McFly: Verifiable Encryption to the Future Made Practical. **Financial Cryptography 2024** [Google Scholar](https://scholar.google.com/scholar?q=McFly%3A+Verifiable+Encryption+to+the+Future+Made+Practical)
> 核心思路：首次提出SWE概念，利用双线性配对和秘密分享实现，密文线性依赖于验证密钥数n。
> 局限与区别：密文大小线性增长，是本文所要突破的主要瓶颈。本文的cSWE方案将密文压缩至多项式对数规模。

[21] Goyal等. Collision Resistant Broadcast and Trace from Positional Witness Encryption. **PKC 2019** (文中称为All-but-one Signatures) [Google Scholar](https://scholar.google.com/scholar?q=Collision+Resistant+Broadcast+and+Trace+from+Positional+Witness+Encryption)
> 核心思路：引入全但一签名（All-but-one Signatures）的概念，即生成一个在特定消息下不存在有效签名的伪密钥。
> 局限与区别：本文将此概念重新命名为强可穿刺签名（SPS），并作为核心构建块，用于确保在安全规约中，对于未被绑定的诚实参与者的密钥，攻击者无法伪造有效签名。

[29] Madathil等. Cryptographic Oracle-Based Conditional Payments. **NDSS 2023** [Google Scholar](https://scholar.google.com/scholar?q=Cryptographic+Oracle-Based+Conditional+Payments)
> 核心思路：提出近等价的原语——基于阈值签名的可验证见证加密（VweTS），用于区块链条件下的基于预言机的支付。
> 局限与区别：同样面临密文大小线性增长的瓶颈，且依赖于特定的理想化模型。

[24] Hubacek等. On the Communication Complexity of Secure Function Evaluation with Long Output. **ITCS 2015** [Google Scholar](https://scholar.google.com/scholar?q=On+the+Communication+Complexity+of+Secure+Function+Evaluation+with+Long+Output)
> 核心思路：引入某处统计绑定的哈希函数（SSB），其哈希密钥可绑定到特定索引，哈希值和证明大小是多项式对数级别。
> 局限与区别：本文利用SSB哈希来压缩对验证密钥集的承诺，使得混淆图灵机不必将全部密钥硬编码，从而支持不可区分的输入验证。

[28] Lin等. Indistinguishability Obfuscation with Non-trivial Efficiency. **PKC 2016** [Google Scholar](https://scholar.google.com/scholar?q=Indistinguishability+Obfuscation+with+Non-trivial+Efficiency)
> 核心思路：证明通用且具有紧凑输出的委托方案蕴含不可区分混淆（iO）。
> 局限与区别：该结果从反面说明，实现紧凑SWE可能确实需要iO这一强假设。本文采用针对图灵机的iO，以支持伪随机份额的解压缩，而无需将全部运算放入较大的电路中。

[27] Koppula等. Indistinguishability Obfuscation for Turing Machines with Unbounded Memory. **STOC 2015** [Google Scholar](https://scholar.google.com/scholar?q=Indistinguishability+Obfuscation+for+Turing+Machines+with+Unbounded+Memory)
> 核心思路：构造了针对图灵机的不可区分混淆器，其混淆后的机器大小与运行时间的对数呈多项式关系。
> 局限与区别：本文依赖于此技术，该技术是实现紧凑性的关键，使得压缩的伪随机计算（秘密共享）能够被安全地委托给解密方，而无需在密文中嵌入巨大的线性计算电路。

[14] Garg等. Candidate Indistinguishability Obfuscation and Functional Encryption for All Circuits. **FOCS 2013** [Google Scholar](https://scholar.google.com/scholar?q=Candidate+Indistinguishability+Obfuscation+and+Functional+Encryption+for+All+Circuits)
> 核心思路：提出首个候选的不可区分混淆构造，使得混淆电路在功能上不可区分。
> 局限与区别：本文虽然基于iO，但并未直接使用电路混淆，而是利用图灵机混淆以实现更优的压缩效率和对长运行时间的支持。

[33] Sahai等. How to Use Indistinguishability Obfuscation: Deniable Encryption, and More. **STOC 2014** [Google Scholar](https://scholar.google.com/scholar?q=How+to+Use+Indistinguishability+Obfuscation%3A+Deniable+Encryption%2C+and+More)
> 核心思路：展示了利用iO构造多种高级密码学原语（如可否认加密）的方法。
> 局限与区别：本文借鉴了其通过混淆电路实现紧凑性的思想，但本文采用的方法更复杂，需要结合SSB哈希、强可穿刺签名等多个组件以处理动态验证密钥集。

### 核心技术与方案

本文的核心目标是构造一个紧凑的签名基础见证加密方案（cSWE），使得密文大小仅为 $\mathcal{O}(\mathsf{poly}(\lambda \cdot \log n))$，而不是 $\mathcal{O}(n)$。方案的整体框架基于不可区分混淆（iO）用于图灵机，并辅以强可穿刺签名（SPS）和某处统计绑定哈希（SSB）等工具。

方案的核心思想是将秘密共享的份额“推迟”到解密时计算。具体构造流程如下：加密方首先选择一个对称加密密钥 $K$，并用它对消息 $m$ 加密，得到密文 $\mathsf{ct}'$。然后，加密方生成一个混淆的图灵机 $\mathsf{ob}M$。该图灵机的功能是：当输入 $(i, (\mathsf{vk}_i,R_i), \tau, \sigma_i)$ 满足SSB验证（证明 $(\mathsf{vk}_i,R_i)$ 属于哈希承诺的集合）且 $\sigma_i$ 是消息 $T$ 的有效签名时，输出一个伪随机生成的秘密份额 $s_i$。具体来说，这些份额是通过伪随机数生成器（PRF）产生的，并构成一个 $t$-of-$n$ 的Shamir秘密共享。图灵机内部会检查是否 $i > i^*$（初始设 $i^* = 0$），如果是，则通过一个while循环计算并输出 $s_i$。这个循环实现了多项式求值：$s_i = K + \sum_{j=1}^{t-1} \mathsf{PRF}(K_1, j) \cdot i^j$。其中 $K$ 即为对称加密密钥。通过这种方式，密文中仅需包含一个很小的混淆图灵机和一个SSB哈希承诺，而非所有 $n$ 个单独的加密份额。解密时，拥有 $t$ 个有效签名的用户分别运行该混淆图灵机，得到 $t$ 个份额，然后通过拉格朗日插值恢复出密钥 $K$，最后解密出 $m$。

在安全证明中，本文采用了一种非自适应安全模型，其中攻击者在看公钥之前就指定了要攻击的标签 $T^*$ 和腐败密钥集合 $J$。安全证明通过一系列混合论证进行。其核心策略是利用强可穿刺签名（SPS）将所有诚实方的密钥替换为“穿刺”在 $T^*$ 上的密钥，使得任何对 $T^*$ 的有效签名在计算上不存在。接着，利用SSB哈希的索引隐藏性，将哈希的统计绑定位置依次切换到每个诚实方的索引 $i^*$，确保图灵机只能输出与特定 $i^*$ 相关的份额。然后通过混淆器的安全性，逐步修改混淆图灵机，将其内部生成份额的逻辑（即while循环）替换为直接从密钥的后缀 $R_i$ 中解密出份额。由于在穿刺密钥下，攻击者无法获得任何对 $T^*$ 的有效签名，因此对于诚实方的索引，图灵机的输出分支永远不会被触发。基于这一点，可以逐步删除所有诚实的份额信息。最终，整个方案的安全性归结为：在没有足够多（$<t$）份额的情况下，无法区分混合群和真实群的秘密共享分布，从而对称密钥 $K$ 在统计上对攻击者隐藏，其安全性可归约到底层对称加密方案的IND-CPA安全性。得益于混淆图灵机和SSB哈希的性质，本方案在描述和操作上均实现了 $\mathcal{O}(\mathsf{poly}(\lambda \cdot \log n))$ 的开销。

### 核心公式与流程

**[SSB哈希的验证**]
$$ 1 \gets \mathsf{SSB.Vrfy}(\mathsf{hk}, h, i, (\mathsf{vk}_i, R_i), \tau) $$
> 作用：用于验证输入中的验证密钥 $(\mathsf{vk}_i, R_i)$ 确实属于承诺数据库中的第 $i$ 个元素，并提供了有效的证明 $\tau$。此机制确保混淆图灵机只接受由加密方所指定的密钥集。

**[Shamir秘密共享的核心计算（图灵机内部）]**
$$ s_i = K + \sum_{j=1}^{t-1} \mathsf{PRF}(K_1, j) \cdot i^j $$
> 作用：这是混淆图灵机内部计算份额的公式。它表示一个关于索引 $i$ 的 $t-1$ 次多项式在点 $i$ 处的求值，而常数项即为对称密钥 $K$。该多项式完全由伪随机函数 $\mathsf{PRF}(K_1, \cdot)$ 定义，从而保证了 $t-1$ 个签名（即 $t-1$ 个份额）无法恢复 $K$。

**[拉格朗日插值恢复密钥]**
$$ K' = \sum_{i \in I} c_i \cdot L_i(0) \quad \text{其中} \quad L_i(0) = \prod_{\substack{j \in I \\ j \neq i}} \frac{-j}{i-j} $$
> 作用：解密方在获得 $|I| \ge t$ 个份额 $c_i$ 后，通过拉格朗日插值计算多项式在0点的值，从而恢复出对称密钥 $K$。这利用了Shamir秘密共享的完美重构性质。

**[强可穿刺签名（SPS）的密钥生成]**
$$ (\mathsf{vk}^*, \mathsf{sk}^*) \gets \mathsf{Sig.PKeyGen}(1^\lambda, T^*) $$
> 作用：为诚实密钥对生成一个穿刺于特定消息 $T^*$ 的密钥。该密钥生成的签名对 $T^*$ 无效（即不存在有效签名），但在其他消息上是正常的。在安全证明中，这一操作确保攻击者无法获得对挑战消息 $T^*$ 的有效签名，从而无法触发混淆图灵机的诚实份额输出分支。

**[紧凑密文结构]**
$$ \mathsf{ct} = (\mathsf{ob}M, \mathsf{ct}', \mathsf{hk}) $$
> 作用：展示了最终的紧凑密文结构。$\mathsf{ob}M$ 是一个大小仅与 $\mathsf{poly}(\lambda, \log n)$ 相关的混淆图灵机，$\mathsf{ct}'$ 是消息的对称加密，$\mathsf{hk}$ 是大小也为 $\mathcal{O}(\mathsf{poly}(\lambda) \cdot \log n)$ 的 SSB 哈希密钥。

### 实验结果
本文是一篇理论性的密码学论文，主要贡献在于提出概念并给出可行性构造，并没有提供具体的实验实现或性能基准测试。因此，没有可供报告的实验数值。本文核心的“性能”体现为渐进理论复杂度：加密生成的密文大小为 $\mathcal{O}(\mathsf{poly}(\lambda \cdot \log n))$，这相比现有SWE方案的 $\mathcal{O}(n)$ 具有理论上的显著改进。解密时，需要 $t$ 次调用混淆图灵机，以及一次 $t$ 个点的拉格朗日插值。混淆图灵机的运行时间与 $t$ 成正比（因为包含一个while循环），但密文大小不再随 $n$ 线性增长。该构造适用于任意多项式数量的验证者和阈值 $t$。

### 局限性与开放问题
本文方案的核心局限在于其基于不可区分混淆（iO）这一非常强的假设，尽管它无需可信设置，但iO的实际效率仍然极低，使得该方案主要停留在理论可行性证明层面。此外，当前方案仅能提供非自适应安全性，即攻击者在看到公钥之前预先指定挑战标签和腐败集，这在实际场景中可能不够强。如何将方案的安全性提升至自适应模型，或者探索基于更标准、弱一些的假设（如LWE）的构造，是重要的开放问题。最后，方案对混淆图灵机的依赖虽然实现了紧凑性，但如何将理论框架转化为可实际部署的高效系统，仍需进一步研究。

### 强关联论文

[8] Desmedt, Y., Frankel, Y.: Threshold cryptosystems. **CRYPTO 1989**

[9] Döttling, N., Hanzlik, L., Magri, B., Wohnig, S.: McFly: Verifiable Encryption to the Future Made Practical. **Financial Cryptography 2024**

[21] Goyal, R., Vusirikala, S., Waters, B.: Collision Resistant Broadcast and Trace from Positional Witness Encryption. **PKC 2019**

[29] Madathil, V., Thyagarajan, S.A.K., Vasilopoulos, D., Fournier, L., Malavolta, G., Moreno-Sanchez, P.: Cryptographic Oracle-Based Conditional Payments. **NDSS 2023**

[24] Hubacek, P., Wichs, D.: On the Communication Complexity of Secure Function Evaluation with Long Output. **ITCS 2015**

[27] Koppula, V., Lewko, A.B., Waters, B.: Indistinguishability Obfuscation for Turing Machines with Unbounded Memory. **STOC 2015**

[14] Garg, S., Gentry, C., Halevi, S., Raykova, M., Sahai, A., Waters, B.: Candidate Indistinguishability Obfuscation and Functional Encryption for All Circuits. **FOCS 2013**

[33] Sahai, A., Waters, B.: How to Use Indistinguishability Obfuscation: Deniable Encryption, and More. **STOC 2014**

[17] Garg, S., Srinivasan, A.: A Simple Construction of iO for Turing Machines. **TCC 2018**

[2] Boneh, D., Lynn, B., Shacham, H.: Short Signatures from the Weil Pairing. **ASIACRYPT 2001**


## 关键词

+ 见证加密
+ 不可区分混淆
+ 可打孔签名
+ 分布式签名
+ 密码学