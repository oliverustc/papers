---
title: "Lova: lattice-based folding scheme from unstructured lattices"
doi: 10.1007/978-981-96-0894-2_10
标题简称: 
论文类型: conference
会议简称: ASIACRYPT
发表年份: 2024
created: 2025-04-21 11:06:02
modified: 2025-04-21 11:07:59
---
## Lova: lattice-based folding scheme from unstructured lattices

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-981-96-0894-2_10)

## 作者

+ Giacomo Fenzi 
+ Christian Knabenhans 
+ Ngoc Khanh Nguyen 
+ Duc Tu Pham 

## 笔记

### 背景与动机

递增可验证计算（IVC）使长计算过程能在任意时刻高效验证其状态正确性，是区块链、可验证延迟函数等应用的核心构件。最早的IVC构造依赖递归简洁非交互知识论证（SNARK），但这类方法对底层SNARK的选择有诸多限制，实践中较为笨重。近年来的折叠方案（folding scheme）提供了一种替代路径，它通过将多个关系实例“折叠”成一个单一实例来简化验证，从而构建IVC。然而，现有折叠方案几乎都基于Pedersen承诺和离散对数假设，因此既无法抵抗量子攻击，又在大的素数域上运算，不够高效。虽然Boneh和Chen提出了首个格基折叠方案LatticeFold [4]，但其安全性建立在更为结构化的Module-SIS假设上，需要实现多项式环算术和NTT友好素数模数，增加了实现复杂性。针对上述问题，Lova旨在构建首个基于非结构化SIS假设的折叠方案，使用硬件友好的2的幂次模数，从而在保持安全性的同时大幅简化实现。

### 相关工作

[1] Kothapalli et al. Nova: Recursive Zero-Knowledge Arguments from Folding Schemes. **CRYPTO 2022** [Google Scholar](https://scholar.google.com/scholar?q=Nova+Recursive+Zero-Knowledge+Arguments+from+Folding+Schemes)  
> 核心思路：提出了折叠方案的概念，并基于离散对数假设和Pedersen承诺构建了Nova，实现高效的IVC。  
> 局限与区别：安全性依赖离散对数假设，无法抵抗量子攻击。Lova将折叠方案的框架迁移到格假设下，并解决了随之而来的范数增长问题。

[2] Boneh, Chen. LatticeFold: A Lattice-based Folding Scheme and its Applications to Succinct Proof Systems. **ePrint 2024/257** [Google Scholar](https://scholar.google.com/scholar?q=LatticeFold+A+Lattice-based+Folding+Scheme+and+its+Applications+to+Succinct+Proof+Systems)  
> 核心思路：首次提出了基于格假设的折叠方案，利用CRT打包和sumcheck论证技术证明无穷范数下的短性。  
> 局限与区别：安全性基于结构化格假设（如Module-SIS），需要实现多项式环算术和NTT。Lova则依赖非结构化的SIS假设，运算只需整数算术。

[3] Baum et al. Sub-linear Lattice-Based Zero-Knowledge Arguments for Arithmetic Circuits. **CRYPTO 2018** [Google Scholar](https://scholar.google.com/scholar?q=Sub-linear+Lattice-Based+Zero-Knowledge+Arguments+for+Arithmetic+Circuits)  
> 核心思路：提出了用于算术电路的次线性格基零知识论证，其中使用了坐标特殊可靠性（Coordinate-Wise Special Soundness）提取技术。  
> 局限与区别：该技术提取的证人存在范数膨胀。Lova通过结合精确欧几里得范数证明和三元挑战集来消除提取时的范数膨胀。

[4] Cini et al. Polynomial Commitments from Lattices: Post-Quantum Security, Fast Verification and Transparent Setup. **ePrint 2024/281** [Google Scholar](https://scholar.google.com/scholar?q=Polynomial+Commitments+from+Lattices+Post-Quantum+Security+Fast+Verification+and+Transparent+Setup)  
> 核心思路：构造了具有快速验证和透明设置的格基多项式承诺方案，其中使用了分解-折叠范式来控制范数增长。  
> 局限与区别：该方案主要用于多项式承诺。Lova将其中的精确欧几里得范数证明技术推广并应用于折叠方案的知识可靠性论证中。

[5] Ajtai. Generating Hard Instances of Lattice Problems. **STOC 1996** [Google Scholar](https://scholar.google.com/scholar?q=Generating+Hard+Instances+of+Lattice+Problems)  
> 核心思路：提出了基于SIS假设的承诺方案（Ajtai承诺），其安全性依赖于格上的最短向量问题。  
> 局限与区别：Ajtai承诺对消息和随机性的范数有严格要求。Lova以此为基本构件，通过分解-折叠范式克服了其范数增长的限制。

[6] Beullens, Seiler. LaBRADOR: Compact Proofs for R1CS from Module-SIS. **CRYPTO 2023** [Google Scholar](https://scholar.google.com/scholar?q=LaBRADOR+Compact+Proofs+for+R1CS+from+Module-SIS)  
> 核心思路：基于Module-SIS假设构造了用于R1CS的紧凑论证，使用了分解-折叠范式。  
> 局限与区别：LaBRADOR依赖于结构化格假设。Lova的工作表明分解-折叠范式可以同样应用于非结构化SIS假设。

### 核心技术与方案

Lova的整体构造分为三个层次，最终实现从 $(R_{q,β,t})^2$ 到 $R_{q,β,t}$ 的归约（即折叠），其中关系 $R_{q,β,t}$ 定义为 Ajtai 承诺的打开关系，包含对矩阵 $S$ 的精确欧几里得范数约束。

**第一层：合并实例**。该层将两个 $R_{q,β,t}$ 实例合并为一个 $R_{q,β,2t}$ 实例。给定 $S_1, S_2$，证明者计算并发送 $U = S_2^\top S_1$ 和 $V = S_1^\top S_2$。验证者构造合并后的实例：$T = [T_1 | T_2]$，$D = \begin{bmatrix} D_1 & V \\ U & D_2 \end{bmatrix}$。由于 $D$ 的对角线由 $D_1$ 和 $D_2$ 的对角线构成，因此 $D_{i,i} \leq β^2$ 自动保持。该层直接满足知识可靠性：从合并的证人 $S = [S_1 | S_2]$ 中可以解析出原始证人 $S_1, S_2$。

**第二层：折叠实例（核心）**。该层通过分解-折叠和精确范数证明，将 $R_{q,β,2t}$ 实例折叠为 $R_{q,β,t}$ 实例。核心协议步骤如下：  
1. 证明者计算分解 $ \tilde{S} = G^{-1}(S)$，其中 $G$ 是基为 $b$ 的 gadget 矩阵，$G^{-1}$ 将 $S$ 的每一列分解为 $k = \lfloor \log_b β \rfloor + 2$ 个较短向量（每个分量在 $[-\lfloor b/2 \rfloor, \lfloor b/2 \rfloor]$ 内）。然后计算 $ \tilde{T} = A \tilde{S} \mod q$ 和 $\tilde{D} = \tilde{S}^\top \tilde{S}$，并将 $(\tilde{T}, \tilde{D})$ 发送给验证者。  
2. 验证者随机采样挑战矩阵 $C \gets \{-1,0,1\}^{2kt × t}$。  
3. 证明者计算并输出折叠后的证人 $S' = \tilde{S} C$。  
4. 验证者执行两个关键检查：$G^\top \tilde{D} G = D$ 和 $\tilde{T} G \equiv T \pmod{q}$，确保 $\tilde{S}$ 是 $S$ 的正确分解且 $\tilde{D}$ 准确记录了 $\tilde{S}$ 的内积。验证者输出折叠后的实例 $(T' = \tilde{T} C, D' = C^\top \tilde{D} C)$。

**完备性论证**：首先验证 $\tilde{T} G \equiv A \tilde{S} G \equiv A S \equiv T \pmod{q}$，以及 $G^\top \tilde{D} G = G^\top \tilde{S}^\top \tilde{S} G = S^\top S = D$。对列 $j$ 有 $||S'_{*,j}|| \le 2kt \lfloor b/2 \rfloor \sqrt{m}$。当参数选择满足 $t ≤ β/(2k \lfloor b/2 \rfloor \sqrt{m})$ 时，该范数不超过 $β$，从而保证了完备性。

**知识可靠性论证**：协议使用三元挑战集 $\mathcal{C} = \{-1,0,1\}$，具有键优势：差值的倒数在模2意义下均为小值（±1），避免了模逆运算带来的范数膨胀。证明分两步：先通过改进的坐标特殊可靠性提取出满足 $A \bar{S} \equiv \tilde{T} \pmod{q}$ 的分解证人 $\bar{S}$，其列范数不超过 $2β$；然后证明若 $S' = \bar{S} C$，则必然有 $\bar{S}^\top \bar{S} = \tilde{D}$，从而提取出的最终证人 $S = \bar{S} G$ 满足 $S^\top S = D$ 且列范数不超过 $β$。后者利用 Demillo-Lipton-Schwartz-Zippel 引理，两个总次数为2的多项式在随机点取值相等的概率不超过 $2/|\mathcal{C}|$。因此，知识误差由 $\kappa_{KS} = O((2/3)^t + 2^{-\lambda})$ 主导，通过选取足够大的 $t$（如 $t=330$）可使其可忽略。

**复杂度分析**：一次折叠的总通信量为 $t^2 \lceil \log β^2 \rceil + 2nkt \lceil \log q \rceil + (2kt)(2kt+1)/2 \cdot \lceil \log \lfloor b/2 \rfloor^2 \rceil$ 比特。证明者和验证者的主要操作是矩阵-矩阵乘法（条目范数有界），计算复杂度为 $O(m \cdot kt \cdot t)$ 数量级。通过使用2的幂次模数 $q=2^{64}$，所有运算可退化到标准64位整数算术，无需实现任何模约减。

### 核心公式与流程

**[Ajtai承诺绑定关系]**
$$A S \equiv T \pmod{q}, \quad ||S_{*,i}|| \leq β$$
> 作用：定义了 SIS 关系 $R_{q,β,t}$ 的核心代数约束和范数约束，绑定性质依赖于 SIS 假设。

**[归约协议：合并实例（Fig. 1）]**
$$U = S_2^\top S_1, V = S_1^\top S_2$$
$$T = [T_1 | T_2], D = \begin{bmatrix} D_1 & V \\ U & D_2 \end{bmatrix}$$
> 作用：将两个 $R_{q,β,t}$ 实例合并为单个 $R_{q,β,2t}$ 实例，保持 $D_{i,i} \leq β^2$。

**[归约协议：折叠实例（Fig. 2）]**
$$\tilde{S} = G^{-1}(S), \quad \tilde{T} = A\tilde{S} \mod q, \quad \tilde{D} = \tilde{S}^\top \tilde{S}$$
$$C \gets \{-1,0,1\}^{2kt \times t}$$
$$S' = \tilde{S} C, \quad T' = \tilde{T} C, \quad D' = C^\top \tilde{D} C$$
$$检查: G^\top \tilde{D} G = D \quad \text{且} \quad \tilde{T} G \equiv T \pmod{q}$$
> 作用：将 $R_{q,β,2t}$ 实例折叠为 $R_{q,β,t}$ 实例。证明者发送 $(\tilde{T}, \tilde{D})$，验证者发送挑战 $C$，证明者输出 $S'$，验证者输出 $(T', D')$。范数控制通过分解范围 $\lfloor b/2 \rfloor \sqrt{m}$ 和挑战值在 $\{-1,0,1\}$ 实现，精确范数由 $\tilde{D}$ 保证。

**[精确范数证明的核心不等式]**
$$f_{i,i}(C_{*,i}) = g_{i,i}(C_{*,i}) \implies \bar{S}^\top \bar{S} = \tilde{D} \quad \text{概率} \leq (2/|\mathcal{C}|)^t$$
> 作用：使用 Demillo-Lipton-Schwartz-Zippel 引理证明，若提取出的 $\bar{S}$ 不满足 $\bar{S}^\top \bar{S} = \tilde{D}$，则其在随机挑战 $C$ 下通过验证的概率至多为 $(2/3)^t$，从而确保了知识可靠性。

### 实验结果

- **实验环境**：AWS EC2 实例，配备 128 GB RAM 和 32 个 Intel Xeon vCPU @ 3.1 GHz。实现语言为 Rust。
- **参数选取**：设置安全参数 $\lambda = 128$，挑战次数 $t = 330$，SIS 模数 $q = 2^{64}$。分解基通过公式 $β = (4t)^2 m$ 确定，使得 $k = 4$（即每列分解为4个更短的列）。模数选择使所有算术运算退化为原生64位整数运算。
- **性能数据（以实例长度 $2^{17}$ 为例）**：在 IVC 设置下（证明者折叠一个新鲜实例与一个重复实例），一次折叠的证明大小为 17.53 MB（完美完备性时）或 16.62 MB（接受可忽略完备性误差时）。证明者运行时间为 321 秒（完美完备性时）或 296 秒（接受可忽略完备性误差时）。在 PCD 设置下（证明者折叠两个独立新鲜实例），证明大小和运行时间约翻倍。
- **可扩展性**：随着实例长度增加（从 $2^{17}$ 到 $2^{19}$），证明大小增长约 10%，证明者运行时间增长约 2.3 倍，均呈近似线性平滑增长。
- **verifier 复杂性**：Verifier 的主要计算包括生成挑战矩阵（约 $3.22 \cdot kt^2$ 比特的哈希输出）、检查两组线性约束（$n \cdot 2t$ 和 $(2t)^2$ 条）、以及检查两组二次约束（$n \cdot 2t$ 和 $(2k)^2 + (2kt)^2$ 条）。这些约束的稀疏性可被下游证明系统进一步利用。
- **与基线对比**：与 LatticeFold [4] 相比，Lova 无需实现多项式环算术或 NTT，仅依赖标准整数算术。与离散对数基构造相比，Lova 提供了量子抵抗性。

### 局限性与开放问题

Lova 目前无法直接支持 R1CS 类 NP 关系，因为折叠过程中出现的交叉项会让已分解证人的范数依赖于 R1CS 矩阵 A、B、C 的条目大小——而后者通常不是短的，这将导致范数失控。作者给出了一个构造折叠方案以支持是NP完全的“子集和”问题的草图，通过将二进制约束编码为内积方程，但尚未扩展到更通用的关系。一个重要的未来工作是设计面向 R1CS 类型关系的格基折叠方案，并使其在小模数下高效实现。

### 强关联论文

[1] Kothapalli et al. Nova: Recursive Zero-Knowledge Arguments from Folding Schemes. **CRYPTO 2022** [Google Scholar](https://scholar.google.com/scholar?q=Nova+Recursive+Zero-Knowledge+Arguments+from+Folding+Schemes)

[2] Boneh, Chen. LatticeFold: A Lattice-based Folding Scheme and its Applications to Succinct Proof Systems. **ePrint 2024/257** [Google Scholar](https://scholar.google.com/scholar?q=LatticeFold+A+Lattice-based+Folding+Scheme+and+its+Applications+to+Succinct+Proof+Systems)

[3] Baum et al. Sub-linear Lattice-Based Zero-Knowledge Arguments for Arithmetic Circuits. **CRYPTO 2018** [Google Scholar](https://scholar.google.com/scholar?q=Sub-linear+Lattice-Based+Zero-Knowledge+Arguments+for+Arithmetic+Circuits)

[4] Cini et al. Polynomial Commitments from Lattices: Post-Quantum Security, Fast Verification and Transparent Setup. **ePrint 2024/281** [Google Scholar](https://scholar.google.com/scholar?q=Polynomial+Commitments+from+Lattices+Post-Quantum+Security+Fast+Verification+and+Transparent+Setup)

[5] Ajtai. Generating Hard Instances of Lattice Problems. **STOC 1996** [Google Scholar](https://scholar.google.com/scholar?q=Generating+Hard+Instances+of+Lattice+Problems)

[6] Beullens, Seiler. LaBRADOR: Compact Proofs for R1CS from Module-SIS. **CRYPTO 2023** [Google Scholar](https://scholar.google.com/scholar?q=LaBRADOR+Compact+Proofs+for+R1CS+from+Module-SIS)

[7] Bünz et al. Proof-Carrying Data Without Succinct Arguments. **CRYPTO 2021** [Google Scholar](https://scholar.google.com/scholar?q=Proof-Carrying+Data+Without+Succinct+Arguments)

[8] Kothapalli, Parno. Algebraic Reductions of Knowledge. **CRYPTO 2023** [Google Scholar](https://scholar.google.com/scholar?q=Algebraic+Reductions+of+Knowledge)

[9] Lyubashevsky et al. Lattice-Based Zero-Knowledge Proofs and Applications: Shorter, Simpler, and More General. **CRYPTO 2022** [Google Scholar](https://scholar.google.com/scholar?q=Lattice-Based+Zero-Knowledge+Proofs+and+Applications+Shorter+Simpler+and+More+General)


## 关键词

+ 折叠方案
+ 格密码学
+ 后量子安全
+ 增量可验证计算
+ SIS假设

+ 折叠方案
+ 格密码学
+ 后量子安全
+ 增量可验证计算
+ SIS假设