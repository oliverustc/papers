---
title: "Concretely efficient lattice-based polynomial commitment from standard assumptions"
doi: 10.1007/978-3-031-68403-6_13

标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 2024
created: 2025-04-21 10:57:11
modified: 2025-04-21 10:57:50
---
## Concretely efficient lattice-based polynomial commitment from standard assumptions

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-68403-6_13)

## 作者

+ Intak Hwang 
+ Jinyeong Seo 
+ Yongsoo Song 

## 笔记

### 背景与动机

多项式承诺是构建零知识简洁非交互知识论证（zkSNARK）的核心原语，其性能直接影响诸多密码协议。现有最实用的多项式承诺方案主要基于两条技术路线：离散对数假设方案[16,30]虽拥有紧凑的证明大小和丰富的同态性质（如证明批处理与递归组合），但无法抵抗量子敌手；基于纠错码的方案[9,25]虽具备后量子安全性，但缺乏同态性质，无法支持高效的递归证明。近年来，格基构造[2,3,21,23]因其有望同时实现抗量子性与功能性而受到关注，但这些方案往往存在具体效率低下或依赖需要进一步密码分析的新假设（如k-R-ISIS假设[39]）等瓶颈。例如，这些格基方案的证明大小与验证复杂度虽可达对数级，但其可提取性依赖于已被启发式攻破的假设，且均需可信设置。本文旨在填补这一空白，提出一个基于标准格假设（MSIS与MLWE）的多项式承诺方案，在实现平方根量级证明大小与验证复杂度的同时，确保具体的高效性，并具备透明设置与公开可验证性。

### 相关工作

[7] Baum 等. Sublinear Lattice-Based Zero-Knowledge Arguments for Arithmetic Circuits. **CRYPTO 2018** [Google Scholar](https://scholar.google.com/scholar?q=Sublinear+Lattice-Based+Zero-Knowledge+Arguments+for+Arithmetic+Circuits)
> 核心思路：基于Ajtai承诺方案构建了证明大小为平方根、知识论证的子线性零知识论证，并采用了批处理技术。
> 局限与区别：其方案仅能承诺小值消息，对于多项式承诺中通常为大素数的消息模数p，直接嵌入会导致参数膨胀；此外，为实现零知识性，其依赖拒绝采样技术，重复率随承诺多项式数量指数增长，不适合需承诺多个多项式的场景。

[13] Bootle 等. Efficient Zero-Knowledge Arguments for Arithmetic Circuits in the Discrete Log Setting. **EUROCRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+Zero-Knowledge+Arguments+for+Arithmetic+Circuits+in+the+Discrete+Log+Setting)
> 核心思路：基于Pedersen承诺，通过将多项式系数矩阵化并利用Vandermonde矩阵可逆性，实现了平方根量级的证明大小。
> 局限与区别：该构造依赖离散对数假设的代数性质（如Vandermonde矩阵在Z_p上的可逆性），无法直接迁移至Ajtai承诺的R环上。本文通过重设计知识提取器（基于[7]的批处理sigma协议）并适配其盲化技术至离散高斯分布，解决了这一兼容性问题。

[25] Golovnev 等. Brakedown: Linear-Time and Field-Agnostic SNARKs for R1CS. **CRYPTO 2023** [Google Scholar](https://scholar.google.com/scholar?q=Brakedown%3A+Linear-Time+and+Field-Agnostic+SNARKs+for+R1CS)
> 核心思路：基于纠错码构建了线性证明时间的多项式承诺方案，证明大小为平方根量级，具有后量子安全性。
> 局限与区别：Brakedown缺乏同态性质，无法支持高效的递归证明组合。本文方案在提供相近证明大小与性能的同时，具备线性同态性，有利于证明批处理与递归组合。

[3] Albrecht 等. SLAP: Succinct Lattice-Based Polynomial Commitments from Standard Assumptions. **EUROCRYPT 2024** [Google Scholar](https://scholar.google.com/scholar?q=SLAP%3A+Succinct+Lattice-Based+Polynomial+Commitments+from+Standard+Assumptions)
> 核心思路：基于标准格假设构建了证明大小为对数量级的承诺方案，但需可信设置。
> 局限与区别：SLAP的证明大小虽渐近更优，但具体实现中，对于多项式度2^20，其证明大小为36.5 MB，远大于本文的8.93 MB（约4.1倍）。此外，SLAP未提供证明生成与验证的具体性能基准。

[27] Kim 等. Toward Practical Lattice-Based Proof of Knowledge from Hint-MLWE. **CRYPTO 2023** [Google Scholar](https://scholar.google.com/scholar?q=Toward+Practical+Lattice-Based+Proof+of+Knowledge+from+Hint-MLWE)
> 核心思路：为BDLOP承诺方案设计了无需拒绝采样的POK协议，通过利用离散高斯分布的性质实现模拟性。
> 局限与区别：该工作直接应用于BDLOP（其POK语句仅依赖于承诺随机性），而本文将其核心思想推广至Ajtai承诺（其语句同时依赖于消息与随机性）。本文的创新在于提出了随机化编码技术，使编码后的消息也服从离散高斯分布，从而消除了拒绝采样。

### 核心技术与方案

本文方案分为两个层次：一是修改的Ajtai承诺方案及其证明打开知识协议，二是基于此构建的多项式承诺方案。

**修改的Ajtai承诺方案**：核心在于解决两个关键问题。  
1. **可编码大消息的紧凑承诺**：多项式承诺中消息模数p（如255位素数）远大于为绑定性所设的承诺模数q。为解决参数膨胀，本文提出了新编码方法。该编码（Ecd）将$\mathbb{Z}_p^{d/r}$中的消息映射为R中的小范数多项式（范数$\le (b+2)/2$），通过利用同构$\varphi: R/(X^{d/r}-b) \xrightarrow{\cong} \mathbb{Z}_p^{d/r}$（其中$p=b^r+1$）。解码（Dcd）则应用$\varphi$恢复消息。编码后，消息范数从$O(r\log b)$降至$O(\log b+\log r)$，从而q可相应减小约$r^2$倍。  
2. **无需拒绝采样的可模拟POK**：为消除拒绝采样带来的指数级重复率，本文提出了随机化编码（R.Ecd）。由于解码仅依赖于编码结果模$X^{d/r}-b$的同余类，因此可为输入$\vec{a}$采样一个服从离散高斯分布$D_{\text{Ecd}(\vec{a})+P\mathbb{Z}^d,\mathfrak{s}P}$的随机代表，其中P是$X^{d/r}-b$的负循环矩阵。这保证了编码结果满足同余关系的同时，其分布可被模拟。  

基于此，POK协议$\Pi_{\text{Open}}$（图1）采用文献[7]的批处理技术，可同时证明k个承诺的打开知识。协议中，证明者生成掩码$\vec{\pmb{g}}_j$（服从随机化编码）和$\vec{\gamma}_j$（服从离散高斯），响应挑战$\pmb{c}_{j,i}$（取自单项式集）后计算$\vec{\pmb{t}}_j=\vec{\pmb{g}}_j+\sum_i \pmb{c}_{j,i}\cdot\vec{\pmb{m}}_i$和$\vec{\tau}_j=\vec{\gamma}_j+\sum_i \pmb{c}_{j,i}\cdot\vec{\mu}_i$。其完备性由适当选取的高斯宽度参数保证（定理2）。可靠性的关键是通过重绕提取器[7]获得合法打开（定理3）。模拟性的核心是利用卷积引理（引理10）和线性组合引理（引理11）证明，即使响应部分泄露信息，通过Hint-MLWE困难性假设，敌手也无法区分真实协议与模拟器生成的转录（定理4）。

**多项式承诺方案**：整体框架遵循Bootle和Groth[13,14]的结构，但对其两处核心机制进行了适配。  
1. **提取性**：原方案依赖Vandermonde矩阵在$\mathbb{Z}_p$上的可逆性进行知识提取。由于该性质在R中一般不成立，本文通过额外打开知识协议$\pi_{\text{PC.Open}}$提供提取性。该协议可打开前m个承诺，并结合评估证明$\rho=(\vec{e},\vec{\varepsilon})$恢复最后一个承诺的打开（定理8）。  
2. **评估隐藏性**：原方案使用均匀盲化器$b_i\in\mathbb{Z}_p$隐藏系数，本文将其替换为由随机化编码生成的离散高斯盲化器。具体地，在承诺阶段，从$\mathbb{Z}_p$均匀抽取$b_1,\dots,b_{n-1}$，定义$\vec{h}_m=(b_1,\dots,b_{n-1},0)$和$\vec{h}_{m+1}=(0,-b_1,\dots,-b_{n-1})$，并对它们执行随机化编码。评估证明$\vec{e}=\sum_{i=0}^{m-1}\text{Ecd}(x^{ni})\cdot\vec{\pmb{h}}_i + \text{Ecd}(x)\cdot\vec{\pmb{h}}_m + \vec{\pmb{h}}_{m+1}$。由于盲化器对应的编码结果服从离散高斯，通过Hint-MLWE假设可证明模拟器能生成不可区分的证明（定理9）。

**复杂度分析**：当设$n=m=\sqrt{N}$时，证明者和验证者的计算复杂度均为$\tilde{O}(N\cdot\text{polylog}(N))$（通信复杂度$\tilde{O}(\sqrt{N})$），实现了平方根量级的验证与通信开销。此外，方案天然支持线性同态性。

### 核心公式与流程

**[编码映射]**
$$ \varphi: \bar{\mathbf{a}} = \sum_{i=0}^{d/r-1}\sum_{j=0}^{r-1} a_{(d/r)j+i} X^{(d/r)j+i} \mapsto \left(\sum_{j=0}^{r-1} a_{(d/r)j} b^j, \ldots, \sum_{j=0}^{r-1} a_{(d/r)(j+1)-1} b^j\right) \in \mathbb{Z}_p^{d/r} $$
> 作用：将多项式环R/(X^{d/r} - b)中的元素同构映射到$\mathbb{Z}_p^{d/r}$，其中$p = b^r + 1$。编码Ecd利用此同构的逆，将大整数表示为小系数多项式。

**[承诺生成与验证]**
承诺：$\vec{\mathfrak{m}} = \mathbf{A}_0 \vec{\pmb{m}} + \mathbf{A}_1 \vec{\mu} \pmod{q}$  
验证：$\mathbf{A}_0 \vec{\pmb{e}} + \mathbf{A}_1 \vec{\varepsilon} = \sum_{i=0}^{m-1} \text{Ecd}(x^{ni}) \cdot \vec{\mathfrak{h}}_i + \text{Ecd}(x) \cdot \vec{\mathfrak{h}}_m + \vec{\mathfrak{h}}_{m+1} \pmod{q}$  
> 作用：Ajtai承诺方案的核心线性形式。绑定性约简为MSIS问题，隐藏性约简为MLWE问题。

**[POK协议响应计算与验证]**
响应：$\vec{\pmb{t}}_j = \vec{\pmb{g}}_j + \sum_{i=0}^{k-1} \pmb{c}_{j,i} \cdot \vec{\pmb{m}}_i, \quad \vec{\tau}_j = \vec{\gamma}_j + \sum_{i=0}^{k-1} \pmb{c}_{j,i} \cdot \vec{\mu}_i$  
验证：$\|\vec{\pmb{t}}_j \| \vec{\tau}_j \|_2 \stackrel{?}{\le} \beta_{\text{Open}}, \quad \mathbf{A}_0 \vec{\pmb{t}}_j + \mathbf{A}_1 \vec{\tau}_j \stackrel{?}{=} \vec{\mathfrak{g}}_j + \sum_{i=0}^{-1} \pmb{c}_{j,i} \cdot \vec{\mathfrak{m}}_i$  
> 作用：Sigma协议的核心步骤。证明者使用掩码响应线性挑战，验证者检查范数界与承诺匹配性。

**[离散高斯卷积引理]**
对于$k>1$，若$\sqrt{\Sigma/2} \ge \eta_\varepsilon(\Lambda)$，则$\sum_{i=0}^{k-1} \mathcal{D}_{\vec{u}_i+\Lambda,\sqrt{\Sigma}}$的分布统计接近$\mathcal{D}_{\sum \vec{u}_i+\Lambda,\sqrt{k\Sigma}}$。
> 作用：证明模拟性的关键工具，允许分解或合并多个离散高斯分布。

### 实验结果

实验采用Rust语言实现，在Intel Xeon Platinum 8268 CPU（2.90 GHz, 384GB RAM）上单线程运行，Fiat-Shamir变换使用SHA-3哈希。参数设置：消息模数p为255位（b=63388, r=16），承诺模数q约112位，环维度d=2048，MSIS秩$\mu=1$，MLWE秩$\nu=2$。

基准测试（表3）显示，对于多项式度$N$从$2^{19}$到$2^{25}$，本文方案（含零知识）的证明者耗时从3.55秒到188秒，验证者耗时从0.14秒到1.07秒，通信开销（承诺+评估+打开证明）从6.07 MB到47.5 MB。与Brakedown [25]相比，在非零知识设置下，证明者时间相近（如$N=2^{21}$时，本文3.47秒对比Brakedown 2.41秒）；验证者时间与通信开销大致相当。与FRI [9]相比，证明者性能稍慢，但通信开销大一个数量级。

关键对比是与SLAP [3]（表4）：对于$N=2^{20}$，本文证明大小为8.93 MB，SLAP为36.5 MB，压缩约4.1倍。

### 局限性与开放问题

离散高斯采样是当前证明者性能的主要瓶颈，优化采样算法可直接加速协议。在证明大小方面，采用分层Ajtai承诺[15]可将渐近复杂度从$\tilde{O}(\sqrt{N})$进一步降至$\tilde{O}(N^{1/c})$，实现更紧凑的证明。此外，当前实现仅证明了概念的可行性，未进行并行化或针对常用平台（如GPU）的深度优化，实际部署性能仍有提升空间。

### 强关联论文

[7] Baum, C., et al. Sublinear Lattice-Based Zero-Knowledge Arguments for Arithmetic Circuits. **CRYPTO 2018** [Google Scholar](https://scholar.google.com/scholar?q=Sublinear+Lattice-Based+Zero-Knowledge+Arguments+for+Arithmetic+Circuits)

[13] Bootle, J., et al. Efficient Zero-Knowledge Arguments for Arithmetic Circuits in the Discrete Log Setting. **EUROCRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+Zero-Knowledge+Arguments+for+Arithmetic+Circuits+in+the+Discrete+Log+Setting)

[14] Bootle, J., et al. Efficient Batch Zero-Knowledge Arguments for Low Degree Polynomials. **PKC 2018** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+Batch+Zero-Knowledge+Arguments+for+Low+Degree+Polynomials)

[25] Golovnev, A., et al. Brakedown: Linear-Time and Field-Agnostic SNARKs for R1CS. **CRYPTO 2023** [Google Scholar](https://scholar.google.com/scholar?q=Brakedown%3A+Linear-Time+and+Field-Agnostic+SNARKs+for+R1CS)

[3] Albrecht, M.R., et al. SLAP: Succinct Lattice-Based Polynomial Commitments from Standard Assumptions. **EUROCRYPT 2024** [Google Scholar](https://scholar.google.com/scholar?q=SLAP%3A+Succinct+Lattice-Based+Polynomial+Commitments+from+Standard+Assumptions)

[27] Kim, D., et al. Toward Practical Lattice-Based Proof of Knowledge from Hint-MLWE. **CRYPTO 2023** [Google Scholar](https://scholar.google.com/scholar?q=Toward+Practical+Lattice-Based+Proof+of+Knowledge+from+Hint-MLWE)

[8] Baum, C., et al. More Efficient Commitments from Structured Lattice Assumptions. **SCN 2018** [Google Scholar](https://scholar.google.com/scholar?q=More+Efficient+Commitments+from+Structured+Lattice+Assumptions)

[9] Ben-Sasson, E., et al. Fast Reed-Solomon Interactive Oracle Proofs of Proximity. **ICALP 2018** [Google Scholar](https://scholar.google.com/scholar?q=Fast+Reed-Solomon+Interactive+Oracle+Proofs+of+Proximity)

[16] Bünz, B., et al. Bulletproofs: Short Proofs for Confidential Transactions and More. **IEEE S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Bulletproofs%3A+Short+Proofs+for+Confidential+Transactions+and+More)

[31] Lyubashevsky, V. Lattice Signatures Without Trapdoors. **EUROCRYPT 2012** [Google Scholar](https://scholar.google.com/scholar?q=Lattice+Signatures+Without+Trapdoors)


## 关键词

+ 格基多项式承诺平方根证明
+ 标准格假设透明设置zkSNARK
+ 后量子多项式承诺同态性
+ 递归证明批处理格基方案
+ 具体高效格承诺与Brakedown比较