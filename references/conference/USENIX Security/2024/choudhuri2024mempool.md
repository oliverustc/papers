---
title: "Mempool privacy via batched threshold encryption: Attacks and defenses"
标题简称:
论文类型: conference
会议简称: USENIX Security
发表年份: 2024
created: 2025-04-29 10:17:53
modified: 2025-04-29 10:19:47
---

## Mempool privacy via batched threshold encryption: Attacks and defenses

## 发表信息

+ [原文链接](https://www.usenix.org/conference/usenixsecurity24/presentation/choudhuri)

## 作者

+ [Arka Rai Choudhuri](Arka%20Rai%20Choudhuri.md)
+ [Sanjam Garg](Sanjam%20Garg.md) 
+ Julien Piet 
+ [Guru-Vamsi Policharla](Guru-Vamsi%20Policharla.md)
## 笔记

### 背景与动机  
区块链去中心化金融（DeFi）的用户面临严重的不对称信息问题：矿工或区块构建者不仅能看到内存池（mempool）中所有交易详情，还能控制交易执行顺序，从而实施抢跑、夹击等市场操纵策略（即“矿工可提取价值”MEV）[18]。据统计仅2021年以太坊上因MEV损失约2亿美元，且多数收益归矿工[48]。此外，用户发现智能合约漏洞后需紧急修复，但若修复交易在mempool中被提前窥见，攻击者可抢在修复前窃取资金——这类“暗森林”攻击已普遍存在[52,54]。因此保护mempool中交易的隐私至关重要。现有基于阈值公钥加密的方案[5,58]存在两大缺陷：一是无法抵抗“可塑性攻击”（adversary可篡改密文或复制密文中的标签从而窃取未上链交易的信息）；二是解密时通信量与委员会规模n和区块交易数B线性相关（O(nB)），在带宽受限的区块链网络中造成不可接受的延迟（每千字节额外增加约80ms广播延迟[22]）。本文旨在填补这一空白，提出**批处理阈值加密**（batched threshold encryption, bTPKE）并给出首个具体高效的构造。

### 相关工作  

[5] Bebel et al. Ferveo: Threshold decryption for mempool privacy in BFT networks. **ePrint 2022** [Google Scholar](https://scholar.google.com/scholar?q=Ferveo+Threshold+decryption+for+mempool+privacy+in+BFT+networks)  
> 核心思路：采用阈值加密保护mempool隐私，委员会成员广播部分解密，组合后得到明文。  
> 局限与区别：解密通信量为O(nB)，且未解决可塑性攻击；本文构造将通信量降为O(n)并实现CCA2安全。

[24] Döttling et al. McFly: Verifiable encryption to the future made practical. **ePrint 2022** [Google Scholar](https://scholar.google.com/scholar?q=McFly+Verifiable+encryption+to+the+future+made+practical)  
> 核心思路：利用聚合BLS签名作为解密密钥，实现“对未来加密”的等待加密。  
> 局限与区别：未上链的交易在密钥发布后失去隐私（无“待处理交易隐私”）；本文通过批处理阈值加密避免此问题。

[58] Shutter Network contributors. The shutter network. **online 2021** [Google Scholar](https://scholar.google.com/scholar?q=The+shutter+network)  
> 核心思路：部署基于身份基阈值加密的mempool隐私方案，同一epoch共享一个解密密钥。  
> 局限与区别：可塑性攻击（明文攻击者可篡改密文导致隐私泄露）；未上链交易在epoch结束后被解密。本文发现并披露了该漏洞。

[13] Canetti et al. An efficient threshold public key cryptosystem secure against adaptive chosen ciphertext attack. **EUROCRYPT 1999** [Google Scholar](https://scholar.google.com/scholar?q=An+efficient+threshold+public+key+cryptosystem+secure+against+adaptive+chosen+ciphertext+attack)  
> 核心思路：提出CCA2安全的阈值公钥加密，每个密文解密需各成员广播部分解密。  
> 局限与区别：通信量O(nB)，不适合大区块；本文定义了批处理阈值加密的更强效率要求。

[12] Boneh et al. Key homomorphic PRFs and their applications. **CRYPTO 2013** [Google Scholar](https://scholar.google.com/scholar?q=Key+homomorphic+PRFs+and+their+applications)  
> 核心思路：构建门限Cramer-Shoup加密方案。  
> 局限与区别：效率与[13]类似，无法满足亚线性通信需求。

[39] Kate et al. Constant-size commitments to polynomials and their applications. **ASIACRYPT 2010** [Google Scholar](https://scholar.google.com/scholar?q=Constant-size+commitments+to+polynomials+and+their+applications)  
> 核心思路：提出KZG多项式承诺方案，承诺和打开证明均为常大小。  
> 作用：本文基于此构建批处理阈值加密，利用其可验证的打开证明实现“先加密后批量解密”。

[11] Boneh et al. Identity-based encryption from the Weil pairing. **CRYPTO 2001** [Google Scholar](https://scholar.google.com/scholar?q=Identity-based+encryption+from+the+Weil+pairing)  
> 核心思路：利用双线性对实现身份基加密，加密时使用身份对应公钥。  
> 作用：本文借鉴其构造中的哈希与对幂运算，将密文设计为“对多项式打开证明的加密”。

[24] (同上，因直接对比，已列)  
[5] (同上)  
[58] (同上)  

### 核心技术与方案  
**整体框架**：本文定义批处理阈值公钥加密（bTPKE）的语法与安全模型（通过理想功能$\mathcal{F}_{\mathsf{bTPKE}}$形式化），要求：①加密时间与委员会规模无关（O(1)）；②每方部分解密大小亚线性于批大小B（实际为常数）；③秘密保留未选入批的密文隐私。构造基于KZG多项式承诺方案，利用其确定性承诺和可验证打开，将委员会持有的秘密设为多项式陷阱门（τ和α），用户将消息加密到随机点对$(x,y)$，委员会通过插值唯一$B$次多项式$p(X)$满足所有选定点并广播$p(0)$实现批量解密。

**构造思路**：  
- **Setup**：生成CRS（$g,g^\tau,\dots,g^{\tau^B},h,h^\tau$）和$\gamma$处的拉格朗日系数$L_i(\gamma)$的秘密共享；公钥pk包含CRS和NIZK的CRS。  
- **EpochSetup**：为每个epoch采样$\alpha,\delta,r$，发布$\tilde{g}=g^\delta,\tilde{h}=h^\delta$和$\mathsf{com}=g^\alpha\tilde{g}^r$；委员会持有$[\alpha L_B(\gamma)]$和$[r]$的秘密共享。  
- **Enc**：用户选随机$x\in\Omega$，计算$S=g^s$和$y=H(S)$；加密消息$M$为：  
  $$  
  \mathsf{ct}^{(1)}=H(e(\mathsf{com}/g^y,h)^\rho)\oplus M,\quad \mathsf{ct}^{(2)}=(h^\tau/h^x)^\rho,\quad \mathsf{ct}^{(3)}=\tilde{h}^\rho,  
  $$  
  并附上$S,x$及NIZK证明$\phi$（证明知道$s,\rho$）。  
- **BatchDec**：委员会选定$B$个密文（$x_i$互异），通过插值多项式$p(X)$满足$p(\omega^i)=y_i$且$p(\tau)=\alpha$（因为$\mathsf{com}=g^{p(\tau)}$）。广播$[p(\gamma)]_i$和$g^{[r]_i}$。  
- **Combine**：重构$p(\gamma)$和$g^r$，通过Fourier变换生成所有KZG打开证明$\pi_i=(g^{q_i(\tau)},g^r)$，其中$q_i(X)=(p(X)-y_i)/(X-x_i)$；解密：  
  $$  
  M_i=\mathsf{ct}_i^{(1)}\oplus H\big(e(\pi_i^1,\mathsf{ct}_i^{(2)})\cdot e(\pi_i^2,\mathsf{ct}_i^{(3)})\big).  
  $$

**安全性直觉**：CCA2安全性通过使用NIZK确保密文不可塑；未选入批的密文因多项式$p$在$x$处不等于$y$而无法打开；利用随机KZG承诺的隐藏性，即使知道$p(X)$也无法打开虚假点。协议在$t<n/3$恶意模型下模拟理想功能，依赖q-SBDHT假设和随机谕言模型。

**渐进复杂度**：
- 加密：O(1)时间，密文大小370字节（32字节消息时）。
- 部分解密：每方O(B)（主要耗在验证NIZK），大小80字节（1个域元素+1个$\mathbb{G}_1$元素），与B无关。
- 重构：O(B log B)群运算+O(B)对运算，完全可并行。

### 核心公式与流程  

**[KZG多项式承诺打开证明]**  
$$  
e(\mathsf{com}/g^y, h) = e(\pi^1, h^\tau/h^x) \cdot e(\pi^2,\tilde{h}),  
$$  
其中$\mathsf{com}=\tilde{g}^r g^{p(\tau)}$，$\pi^1=g^{q(\tau)}$，$q(X)=(p(X)-y)/(X-x)$，$\pi^2=g^r$。  
> 作用：验证打开的正确性，本文利用该等式组织加密：用户将$e(\mathsf{com}/g^y,h)^\rho$作为蒙蔽掩码，并提供$h^{\rho(\tau-x)}$和$\tilde{h}^\rho$供解密时计算配对。

**[加密公式]**
$$
\operatorname{ct} = \big( H(e(\operatorname{com}/g^{y}, h)^\rho) \oplus M,\; (h^\tau/h^x)^\rho,\; \tilde{h}^\rho,\; S,\; x,\; \phi \big).
$$
> 作用：用户用随机对$(x,y)$（$y=H(g^s)$）和随机$\rho$加密，使得只有知道对应多项式打开证明者才能恢复掩码。

**[批量解密部分解密输出]**
$$
[ p(\gamma) ]_i = \sum_{j=0}^{B-1} p(x_j)[L_j(\gamma)]_i + [L_B(\gamma)p(\tau)]_i,
$$
其中$x_j$为选中的密文中的点，$p(\tau)=\alpha$，$L_j$为拉格朗日系数。
> 作用：每个委员会成员利用其秘密共享线性计算$p(\gamma)$的份额，广播后重构即可恢复整个多项式$p(X)$。

**[重构与消息恢复]**
$$
M_i = \operatorname{ct}_i^{(1)} \oplus H\big( e(g^{q_i(\tau)},\,(h^\tau/h^{x_i})^\rho) \cdot e(g^r,\tilde{h}^\rho) \big).
$$
> 作用：利用重构的多项式$p(X)$和$g^r$生成KZG打开证明，通过双线性对计算蒙蔽掩码后解密。

### 实验结果  
实验在2019款MacBook Pro（2.4 GHz Intel Core i9，16GB RAM）单线程模式下运行，采用BLS12-381曲线和BLAKE3哈希函数。  
- **加密时间**：小于6ms，与委员会规模或批大小无关。  
- **密文大小**：370字节（含1个$\mathbb{G}_1$元素、2个$\mathbb{G}_2$元素、3个域元素、2字节$x$索引及消息本身）。  
- **部分解密时间**：与批大小线性相关，批大小为512时约2818.6ms，主要开销来自NIZK验证（>99%）。  
- **重构时间**：批大小为512时约3472.2ms，瓶颈为O(BlogB)群运算和O(B)对配对。  
- **通信量**：每方部分解密仅80字节（1个域元素+1个$\mathbb{G}_1$元素），委员会128人、批512笔交易时总广播10KB，而Ferveo需要3MB（慢约300倍）。  
- **委员会变更**：利用[33]的动态主动秘密分享协议，64人委员会在WAN下刷新一个秘密需1.5秒（含设置8.21秒）。  
- **与已有的对比**：本文加密gas成本约$1.9（较Ferveo的$0.7高），但解密广播仅占区块大小2%（Ferveo为500%），权衡可接受。

### 局限性与开放问题  
本文的Setup和EpochSetup阶段需要较为昂贵的MPC（约100倍于仅需分布式密钥生成的方案），虽然后者可提前运行，但实际部署时仍需优化MPC具体实现。当前构造假设可信经销商，委员会需用MPC模拟，文献中仅给出了协议轮廓而未提供完整实现。NIZK的验证开销占部分解密主导（>99%），如何设计可批量验证的零知识证明以降低计算开销是未来方向。此外，协议只能容忍少于n/3恶意委员会成员（使用承诺和纠错可提升至n/2但增加开销），实际系统需要权衡安全性、效率和激励机制的综合设计。

### 强关联论文  

[5] Bebel et al. Ferveo: Threshold decryption for mempool privacy in BFT networks. **ePrint 2022** [Google Scholar](https://scholar.google.com/scholar?q=Ferveo+Threshold+decryption+for+mempool+privacy+in+BFT+networks)

[24] Döttling et al. McFly: Verifiable encryption to the future made practical. **ePrint 2022** [Google Scholar](https://scholar.google.com/scholar?q=McFly+Verifiable+encryption+to+the+future+made+practical)

[58] Shutter Network contributors. The shutter network. **online 2021** [Google Scholar](https://scholar.google.com/scholar?q=The+shutter+network)

[13] Canetti et al. An efficient threshold public key cryptosystem secure against adaptive chosen ciphertext attack. **EUROCRYPT 1999** [Google Scholar](https://scholar.google.com/scholar?q=An+efficient+threshold+public+key+cryptosystem+secure+against+adaptive+chosen+ciphertext+attack)

[39] Kate et al. Constant-size commitments to polynomials and their applications. **ASIACRYPT 2010** [Google Scholar](https://scholar.google.com/scholar?q=Constant-size+commitments+to+polynomials+and+their+applications)

[11] Boneh et al. Identity-based encryption from the Weil pairing. **CRYPTO 2001** [Google Scholar](https://scholar.google.com/scholar?q=Identity-based+encryption+from+the+Weil+pairing)


## 关键词

+ 批量阈值加密内存池隐私
+ DeFi交易隐私保护
+ 阈值加密效率优化
+ 抗抢先交易协议
+ 区块链交易内存池隐私
+ 委员会解密通信复杂度
