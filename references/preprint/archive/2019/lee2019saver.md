---
title: "SAVER: SNARK-friendly, Additively-homomorphic, and Verifiable Encryption and decryption with Rerandomization"
标题简称:
论文类型: preprint
预印本简称: archive
发表年份: 2019
---

## SAVER: SNARK-friendly, Additively-homomorphic, and Verifiable Encryption and decryption with Rerandomization

## 发表信息

+ [原文链接](https://eprint.iacr.org/2019/1270)

## 作者

+ Jiwon Lee 
+ Jaekyoung Choi 
+ Jihye Kim 
+ [Hyunok Oh](Hyunok%20Oh.md)
## 笔记

### 背景与动机
可验证加密允许加密者证明被加密数据的特定性质，是构建信任协议（如群签名、密钥托管）的重要原语。理想情况是将可验证加密与支持任意关系的零知识证明（如zk-SNARK）结合，从而实现通用、灵活的可验证加密。然而，确保加密与证明中消息一致性的朴素方法是将整个加密算法编码到zk-SNARK电路中，这会导致电路规模庞大，造成证明时间和CRS大小不切实际。尽管存在针对特定加密（如RSA-OAEP）的电路优化工作[KZM+15a]，但面对现代复杂加密方案（如属性基加密、可再随机化加密）时，这种方法仍因包含过多复杂密码运算而效率低下。本文旨在通过将加密与zk-SNARK电路解耦，设计一种高效且支持多种高级功能的通用可验证加密方案，从而填补这一空白。

### 相关工作

[Gro16] Jens Groth. On the Size of Pairing-Based Non-interactive Arguments. **EUROCRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=On+the+Size+of+Pairing-Based+Non-interactive+Arguments)
> 核心思路：提出了一个至今仍是效率基准的配对-based zk-SNARK，证明仅包含三个群元素。
> 局限与区别：该方案本身不直接支持可验证加密，且证明不具备不可延展性。本文以其为基础构建加密与证明的连接，并扩展了其功能。

[CFQ19] Matteo Campanelli, Dario Fiore, Anaïs Querol. LegoSNARK: Modular Design and Composition of Succinct Zero-Knowledge Proofs. **ACM CCS 2019** [Google Scholar](https://scholar.google.com/scholar?q=LegoSNARK+Modular+Design+and+Composition+of+Succinct+Zero-Knowledge+Proofs)
> 核心思路：提出了承诺-证明框架，通过承诺连接不同的苏零知识证明系统。
> 局限与区别：该框架需要承诺携带加密，但当时不存在能输出兼容承诺的加密方案。本文设计的SAVER是一种承诺携带加密，可直接融入该框架。

[KZM+15a] Ahmed Kosba, Zhichao Zhao, Andrew Miller, Yi Qian, T-H Hubert Chan, Charalampos Papamanthou, Rafael Pass, Abhi Shelat, Elaine Shi. How to Use SNARKs in Universally Composable Protocols. **IACR ePrint 2015/1093** [Google Scholar](https://scholar.google.com/scholar?q=How+to+Use+SNARKs+in+Universally+Composable+Protocols)
> 核心思路：提出了在SNARK电路中使用友谊优化电路的方式来包含标准加密（如RSA-OAEP）的方法。
> 局限与区别：其加密-in-the-circuit方法在面对更复杂的加密（如加法同态加密）时效率仍然很低。本文通过分离加密和证明电路，大幅提升了效率。

[CS03] Jan Camenisch, Victor Shoup. Practical Verifiable Encryption and Decryption of Discrete Logarithms. **CRYPTO 2003** [Google Scholar](https://scholar.google.com/scholar?q=Practical+Verifiable+Encryption+and+Decryption+of+Discrete+Logarithms)
> 核心思路：提出了基于离散对数的可验证加密和解密方案，证明了密文是特定底数的离散对数。
> 局限与区别：关系被预定义为离散对数问题，通用性不足。本文旨在支持任意关系的通用可验证加密。

[BG18] Sean Bowe, Ariel Gabizon. Making Groth’s zk-SNARK Simulation Extractable in the Random Oracle Model. **IACR ePrint 2018/187** [Google Scholar](https://scholar.google.com/scholar?q=Making+Groth+zk-SNARK+Simulation+Extractable+in+the+Random+Oracle+Model)
> 核心思路：通过引入随机谕言机将Groth的zk-SNARK改造为模拟可抽取的，但代价是证明大小增加到5个元素。
> 局限与区别：本文设计时考虑了与不同zk-SNARK的兼容性，但主要基于[Gro16]构建，并说明可适配其他方案。

[BCG+14] Eli Ben-Sasson, Alessandro Chiesa, Christina Garman, Matthew Green, Ian Miers, Eran Tromer, Madars Virza. Zerocash: Decentralized Anonymous Payments from Bitcoin. **IEEE S&P 2014** [Google Scholar](https://scholar.google.com/scholar?q=Zerocash+Decentralized+Anonymous+Payments+from+Bitcoin)
> 核心思路：在zk-SNARK电路中实现Merkle树成员证明，以实现匿名性。
> 局限与区别：该系统中加密是用于交易的，并未支持复杂的可验证加密，特别是无法将加密过程与电路分离。本文借鉴其成员证明技术，并应用于投票场景。

### 核心技术与方案

本文提出的SAVER方案核心思想是将加密与zk-SNARK证明解耦。首先，标准zk-SNARK的验证方程涉及对语句的线性编码。SAVER巧妙地将属于消息的一部分语句嵌入到ElGamal风格的密文中，形成一个初始密文。为了消除盲化因子对验证方程的干扰，方案在CRS中引入了$G^{-\gamma}$元素，并让证明者在证明中调整最后一个证明元素C，使得验证方程中产生的多余项被相互抵消。

具体构造上，消息M被分割为小块$m_i$。公钥PK包含加密所需的公钥和用于验证的承诺参数。加密算法Enc生成一个包含多个块$\mathcal{CT}$的密文，其中第一个块$c_0$是随机数的承诺，后续块$c_i$包含对$m_i$的加密，最后一个块$\psi$是一个Pedersen向量承诺，其运算与密文其他部分一致。证明$\pi$由底层zk-SNARK生成，但最终的证明元素C会与根据随机数计算的参数$P_2^r$相乘。验证算法Verify_Enc通过验证两个等式来保证安全性：第一个等式确保了密文各组件与承诺$\psi$的一致性；第二个等式是改造后的zk-SNARK验证方程，它验证了加密消息和公开语句满足的关系。

除了可验证加密，SAVER还支持加法同态性：两个密文逐个分量相乘得到新密文，解密结果为对应消息之和。再随机化算法能独立生成与原始明文和证明分布相同的新密文和证明，从而支持无需链接性的应用（如投票）。可验证解密算法通过提供一个证明$\nu$，让任何验证者都能确信解密出的消息确实是密文中的内容，而无需知晓解密私钥。

安全性方面，方案在标准模型下基于Decisional Polynomial (D-Poly) 假设满足IND-CPA安全，其证明通过混合论证将攻击SAVER的敌手规约到区分D-Poly挑战的算法。加密可靠性则通过batch-PKE假设和底层zk-SNARK的可靠性来证明，分析了验证方程必须迫使加密的消息与证明中的关系一致。再随机化安全性证明了新证明和密文的联合分布与原始分布不可区分。解密可靠性通过分析验证方程，证明无法为错误的解密消息伪造一个有效的解密证明。系统渐进复杂度上，证明大小为常数（如128B），密文和密钥大小线性依赖于消息块数，证明者计算量主要由底层zk-SNARK的证明时间决定（约0.7s）。

### 核心公式与流程

**[SAVER验证方程]**
$$e(A, B) = e(G^\alpha, H^\beta) \cdot e(\prod_{i=0}^{n} c_i \cdot \prod_{i=n+1}^{l} G_i^{\phi_i}, H^\gamma) \cdot e(C, H^\delta)$$
> 作用：这是改造后的zk-SNARK核心验证方程。该方程同时验证了密文$\mathcal{CT}$中的加密消息和公开语句$\phi_{n+1}, \dots, \phi_l$满足预定义的关系。通过将密文块$c_i$直接放入验证方程，实现了加密与证明的捆绑，而无需在电路内部执行加密算法。

**[SAVER密文和承诺一致性验证]**
$$\prod_{i=0}^n e(c_i, Z_i) = e(\psi, H)$$
> 作用：该方程验证了密文的各个组成部分$c_0, \dots, c_n$与承诺$\psi$之间的一致性，确保了密文结构的正确性，避免了敌手以不一致的方式构造密文。

**[SAVER加法同态性]**
$$\mathcal{CT} \circ \mathcal{CT}' = (X_0^{r+r'}, \{X_i^{r+r'} G_i^{m_i+m_i'}\}_{i=1}^n, P_1^{r+r'} \prod_{j=1}^n Y_j^{m_j+m_j'})$$
> 作用：展示了SAVER支持的加法同态操作。两个密文通过元素级运算（通常是群操作，如椭圆曲线上的点加）得到新密文，对应于对原始消息向量的加法。

### 实验结果

实验在Ubuntu 18.04，Intel i-5 (3.4GHz) 四核，24GB内存的机器上运行，使用了libsnark库和Ajtai哈希函数。针对投票场景，Merkle树高度设为16（支持$2^{16}$选民）。核心性能指标如下：对于2048位消息（|M| = 2048 bits），SAVER加密（不含zk-SNARK证明）仅需8.8ms，而zk-SNARK证明时间约为0.74秒。CRS大小恒定在16MB，几乎不受消息大小影响。密文大小为2381B，公钥和验证密钥大小约为8.7KB和8.5KB，两者随消息线性增长。解密时间为300.4ms。实验结果表明，SAVER将加密开销从复杂的zk-SNARK电路中分离出来，使得加密操作本身极其高效，而证明时间也被控制在亚秒级，展现了出色的实用性。

### 局限性与开放问题
SAVER的安全性基于标准模型下的非标准假设（如Batch-PKE和D-Poly），这或许不如基于标准假设（如SXDH）的方案那样有广泛的信任基础。其次，解密过程需要计算小范围内的离散对数，随着消息块大小的增加，解密时间会显著增长，这限制了其在高吞吐量环境下的应用。此外，方案依赖于将消息分割为小块以进行高效解密，这可能会增加在需要证明复杂消息结构时的电路设计复杂度。最后，虽然论文提出了可适配其他zk-SNARK，但具体实现和性能分析主要围绕[Gro16]进行，其通用性尚需更多实例检验。

### 强关联论文

[Gro16] Jens Groth. On the Size of Pairing-Based Non-interactive Arguments. **EUROCRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=On+the+Size+of+Pairing-Based+Non-interactive+Arguments)

[CFQ19] Matteo Campanelli, Dario Fiore, Anaïs Querol. LegoSNARK: Modular Design and Composition of Succinct Zero-Knowledge Proofs. **ACM CCS 2019** [Google Scholar](https://scholar.google.com/scholar?q=LegoSNARK+Modular+Design+and+Composition+of+Succinct+Zero-Knowledge+Proofs)

[KZM+15a] Ahmed Kosba, Zhichao Zhao, Andrew Miller, Yi Qian, T-H Hubert Chan, Charalampos Papamanthou, Rafael Pass, Abhi Shelat, Elaine Shi. How to Use SNARKs in Universally Composable Protocols. **IACR ePrint 2015/1093** [Google Scholar](https://scholar.google.com/scholar?q=How+to+Use+SNARKs+in+Universally+Composable+Protocols)

[CS03] Jan Camenisch, Victor Shoup. Practical Verifiable Encryption and Decryption of Discrete Logarithms. **CRYPTO 2003** [Google Scholar](https://scholar.google.com/scholar?q=Practical+Verifiable+Encryption+and+Decryption+of+Discrete+Logarithms)

[BG18] Sean Bowe, Ariel Gabizon. Making Groth's zk-SNARK Simulation Extractable in the Random Oracle Model. **IACR ePrint 2018/187** [Google Scholar](https://scholar.google.com/scholar?q=Making+Groth+zk-SNARK+Simulation+Extractable+in+the+Random+Oracle+Model)

[BCG+14] Eli Ben-Sasson, Alessandro Chiesa, Christina Garman, Matthew Green, Ian Miers, Eran Tromer, Madars Virza. Zerocash: Decentralized Anonymous Payments from Bitcoin. **IEEE S&P 2014** [Google Scholar](https://scholar.google.com/scholar?q=Zerocash+Decentralized+Anonymous+Payments+from+Bitcoin)

[Gab19] Ariel Gabizon. On the Efficiency of Pairing-Based Proofs under the d-PKE. **IACR ePrint 2019/148** [Google Scholar](https://scholar.google.com/scholar?q=On+the+Efficiency+of+Pairing-Based+Proofs+under+the+d-PKE)


## 关键词

+ SAVER SNARK解耦可验证加密
+ zk-SNARK加法同态加密结合
+ 可验证解密重随机化密文
+ ElGamal同态加密SNARK友好
+ Vote-SAVER无收据选民匿名投票