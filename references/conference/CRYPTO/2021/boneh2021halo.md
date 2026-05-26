---
title: "Halo Infinite: Proof-Carrying Data from Additive Polynomial Commitments"

标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 2021
modified: 2025-04-10 16:55:41
---

## Halo Infinite: Proof-Carrying Data from Additive Polynomial Commitments

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-030-84242-0_23)
+ [Major revision on archive](https://eprint.iacr.org/2020/1536)

## 作者

+ [Dan Boneh](Dan%20Boneh.md)
+ Justin Drake
+ [Ben Fisch](Ben%20Fisch.md)
+ [Ariel Gabizon](Ariel%20Gabizon.md)

## 笔记

### 背景与动机
多项式承诺方案（PCS）是构建简洁非交互式论证系统（SNARK）的核心原语，它允许证明者承诺一个多项式并在任意点证明其估值，且承诺和证明的大小需亚线性于多项式度数 [54]。然而，利用PCS构造更强大的证明携带数据（PCD）系统长期面临瓶颈：传统方法要求昂贵的SNARK递归，将完整验证器描述嵌入递归语句，导致只有当验证器本身足够高效（即SNARK）时才能实现PCD [15, 64]。Halo协议首次展示了无需SNARK即可构建PCD的替代路径，它利用Bulletproofs PCS内积论证的聚合性质 [21, 26]，但其构造依赖于对Fiat-Shamir变换的具体实例化，是一种启发式方案。本文旨在抽象和推广Halo方法背后的核心机制，证明从任何满足简单可加性质的PCS出发，甚至从仅具备高效线性组合方案的非加法PCS出发，均可系统性地构造PCD系统，从而填补从一般PCS到完全PCD之间的理论空白，并为未来新型PCS的工程实践提供统一蓝图 [1, 2]。这一成果表明，即使PCS本身不具备高效验证属性（如Bulletproofs），只要其满足本文定义的抽象可加性，就能可靠地构建出PCD。

### 相关工作
[19] Bootle等. Efficient Zero-Knowledge Arguments for Arithmetic Circuits in the Discrete Log Setting. **EUROCRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+Zero-Knowledge+Arguments+for+Arithmetic+Circuits+in+the+Discrete+Log+Setting)
> 核心思路：基于离散对数假设，通过内积论证实现承诺向量的子线性大小零知识证明。
> 局限与区别：其内积论证虽具备聚合性质，但本文将其抽象为加法PCS的公共聚合方案的一个实例，并指出该性质是更一般线性组合方案的特例。

[21] Bowe等. Halo: Recursive Proof Composition without a Trusted Setup. **Eprint 2019** [Google Scholar](https://scholar.google.com/scholar?q=Halo+Recursive+Proof+Composition+without+a+Trusted+Setup)
> 核心思路：首次提出利用Bulletproofs PCS的公共聚合性质构建无信任设置的递归证明（IVC），绕过传统SNARK递归。
> 局限与区别：Halo的构造是特例化的，直接针对Bulletproofs。本文将其核心机制抽象为一般性定理（定理5.2），证明任何加法PCS均可编译为具公共聚合能力的方案。

[26] Bünz等. Proof-Carrying Data from Accumulation Schemes. **Eprint 2020** [Google Scholar](https://scholar.google.com/scholar?q=Proof-Carrying+Data+from+Accumulation+Schemes)
> 核心思路：独立定义PCS累积方案，证明其可用于构建PCD，并给出从PCS累积到PCD的通用编译器。
> 局限与区别：本文的公共聚合方案满足累积方案定义，同时定义的私密聚合方案可构建线性大小的PCD。本文更深入地阐述了聚合方案与加法PCS间的理论联系（定理4.2和5.2）。

[54] Kate等. Constant-Size Commitments to Polynomials and Their Applications. **ASIACRYPT 2010** [Google Scholar](https://scholar.google.com/scholar?q=Constant-Size+Commitments+to+Polynomials+and+Their+Applications)
> 核心思路：引入多项式承诺概念，基于双线性对构造常数大小承诺和线性大小验证的评估证明。
> 局限与区别：本文指出KZG是典型的加法PCS，并分析其线性组合方案的摊销比率。同时，本文的公共聚合构造（定理5.2）不依赖双线性对，仅依赖一般同态PCS。

[23] Bünz等. Transparent SNARKs from DARK Compilers. **EUROCRYPT 2020** [Google Scholar](https://scholar.google.com/scholar?q=Transparent+SNARKs+from+DARK+Compilers)
> 核心思路：基于未知阶群（如类群）构建透明PCS，承诺和证明均为多项式大小。
> 局限与区别：DARK被标注为有界加法，其群加法操作仅有限次有效。本文的线性组合方案理论仍适用，但效率受限于有界性。

### 核心技术与方案
本文的核心贡献是定义并利用加法PCS的两个抽象性质——线性组合方案和私密/公共聚合方案，系统化地构建PCD系统。整个构造分为三个层次。

**线性组合方案与私密聚合方案**。首先，本文定义了一个线性组合方案，它允许证明者将多个多项式承诺线性组合成一个紧凑的新承诺，并能够打开这个新承诺以验证线性关系成立。关键创新在于定理4.2：任何具备线性组合方案的PCS都自动拥有一个私密聚合方案。该聚合方案通过一个两轮交互协议实现批量打开：第一轮，证明者发送一个承诺$C_q$，对应一个商多项式$q(X) = \sum_{i=1}^k \rho^{i-1} z_i f_i / z$，其中$z = \prod (X - \omega)$是零化多项式，$z_i = z / (X - \omega_i)$，$\rho$是挑战。第二轮，证明者构造多项式$g(X) = \sum \rho^{i-1} z_i(r) f_i(X) - z(r) q(X)$并在随机点$r$处打开$C_g$。安全性的核心在于引理4.7：由范德蒙矩阵$V$和非零矩阵$R$做哈达玛积后，所得矩阵以压倒性概率可逆，从而保证从$k$个不同挑战副本中提取正确多项式。私密聚合的通信为一个群元素加两个域元素，证明者计算量$O(k \log k)$，验证者$O(k \lambda)$。

**公共聚合方案**。公共聚合方案允许一个不知多项式具体值的聚合者将多个公开的证明摘要聚合。本文定理5.2给出一般构造：从任何加法PCS出发，通过编译器1（利用预计算基承诺将PCS转化为同态形式），再通过编译器2，该编译器本质上在Eval证明前附加一个同态原像知识证明协议。该协议通过递归二分递归约简同态原像问题，核心是图3所示的HPI协议。递归过程中，证明者发送一个中间承诺$y' = y_L + \alpha^2 y_R + \alpha y$，其中$\alpha$是挑战，递归规模减半，直到最终公开一个整数$x$。安全性证明依赖于分叉引理生成一个深度为$\log n$、分支因子为3的接受树，然后通过解线性方程组提取出同态原像（形如$[ [ x ] ]_g = t \cdot y$）。对于$\ell$个证明的公共聚合，通信为一个群元素加两个域元素，验证者$O(\ell \log \ell)$域操作加$O(\ell \lambda)$群操作。

**从聚合到PCD**。最后，文章阐明公共聚合方案满足Bünz等人定义的PCS累积方案，因此可直接套用其PCD编译器。此外，私密累积方案也可通过传递内部状态作为“建议”来构造PCD，虽然证明大小为线性，但递归语句大小仅依赖于累积验证器大小。这一构造不要求底层PCS验证高效，仅要求PCS具备加性。因此，从简单的Pedersen哈希函数出发即可实例化，大幅降低了递归阈值。

### 核心公式与流程

**[零化多项式与商多项式构造]**
$$z(X) := \prod_{\omega \in \Omega} (X - \omega), \quad z_i(X) := \prod_{\omega \in \bar{\Omega}_i} (X - \omega), \quad q(X) := \sum_{i=1}^k \rho^{i-1} z_i f_i / z$$
> 作用：定义用于批量打开的零化多项式$z$（包含所有评估点）和每个多项式各自的零化多项式$z_i$（排除该多项式的点），以及证明者构造的商多项式$q$，这是私密聚合中第一轮通信的主要内容，其承诺$C_q$是后续交互的基础。

**[私密聚合中验证者构造的线性组合]**
$$C_g := \sum_{i=1}^k \rho^{i-1} z_i(r) \cdot C_i - z(r) \cdot C_q, \quad g(r) = 0$$
> 作用：验证者通过公开数据计算聚合承诺$C_g$，并接受对$g$在$r$点值为0的证明。正确性保证了若所有原始多项式估值正确，则$g(r)=0$；安全性保证了从多个成功的交互副本可提取原始多项式。

**[HPI协议递归本轮的计算]**
$$y' := y_L + \alpha^2 y_R + \alpha y, \quad \mathbf{g}' := \mathbf{g}_R + \alpha \mathbf{g}_L, \quad \mathbf{x}' := \mathbf{x}_L + \alpha \mathbf{x}_R$$
> 作用：HPI协议中，证明者和验证者递归地将大小为$n$的同态原像问题约简为大小为$n/2$的问题。验证者只需计算$y'$的线性组合，无需计算$g'$，因为安全性分析仅依赖$y'$包含的信息。该递归最终公开一个整数$x$验证$x \cdot g_{leaf} = y_{leaf}$。

**[公开聚合编译后Eval*协议结构]**
$$\text{Step 1: HPI on } \phi_x, \quad \text{Step 2: Eval on } (C', x, y')$$
> 作用：转换后的Eval*协议将原PCS的Eval嵌入到一个两步协议中。第一步运行同态原像知识证明，确保证明者能提供$(t, \mathbf{v})$满足$\phi_x(\mathbf{v}) = (t \cdot C, t \cdot y)$；第二步运行原始Eval打开中间承诺$C'$。这种结构使基于Fiat-Shamir的公开聚合成为可能。

### 实验结果
本文未提供具体的性能基准测试数据，因为它是一篇理论构建论文，主要贡献在于定义抽象性质和证明充分性。然而，文章通过分析性表格给出了不同PCS方案的线性组合摊销比率，为性能评估提供了量化基础。例如，Bulletproofs、Dory和KZG的摊销比率为$1/\ell$，意味着每增加一个聚合的承诺，额外开销被均匀分摊。针对DARK的有界加性，同样给出了$1/\ell$的比率，同时注明其群运算存在次数上限。在验证者复杂度方面，Bulletproofs的Eval验证者开销为$\Omega(d)$（线性于度数），而线性组合验证者开销为$O_\lambda(\ell)$，因此在聚合大量承诺时摊销收益明显。Dory和KZG的Eval验证者分别为$\Omega(\log d)$和$\Omega(1)$，因此摊销空间较小。对于实际规模，论文指出后续工作[25]实现了基于简单Pedersen哈希的实例化，在递归阈值（递归语句大小）上取得了数量级缩减，但具体数值（如时间、内存、证明大小）未在本文中呈现。这些分析表明，本文方案特别适用于需要大量并行评估（如多次状态转换验证）且底层PCS验证开销（如Bulletproofs）主导的场景。

### 局限性与开放问题
本文的构造及其导出的PCD和IVC方案均依赖于对Fiat-Shamir变换的具体实例化，即使用碰撞哈希函数替代随机预言机，因此属于启发式安全，而非标准模型下的可证明安全 [33]。此外，对于非加性的PCS（如FRI），本文未提出通用转换，仅指出其可通过专门化的批处理协议实现类似效果。公开聚合方案中，证明者需要计算规模巨大的整数线性组合（$O(\lambda n)$），在低延迟场景下可能构成瓶颈。最后，虽然本文证明了存在性路径，但具体工程实现中的参数优化、具体哈希函数选择以及实际网络环境下的通信开销仍需进一步探索和验证。

### 强关联论文
[19] Bootle, J., Cerulli, A., Chaidos, P., Groth, J., Petit, C. Efficient Zero-Knowledge Arguments for Arithmetic Circuits in the Discrete Log Setting. **EUROCRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+Zero-Knowledge+Arguments+for+Arithmetic+Circuits+in+the+Discrete+Log+Setting)

[21] Bowe, S., Grigg, J., Hopwood, D. Halo: Recursive Proof Composition without a Trusted Setup. **Eprint 2019** [Google Scholar](https://scholar.google.com/scholar?q=Halo+Recursive+Proof+Composition+without+a+Trusted+Setup)

[22] Bünz, B., Bootle, J., Boneh, D., Poelstra, A., Wuille, P., Maxwell, G. Bulletproofs: Short Proofs for Confidential Transactions and More. **IEEE S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Bulletproofs+Short+Proofs+for+Confidential+Transactions+and+More)

[23] Bünz, B., Fisch, B., Szepieniec, A. Transparent SNARKs from DARK Compilers. **EUROCRYPT 2020** [Google Scholar](https://scholar.google.com/scholar?q=Transparent+SNARKs+from+DARK+Compilers)

[25] Bünz, B., Chiesa, A., Lin, W., Mishra, P., Spooner, N. Proof-Carrying Data without Succinct Arguments. **Eprint 2020** [Google Scholar](https://scholar.google.com/scholar?q=Proof-Carrying+Data+without+Succinct+Arguments)

[26] Bünz, B., Chiesa, A., Mishra, P., Spooner, N. Proof-Carrying Data from Accumulation Schemes. **Eprint 2020** [Google Scholar](https://scholar.google.com/scholar?q=Proof-Carrying+Data+from+Accumulation+Schemes)

[34] Chiesa, A., Ojha, D., Spooner, N. Fractal: Post-Quantum and Transparent Recursive Proofs from Holography. **EUROCRYPT 2020** [Google Scholar](https://scholar.google.com/scholar?q=Fractal+Post-Quantum+and+Transparent+Recursive+Proofs+from+Holography)

[54] Kate, A., Zaverucha, G.M., Goldberg, I. Constant-Size Commitments to Polynomials and Their Applications. **ASIACRYPT 2010** [Google Scholar](https://scholar.google.com/scholar?q=Constant-Size+Commitments+to+Polynomials+and+Their+Applications)

[57] Lee, J. Dory: Efficient, Transparent Arguments for Generalised Inner Products and Polynomial Commitments. **Eprint 2020** [Google Scholar](https://scholar.google.com/scholar?q=Dory+Efficient+Transparent+Arguments+for+Generalised+Inner+Products+and+Polynomial+Commitments)

[64] Valiant, P. Incrementally Verifiable Computation or Proofs of Knowledge Imply Time/Space Efficiency. **TCC 2008** [Google Scholar](https://scholar.google.com/scholar?q=Incrementally+Verifiable+Computation+or+Proofs+of+Knowledge+Imply+Time+Space+Efficiency)


## 关键词

+ Halo Infinite加法多项式承诺PCD
+ 证明携带数据SNARK递归避免
+ 同态PCS聚合线性组合承诺
+ 增量可验证计算Bulletproofs扩展
+ 无可信设置SNARK PCD新构造