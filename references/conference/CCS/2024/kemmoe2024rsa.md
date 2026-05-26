---
title: "RSA-Based Dynamic Accumulator without Hashing into Primes"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2024
---

## RSA-Based Dynamic Accumulator without Hashing into Primes

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3658644.3690199)

## 作者

+ Victor Youdom Kemmoe 
+ [Anna Lysyanskaya](Anna%20Lysyanskaya.md) 


## 笔记

### 背景与动机
密码学累加器是一种紧凑的数据结构，用于表示一个集合的元素，并提供紧凑的成员证明或非成员证明。它在分布式系统的证书撤销场景中具有重要应用价值，例如WebPKI，一个理想的累加器能够使浏览器仅需验证一个固定大小的累加器值和一个简短见证，即可判断证书是否被吊销，从而极大降低移动设备的通信和计算开销。然而，现有基于RSA的动态累加器要求待累加的元素必须表示为素数，导致每次添加元素前都需要执行昂贵的哈希到素数的操作，其计算开销约为$O(\log N)$次素性测试，成为实际部署的主要性能瓶颈。尽管后来出现了基于双线性映射的累加器方案，但这些方案要么需要线性于集合上限大小的公共参考串，要么依赖持有陷门的受信第三方才能高效添加元素，限制了其去中心化应用。本文旨在填补这一空白，提出一种无需哈希到素数的RSA动态累加器，大幅提升效率，使其能够首次成为WebPKI类系统中证书撤销机制的可行候选方案。

### 相关工作

[5] Barić 等. Collision-Free Accumulators and Fail-Stop Signature Schemes Without Trees. **EUROCRYPT 1997** [Google Scholar](https://scholar.google.com/scholar?q=Collision-Free+Accumulators+and+Fail-Stop+Signature+Schemes+Without+Trees)
> 核心思路：首次证明，若将累加器域限制为素数，则Benaloh-de Mare构造在强RSA假设下是安全的。
> 局限与区别：该方案要求所有元素均为素数，哈希到素数的过程成为性能瓶颈；本文将其替换为哈希到大奇数，并通过引入“平滑因子”处理潜在的H(x)约数问题。

[16] Camenisch 等. Dynamic Accumulators and Application to Efficient Revocation of Anonymous Credentials. **CRYPTO 2002** [Google Scholar](https://scholar.google.com/scholar?q=Dynamic+Accumulators+and+Application+to+Efficient+Revocation+of+Anonymous+Credentials)
> 核心思路：在Barić-Pfitzmann素数域累加器基础上，利用Shamir技巧实现元素的高效删除和见证更新。
> 局限与区别：当哈希输出不再为素数时，Shamir技巧的GCD不一定为1；本文引入广义见证的概念，将GCD因子存入见证的平滑因子元组中，从而恢复更新的正确性。

[25] Li 等. Universal Accumulators with Efficient Nonmembership Proofs. **ACNS 2007** [Google Scholar](https://scholar.google.com/scholar?q=Universal+Accumulators+with+Efficient+Nonmembership+Proofs)
> 核心思路：扩展了Camenisch-Lysyanskaya的动态累加器，支持非成员证明，并给出高效的见证更新方法。
> 局限与区别：其安全定义不允许敌手进行删除操作，且哈希到素数的要求仍然存在；本文放宽了哈希要求，同时给出了包含删除操作的安全定义。

[34] Wesolowski. Efficient Verifiable Delay Functions. **Journal of Cryptology 2020** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+Verifiable+Delay+Functions)
> 核心思路：提出了基于自适应根假设的指数证明协议，其中验证器发送随机素数挑战，证明器返回压缩的幂次结果。
> 局限与区别：协议的非交互转换需要哈希到素数；本文提出SimPoE变体，将挑战空间从素数改为大奇数，并在随机预言机模型下证明其可靠性。

[7] Benaloh 等. One-Way Accumulators: A Decentralized Alternative to Digital Signatures. **EUROCRYPT 1993** [Google Scholar](https://scholar.google.com/scholar?q=One-Way+Accumulators:+A+Decentralized+Alternative+to+Digital+Signatures)
> 核心思路：提出RSA累加器的原始概念，累加器值为$A_0^{\prod_{x \in S} x} \mod n$，见证为$A_0^{\prod_{x' \in S, x' \neq x} x'} \mod n$。
> 局限与区别：方案本身未达完备的正确性/安全性，且不支持元素删除；本文在其基础上引入随机预言机和广义见证，实现了动态性和可证明安全性。

[3] Baldimtsi 等. Accumulators with Applications to Anonymity-Preserving Revocation. **EuroS&P 2017** [Google Scholar](https://scholar.google.com/scholar?q=Accumulators+with+Applications+to+Anonymity-Preserving+Revocation)
> 核心思路：系统化提出了累加器的形式化定义，并给出了基于RSA的CL-RSA-B构造。
> 局限与区别：该构造依赖素数输入才能实现正确的见证更新；本文通过存储GCD因子，使得相同的见证更新公式在非素数输入下仍然有效。

[30] Nguyen. Accumulators from Bilinear Pairings and Applications. **CT-RSA 2005** [Google Scholar](https://scholar.google.com/scholar?q=Accumulators+from+Bilinear+Pairings+and+Applications)
> 核心思路：提出了基于双线性映射的累加器，支持高效的动态更新和通用证明。
> 局限与区别：需要线性于集合上限的公共参考串，或依赖持有陷门的受信第三方；本文专注于RSA构造，避免了此需求。

[24] Larisch 等. CRLite: A Scalable System For Pushing All TLS Revocations To Browsers. **IEEE S&P 2017** [Google Scholar](https://scholar.google.com/scholar?q=CRLite:+A+Scalable+System+For+Pushing+All+TLS+Revocations+To+Browsers)
> 核心思路：设计了一种基于布隆过滤器和级联过滤的证书吊销验证系统，将吊销数据库压缩至约5MB。
> 局限与区别：CRLite仍需用户下载数兆字节的过滤数据；本文的累加器方案可将验证所需数据压缩至单个群元素和见证，通信开销更低。

### 核心技术与方案

本文的核心构造分为以下几个层次：首先，在随机预言机模型下，将哈希函数$H$的输出域设定为大奇数，并利用数论引理（Lemma 2&Corollary 1）保证任意输入的$H(x)$的最大素因子以压倒性概率大于$2^\tau$，从而防止一个元素的哈希值整除其他元素哈希值的乘积。基于此，累加器定义为$\mathsf{A}_S = \mathsf{A}_0^{\prod_{x \in S} H(x)} \mod n$，其中$\mathsf{A}_0$为初始值。成员见证$w_x = (w, \mathsf{s})$的构造分两种场景：若持有陷门sk，则直接计算$w = \mathsf{A}_0^{1/H(x)} \mod n$并令$\mathsf{s}=(1)$；若不持有陷门，则通过更新累加器值$\mathsf{A}' = \mathsf{A}^{H(x)}$并设置$w = \mathsf{A}$。安全证明通过构建一个从打破累加器安全性的敌手到解决灵活RSA问题的规约来完成：规约者猜测敌手伪造见证时使用的随机预言机查询索引，并相应嵌入强RSA挑战，最终利用Shamir技巧提取一个非平凡根。

其次，为支持元素删除，本文引入了广义见证概念。假设删除元素y时，其哈希值$H(y)$与$x$的哈希值$H(x)$的最大公因子$d = \gcd(H(x), H(y)) > 1$。此时，直接应用Camenisch-Lysyanskaya的见证更新公式无法保证$(w')^{H(x)} = \mathsf{A}'$。本文的解决方法是：在见证中额外存储一个元组$\mathsf{s}$，用于记录所有形如$d$的$2^\tau$-平滑因子。具体地，更新时先计算$x' = H(x) / \prod_{s \in \mathsf{s}} s$和$v' = H(y) / \delta$（其中$\delta$为删除时提供的平滑因子），然后利用扩展欧几里得算法找到$a, b$使得$a x' + b v' = \gcd(x', v')$，计算$w' = (\mathsf{A}')^a w^b \mod n$。若$\gcd(x', v') > 1$，则将其加入$\mathsf{s}$。这样，验证时只需检查$w^{H(x) / \prod_{s \in \mathsf{s}} s} = \mathsf{A}$，即可保证正确性。Lemma 4证明了正确的见证更新失败概率可忽略。

第三，对于通用累加器，本文扩展了Li-Li-Xue的非成员证明技术。给定非成员$x \notin S$，由于$H(x) \nmid \prod_{x' \in S} H(x')$以压倒性概率成立，可分解$H(x) = x \cdot k$，其中$x$与累加器乘积互质且$P^+(x) > 2^\tau$，$k$为$2^\tau$-平滑因子。然后找到$a, B$使得$\mathsf{A}^a B^{x} = u$（$u$为初始累加器值），非成员见证记为$(a, B, \mathsf{s})$，其中$\mathsf{s}$存储$k$的平滑因子。更新非成员见证时，根据添加或删除操作，通过调整$a$和$B$并更新$\mathsf{s}$中的平滑因子，使得验证方程仍然成立。

最后，为实现见证聚合，本文提出了SimPoE协议。该协议是Wesolowski指数证明的变体：验证器发送一个从大奇数集$\text{Odds}(2^{\ell-1}, 2^\ell-1)$中均匀随机采样的挑战$c$，证明器计算$\pi = v^{\lfloor e / c \rfloor}$，验证器检查$\pi^c v^{e \mod c} = u$。Theorem 4证明，在自适应根假设下，只要挑战空间中的大数以压倒性概率含有大素因子，协议就是可靠的。与原始方案相比，SimPoE的非交互版本（NI-SimPoE）通过随机预言机$H$生成挑战，避免了哈希到素数的开销。利用NI-SimPoE，成员见证聚合可简化为：合并两个见证为单个$w_{x,y}$满足$w_{x,y}^{x y'} = \mathsf{A}$（其中$y'$为消去GCD后的因子），并附加一个对$(w_{x,y}, \mathsf{A}, x y')$的NI-SimPoE证明，验证时仅需检查该证明。非成员见证聚合类似，通过合并$a, B$并附加两个NI-SimPoE证明（分别验证$\mathsf{A}^{a_{x,y}} = \mathsf{C}$和$B_{x,y}^{x y'} = \mathsf{D}$）。系统复杂度方面，累加器值和见证大小为$\text{poly}(\lambda)$，聚合后的验证时间复杂度与验证单一元素相当，更新信息大小为$\Omega(s)$（$s$为操作次数），满足Camacho-Hevia的下界。

### 核心公式与流程

**[累加器定义]**
$$ \mathsf{A}_S = \mathsf{A}_0^{\prod_{x \in S} H(x)} \mod n $$
> 作用：定义代表集合$S$的累加器值，其中$H$为随机预言机，输出域为$\text{Odds}(2^{\ell-1}, 2^\ell-1)$。

**[成员验证]**
$$ w^{H(x) / \prod_{i=1}^{|\mathsf{s}|} \mathsf{s}[i]} \equiv \mathsf{A} \pmod{n} \quad \text{且} \quad \forall i, \mathsf{s}[i] \leq 2^\tau $$
> 作用：验证成员关系。$w$为群元素，$\mathsf{s}$为存储$2^\tau$-平滑因子的元组，用于消去$x$的哈希值中的小因子。

**[认证更新公式——删除]**
$$ a x' + b v' = \gcd(x', v'), \quad w' = (\mathsf{A}')^{a} w^{b} \mod n, \quad \mathsf{s}' = \mathsf{s} \| (\gcd(x', v')) $$
> 作用：在删除元素$y$后更新元素$x$的见证。$x' = H(x) / \prod_{s \in \mathsf{s}} s$，$v' = H(y) / \delta$，$\delta$为删除时提供的小因子。通过Shamir技巧和存储GCD因子保证更新后$(w')^{x' / \gcd(x', v')} = \mathsf{A}'$。

**[SimPoE协议]**
$$ \text{Verifier: } c \leftarrow \text{Odds}(2^{\ell-1}, 2^\ell-1), \quad \text{Prover: } \pi = v^{\lfloor e/c \rfloor}, \quad \text{Check: } \pi^c v^{e \bmod c} \equiv u \pmod{n} $$
> 作用：证明$v^e = u$。将Wesolowski的挑战空间从素数改为大奇数，避开了哈希到素数的需求。在自适应根假设下可靠。

**[非成员验证]**
$$ \mathsf{A}^{a} B^{H(x) / \prod_{i=1}^{|\mathsf{s}|} \mathsf{s}[i]} \equiv u \pmod{n}, \quad \forall i, \mathsf{s}[i] \leq 2^\tau $$
> 作用：验证$x \notin S$。$u$为初始累加器值，$a$和$B$由扩展欧几里得算法得到，$\mathsf{s}$存储$H(x)$中被$\prod_{x' \in S} H(x')$整除的小因子。

### 实验结果

实验在一台Intel Core i7-11800H 2.30 GHz CPU、16 GB RAM的笔记本电脑上完成，使用SageMath 9.5实现。哈希到素数的方案采用Barić-Pfitzmann构造，底层哈希为Blake2b，素性测试使用Miller-Rabin（50轮），误差概率$10^{-30}$。哈希到大奇数的方案通过拼接多个Blake2b输出并翻转首尾比特实现。RSA模数长度遵循NIST建议：2048-bit（$\lambda=112$），3072-bit（$\lambda=128$），7680-bit（$\lambda=192$），15360-bit（$\lambda=256$）。输入均为4 KB。对于$\lambda=128$（实际部署常用安全级别），哈希到大奇数（1704-bit）仅需0.60 ms，而哈希到素数（264-bit）需13.62 ms，加速比约23倍。使用私钥的Add操作：本文方案耗时7.38 ms，哈希到素数方案耗时20.37 ms。验证操作：本文方案耗时4.02 ms，哈希到素数方案耗时6.01 ms。对于$\lambda=112$，本文的All-in-one成员见证大小为436 bytes，而基于素数的方案为256 bytes；非成员见证本文为616 bytes，素数为285 bytes。SimPoE证明时间两者相近（约2.15 s vs. 2.24 s for 128 KB exponent），但验证时间本文为7.27 ms，素数方案为6.55 ms。总体而言，本文在$\lambda\leq 128$时取得显著性能优势，但在更高安全级别（$\lambda \geq 192$）因哈希输出过长（2896-bit）导致模幂运算开销增大，优势减弱。

### 局限性与开放问题

本文方案的成员见证大小在$\lambda=128$时约为436 bytes，是素数方案（256 bytes）的1.7倍，对于极度受限的IoT设备可能仍有负担。非成员证明的生成（NonMemWitCreate）需遍历所有累加元素，时间复杂度为$O(|S|)$，在大规模动态集合中不够高效。未来工作可探索如何利用累加器的分治或并行结构降低见证大小；同时，SimPoE在RSA群$\mathbb{Z}_n^*$中可能出现符号问题（如$(-u, v, e)$），需限定在QR$_n$子群中使用，这也限制了其通用性。

### 强关联论文

[5] Barić et al. Collision-Free Accumulators and Fail-Stop Signature Schemes Without Trees. **EUROCRYPT 1997** [Google Scholar](https://scholar.google.com/scholar?q=Collision-Free+Accumulators+and+Fail-Stop+Signature+Schemes+Without+Trees)

[7] Benaloh et al. One-Way Accumulators: A Decentralized Alternative to Digital Signatures. **EUROCRYPT 1993** [Google Scholar](https://scholar.google.com/scholar?q=One-Way+Accumulators:+A+Decentralized+Alternative+to+Digital+Signatures)

[16] Camenisch et al. Dynamic Accumulators and Application to Efficient Revocation of Anonymous Credentials. **CRYPTO 2002** [Google Scholar](https://scholar.google.com/scholar?q=Dynamic+Accumulators+and+Application+to+Efficient+Revocation+of+Anonymous+Credentials)

[25] Li et al. Universal Accumulators with Efficient Nonmembership Proofs. **ACNS 2007** [Google Scholar](https://scholar.google.com/scholar?q=Universal+Accumulators+with+Efficient+Nonmembership+Proofs)

[34] Wesolowski. Efficient Verifiable Delay Functions. **Journal of Cryptology 2020** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+Verifiable+Delay+Functions)

[3] Baldimtsi et al. Accumulators with Applications to Anonymity-Preserving Revocation. **EuroS&P 2017** [Google Scholar](https://scholar.google.com/scholar?q=Accumulators+with+Applications+to+Anonymity-Preserving+Revocation)

[24] Larisch et al. CRLite: A Scalable System For Pushing All TLS Revocations To Browsers. **IEEE S&P 2017** [Google Scholar](https://scholar.google.com/scholar?q=CRLite:+A+Scalable+System+For+Pushing+All+TLS+Revocations+To+Browsers)

[30] Nguyen. Accumulators from Bilinear Pairings and Applications. **CT-RSA 2005** [Google Scholar](https://scholar.google.com/scholar?q=Accumulators+from+Bilinear+Pairings+and+Applications)


## 关键词

+ RSA动态累加器
+ 通用累加器
+ 见证聚合
+ 证书撤销机制
+ 无素数映射的指数证明