---
title: "ZKSQL: Verifiable and Efficient Query Evaluation with Zero-Knowledge Proofs"
标题简称:
论文类型: conference
会议简称: VLDB
发表年份: 2023

modified: 2025-04-09 14:00:47
---

## ZKSQL: Verifiable and Efficient Query Evaluation with Zero-Knowledge Proofs

## 发表信息

+ [原文链接](https://dl.acm.org/doi/10.14778/3594512.3594513)

## 作者

+ Xiling Li
+ [Chenkai Weng](Chenkai%20Weng.md)
+ Yongxin Xu
+ [Xiao Wang](Xiao%20Wang.md)
+ Jennie Rogers

## 笔记

### 背景与动机
数据库广泛存储个人隐私信息，数据提供者既要保护隐私，又需在监管场景（如美国SEC申报）中提供正确的聚合统计结果。传统数据库无法同时保证答案的正确性（完整性）与数据的保密性。零知识证明（ZK proofs）理论上可解决这一矛盾，但直接对SQL查询执行采用电路式ZK证明会产生5–6个数量级的性能开销。现有方案如IntegriDB [34] 和vSQL [32] 仅提供完整性（无零知识），而vSQL的ZK扩展 [33] 不支持ad-hoc查询且未实现。本文旨在填补这一空白：提出首个支持ad-hoc SQL查询的零知识验证系统ZKSQL，在保持正确性、完备性、零知识的前提下，实现可实用的性能。

### 相关工作

[2] Bajaj等. CorrectDB: SQL engine with practical query authentication. **PVLDB 2013** [Google Scholar](https://scholar.google.com/scholar?q=CorrectDB+SQL+engine+with+practical+query+authentication)
> 核心思路：基于可信硬件的SQL查询认证。
> 局限与区别：不提供零知识，泄露程序轨迹信息；ZKSQL基于密码学协议，不依赖特殊硬件。

[34] Zhang等. IntegriDB: Verifiable SQL for Outsourced Databases. **ACM CCS 2015** [Google Scholar](https://scholar.google.com/scholar?q=IntegriDB+Verifiable+SQL+for+Outsourced+Databases)
> 核心思路：可验证计算协议用于外包数据库查询。
> 局限与区别：仅保障完整性，不提供零知识；ZKSQL同时提供零知识。

[32] Zhang等. vSQL: Verifying Arbitrary SQL Queries over Dynamic Outsourced Databases. **IEEE S&P 2017** [Google Scholar](https://scholar.google.com/scholar?q=vSQL+Verifying+Arbitrary+SQL+Queries+over+Dynamic+Outsourced+Databases)
> 核心思路：验证任意SQL查询的正确性。
> 局限与区别：外包场景，无零知识；ZKSQL支持prover持有私有数据库的证明。

[33] Zhang等. A Zero-Knowledge Version of vSQL. **ePrint 2017** [Google Scholar](https://scholar.google.com/scholar?q=A+Zero-Knowledge+Version+of+vSQL)
> 核心思路：从vSQL扩展零知识。
> 局限与区别：理论框架，未实现ad-hoc查询；ZKSQL给出完整系统实现并支持任意SQL。

[5] Baum等. Mac’n’Cheese: Zero-Knowledge Proofs for Boolean and Arithmetic Circuits with Nested Disjunctions. **CRYPTO 2021** [Google Scholar](https://scholar.google.com/scholar?q=Mac%27n%27Cheese+Zero-Knowledge+Proofs+for+Boolean+and+Arithmetic+Circuits+with+Nested+Disjunctions)
> 核心思路：基于VOLE的高效ZK协议。
> 区别：ZKSQL将其作为底层密码后端，并构建高级SQL算子协议。

[12] Dittmer等. Line-Point Zero Knowledge and Its Applications. **ITC 2021** [Google Scholar](https://scholar.google.com/scholar?q=Line-Point+Zero+Knowledge+and+Its+Applications)
> 核心思路：line-point ZK协议。
> 区别：同[5]，为ZKSQL提供电路级基础。

[29] Weng等. Wolverine: Fast, Scalable, and Communication-Efficient Zero-Knowledge Proofs for Boolean and Arithmetic Circuits. **IEEE S&P 2021** [Google Scholar](https://scholar.google.com/scholar?q=Wolverine+Fast+Scalable+and+Communication-Efficient+Zero-Knowledge+Proofs+for+Boolean+and+Arithmetic+Circuits)
> 核心思路：VOLE-based ZK，通信高效。
> 区别：ZKSQL在此之上实现SQL算子。

[30] Yang等. QuickSilver: Efficient and Affordable Zero-Knowledge Proofs for Circuits and Polynomials over Any Field. **ACM CCS 2021** [Google Scholar](https://scholar.google.com/scholar?q=QuickSilver+Efficient+and+Affordable+Zero-Knowledge+Proofs+for+Circuits+and+Polynomials+over+Any+Field)
> 核心思路：VOLE-based ZK，支持任意域。
> 区别：用作ZKSQL的底层协议。

[13] Franzese等. Constant-Overhead Zero-Knowledge for RAM Programs. **ACM CCS 2021** [Google Scholar](https://scholar.google.com/scholar?q=Constant-Overhead+Zero-Knowledge+for+RAM+Programs)
> 核心思路：set equality的多项式方法。
> 区别：ZKSQL借用其多项式方法优化集合操作。

[28] Wang等. EMP-toolkit: Efficient MultiParty computation toolkit. **GitHub 2016** [Google Scholar](https://scholar.google.com/scholar?q=EMP-toolkit+Efficient+MultiParty+computation+toolkit)
> 核心思路：多方计算与ZK框架。
> 区别：ZKSQL基于此实现。

### 核心技术与方案

ZKSQL采用commit-and-prove范式：prover $\mathcal{P}$ 首先对其私有数据库 $D$ 的每一位进行认证承诺，生成 $[D]_{\mathcal{P}}$ 和 $[D]_{\mathcal{V}}$（$\mathcal{P}$ 与 $\mathcal{V}$ 各自持有份额，满足 $[D]_{\mathcal{P}} = [D]_{\mathcal{V}} + D \cdot \Delta_{\mathcal{V}}$）。这一承诺一次完成，可支持后续任意多次查询，且不泄露 $D$ 的内容。$\mathcal{V}$ 仅知道 $D$ 的schema和每张表的基数，以及 $[D]_{\mathcal{V}}$ 和密钥 $\Delta_{\mathcal{V}}$。查询阶段，双方根据SQL语句解析出算子DAG，分层生成认证的中间结果，最终输出查询答案 $A$ 及其认证标签 $[A]$，并调用Verify协议证明 $[A]$ 等于公开承诺的答案 $A$。

系统分为电路基础协议和集合基础协议两种构造。电路基础协议直接通过 $\mathcal{F}_{\mathrm{ZK}}$ 的Compute和Verify功能实现算子逻辑，如Project、Filter、Aggregate。以Filter为例：对每个输入元组 $[r_i]$，双方计算布尔电路 $C_p$ 判定是否满足谓词 $p$，输出 $[t_i]$；若 $p$ 为真且 $r_i$ 非dummy，则 $t_i$ 保持非dummy，否则标记为dummy（tombstone）。为保持 oblivious，输出表基数与输入相同，必要时通过排序dummy标签并截断进行padding。Aggregate先按group-by属性排序，再逐元组累积聚合状态，同一group内仅保留一个非dummy元组。

集合基础协议（Sort、Join）借助 $\mathcal{F}_{\mathrm{ZKSET}}$（图3）实现。对于Sort，$\mathcal{P}$ 本地排序后输入 $[T]$，然后双方执行Equality检查 $[T]$ 与 $[R]$ 是否集合相等，再执行 $(n-1)$ 次比较电路检查 $[t_i] \leq [t_{i+1}]$（按排序定义 $S$）。联合Join的验证需三条：谓词检查（每行非dummy时满足join谓词）、集合差检查（$U \subseteq R$ 且 $\Delta_R = R \setminus U$ 类似对 $S$）、不交检查（$K_R \cap K_S = \emptyset$，即未参与join的key无匹配）。其中Equality采用Schwartz-Zippel引理：$\mathcal{V}$ 选取随机点 $a \in \mathbb{F}_{2^\kappa}$，双方计算 $\prod_{i=1}^n ([r_i]-a) - \prod_{i=1}^n ([s_i]-a)$，若等于0则接受。Disjoint通过构造排序后的合并表并检查相邻不相等实现。Intersection和Union作为辅助。

安全性方面，ZKSQL在 $\mathcal{F}_{\mathrm{ZK}}$ 混合模型下证明协议 $\Pi_{\mathrm{ZKSET}}$ 和 $\Pi_{\mathrm{SET\_OP}}$ UC-实现 $\mathcal{F}_{\mathrm{ZKSET}}$ 和 $\mathcal{F}_{\mathrm{ZKSQL}}$。电路部分直接依赖底层VOLE协议的安全性（见[30]）。集合协议的安全性基于：Equality的soundness error为 $n/2^\kappa$；Disjoint错误为 $O(n/2^\kappa)$。零知识性质通过模拟器模拟$\mathcal{V}$的视图证明，对于恶意$\mathcal{P}$则通过提取其输入并发送到理想功能来保证。

渐进复杂度：所有集合操作（Equality, Disjoint, Intersection, Union）为 $O(n)$（$n$为表元组数）通信和计算；Sort的order check需 $O(n\log n)$ 个比较门，但Equality仅 $O(n)$；Join中谓词检查为 $O(m)$ （$m$为输出元组数），集合差和不交检查各为 $O(n)$。与纯电路基准（$O(n\log^2 n)$ 或更多）相比，集合操作大幅降低了开销。

### 核心公式与流程

**[承诺关系]**
$$[D]_{\mathcal{P}} = [D]_{\mathcal{V}} + D \cdot \Delta_{\mathcal{V}}$$
> 作用：描述prover与verifier共享的认证标签关系，$[D]_{\mathcal{P}}$ 和 $[D]_{\mathcal{V}}$ 分别为双方持有的份额，$\Delta_{\mathcal{V}}$ 仅verifier知道。

**[Set Equality (Schwartz-Zippel)]**
$$\prod_{i=1}^n ([r_i] - a) - \prod_{i=1}^n ([s_i] - a) \stackrel{?}{=} 0$$
> 作用：随机点 $a \in \mathbb{F}_{2^\kappa}$ 下，若两个多项式恒等则值为0，否则以概率 $\leq n/2^\kappa$ 误判。

**[Packing函数]**
$$[t_i'] \gets \sum_{k=1}^{d} c_k \cdot \left( \sum_{j=1}^{\kappa} [t_i^{k\cdot \kappa + j}] \cdot X^{j-1} \right)$$
> 作用：将 $m$ 比特元组通过线性哈希压缩为 $\kappa$ 比特，用于集合操作前降维，其中 $d = \lceil m/\kappa \rceil$，系数 $c_k$ 由 $\mathcal{V}$ 随机选取。

**[Sort验证流程]**
1. $\mathcal{P}$ 本地排序得 $R_{\mathbb{S}}$，双方输入 $[T]$；  
2. Equality($[R]$, $[T]$)；  
3. 对 $i \in [n-1]$ 调用 Verify($C_{\mathbb{S}}$, $[t_i]$, $[t_{i+1}]$) 验证单调性。
> 作用：无需跟踪排序过程，仅需证明集合相等且顺序正确。

**[Join验证流程]**
1. $\mathcal{P}$ 本地计算 $T \gets R \bowtie_p S$，双方输入 $[T]$；  
2. 对每行调用 Verify($C_p$, $[t_i]$) 验证谓词；  
3. 提取 $[U] \gets \pi_{R\text{ columns}}([T])$, $[V] \gets \pi_{S\text{ columns}}([T])$；  
4. $\mathcal{P}$ 输入 $\Delta_R \gets R \setminus U$, $\Delta_S \gets S \setminus V$；  
5. Equality($\Delta_R||U$, $R$) 且 Equality($\Delta_S||V$, $S$)；  
6. 投影 $[K_R] \gets \pi_{p_R}([\Delta_R])$, $[K_S] \gets \pi_{p_S}([\Delta_S])$；  
7. Disjoint($[K_R]$, $[K_S]$)。
> 作用：通过集合差和不交性证明输出 $T$ 恰为所有匹配元组，无遗漏无冗余。

### 实验结果

实验基于TPC-H子集查询（Q1, Q3, Q5, Q8, Q9, Q18），使用24核AWS EC2 r6i.4xlarge实例（128 GB RAM，12.5 Gbps网络），数据库规模分为60k行、120k行、240k行lineitem表。与纯电路基线（Circuit-Only）对比：ZKSQL集合优化实现平均两个数量级加速，最大加速比为Q18达到410倍（因Q18多表join且无算术表达式）。Q1（多聚合但少join）加速比仅2倍。相对于无padding（泄露中间基数）版本，oblivious padding带来最大12倍（Q8）或10.5倍（Q18）性能惩罚。网络瓶颈测试显示，带宽降至5 Mbps时仅约2倍减速，证明系统主要受计算而非通信限制。按数据库规模扩展：绝大多数查询运行时随数据量线性增长，Q9因行宽较大导致3倍减速。财务成本估算：60k行下ZKSQL每查询成本0.04–0.42美元，而Circuit-Only基线为0.22–35.39美元，总成本从74.28美元降至0.89美元（60k行）。承诺阶段（一次设置）仅占总运行时0.6%，总通信量1.1%。

### 局限性与开放问题

ZKSQL仅支持等值连接（equi-join），更复杂的连接谓词（如不等式、模式匹配）需借助笛卡尔积加过滤，开销巨大。当前算子顺序优化（如投影下推、过滤合并）仍有改进空间，以进一步减少数据传递。系统对浮点运算的ZK证明开销极高（实验中转换为64位整数），未来可探索更高效的浮点ZK方案。此外，Join中基本join的输出基数固定为 $|R| \times |S|$ 会导致大量padding，仅主键-外键连接可自动优化，其他场景效率较低。

### 强关联论文

[2] Sumeet Bajaj and Radu Sion. CorrectDB: SQL engine with practical query authentication. **PVLDB 2013** [Google Scholar](https://scholar.google.com/scholar?q=CorrectDB+SQL+engine+with+practical+query+authentication)

[5] Carsten Baum, Alex J. Malozemoff, Marc B. Rosen, and Peter Scholl. Mac’n’Cheese: Zero-Knowledge Proofs for Boolean and Arithmetic Circuits with Nested Disjunctions. **CRYPTO 2021** [Google Scholar](https://scholar.google.com/scholar?q=Mac%27n%27Cheese+Zero-Knowledge+Proofs+for+Boolean+and+Arithmetic+Circuits+with+Nested+Disjunctions)

[12] Samuel Dittmer, Yuval Ishai, and Rafail Ostrovsky. Line-Point Zero Knowledge and Its Applications. **ITC 2021** [Google Scholar](https://scholar.google.com/scholar?q=Line-Point+Zero+Knowledge+and+Its+Applications)

[13] Nicholas Franzese, Jonathan Katz, Steve Lu, Rafail Ostrovsky, Xiao Wang, and Chenkai Weng. Constant-Overhead Zero-Knowledge for RAM Programs. **ACM CCS 2021** [Google Scholar](https://scholar.google.com/scholar?q=Constant-Overhead+Zero-Knowledge+for+RAM+Programs)

[28] Xiao Wang, Alex J. Malozemoff, and Jonathan Katz. EMP-toolkit: Efficient MultiParty computation toolkit. **GitHub 2016** [Google Scholar](https://scholar.google.com/scholar?q=EMP-toolkit+Efficient+MultiParty+computation+toolkit)

[29] Chenkai Weng, Kang Yang, Jonathan Katz, and Xiao Wang. Wolverine: Fast, Scalable, and Communication-Efficient Zero-Knowledge Proofs for Boolean and Arithmetic Circuits. **IEEE S&P 2021** [Google Scholar](https://scholar.google.com/scholar?q=Wolverine+Fast+Scalable+and+Communication-Efficient+Zero-Knowledge+Proofs+for+Boolean+and+Arithmetic+Circuits)

[30] Kang Yang, Pratik Sarkar, Chenkai Weng, and Xiao Wang. QuickSilver: Efficient and Affordable Zero-Knowledge Proofs for Circuits and Polynomials over Any Field. **ACM CCS 2021** [Google Scholar](https://scholar.google.com/scholar?q=QuickSilver+Efficient+and+Affordable+Zero-Knowledge+Proofs+for+Circuits+and+Polynomials+over+Any+Field)

[32] Yupeng Zhang, Daniel Genkin, Jonathan Katz, Dimitrios Papadopoulos, and Charalampos Papamanthou. vSQL: Verifying Arbitrary SQL Queries over Dynamic Outsourced Databases. **IEEE S&P 2017** [Google Scholar](https://scholar.google.com/scholar?q=vSQL+Verifying+Arbitrary+SQL+Queries+over+Dynamic+Outsourced+Databases)

[33] Yupeng Zhang, Daniel Genkin, Jonathan Katz, Dimitrios Papadopoulos, and Charalampos Papamanthou. A Zero-Knowledge Version of vSQL. **ePrint 2017** [Google Scholar](https://scholar.google.com/scholar?q=A+Zero-Knowledge+Version+of+vSQL)

[34] Yupeng Zhang, Jonathan Katz, and Charalampos Papamanthou. IntegriDB: Verifiable SQL for Outsourced Databases. **ACM CCS 2015** [Google Scholar](https://scholar.google.com/scholar?q=IntegriDB+Verifiable+SQL+for+Outsourced+Databases)


## 关键词

+ ZKSQL零知识SQL查询验证
+ 隐私保护数据库查询
+ 认证集合运算
+ SQL查询完整性证明
+ 监管数据隐私合规
+ 零知识证明数据统计