---
title: "Spartan: Efficient and general-purpose zkSNARKs without trusted setup"
doi: 10.1007/978-3-030-56877-1_25

标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 2020
modified: 2025-04-11 14:43:37
---
## Spartan: Efficient and general-purpose zkSNARKs without trusted setup

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-030-56877-1_25)

## 作者

+ [Srinath Setty](Srinath%20Setty.md)

## 笔记

### 背景与动机

零知识简洁非交互知识论证（zkSNARK）使证明者能向验证者证明一个NP语句的成员关系，同时保持证明长度和验证时间在语句规模的亚线性范围内，且不泄露任何额外信息。然而，几乎所有实用zkSNARK都依赖可信设置，即需要生成一个包含陷阱门的结构化公共参考串，这在许多现实场景中不可行。近期涌现的透明zkSNARK（如Hyrax、STARK、Aurora、Ligero、Bulletproofs）无需可信设置，但各有局限：Hyrax仅支持低深度均匀电路，否则验证开销呈线性；STARK要求电路包含一系列相同子电路，否则增大会导致证明者代价剧增；Ligero、Bulletproofs和Aurora的验证者代价均为$O(n)$。因此，设计一种无需可信设置、支持任意NP语句且验证者开销亚线性的zkSNARK是一个悬而未决的核心问题。本文旨在填补这一空白，提出Spartan系列方案，首次实现透明zkSNARK中验证者开销亚线性且不要求语句具有任何均匀结构，同时提供时间最优的证明者。

### 相关工作

[47] Gennaro等. Quadratic span programs and succinct NIZKs without PCPs. **EUROCRYPT 2013** [Google Scholar](https://scholar.google.com/scholar?q=Quadratic+span+programs+and+succinct+NIZKs+without+PCPs)
> 核心思路：提出二次算术程序（QAP），构造了首个实用的zkSNARK，证明大小$O(1)$，验证开销$O(|io|)$。
> 局限与区别：需要每类语句进行一次可信设置，且设置过程产生$O(n)$大小的公共参考串并需保密陷阱门。Spartan无需可信设置。

[84] Wahby等. Doubly-efficient zkSNARKs without trusted setup. **S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Doubly-efficient+zkSNARKs+without+trusted+setup)
> 核心思路：提出Hyrax，一种透明zkSNARK，利用双效交互证明技术，验证开销亚线性仅对数据并行电路成立。
> 局限与区别：Hyrax的计算模型为分层算术电路，验证开销与电路深度线性相关；任意电路转化为分层形式可能导致平方扩增。Spartan支持任意R1CS实例且验证亚线性。

[10] Ben-Sasson等. Scalable, transparent, and post-quantum secure computational integrity. **ePrint 2018/046** [Google Scholar](https://scholar.google.com/scholar?q=Scalable+transparent+and+post-quantum+secure+computational+integrity)
> 核心思路：提出STARK，基于交互式Oracle证明（IOP），抗量子，证明大小$O(\log^2 n)$。
> 局限与区别：要求电路由一系列相同子电路组成，否则验证开销不亚线性；任意电路转换后增大10-1000倍，导致证明者代价成倍增加。Spartan无此限制。

[16] Ben-Sasson等. Aurora: transparent succinct arguments for R1CS. **EUROCRYPT 2019** [Google Scholar](https://scholar.google.com/scholar?q=Aurora+transparent+succinct+arguments+for+R1CS)
> 核心思路：基于IOP构造透明zkSNARK，直接支持R1CS，证明大小$O(\log^2 n)$。
> 局限与区别：验证者开销为$O(n)$（线性），未实现亚线性验证。Spartan通过计算承诺实现亚线性验证。

[3] Ames等. Ligero: lightweight sublinear arguments without a trusted setup. **CCS 2017** [Google Scholar](https://scholar.google.com/scholar?q=Ligero+lightweight+sublinear+arguments+without+a+trusted+setup)
> 核心思路：利用“MPC in the head”范式构造透明NIZK，证明大小$O(\sqrt{n})$。
> 局限与区别：验证者开销为$O(n)$（线性）。Spartan验证亚线性且证明者更快。

[32] Bünz等. Transparent SNARKs from DARK compilers. **ePrint 2019/1229** [Google Scholar](https://scholar.google.com/scholar?q=Transparent+SNARKs+from+DARK+compilers)
> 核心思路：提出SuperSonic，基于类群假设的透明zkSNARK，证明大小$O(\log n)$。
> 局限与区别：验证者通过预处理实现亚线性，但实际开销较高。Spartan的证明者速度快36-152倍。

[85] Xie等. Libra: succinct zero-knowledge proofs with optimal prover computation. **ePrint 2019/317** [Google Scholar](https://scholar.google.com/scholar?q=Libra+succinct+zero-knowledge+proofs+with+optimal+prover+computation)
> 核心思路：提出Libra，一种证明者时间最优的zkSNARK，支持均匀分层电路。
> 局限与区别：需要私有可信设置，验证开销与电路深度线性相关，不支持任意R1CS。Spartan无需设置且支持任意R1CS。

[86] Zhang等. Transparent polynomial delegation and its applications to zero knowledge proof. **S&P 2020** [Google Scholar](https://scholar.google.com/scholar?q=Transparent+polynomial+delegation+and+its+applications+to+zero+knowledge+proof)
> 核心思路：提出Virgo，基于多项式承诺的透明zkSNARK，计算模型与Hyrax相同。
> 局限与区别：仅在低深度均匀电路上实现亚线性验证。Spartan适用于任意R1CS。

[36] Chiesa等. Fractal: post-quantum and transparent recursive proofs from holography. **ePrint 2019/1076** [Google Scholar](https://scholar.google.com/scholar?q=Fractal+post-quantum+and+transparent+recursive+proofs+from+holography)
> 核心思路：提出Fractal，一种透明zkSNARK，通过全息技术实现验证亚线性。
> 局限与区别：实际开销较高，在$2^{18}$约束下Spartan的证明者快36倍，证明大小短23倍。

### 核心技术与方案

#### 1. 整体框架

Spartan的核心思想是将R1CS实例编码为低次多项式，然后利用和检查协议（sum-check protocol）将验证问题归约为单个多项式求值，再通过多项式承诺方案完成求值证明。整个构造分为三个层次：（a）一种新的R1CS多项式编码，将实例转换为一个次数为3的对数变量多项式；（b）一个公开硬币的简洁交互论证，该论证将和检查协议与可提取多项式承诺方案相结合，实现证明者线性时间、通信亚线性；（c）计算承诺（computation commitments）原语，使验证者通过预处理将矩阵多项式的求值委托给证明者，从而实现验证开销亚线性。为了支持稀疏多项式的高效承诺，进一步提出了spark编译器，它通过离线内存检查技术将稀疏多项式承诺转化为等价的密集多项式承诺。

#### 2. R1CS的多项式编码（Theorem 4.1）

给定R1CS实例$\mathbb{x}=(\mathbb{F},A,B,C,io,m,n)$，令$s=\lceil \log m\rceil$。将矩阵$A,B,C$视为$\{0,1\}^s\times\{0,1\}^s\to\mathbb{F}$的函数，将向量$Z=(io,1,w)$视为$\{0,1\}^s\to\mathbb{F}$的函数。定义函数$F_{io}(x)=\big(\sum_{y}A(x,y)Z(y)\big)\cdot\big(\sum_{y}B(x,y)Z(y)\big)-\sum_{y}C(x,y)Z(y)$，则$\forall x\in\{0,1\}^s$，$F_{io}(x)=0$当且仅当实例可满足。取其多项式扩展$\widetilde{F}_{io}$，并构造$Q_{io}(t)=\sum_{x\in\{0,1\}^s}\widetilde{F}_{io}(x)\cdot\widetilde{\mathrm{eq}}(t,x)$，其中$\widetilde{\mathrm{eq}}$是等式函数的双线性扩展。则$Q_{io}(t)$是零多项式当且仅当$\widetilde{F}_{io}$在超立方体上处处为零。通过随机点$\tau\in_R\mathbb{F}^s$，可检验$Q_{io}(\tau)=0$（Schwartz-Zippel引理给出错误概率$\leq\log m/|\mathbb{F}|$）。因此，定义$G_{io,\tau}(x)=\widetilde{F}_{io}(x)\cdot\widetilde{\mathrm{eq}}(\tau,x)$，这是一个次数为3的$s$变量多项式，其和为0等价于实例可满足。

#### 3. 公开硬币简洁交互论证（Theorem 5.1）

论证流程如下：证明者$\mathcal{P}$首先对证人$w$的多线性扩展$\widetilde{w}$进行多项式承诺（承诺$C$）。验证者$\mathcal{V}$发送随机挑战$\tau$。双方运行第一轮和检查协议验证$\sum_{x}G_{io,\tau}(x)=0$，归约为$e_x\stackrel{?}{=}G_{io,\tau}(r_x)$。为了计算$G_{io,\tau}(r_x)$，需评估$\widetilde{A}(r_x,\cdot),\widetilde{B}(r_x,\cdot),\widetilde{C}(r_x,\cdot)$与$\widetilde{Z}$的内积。$\mathcal{P}$首先发送三个值$v_A,v_B,v_C$分别对应$\overline{A}(r_x),\overline{B}(r_x),\overline{C}(r_x)$，$\mathcal{V}$检验$e_x=(v_A v_B-v_C)\cdot\widetilde{\mathrm{eq}}(r_x,\tau)$。然后$\mathcal{V}$随机选择$r_A,r_B,r_C$，定义$c=r_A v_A+r_B v_B+r_C v_C$，双方运行第二轮和检查协议验证$c\stackrel{?}{=}\sum_{y} M_{r_x}(y)$，其中$M_{r_x}(y)=r_A\widetilde{A}(r_x,y)\widetilde{Z}(y)+r_B\widetilde{B}(r_x,y)\widetilde{Z}(y)+r_C\widetilde{C}(r_x,y)\widetilde{Z}(y)$。这归约为评估$M_{r_x}(r_y)$，其中$\widetilde{Z}(r_y)$通过多项式承诺的Eval协议获得，其余项可由$\mathcal{V}$用$O(n)$计算（或通过计算承诺降为亚线性）。$\mathcal{V}$最终验证$e_y=(r_A v_1+r_B v_2+r_C v_3)\cdot v_Z$，其中$v_1,v_2,v_3$由$\mathcal{P}$提供（通过多项式承诺Eval验证），$v_Z$由$\widetilde{w}(r_y)$计算。

安全证明依赖：和检查协议的完备性和可靠性（错误概率$\ell\mu/|\mathbb{F}|$），以及多项式承诺方案的提取性知识证言。最终得到公开硬币论证，通信量$O(\log m)+$承诺大小+PC.Eval通信。

#### 4. 计算承诺（Computation Commitments）

为了去除验证者的$O(n)$开销，引入预处理：验证者离线计算矩阵$A,B,C$的多线性扩展$\widetilde{A},\widetilde{B},\widetilde{C}$的承诺（通过extractable多项式承诺方案）。在论证中，$\mathcal{V}$不再直接计算$\widetilde{A}(r_x,r_y)$等，而是要求$\mathcal{P}$提供这些值，并通过PC.Eval验证它们与承诺一致。验证者的预处理成本为$O(n)$，但可摊销到后续所有具有相同结构的R1CS实例中。这类似于GGPR的预设置但无需秘密陷阱门。

#### 5. Spark编译器

现有多项式承诺方案对稀疏多项式（如$\widetilde{A}$）的承诺代价高昂，因为其密集表示为稀疏的$n$元组。spark编译器将稀疏多项式承诺转化为等价的密集多项式承诺，同时保持线性时间证明者。核心思想是利用离线内存检查技术构造一个$O(n)$大小的电路，来验证稀疏多项式在给定点的求值。具体地，对于稀疏多项式$\widetilde{M}$（以$\{row_i,col_i,val_i\}$编码），计算$e_{row,i}=\widetilde{\mathrm{eq}}(row_i,r_x), e_{col,i}=\widetilde{\mathrm{eq}}(col_i,r_y)$，然后输出$\sum_{i}val_i\cdot e_{row,i}\cdot e_{col,i}$。该求值可转化为内存检查：维护一个大小为$m$的表，记录$\widetilde{\mathrm{eq}}(\cdot,r_x)$，对$row$序列进行内存操作，通过公共硬币哈希函数$h_\gamma(a,v,t)=a\gamma^2+v\gamma+t$和多重集哈希$\mathcal{H}_\gamma(\mathcal{M})=\prod_{e\in\mathcal{M}}(e-\gamma)$来验证内存操作的正确性。最后通过Hyrax等协议将该电路的满足性证明封装为多项式承诺的Eval协议。spark的开销：证明者$O(n)$，通信$O(\log^2 n)$，验证者$O(\sqrt{n})$（当底层为Hyrax-PC时）或$O(\log^2 n)$（当底层为vSQL-VPD时）。

#### 渐进复杂度总结

不同实例化的复杂度如图2所示：$\text{Spartan}_{\text{DL}}$（基于DLOG假设）证明者$O(n)$，证明大小$O(\sqrt{n})$，验证者$O(\sqrt{n})$；$\text{Spartan}_{\text{KE}}$（基于q-PKE假设）证明者$O(n)$，证明大小$O(\log^2 n)$，验证者$O(\log^2 n)$；$\text{Spartan}_{\text{RO}}$（随机预言机模型）证明者$O(n\log n)$，证明大小$O(\log^2 n)$，验证者$O(\log^2 n)$。

### 核心公式与流程

**[R1CS多项式编码]**
$$F_{io}(x)=\left(\sum_{y}A(x,y)Z(y)\right)\cdot\left(\sum_{y}B(x,y)Z(y)\right)-\sum_{y}C(x,y)Z(y),\quad x\in\{0,1\}^s$$
$$Q_{io}(t)=\sum_{x\in\{0,1\}^s}\widetilde{F}_{io}(x)\cdot\widetilde{\mathrm{eq}}(t,x),\quad \mathcal{G}_{io,\tau}(x)=\widetilde{F}_{io}(x)\cdot\widetilde{\mathrm{eq}}(\tau,x)$$
> 作用：将R1CS可满足性归约为低次多项式在超立方体上的和是否为0。

**[和检查归约]**
$$e_x\gets\langle\mathcal{P}_{SC}(\mathcal{G}_{io,\tau}),\mathcal{V}_{SC}(r_x)\rangle(\mu_1,\ell_1,T_1),\quad T_1=0,\mu_1=\log m,\ell_1=3$$
$$c = r_A v_A + r_B v_B + r_C v_C,\quad e_y\gets\langle\mathcal{P}_{SC}(M_{r_x}),\mathcal{V}_{SC}(r_y)\rangle(\mu_2,\ell_2,T_2),\quad \mu_2=\log m,\ell_2=2$$
> 作用：利用两轮和检查协议将R1CS验证归约为单个多项式求值$\mathcal{G}_{io,\tau}(r_x)$和$M_{r_x}(r_y)$。

**[Spark电路内存检查]**
$$h_\gamma(a,v,t)=a\cdot\gamma^2+v\cdot\gamma+t,\quad \mathcal{H}_\gamma(\mathcal{M})=\prod_{e\in\mathcal{M}}(e-\gamma)$$
$$\mathcal{H}_{\gamma_2}(Init)\cdot\mathcal{H}_{\gamma_2}(WS)=\mathcal{H}_{\gamma_2}(RS)\cdot\mathcal{H}_{\gamma_2}(Audit)$$
> 作用：利用公共硬币哈希验证内存操作序列的正确性，确保稀疏多项式求值与承诺一致。

### 实验结果

实验环境：单核Intel Core i7-1065G7，16GB RAM，Ubuntu 20.04 on Windows 10。评估$2^{10}$到$2^{20}$个约束的R1CS实例。对比基线：Groth16、Hyrax、Ligero、Aurora、Fractal。核心结果：在$2^{20}$约束下，Spartan的SNARK变体（$\text{Spartan}_{\text{SNARK}}$）证明者耗时36.3秒，较Fractal（$2^{18}$约束时337秒）快约36倍；较Ligero（112秒）快约3倍，较Aurora（688秒）快约19倍，较Hyrax（447秒）快约12倍。$\text{Spartan}_{\text{NIZK}}$变体（线性验证）证明者仅4.5秒，较Groth16（76.2秒）快约17倍。证明大小：$\text{Spartan}_{\text{SNARK}}$在$2^{20}$约束下为142KB，比Fractal（2.3MB）短约16倍，比Aurora（1.6MB）短约11倍，比Ligero（20MB）短约140倍。验证时间：$\text{Spartan}_{\text{SNARK}}$为100.3ms，较Fractal（204ms）快约2倍，较Ligero（38.5s）快约383倍，较Aurora（133s）快约1326倍，较Hyrax（8.1s）快约80倍。预处理器时间：$\text{Spartan}_{\text{SNARK}}$在$2^{20}$约束下需15.1秒，较Fractal（389秒）快约26倍，较Groth16（71.9秒）快约4.7倍。

### 局限性与开放问题

Spartan的SNARK变体需要预处理（编码器），该预处理开销为$O(n)$，虽然可摊销，但单次证明场景下总成本仍高于NIZK变体。当前实现的spark编译器依赖于Hyrax-PC，证明大小和验证时间均为$O(\sqrt{n})$，在超大规模实例下不如$O(\log^2 n)$方案。此外，所有变体的安全假设需在标准模型下进一步验证；例如$\text{Spartan}_{\text{DL}}$依赖随机预言机和离散对数假设，后量子安全需求下可能需要切换到抗量子假设的承诺方案。最后，将Spartan扩展为递归证明（如Halo-like）和实际应用中的端到端集成仍有待探索。

### 强关联论文

[47] Gennaro R., Gentry C., Parno B., Raykova M. Quadratic span programs and succinct NIZKs without PCPs. **EUROCRYPT 2013** [Google Scholar](https://scholar.google.com/scholar?q=Quadratic+span+programs+and+succinct+NIZKs+without+PCPs)

[84] Wahby R.S., Tzialla I., Shelat A., Thaler J., Walfish M. Doubly-efficient zkSNARKs without trusted setup. **S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Doubly-efficient+zkSNARKs+without+trusted+setup)

[10] Ben-Sasson E., Bentov I., Horesh Y., Riabzev M. Scalable, transparent, and post-quantum secure computational integrity. **ePrint 2018/046** [Google Scholar](https://scholar.google.com/scholar?q=Scalable+transparent+and+post-quantum+secure+computational+integrity)

[16] Ben-Sasson E., Chiesa A., Riabzev M., Spooner N., Virza M., Ward N.P. Aurora: transparent succinct arguments for R1CS. **EUROCRYPT 2019** [Google Scholar](https://scholar.google.com/scholar?q=Aurora+transparent+succinct+arguments+for+R1CS)

[3] Ames S., Hazay C., Ishai Y., Venkitasubramaniam M. Ligero: lightweight sublinear arguments without a trusted setup. **CCS 2017** [Google Scholar](https://scholar.google.com/scholar?q=Ligero+lightweight+sublinear+arguments+without+a+trusted+setup)

[85] Xie T., Zhang J., Zhang Y., Papamanthou C., Song D. Libra: succinct zero-knowledge proofs with optimal prover computation. **ePrint 2019/317** [Google Scholar](https://scholar.google.com/scholar?q=Libra+succinct+zero-knowledge+proofs+with+optimal+prover+computation)

[86] Zhang J., Xie T., Zhang Y., Song D. Transparent polynomial delegation and its applications to zero knowledge proof. **S&P 2020** [Google Scholar](https://scholar.google.com/scholar?q=Transparent+polynomial+delegation+and+its+applications+to+zero+knowledge+proof)

[36] Chiesa A., Ojha D., Spooner N. Fractal: post-quantum and transparent recursive proofs from holography. **ePrint 2019/1076** [Google Scholar](https://scholar.google.com/scholar?q=Fractal+post-quantum+and+transparent+recursive+proofs+from+holography)

[87] Zhang Y., Genkin D., Katz J., Papadopoulos D., Papamanthou C. vSQL: verifying arbitrary SQL queries over dynamic outsourced databases. **S&P 2017** [Google Scholar](https://scholar.google.com/scholar?q=vSQL+verifying+arbitrary+SQL+queries+over+dynamic+outsourced+databases)

[32] Bünz B., Fisch B., Szepieniec A. Transparent SNARKs from DARK compilers. **ePrint 2019/1229** [Google Scholar](https://scholar.google.com/scholar?q=Transparent+SNARKs+from+DARK+compilers)


## 关键词

+ Spartan透明zkSNARK无可信设置
+ R1CS次线性验证计算承诺
+ spark稀疏多线性多项式编译器
+ 和谐检查协议SNARK构造
+ 离散对数假设最优证明者