---
title: "Non-interactive zero-knowledge proof of knowledge and chosen ciphertext attack"
标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 1991
created: 2025-04-23 09:18:01
modified: 2025-04-23 11:46:50
---

## Non-interactive zero-knowledge proof of knowledge and chosen ciphertext attack

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/3-540-46766-1_35)

## 作者

+ Charles Rackoff 
+ Daniel R Simon 

## 笔记

### 背景与动机
在现代密码学中，核心目标之一是形式化并解决多方在不安全通信环境下的安全通信问题。一种强安全性需求是抵抗选择密文攻击，其中攻击者可以在获得目标密文前后，请求解密任意挑选的密文。Galil, Haber 和 Yung [GHY] 利用交互式零知识证明构造了抵抗此类攻击的公钥密码系统，但该方法需要交互。将交互去除面临两个紧密相关的问题：首先，非交互地证明知识在直觉上不清晰，因为接收者可能将证明转发给他人；其次，攻击者可以通过回放攻击，将被攻击的密文包含在解密请求中。Naor 和 Yung [NY] 提出的午餐时间攻击模型回避了回放问题，但限制攻击者只能在收到目标密文前获得解密结果，这不符合现实场景。本文旨在填补这一空白：在更现实且更强的攻击模型下，构造一个非交互的、抵抗选择密文攻击的公钥密码系统，其核心思想是让每个发送者拥有一个与公开标识相关联的秘密，并利用非交互零知识知识证明来确保每个合法加密的发送者确实知道其解密结果。

### 相关工作

[BFM] Blum, Feldman, and Micali. Non-Interactive Zero Knowledge and its Applications. **STOC 1988** [Google Scholar](https://scholar.google.com/scholar?q=Non-Interactive+Zero+Knowledge+and+its+Applications)
> 核心思路：首次定义了非交互式零知识证明系统，并给出了其应用。
> 局限与区别：该工作定义了基本概念，本文则在其基础上定义了更复杂的非交互零知识知识证明，并将其应用于抵抗选择密文攻击的密码系统构造。

[FFS] Feige, Fiat, and Shamir. Zero Knowledge Proofs of Identity. **STOC 1987** [Google Scholar](https://scholar.google.com/scholar?q=Zero+Knowledge+Proofs+of+Identity)
> 核心思路：定义了交互式零知识知识证明，要求能够从访问证明者图灵机中恢复出知识。
> 局限与区别：本文所定义的交互式模型过于复杂，且需要交互；本文引入的非交互版本在更丰富的设置下更简单，并规避了交互要求。

[GHY] Galil, Haber, and Yung. Symmetric Public-Key Cryptosystems. **J. Cryptology submitted** [Google Scholar](https://scholar.google.com/scholar?q=Symmetric+Public-Key+Cryptosystems)
> 核心思路：使用交互式零知识知识证明构造抵抗选择密文攻击的公钥密码系统。
> 局限与区别：该方案需要交互，而本文的目标是在非交互环境下实现同样的安全性，并为此引入了新的模型定义。

[NY] Naor and Yung. Public-Key Cryptosystems Provably Secure Against Chosen Ciphertext Attacks. **STOC 1990** [Google Scholar](https://scholar.google.com/scholar?q=Public-Key+Cryptosystems+Provably+Secure+Against+Chosen+Ciphertext+Attacks)
> 核心思路：提出抵抗午餐时间攻击（一种较弱的选择密文攻击）的方案，利用双重加密和非交互零知识证明。
> 局限与区别：该攻击模型限制攻击者只能在获得目标密文前解密，不如本文考虑的、允许攻击者在获得目标密文后继续解密的模型强。本文在此基础上，通过引入发送者秘密的概念，抵御了回放攻击。

[FLS] Feige, Lapidot, and Shamir. Multiple Non-Interactive Zero-Knowledge Proofs Based on a Single Random String. **FOCS 1990** [Google Scholar](https://scholar.google.com/scholar?q=Multiple+Non-Interactive+Zero-Knowledge+Proofs+Based+on+a+Single+Random+String)
> 核心思路：给出了基于单向陷门函数假设构造的非交互式零知识证明系统，可用于任何NP语言。
> 局限与区别：本文直接将其作为基础工具，用以构造更高级的非交互零知识知识证明。

[GM] Goldwasser and Micali. Probabilistic Encryption. **JCSS 1984** [Google Scholar](https://scholar.google.com/scholar?q=Probabilistic+Encryption)
> 核心思路：定义了公钥密码系统的安全性（抵御选择明文攻击），并给出了基于陷门函数的构造。
> 局限与区别：本文的基础安全定义（单一加密攻击）沿用此处的定义，并在此基础之上增强以抵御选择密文攻击。

[DDN] Dolev, Dwork, and Naor. Non-Malleable Cryptography. **STOC 1991** [Google Scholar](https://scholar.google.com/scholar?q=Non-Malleable+Cryptography)
> 核心思路：独立提出了一个更复杂的密码系统，能抵抗更强的、允许攻击者查询任何非目标密文的攻击（无需秘密信息）。
> 局限与区别：本文提出了另一种方案来解决类似的攻击（消息限制的选择密文攻击），通过引入数字签名来增强安全性，而[DDN]的方案不依赖发送者拥有秘密。

### 核心技术与方案
本文的核心技术在于利用非交互零知识知识证明，将一个基础的安全公钥密码系统提升为能抵抗选择密文攻击的系统。方案分三个层次，逐步增强安全模型。

首先，论文定义了一个新的模型，其中每个用户由可信中心分配一个密钥对 $(s^u, p^u)$，且所有用户能识别合法公钥。消息的“假定发送者”由其公钥标识。在此模型下，选择密文攻击有两种定义方式。**攻击者特定选择密文攻击**（定义2.3）中，攻击者只能请求解密以自己为假定发送者的密文。**消息限制选择密文攻击**（定义2.4）中，攻击者可请求解密任何密文，唯一例外是攻击的目标密文本身，这种更强的攻击防止了回放。

为基础构造，论文定义并构造了**非交互零知识知识证明**（定义3.2）。核心思路是：证明者用自己的公钥 $p$ 加密一个语言成员资格的证据 $w$，并附加一个非交互零知识证明，表明加密的内容确实是证据。由于解密需要证明者的私钥 $s$，而如果验证者通过证明，则必然存在一个知识提取者 $F$，它能在给定 $(s, p)$ 的情况下，从证明中恢复出证据 $w$。这利用了 $M_C$ 生成的 $(s, p)$ 分布。

基于此，**定理4.2** 构造了抵抗攻击者特定选择密文攻击的密码系统 $(N_C, N_E, N_D)$。加密过程为：发送方 $u$ 使用基础密码系统 $M_E$ 加密比特 $b$ 得到 $e$，然后利用 $(s^u, p^u)$ 和随机串 $r^u$（作为公共参考串），构造一个非交互零知识知识证明 $\pi$，表明自己知道 $e$ 的解密。解密时，接收方先验证 $\pi$，若有效则解密。安全性证明通过归约进行：若存在攻击者 $A$ 能攻破新系统，则可构造一个算法 $B$ 攻破基础系统 $M_E$。$B$ 模拟新系统，当 $A$ 请求解密以他人为发送者的密文时，$B$ 利用自己的知识提取器 $F$ 获取解密证据（如随机数），从而有效回答；当 $A$ 自身为发送者时，$B$ 直接用自己的密钥 $s^A$ 解密。模拟的证明由 $B$ 通过模拟器生成，与真实证明不可区分。**通信量与计算复杂度**：相比基础系统，新增了一系列零知识证明，其大小与安全参数的多项式相关。

**定理4.3** 进一步构造了抵抗消息限制选择密文攻击的方案，重点在于防范回放和冒充。方案在公钥中增加一个数字签名密钥对 $(\hat{s}^u, \hat{p}^u)$。加密时，发送者对 $(e, \pi)$ 进行数字签名。解密时，需同时验证 $\pi$ 和签名。安全性证明增加了对数字签名方案安全性的归约：攻击者若想生成一个非目标密文（以他人身份）并成功欺骗，必须伪造签名，这被签名方案的安全性所保证。

### 核心公式与流程

**攻击者特定选择密文攻击安全的加密方案 (定理4.2)**

- **密钥生成 $N_C$**：
  $$ (s^u, p^u) \leftarrow M_C(1^n) $$
  $$ \text{公钥}: (p^u, r^u) \quad \text{私钥}: s^u $$
  其中 $r^u$ 是用于零知识证明的随机串。

- **加密 $N_E$**：
  $$ e \leftarrow M_E(s^u, p^u, p^v, b) $$
  $$ \pi \leftarrow P((s^u, (p^u, r^u)), \text{statement: } \exists w \text{ s.t. } M_E(s^u, p^u, p^v, w)=e) $$
  > 作用：生成基础加密密文 $e$，并附带一个非交互零知识知识证明 $\pi$，证明发送者知道 $e$ 对应的明文（或解密所需的随机数）。

  **输出**: $(e, \pi)$

- **解密 $N_D$**：
  $$ \text{若 } V((p^u, r^u), \text{statement}, \pi) = \text{accept}, \text{ 则输出 } M_D(s^v, p^v, p^u, e) $$
  $$ \text{否则输出 } “?” $$
  > 作用：首先验证知识证明，只有通过验证才进行基础解密。

**消息限制选择密文攻击安全的加密方案 (定理4.3)**

- **密钥生成 $N_C$**：
  $$ (s^u, p^u) \leftarrow M_C(1^n) $$
  $$ (\hat{s}^u, \hat{p}^u) \leftarrow \text{KeyGen}_{\text{sig}}(1^n) $$
  $$ \text{公钥}: (p^u, \hat{p}^u, r^u) \quad \text{私钥}: (s^u, \hat{s}^u) $$
  > 作用：额外生成一个用于数字签名的密钥对。

- **加密 $N_E$**：
  $$ (e, \pi) \leftarrow \text{Encrypt}_{\text{thm4.2}}((s^u, \hat{s}^u), (p^u, \hat{p}^u, r^u), (p^v, \hat{p}^v, r^v), b) $$
  $$ \sigma \leftarrow \text{Sign}(\hat{s}^u, (e, \pi)) $$
  > 作用：对密文和证明的元组进行数字签名。

  **输出**: $(e, \pi, \sigma)$

- **解密 $N_D$**：
  $$ \text{若 } \text{Verify}(\hat{p}^u, (e, \pi), \sigma) = \text{accept} \text{ 且 } V(\ldots, \pi) = \text{accept} $$
  $$ \text{则输出 } M_D(s^v, p^v, p^u, e) $$
  $$ \text{否则输出 } “?” $$
  > 作用：同时验证数字签名和知识证明，确保消息未经篡改且有合法发送者。

### 实验结果
本论文是一篇理论性构造和安全性证明，不包含任何实验评估。核心结论是理论上的，依赖于底层密码原语的安全性假设（如存在陷门函数），并证明了所构造的系统在定义的安全模型下是安全的。

### 局限性与开放问题
本文提出的模型依赖于“假定发送者”的概念，需要一个可信中心来分配和管理公钥，并在公钥中嵌入随机串。进一步需要发展安全性的严格定义，考虑通信量分析，并研究对消息施加时间性约束的必要任务。

### 强关联论文

[BFM] Blum, Feldman, and Micali. Non-Interactive Zero Knowledge and its Applications. **STOC 1988** [Google Scholar](https://scholar.google.com/scholar?q=Non-Interactive+Zero+Knowledge+and+its+Applications)

[FFS] Feige, Fiat, and Shamir. Zero Knowledge Proofs of Identity. **STOC 1987** [Google Scholar](https://scholar.google.com/scholar?q=Zero+Knowledge+Proofs+of+Identity)

[GHY] Galil, Haber, and Yung. Symmetric Public-Key Cryptosystems. **J. Cryptology submitted** [Google Scholar](https://scholar.google.com/scholar?q=Symmetric+Public-Key+Cryptosystems)

[NY] Naor and Yung. Public-Key Cryptosystems Provably Secure Against Chosen Ciphertext Attacks. **STOC 1990** [Google Scholar](https://scholar.google.com/scholar?q=Public-Key+Cryptosystems+Provably+Secure+Against+Chosen+Ciphertext+Attacks)

[FLS] Feige, Lapidot, and Shamir. Multiple Non-Interactive Zero-Knowledge Proofs Based on a Single Random String. **FOCS 1990** [Google Scholar](https://scholar.google.com/scholar?q=Multiple+Non-Interactive+Zero-Knowledge+Proofs+Based+on+a+Single+Random+String)

[GM] Goldwasser and Micali. Probabilistic Encryption. **JCSS 1984** [Google Scholar](https://scholar.google.com/scholar?q=Probabilistic+Encryption)

[DDN] Dolev, Dwork, and Naor. Non-Malleable Cryptography. **STOC 1991** [Google Scholar](https://scholar.google.com/scholar?q=Non-Malleable+Cryptography)


## 关键词

+ 非交互式零知识证明
+ 知识证明
+ 选择密文攻击
+ 公钥密码系统
+ CCA安全性

