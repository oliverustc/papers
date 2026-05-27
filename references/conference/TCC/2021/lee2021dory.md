---
title: "Dory: Efficient, transparent arguments for generalised inner products and polynomial commitments"
doi: 10.1007/978-3-030-90453-1_1
标题简称:
论文类型: conference
会议简称: TCC
发表年份: 2021
created: 2025-04-28 16:53:19
modified: 2025-04-28 16:55:15
---
## Dory: Efficient, transparent arguments for generalised inner products and polynomial commitments

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-030-90453-1_1)

## 作者

+ [Jonathan Lee](Jonathan%20Lee.md)
## 笔记

### 背景与动机
透明设置的零知识简洁论证在密码学中具有重要地位，尤其是用于Rank-1约束系统可满足性的zkSNARKs。通用策略将证明分为两个阶段：信息论论证将存在满足性赋值的证明简化为对多项式求值承诺的一致性检查，然后使用具有亚线性验证时间的计算合理论证来证明这些求值承诺的正确性。Dory论文关注的是后一类论证，即内积论证或多项式承诺方案。此前透明多项式承诺方案存在显著瓶颈：基于离散对数的方案（如Hyrax）需要$\Omega(n^{1/2})$的验证者计算和大小相似的承诺；基于Reed-Solomon交互式预言机证明的方案（如Fractal）因底层IOPP的可靠性误差较大而需要大量重复；基于未知阶群的方案（如Supersonic）群运算速度远慢于曲线运算。Dory旨在填补这一空白，通过新的技术实现对数复杂度的验证者计算，同时保持透明设置和可证明安全性，为高效、透明的多项式承诺提供新的可能性。

### 相关工作

[13] Bootle等. Efficient zero-knowledge arguments for arithmetic circuits in the discrete log setting. **EUROCRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+zero-knowledge+arguments+for+arithmetic+circuits+in+the+discrete+log+setting)
> 核心思路：提出了基于离散对数困难性的内积论证，通信复杂度为对数，但验证者计算为线性。
> 局限与区别：验证者计算量仍为线性，Dory通过利用配对群的结构保持承诺实现了对数验证者。

[15] Bünz等. Bulletproofs: Short proofs for confidential transactions and more. **S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Bulletproofs:+Short+proofs+for+confidential+transactions+and+more)
> 核心思路：改进了内积论证，将其应用于机密交易，通信复杂度为对数。
> 局限与区别：同样具有线性验证者计算，Dory在此基础上引入结构化承诺键和并行归约实现亚线性验证。

[17] Bünz等. Proofs for inner pairing products and applications. **ePrint 2019** [Google Scholar](https://scholar.google.com/scholar?q=Proofs+for+inner+pairing+products+and+applications)
> 核心思路：将内积论证扩展到配对群，利用Kate承诺结构化承诺键实现亚线性验证，但需要可信设置。
> 局限与区别：依赖可信设置和知识指数假设，Dory在透明设置下实现了相似的渐近性能。

[34] Wahby等. Doubly-efficient zkSNARKs without trusted setup. **S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Doubly-efficient+zkSNARKs+without+trusted+setup)
> 核心思路：提出了Hyrax，基于矩阵承诺和内积论证实现多项式承诺，承诺大小为$\Omega(n^{1/2})$。
> 局限与区别：承诺大小和验证者计算均为亚线性但不够理想，Dory实现了常数大小的承诺和对数验证者。

[27] Kate等. Constant-size commitments to polynomials and their applications. **ASIACRYPT 2010** [Google Scholar](https://scholar.google.com/scholar?q=Constant-size+commitments+to+polynomials+and+their+applications)
> 核心思路：提出了常数大小的多项式承诺，但需要可信设置和知识指数假设。
> 局限与区别：依赖不可证的知识指数假设，Dory在透明设置下实现了类似的常数大小承诺。

[31] Setty. Spartan: efficient and general-purpose zkSNARKs without trusted setup. **CRYPTO 2020** [Google Scholar](https://scholar.google.com/scholar?q=Spartan:+efficient+and+general-purpose+zkSNARKs+without+trusted+setup)
> 核心思路：提出了独立的通用多项式承诺方案，基于离散对数实现线性证明者，亚线性承诺和证明大小。
> 局限与区别：验证者计算仍为$O(n^{1/2})$，Dory实现了对数验证者，且批处理时边际成本更低。

[14] Bowe等. Recursive proof composition without a trusted setup. **ePrint 2019** [Google Scholar](https://scholar.google.com/scholar?q=Recursive+proof+composition+without+a+trusted+setup)
> 核心思路：提出了通过"折叠"技术实现递归组合，优化了内积论证的验证者计算。
> 局限与区别：主要关注递归组合，Dory将类似思想用于构造对数复杂度的内积论证。

[11] Block等. Time- and space-efficient arguments from groups of unknown order. **CRYPTO 2021** [Google Scholar](https://scholar.google.com/scholar?q=Time-+and+space-efficient+arguments+from+groups+of+unknown+order)
> 核心思路：基于未知阶群构造Diophantine论证，属于DARK-GUO类方案。
> 局限与区别：群运算速度远慢于曲线运算（约270倍），Dory使用配对群实现更优的实践性能。

[34] Wahby等. Doubly-efficient zkSNARKs without trusted setup. **S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Doubly-efficient+zkSNARKs+without+trusted+setup)
> 核心思路：Hyrax使用矩阵承诺策略，将多项式表示为矩阵的向量-矩阵-向量乘积。
> 局限与区别：需要$O(n^{1/2})$大小的承诺和验证者计算，Dory通过对数内积论证改进。

### 核心技术与方案
本文提出Dory，一种透明的内配对乘积论证系统，并在此基础上构建多项式承诺方案。核心技术层次分为四个部分。

**1. 标量乘积协议**
该协议处理长度为1的内积情况。Prover持有$v_1 \in \mathbb{G}_1$，$v_2 \in \mathbb{G}_2$以及各自的盲化因子，证明$C = e(v_1, v_2) + r_C e(H_1, H_2)$。协议通过将验证者挑战$c$和$d$组合进检查方程，将通常的三个配对检查合并为一个，降低了通信开销。安全性基于SXDH假设，通过树可提取性证明$(9, 9/|\mathbb{F}|)$次自适应。

**2. Dory-Reduce**
这是核心的递归归约步骤。给定关于长度为$n=2^m$向量的三个声明$(C, D_1, D_2)$，通过Prover发送4个额外的承诺$(D_{1L}, D_{1R}, D_{2L}, D_{2R})$和两个交叉项$(C_+, C_-)$，结合验证者的两个挑战$\beta$和$\alpha$，归约为关于长度为$n/2$向量的新声明$(C', D_1', D_2')$。关键创新在于交换了折叠和组合两个阶段的顺序，使得Prover只需发送6个$\mathbb{G}_T$元素而非8个。安全性基于SXDH下承诺的绑定性和树可提取性。

**3. Dory-Innerproduct**
将Dory-Reduce递归应用$m$次，将长度为$2^m$的向量归约到长度为1，然后调用标量乘积协议。通信量为$6 \log n$个$\mathbb{G}_T$元素加常数个额外元素。Prover的计算主导于总大小为$6n$的多配对运算和$O(n)$域运算。验证者计算可以通过预先计算并延迟执行（deferred computation）汇总为一个大小为$9m+9$的$\mathbb{G}_T$多指数运算加常数个配对，实现$O(\log n)$的验证者复杂度。

**4. 多项式承诺的构建**
对于任意多元多项式，通过将其重新表述为多线性多项式，进而表示为向量-矩阵-向量乘积$f(\vec{x}) = \vec{L}^T M \vec{R}$，其中$\vec{L}, \vec{R}$具有乘法结构（Kronecker乘积形式）。Dory-PC-RE协议通过以下步骤证明：Prover提交矩阵$M$（使用双层同态承诺），计算$\vec{v} = \vec{L}^T M$，并通过Dory-Innerproduct证明$T = \langle \vec{T}', \Gamma_2 \rangle$，$E_1 = \langle \vec{L}, \vec{T}' \rangle$和$E_2 = \langle \vec{v}, \vec{R} \rangle \Gamma_{1,\text{fin}}$的正确性。Dory-PC通过额外采样一个随机点进行两次Dory-PC-RE，实现了完全的可提取性而非仅随机求值可提取性。

**批处理**：利用Batch-Innerproduct协议，可以将多个内积声明合并为一个。对于$\ell$个批处理，验证者骤降为$O(\ell + \log n)$个指数运算和$O(\ell \log n)$个域运算，边际代价随$\ell$增加而显著降低。

### 核心公式与流程

**[Dory-Reduce协议]**
$$
\begin{array}{l}
\mathcal{P} \to \mathcal{V}: D_{1L}, D_{1R}, D_{2L}, D_{2R} \\
\mathcal{V} \to \mathcal{P}: \beta \\
\mathcal{P} \to \mathcal{V}: C_+, C_- \\
\mathcal{V} \to \mathcal{P}: \alpha \\
\mathcal{V}: C' = C + \chi + \beta D_2 + \beta^{-1} D_1 + \alpha C_+ + \alpha^{-1} C_- \\
\quad D_1' = \alpha D_{1L} + D_{1R} + \alpha\beta \Delta_{1L} + \beta \Delta_{1R} \\
\quad D_2' = \alpha^{-1} D_{2L} + D_{2R} + \alpha^{-1}\beta^{-1} \Delta_{2L} + \beta^{-1} \Delta_{2R}
\end{array}
$$
> 作用：将长度为$n$的内积声明归约到长度为$n/2$的内积声明，通信量为6个$\mathbb{G}_T$元素。

**[标量乘积协议验证方程]**
$$
e(E_1 + d\Gamma_1, E_2 + d^{-1}\Gamma_2) = \chi + R + cQ + c^2 C + dP_2 + dcD_2 + d^{-1}P_1 + d^{-1}cD_1 - (r_3 + dr_2 + d^{-1}r_1)H_T
$$
> 作用：通过将三个配对检查合并为一个，将长度为1的标量乘积声明的验证简化为单个配对方程。

**[多项式评估的向量-矩阵-向量表示]**
$$
f(x_1, \dots, x_\ell) = \sum_{(i_1,\dots,i_r)\in\{1,2\}^r} T_{i_1,\dots,i_r} \prod_{j=1}^r x_j^{i_j-1} = \vec{L}^T M \vec{R}
$$
> 作用：将任意多元多项式转化为多线性多项式，再表示为Kronecker乘积向量与矩阵的乘积形式。

**[延迟计算后验证者的核心计算]**
$$
C \leftarrow C + \chi + \beta_0 D_2^0 + \beta_0^{-1} D_1^0 + \sum_{j=0}^{m-1}(\alpha_j C_+^j + \alpha_j^{-1} C_-^j) + \cdots
$$
> 作用：通过将递归归约的计算延迟到最终检查，验证者的群运算简化为单个$O(m)$大小的多指数运算。

**[批处理内积的折叠]**
$$
\mathcal{V}: D_1'' \leftarrow \gamma D_1 + D_1', \quad D_2'' \leftarrow \gamma D_2 + D_2', \quad C'' \leftarrow \gamma^2 C + \gamma X + C'
$$
> 作用：将两个内积声明$(C, D_1, D_2)$和$(C', D_1', D_2')$通过验证者挑战$\gamma$合并为一个声明$(C'', D_1'', D_2'')$。

### 实验结果
实验在AMD Ryzen 5 3600 CPU（3.6GHz，16GB RAM）单核上运行，使用BLS12-381曲线（通过blstrs实现）和Spartan库作为基线。对于$n=2^{20}$的稠密多线性多项式：承诺大小为192字节（固定）；求值证明约18 kB；证明者生成时间3秒；验证者验证时间25毫秒。与Spartan-PC（基于Curve25519的离散对数方案）对比：承诺时间常数2.7倍慢，匹配BLS12-381与Curve25519的算术速度比；证明者时间对$n=2^{20}$时约30%慢，但对于$n=2^{28}$时Dory更快（因Spartan-PC的$O(n)$域运算成为瓶颈）；验证者时间对$n\geq 2^{24}$时Dory更优（$O(\log n)$ vs $O(n^{1/2})$）；通信量方面，Dory证明大小约16 kB，是Spartan-PC的约24倍（源自BLS12-381的配对群元素大小），但对$n=2^{18}$时Dory单次求值证明已小于Spartan-PC的单次承诺大小。批处理时，对于$n=2^{20}$：批处理256个求值时，每个求值的边际成本为<1 kB通信，300毫秒证明者时间和1毫秒验证者时间；批处理使验证者计算节省常数11.5倍，通信节省$2\log n$倍。

### 局限性与开放问题
Dory的证明大小虽为对数，但常数因子较大（BLS12-381上约16 kB），对于一些对通信敏感的应用（如区块链）可能是瓶颈。目前的实现基于单一配对友好曲线，未来可探索更高效的曲线或压缩技术。方案的完全可提取性需要采样$O(n^2)$个随机点，这在实践中可能带来额外的开销；对于仅需随机求值可提取性的应用可接受，但对于需要完全知识证明的场景仍需优化。

### 强关联论文

[13] Bootle等. Efficient zero-knowledge arguments for arithmetic circuits in the discrete log setting. **EUROCRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+zero-knowledge+arguments+for+arithmetic+circuits+in+the+discrete+log+setting)

[15] Bünz等. Bulletproofs: Short proofs for confidential transactions and more. **S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Bulletproofs:+Short+proofs+for+confidential+transactions+and+more)

[17] Bünz等. Proofs for inner pairing products and applications. **ePrint 2019** [Google Scholar](https://scholar.google.com/scholar?q=Proofs+for+inner+pairing+products+and+applications)

[27] Kate等. Constant-size commitments to polynomials and their applications. **ASIACRYPT 2010** [Google Scholar](https://scholar.google.com/scholar?q=Constant-size+commitments+to+polynomials+and+their+applications)

[31] Setty. Spartan: efficient and general-purpose zkSNARKs without trusted setup. **CRYPTO 2020** [Google Scholar](https://scholar.google.com/scholar?q=Spartan:+efficient+and+general-purpose+zkSNARKs+without+trusted+setup)

[34] Wahby等. Doubly-efficient zkSNARKs without trusted setup. **S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Doubly-efficient+zkSNARKs+without+trusted+setup)

[14] Bowe等. Recursive proof composition without a trusted setup. **ePrint 2019** [Google Scholar](https://scholar.google.com/scholar?q=Recursive+proof+composition+without+a+trusted+setup)

[11] Block等. Time- and space-efficient arguments from groups of unknown order. **CRYPTO 2021** [Google Scholar](https://scholar.google.com/scholar?q=Time-+and+space-efficient+arguments+from+groups+of+unknown+order)

[2] Abe等. Structure-preserving signatures and commitments to group elements. **CRYPTO 2010** [Google Scholar](https://scholar.google.com/scholar?q=Structure-preserving+signatures+and+commitments+to+group+elements)

[23] Groth. Efficient zero-knowledge arguments from two-tiered homomorphic commitments. **ASIACRYPT 2011** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+zero-knowledge+arguments+from+two-tiered+homomorphic+commitments)


## 关键词

+ 透明设置多项式承诺
+ 内积论证系统Dory
+ SXDH假设安全归约
+ 配对群多重指数运算
+ 批处理多项式评估验证
+ 简洁论证系统效率
