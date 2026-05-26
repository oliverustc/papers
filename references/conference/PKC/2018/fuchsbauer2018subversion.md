---
title: "Subversion-zero-knowledge SNARKs"
标题简称:
论文类型: conference
会议简称: PKC
发表年份: 2018
modified: 2025-04-08 17:22:54
---

## Subversion-zero-knowledge SNARKs

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-319-76578-5_11)

## 作者

+ [Georg Fuchsbauer](Georg%20Fuchsbauer.md)
## 笔记

### 背景与动机
零知识证明系统需要可信设置来生成公共参考串（CRS），但参数一旦被恶意篡改，不仅可靠性可能被破坏，零知识性也会受到威胁。在Zcash的匿名交易和比特币上的零知识条件支付（ZKCP）中，SNARK被广泛使用，而ZKCP的买家可以恶意生成CRS从而窃取卖家的秘密信息，这正是Campanelli等人发现的攻击。现有方案要么需要复杂的多方计算来安全生成CRS，要么在参数被篡改时完全丧失隐私保障。本文试图回答一个关键问题：在CRS由对手任意生成的情况下，能否仍然保证零知识性？作者基于平方知识指数（SKE）假设，证明五个主流SNARK方案（包括Zcash底层方案）在经过简单的CRS可验证性检查后，即可满足子版本零知识（S-ZK），并且其中四个方案无需修改CRS结构，仅Pinocchio需增加4个群元素。

### 相关工作

[GGPR13] Gennaro等. Quadratic Span Programs and Succinct NIZKs without PCPs. **EUROCRYPT 2013** [Google Scholar](https://scholar.google.com/scholar?q=Quadratic+Span+Programs+and+Succinct+NIZKs+without+PCPs)
> 核心思路：提出QSP/QAP概念，并构造了第一个基于配对的高效SNARK，证明由8个群元素组成。
> 局限与区别：仅假设CRS可信，未考虑参数被恶意篡改的情况。本文证明其QSP和QAP版本均满足S-ZK。

[BCTV14] Ben-Sasson等. Succinct Non-Interactive Zero Knowledge for a von Neumann Architecture. **USENIX Security 2014** [Google Scholar](https://scholar.google.com/scholar?q=Succinct+Non-Interactive+Zero+Knowledge+for+a+von+Neumann+Architecture)
> 核心思路：优化Pinocchio到非对称群，简化解密密钥，实现于libsnark，用于Zcash。
> 局限与区别：原方案在参数被篡改时不是S-ZK（如Campanelli攻击）。本文通过添加4个群元素使其可验证，并证明S-ZK。

[DFGK14] Danezis等. Square Span Programs with Applications to Succinct NIZK Arguments. **ASIACRYPT 2014** [Google Scholar](https://scholar.google.com/scholar?q=Square+Span+Programs+with+Applications+to+Succinct+NIZK+Arguments)
> 核心思路：提出平方跨度程序（SSP），将证明大小降至4个群元素。
> 局限与区别：其CRS已可直接用双线性映射验证。本文证明其S-ZK（与Pinocchio类似）。

[Gro16] Groth. On the Size of Pairing-Based Non-Interactive Arguments. **EUROCRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=On+the+Size+of+Pairing-Based+Non-Interactive+Arguments)
> 核心思路：将SNARK证明大小降至3个群元素，验证仅需3对双线性对，是目前最优方案。
> 局限与区别：证明模拟需要α,β，而SKE只能提取τ和δ。本文通过巧妙构造仅用τ和δ即可模拟证明，证明其S-ZK。

[BFS16] Bellare等. NIZKs with an Untrusted CRS: Security in the Face of Parameter Subversion. **ASIACRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=NIZKs+with+an+Untrusted+CRS%3A+Security+in+the+Face+of+Parameter+Subversion)
> 核心思路：正式定义S-SND、S-WI、S-ZK，并基于DH-KEA构造了一个S-ZK的NIZK方案。
> 局限与区别：他们的方案需要固定群生成器且效率较低。本文将其框架应用于实际SNARK，并引入更弱的SKE假设。

[CGGN17] Campanelli等. Zero-Knowledge Contingent Payments Revisited: Attacks and Services. **ACM CCS 2017** [Google Scholar](https://scholar.google.com/scholar?q=Zero-Knowledge+Contingent+Payments+Revisited%3A+Attacks+and+Services)
> 核心思路：发现libsnark中Pinocchio实现的S-ZK攻击，并建议使用GGPR方案。
> 局限与区别：他们认为Pinocchio需要重大修改。本文证明仅需添加4个群元素即可恢复S-ZK。

[PHGR13] Parno等. Pinocchio: Nearly Practical Verifiable Computation. **IEEE S&P 2013** [Google Scholar](https://scholar.google.com/scholar?q=Pinocchio%3A+Nearly+Practical+Verifiable+Computation)
> 核心思路：改进GGPR的效率，实现Pinocchio方案。
> 局限与区别：不涉及子版本安全性。本文在其非对称版本上添加验证键。

[ABLZ17] Abdolmaleki等. A Subversion-Resistant SNARK. **ASIACRYPT 2017** [Google Scholar](https://scholar.google.com/scholar?q=A+Subversion-Resistant+SNARK)
> 核心思路：提出Groth方案的S-ZK变体，需要修改CRS（增加2d个元素），假设更强（要求输出(sP1,sP2)必须知道s）。
> 局限与区别：本文不需要修改Groth方案的原CRS结构（仅需验证），假设更弱（SKE在Type-3群中成立）。

### 核心技术与方案

本文的整体框架包括三个层次：首先定义平方知识指数（SKE）假设作为提取陷门的手段；然后为每个候选SNARK设计CRS可验证性程序，使得一个通过验证的CRS必然具有正确的代数结构（存在秘密值τ、ρ等）；最后证明在这些CRS下可以用提取出的τ（和/或δ）模拟出与真实证明分布不可区分的模拟证明，从而满足S-ZK。

**SKE假设**：在非对称群中，如果敌手输出$(S_0,S_1,S_2,T_0,T_1)$满足$e(S_1,T_0)=e(S_0,T_1)$且$e(S_1,T_1)=e(S_2,T_0)$，则存在提取器以压倒性概率从敌手随机带中提取出$s$使得$S_1=sS_0$，$S_2=s^2S_0$，$T_1=sT_0$。该假设在通用群模型下可证。

**核心构造思路**：
1. **CRS可验证性**：对于每个方案，定义一系列配对等式作为检查，确保CRS中各元素间的对数关系正确（如$pk_{H,i}=\tau^i P_1$可通过配对$e(pk_{H,i},P_2)=e(pk_{H,i-1},ck_H)$验证）。通过验证的CRS必然存在秘密值τ（以及α,β,γ,δ等）且非零。
2. **陷门提取**：利用SKE，从CRS中提取τ（以及Groth方案还需通过二次SKE提取δ）。提取基于CRS中成对出现的元素（如$(P_1,\tau P_1,\tau^2 P_1,P_2,\tau P_2)$）。
3. **模拟证明**：对每个方案，给出只用τ（或τ和δ）即可生成与真实证明分布相同的模拟证明。关键在于利用$Z(\tau)\neq 0$从CRS中派生模拟所需的秘密值（如$\rho_A P_1 = Z(\tau)^{-1}pk_{A,m+1}$）。对于Groth方案，模拟公式为：
   $$\pi_A := aP_1 + pk_\alpha,\quad \pi_B' := bP_2 + pk_\beta',$$
   $$\pi_C := \delta^{-1}\big(ab - C_0(\tau)-\sum x_iC_i(\tau)\big)P_1 + \delta^{-1}\big(b-B_0(\tau)-\sum x_iB_i(\tau)\big)pk_\alpha + \delta^{-1}\big(a-A_0(\tau)-\sum x_iA_i(\tau)\big)pk_\beta.$$
4. **安全性证明**：以事件E表示CRS通过验证但提取器失败。由SKE，E的概率可忽略。在E不发生时，真实证明的随机元素（如$r\delta P_1$）与模拟证明的随机元素（如$aP_1$）均均匀分布，且验证等式唯一确定其余元素，因此分布完全一致。

**复杂度分析**：各方案证明大小不变（Pinocchio 8元素，Groth 3元素），验证计算量仅增加常数次配对（用于CRS验证）。CRS验证的一次性开销对每个方案是$O(m+d)$次配对，其中$m$是电路门数，$d$是QAP度数。

### 核心公式与流程

**[SKE假设（非对称群）]**
$$
\mathsf{SKE}_{\mathsf{aGen}}: \quad \text{Game returns true if } e(S_1,T_0)=e(S_0,T_1) \ \wedge\ e(S_1,T_1)=e(S_2,T_0) \ \wedge\ sS_0\neq S_1.
$$
> 作用：允许从形如$(S_0,S_1,S_2,T_0,T_1)$的五元组中提取秘密值$s$，用于CRS中$\tau$和$\delta$的提取。

**[Pinocchio CRS验证中的配对检查]**
$$
e(pk_{H,i},P_2)=e(pk_{H,i-1},ck_H),\quad e(pk_{A,i},P_2)=e\big(\sum_{j=0}^{d-1}a_{i,j}pk_{H,j},ck_A\big),\quad \text{等}.
$$
> 作用：验证$pk_H$与$\tau$的关系、$pk_A$与$\tau$和$\rho_A$的关系。

**[Pinocchio模拟证明公式]**
$$
\pi_A := a\cdot sk_A - vk_x,\quad \pi_B := b\cdot sk_B,\quad \pi_C := c\cdot sk_C,\quad \pi_H := Z(\tau)^{-1}(ab-c)P_1,
$$
其中$sk_A = Z(\tau)^{-1}pk_{A,m+1}=\rho_AP_1$，等等。
> 作用：用提取的$\tau$和从CRS导出的$sk$，构造与真实证明不可区分的模拟证明。

**[Groth模拟证明公式]**
$$
\pi_A := aP_1 + pk_\alpha,\quad \pi_B' := bP_2 + pk_\beta',
$$
$$
\pi_C := \delta^{-1}\big(ab - C_0(\tau)-\sum x_iC_i(\tau)\big)P_1 + \delta^{-1}\big(b - B_0(\tau)-\sum x_iB_i(\tau)\big)pk_\alpha + \delta^{-1}\big(a - A_0(\tau)-\sum x_iA_i(\tau)\big)pk_\beta.
$$
> 作用：仅用$\tau$和$\delta$即可模拟证明，无需$\alpha,\beta$信息。

### 实验结果

本文为理论性论文，不包含实验数据。所有结果均以定理形式陈述：对于每个候选SNARK，在SKE假设下，证明其满足S-ZK。其中Pinocchio方案需额外添加4个群元素（ck）并执行CRS验证，其余方案仅需执行CRS验证。定理证明基于通用群模型中的SKE可证性以及对各方案模拟算法的完备性验证。实际性能方面，CRS验证的额外计算量为$O(m+d)$次配对，对于典型电路规模（如Zcash中约10k门），完全可行且一次验证后即可反复使用。Zcash的参数已经通过多方协议生成，本文论证了即使所有参与方合谋，在ROM和SKE假设下Zcash仍提供子版本匿名性。

### 局限性与开放问题

本文依赖SKE这个知识假设，虽然已在通用群模型中可证，但在实际群中仍是非标准强假设；对Type-2（存在从$\mathbb{G}_2$到$\mathbb{G}_1$的有效同态）的非对称群，SKE可能不成立。本文未考虑如何防范更隐蔽的CRS篡改，例如在验证元素中嵌入隐信道。此外，CRS验证虽为一次性操作，但对于极大规模电路（如百万门）其配对数量仍可能成为瓶颈。未来工作包括在标准假设（如DLIN）下构造S-ZK的SNARK，或设计无需CRS验证的隐性安全方案。

### 强关联论文

[GGPR13] Gennaro等. Quadratic Span Programs and Succinct NIZKs without PCPs. **EUROCRYPT 2013** [Google Scholar](https://scholar.google.com/scholar?q=Quadratic+Span+Programs+and+Succinct+NIZKs+without+PCPs)

[BCTV14] Ben-Sasson等. Succinct Non-Interactive Zero Knowledge for a von Neumann Architecture. **USENIX Security 2014** [Google Scholar](https://scholar.google.com/scholar?q=Succinct+Non-Interactive+Zero+Knowledge+for+a+von+Neumann+Architecture)

[DFGK14] Danezis等. Square Span Programs with Applications to Succinct NIZK Arguments. **ASIACRYPT 2014** [Google Scholar](https://scholar.google.com/scholar?q=Square+Span+Programs+with+Applications+to+Succinct+NIZK+Arguments)

[Gro16] Groth. On the Size of Pairing-Based Non-Interactive Arguments. **EUROCRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=On+the+Size+of+Pairing-Based+Non-Interactive+Arguments)

[BFS16] Bellare等. NIZKs with an Untrusted CRS: Security in the Face of Parameter Subversion. **ASIACRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=NIZKs+with+an+Untrusted+CRS%3A+Security+in+the+Face+of+Parameter+Subversion)

[CGGN17] Campanelli等. Zero-Knowledge Contingent Payments Revisited: Attacks and Services. **ACM CCS 2017** [Google Scholar](https://scholar.google.com/scholar?q=Zero-Knowledge+Contingent+Payments+Revisited%3A+Attacks+and+Services)

[PHGR13] Parno等. Pinocchio: Nearly Practical Verifiable Computation. **IEEE S&P 2013** [Google Scholar](https://scholar.google.com/scholar?q=Pinocchio%3A+Nearly+Practical+Verifiable+Computation)

[ABLZ17] Abdolmaleki等. A Subversion-Resistant SNARK. **ASIACRYPT 2017** [Google Scholar](https://scholar.google.com/scholar?q=A+Subversion-Resistant+SNARK)


## 关键词

+ 子版本零知识
+ SNARK安全性
+ 公共参考字符串
+ 恶意设置安全性
+ Zcash匿名性
+ 有条件零知识支付