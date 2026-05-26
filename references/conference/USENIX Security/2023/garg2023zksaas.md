---
title: "zkSaaS: Zero-KnowledgeSNARKs as a Service"
标题简称:
论文类型: conference
会议简称: USENIX Security
发表年份: 2023
modified: 2025-04-11 11:17:00
---

## zkSaaS: Zero-KnowledgeSNARKs as a Service

## 发表信息

+ [原文链接](https://www.usenix.org/conference/usenixsecurity23/presentation/garg)

## 作者

+ [Sanjam Garg](Sanjam%20Garg.md) 
+ [Aarushi Goel](Aarushi%20Goel.md)
+ [Abhishek Jain](Abhishek%20Jain.md)
+ [Guru-Vamsi Policharla](Guru-Vamsi%20Policharla.md)
+ Sruthi Sekar 

## 笔记

### 背景与动机
零知识简明非交互知识论证（zk-SNARKs）经过十年研究已走向实际应用，但其显著的证明生成时间开销和内存消耗仍是主要瓶颈，对低算力用户构成准入障碍。为此有两种思路：一是用户将证明生成外包给云服务器，但此举要求直接暴露见证，存在内部人员窃取数据的隐私风险；二是Ozdemir等人引入的协作式zk-SNARKs [61]，通过安全多方计算（MPC）将证明分布式生成，但该方案中每个服务器承担的工作量与单证明者相同，无法加速整体运行时间。本文填补的空白是在不牺牲见证隐私的前提下，将证明生成任务外包给一组服务器以实现显著的加速效果，即结合隐私保护与并行加速，使弱设备用户能利用外部算力生成大规模电路的证明。

### 相关工作

[61] Ozdemir et al. Experimenting with Collaborative zk-SNARKs: Zero-Knowledge Proofs for Distributed Secrets. **USENIX Security 2022** [Google Scholar](https://scholar.google.com/scholar?q=Experimenting+with+Collaborative+zk-SNARKs)
> 核心思路：设计MPC协议使一组持有见证份额的服务器共同生成单个简洁证明，见证在多数服务器诚实下保持隐私。
> 局限与区别：所有服务器并行运行且各自承担与单证明者相同的工作量，无法获得加速；本文通过打包秘密共享（PSS）显著降低每个服务器的工作量，实现并行加速。

[77] Wu et al. DIZK: A Distributed Zero Knowledge Proof System. **USENIX Security 2018** [Google Scholar](https://scholar.google.com/scholar?q=DIZK%3A+A+Distributed+Zero+Knowledge+Proof+System)
> 核心思路：利用集群并行计算加速证明生成，将计算任务分发到多台机器。
> 局限与区别：要求见证以明文形式暴露给集群，导致隐私丧失；本文在分布式环境中保持见证保密。

[5] Bar-Ilan et al. Noncryptographic Fault-Tolerant Computing in Constant Number of Rounds of Interaction. **PODC 1989** [Google Scholar](https://scholar.google.com/scholar?q=Noncryptographic+Fault-Tolerant+Computing+in+Constant+Number+of+Rounds+of+Interaction)
> 核心思路：提出常数轮安全计算无界乘法（unbounded multiplication）的协议。
> 局限与区别：该协议适用于通用计算，本文将其改造为针对部分乘积的专用子协议，并整合打包秘密共享以降低总通信量。

[36] Franklin et al. Communication Complexity of Secure Computation. **STOC 1992** [Google Scholar](https://scholar.google.com/scholar?q=Communication+Complexity+of+Secure+Computation)
> 核心思路：提出打包秘密共享（Packed Secret Sharing）技术，允许一次共享多个秘密并高效执行SIMD操作。
> 区别：本文利用PSS作为核心工具，实现FFT、MSM等子协议的高效并行化处理。

[48] Groth. On the Size of Pairing-Based Non-interactive Arguments. **EUROCRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=On+the+Size+of+Pairing-Based+Non-interactive+Arguments)
> 核心思路：Groth16是目前证明最短的zk-SNARK之一，证明仅包含3个群元素。
> 区别：本文以其为目标之一，设计了zkSaaS协议实现其证明的分布式生成与加速。

[27] Chiesa et al. Marlin: Preprocessing zkSNARKs with Universal and Updatable SRS. **EUROCRYPT 2020** [Google Scholar](https://scholar.google.com/scholar?q=Marlin%3A+Preprocessing+zkSNARKs+with+Universal+and+Updatable+SRS)
> 核心思路：基于交互式预言证明（IOP）的预处理zk-SNARK，使用KZG多项式承诺。
> 区别：本文针对其协议步骤设计了分布式的FFT、部分乘积等子协议，以实现加速。

[37] Gabizon et al. PLONK: Permutations over Lagrange-bases for Oecumenical Noninteractive Arguments of Knowledge. **ePrint 2019** [Google Scholar](https://scholar.google.com/scholar?q=PLONK%3A+Permutations+over+Lagrange-bases+for+Oecumenical+Noninteractive+Arguments+of+Knowledge)
> 核心思路：通用且可更新设置规则的zk-SNARK，依赖部分乘积和多项式运算。
> 区别：本文为其设计了分布式的部分乘积协议，并实现了约22倍的加速。

[70] Smart et al. Distributing Any Elliptic Curve Based Protocol. **IMA Int. Conf. 2019** [Google Scholar](https://scholar.google.com/scholar?q=Distributing+Any+Elliptic+Curve+Based+Protocol)
> 核心思路：将多项式秘密共享推广到群操作，支持加法与乘法（在指数上）的分布式计算。
> 区别：本文借用了该思想实现分布式MSM，但结合了打包技术以降低计算量。

[64] Pippenger. On the Evaluation of Powers and Monomials. **SIAM J. Comput. 1980** [Google Scholar](https://scholar.google.com/scholar?q=On+the+Evaluation+of+Powers+and+Monomials)
> 核心思路：Pippenger算法用O(N/log N)群操作完成N个多标量乘法。
> 区别：该算法缺少SIMD结构，不适合直接用于本文的PSS技术，本文因而采用更简单但可向量化的方法。

[54] Kate et al. Constant-Size Commitments to Polynomials and Their Applications. **ASIACRYPT 2010** [Google Scholar](https://scholar.google.com/scholar?q=Constant-Size+Commitments+to+Polynomials+and+Their+Applications)
> 核心思路：KZG多项式承诺方案，提供常数大小的承诺和打开证明。
> 区别：本文在分布式上下文中使用KZG承诺，依赖MSM和多项式除法子协议。

### 核心技术与方案

**整体框架**：zkSaaS是一个MPC协议，客户端拥有语句 $\phi$ 和见证 $w$，首先本地计算扩展见证 $z$（即R1CS电路的完整赋值），然后使用打包秘密共享（PSS）将 $z$ 分发给 $n$ 个服务器。服务器随后基于这些共享，通过运行分布式子协议共同执行原zk-SNARK的证明算法。框架要求：预处理阶段产生的相关性随机性独立于关系；一个大型服务器（记作 $P_1$）需 $\mathcal{O}(S_{\text{prover}})$ 存储，其余 $n-1$ 个弱服务器仅需 $\mathcal{O}(S_{\text{prover}}/n)$ 存储；计算方面，密码学操作几乎均匀分配，域运算则主要分配给 $P_1$。通信拓扑为星型，仅需客户端与各服务器、$P_1$ 与其余服务器之间的信道。

**关键技术——打包秘密共享（PSS）**：使用多项式将 $\ell$ 个域元素打包成一个份额，每个服务器 $P_i$ 获得一个评估点上的值。要求 $\ell = \mathcal{O}(n)$，且诚实方数量 $> n/2 + \ell$。PSS支持SIMD操作：加法可本地完成，乘法后多项式度数翻倍，需一轮通信进行度数约简。本文所有子协议均基于PSS构建。

**分布式FFT**：核心观察是FFT的每一递归层 $F_{\text{FFT}}^i$ 是线性函数。通过将输入按特定顺序打包成 $\ell$ 长的向量，前 $\log(m/\ell)$ 层可由各服务器本地计算而不需交互。对于剩余的 $\log \ell$ 层，利用线性性进行掩码：服务器预先获得随机值 $r_i$ 的PSS以及 $s_i = F_{\text{FFT}}^1(\dots(F_{\text{FFT}}^{\log \ell}(r_1,\dots,r_m)))$ 的PSS。各服务器将第 $\log \ell$ 层的输出加上 $r_i$ 的PSS后发送给 $P_1$，$P_1$ 重建并计算剩余FFT层，再广播结果。各服务器减去 $s_i$ 的PSS即可得到正确输出。该协议仅需两轮通信，$P_1$ 做 $\mathcal{O}((\log \ell + \log n)m + m(\log m - \log \ell)/\ell)$ 域运算，其余服务器做 $\mathcal{O}(m(\log m - \log \ell)/\ell)$ 域运算。

**分布式MSM**：MSM形如 $\prod_{i \in [m]} A_i^{b_i}$。利用PSS将输入分组为 $\ell$ 长的向量，各服务器首先对每组计算局部的MSM（涉及指数上的乘法，度数翻倍需通信约简），得到 $\ell$ 个中间值 $C_1,\dots,C_\ell$ 的PSS。然后通过转换为普通阈值共享并本地相乘，得到最终结果。该协议常数轮，每服务器执行 $\mathcal{O}(m/\ell)$ 次群指数运算，通信 $\mathcal{O}(1)$ 个群元素。

**分布式部分乘积**：函数 $F_{\text{part}}(x_1,\dots,x_m) = (\prod_{j\in[i]} x_j)_{i\in[m]}$。核心重写为并行SIMD形式：将输入划分为 $\ell$ 组，先并行计算各组的局部部分乘积，再组合各组结果。利用Bar-Ilan和Beaver [5] 的常数轮无界乘法协议，每组内部可在常数轮内完成。最终协议常数轮，$P_1$ 做 $\mathcal{O}(m)$ 域运算并通信 $\mathcal{O}(m)$，其余服务器做 $\mathcal{O}(m/\ell)$ 域运算并通信 $\mathcal{O}(m/\ell)$。

**组合与安全性**：定义可接受的zk-SNARK（$n$-admissible）为证明算法可表示为仅包含MSM、FFT、部分乘积、乘法、加法、置换六种门的电路，且 $o(n)$ 输入的门数量受限于 $\mathcal{O}(T_{\text{crypto}}/n)$ 等条件。本文证明，对于这样的可接受zk-SNARK，上述子协议可直接组合得到安全的zkSaaS。安全性方面：在诚实多数假设下（$\le n/2 - \ell$ 个半诚实的腐败方），协议满足完备性和 $t$-零知识（模拟器可在没有见证的情况下生成腐败方的视图）。此外，即使所有服务器恶意，输出证明的可靠性仍由底层zk-SNARK保证。

### 核心公式与流程

**[FFT递归函数]**
$$F_{\text{FFT}}^i\left(\{x_j^{i,k}\}_{j\in[2^i], k\in[m/2^i]}\right) := \{x_j^{i-1,k}\}_{j\in[2^{i-1}], k\in[m/2^{i-1}]},$$
其中 $x_j^{i-1,k} = x_{2j-1}^{i,k} + \omega^{k2^{i-1}} \cdot x_{2j}^{i,k}$，$\omega$ 为 $m$ 次本原单位根。
> 作用：定义了FFT在单个递归层的线性操作。

**[MSM定义]**
$$F_{\text{MSM}}(y_1,\dots,y_m, X_1,\dots,X_m) = \prod_{j\in[m]}(X_j)^{y_j}$$
> 作用：多标量乘法是zk-SNARK中最昂贵的操作，本文提出分布式实现。

**[部分乘积函数]**
$$F_{\text{part}}(x_1,\dots,x_m) = (\prod_{j\in[i]} x_j)_{i\in[m]}$$
> 作用：Plonk等协议需要此函数计算累计乘积，本文通过重写为并行形式实现分布式计算。

**[zkSaaS定义核心]**
$$\Pi_{\text{online}}(\text{crs}, \phi, w, \text{pre}_1,\dots,\text{pre}_n) \to \pi$$
$$\text{Pr}\left[ \text{Ver}(\text{crs},\phi,\pi)=0 \right] \le \text{negl}(\lambda) \quad \text{(Completeness)}$$
$$\{\text{view}_{\Pi_{\text{online}}}^{\mathcal{A}}[\phi,w]\} \approx_c \{\text{Sim}_{\text{zkSaaS}}(\text{crs}, \phi, b, \{\text{pre}_i\}_{i\in\text{Corr}})\} \quad \text{(Zero-knowledge)}$$
> 作用：形式化定义了zkSaaS框架的完备性和零知识性质，其中 $b$ 表示 $\phi$ 是否在 $R$ 中。

### 实验结果

实验在Google Cloud Platform上进行：弱服务器为1 vCPU、2GB内存的自定义N1实例；大型服务器为96 vCPU、128GB RAM的N1实例；基准消费者机器为1 vCPU、4GB内存。使用Groth16和Plonk协议，在4Gbps高速网络下与本地单证明者对比。对于 $2^{25}$ 个约束的Groth16证明，128台服务器的zkSaaS协议比本地快约22倍；对于 $2^{21}$ 个门的Plonk证明，加速也达到约22倍。当将服务器从8台增加到128台时，对于 $2^{19}$ 约束的Grooth16，加速从约1.9倍提升至22倍。网络速度影响实验表明，即使在64Mbps的低速网络下，性能退化也仅约2倍。财务成本估算显示：使用128台服务器在4Gbps链路上为 $2^{19}$ 约束生成Groth16证明的费用低于18美分，在64Mbps链路上则低于23美分。

### 局限性与开放问题

当前方案依赖于一个大型服务器承担O(m)存储和部分域运算，若能将FFT子协议设计为完全均衡负载，可进一步弱化对强大单点的依赖。另一个方向是设计适用于不依赖FFT的zk-SNARK（如Orion、Brakedown、Hyperplonk）的zkSaaS变体。最后，本文的安全模型仅针对半诚实腐败，将其提升为能抵抗恶意服务器的方案仍需形式化论证，尽管文中给出了可以通过现有高效编译器实现的大致方向。

### 强关联论文

[5] Bar-Ilan et al. Noncryptographic Fault-Tolerant Computing in Constant Number of Rounds of Interaction. **PODC 1989** [Google Scholar](https://scholar.google.com/scholar?q=Noncryptographic+Fault-Tolerant+Computing+in+Constant+Number+of+Rounds+of+Interaction)

[27] Chiesa et al. Marlin: Preprocessing zkSNARKs with Universal and Updatable SRS. **EUROCRYPT 2020** [Google Scholar](https://scholar.google.com/scholar?q=Marlin%3A+Preprocessing+zkSNARKs+with+Universal+and+Updatable+SRS)

[37] Gabizon et al. PLONK: Permutations over Lagrange-bases for Oecumenical Noninteractive Arguments of Knowledge. **ePrint 2019** [Google Scholar](https://scholar.google.com/scholar?q=PLONK%3A+Permutations+over+Lagrange-bases+for+Oecumenical+Noninteractive+Arguments+of+Knowledge)

[48] Groth. On the Size of Pairing-Based Non-interactive Arguments. **EUROCRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=On+the+Size+of+Pairing-Based+Non-interactive+Arguments)

[54] Kate et al. Constant-Size Commitments to Polynomials and Their Applications. **ASIACRYPT 2010** [Google Scholar](https://scholar.google.com/scholar?q=Constant-Size+Commitments+to+Polynomials+and+Their+Applications)

[61] Ozdemir et al. Experimenting with Collaborative zk-SNARKs: Zero-Knowledge Proofs for Distributed Secrets. **USENIX Security 2022** [Google Scholar](https://scholar.google.com/scholar?q=Experimenting+with+Collaborative+zk-SNARKs%3A+Zero-Knowledge+Proofs+for+Distributed+Secrets)

[64] Pippenger. On the Evaluation of Powers and Monomials. **SIAM J. Comput. 1980** [Google Scholar](https://scholar.google.com/scholar?q=On+the+Evaluation+of+Powers+and+Monomials)

[70] Smart et al. Distributing Any Elliptic Curve Based Protocol. **IMA Int. Conf. 2019** [Google Scholar](https://scholar.google.com/scholar?q=Distributing+Any+Elliptic+Curve+Based+Protocol)

[77] Wu et al. DIZK: A Distributed Zero Knowledge Proof System. **USENIX Security 2018** [Google Scholar](https://scholar.google.com/scholar?q=DIZK%3A+A+Distributed+Zero+Knowledge+Proof+System)

[36] Franklin et al. Communication Complexity of Secure Computation. **STOC 1992** [Google Scholar](https://scholar.google.com/scholar?q=Communication+Complexity+of+Secure+Computation)


## 关键词

+ zkSaaS分布式zkSNARK服务
+ 证明生成外包多服务器
+ Groth16 Plonk分布式加速
+ 隐私保护证明外包
+ 抗合谋见证隐私保护
+ zk-SNARK云计算框架
