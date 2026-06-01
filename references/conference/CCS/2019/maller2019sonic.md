---
title: "Sonic: Zero-Knowledge SNARKs from Linear-Size Universal and Updatable Structured Reference Strings"
doi: 10.1145/3319535.3339817
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2019
modified: 2025-04-15 16:37:28
created: 2025-04-08 17:28:08
---
## Sonic: Zero-Knowledge SNARKs from Linear-Size Universal and Updatable Structured Reference Strings

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3319535.3339817)

## 作者

+ [Mary Maller](Mary%20Maller.md)
+ [Sean Bowe](Sean%20Bowe.md)
+ [Markulf Kohlweiss](Markulf%20Kohlweiss.md)
+ [Sarah Meiklejohn](Sarah%20Meiklejohn.md)
## 笔记

### 背景与动机
零知识证明在隐私计算和区块链等领域有广泛应用，但在系统落地中面临关键矛盾：既需要简洁的证明和高效的验证（如zk-SNARKs的常量级开销），又希望避免可信设置带来的安全风险和部署灵活性损失。传统的zk-SNARKs需要为每个关系单独执行一次可信设置，且SRS无法复用；即便通过多方安全计算降低单一信任假设，生成的新参数仍绑定于特定电路，任何电路修改都需要重新执行代价高昂的初始化。Groth等人[46]提出的通用且可更新的SRS方案突破了这一瓶颈，但该方案的SRS大小与电路大小的平方成正比，在Zcash这类拥有数亿乘法门的电路中，SRS将达到TB量级，完全不切实际。本文设计并实现了一个新的zk-SNARK方案Sonic，其SRS大小与支持的电路规模呈线性关系，并且是通用和可更新的，同时保持了常量级的证明大小和验证时间，从而首次使大规模、分布式的持续设置成为现实。

### 相关工作
[22] Bootle 等. Efficient zero-knowledge arguments for arithmetic circuits in the discrete log setting. **EUROCRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+zero-knowledge+arguments+for+arithmetic+circuits+in+the+discrete+log+setting)
> 核心思路：设计了一种基于离散对数假设的双变量多项式方程来表示算术电路的可满足性。
> 局限与区别：该构造的验证开销与电路规模呈线性关系，且未提供通用可更新SRS。Sonic直接采用了该多项式方程作为约束系统的核心表达方式。

[26] Bünz 等. Bulletproofs: Short proofs for confidential transactions and more. **IEEE S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Bulletproofs+Short+proofs+for+confidential+transactions+and+more)
> 核心思路：提出基于离散对数的、无需可信设置的对数大小证明，具有很好的隐私保护。
> 局限与区别：证明验证时间随电路规模线性增长，对于大型电路的验证开销较高。Sonic的验证是常量时间，且具有更优的批量验证性。

[45] Groth. On the size of pairing-based non-interactive arguments. **EUROCRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=On+the+size+of+pairing-based+non-interactive+arguments)
> 核心思路：设计了当时最实用的zk-SNARK，证明只有3个群元素，验证仅需常量级配对操作。
> 局限与区别：该方案需要为每个电路执行一次专用的可信设置，SRS不可通用、不可更新。Sonic实现了通用且可更新的SRS，同时保持了与之竞争的验证效率。

[46] Groth 等. Updatable and universal common reference strings with applications to zk-snarks. **CRYPTO 2018** [Google Scholar](https://scholar.google.com/scholar?q=Updatable+and+universal+common+reference+strings+with+applications+to+zk-snarks)
> 核心思路：首次形式化定义了SRS的可更新性和通用性，并基于此构造了一个zk-SNARK方案。
> 局限与区别：该方案的全局SRS大小为O(n²)，对于大规模电路不切实际。Sonic在相同功能条件下，将SRS大小降低到O(n)。

[37] Fuchsbauer 等. The algebraic group model and its applications. **CRYPTO 2018** [Google Scholar](https://scholar.google.com/scholar?q=The+algebraic+group+model+and+its+applications)
> 核心思路：提出代数群模型（AGM），作为标准模型和通用群模型之间的折衷，允许更强的约简证明。
> 局限与区别：本文不依赖更复杂的知识假设（如KOE），而是在AGM下证明安全性，这避免了在第二个源群中引入证明元素，从而提高了效率。

[50] Kate 等. Constant-size commitments to polynomials and their applications. **ASIACRYPT 2010** [Google Scholar](https://scholar.google.com/scholar?q=Constant-size+commitments+to+polynomials+and+their+applications)
> 核心思路：提出基于配对的单变量多项式承诺方案，承诺和证明均为常量级。
> 局限与区别：Sonic将其框架适配到双变量多项式，通过仅对形如 ∑ a_i X^i Y^i 的特殊多项式进行单变量承诺，并利用第二个变量y作为公开挑战，在协议执行过程中确定，从而将双变量问题转化为单变量的承诺验证。

[58] Papamanthou 等. Signatures of correct computation. **TCC 2013** [Google Scholar](https://scholar.google.com/scholar?q=Signatures+of+correct+computation)
> 核心思路：提出了面向多变量多项式的签名，可用于验证计算的正确性。
> 局限与区别：若直接用于Sonic的双变量高阶多项式，会导致SRS为O(n²)。Sonic提出了两种更高效的特殊构造：一种是使用排列论和累乘论证的简洁构造，另一种是借助“帮助者”实现实用化的高效批量验证构造。

[61] Wahby 等. Doubly-efficient zkSNARKs without trusted setup. **IEEE S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Doubly-efficient+zkSNARKs+without+trusted+setup)
> 核心思路：使用并行化的sum-check协议处理电路，特别适合具有高并行性和小见证（如Merkle树包含证明）的电路。
> 局限与区别：该方案没有通用可更新的SRS，其安全性基于离散对数假设，且对一般电路的效率不如专为常量验证设计的zk-SNARKs。

[13] Ben-Sasson 等. Aurora: Transparent succinct arguments for R1CS. **IACR ePrint 2018/828** [Google Scholar](https://scholar.google.com/scholar?q=Aurora+Transparent+succinct+arguments+for+R1CS)
> 核心思路：使用基于Reed-Solomon码的交互式谕言证明（IOP）技术，实现无需设置的后量子安全简洁证明。
> 局限与区别：Aurora的证明验证时间与电路大小成线性关系，且证明大小仍在数百KB量级。Sonic在配对友好曲线上实现了更优的恒定验证时间和更小的证明体。

### 核心技术与方案
Sonic的整体架构建立在两个核心密码学原语之上：一个多项式承诺方案和一个“正确计算签名”（Signature of Correct Computation）。证明过程首先将整个电路的约束系统压缩成一个双变量多项式方程，该方程来自于Bootle等人的工作[22]。约束系统包含乘法约束（a ∘ b = c）和线性约束（a·u_q + b·v_q + c·w_q = k_q），论文通过引入一个形式变量Y将它们合并成一个多项式等式。具体地，在定义辅助多项式u_i(Y), v_i(Y), w_i(Y)和k(Y)后，约束系统的可满足性等价于形如a·u(Y) + b·v(Y) + c·w(Y) + ∑ a_i b_i (Y^i + Y^{-i}) - k(Y) = 0的等式恒成立。接着，Sonic利用一个名为r(X,Y)的线性化多项式和一个名为s(X,Y)的公开多项式，构造了目标多项式t(X,Y) = r(X,1) * (r(X,Y) + s(X,Y)) - k(Y)，使得t(X,Y)的零次项系数恰好是上述约束等式的左边。因此，证明系统只需要证明对于随机挑战y，多项式t(X,y)的零次项系数为零。

为了实现这一点，Sonic协议使用了三步交互：
1. **多项式承诺**：证明者构造多项式r(X,Y)，并承诺单变量多项式r(X,1) (记为承诺R) 和随后一个根据挑战y计算出的t(X,y) (记为承诺T)。承诺方案使用了Kate等人的方案的变种，能对带负指数的Laurent多项式进行常量大小的承诺和验证。这里的SRS包含{g^{x^i}, g^{αx^i}, h^{x^i}, h^{αx^i}}等项，osize为O(d)，其中d是电路的深度。
2. **挑战与打开**：验证者发送随机挑战y和z。证明者打开承诺R，提供r(z,1)和r(zy,1)（因为r(zy,1) = r(z,y)），并打开承诺T，提供t(z,y)。
3. **验证方程**：验证者检查正确的计算签名（scV）以确保s(z,y)正确，然后检查t(z,y) = r(z,1) * (r(z,y) + s(z,y)) - k(y)，并验证所有多项式承诺的打开证明（pcV）。如果所有检查通过，则接受。

该协议的安全性依赖于两个核心组件的安全性：多项式承诺方案和正确计算签名。多项式承诺方案的评估绑定性和有界多项式可提取性在代数群模型（AGM）下基于q-DLOG假设被证明。证明通过构造一个代数敌手，其输出群元素携带代数表示，进而约简到求解q-DLOG问题。本文证明，如果一个代数敌手可以输出有效的打开，那么它必定知道一个满足特定约束的Laurent多项式，或者可以解决一个计算Diffie-Hellman实例。协议的整体证人扩展仿真性质则基于正确计算签名的可靠性：它确保s = s(z,y)精确成立，在此基础上，通过多项式恒等原理（一次随机挑战下根的数量有限），系统保证了如果t = a(b+s) - k(y)对于足够多的随机y成立，则整个原始的约束系统必然被满足。

协议实现了子版本零知识：即即使恶意验证者完全生成了SRS，他仍然无法区分真实证明与模拟证明。模拟证明通过利用从SRS中提取的trapdoor（g^α）来生成随机盲化多项式，并与真实证明中的分布计算上不可区分。文章提供了零知识性和知识可靠性的完整证明大纲。

在渐进复杂度方面，Sonic的证明大小为常数（在无人辅助的简洁版本中，通过批量化技术，证明包含20个G₁元素和16个域元素，约1kB；在辅助版本中为7个G₁元素和5个域元素，约256字节）。证明者的计算量为O(n log n)次群指数运算，验证者在辅助情况下的边际开销仅为约10次配对运算（一次性配对成本可摊销），这使得验证效率与传统最有效的预计算zk-SNARK相竞争。

### 核心公式与流程

**约束系统核心等式**
\[
\mathbf{a}\cdot\mathbf{u}(Y) + \mathbf{b}\cdot\mathbf{v}(Y) + \mathbf{c}\cdot\mathbf{w}(Y) + \sum_{i=1}^n a_i b_i (Y^i + Y^{-i}) - k(Y) = 0
\]
> 作用：将电路的n个乘法约束和Q个线性约束融合成一个双变量多项式恒等式，是协议正确性的基础。

**目标多项式t(X,Y)的构造**
\[
t(X,Y) = r(X,1) \cdot r'(X,Y) - k(Y)
\]
其中 \( r'(X,Y) = r(X,Y) + s(X,Y) \)，且s(X,Y)是由电路公开信息决定的多项式。
> 作用：将约束检查转化为证明t(X,Y)的零次项系数为零，这是协议交互的最终目标。

**Sonic协议交互步骤（核心流程）**
> 证明者(Prover)持有秘密见证(a,b,c)和公共实例参数。
> 1. **zkP1**：生成四个随机盲化系数，构造r(X,Y)，计算并发送对r(X,1)的承诺R。
> 2. **zkV1**：验证者发送随机挑战y。
> 3. **zkP2**：证明者计算t(X,y)，计算并发送对t(X,y)的承诺T。
> 4. **zkV2**：验证者发送第二个随机挑战z。
> 5. **zkP3**：证明者打开承诺R得到a=r(z,1)和b=r(zy,1)，打开承诺T得到t=t(z,y)，并计算正确的计算签名(s, sc)。发送所有打开值和签名。
> 6. **zkV3**：验证者检查验证方程: t = a(b+s) - k(y) 以及所有多项式承诺验证(pcV)和正确计算签名验证(scV)均通过。

**多项式承诺方案（核心验证方程）**
\[
e(W, h^{\alpha x}) \cdot e(g^v W^{-z}, h^{\alpha}) = e(F, h^{x^{-d+\text{max}}})
\]
> 作用：用于验证多项式在点z处的取值v = f(z)是否正确，确保承诺F确实绑定了某个多项式。其中W是见证w(X) = (f(X) - f(z))/(X-z)在x处的赋值。

**正确计算签名（笛卡尔制约下的验证）**
在无人辅助的版本中，通过排列论证和累乘论证来验证s(X,Y)在特定点处的正确计算。在辅助版本（hscP/hscV）中，通过承诺公开多项式在不同分支点的取值并交叉验证来达成常量开销的批量验证。

### 实验结果
论文使用开源的Rust实现Sonic（辅助版本）[1]并进行了性能评估。实验平台是CPU i7-2600K (3.4GHz) 搭配32GB RAM，使用BLS12-381椭圆曲线（目标128位安全级别）。针对不同的哈希电路Pedersen Hash (输入48, 384位) 和 SHA256 (输入512, 1024, 1536位) 进行了测试。对于SHA256 (39,516个乘法门)，证明大小为256字节，生成SRS耗时422.39秒，单个证明的计算时间为14.63秒，辅助者边际验证延迟仅为0.68毫秒。对于更大的SHA256 (117,010个门)，SRS大小上升到273.14 MB，整个实验证明：验证者在优化后的批量场景下的边际开销（0.68~0.72ms）基本保持恒定且与电路规模无关，而Bulletproofs在类似SHA256规模下的证明大小为1376字节，验证时间为41.52ms（虽然不是直接对比，但体现了Sonic的常量验证优势）。对比于Groth 2016方案的理论理想批量验证边际成本（约0.6ms），Sonic的0.68ms非常接近，达到了可以替代的水平。证明生成成本随着电路规模线性增长，符合预期。

### 局限性与开放问题
尽管Sonic实现了通用可更新SRS，但其全局SRS大小仍与电路深度d呈线性关系，对于门数很大的电路，SRS的存储和传输开销依然显著（如117k门电路的SRS达到273 MB）。未辅助版本的证明体（约1kB）和证明者计算（约180n次指数运算）都明显高于辅助版本，该版本仅作为理论上的存在证明而不具备实际优势。此外，Sonic的整体安全模型依赖于代数群模型（AGM），虽然它比随机谕言模型更贴近现实，但毕竟不是标准模型假设，系统性的模型适应性和后量子抵抗性仍是一个开放问题。最后，论文所实现的代码未被编写为恒定时间算法，这可能会引入侧信道攻击的风险，影响实际部署的安全边界。

### 强关联论文

[22] Bootle 等. Efficient zero-knowledge arguments for arithmetic circuits in the discrete log setting. **EUROCRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+zero-knowledge+arguments+for+arithmetic+circuits+in+the+discrete+log+setting)

[26] Bünz 等. Bulletproofs: Short proofs for confidential transactions and more. **IEEE S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Bulletproofs+Short+proofs+for+confidential+transactions+and+more)

[45] Groth. On the size of pairing-based non-interactive arguments. **EUROCRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=On+the+size+of+pairing-based+non-interactive+arguments)

[46] Groth 等. Updatable and universal common reference strings with applications to zk-snarks. **CRYPTO 2018** [Google Scholar](https://scholar.google.com/scholar?q=Updatable+and+universal+common+reference+strings+with+applications+to+zk-snarks)

[37] Fuchsbauer 等. The algebraic group model and its applications. **CRYPTO 2018** [Google Scholar](https://scholar.google.com/scholar?q=The+algebraic+group+model+and+its+applications)

[50] Kate 等. Constant-size commitments to polynomials and their applications. **ASIACRYPT 2010** [Google Scholar](https://scholar.google.com/scholar?q=Constant-size+commitments+to+polynomials+and+their+applications)

[58] Papamanthou 等. Signatures of correct computation. **TCC 2013** [Google Scholar](https://scholar.google.com/scholar?q=Signatures+of+correct+computation)

[61] Wahby 等. Doubly-efficient zkSNARKs without trusted setup. **IEEE S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Doubly-efficient+zkSNARKs+without+trusted+setup)

[13] Ben-Sasson 等. Aurora: Transparent succinct arguments for R1CS. **IACR ePrint 2018/828** [Google Scholar](https://scholar.google.com/scholar?q=Aurora+Transparent+succinct+arguments+for+R1CS)


## 关键词

+ 零知识证明
+ SNARK
+ 通用参考字符串
+ 可更新参数
+ 批量验证