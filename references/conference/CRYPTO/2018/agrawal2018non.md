---
title: "Non-interactive zero-knowledge proofs for composite statements"

标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 2018
modified: 2025-04-14 09:58:24
---

## Non-interactive zero-knowledge proofs for composite statements

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-319-96878-0_22)

## 作者

+ Shashank Agrawal 
+ [Chaya Ganesh](Chaya%20Ganesh.md)
+ [Payman Mohassel](Payman%20Mohassel.md)
## 笔记

好的，作为一名密码学领域的研究助手，我将根据您提供的论文全文，按照指定的格式输出详尽的结构化笔记。

---

### 背景与动机

非交互式零知识证明的两种主流设计——Sigma协议与基于QAP的zk-SNARKs——分别擅长处理代数型语句和算术型语句。Sigma协议对于证明离散对数关系等代数语句极为高效，但在处理哈希函数、分组密码这类非代数运算时，需要将每个门电路表示为代数关系，导致证明开销线性增长，变得不切实际。zk-SNARKs则恰恰相反，它能以恒定大小的证明和快速验证时间来处理算术电路，但其证明者代价和CRS大小均与电路规模成正比，用于证明一个简单的指数运算时，其电路规模可能达到数百万个门，效率极低。在现实应用中，如比特币交易所的偿付能力证明、匿名凭证和加密货币中的zk-SNARKs，常常需要同时证明包含代数运算和哈希运算的复合语句。现有方案要么被迫将整个语句表达为一种形式（如用SNARK证明指数运算），导致性能瓶颈；要么在交互式设置下才能实现。因此，本文旨在填补这一空白，设计一个通用的NIZK框架，能够将代数部分和算术部分的高效证明技术（Sigma协议和zk-SNARKs）以AND、OR和函数组合的方式任意组合，从而在证明大小、证明者开销和CRS大小等维度上探索最优权衡。

### 相关工作

[39] Gennaro等人. Quadratic Span Programs and Succinct NIZKs without PCPs. **EUROCRYPT 2013** [Google Scholar](https://scholar.google.com/scholar?q=Quadratic+Span+Programs+and+Succinct+NIZKs+without+PCPs)
> 核心思路：提出了QAP概念，将电路计算编码为多项式除法的整除关系，是实现高效zk-SNARK的基础。
> 局限与区别：该工作本身不处理复合语句；本文在其基础上，通过修改CRS和证明结构，使其能够承诺输入输出，从而与Sigma协议组合。

[26] Cramer等人. Proofs of Partial Knowledge and Simplified Design of Witness Hiding Protocols. **CRYPTO 1994** [Google Scholar](https://scholar.google.com/scholar?q=Proofs+of+Partial+Knowledge+and+Simplified+Design+of+Witness+Hiding+Protocols)
> 核心思路：提出了Sigma协议的OR组合定理，允许证明两个语句中至少有一个为真，而不泄露是哪一个。
> 局限与区别：该技术局限于Sigma协议本身；本文将其思想扩展到混合Sigma协议和zk-SNARK的复合证明中。

[19] Camenisch和Stadler. Efficient Group Signature Schemes for Large Groups. **CRYPTO 1997** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+Group+Signature+Schemes+for+Large+Groups)
> 核心思路：提出了证明关于离散对数、承诺等代数关系的Sigma协议，是Sigma协议库的经典工作。
> 局限与区别：这些协议无法高效处理非代数关系；本文需要构建新的Sigma协议来处理椭圆曲线点加法和双离散对数等，以适应组合需求。

[57] Parno等人. Pinocchio: Nearly Practical Verifiable Computation. **IEEE S&P 2013** [Google Scholar](https://scholar.google.com/scholar?q=Pinocchio+Nearly+Practical+Verifiable+Computation)
> 核心思路：提出了Pinocchio协议，一个非常实用的QAP-based zk-SNARK实现。
> 局限与区别：本文以其为起点，非黑盒地修改其内部结构，分离输入输出电路的CRS，使得SNARK证明中包含了可用于承诺绑定的多项式求值结果。

[27] Dagher等人. Provisions: Privacy-Preserving Proofs of Solvency for Bitcoin Exchanges. **ACM CCS 2015** [Google Scholar](https://scholar.google.com/scholar?q=Provisions+Privacy+Preserving+Proofs+of+Solvency+for+Bitcoin+Exchanges)
> 核心思路：提出了基于Sigma协议的比特币偿付能力证明系统。
> 局限与区别：该方案只能处理pay-to-pubkey模式，无法处理需要哈希运算（pay-to-hash-address）的比特币地址，因为后者是复合语句；本文的方案解决了这个局限。

[30] Delignat-Lavaud等人. Cinderella: Turning Shabby X.509 Certificates into Elegant Anonymous Credentials with the Magic of Verifiable Computation. **IEEE S&P 2016** [Google Scholar](https://scholar.google.com/scholar?q=Cinderella+Turning+Shabby+X.509+Certificates+into+Elegant+Anonymous+Credentials+with+the+Magic+of+Verifiable+Computation)
> 核心思路：使用zk-SNARK来证明RSA签名验证，以此实现匿名凭证。
> 局限与区别：将整个RSA运算（包括指数运算）表示为电路，导致证明者开销巨大；本文通过组合Sigma协议和zk-SNARK，避免了此开销。

[21] Chase等人. Efficient Zero-Knowledge Proof of Algebraic and Non-Algebraic Statements with Applications to Privacy Preserving Credentials. **CRYPTO 2016** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+Zero+Knowledge+Proof+of+Algebraic+and+Non+Algebraic+Statements+with+Applications+to+Privacy+Preserving+Credentials)
> 核心思路：提出了交互式零知识证明来处理代数与非代数混合语句。
> 局限与区别：该方案是交互式的，且依赖于混淆电路，非交互性弱于本文；本文的目标是实现非交互式证明。

[8] Ben-Sasson等人. Zerocash: Decentralized Anonymous Payments from Bitcoin. **IEEE S&P 2014** [Google Scholar](https://scholar.google.com/scholar?q=Zerocash+Decentralized+Anonymous+Payments+from+Bitcoin)
> 核心思路：使用zk-SNARK构建匿名加密货币，其中证明的语句包含了复杂的哈希运算链。
> 局限与区别：该方案的CRS大小与所有电路函数相关，巨大且不具复用性；本文的方法可通过分段证明来减小CRS大小并提高复用性。

[15] Bünz等人. Bulletproofs: Efficient Range Proofs for Confidential Transactions. **ePrint 2017** [Google Scholar](https://scholar.google.com/scholar?q=Bulletproofs+Efficient+Range+Proofs+for+Confidential+Transactions)
> 核心思路：提出了对数大小的范围证明协议，非常高效。
> 局限与区别：本文未提出新协议，而是将Bulletproofs作为高效的范围证明工具，用于优化其代数部分证明的大小和效率。

[35] Fiore等人. Hash First, Argue Later: Adaptive Verifiable Computations on Outsourced Data. **ACM CCS 2016** [Google Scholar](https://scholar.google.com/scholar?q=Hash+First+Argue+Later+Adaptive+Verifiable+Computations+on+Outsourced+Data)
> 核心思路：利用SNARK证明中的多指数运算作为数据的“哈希”，实现可验证计算。
> 局限与区别：其目标是数据重用；本文的技术思路类似，但目标是使SNARK证明与代数承诺相兼容，以连接不同的证明系统。

### 核心技术与方案

本文的核心贡献是一个通用的框架，用于构造复合语句的NIZK。框架的核心是构建两个基础模块，然后利用它们实现AND、OR和函数组合。

首先是针对**代数语句的基础模块**：实现在承诺输入和输出上的Sigma协议。文章重点解决了一个核心技术难题：如何在椭圆曲线群上证明双离散对数，即给定对私钥$\lambda$的承诺和对点$h = \lambda P$的承诺，证明两者之间的关系。这要求证明一个群元素等于另一个群元素的倍数。文章首先构造了一个底层的点加法证明协议`pointAddition`，它通过代数变换将椭圆曲线的点加公式转化为关于坐标的多项式等式，然后利用Sigma协议证明提交的坐标值满足这些等式。该协议通过在一个更大阶的群$G_2$（其阶$q > 2t^3$）中对坐标进行承诺，并通过范围证明确保算术运算在模$t$而不是模$q$下进行。基于`pointAddition`，文章构造了双离散对数证明协议`ddlog`，证明者通过处理1-bit挑战来逐步证明知识。这些协议构成了代数部分的基础，其安全性由Sigma协议的标准特性（完备性、特殊可靠性、特殊诚实验证者零知识）保证。该部分的安全证明不依赖于q型假设，而是依赖于承诺方案的绑定性和隐藏性，以及Sigma协议的标准性质。

其次是针对**算术语句的基础模块**：实现在承诺输入和输出上的zk-SNARK。文章以Pinocchio [57]协议为模板，通过非黑盒方式修改了CRS和证明结构。具体地，将QAP的电路线索引分为私有输入、公共输入、中间值和输出。在CRS中，对应于私有输入的CRS元素被分离出来。在证明中，对应于私有输入的多项式求值（如$g_v^{v_{com}(s)}$）被作为单独的证明元素输出。然后，文章利用一个`comEq`协议，证明该证明元素与一个独立的Pedersen承诺承诺了相同的值。通过加入随机化因子，协议升级为零知识的`zk-comInSnark`和`zk-comIOSnark`（用于同时承诺输入和输出）。这些协议的安全性依赖于q-PDH、2q-SDH和d-PKE等q型假设以及离散对数假设。其效率与底层SNARK相当，每多一个承诺输入/输出只增加极少量元素。

有了这两个基础模块，文章展示了如何组合它们来构建复合语句。这需要另一个关键组件`Eq`，用于证明不同阶数群中的承诺等价。在此基础上，文章给出了四种函数组合方式（算术-算术，代数-算术，算术-代数，代数-代数）的构造。例如，当外层$f_1$是算术、内层$f_2$是代数时（如证明$H(g^x)$），证明者先对$x$和中间结果$g^x$进行承诺，然后用Sigma协议（`ddlog`）证明$x$和$g^x$的关系，用zk-SNARK证明$g^x$和$h$的关系。当内层$f_1$是代数、外层$f_2$是算术时，则需要将中间结果在两个群中分别承诺，并用`Eq`证明其值相同。OR组合的构造方案也类似，通过在输出比特上做OR来实现对语句的或关系证明。AND组合则直接通过并行运行两个证明即可。所有这些构造的安全性都归结为基础模块的安全性。

### 核心公式与流程

**[QAP定义]**
$$p(x) = \left(v_0(x) + \sum_{k=1}^{m} a_k v_k(x)\right) \cdot \left(w_0(x) + \sum_{k=1}^{m} a_k w_k(x)\right) - \left(y_0(x) + \sum_{k=1}^{m} a_k y_k(x)\right)$$
$$t(x) \mid p(x)$$
> 作用：定义了QAP的计算模型。一个计算是否正确，等价于是否存在中间值的赋值，使得目标多项式$t(x)$整除由三个多项式线性组合构成的多项式$p(x)$。

**[点加法公式转换（用于Sigma协议）]**
$$

L_x(x_1, y_1, x_2, y_2) = x_3 x_2^2 + x_3 x_1^2 + x_1^3 + x_2^3 + 2 y_1 y_2
$$

$$

R_x(x_1, y_1, x_2, y_2) = y_2^2 + y_1^2 + x_1^2 x_2 + x_1 x_2^2 + 2 x_1 x_2 x_3
$$

$$

L_y(x_1, y_1, x_2, y_2) = x_2 y_3 + x_3 y_2 + x_2 y_1
$$

$$

R_y(x_1, y_1, x_2, y_2) = x_1 y_2 + x_3 y_1 + x_1 y_3
$$

> 作用：将椭圆曲线上的点加公式转化为关于坐标的多项式等式，使得可以用Sigma协议证明提交的坐标值满足$T=P+Q$关系，而不需要在原始曲线域$F_t$中进行复杂的域运算证明。

**[双离散对数证明 (ddlog) 核心流程]**
给定对$\lambda$的承诺$C_1=\mathsf{Com}_p(\lambda)$和对$h=\lambda P$的承诺$C_2, C_3=\mathsf{Com}_q(x), \mathsf{Com}_q(y)$:
1.  证明者随机选取$\alpha$，计算$(a_1, a_2, a_3)=(\mathsf{Com}_p(\alpha), \mathsf{Com}_q(\gamma_1), \mathsf{Com}_q(\gamma_2))$，其中$(\gamma_1, \gamma_2) = \alpha P$.
2.  验证者发送挑战比特$c$.
3.  若$c=0$，证明者发送$(\alpha, \beta_1, \beta_2, \beta_3)$；验证者检查承诺是否正确.
4.  若$c=1$，证明者计算$z_1 = \alpha - \lambda$，然后使用`pointAddition`协议证明$T = z_1 P  = (\gamma_1, \gamma_2) - (x, y)$. 验证$(\gamma_1, \gamma_2) = z_1 P + (x, y)$.
> 作用：这是Sigma协议的核心，通过比特挑战，确保证明者知道$\lambda$。它能在椭圆曲线群上证明承诺值与一个点存在倍数关系，这是连接代数证明和算术证明的关键桥梁。

**[zk-comInSnark 协议结构]**
-   **CRS**: 将QAP电路线分为私有输入$I_{com}$、公共输入$I_{pub}$、中间值$I_{mid}$、输出$I_{out}$。对应的多项式求值CRS元素被分别生成。
-   **证明**:
    -   计算标准SNARK证明$\pi$，但将其中对应私有输入的多项式求值结果（如$g_v^{v_{com}(s)}$）作为独立元素。
    -   利用`comEq`协议证明$\pi$中的元素（如$g_v^{v_{com}(s)}$）与Pedersen承诺$C_i$是同一组值的承诺。
-   **验证**: 验证标准SNARK的配对等式（检查$p(s)$被$t(s)$整除），验证“span check”（确保多项式是正确线性组合），验证“same coefficients check”（确保三个多项式使用相同的系数），最后验证`comEq`协议。
> 作用：这是一个通用编译器，将标准zk-SNARK转换为能接收或输出代数承诺的版本，使得它能够与Sigma协议在承诺层面进行交互和组合。

### 实验结果

论文在附录A中给出了对两个应用场景的性能估算，对比了本文方法、纯Sigma协议方案（如Provisions）和纯zk-SNARK方案（如Cinderella）。
在**比特币偿付能力证明**场景中，假设匿名集大小$n=500,000$，客户账户数$c=2,000,000$。Provisions方案的证明大小为$5 \times 10^6$个元素，证明者计算量为$4 \times 10^7$次指数运算，但它只能处理pay-to-pub地址。本文方案的证明大小为$2396n + \log p + \log n$，约为$1.2 \times 10^9$个元素，证明者计算量为$(|H| + 30p + 1800)n + c$次指数运算，约为$1.5 \times 10^{10}$次指数运算（假设曲线域大小$p=256$比特）。作为对比，纯SNARK方案证明大小仅为7个元素，但证明者计算量高达$(|H| + p^3)n + c \approx 1.7 \times 10^{13}$次指数运算。本文方案的证明者工作比纯SNARK方案减少了约500倍，但代价是证明大小大幅增加。
在**隐私保护凭据**场景中，对比了RSA签名验证。Cinderella方案证明大小为7个元素，但证明者需要处理约164,826个方程。本文方案证明大小为$42 + \log p$（约298个元素），证明者计算量为$|H| + \log p + 16$次指数运算。相比Cinderella，证明者工作减少了约87%，但证明大小从7个元素增加到298个。本文还对比了交互式方案[21]，其证明大小为$|H|$，证明者工作为$|m|+|h|$次指数运算加对称密钥操作。本文方案在非交互性上更优。

### 局限性与开放问题

本文的构造证明了可行性，但其代数部分的Sigma协议（如`ddlog`）尺寸较大（约2370个元素），导致在需要大量代数证明的应用中整体证明尺寸依然显著。虽然可以通过运行多次双离散对数协议并将所有元素合并在一个证明中来减少开销，但未来的工作可以尝试寻找更紧凑的代数证明协议。此外，本文的SNARK部分依赖于q型假设，这些假设的强度高于标准假设，且随着电路大小变化，影响了整体安全性。一个开放问题是，是否可以将本文的工作与基于标准假设的SNARK或更高效的承诺方案相结合，同时保持复合语句证明的效率。另一方面，本文的协议都是针对特定群结构的，如何将其推广到更一般的代数结构（如格密码）也是一个有意义的探索方向。最后，文中省略了部分协议（如`Eq`）的细节，完整的证明和实现是未来工作。

### 强关联论文

[39] Gennaro等人. Quadratic Span Programs and Succinct NIZKs without PCPs. **EUROCRYPT 2013** [Google Scholar](https://scholar.google.com/scholar?q=Quadratic+Span+Programs+and+Succinct+NIZKs+without+PCPs)

[26] Cramer等人. Proofs of Partial Knowledge and Simplified Design of Witness Hiding Protocols. **CRYPTO 1994** [Google Scholar](https://scholar.google.com/scholar?q=Proofs+of+Partial+Knowledge+and+Simplified+Design+of+Witness+Hiding+Protocols)

[19] Camenisch和Stadler. Efficient Group Signature Schemes for Large Groups. **CRYPTO 1997** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+Group+Signature+Schemes+for+Large+Groups)

[57] Parno等人. Pinocchio: Nearly Practical Verifiable Computation. **IEEE S&P 2013** [Google Scholar](https://scholar.google.com/scholar?q=Pinocchio+Nearly+Practical+Verifiable+Computation)

[27] Dagher等人. Provisions: Privacy-Preserving Proofs of Solvency for Bitcoin Exchanges. **ACM CCS 2015** [Google Scholar](https://scholar.google.com/scholar?q=Provisions+Privacy+Preserving+Proofs+of+Solvency+for+Bitcoin+Exchanges)

[30] Delignat-Lavaud等人. Cinderella: Turning Shabby X.509 Certificates into Elegant Anonymous Credentials with the Magic of Verifiable Computation. **IEEE S&P 2016** [Google Scholar](https://scholar.google.com/scholar?q=Cinderella+Turning+Shabby+X.509+Certificates+into+Elegant+Anonymous+Credentials+with+the+Magic+of+Verifiable+Computation)

[21] Chase等人. Efficient Zero-Knowledge Proof of Algebraic and Non-Algebraic Statements with Applications to Privacy Preserving Credentials. **CRYPTO 2016** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+Zero+Knowledge+Proof+of+Algebraic+and+Non+Algebraic+Statements+with+Applications+to+Privacy+Preserving+Credentials)

[8] Ben-Sasson等人. Zerocash: Decentralized Anonymous Payments from Bitcoin. **IEEE S&P 2014** [Google Scholar](https://scholar.google.com/scholar?q=Zerocash+Decentralized+Anonymous+Payments+from+Bitcoin)

[15] Bünz等人. Bulletproofs: Efficient Range Proofs for Confidential Transactions. **ePrint 2017** [Google Scholar](https://scholar.google.com/scholar?q=Bulletproofs+Efficient+Range+Proofs+for+Confidential+Transactions)

[35] Fiore等人. Hash First, Argue Later: Adaptive Verifiable Computations on Outsourced Data. **ACM CCS 2016** [Google Scholar](https://scholar.google.com/scholar?q=Hash+First+Argue+Later+Adaptive+Verifiable+Computations+on+Outsourced+Data)


## 关键词

+ 复合语句NIZK非交互零知识
+ Sigma协议QAP-SNARK混合框架
+ 代数算术语句AND-OR组合证明
+ 隐私凭证加密货币审计应用
+ 证明大小证明开销权衡CRS