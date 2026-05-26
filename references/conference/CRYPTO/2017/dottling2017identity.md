---
title: "Identity-based encryption from the Diffie-Hellman assumption"

标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 2017
created: 2025-04-29 10:30:46
modified: 2025-04-29 10:31:21
---

## Identity-based encryption from the Diffie-Hellman assumption

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-319-63688-7_18)

## 作者

+ [Nico Döttling](Nico%20D%C3%B6ttling.md)
+ [Sanjam Garg](Sanjam%20Garg.md) 

## 笔记

好的，作为一名密码学领域的研究助手，我将根据您提供的论文全文，按照指定格式输出详尽的结构化笔记。

### 背景与动机

身份基加密（IBE）方案允许使用接收者的身份字符串（如电子邮件地址）作为公钥进行加密，极大地简化了公钥证书的管理难题。尽管 Boneh 和 Franklin 于 CRYPTO 2001 首次提出了基于双线性配对的可行 IBE 方案 [11]，但所有已知构造均依赖于特定的代数结构，如双线性映射或格上的 LWE 问题。一个根本性的开放问题是能否基于更基础、更通用的假设，如计算性 Diffie-Hellman（CDH）假设或大整数分解假设，来构造 IBE 方案。此前，Boneh 等人的工作 [13] 证明了无法通过黑盒使用陷门置换或 CCA 安全的公钥加密来实现 IBE，而 Papakonstantinou 等人 [42] 也证明了仅黑盒使用 DDH 困难群组是无法实现 IBE 的。这些否定结果暗示了任何基于 CDH 的构造都必须打破黑盒还原的框架，对底层原语进行非黑盒使用。本工作填补了这项空白，首次展示了如何通过非黑盒地使用混淆电路，从 CDH 假设构造出标准安全定义的 IBE 和选择性安全的层级式 IBE（HIBE）方案。

### 相关工作

[11] Boneh Dan, Franklin Matt. Identity-Based Encryption from the Weil Pairing. **CRYPTO 2001** [Google Scholar](https://scholar.google.com/scholar?q=Identity-Based+Encryption+from+the+Weil+Pairing)
> 核心思路：首次提出了可行的 IBE 构造，利用 Weil 配对上的双线性性质实现身份到公钥的映射。
> 局限与区别：依赖于双线性映射这一特殊代数结构，而本文的目标是从更基础的 CDH 假设出发，无需配对即可实现 IBE。

[42] Papakonstantinou et al. How Powerful are the DDH Hard Groups? **ePrint 2012** [Google Scholar](https://scholar.google.com/scholar?q=How+Powerful+are+the+DDH+Hard+Groups)
> 核心思路：证明了在黑盒使用群运算的前提下，无法基于 DDH 困难群组构造 IBE。
> 局限与区别：该 impossibility 结果约束了黑盒构造的可能性，而本文通过非黑盒使用底层密码原语（混淆电路）来绕过这一限制。

[13] Boneh et al. On the Impossibility of Basing Identity Based Encryption on Trapdoor Permutations. **FOCS 2008** [Google Scholar](https://scholar.google.com/scholar?q=On+the+Impossibility+of+Basing+Identity+Based+Encryption+on+Trapdoor+Permutations)
> 核心思路：证明了无法通过黑盒方式，基于陷门置换或 CCA 安全的公钥加密来构造 IBE。
> 局限与区别：进一步强化了构造 IBE 的难度，本文通过非黑盒技术回避了这些 impossibility 壁垒。

[19] Cocks Clifford. An Identity Based Encryption Scheme Based on Quadratic Residues. **Cryptography and Coding 2001** [Google Scholar](https://scholar.google.com/scholar?q=An+Identity+Based+Encryption+Scheme+Based+on+Quadratic+Residues)
> 核心思路：提出了基于二次剩余假设的 IBE 方案，是少数不依赖配对但基于数论假设的构造之一。
> 局限与区别：该方案效率不高，且其安全性证明需要随机预言机模型，而本文方案无需随机预言机，基于 CDH 的标准模型。

[3] Agrawal Shweta, Boyen Xavier. Identity-Based Encryption from Lattices in the Standard Model. **Manuscript 2009** [Google Scholar](https://scholar.google.com/scholar?q=Identity-Based+Encryption+from+Lattices+in+the+Standard+Model)
> 核心思路：提出了基于格上 LWE 假设的标准模型下的 IBE 方案。
> 局限与区别：依赖 LWE 问题，而非群论假设。本文则探索了基于 CDH 这一更经典群论假设的可能性。

[6] Bellare Mihir, Rogaway Phillip. Random Oracles are Practical: A Paradigm for Designing Efficient Protocols. **ACM CCS 1993** [Google Scholar](https://scholar.google.com/scholar?q=Random+Oracles+are+Practical)
> 核心思路：提出了随机预言机模型，作为设计高效密码协议的一种实用范式。
> 局限与区别：许多早期 IBE 方案 [11, 19] 在该模型下证明安全，而本文构造的目标是在标准模型下实现安全。

### 核心技术与方案

本方案的核心思路是构建一个名为“变色龙加密”的新原语，并通过将其与混淆电路结合，以非黑盒的方式将指数级的公钥“压缩”进短的全局公开参数中，从而绕过已知的 impossibility 结果。该方案包含两个主要层次。

**第一层：从 CDH 到变色龙加密方案。** 作者首先构造了一个基于 CDH 假设的变色龙加密方案。该方案包含一个带陷门的变色龙哈希函数。哈希函数定义为 $\mathsf{H}(\mathsf{k}, \mathsf{x}; r) = g^r \prod_{j\in [n]} g_{j, \mathsf{x}_j}$。其加密功能允许加密者在知道哈希值 `h`、位置 `i` 和比特 `b` 的情况下，加密一个消息 `m`，生成密文 `ct`。解密时，只有知道 `h` 的原像 `(x, r)`，且 `x` 的第 `i` 位恰好等于加密时使用的比特 `b`，才能成功解密。其安全性基于 DDH 假设，可以通过一个标准的归约证明：若敌手能区分对 0 和 1 的加密，则可构造算法区分 DDH 元组。该变色龙加密方案可以基于素数阶群上的 CDH 假设或基于复合阶（Blum 整数）群上的大整数分解假设实例化。

**第二层：从变色龙加密到 IBE 方案。** 该 IBE 构造的核心是构建一棵深度为 `n` 的指数级大小的二叉树，每个叶子对应一个长度为 `n` 的身份。树中的每个节点 `v` 被分配了一个哈希值 `h_v`，哈希值通过递归方式计算：非叶子节点的哈希值依赖于其子节点的哈希值，叶子节点的哈希值依赖于一对随机生成的公钥 `(ek_{v||0}, ek_{v||1})`。所有哈希值和密钥对均由伪随机函数（PRF）可重现地生成，确保了整个指数大树的“压缩”表示。设置阶段输出根哈希值 `h_ε` 和各层的哈希密钥 `k_i` 作为主公钥；主私钥包含对应的陷门和 PRF 种子。一个身份 `id` 的私钥包含从根到叶子路径上所有节点的“本地密钥”（以及叶子的解密密钥 `dk_id`），这些本地密钥足以让用户遍历整个路径。

加密过程使用 `n+1` 个混淆电路。从 `P^0` 到 `P^{n-1}`，每个电路 `P^i` 的功能是：输入一个哈希值 `h_v`，输出一组由变色龙加密算法加密的输入标签，这些标签是下一个混淆电路的输入。电路 `T` 则是输入一个公钥 `ek`，输出消息 `m` 在该公钥下的加密。这些电路依次连接：`P^0` 的输入是 `h_ε`，其输出标签的密文集可以通过变色龙解密得到 `P^1` 的输入标签。这个过程逐层进行，直到解密出 `(ek_id, m)`，最后由解密密钥 `dk_id` 还原出明文。安全性证明通过一系列混合论证完成，逐层将真实的混淆电路替换为模拟生成的电路，最终将挑战密文中的消息替换为随机值，从而证明其安全性。该构造的计算复杂度主要来源于非黑盒使用底层加密算法在混淆电路内部生成密文，但可以通过将部分计算（如模幂运算）移出混淆电路进行优化。

### 核心公式与流程

**[变色龙哈希函数]**
$$
\mathsf{H}(\mathsf{k}, \mathsf{x}; r) = g^r \prod_{j\in [n]} g_{j, \mathsf{x}_j}
$$
> 作用：将输入 `x` 和随机数 `r` 映射到一个群元素 `h`。陷门允许在知道原像的情况下找到任意新原像，使得哈希值不变。

**[变色龙加密算法]**
$$
\mathsf{Enc}(\mathsf{k}, (\mathsf{h}, i, b), \mathsf{m}) = (e, c, c', \{c_{j,0}, c_{j,1}\}_{j\in [n]\setminus\{i\}})
$$
其中，$c = g^\rho$, $c' = \mathsf{h}^\rho$, $e = \mathsf{m} \oplus \mathsf{HardCore}(g_{i,b}^\rho)$。
> 作用：加密消息 `m`，使得只有知道满足 `h = H(k, x; r)` 且 `x_i = b` 的 `(x, r)` 的用户才能解密。

**[IBE 树结构定义]**
$$
h_{\mathsf{v}} = \begin{cases} \mathsf{H}(\mathsf{k}_{|\mathsf{v}|}, ek_{\mathsf{v}||0} \| ek_{\mathsf{v}||1}; r_{\mathsf{v}}) & \mathsf{v} \in \{0,1\}^{n-1} \\ \mathsf{H}(\mathsf{k}_{|\mathsf{v}|}, h_{\mathsf{v}||0} \| h_{\mathsf{v}||1}; r_{\mathsf{v}}) & \mathsf{v} \in \{0,1\}^{< n-1} \cup \{\varepsilon\} \end{cases}
$$
> 作用：定义了如何从底层公钥递归构建指数级大小的树结构，将身份映射到整个系统参数。

**[混合论证 - 安全归约的关键步骤]**
$$
\mathcal{H}_{\tau-1} \overset{c}{\approx} \mathcal{H}_{\tau}
$$
> 作用：证明了在计算意义上，相邻两个混合体的不可区分，从而将 `n+1` 个混淆电路（`P^0` 到 `T`）逐步从真实变为模拟，完成安全归约。

### 实验结果

论文正文中并未提供具体的实验数据或性能基准测试。作者明确指出，由于其构造大量非黑盒地使用了底层密码原语（即在混淆电路内部运行加密算法），导致方案效率较低，与基于双线性映射的高效 IBE 方案相比不具有竞争力。论文的效率讨论仅限于渐进复杂度的理论分析。例如，加密过程需要生成 `n+1` 个混淆电路，每个包含 `O(λ)` 个非黑盒的模幂运算。文中在“效率说明”部分指出，通过将部分计算移出混淆电路，可以将每个 `P` 电路中的非黑盒模幂运算次数减少到 2 次，并将树的分支因子从 2 增大以减少树深度，从而提高效率。然而，这些优化仅停留在理论设计阶段，未进行实际实现与验证。因此，本工作的主要贡献是理论上的可行性证明，而非工程实践。

### 局限性与开放问题

1.  该构造效率极低，主要由非黑盒使用底层加密算法导致的巨大开销所致，目前不具备实际应用价值。优化方案虽然被提出，但并未实现，其实际效果未知。
2.  构造得到的 HIBE 方案仅满足选择性安全，而非更强的适应性安全。虽然作者后续工作 [21] 提出了通用的转换方法，但本文的 HIBE 构造本身仍有安全性的提升空间。
3.  完全基于 CDH 假设构造高效的 IBE 方案仍然是该领域的一个核心开放问题，本文的主要贡献在于首次证明了“可能性”，而“高效性”有待未来工作解决。

### 强关联论文

[11] Boneh Dan, Franklin Matt. Identity-Based Encryption from the Weil Pairing. **CRYPTO 2001** [Google Scholar](https://scholar.google.com/scholar?q=Identity-Based+Encryption+from+the+Weil+Pairing)

[13] Boneh et al. On the Impossibility of Basing Identity Based Encryption on Trapdoor Permutations. **FOCS 2008** [Google Scholar](https://scholar.google.com/scholar?q=On+the+Impossibility+of+Basing+Identity+Based+Encryption+on+Trapdoor+Permutations)

[42] Papakonstantinou et al. How Powerful are the DDH Hard Groups? **ePrint 2012** [Google Scholar](https://scholar.google.com/scholar?q=How+Powerful+are+the+DDH+Hard+Groups)

[21] Döttling Nico, Garg Sanjam. From Selective IBE to Full IBE and Selective HIBE. **Manuscript 2017** [Google Scholar](https://scholar.google.com/scholar?q=From+Selective+IBE+to+Full+IBE+and+Selective+HIBE)

[5] Bellare et al. Foundations of Garbled Circuits. **ACM CCS 2012** [Google Scholar](https://scholar.google.com/scholar?q=Foundations+of+Garbled+Circuits)

[30] Goldreich Oded, Levin Leonid. A Hard-Core Predicate for All One-Way Functions. **STOC 1989** [Google Scholar](https://scholar.google.com/scholar?q=A+Hard-Core+Predicate+for+All+One-Way+Functions)

[46] Shmuely Z. Composite Diffie-Hellman Public-Key Generating Systems are Hard to Break. **Technical Report, Technion 1985** [Google Scholar](https://scholar.google.com/scholar?q=Composite+Diffie-Hellman+Public-Key+Generating+Systems+are+Hard+to+Break)

[38] McCurley Kevin. A Key Distribution System Equivalent to Factoring. **Journal of Cryptology 1988** [Google Scholar](https://scholar.google.com/scholar?q=A+Key+Distribution+System+Equivalent+to+Factoring)

[29] Goldreich et al. How to Construct Random Functions. **FOCS 1984** [Google Scholar](https://scholar.google.com/scholar?q=How+to+Construct+Random+Functions)

[34] Krawczyk Hugo, Rabin Tal. Chameleon Hashing and Signatures. **ePrint 1998** [Google Scholar](https://scholar.google.com/scholar?q=Chameleon+Hashing+and+Signatures)


## 关键词

+ 身份基加密Diffie-Hellman假设
+ 分层身份基加密因子分解
+ 混淆电路非黑盒密码原语使用
+ 无配对群IBE首次构造
+ 绕过不可能性结果IBE构造