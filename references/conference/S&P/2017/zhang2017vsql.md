---
title: "vSQL: Verifying arbitrary SQL queries over dynamic outsourced databases"
doi: 10.1109/sp.2017.43
标题简称:
论文类型: conference
会议简称: S&P
发表年份: 2017
---
## VSQL: Verifying arbitrary SQL queries over dynamic outsourced databases

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/7958614)

## 作者

+ [Yupeng Zhang](Yupeng%20Zhang.md) 
+ Daniel Genkin 
+ [Jonathan Katz](Jonathan%20Katz.md) 
+ [Dimitrios Papadopoulos](Dimitrios%20Papadopoulos.md) 
+ [Charalampos Papamanthou](Charalampos%20Papamanthou.md) 


## 笔记

### 背景与动机

云数据库服务（如 Amazon RDS、Google Cloud SQL）允许用户将大型数据库外包给服务器，并通过 SQL 查询获取结果。然而，服务器可能不可信，用户需要验证返回结果的正确性。已有的解决方案存在显著缺陷：通用方案（如 SNARKs）可验证任意计算，但服务器开销过高；专用方案（如认证数据结构）仅支持特定查询类型，表达能力有限。现有系统无法同时满足高效率、强表达和动态更新的需求。vSQL 旨在填补这一空白，首次实现支持任意 SQL 查询（包括更新）的公开可验证数据库系统，且服务器计算量与输入输出规模呈线性关系，与电路大小无关。

### 相关工作

[25] Cormode et al. Practical verified computation with streaming interactive proofs. **ITCS 2012** [Google Scholar](https://scholar.google.com/scholar?q=Practical+verified+computation+with+streaming+interactive+proofs)
> 核心思路：提出 CMT 交互式证明协议，将电路求值分解为逐层求和校验，验证开销与电路深度和层规模呈多项式对数关系，服务器开销与电路规模呈线性关系。
> 局限与区别：CMT 协议假设输入为验证者已知，不支持外包输入和辅助输入。vSQL 通过多项式委托扩展 CMT 以支持外包数据库和非确定性计算。

[56] Vu et al. A hybrid architecture for interactive verifiable computation. **S&P 2013** [Google Scholar](https://scholar.google.com/scholar?q=A+hybrid+architecture+for+interactive+verifiable+computation)
> 核心思路：结合 CMT 协议与 SNARK 架构，支持非确定性计算，但需将整个辅助输入发送给验证者。
> 局限与区别：当辅助输入规模与数据库相当时，通信开销不可接受。vSQL 使用多项式委托对辅助输入做承诺，仅需传输简短证明，避免了大量通信。

[51] Parno et al. Pinocchio: Nearly practical verifiable computation. **S&P 2013** [Google Scholar](https://scholar.google.com/scholar?q=Pinocchio%3A+Nearly+practical+verifiable+computation)
> 核心思路：基于 SNARK 的通用验证计算系统，证明尺寸恒定。
> 局限与区别：服务器时间与电路规模呈拟线性关系，且需要查询依赖的预计算。vSQL 的服务器时间主要取决于输入/输出规模，无需针对每个查询预计算，速度提升 5–120 倍。

[60] Zhang et al. IntegriDB: Verifiable SQL for outsourced databases. **CCS 2015** [Google Scholar](https://scholar.google.com/scholar?q=IntegriDB%3A+Verifiable+SQL+for+outsourced+databases)
> 核心思路：支持 SQL 子集（如选择、投影）的专用验证系统。
> 局限与区别：仅支持有限查询类型，连接查询等复杂操作无法直接处理。vSQL 支持任意 SQL 查询，且性能可比甚至优于 IntegriDB。

[39] Kate et al. Constant-size commitments to polynomials and their applications. **ASIACRYPT 2010** [Google Scholar](https://scholar.google.com/scholar?q=Constant-size+commitments+to+polynomials+and+their+applications)
> 核心思路：提出多项式承诺方案，用于可验证多项式求值。
> 局限与区别：该方案缺乏知识提取性质。vSQL 在其基础上增加双线性对验证以支持知识健全性，确保恶意服务器必须“知道”一个合法多项式。

[49] Papamanthou et al. Signatures of correct computation. **TCC 2013** [Google Scholar](https://scholar.google.com/scholar?q=Signatures+of+correct+computation)
> 核心思路：扩展多项式委托到多元情形，支持变量度约束。
> 局限与区别：未提供知识提取性质。vSQL 通过修改承诺格式（包含两个相关指数元素）实现提取性。

[4] libsnark: A C++ library for zkSNARK proofs. [Google Scholar](https://scholar.google.com/scholar?q=libsnark%3A+A+C%2B%2B+library+for+zkSNARK+proofs)
> 核心思路：SNARK 系统的高效实现，是 vSQL 的主要对比基线。
> 局限与区别：服务器时间巨大，无法处理动态更新。vSQL 服务器时间快 5–120 倍。

[54] Thaler. Time-optimal interactive proofs for circuit evaluation. **CRYPTO 2013** [Google Scholar](https://scholar.google.com/scholar?q=Time-optimal+interactive+proofs+for+circuit+evaluation)
> 核心思路：优化 CMT 协议，实现时间最优的交互式证明。
> 局限与区别：仍需要验证者已知输入。vSQL 的优化技术（如零测试、避免中继门）借鉴了其思路。

### 核心技术与方案

vSQL 的整体框架结合了 CMT 交互式证明协议和可提取可验证多项式委托协议。首先，在预处理阶段，客户端将数据库 $D$ 视为数组，计算其多重线性扩展 $\tilde{D}$，并使用多项式委托协议的 Commit 算法生成承诺 $\mathsf{com}$ 存储于本地，同时将 $D$ 上传至服务器。该承诺 $\mathsf{com}$ 是常数大小的群元素对 $(c_1, c_2)$，满足 $c_1 = g^{\tilde{D}(s_1,\dots,s_\ell)}, c_2 = g^{\alpha \tilde{D}(s_1,\dots,s_\ell)}$，其中秘密参数 $s_i,\alpha$ 由 KeyGen 生成。

查询阶段分为选择和更新两类。对于选择查询，服务器计算辅助输入（如用于零测试的逆元、排序后的数组），并对其多重线性扩展分别生成承诺。然后运行 CMT 协议的前两步（输出中间值 $r_d, a_d$）。在最后一步，客户端需要验证 $\tilde{V}_d(r_d) = a_d$，其中 $\tilde{V}_d$ 是电路输入层的多重线性扩展。客户端随机选择向量 $\rho^{(i)}$，服务器返回 $\tilde{B}_i(r_d')$ 及其多项式委托证明 $\pi_i$。客户端通过 Ver 验证所有承诺的正确性，然后利用多重线性扩展的线性组合性质（公式 (2)）结合所有 $v_i$ 计算 $\tilde{V}_d(r_d)$，并与 $a_d$ 比对。这种设计使得客户端仅需执行常数次双线性配对运算，工作量与输入输出规模呈亚线性关系。

对于更新查询，服务器先获取新数据库 $D'$，对其多重线性扩展 $\tilde{V}_{\text{out}}$ 计算新承诺 $\mathsf{com}_{\text{out}}$。客户端随机选择 $r_0$，服务器返回 $a_0 = \tilde{V}_{\text{out}}(r_0)$ 及其证明。客户端验证该承诺后，将 $r_0, a_0$ 作为 CMT 协议第二阶段的起点，继续运行 CMT 直至输入层，最后通过与选择查询相同的方式验证输入层的值。若验证通过，客户端将本地承诺更新为 $\mathsf{com}_{\text{out}}$。这种分离策略避免了在电路中嵌入承诺计算，将服务器开销控制在 $O(|C| \log S')$。

安全性依赖于两个假设：$q$-强 Diffie-Hellman 假设（Assumption 1）和 $(\ell,d)$-Power Knowledge of Exponent 假设（Assumption 2）。前者保证对手无法伪造合法的多项式承诺；后者保证如果对手能生成满足配对等式的有效证明，则存在提取器可恢复出对应的多项式。完备性和可靠性分别在 Theorem 3 和 Theorem 4 中给出证明思路。系统渐进复杂度：客户端设置时间 $O(|D|)$，查询交互轮数 $O(d \log S)$，客户验证时间 $O(k + d \cdot \text{poly}\log(S) + \log(|B|+|D|))$，服务器计算时间 $O(|C| \cdot \log S' + (|B|+|D|)\log(|B|+|D|))$。

### 核心公式与流程

**[多项式委托协议的Verify方程]**
$$e(c_1/g^{y}, g) = e(g^{s_\ell - t_\ell}, g^{q_\ell(s_\ell)}) \cdot \prod_{i=1}^{\ell-1} e(g^{r_i(s_i-t_i)+s_{i+1}-t_{i+1}}, \pi_i)$$
> 作用：验证承诺 com 对应的多项式在点 t 处的求值 y 是否正确，同时检查承诺的格式（第二个方程 $e(c_1,g^\alpha)=e(c_2,g)$ 确保提取性）。

**[多重线性扩展的组合公式]**
$$\tilde{A}(x_1,\dots,x_{\log(nm)}) = \sum_{i=0}^{m-1} \prod_{j=1}^{\log m} \mathcal{X}_{i_j}(x_j) \tilde{A}_i(x_{\log m+1},\dots,x_{\log(nm)})$$
> 作用：将多个等长数组的扩展多项式合并为一个整体扩展的求值，实现客户端无需知道全部输入即可通过服务器返回的部分求值和线性组合得到最终求值。

**[CMT协议第i层递归公式]**
$$\tilde{V}_i(z) = \sum_{\substack{g\in\{0,1\}^{s_i}\\u,v\in\{0,1\}^{s_{i+1}}}} \tilde{\beta}_i(z,g)\cdot \left(\tilde{\mathsf{add}}_{i+1}(g,u,v)\cdot(\tilde{V}_{i+1}(u)+\tilde{V}_{i+1}(v)) + \tilde{\mathsf{mult}}_{i+1}(g,u,v)\cdot(\tilde{V}_{i+1}(u)\cdot\tilde{V}_{i+1}(v))\right)$$
> 作用：将电路第 i+1 层的输出与第 i 层的输入关联，利用 sum-check 协议逐层将求值问题归约至输入层，最终验证者只需检查输入层的多重线性扩展求值。

**[零测试的非确定性电路构造]**
$$x' = x \cdot y,\quad z = x \cdot (1 - x \cdot y)$$
> 作用：若 $x \neq 0$，服务器可设 $y = x^{-1}$，此时 $x'=1, z=0$；若 $x=0$，则任何 $y$ 均得 $x'=0, z=0$。客户端通过两个 CMT 实例分别验证 $z=0$ 和 $x'$ 被正确用于后续电路，实现高效的零测试。

### 实验结果

实验在 Amazon EC2 c4.8xlarge 机器（60GB RAM，36 核）上进行，WAN 网络延迟 72ms，带宽 9MB/s。使用 TPC-H 基准测试数据集，最大表含 600 万行、13 列。对比基线包括 IntegriDB（专用系统）和 libsnark（通用 SNARK 实现）。vSQL 的设置时间约 2467 秒，而 IntegriDB 因内存消耗无法完成设置，估计约 350000 秒。对于查询 #19（范围查询+连接+聚合），vSQL 服务器时间 4892 秒，客户端 162ms，总时间（WAN）4957 秒，IntegriDB 服务器时间 6376 秒，客户端 232ms，vSQL 快约 23%。对于查询 #5（多路连接+嵌套查询），IntegriDB 不支持，vSQL 服务器 5069 秒，客户端 398ms。与 SNARK 对比，libsnark 估计服务器时间 196000 秒（#19）至 615000 秒（#5），vSQL 快 5–120 倍。vSQL 客户端验证时间（对数级增长）始终低于 0.5 秒。通信量在 85.7KB 以下。

### 局限性与开放问题

vSQL 的理论支持所有可表示为非确定性算术电路的 SQL 查询，但未实现子字符串和通配符查询，这些操作需要额外电路优化。对于较为复杂的嵌套查询或递归 SQL（Turing 完备变体），一般电路归约的效率较低。未来工作可探索更高效的电路生成技术，以及将本文的多项式委托协议扩展到支持更多通用计算模型（如 RAM 程序）以处理复杂操作。

### 强关联论文

[25] Cormode et al. Practical verified computation with streaming interactive proofs. **ITCS 2012** [Google Scholar](https://scholar.google.com/scholar?q=Practical+verified+computation+with+streaming+interactive+proofs)

[56] Vu et al. A hybrid architecture for interactive verifiable computation. **S&P 2013** [Google Scholar](https://scholar.google.com/scholar?q=A+hybrid+architecture+for+interactive+verifiable+computation)

[51] Parno et al. Pinocchio: Nearly practical verifiable computation. **S&P 2013** [Google Scholar](https://scholar.google.com/scholar?q=Pinocchio%3A+Nearly+practical+verifiable+computation)

[60] Zhang et al. IntegriDB: Verifiable SQL for outsourced databases. **CCS 2015** [Google Scholar](https://scholar.google.com/scholar?q=IntegriDB%3A+Verifiable+SQL+for+outsourced+databases)

[39] Kate et al. Constant-size commitments to polynomials and their applications. **ASIACRYPT 2010** [Google Scholar](https://scholar.google.com/scholar?q=Constant-size+commitments+to+polynomials+and+their+applications)

[49] Papamanthou et al. Signatures of correct computation. **TCC 2013** [Google Scholar](https://scholar.google.com/scholar?q=Signatures+of+correct+computation)

[4] libsnark: A C++ library for zkSNARK proofs. **2014** [Google Scholar](https://scholar.google.com/scholar?q=libsnark%3A+A+C%2B%2B+library+for+zkSNARK+proofs)

[54] Thaler. Time-optimal interactive proofs for circuit evaluation. **CRYPTO 2013** [Google Scholar](https://scholar.google.com/scholar?q=Time-optimal+interactive+proofs+for+circuit+evaluation)

[33] Goldwasser et al. Delegating computation: interactive proofs for muggles. **STOC 2008** [Google Scholar](https://scholar.google.com/scholar?q=Delegating+computation%3A+interactive+proofs+for+muggles)

[44] Lund et al. Algebraic methods for interactive proof systems. **J. ACM 1992** [Google Scholar](https://scholar.google.com/scholar?q=Algebraic+methods+for+interactive+proof+systems)


## 关键词

+ 可验证SQL查询
+ 交互证明协议
+ 云数据库验证
+ 多项式委托协议
+ 动态数据库
+ CMT协议扩展