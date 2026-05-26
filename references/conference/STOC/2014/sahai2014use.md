---
title: "How to use indistinguishability obfuscation: deniable encryption, and more"
标题简称:
论文类型: conference
会议简称: STOC
发表年份: 2014
created: 2025-04-29 10:26:41
modified: 2025-04-29 10:27:09
---

## How to use indistinguishability obfuscation: deniable encryption, and more

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/2591796.2591825)

## 作者

+ [Amit Sahai](Amit%20Sahai.md)
+ [Brent Waters](Brent%20Waters.md)
## 笔记

### 背景与动机
程序混淆旨在使程序变得“不可理解”的同时保持功能。Barak 等人于 2001 年提出了虚拟黑盒混淆和不可区分混淆两种概念，并证明前者对通用程序是不可能的，而后者虽可构造却缺乏明确的应用价值。Garg 等人于 2013 年给出了第一个高效的不可区分混淆候选方案，并展示了其在功能加密中的应用，但诸多基本问题仍未解决，例如能否用不可区分混淆将自然私钥加密方案转化为公钥加密方案。此外，Canetti 等人于 1997 年提出的可否认加密问题一直悬而未决：发送者在被胁迫公开消息和加密随机数后应能提供令人信服的假随机数来解释任意替代消息，且无需事先规划。现有可否认加密方案均只能达到可忽略但非可忽略的区分优势，且高调声称的解决方案随后被证伪。本文旨在引入“穿刺程序”技术，系统研究不可区分混淆在多种密码目标中的应用，并首次给出无需发送者事先规划的可否认加密构造。

### 相关工作

[1] Barak 等. On the (im)possibility of obfuscating programs. **CRYPTO 2001** [Google Scholar](https://scholar.google.com/scholar?q=On+the+impossibility+of+obfuscating+programs)
> 核心思路：提出了虚拟黑盒混淆和不可区分混淆两种定义，并证明了虚拟黑盒混淆对一般程序是不可能的。
> 局限与区别：虚拟黑盒混淆无法实现，而不可区分混淆的应用前景在当时不明确。本文在此基础上开发了穿刺程序技术，发掘了不可区分混淆的广泛可用性。

[2] Barak 等. On the (im)possibility of obfuscating programs. **J. ACM 2012** [Google Scholar](https://scholar.google.com/scholar?q=On+the+impossibility+of+obfuscating+programs+JACM)
> 核心思路：与[1]相同，是期刊版本。
> 局限与区别：同[1]。

[3] Boneh 和 Waters. Constrained pseudorandom functions and their applications. **ePrint 2013** [Google Scholar](https://scholar.google.com/scholar?q=Constrained+pseudorandom+functions+and+their+applications)
> 核心思路：定义了约束伪随机函数（包括穿刺PRF），并基于GGM构造给出实现。
> 局限与区别：该工作独立发现了穿刺PRF的构造，但未将其与不可区分混淆结合。本文利用穿刺PRF作为穿刺程序技术的核心组件。

[4] Boyle 等. Functional signatures and pseudorandom functions. **ePrint 2013** [Google Scholar](https://scholar.google.com/scholar?q=Functional+signatures+and+pseudorandom+functions)
> 核心思路：提出功能签名并独立构造了穿刺PRF。
> 局限与区别：同[3]。

[8] Canetti 等. Deniable encryption. **CRYPTO 1997** [Google Scholar](https://scholar.google.com/scholar?q=Deniable+encryption)
> 核心思路：提出了可否认加密的概念和开放问题，给出了一个交互式方案但具有可忽略的区分优势。
> 局限与区别：该方案存在1/n的区分优势，且所有后续方案均被证明有缺陷。本文首次给出非交互且无区分优势的构造。

[10] Dürmuth 和 Freeman. Deniable encryption with negligible detection probability: An interactive construction. **EUROCRYPT 2011** [Google Scholar](https://scholar.google.com/scholar?q=Deniable+encryption+with+negligible+detection+probability)
> 核心思路：声称构造了检测概率可忽略的可否认加密，但随后被证明有误。
> 局限与区别：本文指出该方案已被证伪，并给出了正确的构造。

[12] Garg 等. Candidate indistinguishability obfuscation and functional encryption for all circuits. **FOCS 2013** [Google Scholar](https://scholar.google.com/scholar?q=Candidate+indistinguishability+obfuscation+and+functional+encryption+for+all+circuits)
> 核心思路：提出了首个通用的不可区分混淆候选方案，并用于构造功能加密。
> 局限与区别：该工作未解决可否认加密等其他基本原语。本文以其为基础，开发穿刺程序技术并扩展应用。

[17] Goldreich 等. How to construct random functions (extended abstract). **FOCS 1984** [Google Scholar](https://scholar.google.com/scholar?q=How+to+construct+random+functions)
> 核心思路：基于任意伪随机生成器构造伪随机函数（GGM构造）。
> 局限与区别：GGM构造天然支持穿刺，这是本文穿刺PRF的基础。

[20] Kiayias 等. Delegatable pseudorandom functions and applications. **ePrint 2013** [Google Scholar](https://scholar.google.com/scholar?q=Delegatable+pseudorandom+functions+and+applications)
> 核心思路：独立提出穿刺PRF概念并给出构造。
> 局限与区别：同[3]。

[21] Moran 和 Rosen. There is no indistinguishability obfuscation in pessiland. **ePrint 2013** [Google Scholar](https://scholar.google.com/scholar?q=There+is+no+indistinguishability+obfuscation+in+pessiland)
> 核心思路：证明了若NP≠co-RP，则不可区分混淆蕴含单向函数存在。
> 局限与区别：本文引用了该结果说明额外假设的必要性。

### 核心技术与方案

本文提出了“穿刺程序”技术，其核心思想是对待混淆的程序进行“外科手术式”的修改——移除一个关键元素，使得修改后的程序与原始程序功能相同，从而可以用不可区分混淆（iO）来替换。结合伪随机生成器（PRG）和穿刺伪随机函数（PRF），该技术得以实现。

首先，以公钥加密构造为例说明。经典私钥加密方案中，密钥K是一个PRF密钥，加密消息m时选取随机r，输出(r, PRF(K, r)⊕m)。若将加密函数本身用iO混淆作为公钥，则面临攻击：挑战密文(r*, e*)中，敌手可直接查询混淆程序得到PRF(K, r*)。为此，引入PRG将r映射到更长的串t=PRG(r)，然后令密文为(t, PRF(K, t)⊕m)。由于PRG的像稀疏，挑战密文中的t*几乎肯定不在PRG像中，因此原始加密函数永远不会在t*上调用PRF。于是可以构造一个“穿刺”版本的加密函数，其中PRF密钥被穿刺掉t*点，两个函数功能等价，iO保证不可区分。而敌手没有关于PRF(K, t*)的信息，从而安全性由PRF伪随机性保证。

对于可否认加密，构造更为复杂。公钥包含两个混淆程序：Encrypt和Explain。Encrypt接收消息m和随机数u=(u[1],u[2])，先检查u是否是一个“隐藏稀疏触发器”——即是否存在(m',c',r')使得u[1]=F₂(K₂,(m',c',PRG(r')))且F₃(K₃,u[1])⊕u[2]=(m',c',PRG(r'))。若触发，则输出c'；否则正常加密：用F₁(K₁,(m,u))作为随机数调用底层公钥加密EPKE。Explain算法对任意(c,m)输出编码e=(α,β)，其中α=F₂(K₂,(m,c,PRG(r)))，β=F₃(K₃,α)⊕(m,c,PRG(r))。正确性要求触发集极其稀疏，因此均匀随机u几乎总是正常加密。

安全性证明依赖于穿刺程序技术的多次应用：首先将Explain中PRG(r*)替换为真随机值r̃，从而可穿刺F₂的输入点(m*,c*,r̃)，再逐步将α*和β*替换为随机值。同时Encrypt程序需保持Encrypt(m*; u*)=Encrypt(m*; e*)=c*不变，利用F₂的注入性和F₃的穿刺特性实现功能等价。

系统复杂度：加密时调用一次iO混淆的程序（包含PRF和PRG），密文长度约500-600位（若采用128位AES PRG和GGM构造）。解密只需计算一次PRF。公钥大小为混淆电路大小（与安全参数多项式相关）。本文还构造了短签名、CCA安全加密、NIZK、陷门函数、不经意传输等原语，均依赖i.O和单向函数，通信和计算复杂度各具特色。

### 核心公式与流程

**[公钥加密方案 Setup]**
$$ \text{PK} = i\mathcal{O}(\text{PKE\_Encrypt}), \quad \text{SK} = K $$
> 作用：公钥为加密程序的混淆，私钥为PRF密钥。

**[公钥加密方案 Encrypt]**
$$ c = (t = \text{PRG}(r),\; F(K, t) \oplus m) $$
> 作用：加密消息m，输出短密文（第一分量是PRG输出，第二分量是PRF掩码异或）。

**[可否认加密 Encrypt 程序中的隐藏触发器检查]**
$$ \text{if } F_3(K_3, u[1]) \oplus u[2] = (m', c', r') \text{ and } u[1] = F_2(K_2, (m', c', \text{PRG}(r'))): \text{ output } c' $$
> 作用：检测随机数u是否为编码过的触发器，若是则直接输出内置密文。

**[可否认加密 Explain 程序]**
$$ \alpha = F_2(K_2, (m, c, \text{PRG}(r))),\quad \beta = F_3(K_3, \alpha) \oplus (m, c, \text{PRG}(r)),\quad e = (\alpha, \beta) $$
> 作用：为任意密文c和消息m生成假随机数e，该e是隐藏触发器。

**[可否认加密公钥组成]**
$$ \text{PK} = (i\mathcal{O}(\text{Encrypt}),\; i\mathcal{O}(\text{Explain})) $$
> 作用：公钥包含加密和解释两个混淆程序。

### 实验结果
本文为理论密码学工作，未提供实验评估。所有构造均以安全参数λ的多项式时间内完成，具体性能取决于底层原语（如PRF、PRG、iO实例化）。在假设存在有效iO候选（如[12]）和标准单向函数的前提下，方案在渐进意义下可行。可否认加密的密文长度和公共参数大小与安全参数呈多项式关系，解密只需常数次PRF计算。公钥加密的密文长度可短至300比特左右（基于128位AES和GGM PRF），远优于通过witness encryption间接构造的方案。

### 局限性与开放问题
本文的所有构造均依赖不可区分混淆候选方案的安全性，而该候选基于非标准代数假设，尚需进一步分析或归约到更标准的假设。此外，可否认加密方案中Encrypt程序需要检查隐藏触发器，导致加密时间相对较长；如何优化加密效率是尚待解决的问题。另外，本文的签名方案仅满足选择性安全（选择性伪造），能否提升到自适应安全而不显著增加复杂度仍未解决。

### 强关联论文

[1] Barak 等. On the (im)possibility of obfuscating programs. **CRYPTO 2001** [Google Scholar](https://scholar.google.com/scholar?q=On+the+impossibility+of+obfuscating+programs)

[2] Barak 等. On the (im)possibility of obfuscating programs. **J. ACM 2012** [Google Scholar](https://scholar.google.com/scholar?q=On+the+impossibility+of+obfuscating+programs+JACM)

[3] Boneh 和 Waters. Constrained pseudorandom functions and their applications. **ePrint 2013** [Google Scholar](https://scholar.google.com/scholar?q=Constrained+pseudorandom+functions+and+their+applications)

[4] Boyle 等. Functional signatures and pseudorandom functions. **ePrint 2013** [Google Scholar](https://scholar.google.com/scholar?q=Functional+signatures+and+pseudorandom+functions)

[8] Canetti 等. Deniable encryption. **CRYPTO 1997** [Google Scholar](https://scholar.google.com/scholar?q=Deniable+encryption)

[10] Dürmuth 和 Freeman. Deniable encryption with negligible detection probability: An interactive construction. **EUROCRYPT 2011** [Google Scholar](https://scholar.google.com/scholar?q=Deniable+encryption+with+negligible+detection+probability)

[12] Garg 等. Candidate indistinguishability obfuscation and functional encryption for all circuits. **FOCS 2013** [Google Scholar](https://scholar.google.com/scholar?q=Candidate+indistinguishability+obfuscation+and+functional+encryption+for+all+circuits)

[17] Goldreich 等. How to construct random functions (extended abstract). **FOCS 1984** [Google Scholar](https://scholar.google.com/scholar?q=How+to+construct+random+functions)

[20] Kiayias 等. Delegatable pseudorandom functions and applications. **ePrint 2013** [Google Scholar](https://scholar.google.com/scholar?q=Delegatable+pseudorandom+functions+and+applications)

[21] Moran 和 Rosen. There is no indistinguishability obfuscation in pessiland. **ePrint 2013** [Google Scholar](https://scholar.google.com/scholar?q=There+is+no+indistinguishability+obfuscation+in+pessiland)


## 关键词

+ 不可区分性混淆iO
+ 打孔程序技术
+ 可否认加密
+ 非交互式零知识证明NIZK
+ 核心密码学原语构建
+ 单向函数密码应用

