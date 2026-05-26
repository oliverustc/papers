---
title: "Transparent SNARKs from DARK Compilers"
标题简称:
论文类型: conference
会议简称: EUROCRYPT
发表年份: 2020
modified: 2025-04-09 15:54:05
---

## Transparent SNARKs from DARK Compilers

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-030-45721-1_24)

## 作者

+ [Benedikt Bünz](Benedikt%20Bünz.md)
+ [Ben Fisch](Ben%20Fisch.md)
+ Alan Szepieniec

## 笔记

### 背景与动机
对可验证外包计算和零知识证明的工业需求，特别是区块链领域对隐私和完整性验证的需求，催生了高效证明系统的研究。理想的证明系统应同时具备简洁性（证明大小亚线性于计算规模）、非交互性、证明者可扩展性（证明时间拟线性）以及验证者可扩展性（验证时间亚线性）。当前性能最佳的证明系统，如基于双线性对的预处理SNARKs，实现了极小的证明和常数级验证时间，但其严重依赖可信设置。即使通过多方安全计算执行，该设置过程依然复杂且需要信任假设。透明证明系统无需任何可信设置，但现有方案存在显著瓶颈。zk-STARKs的证明大小和验证复杂度为 $O_\lambda(\log^2 T)$，对百万门电路证明约600 KB，远超预处理SNARKs的200字节。Bulletproofs的证明虽小，但验证时间与电路规模呈线性关系。另一类通用SNARKs通过将电路可满足性归约到概率性多项式测试，并结合多项式承诺方案，但如Kate等人所提出的承诺方案[39]仍需要一个针对每项电路的可信设置。本文旨在填补空白，构建一个无需可信设置的透明多项式承诺方案，并以此为基础，通过Polynomial IOP框架编译出首个兼具实用证明者效率、渐近对数级证明大小和验证时间的透明zk-SNARK系统Supersonic。

### 相关工作

[29] Fujisaki, E., Okamoto, T. Statistical zero knowledge protocols to prove modular polynomial relations. **CRYPTO 1997** [Google Scholar](https://scholar.google.com/scholar?q=Statistical+zero+knowledge+protocols+to+prove+modular+polynomial+relations)
> 核心思路：基于RSA群提出了同态整数承诺方案，并提供协议证明一组承诺整数满足模多项式方程。
> 局限与区别：该工作开启了基于隐藏阶群构建密码协议的先河，但本文的DARK编译器将其作为关键组件，并进一步集成到Polynomial IOP框架中以构造完整的SNARK系统。

[25] Damgård, I., Fujisaki, E. A statistically-hiding integer commitment scheme based on groups with hidden order. **ASIACRYPT 2002** [Google Scholar](https://scholar.google.com/scholar?q=A+statistically-hiding+integer+commitment+scheme+based+on+groups+with+hidden+order)
> 核心思路：修复了[29]中协议的可靠性证明，并首次建议使用类群（class groups）作为未知阶群的候选。
> 局限与区别：该工作奠定了类群在密码学中的应用基础，这与本文中使用类群实现完全透明设置的技术路线直接相关。

[42] Lipmaa, H. On diophantine complexity and statistical zero-knowledge arguments. **ASIACRYPT 2003** [Google Scholar](https://scholar.google.com/scholar?q=On+diophantine+complexity+and+statistical+zero-knowledge+arguments)
> 核心思路：将整数承诺方案构造的零知识证明与丢番图复杂性联系起来，提出了“迪奥芬图论证”（DARK）的概念。
> 局限与区别：本文的DARK编译器延续并深化了这一概念，将其具体应用于多项式承诺，并实现了对级别数评估证明的验和。

[53] Wesolowski, B. Efficient verifiable delay functions. **EUROCRYPT 2019** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+verifiable+delay+functions)
> 核心思路：提出了一个简洁的指数外包证明（PoE）协议，允许在未知阶群中高效验证大指数运算的正确性。
> 局限与区别：该工作的PoE协议是本文DARK多项式承诺方案中实现验证者高效性（对数级验证时间）的关键底层工具。

[4] Ben-Sasson, E., et al. Scalable zero knowledge with no trusted setup. **CRYPTO 2019** [Google Scholar](https://scholar.google.com/scholar?q=Scalable+zero+knowledge+with+no+trusted+setup)
> 核心思路：提出了zk-STARKs，一个完全透明的证明系统，证明大小和验证复杂度为 $O_\lambda(\log^2 T)$。
> 局限与区别：本文的Supersonic在证明大小上优于STARKs（$O_\lambda(\log T)$），但STARKs基于哈希函数，具有量子安全性。

[43] Maller, M., et al. Sonic: Zero-knowledge snarks from linear-size universal and updatable structured reference strings. **ePrint 2019** [Google Scholar](https://scholar.google.com/scholar?q=Sonic%3A+Zero-knowledge+snarks+from+linear-size+universal+and+updatable+structured+reference+strings)
> 核心思路：提出了Sonic，一个具有通用和可更新SRS的zk-SNARK，其Polynomial IOP是其核心。
> 局限与区别：本文的DARK编译器可以应用于Sonic的Polynomial IOP，从而将其从需要通用SRS的构造转变为完全透明的Supersonic变体。

[30] Gabizon, A., et al. PLONK: Permutations over lagrange-bases for oecumenical noninteractive arguments of knowledge. **ePrint 2019** [Google Scholar](https://scholar.google.com/scholar?q=PLONK%3A+Permutations+over+lagrange-bases+for+oecumenical+noninteractive+arguments+of+knowledge)
> 核心思路：改进了Sonic的Polynomial IOP，减少了评估点和多项式数量，提高了效率。
> 局限与区别：本文编译PLONK的Polynomial IOP来构造Supersonic，获得了更优的性能（更小的证明和更快的验证）。

[39] Kate, A., et al. Constant-size commitments to polynomials and their applications. **ASIACRYPT 2010** [Google Scholar](https://scholar.google.com/scholar?q=Constant-size+commitments+to+polynomials+and+their+applications)
> 核心思路：提出了一个基于双线性配对的多项式承诺方案，具有常数级的承诺和证明大小。
> 局限与区别：该方案（KZG方案）需要可信设置。本文的核心贡献是提出了一个不需要可信设置的替代方案（DARK），从而消除了这一信任假设。

[3] Ben-Sasson, E., et al. Fast reed-solomon interactive oracle proofs of proximity. **ICALP 2018** [Google Scholar](https://scholar.google.com/scholar?q=Fast+reed-solomon+interactive+oracle+proofs+of+proximity)
> 核心思路：提出了FRI协议，一个高效的交互式预言机接近性证明。
> 局限与区别：FRI可以被看作是一种基于哈希的透明多项式承诺，但用于编译SNARKs时，其证明大小为 $O(\lambda \log^2 d)$。本文的DARK方案提供了更优的对数级证明大小。

### 核心技术与方案

本文的整体框架包含三个核心层次：一个新的多项式承诺方案（DARK编译器）、一个统一的信息论框架（Polynomial IOPs）以及将二者结合以构造透明SNARKs的编译方法。

#### 多项式承诺方案（DARK Compiler）
该方案的核心创新在于将多项式编码为整数，并在未知阶群中对其进行承诺。首先，将域多项式 $f(X) \in \mathbb{Z}_p[X]$ 的系数映射到区间 $[-\frac{p-1}{2}, \frac{p-1}{2}]$，得到一个整数系数多项式 $\hat{f}(X)$。然后，通过在一个“足够大”的整数 $q$ 上求值，将其编码为单个整数 $\hat{f}(q)$。编码的加法和乘以 $X^k$ 的同态性可以通过承诺的群运算体现。

承诺机制：在未知阶群 $\mathbb{G}$（如RSA群或类群）中，承诺值为 $\mathsf{C} = \mathsf{g}^{\hat{f}(q)}$，其中 $\mathsf{g}$ 是随机生成元。此承诺的绑定性依赖于群的未知阶性质。评估协议（Eval）的核心是一个递归的二分过程，将证明 $f(z)=y$ 归约到证明一个degree约为一半的多项式 $\alpha f_L(X) + f_R(X)$ 在 $z$ 处的求值。该协议的关键步骤是，在每一轮递归中，验证者需要检查承诺的一致性 $\mathsf{C}_L \cdot \mathsf{C}_R^{q^{d'+1}} = \mathsf{C}$。直接计算该指数代价高昂，因此利用Wesolowski的指数外包证明（PoE）[53] 将此计算外包给证明者，从而将验证者的工作量降低到对数级别。

安全性：该方案的绑定性依赖于Strong RSA假设和Adaptive Root假设。评估协议具有知识可靠性（witness-extended emulation），证明策略是构造一个提取器，通过递归地重放证明者并从多个 $\alpha$ 值对应的递归结果中提取出多项式系数。

#### Polynomial IOP框架
Polynomial IOP是对代数线性IOP [9, 11] 的一个细化。在Polynomial IOP中，证明者在每一轮发送的是一整个多元多项式 $\pi_i(\mathbf{X})$，而验证者可以查询该多项式在任意点上的求值。此框架将信息论基础与具体密码学承诺方案解耦。关键结果是，任何（有限制条件的）代数线性IOP都可以通过一些辅助工具（如系数查询和内积证明）转化为一个Polynomial IOP。例如，一个t轮代数线性IOP可以被转化为一个 $(t+1)$-轮Polynomial IOP，且后者具有预处理阶段。

#### SNARK编译
给定一个Public-coin Polynomial IOP和一个多项式承诺方案（如DARK），可以编译成一个交互式论证。具体地，在对应的IOP轮中，证明者发送其多项式 $\pi$ 的承诺 $c_\pi$；当IOP验证者需要查询某点 $z$ 时，双方执行一个交互式的$\mathsf{Eval}(c_\pi, z, y)$协议来证明 $\pi(z)=y$。如果承诺方案具有知识可靠性，且Polynomial IOP具有知识可靠性，则编译后的交互式论证也具有知识可靠性。最后，通过Fiat-Shamir变换可将交互式论证转换为非交互式SNARK。

**Supersonic 具体构造与复杂度**：将DARK多项式承诺方案应用到PLONK [30] 的Polynomial IOP上，并进行batching优化，得到Supersonic。对于算术电路规模为 $n$ 的NP关系，Supersonic的证明者和验证者在预处理阶段各需 $O(n \log n)$ 时间。在线阶段，证明大小为 $O(\lambda \log n)$，验证时间为 $O(\lambda \log n)$。与PLONK相比，它用对数级的证明和验证时间换取了透明性。

### 核心公式与流程

**[整数编码方案]**
定义 $f(X) = \sum_{i=0}^{d} f_i X^i \in \mathbb{Z}_p[X]$。选择系数代表在 $[-\frac{p-1}{2}, \frac{p-1}{2}]$，得到 $\hat{f}(X) \in \mathbb{Z}[X]$。整数编码为 $\mathsf{Enc}(f) = \hat{f}(q) \in \mathbb{Z}$，其中 $q$ 是一个足够大的整数。
> 作用：将多项式问题转化为整数算术问题，为在未知阶群上进行承诺奠定基础。

**[EvalBounded递归协议（核心协议）]**
给定承诺 $\mathsf{C} = \mathsf{g}^{\hat{f}(q)}$，点 $z$，值 $y$，度 $d$，协调边界 $b$。
1. 若 $d=0$：证明者发送常数 $f$。验证者检查 $|f| \le b$, $f \equiv y \mod p$, $\mathsf{g}^f = \mathsf{C}$。
2. 若 $d+1$ 为奇数，则将多项式乘以 $X$，并递归。
3. 若 $d+1$ 为偶数，设 $d' = (d+1)/2 - 1$。
   - 证明者将 $f$ 分解为 $f_L(X)$ 和 $f_R(X)$。
   - 证明者发送 $y_L = f_L(z) \mod p$, $y_R = f_R(z) \mod p$, 以及承诺 $\mathsf{C}_L = \mathsf{g}^{\hat{f}_L(q)}$, $\mathsf{C}_R = \mathsf{g}^{\hat{f}_R(q)}$。
   - 验证者检查 $y \equiv y_L + z^{d'+1} y_R \mod p$。
   - 双方执行PoE协议检查 $\mathsf{C}_L \cdot \mathsf{C}_R^{q^{d'+1}} = \mathsf{C}$。
   - 验证者发送随机挑战 $\alpha \in [-\frac{p-1}{2}, \frac{p-1}{2}]$。
   - 双方计算 $y' = \alpha y_L + y_R \mod p$, $\mathsf{C}' = \mathsf{C}_L^{\alpha} \mathsf{C}_R$, $b' = b \cdot \frac{p+1}{2}$。
   - 递归执行 EvalBounded($\mathsf{C}'$, $z$, $y'$, $d'$, $b'$)。
> 作用：将Eval问题归约为更小度数的多项式，总轮数为 $\log_2(d+1)$。

**[指数外包证明 (PoE) [53]]**
为了证明 $\mathsf{w} = \mathsf{u}^x$。
1. 验证者发送随机素数 $\ell$。
2. 证明者计算商 $q$ 和余数 $r$ 使得 $x = q\ell + r$。
3. 证明者发送 $\mathsf{Q} = \mathsf{u}^q$。
4. 验证者计算 $r = x \mod \ell$，并检查 $\mathsf{Q}^\ell \mathsf{u}^r = \mathsf{w}$。
> 作用：在未知阶群中高效验证大指数运算，将EvalBounded中验证者的工作量从 $O(d)$ 降低到 $O(\log d)$。

**[解码算法 Dec]**
给定整数 $y = \hat{f}(q)$，Recover多项式系数 $f_i$：
1. 对于 $k=0$ 到 $\lfloor \log_q(|y|) \rfloor$:
2.   计算 $S_{k-1} \leftarrow (y \bmod q^k)$，若 $S_{k-1} > q^k/2$ 则 $S_{k-1} \leftarrow q^k - S_{k-1}$。
3.   计算 $S_k \leftarrow (y \bmod q^{k+1})$，若 $S_k > q^{k+1}/2$ 则 $S_k \leftarrow q^{k+1} - S_k$。
4.   计算 $f_k \leftarrow (S_k - S_{k-1}) / q^k$。
> 作用：保证编码的单射性（Fact 1），即只要整数 $y$ 的绝对值小于 $q^{d+1}/2$，就能唯一解码出系数绝对值小于 $q/2$ 的多项式，这是绑定性证明的关键。

### 实验结果

本文的实验是基于理论分析和参数估计，而非具体实现。实验设置的基线对比包括PLONK [30]、Groth16 [35]、Bulletproofs [18]、STARK [4] 等方案。核心性能数值评估了Supersonic的证明大小和验证时间。估计中使用了120比特的安全等级（λ=120）。对于包含 $2^{20}$（约100万）个门的电路，Supersonic（基于PLONK编译）的证明大小为10.1 KB，这比STARK的600 KB小了一个数量级，但比PLONK的720比特大。验证者需要执行约 $3\log_2(2^{20}) \approx 60$ 次群运算。在假设每次群运行为10微秒的条件下，总验证时间约为72毫秒。当使用1200比特的类群以实现100比特安全等级时，证明大小可进一步降低至7.8 KB。与基线对比，Supersonic在透明设置下首次实现了对数级证明大小和验证时间，与PLONK和Groth16相比，其以更大的证明开销换取了无需信任假设的优势。与Bulletproofs相比，验证时间得到了质的提升。与STARK相比，证明大小和验证复杂度渐近性地更优（$O_\lambda(\log T)$ vs $O_\lambda(\log^2 T)$）。然而，这种优势以证明者时间为代价，证明者需要进行 $O(n \log n)$ 次大整数（如1200或3048比特）的群指数运算，其具体效率远低于STARK中所用的轻量级FFT和哈希。结论是，Supersonic在证明大小和验证速度之间取得了权衡，而证明者效率是其短板。

### 局限性与开放问题

重要开放问题包括：如何设计支持稀疏多项式的承诺方案，以直接高效编译如QAPs等简单信息论协议，因为当前方案即使对零系数也需要线性时间处理。其次，Supersonic的具体实现和性能比较仍是空白，其理论上的拟线性证明者时间能否在工程上实现可接受的水平尚待验证。最后，该工作进一步推动了对类群和未知阶群的研究，特别是本文依赖于最近提出的Adaptive Root假设，其安全性和实现细节仍需深入分析。此外，DARK编译器的底层信息论协议是否可以被同态承诺方案在其他不同假设下实例化也是一个开放方向。

### 强关联论文

[4] Ben-Sasson, E., et al. Scalable zero knowledge with no trusted setup. **CRYPTO 2019** [Google Scholar](https://scholar.google.com/scholar?q=Scalable+zero+knowledge+with+no+trusted+setup)

[30] Gabizon, A., et al. PLONK: Permutations over lagrange-bases for oecumenical noninteractive arguments of knowledge. **ePrint 2019** [Google Scholar](https://scholar.google.com/scholar?q=PLONK%3A+Permutations+over+lagrange-bases+for+oecumenical+noninteractive+arguments+of+knowledge)

[43] Maller, M., et al. Sonic: Zero-knowledge snarks from linear-size universal and updatable structured reference strings. **ePrint 2019** [Google Scholar](https://scholar.google.com/scholar?q=Sonic%3A+Zero-knowledge+snarks+from+linear-size+universal+and+updatable+structured+reference+strings)

[39] Kate, A., et al. Constant-size commitments to polynomials and their applications. **ASIACRYPT 2020** [Google Scholar](https://scholar.google.com/scholar?q=Constant-size+commitments+to+polynomials+and+their+applications)

[53] Wesolowski, B. Efficient verifiable delay functions. **EUROCRYPT 2019** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+verifiable+delay+functions)

[22] Chiesa, A., et al. Marlin: preprocessing zkSNARKs with universal and updatable SRS. **ePrint 2019** [Google Scholar](https://scholar.google.com/scholar?q=Marlin%3A+preprocessing+zkSNARKs+with+universal+and+updatable+SRS)

[25] Damgård, I., Fujisaki, E. A statistically-hiding integer commitment scheme based on groups with hidden order. **ASIACRYPT 2002** [Google Scholar](https://scholar.google.com/scholar?q=A+statistically-hiding+integer+commitment+scheme+based+on+groups+with+hidden+order)

[42] Lipmaa, H. On diophantine complexity and statistical zero-knowledge arguments. **ASIACRYPT 2003** [Google Scholar](https://scholar.google.com/scholar?q=On+diophantine+complexity+and+statistical+zero-knowledge+arguments)

[35] Groth, J. On the size of pairing-based non-interactive arguments. **EUROCRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=On+the+size+of+pairing-based+non-interactive+arguments)

[18] Bünz, B., et al. Bulletproofs: short proofs for confidential transactions and more. **S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Bulletproofs%3A+short+proofs+for+confidential+transactions+and+more)


## 关键词

+ 透明SNARK
+ 多项式承诺方案
+ 丢番图知识论证
+ 未知阶群
+ Supersonic