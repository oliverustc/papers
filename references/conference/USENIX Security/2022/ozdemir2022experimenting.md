---
title: "Experimenting with collaborative zk-SNARKs: Zero-Knowledge proofs for distributed secrets"
标题简称:
论文类型: conference
会议简称: USENIX Security
发表年份: 2022
modified: 2025-04-13 14:36:11
---

## Experimenting with collaborative zk-SNARKs: Zero-Knowledge proofs for distributed secrets

## 发表信息

+ [原文链接](https://www.usenix.org/conference/usenixsecurity22/presentation/ozdemir)

## 作者

+ [Alex Ozdemir](Alex%20Ozdemir.md) 
+ [Dan Boneh](Dan%20Boneh.md) 

## 笔记

好的，这是根据您提供的论文全文生成的详尽结构化笔记。

### 背景与动机
零知识简洁的非交互式知识论证（zk-SNARKs）是一种强大的密码学原语，允许证明者向验证者证明其拥有满足某个公开NP关系的秘密数据（即证据），同时不泄露任何关于证据的信息。然而，传统的zk-SNARK设计假定所有秘密证据都由单一证明者持有，这限制了它在秘密数据分布于多方间的场景下的应用，例如多家医院联合统计医疗数据、多个信用机构联合计算个人信用评分等。一个自然的解决方案是将多个秘密数据持有方视为一个整体，让他们通过安全多方计算（MPC）协议协同运行单证明者的zk-SNARK证明生成算法。然而，直接使用通用MPC协议会导致性能灾难，因为二者各自的性能开销都是成千上万倍的，组合后会产生数百万倍的性能下降。本文旨在探索“协作式zk-SNARK”的可行性，目标是设计高效的多方协议，使得在安全前提下，多方向共同产生一个简洁证明的开销接近甚至与单方证明相当。

### 相关工作
[23] Bitansky et al. The hunting of the SNARK. **Journal of Cryptology 2017**
> 核心思路：首次系统性地定义了zk-SNARK的概念及其安全属性。
> 局限与区别：本文在其安全定义基础上，扩展定义了多方分布证据场景下的协作式zk-SNARK。

[66] Groth. On the size of pairing-based non-interactive arguments. **EUROCRYPT 2016**
> 核心思路：提出Groth16，一种证明尺寸极小（仅3个群元素）、验证极快的zk-SNARK。
> 局限与区别：本文以其为基础构造协作协议，并因其低乘法深度而被证明是极其“MPC友好”的。

[53] Gabizon et al. PLONK: Permutations over lagrange-bases for oecumenical noninteractive arguments of knowledge. **ePrint 2019**
> 核心思路：提出Plonk，一种拥有通用且可更新可信设置的zk-SNARK。
> 局限与区别：本文指出其证明生成中包含的PRODCHECK子协议在MPC中会产生大量通信，因而是MPC不友好的。

[40] Chiesa et al. Marlin: Preprocessing zkSNARKs with universal and updatable SRS. **EUROCRYPT 2020**
> 核心思路：提出Marlin，同样拥有通用且可更新可信设置的zk-SNARK。
> 局限与区别：本文以其为基础构造协作协议，其SUMCHECK子协议被证明具有良好的MPC适应性。

[41] Chiesa et al. Fractal: Post-quantum and transparent recursive proofs from holography. **EUROCRYPT 2020**
> 核心思路：提出Fractal，一种不依赖可信设置的透明zk-SNARK，基于哈希和低度测试。
> 局限与区别：本文指出，尽管其低度测试可适应MPC，但其核心的向量承诺（Merkle树）因哈希运算的非线性而在MPC中极其昂贵，除非以牺牲证明尺寸为代价。

[46] Damgård et al. Multiparty computation from somewhat homomorphic encryption. **CRYPTO 2012**
> 核心思路：提出SPDZ协议，一种支持恶意安全、允许最多N-1个参与方被腐化的MPC协议。
> 局限与区别：本文将其作为底层MPC协议，并针对椭圆曲线计算场景进行扩展，用于构建抗恶意多数方的协作式zk-SNARK。

[64] Goyal et al. Guaranteed output delivery comes free in honest majority MPC. **CRYPTO 2020**
> 核心思路：提出GSZ协议，一种高效的、支持诚实多数的MPC协议，基于Shamir秘密共享。
> 局限与区别：本文将其作为底层MPC协议，并扩展至椭圆曲线计算，用于构建抗恶意少数方的协作式zk-SNARK。

[76] Kate et al. Constant-size commitments to polynomials and their applications. **ASIACRYPT 2010**
> 核心思路：提出KZG多项式承诺方案，具有常数大小的承诺和求值证明。
> 局限与区别：本文巧妙地将KZG方案推广至秘密共享的多项式，使得多方可以各自在本地进行承诺和求值证明，无需交互，从而在多证明者环境下极其高效。

[4] Bar-Ilan and Beaver. Non-cryptographic fault-tolerant computing in constant number of rounds of interaction. **8th ACM PODC 1989**
> 核心思路：提出一种在常数轮内计算一系列部分乘积的技术。
> 局限与区别：本文使用该技术优化Plonk中的PRODCHECK协议，将原本需要O(n)轮的通信优化至常数轮，是实现Plonk协作化的关键。

### 核心技术与方案
本文的核心思路是将zk-SNARK的证明生成算法实现为一个安全的MPC协议。为此，作者提出了一套技术框架，通过优化底层代数操作的MPC开销，来提升协作证明的整体效率。

首先，作者将MPC协议（SPDZ和GSZ）直接扩展至椭圆曲线上的运算。他们观察到，椭圆曲线的加法、标量乘法等操作可以“线性地”作用于秘密共享的份额上。这意味着，如果一个运算对于秘密共享的标量是线性的（例如，椭圆曲线的加法对标量是线性的），那么在MPC中计算该运算时，每个参与方只需要在本地对自己持有的份额执行相同的操作，无需任何通信。这个特性被（线性秘密共享下的）多方证明者利用，使得核心的计算瓶颈，如多标量乘法和快速傅里叶变换，能够以共享方式廉价的执行：与单方计算的成本几乎相同。

其次，作者将KZG多项式承诺方案自然扩展至秘密共享的多项式。设一个多项式$f$的系数以线性秘密共享方案表示为$[f]$。那么，对共享多项式的承诺计算为$c \leftarrow \sum_{i=0}^d f_i \cdot (\alpha^i \cdot g_1)$，其中$\alpha^i \cdot g_1$是公开参数。由于这是一个线性运算（MSM），每个参与方可以用自己的系数份额$f_i^{(j)}$在本地计算出承诺的份额$c^{(j)}$，然后合起来就是完整的承诺$c$。同样，对于KZG的求值证明，需要计算多项式除法$(q, r) \leftarrow f / (X-x)$。因为除数是公开的，这是一个线性运算，每个参与方可以在本地计算其多项式份额的除法，得到的商和余数份额即为正确结果。这证明了对共享多项式，可以在没有交互的情况下生成正确的承诺和求值证明。

最后，针对不同SNARK中的特定子协议，作者设计了特定的MPC优化。对于Plonk中的PRODCHECK，需要计算一系列部分乘积$t_i := \prod_{j=1}^i f(\omega^j)$。作者采用Bar-Ilan和Beaver的技术，通过引入随机数$r_i$并在常数轮通信后计算出所有$t_i$，将原本需要O(n)轮的通信优化为常数轮。对于Marlin中的SUMCHECK，其核心操作是验证$f = X \cdot f' + c/|\Omega|$，由于$f'$的系数直接来自$f$，因此整个协议的MPC实现可以直接复用KZG承诺方案对共享多项式的操作，非常直接。对于Fractal，其基于哈希的向量承诺在MPC中开销过大，作者提出一种权衡方案：为每个多项式份额单独生成一个Merkle承诺，这样证明者之间的计算没有额外负担，但代价是证明尺寸和验证时间会随参与方数量N线性增长。

最终，本文给出了三个系统的渐进复杂度。在计算复杂度方面，对于Groth16、Marlin和Plonk，其主要运算（MSM, FFT，多项式除法）在MPC中基本没有额外开销；SPDZ协议因为要处理MAC，计算量约为单方的两倍，而GSZ协议与单方相当。在通信复杂度方面，对于$n$个约束的R1CS系统，Groth16和Marlin的通信量为$O(n)$个域元素（主要用于SPDZ中预处理的乘法三元组或GSZ中的乘法检查），而Plonk因PRODCHECK需要额外的通信，常数项更大。具体来说，对于2方SPDZ下的Groth16，通信量约为$4n$个域元素。文章还证明了一个下界：对于诚实正确的协作证明，如果证据是加法秘密共享的，那么至少需要$\Omega(n)$的通信量，这与通信复杂度的经典困难问题DISJ相关。

### 核心公式与流程

**[KZG多项式承诺的核心性质]**
$$e(\pi, \alpha \cdot g_2 - x \cdot g_2) = e(c - y \cdot g_1, g_2)$$
> 作用：验证关于多项式$f$在点$x$处值为$y$的求值证明$\pi$，其中$c$是$f$的承诺，$\alpha$是陷阱门。本文将此验证过程作为黑盒使用，不参与MPC计算。

**[多证明者KZG承诺协议 PC.Commit']**
$$c^{(i)} \leftarrow \sum_{j=0}^{d} f_j^{(i)} \cdot (\alpha^j \cdot g_1)$$
> 作用：每个参与方$i$使用自己多项式$f^{(i)}$的系数份额，通过本地多标量乘法计算出承诺的份额$c^{(i)}$。由于运算线性，这些份额合起来就是正确承诺$c$。

**[多证明者KZG求值证明协议 PC.Prove']**
$$q^{(i)}, r^{(i)} \leftarrow f^{(i)} / (X - x)$$
$$\pi^{(i)} \leftarrow \sum_{j=0}^{d} q_j^{(i)} \cdot (\alpha^j \cdot g_1)$$
> 作用：每个参与方$i$在本地对其多项式份额$f^{(i)}$进行多项式除法（模$X-x$），得到商$q^{(i)}$和余数$r^{(i)}$，然后再次通过本地计算得到证明份额$\pi^{(i)}$。整个过程无需交互。

**[常数轮计算部分乘积的技术]**
$$t_i := \prod_{j=0}^{i} f(\omega^j)$$
$$步骤1: [r_0], [r_0^{-1}], ..., [r_n], [r_n^{-1}] \leftarrow 随机数份额$$
$$步骤2: 公开计算并打开 [r_{i-1} \cdot t_i \cdot r_i^{-1}]$$
$$步骤3: 计算 [t_i] = (\prod_{j=1}^{i} t_j') \cdot [r_0^{-1} \cdot r_i]$$
> 作用：用于优化Plonk的PRODCHECK子协议。通过在步骤2中一次性打开所有“随机扰动的”中间乘积，将原本需要O(n)轮通信的计算降为常数轮，其中$t_j'$是公开值。

### 实验结果
实验使用谷歌云平台的n2-standard-2实例，单核，3Gb/s网络，对Groth16、Marlin、Plonk进行了评测。核心结论是，在高速网络下，协作证明的开销出奇地低。对于2^20个约束的大型电路，基于GSZ协议的3方协作（抗恶意少数方）的证明时间与单方证明者几乎完全相同；而基于SPDZ协议的2方协作（抗恶意多数方）的证明时间仅为单方证明的约2倍。这种性能得益于MPC友好的设计：SPDZ因维护MAC认证信息，计算量翻倍；而GSZ的计算量与单方相同。对于小规模电路（约束数小于2^10），网络往返延迟（毫秒级）占主导，协作协议比单方慢。随着参与方数量增加，GSZ由于乘法检查的通信轮数与约束数量对数相关，性能会迅速劣化，而SPDZ则因其常数轮通信的特性，性能退化较慢。在低带宽网络（如1Mb/s）下，通信成为瓶颈，协作方案性能显著下降，其中Plonk因其更大的通信量，性能最差。以成本计，在云服务上生成一个百万约束的2方协作Groth16证明，预估成本约为3美分，而单方证明约为0.5美分，两者均在可接受范围内。

### 局限性与开放问题
本文的构建依赖于（线性）秘密共享方案和特定的MPC协议（SPDZ/GSZ），这意味着证明者的证明过程是一个算术电路，无法处理分支或基于秘密数据的条件访问等非电路程序。此外，文章证明了通信量的下界：对于加法秘密共享的证据，协作证明至少需要与约束数n线性相关的通信量，这在根本上限制了进一步降低通信成本的空间。最后，本文构造的协作证明会泄露证据是否满足关系这一比特信息，对于某些特殊关系，这可能被恶意方用于推断其他方的秘密信息。

### 强关联论文
[66] Groth. On the size of pairing-based non-interactive arguments. **EUROCRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=On+the+size+of+pairing-based+non-interactive+arguments)

[53] Gabizon et al. PLONK: Permutations over lagrange-bases for oecumenical noninteractive arguments of knowledge. **IACR ePrint 2019** [Google Scholar](https://scholar.google.com/scholar?q=PLONK+Permutations+over+lagrange-bases+for+oecumenical+noninteractive+arguments+of+knowledge)

[40] Chiesa et al. Marlin: Preprocessing zkSNARKs with universal and updatable SRS. **EUROCRYPT 2020** [Google Scholar](https://scholar.google.com/scholar?q=Marlin+Preprocessing+zkSNARKs+with+universal+and+updatable+SRS)

[41] Chiesa et al. Fractal: Post-quantum and transparent recursive proofs from holography. **EUROCRYPT 2020** [Google Scholar](https://scholar.google.com/scholar?q=Fractal+Post-quantum+and+transparent+recursive+proofs+from+holography)

[46] Damgård et al. Multiparty computation from somewhat homomorphic encryption. **CRYPTO 2012** [Google Scholar](https://scholar.google.com/scholar?q=Multiparty+computation+from+somewhat+homomorphic+encryption)

[64] Goyal et al. Guaranteed output delivery comes free in honest majority MPC. **CRYPTO 2020** [Google Scholar](https://scholar.google.com/scholar?q=Guaranteed+output+delivery+comes+free+in+honest+majority+MPC)

[76] Kate et al. Constant-size commitments to polynomials and their applications. **ASIACRYPT 2010** [Google Scholar](https://scholar.google.com/scholar?q=Constant-size+commitments+to+polynomials+and+their+applications)

[4] Bar-Ilan and Beaver. Non-cryptographic fault-tolerant computing in constant number of rounds of interaction. **8th ACM PODC 1989** [Google Scholar](https://scholar.google.com/scholar?q=Non-cryptographic+fault-tolerant+computing+in+constant+number+of+rounds+of+interaction)


## 关键词

+ 协作zk-SNARK分布式证明
+ 多方安全计算MPC友好性
+ 分布式秘密见证联合证明
+ 基于配对的zk-SNARK优化
+ 恶意多数安全证明协议
+ 配对群多标量乘法MPC
