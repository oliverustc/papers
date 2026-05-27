---
title: "Random oracles are practical: a paradigm for designing efficient protocols"
doi: 10.1145/168588.168596
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 1993
modified: 2025-04-08 11:41:08
---
## Random oracles are practical: a paradigm for designing efficient protocols

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/168588.168596)
+ [2021年重制版](https://cseweb.ucsd.edu/~Mihir/papers/ro.pdf)

## 作者

+ [Mihir Bellare](Mihir%20Bellare.md)
+ Phillip Rogaway

## 笔记

### 背景与动机
密码学理论提供了可证明安全性这一宝贵概念，但传统上获得安全性往往以牺牲效率为代价。理论家将单向函数等视为“基本”原语，并以低效方式构建更强大的原语；然而在实践中，强力原语（如伪随机函数）已可直接获得，而“基本”原语反而难以高效实现。随机神谕范式旨在弥合理论与实践的鸿沟：首先在各方共享随机神谕的模型中设计和证明协议的正确性，然后用“适当选择”的Hash函数替换神谕访问。该范式源于Goldreich、Goldwasser和Micali [20, 21]以及Fiat和Shamir [14]的工作，并受到大量“无正当理由”使用Hash函数的实践的启发。本文系统地将该范式应用于加密、签名和零知识证明等多个密码学问题，获得比标准方案更高效的解决方案，同时保留了可证明安全性的诸多优势。

### 相关工作

[20] Goldreich, S. Goldwasser, S. Micali. How to construct random functions. **J. ACM 1986** [Google Scholar](https://scholar.google.com/scholar?q=How+to+construct+random+functions)
> 核心思路：构造伪随机函数族（PRF），并建议用PRF实例化随机神谕。
> 局限与区别：PRF的种子必须对对手保密，因此只适用于对手无法访问神谕的场景；本文需要公共同等访问的神谕模型以适用更广泛的协议。

[14] A. Fiat, A. Shamir. How to prove yourself: practical solutions to identification and signature problems. **Crypto 1986** [Google Scholar](https://scholar.google.com/scholar?q=How+to+prove+yourself:+practical+solutions+to+identification+and+signature+problems)
> 核心思路：首次明确采用公共随机神谕模型，将交互式身份识别方案转化为数字签名方案。
> 局限与区别：仅针对签名问题；本文将其推广到加密、零知识等更广泛的领域，并给出正式定义和证明。

[24] S. Goldwasser, S. Micali. Probabilistic encryption. **J. Comput. Syst. Sci. 1984** [Google Scholar](https://scholar.google.com/scholar?q=Probabilistic+encryption)
> 核心思路：定义了多项式/语义安全性，并给出基于硬核谓词的加密方案。
> 局限与区别：该方案加密长度和计算开销均为O(k·|x|)，效率极低；本文方案效率高得多。

[4] M. Blum, S. Goldwasser. An efficient probabilistic public-key encryption scheme which hides all partial information. **Crypto 1984** [Google Scholar](https://scholar.google.com/scholar?q=An+efficient+probabilistic+public-key+encryption+scheme+which+hides+all+partial+information)
> 核心思路：更高效的公钥加密方案，密文长度O(|x|+k)。
> 局限与区别：仍需O(|x|)次模平方运算来加密，解密也需多次运算；本文方案只需一次trapdoor permutation运算。

[36] C. Rackoff, D. Simon. Non-interactive zero-knowledge proof of knowledge and chosen ciphertext attack. **Crypto 1991** [Google Scholar](https://scholar.google.com/scholar?q=Non-interactive+zero-knowledge+proof+of+knowledge+and+chosen+ciphertext+attack)
> 核心思路：定义更强的选择密文安全性，并基于NIZK给出解决方案。
> 局限与区别：依赖非交互式零知识证明，效率极低；本文方案在随机神谕模型中高效实现。

[13] D. Dolev, C. Dwork, M. Naor. Non-malleable cryptography. **STOC 1991** [Google Scholar](https://scholar.google.com/scholar?q=Non-malleable+cryptography)
> 核心思路：定义非延展性，并构造安全的加密方案。
> 局限与区别：构造极为低效，涉及大公钥、多个签名和NIZK；本文方案在随机神谕模型中高效实现非延展性。

[34] M. Naor, M. Yung. Public-key cryptosystems provably secure against chosen ciphertext attacks. **STOC 1990** [Google Scholar](https://scholar.google.com/scholar?q=Public-key+cryptosystems+provably+secure+against+chosen+ciphertext+attacks)
> 核心思路：第一个提供选择密文安全性的定义和方案。
> 局限与区别：安全性定义较弱（非[36]定义的强安全性），且方案效率不高。

[6] M. Blum, P. Feldman, S. Micali. Non-interactive zero knowledge and its applications. **STOC 1988** [Google Scholar](https://scholar.google.com/scholar?q=Non-interactive+zero+knowledge+and+its+applications)
> 核心思路：提出非交互式零知识证明（NIZK）并用于多种密码学构造。
> 局限与区别：NIZK构造本身复杂，导致基于它的方案效率低下；本文用随机神谕模型简化构造。

[7] M. Blum, A. De Santis, S. Micali, G. Persiano. Non-interactive zero-knowledge proof systems. **SIAM J. Comput. 1991** [Google Scholar](https://scholar.google.com/scholar?q=Non-interactive+zero-knowledge+proof+systems)
> 核心思路：对NIZK进行系统性研究和形式化。
> 局限与区别：与[6]类似，效率问题限制实用性；本文用随机神谕模型得到更高效的NIZK。

### 核心技术与方案
本文的核心技术是提出并应用随机神谕范式：对加密、签名和零知识证明三类问题分别给出定义和构造。

对于**加密**，论文定义了在随机神谕模型中的多项式安全性、选择密文安全性和非延展性，并提供了两个高效方案。
第一个方案仅使用随机生成器G，加密为 $E^G(x) = f(r) \parallel G(r) \oplus x$，其中f是trapdoor permutation，r随机选取。解密时计算 $D^G(ys) = s \oplus G(f^{-1}(y))$。其安全性证明使用归约：若存在多项式安全性的敌手，则构造算法M利用该敌手来求逆f。M模拟G神谕，并将f的挑战值y用作公钥中的f(r)部分。如果敌手成功区分密文，则必然以不可忽略概率查询了r= f^{-1}(y)的G值，M可借此输出r并以不可忽略概率求逆。该方案只需一次f运算加密和一次f^{-1}运算解密，密文长度为O(|x|+k)。

第二个方案通过添加H神谕增强为选择密文安全和非延展性：$E^{G,H}(x) = f(r) \parallel G(r) \oplus x \parallel H(rx)$。解密时验证H值的正确性，否则输出0。安全性证明类似于第一个方案，但需额外处理密文合法性验证带来的问题。对于选择密文攻击，证明中定义事件A_k（敌手查询了关键值）和L_k（敌手伪造有效密文而未查询H），并证明若敌手成功概率高于1/2+λ(k)，则λ(k) - n(k)2^{-k}不可忽略，从而M成功求逆的概率也非可忽略。非延展性证明通过分析实验1与实验2的差异，证明任何能产生相关密文的敌手都可以被用来求逆f，从而保证概率差异可忽略。

对于**签名**，论文给出了一种简单的构造：对消息m的签名为 $\sigma = f^{-1}(H(m))$，验证等式 $f(\sigma) = H(m)$。安全性证明通过将签名伪造者归约为trapdoor permutation求逆算法M：M随机猜测伪造者H查询中的一个是挑战值y，并用随机值回答其他查询，对于签名查询则用预先计算的对应于该H值的f下的原像回答。若伪造者成功且伪造的消息恰好对应猜测的查询，则伪造的签名即为y的原像。通过分析，M成功概率至少为(1 - 1/n(k))·λ(k)/n(k) - 2^{-k}。

对于**零知识证明**，论文首先给出了在随机神谕模型中的正式定义，特别地，模拟器可以输出部分神谕信息（多项式大小的表T），其余由随机完成操作ROC填充。然后，给出将任意3轮交互式ZK证明转化为非交互式ZK证明的通用构造：设原交互式证明为(P', V')，k(n)=ω(log n)，H为随机Hash函数。证明者并行运行2k次独立证明，取 $\alpha_1,\ldots,\alpha_{2k}$，计算挑战 $b_i'$ 为 $H(\alpha_1\ldots\alpha_{2k})$ 的第i位，再计算相应的 $\beta_i$，最终发送 $(\alpha_1,\ldots,\alpha_{2k},\beta_1,\ldots,\beta_{2k})$。验证者检查所有2k个证明是否通过。该协议非交互，通信和计算开销为原交互式证明的O(k(n))倍。错误概率可降为 $2^{-k(n)}$（通过证明查询次数查询上限T(n)得到 $\epsilon \leq T(n) \cdot 2^{-2k}$）。零知识性通过模拟器S构造：随机选择2k个比特b_i，用原模拟器S'生成每个证明，设置神谕表T使得H在该输入上的输出恰为b_1...b_{2k}。

### 核心公式与流程

**多项式安全加密方案**
$$E^G(x) = f(r) \parallel G(r) \oplus x$$
$$D^G(ys) = s \oplus G(f^{-1}(y))$$
> 作用：基础加密方案，在随机神谕模型中达到多项式安全性，只需一次trapdoor permutation运算。

**选择密文安全与非延展性加密方案**
$$E^{G,H}(x) = f(r) \parallel G(r) \oplus x \parallel H(rx)$$
$$D^{G,H}(y): \text{解析 } y = a \parallel w \parallel b, \text{令 } r = f^{-1}(a), x' = w \oplus G(r); \text{若 } H(r x') = b \text{ 则输出 } x', \text{否则输出 } 0$$
> 作用：增强方案，通过添加H验证达到选择密文安全和非延展性。

**签名方案**
$$\sigma = f^{-1}(H(m)), \quad \text{Verify: } f(\sigma) = H(m)$$
> 作用：经典的Hash-Then-Sign方案，在随机神谕模型中被证明安全。

**ZK互动证明转非交互构造**
$$\text{Prover: } \alpha_1,\ldots,\alpha_{2k} \leftarrow P'(x,\Lambda); \quad b_i \leftarrow H(\alpha_1\ldots\alpha_{2k})[i]; \quad \beta_i \leftarrow P'(x,\alpha_i b_i)$$
$$\text{Verifier: } b_i \leftarrow H(\alpha_1\ldots\alpha_{2k})[i]; \quad \text{accept iff } \forall i: \text{ACC}_{V'}(\alpha_i b_i \beta_i, b_i)=1$$
> 作用：通用转化，将任意3轮交互式ZK证明转化为非交互式ZK证明，开销增加O(k(n))倍。

### 实验结果
本文是理论性论文，没有提供数值实验数据。其“实验结果”主要体现在效率分析对比上。对于加密，本文方案（$O(|x|+k)$密文长度，1次f运算加密，1次f^{-1}运算解密）显著优于传统多项式安全方案（O(k·|x|)密文，O(|x|)次f运算）和Blum-Goldwasser方案（O(|x|+k)密文，但需O(|x|)次模平方加密）。对于签名，方案简单到就是“经典”的Hash-Then-Sign，与之前未证明安全的方案具有相同的实践效率。对于零知识证明，转化后方案的计算和通信开销为原交互式协议的O(k(n))倍，是到目前为止最高效的非交互式零知识证明之一。文中提到Leighton-Micali [28]独立地利用随机神谕模型实现了高效且具有精确安全性分析的签名方案。

### 局限性与开放问题
本文承认，用具体哈希函数实例化随机神谕是启发式的，无法在标准模型下证明安全性。作者指出存在“反例”问题：若协议的设计依赖具体哈希函数的结构，可能会导致随机神谕模型下安全但实例化后不安全。关于如何形式化“独立性”未作处理。开放问题包括：是否存在复杂度理论假设能很好地捕捉公共随机神谕的所有性质？能否将Goldreich等人的伪随机函数簇概念扩展为不涉及隐藏随机性的同样有用且令人信服的概念？

### 强关联论文

[20] Goldreich, S. Goldwasser, S. Micali. How to construct random functions. **J. ACM 1986** [Google Scholar](https://scholar.google.com/scholar?q=How+to+construct+random+functions)

[14] A. Fiat, A. Shamir. How to prove yourself: practical solutions to identification and signature problems. **Crypto 1986** [Google Scholar](https://scholar.google.com/scholar?q=How+to+prove+yourself:+practical+solutions+to+identification+and+signature+problems)

[24] S. Goldwasser, S. Micali. Probabilistic encryption. **J. Comput. Syst. Sci. 1984** [Google Scholar](https://scholar.google.com/scholar?q=Probabilistic+encryption)

[36] C. Rackoff, D. Simon. Non-interactive zero-knowledge proof of knowledge and chosen ciphertext attack. **Crypto 1991** [Google Scholar](https://scholar.google.com/scholar?q=Non-interactive+zero-knowledge+proof+of+knowledge+and+chosen+ciphertext+attack)

[13] D. Dolev, C. Dwork, M. Naor. Non-malleable cryptography. **STOC 1991** [Google Scholar](https://scholar.google.com/scholar?q=Non-malleable+cryptography)

[4] M. Blum, S. Goldwasser. An efficient probabilistic public-key encryption scheme which hides all partial information. **Crypto 1984** [Google Scholar](https://scholar.google.com/scholar?q=An+efficient+probabilistic+public-key+encryption+scheme+which+hides+all+partial+information)

[34] M. Naor, M. Yung. Public-key cryptosystems provably secure against chosen ciphertext attacks. **STOC 1990** [Google Scholar](https://scholar.google.com/scholar?q=Public-key+cryptosystems+provably+secure+against+chosen+ciphertext+attacks)

[6] M. Blum, P. Feldman, S. Micali. Non-interactive zero knowledge and its applications. **STOC 1988** [Google Scholar](https://scholar.google.com/scholar?q=Non-interactive+zero+knowledge+and+its+applications)

[28] T. Leighton, S. Micali. Provably fast and secure digital signature algorithms based on secure hash functions. **Manuscript 1993** [Google Scholar](https://scholar.google.com/scholar?q=Provably+fast+and+secure+digital+signature+algorithms+based+on+secure+hash+functions)

[44] Y. Zheng, J. Seberry. Practical approaches to attaining security against adaptively chosen ciphertext attacks. **Crypto 1992** [Google Scholar](https://scholar.google.com/scholar?q=Practical+approaches+to+attaining+security+against+adaptively+chosen+ciphertext+attacks)


## 关键词

+ 随机预言模型
+ 可证明安全性
+ 数字签名
+ 零知识证明
+ 加密协议