---
title: "Concurrently secure blind schnorr signatures"
doi: 10.1007/978-3-031-58723-8_5
标题简称:
论文类型: conference
会议简称: EUROCRYPT
发表年份: 2024
---
## Concurrently secure blind schnorr signatures

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-58723-8_5)

## 作者

+ [Georg Fuchsbauer](Georg%20Fuchsbauer.md)
+ Mathias Wolf 


## 笔记

### 背景与动机
盲签名作为Chaum于1982年提出的密码学原语，允许用户从签名者处获取对某个消息的签名，而签名者不知道所签消息的具体内容。该原语在电子现金、电子投票、匿名凭证等隐私保护场景中扮演着核心角色。近年来，随着区块链技术的兴起，盲签名的需求再次凸显，特别是在隐私币、盲币交换等应用中，对生成的签名与现有系统兼容性要求极高。Schnorr签名因其高效性（签名短、验证快）和已被主要区块链系统（如Bitcoin通过Taproot升级）采纳，成为目前最重要的签名方案之一。然而，现有的盲Schnorr签名方案面临一个关键挑战：并发安全性。原始的Chaum-Pedersen盲Schnorr协议存在所谓的“ROS问题”漏洞，攻击者可以通过同时打开多个并发会话高效地伪造签名。尽管后续有方案尝试解决此问题，但要么牺牲了签名标准性（如生成的签名不是标准Schnorr签名），要么依赖于更强的假设（如OMDL、mROS问题）或低效的通用构造（如基于混乱电路）。当前，尚没有一个实用的、能够产生标准Schnorr签名的并发安全盲签名方案，这导致了在标准化工作中的缺位。本文旨在填补这一空白，提出了第一个实用的并发安全盲Schnorr签名方案，并将其推广至更一般的“谓词盲签名”概念。

### 相关工作

[Cha82] Chaum, D. Blind signatures for untraceable payments. **CRYPTO 1982** [Google Scholar](https://scholar.google.com/scholar?q=Blind+signatures+for+untraceable+payments)
> 核心思路：开创性地提出了盲签名的概念，允许用户在消息对签名者保密的情况下获得签名。
> 局限与区别：其原始构造不满足并发安全性，易受ROS攻击。

[CP93] Chaum, D., Pedersen, T. P. Wallet databases with observers. **CRYPTO 1992** [Google Scholar](https://scholar.google.com/scholar?q=Wallet+databases+with+observers)
> 核心思路：提出了原始的三轮盲Schnorr签名协议，这是本文构造的起点。
> 局限与区别：该方案本身不具备并发安全性，已被证明在多会话场景下存在漏洞。

[Sch01] Schnorr, C.P. Security of blind discrete log signatures against interactive attacks. **ICICS 2001** [Google Scholar](https://scholar.google.com/scholar?q=Security+of+blind+discrete+log+signatures+against+interactive+attacks)
> 核心思路：首次形式化定义了盲Schnorr签名的并发安全威胁，引入了ROS问题作为其安全性的核心假设。
> 局限与区别：后续研究显示ROS问题并非如最初设想般困难，存在多项式时间攻击[BLL+21]，使得该假设基础不稳。

[FPS20] Fuchsbauer, G., Plouviez, A., Seurin, Y. Blind schnorr signatures and signed ElGamal encryption in the algebraic group model. **EUROCRYPT 2020** [Google Scholar](https://scholar.google.com/scholar?q=Blind+schnorr+signatures+and+signed+ElGamal+encryption+in+the+algebraic+group+model)
> 核心思路：提出了“子句盲Schnorr”变体，通过并行运行两个签名会话并随机完成一个来规避ROS攻击。
> 局限与区别：该方案的安全性依赖一个新的“modified ROS (mROS)”问题假设，而mROS可被亚指数时间求解，导致标准实例化下安全强度仅约70比特，且签名流程复杂。

[BLL+21] Benhamouda, F., Lepoint, T., Loss, J., Orrù, M., Raykova, M. On the (in)security of ROS. **EUROCRYPT 2021** [Google Scholar](https://scholar.google.com/scholar?q=On+the+%28in%29security+of+ROS)
> 核心思路：给出了ROS问题的多项式时间攻击算法，彻底证明了基于ROS假设的盲Schnorr签名方案在并发设置下是不安全的。
> 局限与区别：该工作指出了现有方案的致命缺陷，但并未构造一个安全的替代方案，而是催生了对新安全方案的需求。

[GRS+11] Garg, S., Rao, V., Sahai, A., Schröder, D., Unruh, D. Round optimal blind signatures. **CRYPTO 2011** [Google Scholar](https://scholar.google.com/scholar?q=Round+optimal+blind+signatures)
> 核心思路：提出了一个轮次最优（1轮）的通用盲签名构造，通过使用混乱电路实现。
> 局限与区别：该方案仅为可行性结果，效率极低（签名大小数百KB，运行时间长达一天），不适用于实际应用，特别是与高效的标准Schnorr签名相比。

[KLX22] Kastner, J., Loss, J., Xu, J. On pairing-free blind signature schemes in the algebraic group model. **PKC 2022** [Google Scholar](https://scholar.google.com/scholar?q=On+pairing-free+blind+signature+schemes+in+the+algebraic+group+model)
> 核心思路：证明了原始的Chaum-Pedersen盲Schnorr方案在仅考虑顺序会话（无并发）时，在AGM+ROM下基于OMDL是安全的。
> 局限与区别：该安全证明不适用于并发场景，因此无法防御如[BLL+21]提出的并发攻击。

### 核心技术与方案

本文提出的并发安全盲Schnorr签名方案是对原始Chaum-Pedersen协议的增强修改，以解决其固有的ROS漏洞。方案的核心思想是在协议中引入一个强制的“承诺-证明”步骤，而非单纯依赖用户发送临时盲化值。

*   **构造思路**：原始协议之所以易受ROS攻击，是因为攻击者（用户）可以在看到签名者的第一条消息R后，再选择盲化因子，从而能在多个会话中进行协同攻击。为阻止此攻击，本文方案要求用户在收到签名者的R之前，先提交一个加密的承诺，承诺的内容包括待签消息m和其将使用的盲化因子α、β。具体地，用户使用一个公钥加密方案PKE生成密文C，并将其作为第一条消息发送给签名者。在收到签名者的R后，用户必须使用一个非交互式零知识证明系统NArg来证明其第二条消息c与先前承诺中的内容是一致的，并且待签消息m满足双方事先约定的谓词prd。签名者仅在验证NArg证明通过后，才会回复最后一个值s，从而让用户计算最终签名。

*   **关键步骤与安全直觉**：方案包含四轮交互。
    1.  用户首先生成盲化因子α, β和随机数ρ，计算对(m, α, β)的PKE加密C，并将C发送给签名者。
    2.  签名者收到C后，选取随机数r，计算R = rG，并将R发送给用户。
    3.  用户收到R后，计算盲化后的群元素R' = R + αG+ βX，计算哈希c = H(R', X, m) + β mod q。然后，用户生成一个NArg证明π，证明如下关系成立：存在一个秘密(m, α, β, ρ)使得c是由这些值正确计算得到的、m满足谓词prd、且C是对(m, α, β, ρ)的正确加密。用户将(c, π)发送给签名者。
    4.  签名者验证π的有效性。如果验证通过，签名者计算s = (r + c*x) mod q并发送给用户。用户再计算s' = (s + α) mod q，最终输出标准Schnorr签名σ = (R', s')。

    对于安全性，方案的安全性依赖于三个核心假设：
    *   **不可伪造性**：证明通过若干游戏跳转规约到Schnorr签名方案本身的sEUF-CMA安全性（假设1）、NArg方案的可靠性（soundness）以及离散对数假设（DL）。关键在于，当攻击者在某次会话中成功欺骗时，可以构造一个针对基础Schnorr签名的伪造者（F）或打破NArg可靠性（S）或解决DL问题（D）。
    *   **盲性**：证明通过游戏跳转规约到NArg的零知识性（ZK）和PKE的CPA安全性。首先，将真实证明替换为模拟证明（利用ZK），然后将加密的明文替换为固定消息（利用CPA）。经过这些替换后，整个协议的信息与原始盲Schnorr协议无法区分，而原始协议的盲性是无条件的，因此最终游戏与挑战比特b无关。
    *   **谓词盲签名推广**：方案自然推广至谓词盲签名。通过修改NArg所证明的关系，将“消息m满足谓词prd”作为一条约束加入证明中。这允许签名者对消息内容施加任意可验证的条件，同时保持用户对该条件之外的其它消息内容的隐私。

*   **复杂度分析**：协议的计算开销主要集中在用户端，需要执行一次PKE加密和一次NArg证明的生成。签名者的主要开销是NArg证明的验证。在最常见的椭圆曲线设置（如secp256k1 + SHA-256）下，选择Groth16等证明系统，证明时间可达分钟级，验证时间在亚秒级。通信开销包括一次加密密文、一个群元素R、一个哈希值c、一个NArg证明和一个标量s。相比原始协议，增加了一个密文C和一个证明π，但总体仍在实用范围内。

### 核心公式与流程

**[关系R_Sch]**
$$
\begin{aligned} \mathsf{R}_{\mathsf{Sch}} &\big( (q, \mathbb{G}, G, \mathsf{H}), (X, R, c, C, prd, ek), (m, \alpha, \beta, \rho) \big): \\
R' &:= R + \alpha G + \beta X \\
\text{return } &c \equiv_q \mathsf{H}(R', X, m) + \beta \\
&\wedge \mathrm{P}(prd, m) = 1 \\
&\wedge \text{PKE.Enc}(ek, (m, \alpha, \beta); \rho) = C
\end{aligned}
$$
> 作用：定义了用户需要证明的陈述。用户须证明已知秘密值m, α, β, ρ，使得：1）c是对哈希值和β的正确盲化；2）消息m满足谓词prd；3）密文C是对(m, α, β)的正确加密。这是NArg证明的底层关系，也是方案安全性的核心关联。

**[派生签名公式]**
$$s'G = sG + \alpha G = (r + c x)G + \alpha G = R + cX + \alpha G = R + \alpha G + \beta X + (\mathsf{H}(R', X, m) + \beta)X - \beta X = R' + \mathsf{H}(R', X, m)X$$
> 作用：验证最终得到的签名(R', s')是满足标准Schnorr验证方程的。通过代数推导，展示了协议的完整流程能正确产生一个有效的标准Schnorr签名。

### 实验结果

本文对方案的性能瓶颈——NArg证明系统——进行了基准测试。实验环境为搭载Intel Core i7-10850H CPU @ 2.70 GHz × 12和31 GB RAM的笔记本电脑。

*   **场景设置**：测试了两种Schnorr参数场景：**场景(A)** 使用对NArg友好的Baby JubJub (BJB)曲线和Poseidon哈希函数；**场景(B)** 使用比特币标准参数secp256k1曲线和SHA-256哈希函数。测试了三种证明系统：Groth16（简称G）、PlonK（简称P）和Spartan（简称S）。Spartan用于场景(B2)（谓词盲签名比特币交易）。
*   **核心性能**：在最优化的场景(A1)中（最大硬编码，全盲，BJB+Poseidon），Groth16的证明时间为0.5秒，证明密钥大小为0.8 MB，验证时间为0.4秒。PlonK的证明时间为1.2秒，密钥大小为0.9 MB，验证时间为12毫秒。在最受关注的场景(B2)（最小硬编码，谓词盲签名，secp256k1+SHA-256）中，Groth16的证明时间约为60秒，证明密钥大小为566 MB；PlonK的证明时间约为2分53秒，密钥大小为354 MB。
*   **Spartan表现**：对于场景(B2)，使用Spartan证明系统时，CRS大小锐减至36 kB，无需可信设置。尽管证明时间仍为2分34秒，但其电路复杂度相比Groth16和PlonK降低了超过7倍（从约170万约束降至22万约束），显示了巨大优化潜力。
*   **对比基线**：作为对比，作者引用了基于混乱电路的通用构造，其运行时间约为一天，数据量达819 GB，证明本文方案在效率上实现了数量级上的优势。作者还指出，当采用与Zcash早期版本类似的计算时间（约2分钟）时，本文方案的证明时间是可以接受的。

### 局限性与开放问题

本文方案的主要局限在于其证明系统的效率，特别是在使用标准非友好型曲线（如secp256k1）和哈希函数（如SHA-256）时，证明生成时间达到了分钟级别，这可能不适用于所有低延迟场景。此外，所有实现均基于原型代码，仍有大量的优化空间，包括并行化、针对特定曲线的算法优化以及采用更高效的证明系统。未来的工作可以探索如何在保持安全性的同时，进一步降低用户的计算成本，例如开发对secp256k1和SHA-256更友好的精简证明系统，或者设计绕过昂贵NIZK证明的替代协议。

### 强关联论文

[Cha82] Chaum, D. Blind signatures for untraceable payments. **CRYPTO 1982**

[CP93] Chaum, D., Pedersen, T. P. Wallet databases with observers. **CRYPTO 1992**

[Sch01] Schnorr, C.P. Security of blind discrete log signatures against interactive attacks. **ICICS 2001**

[FPS20] Fuchsbauer, G., Plouviez, A., Seurin, Y. Blind schnorr signatures and signed ElGamal encryption in the algebraic group model. **EUROCRYPT 2020**

[BLL+21] Benhamouda, F., Lepoint, T., Loss, J., Orrù, M., Raykova, M. On the (in)security of ROS. **EUROCRYPT 2021**

[KLX22] Kastner, J., Loss, J., Xu, J. On pairing-free blind signature schemes in the algebraic group model. **PKC 2022**

[GRS+11] Garg, S., Rao, V., Sahai, A., Schröder, D., Unruh, D. Round optimal blind signatures. **CRYPTO 2011**

[KLR21] Katz, J., Loss, J., Rosenberg, M. Boosting the security of blind signature schemes. **ASIACRYPT 2021**

[TZ22] Tessaro, S., Zhu, C. Short pairing-free blind signatures with exponential security. **EUROCRYPT 2022**

[Set20] Setty, S. Spartan: efficient and general-purpose zkSNARKs without trusted setup. **CRYPTO 2020**


## 关键词

+ 并发安全盲签名
+ Schnorr盲签名
+ 谓词盲签名
+ 非交互式零知识证明
+ 拒绝服务攻击防御