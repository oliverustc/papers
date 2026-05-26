---
title: "Aurora: Transparent Succinct Arguments for R1CS"
标题简称: Aurora
论文类型: conference
会议简称: EUROCRYPT
发表年份: 2019
modified: 2025-04-08 18:43:18
---

## Aurora: Transparent Succinct Arguments for R1CS

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-030-17653-2_4)

## 作者

+ Eli Ben-Sasson
+ [Alessandro Chiesa](Alessandro%20Chiesa.md)
+ Michael Riabzev
+ Nicholas Spooner
+ Madars Virza
+ Nicholas P. Ward

## 笔记

### 背景与动机
零知识证明是现代密码学的基础工具，尤其在隐私保护货币系统如Zcash[1,18]中发挥核心作用。许多实际应用要求证明必须是简洁的，即证明大小随计算规模亚线性增长，这被称为简洁非交互式论证（SNARG）。传统的SNARG构造[46]如Pinocchio[67]依赖于需信任的第三方生成公共参数，这种“可信设置”在实际部署中极为不便，因为不存在一个被所有参与者信任的中心化方。尽管可通过安全多方计算[20,32,33]分担信任，但其高昂成本和物流难度限制了可扩展性。同时，基于椭圆曲线双线性对的SNARG在量子计算机面前不安全。因此，透明设置（仅需公开随机性）且后量子安全的SNARG成为迫切需求。现有的透明SNARG如Ligero[4]的证明大小为$O(\sqrt{N})$，Stark[13]的证明大小为$O(\log^2 N)$，但前者对于大规模电路仍显臃肿，后者在面向显式电路时因模型转换产生额外开销。本文提出的Aurora填补了空白：它是首个在透明设置下，针对广泛采用的Rank-1约束系统（R1CS）实现$O(\log^2 N)$证明大小且具备后量子安全性的SNARG。

### 相关工作

[4] Ames et al. **Ligero: lightweight sublinear arguments without a trusted setup.** *CCS 2017* [Google Scholar](https://scholar.google.com/scholar?q=Ligero+lightweight+sublinear+arguments+without+a+trusted+setup)
> 核心思路：利用IPCP（交互式PCP），证明大小为$O(\sqrt{N})$。
> 局限与区别：Ligero的查询复杂度为$O(\sqrt{N})$，而Aurora通过单变量Sumcheck将其降至$O(\log N)$，从而在达到百万门规模时证明大小缩小约20倍。

[13] Ben-Sasson et al. **Scalable, transparent, and post-quantum secure computational integrity.** *ePrint 2018/046* [Google Scholar](https://scholar.google.com/scholar?q=Scalable+transparent+and+post-quantum+secure+computational+integrity)
> 核心思路：基于IOP的STARK协议，针对随机存取机器的有界停机问题。
> 局限与区别：Stark支持均匀计算，但将其用于显式电路时，因路由网络额外开销导致证明大小比Aurora大约15倍，证明者是Aurora的$O(\log N)$倍。

[31] Bootle et al. **Efficient zero-knowledge arguments for arithmetic circuits in the discrete log setting.** *EUROCRYPT 2016* [Google Scholar](https://scholar.google.com/scholar?q=Efficient+zero-knowledge+arguments+for+arithmetic+circuits+in+the+discrete+log+setting)
> 核心思路：Bulletproofs利用递归内积论证，证明大小为$O(\log N)$群元素。
> 局限与区别：依赖Pedersen承诺，易受量子攻击，且验证者需$O(N)$次群指数运算，而Aurora仅需对称密码学。

[79] Wahby et al. **Doubly-efficient zkSNARKs without trusted setup.** *ePrint 2017/1132* [Google Scholar](https://scholar.google.com/scholar?q=Doubly-efficient+zkSNARKs+without+trusted+setup)
> 核心思路：Hyrax通过Cramer-Damgård变换结合双层高效交互证明，证明大小为$O(d \log W)$。
> 局限与区别：同样依赖离散对数假设，不抗量子，且验证者群指数运算与见证大小线性相关。

[14] Ben-Sasson et al. **Fast Reed-Solomon Interactive Oracle Proofs of Proximity.** *ICALP 2018* [Google Scholar](https://scholar.google.com/scholar?q=Fast+Reed-Solomon+Interactive+Oracle+Proofs+of+Proximity)
> 核心思路：FRI协议，高效测试Reed-Solomon码的近邻性，具有$O(\log d)$查询复杂度。
> 区别：Aurora直接使用FRI作为低度测试子程序，并将其嵌入单变量Sumcheck。

[61] Lund et al. **Algebraic methods for interactive proof systems.** *J. ACM 1992* [Google Scholar](https://scholar.google.com/scholar?q=Algebraic+methods+for+interactive+proof+systems)
> 核心思路：经典多变量Sumcheck协议，用于验证多项式在超立方体上求和。
> 局限：原始Sumcheck适用于多变量多项式（Reed-Muller码），无法直接用于单变量Reed-Solomon码，而Aurora设计了其单变量模拟。

[21] Ben-Sasson et al. **Interactive Oracle Proofs.** *TCC 2016-B* [Google Scholar](https://scholar.google.com/scholar?q=Interactive+Oracle+Proofs)
> 核心思路：提出IOP模型，并给出从IOP到非交互式论证的BCS变换。
> 区别：Aurora应用BCS变换将其IOP实例化为SNARG，而Aurora本身提供新的IOP构造。

[14] 同上。

### 核心技术与方案

**整体框架**
Aurora的SNARG基于一个新型的IOP协议。该IOP协议将R1CS实例的验证分解为两个基本子问题：行检查（Rowcheck）和线性检查（Lincheck）。证明者首先发送编码后的赋值$z$及其经矩阵变换后的向量$Az, Bz, Cz$的Reed-Solomon（RS）码字。随后，证明者和验证者并行执行三个Lincheck实例（分别对应$A, B, C$矩阵）和一个Rowcheck实例（验证$Az \circ Bz = Cz$）。Lincheck通过一个归约过程转化为单变量Sumcheck实例，Rowcheck则可通过标准低度测试处理。

**单变量Sumcheck协议**
这是Aurora的核心技术贡献。经典的多变量Sumcheck [61]依赖于多项式的张量结构，而Reed-Solomon码对应的单变量多项式不具备该结构。本文提出，当求和域$H$是域的加法陪集或乘法陪集时，存在一个有效的单变量Sumcheck协议。核心定理（Byott和Chapman [36]）指出，多项式$f$在加法陪集$H$上的和为零当且仅当$f$的$X^{|H|-1}$次项系数为零。因此，当$f$的次数$d < |H|$时，问题等价于测试$f$的次数低于$|H|-1$，这可由FRI低度测试[14]以$O(\log d)$查询复杂度完成。当$d \ge |H|$时，将$f$分解为$f(x) = g(x) + \prod_{\alpha \in H}(x - \alpha) \cdot h(x)$，其中$\deg(g) < |H|$，则$f$与$g$在$H$上一致。证明者发送$h$作为新的预言机，验证者通过查询$f$和$h$可隐式计算$g$，再对$g$执行前述低度测试。该协议证明复杂度为$O(d)$，查询复杂度$O(\log d)$。

**行检查与线性检查**
行检查问题：验证向量$x, y, z$满足$x \circ y = z$。在编码域$L$上，给定RS码字$f, g, h$，需检验$\hat{f}(a) \cdot \hat{g}(a) - \hat{h}(a) = 0$对所有$a \in H$成立。这可通过构造复合多项式$(f \cdot g - h) / Z_H$（其中$Z_H$是域$H$的消去多项式）并测试其低度性来实现。线性检查问题：验证$f(a) = \sum_{b} M_{a,b} g(b)$对所有$a \in H_1$成立。该问题可归约到单变量Sumcheck：构造多项式$p_\alpha$和$p_\alpha^{(M)}$，将矩阵乘法的约束编码为多项式在集合上的求值关系。通过随机线性组合，可将多个并行检查聚合为一个Sumcheck实例。

**零知识实现**
为满足零知识，Aurora采用有界独立性技术。编码赋值$z$时，不使用唯一的低次插值多项式，而是随机采样次数稍高的多项式（如$|H|+9$），使其在非$H$域上的求值独立均匀分布。对于Sumcheck，通过自归约（self-reduction）技术：证明者先发送随机码字$r$及其在$H$上的和$\beta$，验证者发送随机挑战$\rho$，双方转而证明$\sum_{a \in H} (\rho f(a) + r(a)) = \beta$。由于$r$均匀随机，新多项式亦随机，从而隐藏了$f$的信息。

**渐进复杂度**
对于具有$N$个约束（$N = \Theta(m+n)$）的R1CS实例，Aurora IOP的证明长度为$O(N)$域元素，查询复杂度$O(\log N)$，轮复杂度$O(\log N)$。证明者时间$O(N \log N)$域运算，验证者时间$O(N)$域运算。通过BCS变换[21]获得非交互式SNARG后，证明大小变为$O_\lambda(\log^2 N)$，其中$\lambda$为安全参数。

### 核心公式与流程

**[R1CS 关系式]**
给定矩阵 $A, B, C \in \mathbb{F}^{m \times n}$ 和部分赋值 $v \in \mathbb{F}^k$，是否存在 $w \in \mathbb{F}^{n-k}$ 使得对于 $z = (1, v, w)$ 有：
$$(A z) \circ (B z) = C z$$
其中 $\circ$ 表示逐元素乘积。
> 作用：定义了NP完全问题R1CS，是Aurora要证明的语言。

**[单变量Sumcheck协议核心观察]**
设 $H \subseteq \mathbb{F}$ 为加法陪集，$f \in \mathbb{F}[X]$ 满足 $\deg(f) < |H|$。则：
$$\sum_{a \in H} f(a) = 0 \iff \text{系数 of } X^{|H|-1} \text{ in } f \text{ is } 0$$
> 作用：将加和检验转化为低度检验，是单变量Sumcheck的理论基础。

**[多项式分解]**
对于任意多项式 $f \in \mathbb{F}[X]$，存在 $g, h$ 使得：
$$f(X) = g(X) + \prod_{\alpha \in H}(X - \alpha) \cdot h(X)$$
其中 $\deg(g) < |H|$，$\deg(h) < \deg(f) - |H|$。
> 作用：当 $f$ 次数过高时，利用此分解将问题归约到低次多项式 $g$，$h$ 由证明者提供。

**[零知识自归约]**
证明者选择随机 $r$ 并发送 $\beta = \sum_{a \in H} r(a)$。验证者发送 $\rho \in \mathbb{F}$。双方转而证明：
$$\sum_{a \in H} (\rho f(a) + r(a)) = \beta$$
> 作用：将原求和陈述随机化，使后续协议中多项式均匀分布，实现零知识。

**[IOP协议流程（Theorem 4）]**
1. 证明者发送编码后的见证及矩阵乘积：$f_w, f_{Az}, f_{Bz}, f_{Cz}$。
2. 并行执行 $\lambda_i$ 轮：
   - 证明者发送随机码字 $r_i$ 及其和 $\mu_i$。
   - 验证者发送挑战 $\alpha_i$ 和 $s_i$。
   - 构造求和多项式并分解，证明者发送 $h_i$，验证者本地计算 $g_i$。
3. 双方执行FRI低度测试，验证所有预言机的低度性及一致性。
> 作用：描述了Aurora IOP的高层交互步骤，实现R1CS的前述归约。

### 实验结果
实验在一台Intel Xeon W-2155 3.30 GHz 10核CPU和64GB RAM的机器上进行。安全级别设为128比特，使用二进制域 $\mathbb{F}_{2^{192}}$。测试范围从$2^{10}$到$2^{20}$个约束。在$2^{20}$（约100万）约束时，Aurora的证明大小约为220 kB，而Ligero为4.0 MB，Stark为3.2 MB，Aurora分别缩小了约18倍和15倍。证明时间从0.1秒（$2^{10}$）到约100秒（$2^{20}$），验证时间从数毫秒（$2^{10}$）到约1.5秒（$2^{20}$）。验证时间开销相对于本地执行（直接检查赋值）约为常数倍，在$2^{20}$约束时约为15倍。实验表明，证明大小在约束数量超过4000时开始小于原生见证大小，实现了压缩。

### 局限性与开放问题
尽管Aurora的证明大小相对于Ligero和Stark有显著改善，但仍有差距：基于非对称密码学的SNARK（如使用椭圆曲线双线性对）可达到仅百字节级别的证明大小，而Aurora的证明大小随安全参数二次增长。此外，证明时间虽为$O(N \log N)$，但在绝对数值上（几分钟）对于实时性要求高的应用可能仍显昂贵。如何将单变量Sumcheck协议推广到任意子集$H$（而不仅限于陪集），以及如何进一步降低BCS变换中的哈希开销，都是值得探索的方向。

### 强关联论文

[4] Ames et al. **Ligero: lightweight sublinear arguments without a trusted setup.** *CCS 2017*

[13] Ben-Sasson et al. **Scalable, transparent, and post-quantum secure computational integrity.** *ePrint 2018/046*

[14] Ben-Sasson et al. **Fast Reed-Solomon Interactive Oracle Proofs of Proximity.** *ICALP 2018*

[21] Ben-Sasson et al. **Interactive Oracle Proofs.** *TCC 2016-B*

[31] Bootle et al. **Efficient zero-knowledge arguments for arithmetic circuits in the discrete log setting.** *EUROCRYPT 2016*

[61] Lund et al. **Algebraic methods for interactive proof systems.** *J. ACM 1992*

[79] Wahby et al. **Doubly-efficient zkSNARKs without trusted setup.** *ePrint 2017/1132*


## 关键词

+ 透明SNARG
+ R1CS约束系统
+ 交互式预言证明
+ 里德-所罗门码
+ 后量子安全