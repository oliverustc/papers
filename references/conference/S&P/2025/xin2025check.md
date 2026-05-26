---
title: "Check-Before-you-Solve: Verifiable Time-lock Puzzles"
标题简称: 
论文类型: conference
会议简称: S&P
发表年份: 2025
modified: 2025-04-22 17:16:02
created: 2025-04-08 21:15:12
---

## "Check-Before-you-Solve": Verifiable Time-lock Puzzles

## 发表信息

+ 原文链接暂无
+ [archive](https://eprint.iacr.org/2025/225)

## 作者

+ [Jiajun Xin](Jiajun%20Xin.md)
+ [Dimitrios Papadopoulos](Dimitrios%20Papadopoulos.md)

## 笔记

### 背景与动机
时间锁谜题（TLP）[1] 允许谜题生成者创建一个谜题，使得任何求解者都至少需要花费 T 步顺序计算才能得到解，即使使用多机并行也无法加速。这一特性使其被广泛应用于公平合同签署 [2]、密封投标拍卖 [1，8，11，12]、分布式随机性生成 [8，19] 以及去中心化金融中的抢跑预防 [21] 等场景。然而，TLP 的“不对称性”是一把双刃剑：求解者投入大量计算资源后，却无法事先确保得到的解是“有用”的——例如在区块链环境中，恶意生成者可能强迫其他参与者浪费算力去求解一个无意义的谜题。Thyagarajan 等人 [6] 针对时间锁签名这一特例提出了可验证方案，但其依赖线性同态 TLP [3] 与门限秘密共享 [31] 的多次迭代，导致证明时间约 30 秒、验证时间约 40 秒，且存在非可忽略的可靠度误差 (约 \(10^{-12}\))。本文试图填补的空白是：是否存在一种高效方案，能够为任意 NP 关系提供可验证的时间锁谜题，使求解者在投入资源前就能确认解满足特定性质。

### 相关工作

[1] Rivest 等人. Time-lock puzzles and timed-release crypto. **1994未发表论文** [Google Scholar](https://scholar.google.com/scholar?q=Time-lock+puzzles+and+timed-release+crypto)
> 核心思路：首次提出基于重复平方运算的 RSA TLP，生成者知道阶的陷门可快速构造谜题，而求解者需顺序执行 T 步。  
> 局限与区别：无法对解的性质提供任何保证，求解者只能盲目信任生成者。

[2] Boneh 等人. Timed commitments. **CRYPTO 2000** [Google Scholar](https://scholar.google.com/scholar?q=Timed+commitments)
> 核心思路：将 TLP 与承诺方案结合，实现“定时承诺”，在截止时间前承诺者可以反悔。  
> 局限与区别：同样未考虑解的可验证性，不能防止恶意生成者提交无效解。

[3] Malavolta 等人. Homomorphic time-lock puzzles and applications. **CRYPTO 2019** [Google Scholar](https://scholar.google.com/scholar?q=Homomorphic+time-lock+puzzles+and+applications)
> 核心思路：构造线性同态 TLP，支持对多个谜题的同态操作，实现批量求解。  
> 局限与区别：其验证方案（如 [6] 所用）需要门限秘密共享，导致线性膨胀的证明大小和非可忽略的可靠度误差。

[6] Thyagarajan 等人. Verifiable timed signatures made practical. **ACM CCS 2020** [Google Scholar](https://scholar.google.com/scholar?q=Verifiable+timed+signatures+made+practical)
> 核心思路：通过线性同态 TLP 与门限秘密共享实现时间锁签名，使求解者可以保证解是有效签名。  
> 局限与区别：证明和验证开销与门限数线性相关，且存在约 7.25×10⁻¹² 的可靠度误差；本文的 SNARK 方案将其改进为恒定证明大小和可忽略可靠度误差。

[12] Tyagi 等人. Riggs: Decentralized sealed-bid auctions. **ACM CCS 2023** [Google Scholar](https://scholar.google.com/scholar?q=Riggs+Decentralized+sealed-bid+auctions)
> 核心思路：使用 Pedersen 承诺和 TLP 实现密封投标拍卖，通过质押机制保证一致性。  
> 局限与区别：为避免 SNARK 开销采用质押方案，对所有诚实投标者造成资金负担；本文的 VTLP 可作为直接替换，实验表明效率高约 150 倍。

[27] Boneh 等人. Batching techniques for accumulators with applications to IOPs and stateless blockchains. **CRYPTO 2019** [Google Scholar](https://scholar.google.com/scholar?q=Batching+techniques+for+accumulators+with+applications+to+IOPs+and+stateless+blockchains)
> 核心思路：提出 PoKE 和 PoKE∗ 协议，用于隐藏阶群中指数关系的知识证明，支持累积器的批量更新。  
> 局限与区别：仅支持素数模的指数知识证明；本文扩展为通用整数模的 PoKEModN，并进一步构造了双指数与模指数协议。

[28] Camenisch 等人. Efficient group signature schemes for large groups. **CRYPTO 1997** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+group+signature+schemes+for+large+groups)
> 核心思路：首次提出隐藏阶群上的双指数证明协议，但证明大小与验证开销均与安全参数线性相关。  
> 局限与区别：通信和计算复杂度为 O(λ) 量级；本文的 PoKDE 和 PoMoDE 实现了常数大小的证明和常数时间验证。

[42] Wesolowski. Efficient verifiable delay functions. **EUROCRYPT 2019** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+verifiable+delay+functions)
> 核心思路：提出基于自适应根假设的指数证明协议（PoE），用于 VDF 的快速验证。  
> 局限与区别：PoE 仅证明指数关系而非知识；本文将其延伸为知识证明，并推广到双指数和模指数场景。

[57] Campanelli 等人. LegoSNARK: Modular design and composition of succinct zero-knowledge proofs. **ACM CCS 2019** [Google Scholar](https://scholar.google.com/scholar?q=LegoSNARK+Modular+design+and+composition+of+succinct+zero-knowledge+proofs)
> 核心思路：提出 Commit-and-Prove SNARK 框架，支持通过承诺组合多个 SNARK 子证明。  
> 局限与区别：本文利用该框架构建了 OffloadProd 和 OffloadExp，将隐藏阶群上的计算“卸载”到 SNARK 之外。

### 核心技术与方案
本文的整体框架分为三层。第一层是基础的隐藏阶群协议，包括 PoKEModN、PoKDE 及它们的零知识变体 ZK-PoKEModN 和 ZK-PoKDE，并最终构造 ZK-PoMoDE 协议。第二层是 SNARK 卸载技术 OffloadProd（用于证明一组整数的乘积）和 OffloadExp（用于证明 RSA 模指数），它们利用第一层的协议将复杂计算移出 SNARK 电路，仅保留一个轻量级的模约简检查。第三层是两种 VTLP 构造：面向任意 NP 关系的通用方案（结合 OffloadExpCom 和 CP-SNARK），以及面向 RSA 签名/VRF 的高效方案（直接使用 ZK-PoMoDE）。

**PoKEModN 协议**将原 PoKEMon 从素数模推广到任意整数模 n。其核心步骤如下：验证者发送素数挑战 ℓ；证明者计算商 q 和余数 r 使得 \(x = q(\ell \cdot n) + r\)，并发送 \(Q = g^q\) 及 r；验证者检查 \(r \in [\ell \cdot n]\)，\(Q^{\ell n} g^r = C\)，以及 \(r \bmod n = \hat{x}\)。安全性依赖于扩展的 Shamir 技巧：若 \(x \not\equiv r \pmod{\ell n}\)，则 \(\gcd(\ell n, x-r) < \min(\ell n, x-r)\)，可解出非平凡根从而破坏强 RSA 假设。零知识版本 ZK-PoKEModN 通过随机化 \(z = x + mn\)（m 为盲化因子）实现统计零知识。

**PoKDE 协议**用于证明 \(C_1 = g^x\) 且 \(C_2 = g^{x^e}\)。验证者发送素数 ℓ；证明者计算 \(x \bmod \ell = r_1\)、\(x^e \bmod \ell = r_2\) 及对应的商 \(Q_1, Q_2\)；验证者检查 \(Q_1^\ell g^{r_1} = C_1\)、\(Q_2^\ell g^{r_2} = C_2\) 以及 \(r_1^e \equiv r_2 \pmod{\ell}\)。若 \(x_2 \neq x_1^e\)，则可由中国剩余定理构造同一元素的两种指数表示，破坏阶假设。零知识版本 ZK-PoKDE 利用非光滑随机数 \(\gamma\)（概率 \(1-2^{-\lambda}\)）保证盲化后仍能检查指数一致性。

**ZK-PoMoDE 协议**组合上述协议证明 \(C = g^x\) 且 \(x^e \bmod n = \hat{x}\)。证明者先随机化 \(x\) 为 \(x + mn\)，计算 \(C_2 = g^{(x+mn)^e}\)；然后使用 ZK-PoKDE 证明 \(C_1 \times D^n\) 和 \(C_2\) 之间的双指数关系；最后使用 ZK-PoKEModN 证明 \(C_2\) 的指数模 n 等于 \(\hat{x}\)。证明大小为 17 个 G? 元素和 9 个域元素（约 4896 字节），验证时间恒定（29-32 ms）。

**OffloadProd** 用于卸载集合乘积计算：证明者计算隐藏阶群元素 \(A = g^x\)（x 为所有元素的乘积），验证者通过挑战素数 ℓ 检查 \(x \bmod \ell\) 是否等于集合元素乘积模 ℓ；SNARK 电路仅需计算模 ℓ 的乘积，复杂度降至 O(|集合|)。

**OffloadExp** 用于卸载 RSA 模指数：将指数 x 按二进制展开，预计算 \(v_i = u^{2^i} \bmod N\)，累积积 \(\omega = \prod v_i^{x_i}\)。证明者提交 \(A = g^\omega\)，并利用 ZK-PoKEModN 证明 \(\omega \bmod N = C\)；SNARK 电路仅需检查 \(\omega \bmod \ell\) 与由 x 选择的 \(v_i\) 的乘积模 ℓ 一致。与直接在 SNARK 内计算 2048 位指数（约 7200 万约束）相比，OffloadExp 仅需约 53.5 万约束（约 140 倍压缩）。

**通用 VTLP 构造**：生成者使用 RSA TLP [1] 加密解 s，同时通过 OffloadExpCom 证明隐藏阶群承诺 D 满足 \(D = g^{z^\tau \bmod N}\)（\(\tau = 2^T \bmod pq\)）；再通过 CP-SNARK 证明 D 的解码结果满足任意 NP 关系 R。时间锁安全性基于顺序平方假设和 DDH-II 假设，可靠性和零知识分别来自 OffloadExpCom 和 CP-SNARK。

**RSA 签名/VRF VTLP**：直接使用 ZK-PoMoDE 证明 \(D = g^s\) 且 \(s^e \bmod \bar{N} = \text{FDH}(m)\)；再通过 OffloadExpCom 证明 D 与谜题 z 的一致性。无需 SNARK，证明时间约 2.28 秒（e=3）或 3.08 秒（e=17），验证时间 29-32 ms。零知识性依赖于 VRF 的存在伪随机性。

### 核心公式与流程

**[PoKEModN 协议验证式]**
$$
Q^{\ell \cdot n} g^r \stackrel{?}{=} C, \quad r \bmod n = \hat{x}
$$
> 作用：验证隐藏阶群元素 C 的离散对数 x 满足 \(g^x = C\) 且 x 模 n 余 \(\hat{x}\)。

**[ZK-PoKDE 中利用非光滑随机数的关键等式]**
$$
E / K = g^{\omega} = g^{\omega' (m + \gamma)}, \quad E = g^{(x \ell + m + \gamma)^e}, \quad K = C_2^{\ell^e}
$$
> 作用：通过 \(m + \gamma\) 整除 \(x^e - \sigma\) 的论证保证 \(C_2 = g^{x^e}\)；非光滑性使整除概率可忽略。

**[OffloadExp 的累积积与模约简]**
$$
\omega = \prod_{i=0}^{|N|-1} (u^{2^i} \bmod N)^{x_i}, \quad r = \omega \bmod \ell
$$
> 作用：将 RSA 模指数 \(u^x \bmod N\) 转化为二进制乘积形式，仅对模 \(\ell\) 的余数 r 进行 SNARK 检查。

**[通用 VTLP 中解与承诺的绑定]**
$$
D = g^{s'}, \quad s' = s \times 2^{4\lambda} + \nu, \quad z = (s')^{\tau^{-1}} \bmod N
$$
> 作用：用填充随机数 \(\nu\) 将解 s 编码为 \(s'\)，并利用 RSA TLP 的陷门 \(\tau^{-1}\) 构造谜题 z。

### 实验结果
实验在搭载 AMD Ryzen 7 5800H（8 核 3.2 GHz）和 16 GB RAM 的笔记本电脑上运行，所有方案使用 Go 语言实现，SNARK 采用 Groth16（BN254 曲线）。对于 PoMoDE 协议，在 2048 位模数 n 下，指数 e=3 时证明时间 0.2 秒，e=17 时为 1.0 秒，e=256 时为 14.3 秒，验证时间恒为 29-32 ms。通用 VTLP 的解验证（2048 位 TLP）需约 2.08 秒（53.5 万约束），与 CP-SNARK 组合后：MiMC 哈希验证额外增加 0.007 秒，EdDSA 签名验证额外增加 0.05 秒。与 Thyagarajan 等人 [6] 的时间锁签名相比：BLS 签名场景下本文需 1.37 秒（约 \(2.8 \times 10^5\) 约束），而 [6] 在 \(\mathcal{T}=10^6\) 时需要约 30 秒证明和 41 秒验证；EdDSA 场景本文需 1.27 秒，[6] 约 10 秒。与 Riggs [12] 比较：Riggs 对 2048 位随机化器的 TLP 验证需约 328 秒，而本文仅需 2.13 秒（约 150 倍）。RSA 签名/VRF VTLP 中，公开指数 e=3 时证明时间 2.28 秒，e=17 时为 3.08 秒。签名卸载方面，1000 个 3072 位 RSA 签名的 offload 证明需约 30 万约束和 5 秒证明时间，零知识版本增加约 53 万约束和 1.6 秒；与 EdDSA+BabyJubjub 基线（约 75 万约束、13 秒）相比快约 1.5-4 倍。

### 局限性与开放问题
本文的通用 VTLP 构造依赖 Groth16 等预处理的 SNARK，需要为每个关系 R 和每个时间参数 T 进行可信设置，这限制了其在动态参数场景下的灵活性。此外，OffloadExp 的约束规模虽已大幅压缩，但仍与 RSA 模数的比特长度线性相关（约 \(|N|\) 次模 ℓ 运算），对于 4096 位以上模数可能带来性能退化。最后，RSA 签名 VTLP 的安全性依赖 FDH 提的随机预言机模型，在实际部署中需谨慎实例化。

### 强关联论文

[1] Rivest 等人. Time-lock puzzles and timed-release crypto. **1994未发表论文** [Google Scholar](https://scholar.google.com/scholar?q=Time-lock+puzzles+and+timed-release+crypto)

[3] Malavolta 等人. Homomorphic time-lock puzzles and applications. **CRYPTO 2019** [Google Scholar](https://scholar.google.com/scholar?q=Homomorphic+time-lock+puzzles+and+applications)

[6] Thyagarajan 等人. Verifiable timed signatures made practical. **ACM CCS 2020** [Google Scholar](https://scholar.google.com/scholar?q=Verifiable+timed+signatures+made+practical)

[12] Tyagi 等人. Riggs: Decentralized sealed-bid auctions. **ACM CCS 2023** [Google Scholar](https://scholar.google.com/scholar?q=Riggs+Decentralized+sealed-bid+auctions)

[23] Groth. On the size of pairing-based non-interactive arguments. **EUROCRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=On+the+size+of+pairing-based+non-interactive+arguments)

[27] Boneh 等人. Batching techniques for accumulators with applications to IOPs and stateless blockchains. **CRYPTO 2019** [Google Scholar](https://scholar.google.com/scholar?q=Batching+techniques+for+accumulators+with+applications+to+IOPs+and+stateless+blockchains)

[42] Wesolowski. Efficient verifiable delay functions. **EUROCRYPT 2019** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+verifiable+delay+functions)

[57] Campanelli 等人. LegoSNARK: Modular design and composition of succinct zero-knowledge proofs. **ACM CCS 2019** [Google Scholar](https://scholar.google.com/scholar?q=LegoSNARK+Modular+design+and+composition+of+succinct+zero-knowledge+proofs)

[71] Campanelli 等人. Succinct zero-knowledge batch proofs for set accumulators. **ACM CCS 2022** [Google Scholar](https://scholar.google.com/scholar?q=Succinct+zero-knowledge+batch+proofs+for+set+accumulators)

[82] Botrel 等人. gnark: v0.8.0. **GitHub 2023** [Google Scholar](https://scholar.google.com/scholar?q=gnark+v0.8.0)


## 关键词

+ 可验证时间锁谜题VTLP
+ RSA时间锁谜题
+ SNARK电路模群幂运算
+ 常数大小证明
+ 可验证随机函数VRF
+ 分布式随机性生成

**Note:** This is the full version of our publication. We made minor modifications to the security definitions.