---
title: "Identity escrow"
doi: 10.1007/bfb0055727
标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 1998
created: 2025-05-26 04:57:24
modified: 2025-05-26 04:58:13
---
## Identity escrow

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/BFb0055727)

## 作者

+ Joe Kilian
+ Erez Petrank

## 笔记

### 背景与动机
在传统的访问控制中，用户要么完全暴露身份，要么完全匿名，这种刚性设计导致隐私与可追责性难以兼得。例如，高速公路自动收费系统若要求每次通行都记录身份，则会大规模追踪用户行踪；若允许完全匿名，则在发生重大事故（如谋杀）时无法追查责任人。本文将密钥托管的思想引入认证领域，提出身份托管（Identity Escrow）概念：用户向验证者提供足以让授权第三方（托管机构）在必要时恢复其身份的信息，同时验证者得到保证该信息确实可被恢复。该方案在正常工作时不泄露身份，仅在特殊情况下由托管机构介入，从而同时保障日常隐私和紧急可追责性。与通信密钥托管不同，身份托管能增强隐私，且用户和验证者都有动机遵循协议——用户获得隐私保障，验证者获得事后追查能力。现有群签名方案[12]虽具备托管特性，但管理者同时扮演发行者和托管者的角色，无法实现完全分离。本文旨在设计多种实现方案，探索不同特性集（尤其是分离性——托管机构在系统初始化及日常运行中完全不用参与）之间的权衡。

### 相关工作

[12] Chaum, van Heyst. Group Signatures. **EUROCRYPT 1991** [Google Scholar](https://scholar.google.com/scholar?q=Group+Signatures)
> 核心思路：首次提出群签名概念，群内成员可代表群匿名签名，群管理者可揭露签名者身份。
> 局限与区别：群管理者同时担任发行者和托管者，无法将这两个角色分离，不能直接用于实现分离的身份托管。

[11] Camenisch, Stadler. Efficient Group Signature Schemes for Large Groups. **CRYPTO 1997** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+Group+Signature+Schemes+for+Large+Groups)
> 核心思路：提出高效的群签名方案，基于RSA和ElGamal加密，允许将群管理者部分角色分离。
> 局限与区别：该方案可实现弱分离（托管者不参与日常交易），但初始化时仍需托管者参与；本文将其直接改造为身份托管系统，并进一步探索完全分离的方案。

[20] Kilian, Petrank. Identity Escrow. **Theory of Cryptography Library 1997** [Google Scholar](https://scholar.google.com/scholar?q=Identity+Escrow)
> 核心思路：本文的早期版本，使用切割-选择零知识证明实现身份托管。
> 局限与区别：该版本效率较低；当前版本基于群签名方案大幅提升了效率。

[16] El Gamal. A Public Key Cryptosystem and a Signature Scheme Based on Discrete Logarithms. **CRYPTO 1985** [Google Scholar](https://scholar.google.com/scholar?q=A+Public+Key+Cryptosystem+and+a+Signature+Scheme+Based+on+Discrete+Logarithms)
> 核心思路：提出ElGamal加密和签名方案，基于离散对数问题。
> 局限与区别：本文在第五部分基于ElGamal构造身份托管方案，证明所依赖假设并非唯一。

[17] Frankel, Tsiounis, Yung. "Indirect Discourse Proofs": Achieving Efficient Fair Off-Line E-Cash. **ASIACRYPT 1996** [Google Scholar](https://scholar.google.com/scholar?q=%22Indirect+Discourse+Proofs%22%3A+Achieving+Efficient+Fair+Off-Line+E-Cash)
> 核心思路：提出高效的“间接话语证明”，用于加密值的性质证明。
> 局限与区别：这类证明不完全适用于身份托管场景，但提示了更高效方案的可能性。

[33] Young, Yung. Auto-Recoverable Auto-Certifiable Cryptosystems. **EUROCRYPT 1998** [Google Scholar](https://scholar.google.com/scholar?q=Auto-Recoverable+Auto-Certifiable+Cryptosystems)
> 核心思路：利用休眠托管代理实现密钥托管。
> 局限与区别：针对密钥托管而非身份认证；本文将其“休眠”思想引入身份托管，实现分离性。

[1] Asokan, Shoup, Waidner. Optimistic Fair Exchange of Digital Signatures. **IBM Research Report 1997** [Google Scholar](https://scholar.google.com/scholar?q=Optimistic+Fair+Exchange+of+Digital+Signatures)
> 核心思路：使用休眠第三方实现数字签名的公平交换。
> 局限与区别：应用场景不同；本文借鉴休眠代理的思想实现身份托管中的分离性。

[5] Brickell, Gemmel, Kravitz. Trustee-based tracing extensions to anonymous cash and the making of anonymous change. **SODA 1995** [Google Scholar](https://scholar.google.com/scholar?q=Trustee-based+tracing+extensions+to+anonymous+cash+and+the+making+of+anonymous+change)
> 核心思路：在电子现金系统中使用休眠托管代理追踪用户。
> 局限与区别：针对电子现金而非身份认证；本文采用类似思想但针对身份托管。

[32] Stadler, Piveteau, Camenisch. Fair blind signatures. **EUROCRYPT 1995** [Google Scholar](https://scholar.google.com/scholar?q=Fair+blind+signatures)
> 核心思路：提出公平盲签名，允许托管者撤销盲签名的匿名性。
> 局限与区别：针对盲签名；本文将其思想扩展到通用身份托管。

### 核心技术与方案

整个身份托管系统包含四个角色：标识者（用户）、发行者（颁发证书）、验证者（服务提供者）和托管代理（必要时恢复身份）。系统需要满足以下特性：第一层身份有效（合法用户总能通过验证）、第二层身份安全（验证者不能伪造身份）、第二层身份保证托管（托管代理能恢复身份）、抗冒充（即使托管代理也不能伪造用户身份）、分离性（托管代理在初始化及日常运行中不参与）。本文提出了三类核心方案。

**基于群签名的方案（第三节）**：
Camenisch-Stadler的群签名方案[11]通过将群管理者拆分为发行者和托管代理实现弱分离。初始化时，发行者生成RSA模数 \(n = pq\) 和指数 \(e_1, e_2\)；托管代理选择循环群 \(G = \langle g \rangle\)，阶为 \(n\)，元素 \(h \in G\)，以及ElGamal密钥对 \((\rho, y_R = h^\rho)\)。用户随机生成私钥 \(x\)，计算 \(y = x^{e_1}\) 和 \(z = g^y\)，并将 \(z\) 发给发行者注册。签名时，用户发送 \( (y_R^r, h^r g^y) \)（即 \(z\) 的ElGamal加密）以证明其证书。托管代理可解密得 \(z\)，再与发行者协作查找用户身份。该方案实现了第一层身份有效、第二层身份安全、抗冒充，但分离性弱——发行者和托管代理需在初始化时通信，且恢复身份时需双方协作。发行者需保存 \(z\) 到用户身份的映射。

**基于RSA的完全分离方案（第四节）**：
该方案实现分离性：任意持有公钥的第三方都可被指定为托管代理，无需其事先参与。核心是使用RSA证书：发行者选择 \(n = pq\) 和指数 \(e\)，发布一个参数 \(\delta\)。有效证书是满足 \(a^e - b^e = \delta \pmod{n}\) 的数对 \((a,b)\)，其中 \(a^e\) 编码用户身份。标识者将 \(a^e\)（通过概率加密）托管到代理的公钥下。验证时，标识者拆分为 \(a_1, a_2\)（乘法拆分），\(b_1, b_2\)（加法拆分），并引入随机化因子 \(x, y\)，通过切割-选择协议证明他知道一个有效证书。具体而言，标识者提交大量承诺，包括对 \(a_1, a_2, b_1, b_2, (a_1)^e, (a_2)^e, (b_1)^e, (b_2)^e, x, x(a_1)^e, x(b_1)^e, x(a_1 a_2)^e + y, x(b_1 b_2)^e + y\) 等。验证者随机选择5个测试之一，检查承诺间的关系（如乘法一致性、和差关系）。标识者能通过所有测试当且仅当 \((a_1 a_2)^e - (b_1 b_2)^e = \delta\)。错误概率为1/5，重复 \(O(\log(1/\epsilon))\) 次可降至 \(\epsilon\)。托管代理从加密中恢复 \((a_1)^e\) 和 \((a_2)^e\) 从而得到 \(a^e\)，直接获得身份（无需发行者）。该方案完全分离，但发行者可冒充用户（因为他知道所有证书）。文章在4.3节提到可通过让 \(a\) 为 \(g^r\) 且证明离散对数知识，并添加额外证书来抵抗冒充。

**基于ElGamal的方案（第五节）**：
此方案使用ElGamal签名/加密，效率更低但所依赖假设不同。有效证书是数对 \((a,b)\) 满足 \(P^a a^b = g \pmod{p}\)（即对消息“1”的签名）。标识者将 \(a\) 用代理公钥加密为 \((\alpha, \beta) = (g^R, Y^R \cdot a)\)。然后通过复杂的切割-选择协议（含34个基本测试）证明他知道一个有效证书且 \(a\) 被正确加密。认证过程涉及对 \(a_1, a_2\) 的乘法拆分（模 \(pq\)）、对 \(b, R\) 的加法拆分，并验证多个乘积关系。托管代理解密得 \(a\)，再与发行者协作确定用户身份。该方案只有弱分离性（托管者需参与初始化），且抗冒充性弱（发行者可以冒充）。

**安全性论证**：所有安全性论证都是启发式的（heuristic），基于非标准假设。例如，RSA方案假设找到满足 \(a^e - b^e = \delta\) 的新对是困难的；已知一对后产生另一对也是困难的。ElGamal方案假设从给定签名中无法伪造新签名（除了“0”文档的弱点已避免）。零知识性通过承诺和切割-选择保证，且每个测试的视图可被模拟。

**复杂度**：群签名方案效率最高，通信量与群签名一致（常数轮，多项式规模）。RSA方案需要多次切割-选择迭代，每轮需要发送大量承诺，通信量约为 \(O(\log(1/\epsilon))\) 乘以承诺个数（约10-20个承诺和打开）。ElGamal方案更复杂，需要34个基本测试，通信开销更大。

### 核心公式与流程

**[RSA证书定义]**  
$$a^e - b^e \equiv \delta \pmod{n}$$
> 作用：定义有效证书对 \((a,b)\)，其中 \(a^e\) 编码用户身份，\(\delta\) 为公开参数。

**[一阶段验证测试5——核心等式]**  
$$(x (a_1 a_2)^e + y) - (x (b_1 b_2)^e + y) = \delta x$$
> 作用：该等式相当于检查 \( (a_1 a_2)^e - (b_1 b_2)^e = \delta \)，由于 \(x\) 与 \(n\) 互质，可约去 \(x\)。这是切割-选择协议中的第五个测试，直接验证证书有效。

**[群签名方案中的托管加密]**  
$$(y_R^r, h^r g^y)$$
> 作用：这是用户发送的ElGamal加密，其中 \(z = g^y\) 为标识符的托管值。托管代理用私钥 \(\rho\) 解密得 \(h^r\) 的逆元，然后恢复 \(g^y\)。

**[ElGamal证书验证中核心乘法等式]**  
$$P^{a_1 a_2} \cdot (a_1)^{b_1} \cdot (a_2)^{b_1} \cdot (a_1)^{b_2} \cdot (a_2)^{b_2} = g$$
> 作用：该等式等价于 \(P^{a} a^{b} = g\)，即证书验证等式。通过拆分 \(a = a_1 a_2\), \(b = b_1 + b_2\)，将大指数运算转为多个双变量指数乘积。

**[ElGamal加密方案中加密公式]**  
$$E_Y(M, r) = (g^r, M Y^r)$$
> 作用：用于托管标识符的 \(a\) 值。在弱身份验证阶段，用户发送加密后的 \((\alpha, \beta)\)。

### 实验结果

本文是纯粹的理论性论文，没有提供任何实验实现或性能测试。所有方案均以抽象协议的形式给出，未涉及具体参数选择、运行时间或通信开销的测量。作者对效率的评价仅停留在定性比较：群签名方案“高效”，RSA方案“大大低于群签名方案但远高于通用零知识证明”，ElGamal方案“比RSA方案更低效”。因此，无法提供实验数据或基准对比。

### 局限性与开放问题

所有方案的安全性论证均为启发式，缺乏基于标准困难假设（如RSA假设、离散对数假设）的严格归约。基于RSA的完全分离方案存在发行者可冒充用户的弱点，虽然文中提出增强方案（利用离散对数和多个证书），但尚未完成详细描述。群签名方案中的弱分离性要求发行者和托管代理在初始化时通信，未能实现“完全休眠”的托管代理。基于ElGamal的方案则缺乏分离性且效率极低。开放问题包括：设计基于标准假设的高效身份托管方案；实现完全分离且抗冒充的实用系统；将托管机制扩展到支持多个托管代理或门限恢复。

### 强关联论文

[11] J. Camenisch, M. Stadler. Efficient Group Signature Schemes for Large Groups. **CRYPTO 1997** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+Group+Signature+Schemes+for+Large+Groups)

[12] D. Chaum, E. van Heyst. Group Signatures. **EUROCRYPT 1991** [Google Scholar](https://scholar.google.com/scholar?q=Group+Signatures)

[16] T. El Gamal. A Public Key Cryptosystem and a Signature Scheme Based on Discrete Logarithms. **CRYPTO 1985** [Google Scholar](https://scholar.google.com/scholar?q=A+Public+Key+Cryptosystem+and+a+Signature+Scheme+Based+on+Discrete+Logarithms)

[20] J. Kilian, E. Petrank. Identity Escrow. **Theory of Cryptography Library 1997** [Google Scholar](https://scholar.google.com/scholar?q=Identity+Escrow)

[17] Y. Frankel, Y. Tsiounis, M. Yung. "Indirect Discourse Proofs": Achieving Efficient Fair Off-Line E-Cash. **ASIACRYPT 1996** [Google Scholar](https://scholar.google.com/scholar?q=%22Indirect+Discourse+Proofs%22%3A+Achieving+Efficient+Fair+Off-Line+E-Cash)

[33] Adam Young, Moti Yung. Auto-Recoverable Auto-Certifiable Cryptosystems. **EUROCRYPT 1998** [Google Scholar](https://scholar.google.com/scholar?q=Auto-Recoverable+Auto-Certifiable+Cryptosystems)

[1] Asokan, Shoup, Waidner. Optimistic Fair Exchange of Digital Signatures. **IBM Research Report 1997** [Google Scholar](https://scholar.google.com/scholar?q=Optimistic+Fair+Exchange+of+Digital+Signatures)

[5] E. Brickell, P. Gemmel, D. Kravitz. Trustee-based tracing extensions to anonymous cash and the making of anonymous change. **SODA 1995** [Google Scholar](https://scholar.google.com/scholar?q=Trustee-based+tracing+extensions+to+anonymous+cash+and+the+making+of+anonymous+change)

[32] M. Stadler, J.-M. Piveteau, J. Camenisch. Fair blind signatures. **EUROCRYPT 1995** [Google Scholar](https://scholar.google.com/scholar?q=Fair+blind+signatures)


## 关键词

+ 身份托管
+ 匿名撤销
+ 群签名
+ 密钥托管
+ 身份验证
