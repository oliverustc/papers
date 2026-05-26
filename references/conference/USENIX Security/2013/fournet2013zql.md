---
title: "ZQL: A Compiler for Privacy-Preserving Data Processing"
标题简称:
论文类型: conference
会议简称: USENIX Security
发表年份: 2013
---

## ZQL: A Compiler for Privacy-Preserving Data Processing

## 发表信息

+ [原文链接](https://www.usenix.org/conference/usenixsecurity13/technical-sessions/presentation/fournet)

## 作者

+ Cédric Fournet 
+ [Markulf Kohlweiss](Markulf%20Kohlweiss.md) 
+ George Danezis 
+ Zhengqin Luo 


## 笔记

### 背景与动机
现代服务越来越依赖细粒度的用户隐私数据，例如智能电表按用电时段收费、按驾驶里程定价的车险等。传统方案将原始数据全部收集到服务端处理，引发了严重的隐私泄露风险。一种替代思路是让客户端在本地持有由数据源（如电表、车载黑箱）签名的隐私数据，自行执行计算后只上传结果和正确性证明，服务端只需验证证明即可保证结果完整性，同时客户端无需泄露输入数据。然而，手工设计这样的零知识协议需要密码学专家参与，且每次修改计算逻辑都要重新设计，代价高昂。ZQL 提出一种声明式的查询语言，使普通程序员可以用类似 SQL 的形式表达隐私保护计算，编译器自动生成数据源签名、客户端证明和服务端验证的完整代码，同时保证正确性、完整性和隐私性。

### 相关工作

[51] Meiklejohn 等. ZKPDL: A Language-Based System for Efficient Zero-Knowledge Proofs and Electronic Cash. **USENIX Security 2010** [Google Scholar](https://scholar.google.com/scholar?q=ZKPDL%3A+A+Language-Based+System+for+Efficient+Zero-Knowledge+Proofs+and+Electronic+Cash)
> 核心思路：设计自然语言风格的规范语言来指定零知识证明目标，并编译成 Σ-协议。  
> 局限与区别：ZKPDL 主要面向密码协议设计（如电子现金），而 ZQL 专注于一般性的查询计算，并自动处理数据源的签名和证明生成。

[7] Bangerter 等. Automatic Generation of Sigma‑Protocols. **EuroPKI 2009** [Google Scholar](https://scholar.google.com/scholar?q=Automatic+Generation+of+Sigma‑Protocols)
> 核心思路：自动将 Camenisch‑Stadler 表示法描述的证明目标转化为高效 Σ-协议。  
> 局限与区别：CACE 编译器（包括该工作）关注证明逻辑的自动合成，而 ZQL 还包含了完整的查询编译链（数据源、证明者、验证者），并支持表操作和查找。

[2] Almeida 等. Full Proof Cryptography: Verifiable Compilation of Efficient Zero-Knowledge Protocols. **CCS 2012** [Google Scholar](https://scholar.google.com/scholar?q=Full+Proof+Cryptography%3A+Verifiable+Compilation+of+Efficient+Zero-Knowledge+Protocols)
> 核心思路：使用形式化验证技术（如 EasyCrypt）保证编译出的 Σ-协议的正确性和安全性。  
> 局限与区别：该工作侧重于协议安全性的形式化验证，而 ZQL 更强调上层语言设计和对一般查询的支持，安全性通过类型系统和随机预言机模型保证。

[1] Akinyele 等. Charm: A Framework for Rapidly Prototyping Cryptosystems. **Cryptology ePrint 2011** [Google Scholar](https://scholar.google.com/scholar?q=Charm%3A+A+Framework+for+Rapidly+Prototyping+Cryptosystems)
> 核心思路：提供密码学原语库和零知识证明编译器（基于 Camenisch‑Stadler 表示法）。  
> 局限与区别：Charm 的零知识编译器是原型，不如 CACE 和 ZKPDL 成熟，且不提供类似 ZQL 的数据源认证和查询级隐私策略。

[45] Goldberg. Natural Zero-Knowledge Embedding in C++. 个人通讯 2011
> 核心思路：在 C++ 中嵌入零知识证明语言。  
> 局限与区别：该工作未提供完整的编译器或类型系统，ZQL 在高级语言层面隐藏所有密码细节。

[49] Malkhi 等. Fairplay - A Secure Two-Party Computation System. **USENIX Security 2004** [Google Scholar](https://scholar.google.com/scholar?q=Fairplay+-+A+Secure+Two-Party+Computation+System)
> 核心思路：将 Secure Function Evaluation (SFE) 编译为姚氏混淆电路。  
> 局限与区别：ZQL 假设客户端已知所有私密数据，因此可以实现单轮非交互协议，而多方计算需要多轮交互，效率较低且不支持非线性操作（如 join）的高效实现。

[19] Briner. Compiler for Zero-Knowledge Proof-of-Knowledge Protocols. 硕士论文 2004
> 核心思路：早期自动生成 Σ-协议的编译器雏形。  
> 局限与区别：功能有限，未考虑数据源签名和一般查询，ZQL 在此基础上扩展到完整的查询处理系统。

[53] Parno 等. Pinocchio: Nearly Practical Verifiable Computation. **IEEE S&P 2013** [Google Scholar](https://scholar.google.com/scholar?q=Pinocchio%3A+Nearly+Practical+Verifiable+Computation)
> 核心思路：使用 QAP 和配对实现通用的可验证计算（VC）。  
> 局限与区别：Pinocchio 针对任意函数，但需要可信设置，且证明生成成本较高；ZQL 针对特定查询，利用 Σ-协议和 Pedersen 承诺，在受限场景下更高效。

[20] Camenisch 和 Lysyanskaya. A Signature Scheme with Efficient Protocols. **SCN 2002** [Google Scholar](https://scholar.google.com/scholar?q=A+Signature+Scheme+with+Efficient+Protocols)
> 核心思路：提出 CL 签名，支持对已签名消息进行零知识证明。  
> 局限与区别：ZQL 使用 CL 签名作为查找表的基础，但签名方案本身不是编译器对象，而是作为底层工具。

### 核心技术与方案
ZQL 的整体架构如图 1 所示：源查询经编译器生成数据源代码（签名）、证明者代码（客户端）和验证者代码（服务端）。数据源对私密输入进行承诺并签名，证明者使用这些输入执行查询计算，同时为所有私密中间值和结果生成零知识证明，验证者检查证明并输出公开结果。

**语言设计**：ZQL 是一种纯表达式语言，支持整数、表（table）和查找表（lookuptable），以及 map、fold、lookup 等操作。类型系统标记 public/private，通过信息流控制确保私有数据不会隐式泄露，只有显式使用 declassification 操作符 $\downarrow$ 的结果才会被公开。编译器自动推断类型。

**安全定义**：正确性要求诚实参与者协议输出等于源查询结果；隐私性要求任何多项式时间敌手（拥有验证者能力）无法区分产生相同查询结果的两组输入；完整性要求敌手（拥有证明者能力）无法使验证者接受一个无效的结果。隐私是信息论完美的（使用完美隐藏的 Pedersen 承诺），完整性基于随机预言机模型下的离散对数假设和 Strong Diffie-Hellman 假设。

**编译过程**分为三个阶段：
1. **共享翻译**：将源查询扩展为带有承诺、开口和表示方程的中间表达式。对于线性表达式（如 $z = a_0 + \sum a_i x_i$），直接利用 Pedersen 承诺的同态性得到 $C_z = g^{a_0} \prod (C_{x_i})^{a_i}$ 和开口 $o_z = \sum a_i o_{x_i}$。对于非线性乘法 $p = x \cdot y$，添加断言 $1 = C_x^y \cdot g^{-p} \cdot h^{-o'}$，并生成新的承诺 $C_p$。对于查找表，使用 CL 签名证明知识，需要嵌入对签名值盲化的步骤，形成一系列方程（如论文图 5 规则 (9)）。
2. **证明者翻译**：分两遍完成。第一遍，为每个私密变量引入随机数 $t_x$（证明随机数），将共享翻译中的断言转化为哈希扩展：$H \leftarrow \text{extend } H(e_t)$，其中 $e_t$ 是从断言右端替换变量为 $t_x$ 得到的指数表达式。同时将需要传输的承诺和值收集到证据 $a$ 中。第二遍，在计算全局挑战 $c = \text{finalize}(H)$ 后，计算响应 $r_x = t_x - c \cdot x$。最终证明由 $c$、响应和公共值组成。
3. **验证者翻译**：验证者接收证明者传来的公共值、证据和挑战 $c$，逐个处理共享翻译中的断言：对每个断言 $e_P = e_\lambda$，计算 $(e_P)^c \cdot e_r$（其中 $e_r$ 是 $e_\lambda$ 变量替换为响应版本后的表达式），扩展哈希 $H$。最后检查重新计算的挑战是否等于接收的 $c$。若一致则输出公开结果。

**复杂度**（表 1 符号表达式）：以 pay-as-you-go 查询为例（$\ell_{seg}$ 为路段数），证明者的运算包括约 $15E + 40E\cdot\ell_{seg} + 12\ell_{seg}\cdot\hat{e} + 6\hat{e}$（$E$ 为指数运算，$\hat{e}$ 为配对运算），验证者包括 $29E + 35E\cdot\ell_{seg} + 16\ell_{seg}\cdot\hat{e} + 8\hat{e} + \text{sigv}$。证明大小随 $\ell_{seg}$ 线性增长（如 BN254 分支约 28KB 对应 $\ell_{seg}=25$）。这些复杂度主要由每位表中的乘法证明和查找表签名验证决定。

### 核心公式与流程

**[Pedersen 承诺]**
$$C_x = g^x h^{ox},\quad ox \in \mathbb{F}_q \text{ 随机开口}$$
> 作用：对私密整数 $x$ 进行完美隐藏、计算绑定承诺，用于同态证明线性关系。

**[乘法表示方程（共享翻译）]**
对于 $p = x \cdot y$，已知承诺 $C_x = g^x h^{ox}$，则断言：
$$1 = C_x^y \cdot g^{-p} \cdot h^{-o'}$$
其中 $o' = ox \cdot y$ 为开口随机数，该方程等价于 $C_x^y = g^p h^{o'}$，用于 Σ-协议证明。
> 作用：将非线性乘法关系转化为可证明的离散对数表示方程。

**[查找表翻译（核心证明方程）]**
对于查找 $x_0$ 在表 $T$ 中找到行 $(x_0, x_1, \ldots, x_n, e, v, A)$，盲化 $A' = A \cdot h^{-d}$ 后，验证：
$$\hat{e}(Z, \hat{g}) \cdot \hat{e}(1/A', pk_i) = \hat{e}(R_0, \hat{g})^{x_0} \cdots \hat{e}(R_n, \hat{g})^{x_n} \cdot \hat{e}(A', \hat{g})^{e} \cdot \hat{e}(S, \hat{g})^{v} \cdot \hat{e}(h, \hat{g})^{p} \cdot \hat{e}(h, pk_i)^{d}$$
其中 $p = d \cdot e$，$d$ 为盲化随机数。
> 作用：证明证明者知道一个由数据源用 CL 签名签名的元组，且不泄露使用的是哪一行。

**[Σ-协议响应生成（证明者）]**
$$r_x = t_x - c \cdot x \quad (\text{对所有私密变量 } x)$$
挑战 $c = \text{finalize}(H)$，其中 $H$ 由所有公共值和承诺的指数扩展累加得到。
> 作用：使验证者可以通过检查 $\text{finalize}(H') = c$ 来验证证明，其中 $H'$ 由公共值和 $(C_x)^c \cdot g^{r_x} \cdot h^{r_{ox}}$ 等重算。

### 实验结果
实验在三种应用场景（smart meter bill, pay-as-you-go, gps distance）上评估了三个编译器后端（RSA 1024 bits, RSA 2048 bits, BN254 配对曲线）。对于 smart meter bill（读表数 $\ell_{read}=5$），RSA 1024 分支的证明者耗时 586ms，验证者耗时 599ms，证明大小 6,106 字节；BN254 分支证明者 1,374ms，验证者 2,092ms，证明大小 3,773 字节。pay-as-you-go（路段数 $\ell_{seg}=25$）在 RSA 1024 下证明者 5,314ms，验证者 5,111ms，证明大小 57,368 字节；BN254 下证明者 8,305ms，验证者 12,261ms，证明大小 28,819 字节。gps distance（两点间距离）在 BN254 下证明者 841ms，验证者 1,253ms，证明大小 2,751 字节。符号执行后端给出了运算次数与输入规模 $\ell$ 的线性关系（如 pay-as-you-go 验证者需要 $29E + 35E\cdot\ell_{seg} + 16\ell_{seg}\cdot\hat{e} + 8\hat{e} + \text{sigv}$）。C++ 后端验证 pay-as-you-go (RSA 1024) 耗时 4,290ms，而 F# 后端使用原生大整数库耗时 5,111ms，表明主要开销在模指数运算。整体而言，证明大小和运行时对输入规模线性增长，对于典型规模（如 5~25 行）可在秒级完成，适用于实时计费场景。

### 局限性与开放问题
ZQL 的查找表目前必须由外部数据源签名，限制了灵活性；未来可使用累加器或向量承诺实现更灵活的查找。另外，当前编译器仅支持 Σ-协议和 Pedersen 承诺，对于更复杂的语句（如 disjunction）或更高效的证明系统（如 Pinocchio 的 QAP）尚未集成。性能方面，大量指数运算是瓶颈，批处理或多指数技术可加速，但编译器需自动选择最佳编码方案——这是一个开放挑战。语言层面，ZQL 隐藏了所有密码细节，但可能限制高级用户定制编译策略；可考虑提供更高级的 API 以暴露优化选项而不断安全保证。

### 强关联论文

[2] J. B. Almeida, M. Barbosa, E. Bangerter, G. Barthe, S. Krenn, and S. Z. Beguelin. Full proof cryptography: verifiable compilation of efficient zero-knowledge protocols. **CCS 2012**

[7] E. Bangerter, T. Briner, W. Henecka, S. Krenn, A.-R. Sadeghi, and T. Schneider. Automatic generation of sigma-protocols. **EuroPKI 2009**

[19] T. Briner. Compiler for zero-knowledge proof-of-knowledge protocols. **Master thesis, ETH Zurich & IBM Research Lab Zurich, 2004**

[1] J. A. Akinyele, M. D. Green, and A. D. Rubin. Charm: A framework for rapidly prototyping cryptosystems. **Cryptology ePrint Archive, Report 2011/617, 2011**

[51] S. Meiklejohn, C. C. Erway, A. Kupc¸ ¨ u, T. Hinkle, and A. Lysyanskaya. ZKPDL: A language-based system for efficient zero-knowledge proofs and electronic cash. **USENIX Security Symposium 2010**

[20] J. Camenisch and A. Lysyanskaya. A signature scheme with efficient protocols. **SCN 2002**

[45] I. Goldberg. Natural zero-knowledge embedding in c++. **Personal communication, October 2011**

[49] D. Malkhi, N. Nisan, B. Pinkas, and Y. Sella. Fairplay - a secure two-party computation system. **USENIX Security 2004**

[53] B. Parno, C. Gentry, J. Howell, and M. Raykova. Pinocchio: Nearly practical verifiable computation. **IEEE S&P 2013**

[54] T. P. Pedersen. Non-interactive and information-theoretic secure verifiable secret sharing. **CRYPTO 1992**


## 关键词

+ ZQL隐私保护查询语言
+ 零知识协议编译器
+ 私有数据计算认证
+ 查询结果完整性保护
+ 客户端安全计算
+ 隐私保护数据处理

