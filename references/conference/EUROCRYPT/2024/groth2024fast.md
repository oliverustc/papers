---
title: "Fast batched asynchronous distributed key generation"
标题简称:
论文类型: conference
会议简称: EUROCRYPT
发表年份: 2024
created: 2025-05-12 09:08:01
modified: 2025-05-12 09:09:40
---

## Fast batched asynchronous distributed key generation

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-58740-5_13)
+ [archive](https://eprint.iacr.org/2023/1175)

## 作者

+ [Jens Groth](Jens%20Groth.md)
+ [Victor Shoup](Victor%20Shoup.md)
## 笔记

### 背景与动机

在异步通信环境下设计高效的阈值 Schnorr 签名协议，同时保证鲁棒性和最优容错性（即 n > 3t），是一个尚未完全解决的挑战。现有方案中，基于多项式承诺的分布式密钥生成（DKG）协议（如 Feldman 1987 [14]、Pedersen 1991 [26]）在异步模型下计算开销大，且难以实现高吞吐量。SPRINT [3] 虽引入了批量随机性提取技术，但其依赖的传统共享和验证方法仍然限制了性能。本文旨在填补两个空白：一是如何在不使用多项式承诺的前提下，实现可验证的秘密共享（VSS）以高效生成大量密钥份额；二是如何设计一种超可逆矩阵并配备极低开销的群元素乘法算法，以支持批量随机性提取。这两个创新共同驱动了异步阈值签名协议的性能突破——在中等规模签名委员会（如 49 个参与方）下，单个参与方生成一个签名的计算量甚至小于执行一次标准 Schnorr 签名或验证算法。

### 相关工作

[29] Shoup et al. Lightweight Asynchronous Verifiable Secret Sharing. **ePrint 2023**  
> 核心思路：使用仅基于哈希函数的轻量密码学原语实现 AVSS，通信和计算效率高。  
> 局限与区别：该协议仅处理标量共享，不涉及群元素验证；本文在其基础上增加了群元素验证层，形成 GoAVSS。

[3] Benhamouda et al. SPRINT: High-Throughput Robust Distributed Schnorr Signatures. **ePrint 2023**  
> 核心思路：利用批量随机性提取和超可逆矩阵生成大量预签名。  
> 局限与区别：SPRINT 中的共享协议仍依赖多项式承诺，计算开销较大；本文通过无承诺的 GoAVSS 大幅降低了计算量。

[28] Shoup. The Many Faces of Schnorr. **ePrint 2023**  
> 核心思路：系统分析了 Schnorr 签名的安全性及其在阈值设置中的变体，允许预签名存在特定类型的偏差。  
> 局限与区别：该工作未给出具体高效的实现协议；本文基于其安全性框架，实现了实际可行的异步协议。

[21] Hirt et al. Robust Multiparty Computation with Linear Communication Complexity. **CRYPTO 2006**  
> 核心思路：提出了超可逆矩阵的概念，用于从多输入中提取随机性。  
> 局限与区别：该矩阵的乘法算法在群元素上的开销较高；本文给出了基于 Pascal 矩阵的显式构造和高效乘法算法。

[2] Beerliová-Trubíniová et al. Perfectly-Secure MPC with Linear Communication Complexity. **TCC 2008**  
> 核心思路：引入超可逆矩阵实现信息论安全的批量随机性提取。  
> 局限与区别：其构造依赖 Cauch y 矩阵，本文使用 Pascal 矩阵并分析了其超可逆性条件，更适合实际参数。

[6] Bracha. Asynchronous Byzantine Agreement Protocols. **Inf. Comput. 1987**  
> 核心思路：经典的可靠广播协议，通信复杂度 O(n²) 每广播。  
> 局限与区别：本文使用基于纠错码的紧凑广播协议 [29] 以降低通信。

[7] Cachin et al. Asynchronous Verifiable Information Dispersal. **DISC 2005**  
> 核心思路：利用纠错码实现高效广播，通信复杂度 O(n|m|)。  
> 局限与区别：本文采用的紧凑广播协议 [29] 进一步优化了常数因子。

[14] Feldman. A Practical Scheme for Non-Interactive Verifiable Secret Sharing. **FOCS 1987**  
> 核心思路：使用多项式承诺实现可验证的秘密共享。  
> 局限与区别：该方案在异步模型下计算开销大，且需要执行群指数运算；本文通过统计测试和错误校正码避免了承诺。

[26] Pedersen. A Threshold Cryptosystem without a Trusted Party. **EUROCRYPT 1991**  
> 核心思路：使用双多项式实现无条件安全的可验证秘密共享。  
> 局限与区别：同样依赖承诺，本文未采用承诺机制。

[4] Boldyreva. Threshold Signatures, Multisignatures and Blind Signatures Based on the Gap-Diffie-Hellman-Group Signature Scheme. **PKC 2003**  
> 核心思路：阈值 BLS 签名可被用作随机信标。  
> 局限与区别：本文随机信标的实现可用 AVSS 和共识协议，也可用阈值 BLS，但未深入讨论。

### 核心技术与方案

本文的整体框架建立在两层创新之上：第一层是新的群导向异步可验证秘密共享协议（GoAVSS），用于高效实现 MPC 引擎中的 `InputKey`、`LinearOp`、`Open` 操作；第二层是新型超可逆矩阵及其快速群元素乘法算法，用于批量随机性提取。

#### GoAVSS 协议

GoAVSS 允许一个经销商输入 L 个次数不超过 t 的多项式 $f_1,\dots,f_L \in \mathbb{Z}_q[x]_{<d}$（其中 $d = t+1$），每个多项式 $f_\ell$ 定义秘密 $s_\ell = f_\ell(0)$ 和公钥 $S_\ell = s_\ell \mathcal{G}$。协议的目标是让所有参与方获得 $S_\ell$ 和各自的份额 $f_\ell(e_j)$。关键创新是 **不使用多项式承诺**，而是通过一个统计检验来保证公钥与秘密的一致性。

协议步骤（图 6）：

1. 经销商随机生成 n 个次数不超过 t 的盲化多项式 $g^{(k)} \ (k=1,\dots,n)$，并通过 AVSS 共享 $\{g^{(k)}\}_{k}$ 和 $\{f_\ell\}_{\ell}$ 的所有份额。同时，经销商可靠广播公钥 $\mathcal{T}^{(k)} = g^{(k)}(0)\mathcal{G}$ 和 $\mathcal{S}_\ell = f_\ell(0)\mathcal{G}$。
2. 所有参与方（包括经销商）等待 AVSS 输出份额和可靠广播输出公钥，然后发起随机信标，得到随机挑战 $\gamma_\ell^{(k)} \in R \subseteq \mathbb{Z}_q$（$\rho$ 比特长）。
3. 经销商计算响应多项式 $h^{(k)} = g^{(k)} + \sum_{\ell=1}^L \gamma_\ell^{(k)} f_\ell$（次数 $\le t$），并可靠广播 $\{h^{(k)}\}_k$。
4. 每个接收方 $P_j$ 验证两个条件：
   - $h^{(j)}(0)\mathcal{G} = \mathcal{T}^{(j)} + \sum_{\ell} \gamma_\ell^{(j)} \mathcal{S}_\ell$（一个群加法检验）。
   - 对所有 $k$，$h^{(k)}$ 的次数 $\le t$ 且 $h^{(k)}(e_j) = w_j^{(k)} + \sum_{\ell} \gamma_\ell^{(k)} v_{\ell,j}$（$w_j^{(k)}$ 和 $v_{\ell,j}$ 是从 AVSS 获得的份额）。
5. 如果检验通过，参与方发起单边投票协议；最终当投票输出 `done` 时，输出 $\{(\mathcal{S}_\ell, v_{\ell,j})\}_\ell$。

**安全性直觉**：如果经销商是诚实的，模拟器可以随机生成 $h^{(k)}$ 并计算秘密值和份额，使得模拟完美。如果经销商是腐败的，他必须在随机挑战 $\gamma_\ell^{(k)}$ 揭露之前提交 $f_\ell$ 和 $g^{(k)}$。若存在某个 $\ell$ 使得 $\mathcal{S}_\ell \neq f_\ell(0)\mathcal{G}$，则对于任意固定 $k$，等式 $\mathcal{T}^{(k)} + \sum_\ell \gamma_\ell^{(k)}\mathcal{S}_\ell = g^{(k)}(0)\mathcal{G} + \sum_\ell \gamma_\ell^{(k)} f_\ell(0)\mathcal{G}$ 成立的概率至多为 $2^{-\rho}$。由于有至少 $n-2t$ 个诚实参与方通过检验，这些事件独立，失败概率不超过 $\text{Tail}(n-t, n-2t, 1/|R|) \le 2^{-n(\rho-2)/3}$（定理 1）。取 $\rho = \lceil 3\sigma/n \rceil + 2$ 可使失败概率小于 $2^{-\sigma}$。

**复杂度**（假设 $L = \Omega(n^2)$ 摊销，$n=3t+1$）：

- **通信**：每个处理后的共享（processed sharing）约发送 18 个标量和 9 个群元素，即每参与方 $O(\lambda)$ 比特（$\lambda = \log q$）。
- **计算**（摊销后每处理共享）：
  - $1/(t+1)$ 次完整标量/群乘法；
  - 3 次小标量/群乘法（$\rho$ 比特标量，成本约 1-2 次群加法）；
  - $4n$ 次小标量/标量乘法（$\rho$ 比特乘 $\lambda$ 比特，成本约 $1/40$ 群加法）。

#### 超可逆矩阵构造

本文给出两种基于 Pascal 矩阵的显式构造，以及高效乘法算法。

**对称 Pascal 矩阵** $S_{M,N,q} \in \mathbb{Z}_q^{M \times N}$，其第 $i$ 行第 $j$ 列（$i,j$ 从 0 开始）为 $C_{i+j,i}$。定理 3 证明当 $q \ge N$ 时该矩阵是超可逆的（任意 $M$ 列线性无关）。乘法算法利用递推式 $\mathcal{X}_k^{(i)} = \mathcal{X}_k^{(i-1)} + \mathcal{X}_{k+1}^{(i)}$（$i=0,\dots,M-1$，$k=N-2,\dots,0$），得到 $\mathcal{Y}_i = \mathcal{X}_0^{(i)}$，共 $M \cdot (N-1)$ 次群加法。

**上三角 Pascal 矩阵** $U_{M,N,q}$，其第 $i$ 行第 $j$ 列为 $C_{j,i}$（$j \ge i$，否则 0）。定理 4 证明其超可逆性等价于对称情形。乘法算法计算 $\mathcal{Y}_i = \mathcal{X}_i^{(i)}$（通过相同递推），共 $M \cdot (N - (M+1)/2)$ 次群加法。若将 $U_{M,N,q}$ 扩充一列 $(0,\dots,0,1)^\top$ 得到 $U'_{M,N,q}$，则该矩阵是 $M \times (N+1)$ 超可逆的，乘法成本仅增加 1 次群加法。

**应用**：在批量随机性提取中，需要 $(n-2t) \times (n-t)$ 超可逆矩阵。可取 $M = n-2t$，$N = n-t-1$，使用 $U'$ 矩阵，乘法成本为 $(n-2t) \cdot (n/2 - 3/2) + 1$ 次群加法。当 $n=49, t=16$ 时，摊销成本约 23 次群加法每处理共享。进一步，若利用对称 Pascal 矩阵的 **超可逆性**（所有方子阵可逆），当 $N \le 17$ 且 $q > 2^{237}$ 时，可构造 $M \times (M+t)$ 矩阵 $S'_{M,t,q} = [I \mid S_{M,t,q}]$，乘法成本为 $M \cdot t = (n-2t) \cdot t$ 次群加法。对于 $n=49, t=16, M=17$，成本为 $17 \times 16 = 272$ 次群加法分摊到 17 个处理共享，每共享 16 次群加法，同时额外付出 16 次 $\mathbb{Z}_q$ 加法。

#### 组合结果

将 GoAVSS 与超可逆矩阵结合，实现批量预签名生成。离线阶段每预签名的摊销成本：每个参与方执行约 $O(n + \lambda/n)$ 次群加法（例如 $n=49,\lambda=256$ 时为 23 次群加法）。在线阶段（两轮通信，允许批量）每签名摊销通信 6 个标量，计算 $O(n)$ 次 $\mathbb{Z}_q$ 运算。基于 secp256k1 曲线，估计每秒可生成 50,000 个签名（假设 500 Mbps 网络带宽和单核 CPU）。

### 核心公式与流程

**[GoAVSS 协议流程]**

1. Dealer D: 输入 $f_1,\dots,f_L$；生成随机盲化多项式 $g^{(1)},\dots,g^{(n)} \in \mathbb{Z}_q[x]_{<t+1}$；通过 AVSS 共享全部多项式；可靠广播 $\mathcal{T}^{(k)} = g^{(k)}(0)\mathcal{G}$ 和 $\mathcal{S}_\ell = f_\ell(0)\mathcal{G}$。
2. 所有参与方：等待 AVSS 输出和可靠广播；启动随机信标得到 $\gamma_\ell^{(k)}$。
3. D: 计算 $h^{(k)} = g^{(k)} + \sum_{\ell=1}^L \gamma_\ell^{(k)} f_\ell$，可靠广播 $h^{(k)}$。
4. 每个 $P_j$: 验证 (2) $h^{(j)}(0)\mathcal{G} = \mathcal{T}^{(j)} + \sum_\ell \gamma_\ell^{(j)}\mathcal{S}_\ell$ 且 (3) 对所有 $k$，$h^{(k)} \in \mathbb{Z}_q[x]_{<t+1}$ 且 $h^{(k)}(e_j) = w_j^{(k)} + \sum_\ell \gamma_\ell^{(k)} v_{\ell,j}$。若通过，启动单边投票。
5. 当投票输出 `done`，输出 $(\mathcal{S}_\ell, v_{\ell,j})$。

**[对称 Pascal 矩阵乘法算法]**

设 $\mathbf{x} = (\mathcal{X}_0,\dots,\mathcal{X}_{N-1})^\top \in E^{N \times 1}$，目标 $\mathbf{y} = S_{M,N,q}\mathbf{x}$。

初始化 $\mathcal{X}_k^{(-1)} = \mathcal{X}_k$，$k=0,\dots,N-1$。

对 $i=0,\dots,M-1$:
   $\mathcal{X}_{N-1}^{(i)} = \mathcal{X}_{N-1}^{(i-1)}$
   对 $k = N-2,\dots,0$:
       $\mathcal{X}_k^{(i)} = \mathcal{X}_k^{(i-1)} + \mathcal{X}_{k+1}^{(i)}$
   输出 $\mathcal{Y}_i = \mathcal{X}_0^{(i)}$。

成本：$M \cdot (N-1)$ 次群加法。

**[上三角 Pascal 矩阵乘法算法 (扩充版)]**

设 $U'_{M,N,q}$ 为 $M \times (N+1)$ 矩阵，前 $N$ 列为 $U_{M,N,q}$，最后一列为 $(0,\dots,0,1)^\top$。对输入 $\mathbf{x} \in E^{(N+1) \times 1}$，计算 $\mathbf{y} = U'_{M,N,q}\mathbf{x}$。

算法：先按对称 Pascal 算法递推，但 $\mathcal{Y}_i = \mathcal{X}_i^{(i)}$（而非 $\mathcal{X}_0^{(i)}$）。然后加上最后一列的贡献：$\mathcal{Y}_{M-1} = \mathcal{Y}_{M-1} + \mathcal{X}_{N}$（即最后一维输入的单次加法）。

总成本：$M \cdot (N - (M+1)/2) + 1$ 次群加法。

**[安全性错误概率]**

设 $\rho = \lceil 3\sigma/n \rceil + 2$，失败概率 $\le 2^{-n(\rho-2)/3} \le 2^{-\sigma}$。

### 实验结果

本文未进行实际实验，但给出了基于分析的计算估计。参数设定：$n=49$（$t=16$），$\lambda=256$，$\sigma=80$，椭圆曲线 secp256k1，系数 $\rho=7$。离线阶段每预签名摊销成本：GoAVSS 贡献约 7 次群加法；超可逆矩阵（使用 $S'_{17,16,q}$）贡献 16 次群加法；合计 23 次群加法。此外还需 196 次小标量/标量乘法（等效约 5 次群加法），以及编码/解码、哈希、伪随机数生成等开销（总计约 3-5 次群加法）。因此每预签名总群加法当量约 31-33 次。单次群加法在常见机器上约 0.5 μs，故每签名计算时间约 20 μs，对应每秒 50,000 签名。网络方面，每参与方每签名发送 18 标量+9 群元素（约 10,000 bits），500 Mbps 带宽满足 50,000 签名/秒。在线阶段（两轮通信，批量）每签名仅需 6 标量通信，计算复杂度 $O(n)$ $\mathbb{Z}_q$ 运算。

### 局限性与开放问题

协议的安全性分析限于静态腐败模型；若采用自适应腐败，需要将 $\rho$ 增加 1，小幅影响性能。GoAVSS 和超可逆矩阵的大批量生成依赖 $L=\Omega(n^2)$ 或 $L=\Omega(n\log n)$ 的假设，对于小批量应用摊销效果不佳。此外，本文未考虑 ECDSA 所需的乘法操作，仅支持 Schnorr 签名及其线性组合；将 GoAVSS 扩展至支持域乘法（如 Beaver 三元组）仍需进一步研究。最后，协议依赖随机信标，其实践实现（如基于阈值 BLS 或链上共识）可能引入额外延迟和信任假设。

### 强关联论文

[29] Shoup et al. Lightweight Asynchronous Verifiable Secret Sharing. **ePrint 2023** [Google Scholar](https://scholar.google.com/scholar?q=Lightweight+Asynchronous+Verifiable+Secret+Sharing)

[3] Benhamouda et al. SPRINT: High-Throughput Robust Distributed Schnorr Signatures. **ePrint 2023** [Google Scholar](https://scholar.google.com/scholar?q=SPRINT+High-Throughput+Robust+Distributed+Schnorr+Signatures)

[28] Shoup. The Many Faces of Schnorr. **ePrint 2023** [Google Scholar](https://scholar.google.com/scholar?q=The+Many+Faces+of+Schnorr)

[21] Hirt et al. Robust Multiparty Computation with Linear Communication Complexity. **CRYPTO 2006** [Google Scholar](https://scholar.google.com/scholar?q=Robust+Multiparty+Computation+with+Linear+Communication+Complexity)

[2] Beerliová-Trubíniová et al. Perfectly-Secure MPC with Linear Communication Complexity. **TCC 2008** [Google Scholar](https://scholar.google.com/scholar?q=Perfectly-Secure+MPC+with+Linear+Communication+Complexity)

[6] Bracha. Asynchronous Byzantine Agreement Protocols. **Inf. Comput. 1987** [Google Scholar](https://scholar.google.com/scholar?q=Asynchronous+Byzantine+Agreement+Protocols)

[7] Cachin et al. Asynchronous Verifiable Information Dispersal. **DISC 2005** [Google Scholar](https://scholar.google.com/scholar?q=Asynchronous+Verifiable+Information+Dispersal)

[14] Feldman. A Practical Scheme for Non-Interactive Verifiable Secret Sharing. **FOCS 1987** [Google Scholar](https://scholar.google.com/scholar?q=A+Practical+Scheme+for+Non-Interactive+Verifiable+Secret+Sharing)

[26] Pedersen. A Threshold Cryptosystem without a Trusted Party. **EUROCRYPT 1991** [Google Scholar](https://scholar.google.com/scholar?q=A+Threshold+Cryptosystem+without+a+Trusted+Party)

[4] Boldyreva. Threshold Signatures, Multisignatures and Blind Signatures Based on the Gap-Diffie-Hellman-Group Signature Scheme. **PKC 2003** [Google Scholar](https://scholar.google.com/scholar?q=Threshold+Signatures+Multisignatures+and+Blind+Signatures+Based+on+the+Gap-Diffie-Hellman-Group+Signature+Scheme)


## 关键词

+ 门限Schnorr签名
+ 异步分布式密钥生成
+ 超可逆矩阵
+ 批量预签名
+ 多方计算
+ 最优容错性