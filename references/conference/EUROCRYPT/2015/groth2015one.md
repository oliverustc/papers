---
title: "One-out-of-many proofs: Or how to leak a secret and spend a coin"
doi: 10.1007/978-3-662-46803-6_9
标题简称:
论文类型: conference
会议简称: EUROCRYPT
发表年份: 2015
created: 2025-05-12 08:48:43
modified: 2025-05-12 08:57:09
---
## One-out-of-many proofs: Or how to leak a secret and spend a coin

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-662-46803-6_9)

## 作者

+ [Jens Groth](Jens%20Groth.md)
+ [Markulf Kohlweiss](Markulf%20Kohlweiss.md)

## 笔记

### 背景与动机
基于离散对数假设的密码方案在匿名通信和隐私保护领域应用广泛，环签名和Zerocoin是两个代表性应用。环签名允许签名者在不泄露身份的情况下代表一个群体签署消息，Zerocoin则使用户能以匿名方式花费数字货币。然而，现有方案存在显著瓶颈：基于一般性方法的Σ-协议在处理“一个集合中存在一个有效成员”这类合取语句时，通信复杂度与群体规模N呈线性关系 [CDS94]；基于RSA累加器的环签名 [DKNS04] 和Zerocoin方案 [MGGR13] 依赖强RSA假设或可信设置，且签名大小在安全参数上呈立方或五次方增长。本文旨在填补这一空白，构造一个仅依赖同态承诺方案（如Pedersen承诺）的、通信复杂度为对数级别（O(log N)）的Σ-协议，并由此导出高效且弱假设的环签名和无可信设置的Zerocoin方案。

### 相关工作

[AOS04] Abe et al. 1-out-of-n signatures from a variety of keys. **IEICE 2004** [Google Scholar](https://scholar.google.com/scholar?q=1-out-of-n+signatures+from+a+variety+of+keys)
> 核心思路：利用合取证明技术构造环签名，签名大小与群体大小N成线性关系。
> 局限与区别：其通信复杂度为O(N)，不适用于大规模群体。

[BG13] Bayer et al. Zero-Knowledge Argument for Polynomial Evaluation with Application to Blacklists. **EUROCRYPT 2013** [Google Scholar](https://scholar.google.com/scholar?q=Zero-Knowledge+Argument+for+Polynomial+Evaluation+with+Application+to+Blacklists)
> 核心思路：构造对数大小的成员证明，证明承诺值属于一个公开列表，计算复杂度为O(N log² N)。
> 局限与区别：其计算复杂度高于本文的O(N log N)，且本文的构造思路是基于超立方体的权重乘积，与基于多项式求值的思路不同。

[CDS94] Cramer et al. Proof of Partial Knowledge and Simplified Design of Witness Hiding Protocols. **CRYPTO 1994** [Google Scholar](https://scholar.google.com/scholar?q=Proof+of+Partial+Knowledge+and+Simplified+Design+of+Witness+Hiding+Protocols)
> 核心思路：提出构造合取Σ-协议的一般性方法，通信复杂度与子语句数量成线性关系。
> 局限与区别：本文的目标语言是“N个承诺中存在一个对0的承诺”，若直接应用该一般方法，通信量将为O(N)，本文则实现了O(log N)。

[CL02] Camenisch et al. Dynamic Accumulators and Application to Efficient Revocation of Anonymous Credentials. **CRYPTO 2002** [Google Scholar](https://scholar.google.com/scholar?q=Dynamic+Accumulators+and+Application+to+Efficient+Revocation+of+Anonymous+Credentials)
> 核心思路：提出基于强RSA假设的累加器，支持动态成员管理。
> 局限与区别：该工具被用于构造常数大小的环签名 [DKNS04]，但依赖强RSA假设且RSA模数导致签名大小随安全参数立方增长。

[DKNS04] Dodis et al. Anonymous Identification in Ad Hoc Groups. **EUROCRYPT 2004** [Google Scholar](https://scholar.google.com/scholar?q=Anonymous+Identification+in+Ad+Hoc+Groups)
> 核心思路：利用累加器构造常数大小的环签名，签名大小与群体大小无关。
> 局限与区别：需要强RSA假设和RSA模数的可信设置，且签名大小在安全参数上为O(λ³)，而本文为O(λ log λ)。 （注意：原文指出大小与λ³成正比，但定量比较请以原文为准）

[MGGR13] Miers et al. Zerocoin: Anonymous distributed e-cash from bitcoin. **IEEE S&P 2013** [Google Scholar](https://scholar.google.com/scholar?q=Zerocoin%3A+Anonymous+distributed+e-cash+from+bitcoin)
> 核心思路：提出第一个Zerocoin方案，利用RSA累加器和cut-and-choose技术。
> 局限与区别：花费证明的大小在安全参数上呈五次方增长，且需要可信的设置或复杂的技术（如RSA UFOs）来生成公共参数。

[Ngu05] Nguyen. Accumulators from Bilinear Pairings and Applications. **CT-RSA 2005** [Google Scholar](https://scholar.google.com/scholar?q=Accumulators+from+Bilinear+Pairings+and+Applications)
> 核心思路：构造基于双线性对的累加器，并用于常数大小的环签名。
> 局限与区别：依赖双线性对假设，且公钥大小随群体线性增长，签名大小在安全参数上为O(λ³)，不如本文的渐进复杂度。

### 核心技术与方案

本文的核心是构造一个针对“已知N个承诺，存在其中一个承诺是对0的承诺”这一语言的Σ-协议，其通信复杂度为对数级别（O(log N)）。协议基于任意加法同态承诺方案，例如Pedersen承诺。设N=2^n，将承诺索引ℓ和所有i∈{0,...,N-1}表示为二进制串。核心思想是将判断是否存在一个索引ℓ使得c_ℓ是对0的承诺，等价于证明∏_{i=0}^{N-1} c_i^{δ_{iℓ}}是对0的承诺，其中δ_{iℓ}是克罗内克δ函数。通过将δ_{iℓ}分解为位乘积δ_{iℓ}=∏_{j=1}^n δ_{i_j ℓ_j}，协议将问题转化为一个关于随机挑战x的n次多项式的零知识证明。

协议流程如下：证明者首先对ℓ的各个比特位ℓ_j进行承诺，并执行n个并行的Σ-协议（如第2.3节给出的0/1承诺协议）以证明这些承诺包含比特0或1。在这些子协议中，证明者会揭示形如f_j = ℓ_j x + a_j的值。定义f_{j,1}=f_j和f_{j,0}=x-f_j，则对于任意索引i，其对应的多项式为p_i(x)=∏_{j=1}^n f_{j,i_j}=δ_{iℓ}x^n + ∑_{k=0}^{n-1} p_{i,k}x^k。关键观察是，对于i≠ℓ，p_i(x)是次数至多为n-1的多项式；只有当i=ℓ时，p_ℓ(x)是一个首一n次多项式。

证明者在初始消息中额外发送n个辅助承诺c_{d_0},...,c_{d_{n-1}}，设计用于抵消验证等式中次数低于n的低次项。具体地，证明者计算这些c_{d_k}为c_{d_k}=∏_i c_i^{p_{i,k}}·Com_{ck}(0;ρ_k)。收到挑战x后，证明者返回f_1,...,f_n以及用于打开子协议的随机数，并计算一个全局的响应z_d = r x^n - ∑_{k=0}^{n-1} ρ_k x^k。最终验证者检查两个条件：(1) 对于每个j，验证子协议的正确性，即c_{ℓ_j}^x·c_{a_j}=Com_{ck}(f_j;z_{a_j})和c_{ℓ_j}^{x-f_j}·c_{b_j}=Com_{ck}(0;z_{b_j})；(2) 验证整体等式 ∏_i c_i^{∏_j f_{j,i_j}}·∏_{k=0}^{n-1} c_{d_k}^{-x^k}=Com_{ck}(0;z_d)。该验证等式成立的核心在于，由于c_ℓ是对0的承诺，c_ℓ^{x^n}项贡献为0；而c_{d_k}承诺的设计恰好抵消了所有i≠ℓ项中的低次系数，使得整个等式仅在c_ℓ是对0的承诺时成立。

安全性方面，协议满足完美完备性、准唯一响应以及完美特殊诚实验证者零知识。其特殊可靠性为(n+1)-特殊可靠：给定n+1个关于不同挑战的接受证据，可以通过解范德蒙德矩阵提取出对某个承诺c_ℓ的一个有效打开(0, r)。这依赖于承诺方案的（计算）绑定性质。零知识性则依赖于承诺方案的（完美）隐藏性质。当证明者知道所有承诺的打开方式时，其计算量可以优化到约3N log N次Z_q乘法加4 log N个承诺生成。作为成员证明应用，给定一个承诺c和一个列表{λ_0,...,λ_{N-1}}，可通过设置c_i = c·Com_{ck}(-λ_i;0)并证明一个c_i是0的承诺来实现，此时证明者的复杂度降至2N log N次乘法。

### 核心公式与流程

**[关键身份多项式]**
$$p_i(x) = \prod_{j=1}^{n} f_{j,i_j} = \delta_{i\ell}x^n + \sum_{k=0}^{n-1} p_{i,k}x^k$$
> 作用：将“索引ℓ的承诺是对0的承诺”这一陈述编码成一个关于挑战x的多项式。对于目标索引ℓ，该多项式是首一的n次多项式；对于其他索引i≠ℓ，多项式次数至多为n-1。这一结构是整个对数复杂度协议的核心。

**[最终验证等式]**
$$\prod_{i=0}^{N-1} c_i^{\prod_{j=1}^n f_{j,i_j}} \cdot \prod_{k=0}^{n-1} c_{d_k}^{-x^k} = \mathrm{Com}_{ck}(0; z_d)$$
> 作用：该式是验证者检查的核心。利用c_i的承诺值（已知某c_ℓ为0）和预先计算的c_{d_k}（用来抵消低次项），该式在证明者诚实的情况下成立。安全性上，由于c_i对于i≠ℓ贡献的p_i(x)次数<n，可以被c_{d_k}项精确抵消，而c_ℓ项贡献为0·x^n = 0，因此整体为0。

### 实验结果
论文本身为理论构造，未提供实验数据或实现性能评测。其效率讨论集中在渐进复杂度和理论开销。对于环签名，签名大小包括4 log N个群元素（同态承诺）和3 log N +1个Z_q域元素，共O(λ log N)比特，其中λ为群元素大小。证明者计算量为O(N log N)次群指数运算（通过多指数技术优化），验证者计算量为O(N)次群指数运算。与基于RSA累加器的方案（签名大小O(λ³)、依赖强假设）相比，本文在安全假设（仅离散对数）和签名大小方面有显著优势。与基于SNARK的Zerocoin方案相比，后者虽然常数大小但依赖知识假设。本文的方案在安全性和渐进效率之间取得了良好平衡，尤其适用于群体大小N为安全参数多项式规模的应用场景。

### 局限性与开放问题
本文构造的一个局限是，与Bayer和Groth的成员证明 [BG13] 相比，未能自然地导出非成员证明。此外，虽然协议支持对任意同态承诺方案的泛化，但证明者在不知道所有承诺打开方式时的计算量（O(N log N)次指数运算）可能在高基数N下成为瓶颈，而协议主要针对N为多项式规模的设计，对于超大规模列表可能需要进一步优化。另一个开放问题是探索该协议与更复杂证明系统的结合，例如将其用于构造更高效的匿名凭证或可追踪签名方案。

### 强关联论文

[AOS04] Abe et al. 1-out-of-n signatures from a variety of keys. **IEICE 2004** [Google Scholar](https://scholar.google.com/scholar?q=1-out-of-n+signatures+from+a+variety+of+keys)

[BG13] Bayer et al. Zero-Knowledge Argument for Polynomial Evaluation with Application to Blacklists. **EUROCRYPT 2013** [Google Scholar](https://scholar.google.com/scholar?q=Zero-Knowledge+Argument+for+Polynomial+Evaluation+with+Application+to+Blacklists)

[CDS94] Cramer et al. Proof of Partial Knowledge and Simplified Design of Witness Hiding Protocols. **CRYPTO 1994** [Google Scholar](https://scholar.google.com/scholar?q=Proof+of+Partial+Knowledge+and+Simplified+Design+of+Witness+Hiding+Protocols)

[CGS07] Chandran et al. Ring Signatures of Sub-linear Size Without Random Oracles. **ICALP 2007** [Google Scholar](https://scholar.google.com/scholar?q=Ring+Signatures+of+Sub-linear+Size+Without+Random+Oracles)

[DKNS04] Dodis et al. Anonymous Identification in Ad Hoc Groups. **EUROCRYPT 2004** [Google Scholar](https://scholar.google.com/scholar?q=Anonymous+Identification+in+Ad+Hoc+Groups)

[MGGR13] Miers et al. Zerocoin: Anonymous distributed e-cash from bitcoin. **IEEE S&P 2013** [Google Scholar](https://scholar.google.com/scholar?q=Zerocoin%3A+Anonymous+distributed+e-cash+from+bitcoin)

[Ngu05] Nguyen. Accumulators from Bilinear Pairings and Applications. **CT-RSA 2005** [Google Scholar](https://scholar.google.com/scholar?q=Accumulators+from+Bilinear+Pairings+and+Applications)

[Ped91] Pedersen. Non-interactive and Information-Theoretic Secure Verifiable Secret Sharing. **CRYPTO 1991** [Google Scholar](https://scholar.google.com/scholar?q=Non-interactive+and+Information-Theoretic+Secure+Verifiable+Secret+Sharing)

[RST01] Rivest et al. How to Leak a Secret. **ASIACRYPT 2001** [Google Scholar](https://scholar.google.com/scholar?q=How+to+Leak+a+Secret)


## 关键词

+ 一取多证明
+ Sigma协议
+ 环签名
+ 零币
+ Pedersen承诺