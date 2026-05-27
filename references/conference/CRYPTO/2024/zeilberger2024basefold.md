---
title: "BaseFold: Efficient Field-Agnostic Polynomial Commitment Schemes from Foldable Codes"
doi: 10.1007/978-3-031-68403-6_5
标题简称: BaseFold
论文类型: conference
会议简称: CRYPTO
发表年份: 2024
modified: 2025-04-10 16:59:54
---
## BaseFold: Efficient Field-Agnostic Polynomial Commitment Schemes from Foldable Codes

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-68403-6_5)

## 作者

+ [Hadas Zeilberger](Hadas%20Zeilberger.md)
+ [Binyi Chen](Binyi%20Chen.md)

## 笔记

### 背景与动机
简洁的零知识证明系统（zkSNARKs）在区块链、隐私计算等领域至关重要，其核心组件之一是多项式承诺方案（PCS）。PCS允许证明者承诺一个多项式，并在后续证明某个点的取值正确。对于多线性多项式，现有的高效PCS面临一组难以兼得的权衡：基于FRI的PCS具有对数和准线性级的验证者和证明者复杂度，但并非域无关——当应用的目标域（如secp256k1的标量域）与SNARK的固有域不匹配时，需要引入昂贵的非本地域运算，导致电路规模膨胀一个数量级；而域无关的Brakedown PCS虽具有线性时间证明者，但验证者时间和证明大小均为平方根级，远不如FRI。ECFFT2虽然实现了域无关的FRI，但其在多项式承诺场景下的编码复杂度为O(n log^2 n)，效率不足。因此，一个兼具域无关性、线性或近线性时间证明者、以及对数级验证者时间和证明大小的多线性PCS是亟待解决的问题。本文旨在填补这一空白。

### 相关工作

[5] Ben-Sasson, E., Bentov, I., Horesh, Y., Riabzev, M. Fast Reed-Solomon Interactive Oracle Proofs of Proximity. **ICALP 2018** [Google Scholar](https://scholar.google.com/scholar?q=Fast+Reed-Solomon+Interactive+Oracle+Proofs+of+Proximity)
> 核心思路：提出了FRI IOPP，利用Reed-Solomon码的折叠性质实现对数级查询的临近性证明。
> 局限与区别：依赖FFT友好的域，并非域无关；其证明者复杂度O(n log n)低于BaseFold的线性时间证明者。

[26] Golovnev, A., Lee, J., Setty, S., Thaler, J., Wahby, R.S. Brakedown: Linear-time and post-quantum SNARKs for R1CS. **ePrint 2021** [Google Scholar](https://scholar.google.com/scholar?q=Brakedown+Linear-time+and+post-quantum+SNARKs+for+R1CS)
> 核心思路：基于张量码IOPP构造域无关的PCS，证明者和验证者均为线性时间。
> 局限与区别：证明大小和验证者时间为O(√n)，远大于BaseFold的对数级别。

[33] Kohrita, T., Towa, P. Zeromorph: Zero-knowledge multilinear-evaluation proofs from homomorphic univariate commitments. **ePrint 2023** [Google Scholar](https://scholar.google.com/scholar?q=Zeromorph+Zero-knowledge+multilinear-evaluation+proofs+from+homomorphic+univariate+commitments)
> 核心思路：将多线性求值证明转化为对单变量多项式的证明，并利用FRI作为底层IOPP，得到实用的多线性PCS。
> 局限与区别：依赖于FRI，因此不具有域无关性；其证明者复杂度为O(n log n)，BaseFold则为严格线性。

[12] Ben-Sasson, E., Kopparty, S., Saraf, S. Worst-case to average case reductions for the distance to a code. **CCC 2018** [Google Scholar](https://scholar.google.com/scholar?q=Worst-case+to+average+case+reductions+for+the+distance+to+a+code)
> 核心思路：提出ECFFT2技术，利用椭圆曲线上的FFT实现任意域上的近似编码，从而使得FRI可以用于任意大域。
> 局限与区别：在用于多线性PCS时，其编码复杂度为O(n log^2 n)，远慢于BaseFold的O(n log n)。

[20] Chen, B., Bünz, B., Boneh, D., Zhang, Z. HyperPlonk: plonk with linear-time prover and high-degree custom gates. **EUROCRYPT 2023** [Google Scholar](https://scholar.google.com/scholar?q=HyperPlonk+plonk+with+linear-time+prover+and+high-degree+custom+gates)
> 核心思路：使用多线性PIOP和PCS构造SNARK，支持高次自定义门，避免高频域FFT，实现线性时间证明者。
> 局限与区别：本文将其作为后端PIOP，致力于替代其原有的多线性PCS，以提升域无关性和整体效率。

[31] Kate, A., Zaverucha, G.M., Goldberg, I. Constant-size commitments to polynomials and their applications. **ASIACRYPT 2010** [Google Scholar](https://scholar.google.com/scholar?q=Constant-size+commitments+to+polynomials+and+their+applications)
> 核心思路：基于配对双线性群构造KZG承诺，实现常数大小的证明和验证时间。
> 局限与区别：需要可信设置，且限于配对友好域，不具有域无关性，且开销较大。

[38] Papamanthou, C., Shi, E., Tamassia, R. Signatures of correct computation. **TCC 2013** [Google Scholar](https://scholar.google.com/scholar?q=Signatures+of+correct+computation)
> 核心思路：将KZG扩展到多线性多项式。
> 局限与区别：继承了KZG的所有局限性（需要可信设置、非域无关、开销大）。

[16] Bordage, S., Lhotel, M., Nardi, J., Randriam, H. Interactive oracle proofs of proximity to algebraic geometry codes. **CCC 2022** [Google Scholar](https://scholar.google.com/scholar?q=Interactive+oracle+proofs+of+proximity+to+algebraic+geometry+codes)
> 核心思路：将FRI推广到代数几何码，实现域无关性。
> 局限与区别：其编码和验证复杂度仅在FFT友好域上为O(n log n)，在通用域上效率无法保证，不如BaseFold的随机折叠码。

### 核心技术与方案

**1. 折叠码与BaseFold IOPP**

本文的核心洞察是FRI IOPP的有效性源于Reed-Solomon码的一个性质——可折叠性。作者将这一性质抽象为“折叠线性码”的定义（Definition 5）。一个线性码C_d是折叠的，如果其生成矩阵G_d可以表示为递归的块矩阵形式：
$$G_i = \begin{bmatrix} G_{i-1} & G_{i-1} \\ G_{i-1} \cdot T_{i-1} & G_{i-1} \cdot T'_{i-1} \end{bmatrix}$$
其中T_{i-1}和T'_{i-1}是对角矩阵，且对应位置元素不同。给定这样的结构，证明者可以高效地执行“折叠”操作：从上层编码π_{i+1}，利用挑战α_i，通过线性插值计算出下层编码π_i。具体地，对于每个位置j，π_i[j] = f(α_i)，其中f(X)是经过点(T_i[j], π_{i+1}[j])和(T'_i[j], π_{i+1}[j+n_i])的唯一线性多项式。这构成了BaseFold IOPP的核心。协议的commit阶段，证明者根据一系列的折叠挑战α_0,...,α_{d-1}，递归地生成π_d到π_0。在query阶段，验证者抽取一个位置μ，并递归检查折叠操作的一致性，最后检查π_0是否是一个合法的基码字。该IOPP的完备性是直接的，而其可靠性依赖于代码的相对最小距离和Johnson界，证明者欺骗的概率随着查询次数指数级下降。

**2. 随机折叠码**

为了获得一个域无关且可高效编码的折叠码，本文构造了随机折叠码。该码的递归折叠矩阵由随机选取的对角矩阵定义：T_i的对角元素从F^x中均匀采样，并令T'_i = -T_i。基础码G_0是一个MDS码。这样的码具有约n log n次域加法和0.5 n log n次域乘法的编码时间，不受域的大小限制。作者通过精心设计的组合论证和概率分析（Theorem 2），证明了该码具有极高的最小相对距离。例如，对于2^25的码长和1/8的码率，在256-bit域上，其最小相对距离可达0.728。这为IOPP的可靠性提供了坚实的保障。

**3. 多线性多项式承诺方案**

最后，作者将BaseFold IOPP与经典的sum-check协议巧妙结合，构造了多线性PCS。其核心在于：sum-check协议可以将一个任意点的多线性求值问题，转化为在一个随机点上的求值问题；而BaseFold IOPP的最后一层输出π_0恰好是（接近）一个码字的编码，且该码字对应于某个特定点上的缩并值（即经过折叠挑战后的多项式值）。因此，证明者和验证者可以共享同一组折叠挑战（即sum-check的随机挑战），使得最后的IOPP输出与sum-check的最后一个消息对齐。具体协议中，证明者首先发送一个单变量多项式h_d(X)，并开始一个交错的sum-check和IOPP过程。最终，验证者除了检查sum-check的一致性外，还检查BaseFold IOPP.query的输出为接受，并验证π_0 = Enc_0(h_1(r_0) / eq_z(r))，从而将求值声明与承诺绑定。

该方案的安全性包括评估绑定性和知识可靠性。评估绑定性依赖于一个引理（Lemma 7）：如果证明者可以通过验证，则承诺的oracle极大概率接近一个唯一的多线性多项式f的编码，且f(z)=y。该证明利用了IOPP的可靠性、sum-check的可靠性以及折叠操作与多线性多项式求值之间的代数关系。知识可靠性（Theorem 4）则通过构建一个提取器证明：对于任何成功的证明者，提取器可以通过谓词分叉引理（Lemma 9）获得足够多的独立且正确的求值点，进而通过解线性方程组恢复整个多项式f。该方案实现了O(n log n)的证明者时间（编码主导）、O(log^2 n)的验证者时间以及对数级别的证明大小。

### 核心公式与流程

**[折叠码生成矩阵递归定义]**
$$G_i = \begin{bmatrix} G_{i-1} & G_{i-1} \\ G_{i-1} \cdot T_{i-1} & G_{i-1} \cdot T'_{i-1} \end{bmatrix}$$
> 作用：定义了折叠线性码的核心结构，是BaseFold IOPP能够高效递归的基础。

**[编码算法（Protocol 1）]**
对于向量m = (m_l, m_r): Enc_i(m) = (Enc_{i-1}(m_l) + t ∘ Enc_{i-1}(m_r), Enc_{i-1}(m_l) - t ∘ Enc_{i-1}(m_r))，其中t = diag(T_{i-1})。
> 作用：利用递归结构实现了O(n log n)的快速编码。

**[BaseFold IOPP核心折叠操作]**
对于每个位置j，设置g_j(X) = interpolate( (diag(T_i)[j], π_{i+1}[j]), (diag(T'_i)[j], π_{i+1}[j + n_i]) )，然后令π_i[j] = g_j(α_i)。
> 作用：定义了如何在IOPP的commit阶段根据挑战α_i从上层oracle π_{i+1}“折叠”出下层oracle π_i。

**[PCS评估协议核心检查]**
验证者检查：1) sum-check的一致性：h_d(0)+h_d(1)=y 且 h_i(0)+h_i(1)=h_{i+1}(r_i) ∀i；2) IOPP.query输出接受；3) Enc_0( h_1(r_0) / eq_z(r) ) = π_0。
> 作用：将sum-check的最终断言与IOPP的最终oracle π_0绑定，从而将一个任意点求值问题转化并归结为对承诺编码的检查。

### 实验结果

论文使用AWS r6i.8xlarge实例（16核，256 GiB RAM）进行实验，所有方案均使用Blake2s256哈希函数。在ECDSA签名验证基准测试中，Hyperplonk[Basefold]的证明者时间仅为122毫秒，而基于FRI的Hyperplonk[ZeromorphFri]需要2.9秒，前者快约23倍。与另一个域无关方案Brakedown相比，Hyperplonk[Basefold]的证明者时间（3.862秒）与Brakedown（3.691秒）相当，但证明大小仅为23 MB，比Brakedown的254 MB小一个数量级以上，验证者时间仅为87毫秒，比Brakedown的2.725秒快31倍。与ECFFT2相比，BaseFold的编码算法（1.67秒）比ECFFT2的ENTER协议（26.894秒）快16倍。在同一256-bit域下，BaseFold PCS的证明者比ZeromorphFri快2-3倍，但证明大2-3倍，验证者慢约1.2倍。在64-bit域下，由于其随机码的速率降低，性能差距缩小，但如果BaseFold改用接近RS码速率的Reed-Solomon码（BaseFoldFri），则仍可保持约3倍的速度优势。

### 局限性与开放问题
本文的随机折叠码是一个随机化构造，其最小距离是概率保证，未来一个重要的开放问题是能否找到显式的、域无关的、具有高最小相对距离的折叠线性码。此外，虽然BaseFold PCS的证明者时间优于FRI，但其证明大小和对数验证者时间仍然大于KZG系列方案，但在域无关性场景下这是无法避免的。实验也揭示，在低速率、小域下，随机折叠码的性能优势会减弱，探索更优的参数或替代结构是有价值的方向。最后，论文证明了基于IOP的PCS的安全性，但如何将类似于Deep-FRI的技术应用于BaseFold以进一步缩小其与FRI在证明大小和验证者效率上的差距，是一个值得探索的问题。

### 强关联论文

[5] Ben-Sasson, E., Bentov, I., Horesh, Y., Riabzev, M. Fast Reed-Solomon Interactive Oracle Proofs of Proximity. **ICALP 2018** [Google Scholar](https://scholar.google.com/scholar?q=Fast+Reed-Solomon+Interactive+Oracle+Proofs+of+Proximity)

[7] Ben-Sasson, E., Carmon, D., Kopparty, S., Levit, D. Scalable and transparent proofs over all large fields, via elliptic curves. **TCC 2022** [Google Scholar](https://scholar.google.com/scholar?q=Scalable+and+transparent+proofs+over+all+large+fields+via+elliptic+curves)

[11] Ben-Sasson, E., Goldberg, L., Kopparty, S., Saraf, S. DEEP-FRI: sampling outside the box improves soundness. **ITCS 2020** [Google Scholar](https://scholar.google.com/scholar?q=DEEP-FRI+sampling+outside+the+box+improves+soundness)

[12] Ben-Sasson, E., Kopparty, S., Saraf, S. Worst-case to average case reductions for the distance to a code. **CCC 2018** [Google Scholar](https://scholar.google.com/scholar?q=Worst-case+to+average+case+reductions+for+the+distance+to+a+code)

[13] Block, A.R., Garreta, A., Katz, J., Thaler, J., Tiwari, P.R., Zajac, M. Fiat-Shamir security of FRI and related SNARKs. **ePrint 2023** [Google Scholar](https://scholar.google.com/scholar?q=Fiat-Shamir+security+of+FRI+and+related+SNARKs)

[20] Chen, B., Bünz, B., Boneh, D., Zhang, Z. HyperPlonk: plonk with linear-time prover and high-degree custom gates. **EUROCRYPT 2023** [Google Scholar](https://scholar.google.com/scholar?q=HyperPlonk+plonk+with+linear-time+prover+and+high-degree+custom+gates)

[26] Golovnev, A., Lee, J., Setty, S., Thaler, J., Wahby, R.S. Brakedown: Linear-time and post-quantum SNARKs for R1CS. **ePrint 2021** [Google Scholar](https://scholar.google.com/scholar?q=Brakedown+Linear-time+and+post-quantum+SNARKs+for+R1CS)

[31] Kate, A., Zaverucha, G.M., Goldberg, I. Constant-size commitments to polynomials and their applications. **ASIACRYPT 2010** [Google Scholar](https://scholar.google.com/scholar?q=Constant-size+commitments+to+polynomials+and+their+applications)

[33] Kohrita, T., Towa, P. Zeromorph: Zero-knowledge multilinear-evaluation proofs from homomorphic univariate commitments. **ePrint 2023** [Google Scholar](https://scholar.google.com/scholar?q=Zeromorph+Zero-knowledge+multilinear-evaluation+proofs+from+homomorphic+univariate+commitments)

[38] Papamanthou, C., Shi, E., Tamassia, R. Signatures of correct computation. **TCC 2013** [Google Scholar](https://scholar.google.com/scholar?q=Signatures+of+correct+computation)


## 关键词

+ 多项式承诺方案
+ 域无关
+ 可折叠码
+ FRI交互式预言机证明
+ 多线性多项式
+ SNARK