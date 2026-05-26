---
title: "How to Prove Statements Obliviously?"

标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 2024

modified: 2025-04-10 17:07:28
---

## How to Prove Statements Obliviously?

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-68403-6_14)

## 作者

+ [Sanjam Garg](Sanjam%20Garg.md)
+ [Aarushi Goel](Aarushi%20Goel.md)
+ [Mingyuan Wang](Mingyuan%20Wang.md)

## 笔记

### 背景与动机
许多密码学应用需要证明关于隐藏秘密满足特定电路关系的陈述，例如证明群元素之间的线性关系、正确计算同态加密结果等。传统方案要求证明者直接访问秘密值，这在秘密仅以加密或承诺形式存在时不可行，导致必须非黑盒地展开底层密码原语的电路描述，效率极低。现有针对可验证私有计算委托的黑盒方案需昂贵的、不可重用的预处理，多服务器SNARK外包方案则依赖对部分服务器的信任假设。本文旨在填补这一空白，提出一种通用技术——FRI on Hidden Values，使证明者能在仅持有秘密的线性同态封装时高效生成SNARK，并首次在单服务器、无设置等强假设下，为多种应用提供了黑盒可行性。

### 相关工作

[BBHR18] Ben-Sasson等. Fast Reed-Solomon Interactive Oracle Proofs of Proximity. **ICALP 2018** [Google Scholar](https://scholar.google.com/scholar?q=Fast+Reed-Solomon+Interactive+Oracle+Proofs+of+Proximity)
> 核心思路：提出了FRI协议，一种用于测试函数是否接近Reed-Solomon码字的交互式预言机证明，具有对数级验证复杂度。
> 局限与区别：FRI协议要求证明者和验证者访问明文的域求值，无法直接应用于秘密仅以封装形式存在的情形。本文将其扩展为工作于线性同态封装之上。

[BGKS20] Ben-Sasson等. DEEP-FRI: Sampling outside the box improves soundness. **ITCS 2020** [Google Scholar](https://scholar.google.com/scholar?q=DEEP-FRI+Sampling+outside+the+box+improves+soundness)
> 核心思路：提出了基于FRI的多项式承诺方案，证明者可在提交多项式后对其求值进行简洁证明。
> 局限与区别：该方案同样要求证明者直接拥有多项式系数的明文，不适用于秘密封装场景。本文将其推广到隐藏值情形。

[GJM+24] Garg等. Hints: Threshold Signatures with Silent Setup. **IEEE S&P 2024** [Google Scholar](https://scholar.google.com/scholar?q=Threshold+Signatures+with+Silent+Setup)
> 核心思路：提出基于BLS的加权门限签名框架，通过发布公开提示实现聚合器对公钥聚合的SNARK证明。
> 局限与区别：要求各用户发布线性于总人数的提示，导致总通信复杂度呈平方级，且依赖可信设置。本文利用FRI on Hidden Values消除了提示需求和设置，且签名大小为对数平方级。

[DCX+23] Das等. Threshold Signatures from Inner Product Argument: Succinct, Weighted, and Multi-Threshold. **CCS 2023** [Google Scholar](https://scholar.google.com/scholar?q=Threshold+Signatures+from+Inner+Product+Argument)
> 核心思路：与[GJM+24]类似，提出基于内积论证的门限签名框架。
> 局限与区别：同样需要公开提示和设置，且依赖于配对友好群。本文的方案不需要配对，且可应用于Schnorr签名等非配对群。

[CKV10] Chung等. Improved Delegation of Computation using Fully Homomorphic Encryption. **CRYPTO 2010** [Google Scholar](https://scholar.google.com/scholar?q=Improved+Delegation+of+Computation+using+Fully+Homomorphic+Encryption)
> 核心思路：提出基于FHE的可验证私有计算委托方案，通过预处理多个随机输入实现验证。
> 局限与区别：预处理计算量与安全参数和电路大小线性相关，且不可重用。本文方案预处理独立于FHE且可重用，在线验证仅需对数级FHE运算。

[MRV+21] Micali等. Compact Certificates of Collective Knowledge. **IEEE S&P 2021** [Google Scholar](https://scholar.google.com/scholar?q=Compact+Certificates+of+Collective+Knowledge)
> 核心思路：利用Merkle树和随机挑战实现无设置加权门限签名。
> 局限与区别：仅适用于松弛斜坡设置，在陡峭门限下签名大小线性于总人数。本文方案在陡峭门限下签名大小为对数平方级。

[BHV+23] Bhadauria等. Private Polynomial Commitments and Applications to MPC. **PKC 2023** [Google Scholar](https://scholar.google.com/scholar?q=Private+Polynomial+Commitments+and+Applications+to+MPC)
> 核心思路：提出私有多项式承诺，允许承诺者对加密多项式进行承诺和求值证明，依赖配对和内积论证。
> 局限与区别：构造依赖于特定的配对友好加密方案。本文方案适用于任何线性同态封装，更通用。

[BDFG21] Boneh等. Halo Infinite: Proof-Carrying Data from Additive Polynomial Commitments. **CRYPTO 2021** [Google Scholar](https://scholar.google.com/scholar?q=Halo+Infinite+Proof-Carrying+Data+from+Additive+Polynomial+Commitments)
> 核心思路：提出KZG多项式承诺公开聚合方案。
> 局限与区别：聚合开销为线性，验证开销为平方级。本文聚合方案验证开销为线性。

[GGP10] Gennaro等. Non-interactive Verifiable Computing: Outsourcing Computation to Untrusted Workers. **CRYPTO 2010** [Google Scholar](https://scholar.google.com/scholar?q=Non-interactive+Verifiable+Computing+Outsourcing+Computation+to+Untrusted+Workers)
> 核心思路：提出基于FHE的可验证计算方案，客户端预处理多个加密输入。
> 局限与区别：与[CKV10]类似，预处理不可重用且开销大。本文方案更高效。

[BGV11] Benabbas等. Verifiable Delegation of Computation over Large Datasets. **CRYPTO 2011** [Google Scholar](https://scholar.google.com/scholar?q=Verifiable+Delegation+of+Computation+over+Large+Datasets)
> 核心思路：提出大数据集上的可验证计算委托方案。
> 局限与区别：同样面临预处理不可重用的问题。本文方案不同。

### 核心技术与方案

本文的核心技术创新在于将对FRI协议的应用从明文域推广到线性同态封装域。首先，论文形式化定义了线性同态封装LHEncap，涵盖同态加密、同态承诺、群指数等常见原语。然后，发现FRI协议中证明者和验证者在协议全过程中仅对域求值进行线性操作。因此，只要证明者持有封装后的域求值，且验证者能访问这些封装，整个协议流程（包括折叠计算和一致性检查）就可在封装域上直接执行。这构成了FRI on LHEncap协议：证明者提交各层折叠多项式在对应域上的封装求值作为预言机，验证者在查询阶段根据LHEncap的性质（可解密或具有随机数线性同态性）进行验证。在可解密情形下，解密后验证；在随机数线性同态情形下，直接在封装上验证等式。该IOP可获得轮次知识可靠性（约简到标准FRI的知识可靠性 [BGK+23]），并通过[BCS16]编译器和Fiat-Shamir启发式变换为随机预言机模型下的SNARK，知识可靠性误差为查询次数与FRI可靠性误差的乘积。

基于FRI on LHEncap，论文构造了隐藏值上的多项式承诺方案。证明者持有代数系数 $f_0, \ldots, f_d$ 的封装 $[\![f_0]\!], \ldots, [\![f_d]\!]$，使用FFT扩展求值域并计算Merkle承诺。打开证明时，对任意求值点 $x^*$，证明者需证明商多项式 $h(x) = (f(x) - f(x^*))/(x - x^*)$ 是次数不超过 $d-1$ 的多项式。由于 $h(x)$ 的求值可由 $f(x)$ 的封装通过线性运算得到，证明者直接运行FRI on LHEncap来证明 $h$ 的低度性。该方案的承诺大小 $O(1)$，证明生成时间 $O(d)$，证明大小和验证时间均为 $O(\log^2 d)$。

论文随后展示了该工具的三个应用。应用一：可高效验证的私有计算委托。客户端用FHE加密输入，服务器同态计算电路并获取计算轨迹的加密。服务器使用隐藏值多项式承诺对计算轨迹编码的多项式进行承诺，运行多项式IOP（如Fractal [COS20]）的所有步骤，但所有涉及扩展证人的计算都在FHE上执行。最终输出加密的SNARK，客户端解密并验证。除必要的 $|C|$ 次FHE运算外，服务器仅需 $O(|C|\log |C|)$ 次常量乘法深度的FHE运算；证明大小和验证时间为 $O(\log^2 |C|)$，且预处理独立于FHE、可重用。应用二：zkSNARK的私有单服务器外包。修改上一方案，客户端将FHE公钥承诺发送给服务器，服务器生成加密SNARK后返回。客户端解密所有密文，并附加零知识证明证明解密的正确性。这使得最终证明可公开验证，且客户端只需对极少量（polylog级别）密文做非黑盒操作。该方案假设服务器半诚实，安全性基于底层SNARK的知识可靠性和FHE的安全性。应用三：无设置加权门限签名。基于Schnorr多签名方案，将验证密钥设为秘密多项式SK和权重多项式W的多项式承诺。聚合器从签名集合B构建聚合公钥apk，并生成SNARK证明apk是B中公钥的诚实聚合且B的累计权重大于阈值T。证明利用广义求和检查（Lemma 1）建立多项式恒等式：$\text{SK}(x) \cdot B(x) = (\sum_i \text{sk}_i \cdot b_i)/n + Q_x(x) \cdot x + Q_Z(x) \cdot Z(x)$ 和 $W(x) \cdot B(x) = (\sum_i w_i \cdot b_i)/n + Q'_x(x) \cdot x + Q'_Z(x) \cdot Z(x)$，以及二进制检查等式 $B(x) \cdot (1 - B(x)) = Q(x) \cdot Z(x)$。聚合器计算各商多项式的承诺，并在随机挑战点 $r$ 处打开验证。最终签名大小为 $O(\log^2 n)$，验证时间 $O(\log^2 n)$，聚合时间 $O(n \log n)$。在代数群模型和随机预言机模型下，该方案的安全性是可靠的。

### 核心公式与流程

**[FRI折叠公式]**
$$
[\![f_{i+1}(\omega^{2^{i+1} \cdot j})]\!] = \left(\frac{[\![f_i(\omega^{2^i \cdot j})]\!] + [\![f_i(-\omega^{2^i \cdot j})]\!]}{2} + \alpha_i \cdot \frac{[\![f_i(\omega^{2^i \cdot j})]\!] - [\![f_i(-\omega^{2^i \cdot j})]\!]}{2 \cdot \omega^{2^i \cdot j}}\right)
$$
> 作用：FRI on LHEncap第 $i+1$ 轮中，证明者根据上一轮域求值封装和挑战 $\alpha_i$，计算折叠后多项式在缩减域上的封装值。

**[多项式承诺打开证明的商多项式关系]**
$$
[\![h(x)]\!] = \frac{[\![f(x)]\!] - [\![y^*]\!]}{x - x^*}
$$
> 作用：定义商多项式 $h$ 的封装求值，其中 $y^*$ 是待证明的求值点 $x^*$ 处的封装值。证明 $h$ 的低度性等价于证明 $f(x^*)=y^*$。

**[加权门限签名广义求和检查恒等式]**
$$
\text{SK}(x) \cdot B(x) = \frac{\sum_i \text{sk}_i \cdot b_i}{n} + Q_x(x) \cdot x + Q_Z(x) \cdot Z(x)
$$
$$
W(x) \cdot B(x) = \frac{\sum_i w_i \cdot b_i}{n} + Q'_x(x) \cdot x + Q'_Z(x) \cdot Z(x)
$$
$$
B(x) \cdot (1 - B(x)) = Q(x) \cdot Z(x)
$$
> 作用：前两个等式编码聚合公钥 $\prod_i \text{pk}_i^{b_i}$ 的对数和集合B的权重和；第三个等式强制 $B(x)$ 在求值域上的取值仅为0或1，确保B是指示向量。

**[KZG聚合的广义求和检查恒等式]**
$$
\Pi(x) \cdot T(x) \cdot V(x) = \frac{\sum_i Q_i(\tau) \cdot (\tau - x_i) \cdot v^i}{n} + Q_x(x) \cdot x + Q_Z(x) \cdot Z(x)
$$
> 作用：KZG证明聚合的核心恒等式，其中 $\Pi(x)$ 编码各证明 $\pi_i = g^{Q_i(\tau)}$，$T(x)$ 编码 $(\tau - x_i)$，$V(x)$ 编码随机挑战幂次。证明该恒等式成立等价于验证随机线性组合后的配对等式。

### 实验结果
本文未提供传统软件实验，但给出了各方案的理论性能分析。对于可验证私有计算委托：服务器在必要计算外需额外 $O(|C|\log |C|)$ 次常量乘法深度的FHE运算；证明大小和验证时间为 $O(\log^2 |C|)$；预处理独立于FHE且可无限重用。对于zkSNARK私有外包：服务器计算开销为 $O(|R|\log |R|)$ 次FHE运算；最终证明大小与底层zkSNARK证明大小同阶，加上同等规模的零知识证明。对于加权门限签名：聚合时间为 $O(n \log n)$；签名大小和验证时间为 $O(\log^2 n)$；完全无需任何设置或部署前的交互。与相关工作相比，本文的工作在无设置、单服务器、陡峭门限等强约束下提供了首个黑盒可行性结果，但作者指出当前方案主要具有理论意义，设计具体高效的方案是未来方向。

### 局限性与开放问题
本文的zkSNARK外包方案仅在半诚实服务器模型下证明安全性，抵抗恶意服务器的扩展是开放问题。门限签名方案的安全性证明依赖于代数群模型，消除此依赖是一个重要方向。此外，本文方案主要提供了可行性而非具体效率，设计实用化实现（如优化FHE层内运算）是重要的未来工作。

### 强关联论文

[BBHR18] Eli Ben-Sasson, Iddo Bentov, Yinon Horesh, Michael Riabzev. Fast reed-solomon interactive oracle proofs of proximity. **ICALP 2018**

[BGKS20] Eli Ben-Sasson, Lior Goldberg, Swastik Kopparty, Shubhangi Saraf. DEEP-FRI: Sampling outside the box improves soundness. **ITCS 2020**

[COS20] Alessandro Chiesa, Dev Ojha, Nicholas Spooner. Fractal: Post-quantum and transparent recursive proofs from holography. **EUROCRYPT 2020**

[GJM+24] Sanjam Garg, Abhishek Jain, Pratyay Mukherjee, Rohit Sinha, Mingyuan Wang, Yinuo Zhang. Hints: Threshold Signatures with Silent Setup. **IEEE S&P 2024**

[DCX+23] Sourav Das, Philippe Camacho, Zhuolun Xiang, Javier Nieto, Benedikt Bunz, Ling Ren. Threshold Signatures from Inner Product Argument: Succinct, Weighted, and Multi-Threshold. **CCS 2023**

[CKV10] Kai-Min Chung, Yael Kalai, Salil P. Vadhan. Improved delegation of computation using fully homomorphic encryption. **CRYPTO 2010**

[MRV+21] Silvio Micali, Leonid Reyzin, Georgios Vlachos, Riad S. Wahby, Nickolai Zeldovich. Compact certificates of collective knowledge. **IEEE S&P 2021**

[BHV+23] Rishabh Bhadauria, Carmit Hazay, Muthuramakrishnan Venkitasubramaniam, Wenxuan Wu, Yupeng Zhang. Private polynomial commitments and applications to mpc. **PKC 2023**

[BDFG21] Dan Boneh, Justin Drake, Ben Fisch, Ariel Gabizon. Halo infinite: Proof-carrying data from additive polynomial commitments. **CRYPTO 2021**

[BCS16] Eli Ben-Sasson, Alessandro Chiesa, Nicholas Spooner. Interactive oracle proofs. **TCC 2016-B**


## 关键词

+ 隐蔽值FRI多项式承诺技术
+ FHE私有计算委托可验证SNARK
+ zkSNARK单服务器私有委托
+ 无设置加权门限签名方案
+ 线性同态原语隐蔽证明方法