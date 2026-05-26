---
title: "Witness encryption and its applications"
标题简称:
论文类型: conference
会议简称: STOC
发表年份: 2013
created: 2025-04-29 10:19:47
modified: 2025-04-29 10:22:25
---

## Witness encryption and its applications

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/2488608.2488667)

## 作者

+ [Sanjam Garg](Sanjam%20Garg.md) 
+ [Craig Gentry](Craig%20Gentry.md)
+ [Amit Sahai](Amit%20Sahai.md)
+ [Brent Waters](Brent%20Waters.md)
## 笔记

### 背景与动机
传统公钥加密要求接收方拥有与公钥对应的秘密密钥，但在许多场景中，我们关心的是接收方是否知道某个NP问题的解（如填字游戏答案、哥德巴赫猜想的简短证明），而非是否持有密钥。本文正式引入并定义了**见证加密**（Witness Encryption）的概念：对于一个NP语言 \(L\)（对应证言关系 \(R\)），用户可将消息 \(M\) 加密到实例 \(x\) 上，任何知道满足 \(R(x,w)\) 的证言 \(w\) 的接收方能解密；若 \(x \notin L\)，则多项式时间敌手无法区分两个等长消息的加密。加密者本人甚至不知道 \(x\) 是否在语言中。该问题与Rudich于1989年提出的NP完全存取结构的计算秘密共享问题[31]密切相关，且一直缺少候选构造。此外，见证加密可看作构建公钥加密、身份基加密、属性基加密等基本密码原语的一种统一工具，其独特优势在于密钥生成算法复杂度可与底层NP问题的复杂度解耦，例如公钥加密中密钥生成仅需一次伪随机生成器求值，若能从单向函数构造见证加密则可避开公私钥加密的黑盒不可能性结果[24]。

---

### 相关工作

[1] Rudich. Unpublished, 1989.
> 核心思路：首次提出NP完全存取结构的计算秘密共享问题，并指出其可构建新颖的茫然传输协议。
> 局限与区别：该问题自提出后一直未有候选构造，本文首次给出了基于近似多线性映射的候选方案，并指出其等价于见证加密。

[2] Garg, Gentry, Halevi. Candidate Multilinear Maps from Ideal Lattices and Applications. **ePrint 2012/610**
> 核心思路：利用理想格构造“近似”多线性映射（称为分级编码系统），支持有限次加法和乘法同态。
> 局限与区别：原始构造主要面向通用多线性映射应用，本文将其适配到精确覆盖问题的NP实例上，通过提取算法实现容错，并证明了安全性依赖于分级编码的无精确覆盖假设。

[3] Boneh, Silverberg. Applications of Multilinear Forms to Cryptography. **Contemporary Mathematics 2003**
> 核心思路：提出理想多线性群族的概念并探索其在密码学中的潜在应用。
> 局限与区别：纯多线性映射仍为开放问题，本文采用GGH的近似实现，并说明其足以支撑见证加密。

[4] Goldreich, Levin. A Hard-Core Predicate for All One-Way Functions. **STOC 1989**
> 核心思路：任何单向函数都存在硬核谓词（Goldreich-Levin位）。
> 局限与区别：本文在构建身份基加密时利用GL位将签名转化为两个分离的NP语句，从而通过唯一签名性质提取签名伪造。

[5] Groth, Ostrovsky, Sahai. Perfect Non-Interactive Zero Knowledge for NP. **EUROCRYPT 2006**
> 核心思路：构造了完美非交互零知识证明（NIWI），满足完善可靠性。
> 局限与区别：本文在属性基加密和完全安全IBE中利用NIWI和完美绑定的承诺实现一种特殊签名方案，从而支撑分区策略的证明。

[6] Waters. Efficient Identity-Based Encryption Without Random Oracles. **EUROCRYPT 2005**
> 核心思路：通过分区策略（将身份空间划分为可签名和可挑战两部分）实现自适应安全的IBE。
> 局限与区别：Waters方案需处理人工中止问题，本文利用PRF对身份进行编码，使分区概率与查询次数成反比，从而避免人工中止。

---

### 核心技术与方案

**1. 见证加密的正式定义**  
一个见证加密方案由加密算法 Encrypt(\(1^\lambda, x, M\)) 和解密算法 Decrypt(CT, \(w\)) 组成。完备性要求：对于任意 \(M\) 和满足 \(R(x,w)\) 的 \((x,w)\)，解密以压倒性概率恢复 \(M\)。安全性要求：对于任意 \(x \notin L\) 和任意PPT敌手，无法区分对 \(M_0\) 和 \(M_1\) 的密文。注意方案不需要任何设置过程。

**2. 基于分级编码系统的构造**  
使用GGH分级编码系统[11]。给定一个精确覆盖实例 \((n, T_1, \dots, T_\ell)\)，加密者运行 InstGen 获得参数 params 和零测试参数 \(p_{zt}\)，采样随机 \(a_1,\dots,a_n \in R\)。对每个子集 \(T_i\)，计算编码 \(C_i = \mathsf{enc}^\dagger(\text{params}, |T_i|, \prod_{j\in T_i} a_j)\)。密钥为 \(K = \mathsf{ext}(\text{params}, p_{zt}, \mathsf{enc}^\dagger(\text{params}, n, a_1\cdots a_n))\)。解密时，若知道精确覆盖 \(I = \{j_1,\dots,j_{|I|}\}\)，则计算 \(B = \mathsf{mult}(\text{params}, C_{j_1},\dots,C_{j_{|I|}})\)，得到 \(n\) 级编码 \(a_1\cdots a_n\)，再通过抽取算法得到相同密钥 \(K\)。安全性基于决策分级编码无精确覆盖假设：对于无解的精确覆盖实例，敌手无法区分 \(B\) 为 \(a_1\cdots a_n\) 的编码还是随机独立元的编码。

**3. 从见证加密构建公钥加密**  
设 \(G:\{0,1\}^\lambda \to \{0,1\}^{2\lambda}\) 为伪随机生成器。密钥生成：选择随机种子 \(s\)，公钥 \(t = G(s)\)，私钥为 \(s\)。加密时，构造NP实例 \(x\) 使得 \(x \in L\) 当且仅当 \(t\) 处于 \(G\) 的值域中，然后用见证加密将消息 \(M\) 加密到 \(x\) 上。解密时，用 \(s\) 证明 \(t\) 在值域内以获取解密。安全性通过混合论证：先切换 \(t\) 为均匀随机串，此时 \(x \notin L\)，由见证加密安全性保证消息不可区分。该方案的关键是密钥生成复杂度与见证加密复杂度解耦。

**4. 从见证加密构建身份基加密**  
使用唯一签名方案（每个消息最多有一个有效签名）。签名密钥为秘密主密钥，验证密钥为公共参数。为身份 \(I\) 签发签名 \(\sigma\)。加密时，选择随机串 \(r\)，构造两个NP实例 \(x_0\) 和 \(x_1\)，分别对应于“存在签名 \(\sigma\) 使得 GL(\(\sigma,r)=0\) 且验证通过”和“GL(\(\sigma,r)=1\) 且验证通过”。由于唯一签名，只有一个实例为真。解密时，从私钥计算 \(b = \text{GL}(\sigma, r)\)，用对应密文解密。安全性可证：若敌手能区分，则可提取签名伪造。

**5. 从见证加密构建属性基加密（ABE）**  
采用一种特殊签名方案：公共参数包含两个承诺 \(c_1 = \text{Com}(0; r)\) 和 \(c_2 = \text{Com}(0^n; s)\)。密钥生成时，为电路 \(f\) 生成NIWI证明 \(\pi_f\)，证明“要么 \(c_1\) 是0的承诺，要么存在 \(a\) 使得 \(c_2\) 是 \(a\) 的承诺且 \(f(a)=0\)”。加密时，对输入 \(a\) 构造NP实例 \(x'\)：存在电路 \(g\) 和证明 \(\pi_g\) 使得 \(V(x_g, \pi_g)=1\) 且 \(g(a)=1\)，然后用见证加密将消息 \(M\) 加密到 \(x'\) 上。若 \(f(a)=1\)，用户可用其密钥 \((\pi_f)\) 证明 \(x'\) 为真。安全性证明通过切换参数：将 \(c_2\) 切换到攻击者目标输入 \(a^*\) 的承诺，此时任何满足 \(f(a^*)=1\) 的电路 \(f\) 都无法获得有效签名，从而敌手无法解密。

**6. 完全安全身份基加密**  
扩展ABE技巧。公共参数含三个承诺：\(c_1=\text{Com}(0; r)\), \(c_2=\text{Com}(s; R)\), \(c_3=\text{Com}(t; R')\)。密钥生成时，为身份 \(I\) 生成NIWI证明，证明“要么 \(c_1\) 是0的承诺，要么存在 \(s,t\) 使得 \(F'_{s,t}(I) \neq 0\)”，其中 \(F'\) 是PRF截断函数。加密时，构造NP实例：存在身份 \(I\) 的有效NIWI证明。安全性通过分区策略：在证明中将PRF的输出范围隐藏，使得大约 \(1/q\) 的身份可被用作挑战，其余可生成密钥，避免人工中止问题。

**复杂性**：所有构造中，证人加密本身的开销依赖于NP实例的规模（如精确覆盖的 \(n\) 和 \(\ell\)）。基于格的分级编码系统的参数规模为 \(\tilde{O}(n \lambda^2)\)，其中 \(\lambda\) 为安全参数，\(n\) 为多线性级数（等于NP实例中宇宙大小）。密文大小为 \(O(\ell)\) 个编码。解密通过一次多线性乘法（\(|I|\) 个输入）和一次抽取。各应用的渐进复杂度与底层NP问题实例的规模成线性或多项式关系。

---

### 核心公式与流程

**[精确覆盖实例]**
$$x = (n, T_1, \dots, T_\ell), \quad T_i \subseteq [n], \quad \text{witness } I \subseteq [\ell] \text{ such that } \{T_i: i\in I\} \text{ partitions } [n]$$

**[见证加密 KEM 加密]**
$$\forall i \in [\ell]:\ C_i = \mathsf{enc}^\dagger(\text{params}, |T_i|, \prod_{j\in T_i} a_j), \quad K = \mathsf{ext}(\text{params}, p_{zt}, \mathsf{enc}^\dagger(\text{params}, n, a_1\cdots a_n))$$
> 加密：为每个子集生成编码，密钥为全乘积的抽取。

**[见证加密 KEM 解密]**
$$B = \mathsf{mult}(\text{params}, C_{j_1}, \dots, C_{j_{|I|}}), \quad K = \mathsf{ext}(\text{params}, p_{zt}, B)$$
> 解密：用精确覆盖中的子集编码通过多线性乘法得到全乘积的编码。

**[决策分级编码无精确覆盖问题]**
分布1: \((h_1,\dots,h_\ell, \mathsf{enc}^\dagger(\text{params}, n, a_1\cdots a_n))\)，其中 \(h_i = \mathsf{enc}^\dagger(\text{params}, |T_i|, \prod_{j\in T_i} a_j)\)；
分布2: \((h_1,\dots,h_\ell, \mathsf{enc}^\dagger(\text{params}, n, r))\)，\(r\) 独立随机。
> 安全假设：对无解实例，上述两分布计算不可区分。

**[公钥加密构造]**
$$\text{PK} = t = G(s), \quad \text{SK} = s;\quad x \in L \iff \exists s: G(s)=t; \quad \text{CT} = \text{WE.Enc}(1^\lambda, x, M)$$
> 密钥生成：PRG种子；加密：构造值域实例。

**[IBE 构造（利用唯一签名和GL位）]**
$$\text{PP} = \text{verification key}, \quad \text{MSK} = \text{signing key};\quad\text{SK}_I = \text{Sign}(I)$$
$$\text{Encrypt}: \ r \leftarrow \{0,1\}^k;\ x_0: \exists \sigma, \text{GL}(\sigma,r)=0 \land \text{Verify}(I,\sigma)=1;\ x_1: \text{similar with GL}=1$$
$$\text{CT} = (I, x_0, x_1, r, \text{WE.Enc}(x_0, M), \text{WE.Enc}(x_1, M))$$
> 加密创建两个NP实例，分别对应GL位为0和1；由于唯一签名，只有一个实例为真。

**[ABE 构造（利用NIWI和承诺）]**
$$\text{PP} = (c_1, c_2), \ c_1 = \text{Com}(0;r),\ c_2 = \text{Com}(0^n;s);\ \text{SK}_f = (f, \pi_f)$$
$$\pi_f = P(\text{statement: } (c_1 = \text{Com}(0;w_1)) \vee (c_2 = \text{Com}(a;w_2) \land f(a)=0))$$
$$\text{Encrypt}(a, M):\ x': \exists g, \pi_g \text{ s.t. } V(x_g,\pi_g)=1 \land g(a)=1;\ \text{CT} = (a, x', \text{WE.Enc}(x', M))$$
> 密钥是NIWI证明，表明要么承诺为0要么存在\(a\)使电路输出0；加密实例要求存在电路及其证明满足电路在\(a\)上输出1。

---

### 实验结果

论文未提供实验评估。所有构造均为理论方案，安全性依赖于分级编码系统的假设。GGH[11]的原始论文给出了基于理想格的参数选择指南：对于安全参数\(\lambda\)和最大多线性级数\(n\)，选择分圆域的次数\(m = \tilde{O}(n\lambda^2)\)，编码噪声规模需满足乘法容错能力。该方案的密文大小和计算开销主要受限于分级编码系统的效率，目前尚无实际实现。后续工作（如[12]的ABE实现）有基于类似系统的实验，但本文本身没有。

---

### 局限性与开放问题

见证加密的安全性依赖于针对具体NP实例的决策分级编码无精确覆盖假设，该假设并非固定于标准密码学问题。本文证明不可能有基于与实例无关的简单假设的黑盒归约，除非该假设的硬度超过NP问题的判定难度。此外，构造中使用的近似多线性映射存在“噪音”问题，需要参数足够大以保证正确性和安全性，这导致方案效率很低。最后，见证加密方案缺乏设置算法，使得所有应用都只能基于NP完全问题，实际部署中需将目标问题归约到精确覆盖，带来额外开销。

---

### 强关联论文

[5] Boneh, Silverberg. Applications of Multilinear Forms to Cryptography. **Contemporary Mathematics 2003** [Google Scholar](https://scholar.google.com/scholar?q=Applications+of+Multilinear+Forms+to+Cryptography)

[11] Garg, Gentry, Halevi. Candidate Multilinear Maps from Ideal Lattices and Applications. **ePrint 2012/610** [Google Scholar](https://scholar.google.com/scholar?q=Candidate+Multilinear+Maps+from+Ideal+Lattices+and+Applications)

[15] Goldreich, Levin. A Hard-Core Predicate for All One-Way Functions. **STOC 1989** [Google Scholar](https://scholar.google.com/scholar?q=A+Hard-Core+Predicate+for+All+One-Way+Functions)

[18] Goldwasser, Ostrovsky. Invariant Signatures and Non-Interactive Zero-Knowledge Proofs Are Equivalent. **CRYPTO 1992** [Google Scholar](https://scholar.google.com/scholar?q=Invariant+Signatures+and+Non-Interactive+Zero-Knowledge+Proofs+Are+Equivalent)

[20] Groth, Ostrovsky, Sahai. Perfect Non-Interactive Zero Knowledge for NP. **EUROCRYPT 2006** [Google Scholar](https://scholar.google.com/scholar?q=Perfect+Non-Interactive+Zero+Knowledge+for+NP)

[24] Impagliazzo, Rudich. Limits on the Provable Consequences of One-Way Permutations. **STOC 1989** [Google Scholar](https://scholar.google.com/scholar?q=Limits+on+the+Provable+Consequences+of+One-Way+Permutations)

[29] Karp. Reducibility Among Combinatorial Problems. **Complexity of Computer Computations 1972** [Google Scholar](https://scholar.google.com/scholar?q=Reducibility+Among+Combinatorial+Problems)

[31] Rudich. Unpublished, 1989.

[32] Sahai, Waters. Fuzzy Identity-Based Encryption. **EUROCRYPT 2005** [Google Scholar](https://scholar.google.com/scholar?q=Fuzzy+Identity-Based+Encryption)

[35] Waters. Efficient Identity-Based Encryption Without Random Oracles. **EUROCRYPT 2005** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+Identity-Based+Encryption+Without+Random+Oracles)


## 关键词

+ 见证加密Witness Encryption
+ NP语言加密方案
+ 多线性映射密码构造
+ 计算型秘密共享
+ 精确覆盖NP完全问题
+ 密码学原语构建
