---
title: "Post-Quantum Zero-Knowledge and Signatures from Symmetric-Key Primitives"
doi: 10.1145/3133956.3133997
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2017
modified: 2025-04-08 17:11:20
---
## Post-Quantum Zero-Knowledge and Signatures from Symmetric-Key Primitives

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3133956.3133997)

## 作者

+ [Melissa Chase](Melissa%20Chase.md)
+ David Derler
+ Steven Goldfeder
+ [Claudio Orlandi](Claudio%20Orlandi.md)
+ Sebastian Ramacher
+ Christian Rechberger,
+ Daniel Slamanig
+ Greg Zaverucha

## 笔记

### 背景与动机

自从Shor提出多项式时间的量子算法求解整数分解和离散对数问题以来 [81]，人们认识到足够强大的量子计算机能够攻破当今几乎所有公钥密码体制。为此，NIST启动了后量子密码项目，征集包括数字签名在内的后量子安全方案。现有后量子签名方案大多依赖结构化的数论假设：格签名（如BLISS [36]）基于理想格上的SIS问题，代码签名（如FS-Véron [86]）基于音译解码问题，多变量签名（如MQDSS [56]）基于求解多变量二次方程组问题。这些假设的量子安全性尚未被充分研究，例如理想格的安全性认知深度远不及标准格 [75]。纯hash-based签名（如SPHINCS [17]）仅依赖对称密钥原语，可以在标准模型下证明安全，但签名尺寸较大（约41 kB）且常需要维护状态。本文希望填补的空白是：构造一类仅依赖对称密钥原语（如Hash函数和分组密码）即可证明后量子安全的签名方案，同时保持极小的密钥尺寸和高参数灵活性，并同时覆盖随机预言机模型和量子可访问随机预言机模型下的安全性。

### 相关工作

[44] Giacomelli et al. ZKBoo: Faster zero-knowledge for boolean circuits. **USENIX Security 2016** [Google Scholar](https://scholar.google.com/scholar?q=ZKBoo+Faster+zero-knowledge+for+boolean+circuits)
> 核心思路：提出基于MPC-in-the-head范式的Sigma协议ZKBoo，用于对任意布尔电路构造零知识证明，并支持Fiat-Shamir变换得到非交互式证明。
> 局限与区别：ZKBoo的证明尺寸较大，本文通过多个优化（O1-O6）将其减小一半以上，得到ZKB++，且不增加计算开销。

[83] Unruh. Non-interactive zero-knowledge proofs in the quantum random oracle model. **EUROCRYPT 2015** [Google Scholar](https://scholar.google.com/scholar?q=Non-interactive+zero-knowledge+proofs+in+the+quantum+random+oracle+model)
> 核心思路：提出Fiat-Shamir变换的替代方案，可在量子可访问随机预言机模型下证明安全性，但通用的构造会引入4倍左右的尺寸开销。
> 局限与区别：本文通过利用ZKB++应答的重叠结构，将Unruh变换的尺寸开销降至仅1.6倍，并首次将其高效地应用到签名方案中。

[84] Unruh. Quantum proofs of knowledge. **EUROCRYPT 2012** [Google Scholar](https://scholar.google.com/scholar?q=Quantum+proofs+of+knowledge)
> 核心思路：提出在量子模型中证明知识提取性质的理论框架，是Unruh变换的基础。
> 局限与区别：本文修改了Unruh的通用构造，以适应ZKB++的3-特殊可靠性（3-special soundness）和优化后的承诺结构。

[17] Bernstein et al. SPHINCS: practical stateless hash-based signatures. **EUROCRYPT 2015** [Google Scholar](https://scholar.google.com/scholar?q=SPHINCS+practical+stateless+hash-based+signatures)
> 核心思路：构造实用的无状态Hash-based签名方案，安全性完全基于Hash函数的性质。
> 局限与区别：SPHINCS签名尺寸约41 kB（128-bit PQ安全），大于本文Fish方案的约118 kB，但SPHINCS的签名生成和验证时间更快（10-15 ms级）。本文方案提供更小的密钥尺寸（64 B vs. 1 kB）和更高的参数灵活性。

[36] Ducas et al. Lattice signatures and bimodal gaussians. **CRYPTO 2013** [Google Scholar](https://scholar.google.com/scholar?q=Lattice+signatures+and+bimodal+gaussians)
> 核心思路：提出BLISS格签名方案，利用理想格实现接近RSA的性能。
> 局限与区别：BLISS依赖理想格假设，其安全性认知不如标准格深入。本文Fish/Picnic仅依赖对称密钥原语，不引入任何结构化假设。

[56] Hülsing et al. From 5-pass MQ-based identification to MQ-based signatures. **ASIACRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=From+5-pass+MQ-based+identification+to+MQ-based+signatures)
> 核心思路：基于多变量二次方程问题的5-pass识别方案，应用Fiat-Shamir变换得到签名MQDSS。
> 局限与区别：MQDSS依赖多变量问题的困难性假设，签名尺寸约40 kB（128-bit PQ），小于本文方案。本文方案的优势在于仅依赖对称密钥原语，具有更简单的安全假设基础。

### 核心技术与方案

**整体框架**：本文构建两类后量子签名方案Fish和Picnic，共用相同的密钥生成和签名/验证框架（Scheme 2）：公钥为单向函数$f_k$在秘密密钥$x$上的像$y = f_k(x)$，签名即为知道$x$的非交互零知识证明，可绑定消息。区别在于将底层ZKB++ Sigma协议转换为非交互证明的方式：Fish使用Fiat-Shamir变换（安全在ROM中），Picnic使用Unruh变换（安全在QROM中）。

**底层Sigma协议的优化：ZKB++**：ZKBoo [44] 是一个3-消息Sigma协议，证明者将电路计算分解为三方的"在线"模拟并承诺；验证者随机选择两方打开检查。ZKB++通过六个关键优化大幅减小证明尺寸而不增加计算开销：
- O1：将输入份额通过伪随机生成器从种子$k_i$派生，从而View 1和View 2中只需包含种子$k_i$而非输入份额$x_i$本身。
- O2：对于不需要从种子派生的第三份额（$x_3$），只有在挑战要求该视图时才包含。
- O3：只发送被关闭视图对应的承诺，第三视图的承诺由验证者通过哈希从发送的内容中重新计算，不再发送。
- O4：利用种子$k_i$作为承诺的随机化值，省去额外的承诺随机数。
- O5：输出份额$y_i$可从视图内容重新计算，不直接发送；第三份额可通过$y_{e+2} = y + y_e + y_{e+1}$恢复。
- O6：对于被打开的e视图，验证者无需检查每个线值，只需通过检查承诺的绑定性来隐式验证。

ZKB++的证明预期大小为：$t [ c + 2\kappa + \log_2(3) + \ell \cdot (2/3 \cdot m + b) ]$。相比于ZKBoo，证明尺寸减半。

**Fish签名方案**：将ZKB++与Fiat-Shamir变换结合。签名者计算ZKB++的第一消息$r$（包含承诺和输出份额的哈希），再计算$c = H(r, m)$作为挑战，最后发送完整的响应$s$。验证者通过检查$c' = H(r', m') = c$来接受。安全性依赖于底层Sigma协议的3-特殊可靠性和随机预言机模型。具体地，证明者需要$t = \lceil \kappa (\log_2 3 - 1)^{-1} \rceil$轮并行重复以达到$\kappa$比特安全；对于128-bit PQ安全，t = 438。

**Picnic签名方案**：使用Unruh变换代替Fiat-Shamir。证明者为每个可能的挑战（1,2,3）计算响应$s_{ij}$，并计算$g_{ij} = G(s_{ij})$（G是一个排列）。挑战由$H(r_1, ..., r_t, g_{11}, ..., g_{t3})$决定。签名包含所有$r_i$、被选挑战对应的$s_{iJ_i}$以及所有$g_{ij}$。Picnic利用了ZKB++的特点优化：由于三个挑战对应的两个视图有很大的重叠，只需对三个视图本身应用G，而不是对三个独立的响应。仅需额外包含一个视图对应的$G(v)$，使得Unruh的开销仅为1.6倍。

**安全性证明**：
- Fish（FS变换）的EUF-CMA安全性：由Sigma协议的3-特殊可靠性保证，提取器可以获取两份不同挑战的有效响应恢复秘密$x$。证明使用forking引理思想（由于需要三个有效响应，需要额外rewind一次），在ROM中非紧约地归约到单向函数的安全性。
- Picnic（Unruh变换）的模拟提取性：在QROM中证明。零知识性通过序列游戏转化：先编程随机预言机生成挑战，再用随机值替换量子可查询的承诺输出。提取性通过定制Lemma D.2证明：除非找到G的碰撞或随机预言机的碰撞，否则$\text{Ver}^H$接受$\pi$但提取器失败的概率可忽略。该证明依赖于G的不可区分性、承诺的绑定性和$Z\text{KB++}$的3-特殊可靠性。

**渐进复杂度**：
- Fish签名大小：$\Theta(t ( \ell b + \kappa) )$，其中$t = 438$（128-bit PQ），$b$为AND门数，$\ell$为环大小（对于布尔电路$\ell=1$）。
- Picnic签名大小：$\Theta(t ( \ell b + \kappa) )$（约1.6倍Fish）。
- 密钥大小：$O(\kappa)$（sk为$\kappa$比特，pk为$2\kappa$比特）。
- 计算量：$O(t \cdot (b + \text{affine operations of LowMC}))$。
- 存储（证明端）：$O(t \cdot (b + m))$。

### 核心公式与流程

**[ZKB++ 证明大小公式]**
$$
|p| = \lceil \kappa (\log_2 3 - 1)^{-1} \rceil [ c + 2\kappa + \log_2(3) + \ell \cdot (2/3 \cdot m + b) ]
$$
> 作用：给出ZKB++方案在$\kappa$比特安全下，对于拥有$m$个输入、$b$个二进制乘法门、$\ell$比特环的电路的预期证明尺寸。该公式是后续Fish/Picnic签名尺寸计算的基础。

**[ZKB++ 证明验证流程]**
$$\begin{aligned}
x_{e}^{(i)} &\leftarrow \begin{cases}
G(k_1^{(i)}) & \text{if } e^{(i)} = 1 \\
G(k_2^{(i)}) & \text{if } e^{(i)} = 2 \\
x_3^{(i)} \text{ (from } z^{(i)}) & \text{if } e^{(i)} = 3
\end{cases} \\
x_{e+1}^{(i)} &\leftarrow \begin{cases}
G(k_2^{(i)}) & \text{if } e^{(i)} = 1 \\
x_3^{(i)} \text{ (from } z^{(i)}) & \text{if } e^{(i)} = 2 \\
G(k_1^{(i)}) & \text{if } e^{(i)} = 3
\end{cases} \\
\text{View}_{e}^{(i)} &\gets \text{Update}( \ldots \text{Update}(x_{e}^{(i)}, x_{e+1}^{(i)}, k_{e}^{(i)}, k_{e+1}^{(i)}) \ldots) \\
y_{e}^{(i)} &\gets \text{Output}(\text{View}_{e}^{(i)}), \quad y_{e+1}^{(i)} \gets \text{Output}(\text{View}_{e+1}^{(i)}), \quad y_{e+2}^{(i)} \gets y \oplus y_{e}^{(i)} \oplus y_{e+1}^{(i)}
\end{aligned}$$
> 作用：给出验证者在每个并行迭代$i$中重构视图、计算输出份额的步骤。验证者仅需打开两个视图，并通过XOR恢复第三个输出份额，可显著减小证明大小。

**[Fish/Picnic 签名方案（通用框架，Scheme 2）]**
$$\begin{aligned}
&\text{Gen}(1^\kappa):\\
&\quad \text{Choose } k \xleftarrow{R} \mathcal{K}_\kappa, x \xleftarrow{R} \mathcal{D}_\kappa, \text{ compute } y \gets f_k(x), \text{ set } \mathsf{pk} \gets (y,k), \mathsf{sk} \gets (\mathsf{pk}, x).\\
&\text{Sign}(\mathsf{sk}, m):\\
&\quad \text{Compute } p = (r, s) \gets \text{Prove}_H((y,k), x) \text{ with } c \gets H(r,m), \text{ return } \sigma \gets p.\\
&\text{Verify}(\mathsf{pk}, m, \sigma):\\
&\quad \text{Parse } \mathsf{pk} = (y,k), \sigma = p = (r,s). \text{ Return } 1 \text{ iff } \text{Verify}_H((y,k), p) = 1 \text{ with } c \gets H(r,m).
\end{aligned}$$
> 作用：给出Fish和Picnic共享的签名方案框架。Fish使用Fiat-Shamir变换（通过$H(r,m)$计算挑战），Picnic使用Unruh变换（挑战通过$H$从$r$和$g_{ij}$计算）。

### 实验结果

所有实验在Intel Core i7-4790 (4核, 3.60 GHz) 和16 GB RAM上运行，目标128-bit后量子安全，并行重复次数$t=438$。选择LowMC分组密码作为单向函数实例，推荐参数为256-256-10-38（块大小-密钥大小-S盒数-轮数）。Fish-10-38签名尺寸为118,525字节，签名时间29.73 ms，验证时间17.46 ms。Fish-1-316（减少S盒但增加轮数）签名尺寸108,013字节但速度慢（364 ms签名）。Picnic-10-38签名尺寸195,458字节（Unruh开销约1.6倍），签名/验证时间与Fish-10-38近似。与现有PQ签名方案相比：MQDSS签名尺寸约41 kB，速度快（7.21 ms签名）；SPHINCS-256签名尺寸41 kB，签名13.44 ms；BLISS-I签名尺寸5.7 kB，速度极快（0.12 ms签名）。Fish/Picnic的签名尺寸大于MQDSS和SPHINCS，但密钥尺寸仅64 B（vs. ~1 kB for SPHINCS），且不依赖结构化假设。特别是，本文方案相比基于理想格的BLISS（5.7 kB签名）和Ring-TESLA（1.6 kB签名）尺寸大得多，但BLISS和Ring-TESLA依赖的理想格假设安全性认知深度不如标准格。

### 局限性与开放问题

Fish/Picnic方案的签名尺寸（118–195 kB）仍显著大于经典的RSA签名和高效的格签名（如BLISS的5.7 kB），在带宽受限场景下可能不实用。通过设计新的对称密钥原语——特别地优化AND门数与环大小的权衡，有望进一步缩减签名尺寸。此外，ZKBoo/ZKB++协议本身仍然较新，未来可能出现更优的零知识证明方案（如文献[78]中的Ligero），可进一步改善性能。最后，本文的安全性证明在ROM/QROM中均为非紧约的，推广到标准模型或实现更紧的归约仍是开放问题。

### 强关联论文

[44] Giacomelli et al. ZKBoo: Faster zero-knowledge for boolean circuits. **USENIX Security 2016** [Google Scholar](https://scholar.google.com/scholar?q=ZKBoo+Faster+zero-knowledge+for+boolean+circuits)

[83] Unruh. Non-interactive zero-knowledge proofs in the quantum random oracle model. **EUROCRYPT 2015** [Google Scholar](https://scholar.google.com/scholar?q=Non-interactive+zero-knowledge+proofs+in+the+quantum+random+oracle+model)

[84] Unruh. Quantum proofs of knowledge. **EUROCRYPT 2012** [Google Scholar](https://scholar.google.com/scholar?q=Quantum+proofs+of+knowledge)

[17] Bernstein et al. SPHINCS: practical stateless hash-based signatures. **EUROCRYPT 2015** [Google Scholar](https://scholar.google.com/scholar?q=SPHINCS+practical+stateless+hash-based+signatures)

[36] Ducas et al. Lattice signatures and bimodal gaussians. **CRYPTO 2013** [Google Scholar](https://scholar.google.com/scholar?q=Lattice+signatures+and+bimodal+gaussians)

[56] Hülsing et al. From 5-pass MQ-based identification to MQ-based signatures. **ASIACRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=From+5-pass+MQ-based+identification+to+MQ-based+signatures)

[86] Véron. Improved identification schemes based on error-correcting codes. **Appl. Algebra Eng. Commun. Comput.** 1996 [Google Scholar](https://scholar.google.com/scholar?q=Improved+identification+schemes+based+on+error-correcting+codes)

[6] Albrecht et al. Ciphers for MPC and FHE. **EUROCRYPT 2015** [Google Scholar](https://scholar.google.com/scholar?q=Ciphers+for+MPC+and+FHE)

[57] Ishai et al. Zero-knowledge proofs from secure multiparty computation. **SIAM Journal on Computing** 2009 [Google Scholar](https://scholar.google.com/scholar?q=Zero-knowledge+proofs+from+secure+multiparty+computation)

[40] Fiat and Shamir. How to prove yourself: Practical solutions to identification and signature problems. **CRYPTO 1986** [Google Scholar](https://scholar.google.com/scholar?q=How+to+prove+yourself+Practical+solutions+to+identification+and+signature+problems)


## 关键词

+ 后量子密码学
+ 数字签名
+ 对称密钥原语
+ Sigma协议
+ 量子安全性