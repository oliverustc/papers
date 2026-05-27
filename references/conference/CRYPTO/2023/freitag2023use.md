---
title: "How to use plain witness encryption: registered ABE, flexible broadcast, and more"
doi: 10.1007/978-3-031-38551-3_16
标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 2023
created: 2025-04-29 10:34:47
modified: 2025-04-29 17:13:03
---
## How to use plain witness encryption: registered ABE, flexible broadcast, and more

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-38551-3_16)

## 作者

+ Cody Freitag 
+ [Brent Waters](Brent%20Waters.md)
+ David J Wu 

## 笔记

### 背景与动机
公钥加密允许任何人使用公钥加密消息，只有持有对应私钥的接收者才能解密。然而，传统公钥加密需要公钥基础设施来绑定用户身份与公钥。属性基加密（ABE）和广播加密通过引入策略控制或群组广播扩展了功能，但通常依赖一个完全可信的中心化密钥发行机构。这种中心化信任假设在去中心化应用（如电子投票或分布式账本）中构成安全瓶颈和单点故障风险。近年来，虽然基于网格的见证加密构造取得突破 [54,55]，但其应用多局限于基础加密功能，尚未被充分挖掘以实现更高级的原语。先前，灵活广播加密和注册ABE仅能通过极难构造的不可区分混淆（i O）实现 [13,46]。本文试图填补这一空白：探索如何利用普通的见证加密（而非其增强版本如位置见证加密）来构造这些高级原语，从而避免对 i O 的依赖，并有望获得更高效、更基于标准假设的解决方案。

### 相关工作

[13] Boneh 和 Zhandry. multiparty key exchange, efficient traitor tracing, and more from indistinguishability obfuscation. **CRYPTO 2014** [Google Scholar](https://scholar.google.com/scholar?q=multiparty+key+exchange+efficient+traitor+tracing+and+more+from+indistinguishability+obfuscation)
> 核心思路：利用 i O 构造分布式广播加密，用户自行生成密钥但需绑定唯一索引。
> 局限与区别：其安全性依赖 i O，构造复杂且效率低。本文用普通见证加密和函数绑定哈希函数实现类似但不需索引绑定的灵活广播加密。

[46] Hohenberger 等. Registered attribute-based encryption. **EUROCRYPT 2023** [Google Scholar](https://scholar.google.com/scholar?q=Registered+attribute-based+encryption)
> 核心思路：提出注册ABE概念，并用 i O 构造了支持无限用户的方案。
> 局限与区别：i O 的构造使其实际部署困难。本文展示了如何用普通见证加密和函数绑定哈希函数实现相同功能。

[47] Hubáček 和 Wichs. On the communication complexity of secure function evaluation with long output. **ITCS 2015** [Google Scholar](https://scholar.google.com/scholar?q=On+the+communication+complexity+of+secure+function+evaluation+with+long+output)
> 核心思路：引入某种统计绑定哈希（SSB）函数，能统计绑定到输入的少数比特。
> 局限与区别：SSB 函数只能绑定到单个索引，不足以直接用于见证加密的安全证明。本文提出函数绑定哈希，可绑定到输入函数的输出（如析取），从而克服此局限。

[32] Garg 等. Witness encryption and its applications. **STOC 2013** [Google Scholar](https://scholar.google.com/scholar?q=Witness+encryption+and+its+applications)
> 核心思路：提出见证加密的概念，用 NP 语句作为公钥，对应的见证作为私钥。
> 局限与区别：早期构造依赖 i O 或多线性映射。本文基于其基本定义，结合函数绑定哈希来构造高级应用。

[36] Gentry 等. Witness encryption from instance independent assumptions. **CRYPTO 2014** [Google Scholar](https://scholar.google.com/scholar?q=Witness+encryption+from+instance+independent+assumptions)
> 核心思路：提出位置见证加密，具备索引隐藏性质。
> 局限与区别：位置见证加密的构造仍需 i O。本文旨在使用普通见证加密，避免更强更复杂的变体。

[54] Tsabary. Candidate witness encryption from lattice techniques. **CRYPTO 2022** [Google Scholar](https://scholar.google.com/scholar?q=Candidate+witness+encryption+from+lattice+techniques)
> 核心思路：基于 evasive LWE 假设构造见证加密。
> 局限与区别：该构造不直接给出高级应用。本文将其用作底层原语，并证明其可用于构建灵活广播加密和注册ABE。

[55] Vaikuntanathan 等. Witness encryption and null-IO from evasive LWE. **ASIACRYPT 2022** [Google Scholar](https://scholar.google.com/scholar?q=Witness+encryption+and+null-IO+from+evasive+LWE)
> 核心思路：与 [54] 类似，基于 evasive LWE 构造见证加密。
> 局限与区别：同上，其潜能尚未被充分挖掘用于高级应用。本文展示了其应用潜力。

### 核心技术与方案

本文核心技术创新为函数绑定哈希函数，并展示了如何将其与普通见证加密结合，构造灵活广播加密和注册属性基加密。

**函数绑定哈希函数**：传统的位置统计绑定哈希函数只能统计绑定到输入向量的某一个特定位置（例如，绑定 dig 使得只有该位置上的输入值才能被合法打开）。函数绑定哈希函数则将这一思想推广，要求哈希值统计绑定到整个输入向量经过某个函数 f 映射后的输出。具体地，给定一个函数 f 和哈希键 hk，如果计算 dig = H(hk, (x_1, ..., x_n))，那么对于任意索引 j，任何合法的打开 (j, x_j') 都必须满足：存在其他位置的赋值，使得 f 在这些赋值上的输出等于原始 f(x_1, ..., x_n)。否则，该打开就不存在。这意味着，如果函数 f 的输出是 0（比如 f 是析取函数，且所有 g(x_i)=0），那么就不存在一个打开能够声称某个 x_j' 使得 g(x_j')=1，因为这将导致 f 的输出变为 1，与已知的 dig 所绑定的 0 矛盾。这一性质正是安全证明中的关键。

**构造思路**：本文的构造采用一个通用模板。以灵活广播加密为例，系统参数包含一个公钥加密方案 PKE 的公钥 pk 和一个函数绑定哈希的哈希键 hk。每个用户生成密钥时，用 pk 加密比特 1 得到密文 c，并将 c 作为公钥，加密所使用的随机数 r 作为私钥。加密者对一个用户公钥集合 (c_1, ..., c_n) 加密消息 m 时，首先计算 digest = H(hk, (c_1, ..., c_n))，然后将消息 m 用见证加密加密，对应的 NP 语句包含 (hk, pk, digest)。解密时，用户 i 需要提供一个见证，包括其索引 i、公钥 c_i、私钥 r_i 以及一个简洁的打开 π_i，证明 c_i 确实是公钥集合中的第 i 个元素。见证加密的正确性保证了只有能提供有效见证的用户才能解密。

**安全性直觉**：安全证明的核心是利用函数绑定哈希的统计绑定性质。在安全游戏中，敌手不能解密挑战密文，因此攻击者没有私钥。证明开始，我们将挑战密文对应的用户公钥全部替换为加密 0 的密文。然后，将哈希键 hk 设置为统计绑定于函数 f_g，其中 g(c) = PKE.Dec(sk, c)。由于现在所有公钥 c_i 都是加密 0，所以 f_g(c_1, ..., c_n) = 0。现在考虑任何敌手可能提交的见证 (i, c, π, r)。要使验证通过，必须满足 c = PKE.Enc(pk, 1; r)，故 g(c) = 1。但若 f_g 的输出为 0，根据函数绑定哈希的统计绑定性质，不存在合法的打开 π 能证明 c 属于该集合（因为任何包含 c 的集合都会使 f_g 的输出变为 1，与统计绑定的 dig 矛盾）。因此，不存在任何有效见证，挑战密文对应的 NP 语句为假。依据见证加密的安全性，此时消息被隐藏。

**复杂度**：对于 n 用户广播，密文大小为 poly(λ, log n)，用户私钥大小为常数，公钥大小取决于具体构造。在随机谕言模型下，可进一步优化为所有参数（公钥、私钥、密文）均为 polylog(n)。注册ABE的紧凑性类似。

### 核心公式与流程

**[函数绑定哈希的统计绑定安全游戏]**
$$
\operatorname{Pr}[\mathsf{Expt}_{A,n(\lambda)}^{\mathsf{FB}}(\lambda) = 1] \leq \mathsf{negl}(\lambda)
$$
> 作用：定义函数绑定哈希的安全目标。敌手 A 输出函数 f 和输入 (x_1,...,x_k)，Challenger 生成绑定于 f 的 hk 并计算 dig = H(hk, (x_1,...,x_k))。若 A 能针对索引 S 输出打开 π 和值 x_j*，使得 VerOpen 通过，但不存在任何对剩余位置的赋值能使 f 的输出与 dig 所绑定的原输出保持一致，则敌手获胜。该概率可忽略。

**[析取函数的构造]**
构建一棵深度为 $\alpha = \lceil \log_2 n \rceil$ 的 Merkle 树。叶子层：对每个输入 $x_i$，计算 $\mathsf{ct}_i = \mathsf{LHE.Eval}(\mathsf{pk}_0, U(\cdot, x_i), c_g)$，其中 $c_g$ 是加密的函数 g 的密文。内部节点 $j$：使用两级同态加密密钥，计算 $h_j(\mathsf{node}_1, \mathsf{node}_2) = \mathsf{LHE.Eval}(\mathsf{pk}_j, f_{\mathsf{node}_1,\mathsf{node}_2,j}, c_j)$，其中函数 f 为 `if LHE.Dec(sk, node_1) = 1 or LHE.Dec(sk, node_2) = 1 then 1 else 0`。最终根节点 dig 即为加密的析取结果。

> 作用：具体构建了函数绑定哈希函数，明确使用了分层同态加密。安全依赖于同态加密的正确性：若原始输入均使 g 输出 0，则根节点 dig 加密了 0；任何对某个叶子打开为 x_j' 且 g(x_j')=1，回算根节点将得到 1，但统计绑定的 Merkle树节点值已固定为 0，故无法打开。

**[灵活广播加密构造]**
- $\mathsf{Setup}(1^\lambda, n)$: 输出 $\mathsf{pp} = (\mathsf{pk}_{\mathsf{PKE}}, \mathsf{hk})$。
- $\mathsf{KeyGen}(\mathsf{pp})$: $r \leftarrow \{0,1\}^\lambda$, $\mathsf{pk} = \mathsf{PKE.Enc}(\mathsf{pk}_{\mathsf{PKE}}, 1; r)$, $\mathsf{sk}=r$。
- $\mathsf{Enc}(\mathsf{pp}, m, (\mathsf{pk}_1,...,\mathsf{pk}_k))$: $\mathsf{dig} = \mathsf{FBH.Hash}(\mathsf{hk}, (\mathsf{pk}_1,...,\mathsf{pk}_k))$, 输出 $\mathsf{ct} = \mathsf{WE.Enc}(1^\lambda, m, (\mathsf{hk}, \mathsf{pk}_{\mathsf{PKE}}, \mathsf{dig}))$。
- $\mathsf{Dec}(\mathsf{pp}, \mathsf{ct}, (j, \mathsf{sk}_j), (\mathsf{pk}_1,...,\mathsf{pk}_k))$: 计算 $\mathsf{dig}$ 和 $\pi = \mathsf{FBH.ProveOpen}(\mathsf{hk}, (\mathsf{pk}_1,...,\mathsf{pk}_k), \{j\})$，输出 $\mathsf{WE.Dec}(1^\lambda, \mathsf{ct}, (j, \mathsf{pk}_j, \mathsf{sk}_j, \pi))$。

> 作用：展示了灵活广播加密的完整算法流程，明确将公钥定义为加密1的密文，密文为见证加密，解密需提供哈希打开。

### 实验结果
本文为理论构造性论文，未包含实验评估。所有分析均为复杂性理论分析，核心优势在于避免了极重的 i O 原语，转而依赖较弱的见证加密（基于 evasive LWE [54,55] 或其它假设）和基于同态加密的函数绑定哈希。据论文分析，其构造的复杂度为多项式级，且参数（如密文大小、密钥大小）随用户数量的增长呈 polylog(n)。与基于 i O 的方案相比，其潜在效率优势在于底层原语更简单，且可通过近期网格假设的进展实现具体实例化。由于未实验，无法估算具体常数因子和实际运行时间。未来的工作要求基于 [54,55] 的具体参数进行实现。

### 局限性与开放问题
本文方案满足选择性安全性（敌手需预承诺挑战目标），虽指出可通过随机谕言模型提升至自适应安全，但未能在标准模型下完全解决自适应安全问题。注册 ABE 方案在选择性安全下满足无腐败查询，需借助随机谕言模型支持腐败查询，尚未实现完全的适应性安全（如 [46] 中的强安全模型）。函数绑定哈希目前只构造了析取函数类，对于更复杂函数类（如任意多项式电路）的通用构造仍是开放问题。

### 强关联论文

[13] Boneh, D., Zhandry, M. multiparty key exchange, efficient traitor tracing, and more from indistinguishability obfuscation. **CRYPTO 2014**

[46] Hohenberger, S., Lu, G., Waters, B., Wu, D.J. Registered attribute-based encryption. **EUROCRYPT 2023**

[47] Hubáček, P., Wichs, D. On the communication complexity of secure function evaluation with long output. **ITCS 2015**

[32] Garg, S., Gentry, C., Sahai, A., Waters, B. Witness encryption and its applications. **STOC 2013**

[36] Gentry, C., Lewko, A., Waters, B. Witness encryption from instance independent assumptions. **CRYPTO 2014**

[54] Tsabary, R. Candidate witness encryption from lattice techniques. **CRYPTO 2022**

[55] Vaikuntanathan, V., Wee, H., Wichs, D. Witness encryption and null-IO from evasive LWE. **ASIACRYPT 2022**

[38] Gentry, C., Waters, B. Adaptive security in broadcast encryption systems (with short ciphertexts). **EUROCRYPT 2009**

[12] Boneh, D., Waters, B., Zhandry, M. Low overhead broadcast encryption from multilinear maps. **CRYPTO 2014**

[31] Garg, S., Gentry, C., Halevi, S., Raykova, M., Sahai, A., Waters, B. Candidate indistinguishability obfuscation and functional encryption for all circuits. **FOCS 2013**


## 关键词

+ 密码学
+ 零知识
+ 协议