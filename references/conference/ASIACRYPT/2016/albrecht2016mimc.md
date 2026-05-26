---
title: "MiMC: Efficient encryption and cryptographic hashing with minimal multiplicative complexity"
标题简称:
论文类型: conference
会议简称: ASIACRYPT
发表年份: 2016
created: 2025-04-21 17:23:37
modified: 2025-04-21 17:29:58
---

## MiMC: Efficient encryption and cryptographic hashing with minimal multiplicative complexity

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-662-53887-6_7)

## 作者

+ Martin Albrecht 
+ [Lorenzo Grassi](Lorenzo%20Grassi.md)
+ [Christian Rechberger](Christian%20Rechberger.md)
+ [Arnab Roy](Arnab%20Roy.md)
+ Tyge Tiessen 

## 笔记

### 背景与动机
在安全多方计算、全同态加密和零知识证明等现代密码学应用中，被计算的对象常常包含对称密码原语（如伪随机函数或哈希函数）。在这些场景下，域乘法运算构成了最主要的性能瓶颈，而线性运算（如加法或异或）的成本相对可以忽略。虽然已有针对布尔域优化的设计，例如 LowMC [ARS+15]，它们主要关注降低电路深度，但许多协议原生支持在较大域 $\mathrm{GF}(p)$ 或 $\mathrm{GF}(2^n)$ 上的操作，将这些域中的操作编码为布尔电路会带来高昂的转换代价。以AES为例，尽管其S-box在多种域上都有高效描述，但在实际GMW协议的实现中，低AND门数的LowMC却往往难以超越AES，部分原因是LowMC引入了大量异或运算，使其成本不再可忽略。本文旨在填充分布式密码学中一个显著的空白：设计一种在大域上原生工作、域乘法数量极少的对称密码原语，以解决现有方案在域转换代价和乘法数量之间的不平衡问题。

### 相关工作

[KN95] Knudsen, L.R., Nyberg, K. Provable security against a differential attack. **J. Crypt. 1995** [Google Scholar](https://scholar.google.com/scholar?q=Provable+security+against+a+differential+attack)
> 核心思路：提出一种DES风格的Feistel密码，使用域 $\mathrm{GF}(2^{37})$ 上的三次方映射 $x^3$ 作为非线性层，旨在以较少的轮数提供针对差分攻击的可证明安全性。
> 局限与区别：该设计轮数较少（6轮），容易被插值攻击攻破。本文仅在结构上继承了其核心非线性函数 $x^3$，但大幅增加了轮数至数百轮，以抵抗代数攻击。

[JK97] Jakobsen, T., Knudsen, L.R. The interpolation attack on block ciphers. **FSE 1997** [Google Scholar](https://scholar.google.com/scholar?q=The+interpolation+attack+on+block+ciphers)
> 核心思路：提出插值攻击，通过构造加密函数的插值多项式来恢复密钥，并成功攻击了类似本文设计的简化密码变体。
> 局限与区别：本文的设计直接重置了该攻击中被破解的密码，并证明了增加轮数可以使插值多项式的次数足够高，从而有效地抵抗该攻击。

[ARS+15] Albrecht, M.R., Rechberger, C., Schneider, T., Tiessen, T., Zohner, M. Ciphers for MPC and FHE. **EUROCRYPT 2015** [Google Scholar](https://scholar.google.com/scholar?q=Ciphers+for+MPC+and+FHE)
> 核心思路：提出LowMC系列密码，专门针对MPC和FHE应用进行优化，目标是降低布尔域 $\mathrm{GF}(2)$ 上的AND门数量。
> 局限与区别：LowMC在布尔域上进行优化，当应用于原生支持大域操作的协议时，需要昂贵的域转换，且其大量的异或运算在某些场景下（如SNARKs）会显著拖慢性能。本文则直接在大域上设计，追求原生高效。

[PH78] Pohlig, S.C., Hellman, M.E. An improved algorithm for computing logarithms over GF(p) and its cryptographic significance. **IEEE Trans. Inf. Theory 1978** [Google Scholar](https://scholar.google.com/scholar?q=An+improved+algorithm+for+computing+logarithms+over+GF(p)+and+its+cryptographic+significance)
> 核心思路：提出Pohlig-Hellman密码，其加密和解密直接基于域上的指数运算 $c = m^k \mod p$，安全性依赖于离散对数问题的困难性。
> 局限与区别：该密码的安全性基于数论假设，导致密钥恢复问题的复杂度远超 $O(n)$，因此达到安全级别所需的乘法数量随域大小超线性增长，不如MiMC的线性增长高效。

### 核心技术与方案

本文提出了一族名为“MiMC”的对称密码原语，其核心思想是使用一个极其简单的轮函数——域上的三次方映射 $F(x) = x^3$——并在轮间加入密钥和常量。整个设计围绕最小化域乘法数量展开。

**MiMC-n/n（SPN结构）**：该变体适用于域 $\mathbb{F}_{2^n}$（n为奇数以确保$x^3$是置换）或 $\mathbb{F}_p$（需满足 $\gcd(3, p-1)=1$）。加密过程为：
$$E_k(x) = (F_{r-1} \circ \dots \circ F_0)(x) \oplus k$$
其中轮函数 $F_i(x) = (x \oplus k \oplus c_i)^3$，$c_i$为轮常量。解密时需计算逆函数 $F^{-1}(x) = x^s$，其中 $s = (2^{n+1}-1)/3$。轮数 $r = \lceil n / \log_2 3 \rceil$，该参数由抵抗插值攻击的要求决定：一个$r$轮加密函数的代数次数为 $3^r$，当 $3^r \geq 2^n$ 时，插值多项式的次数将达到域的大小，攻击复杂度不可行。

**MiMC-2n/n（Feistel结构）**：该变体通过Feistel网络处理更大的块，其轮函数为：
$$x_L || x_R \longleftarrow x_R \oplus (x_L \oplus k \oplus c_i)^3 || x_L$$
轮数翻倍为 $r' = 2 \cdot \lceil n / \log_2 3 \rceil$。这个翻倍的要求源自一种边信道攻击——中间相遇GCD攻击。攻击者可以构造两个函数 $G'(K, x_i)$ 和 $G''(K, y_i)$，分别表示从明文或密文方向加密至中间轮的状态。边信道攻击通过计算这两个函数的GCD来提取密钥，其复杂度由较低的多项式次数（$3^{r/2}$）决定。若轮数仅为 $r$，则安全强度不足，故需加倍至 $2r$。

**MiMChash（哈希函数）**：基于Sponge框架构造。使用全零密钥的MiMC置换。为达到256位安全级别（如MiMCHash-256），采用MiMC-1025/1025置换，其中1025位状态被分为512位速率和513位容量，提供128位抗碰撞安全性和256位抗原像安全性。安全性论证基于置换的输出不可与随机置换区分，而MiMC轮数的选择已能抵抗高达 $2^s$ 对输入输出下的区分攻击。

**安全性论证**：
*   **插值攻击**：通过选择轮数 $r = \lceil n / \log_2 3\rceil$，使得加密函数的插值多项式阶数达到或超过域的大小 $\mathbb{F}_{2^n}$，从而使攻击者无法构造或使用该多项式。
*   **GCD攻击**：由于加密过程是密钥的显式多项式，两个已知明密文对对应的一元多项式共享 $(K-k)$ 作为公因子。通过计算GCD即可恢复密钥。MiMC-n/n的两个多项式次数均为 $3^r$，GCD计算复杂度为 $O(r^2 3^r)$。对于Feistel版本，中间相遇GCD攻击将复杂度降至 $O(r^2 3^{r/2})$，迫使轮数翻倍。
*   **差分/线性攻击**：由于 $F(x)=x^3$ 是几乎完美非线性（APN）函数，其差分概率上限为 $2/2^n$，线性相关性上限为 $2^{-n+1}$。经过一轮后，差分/线性特征的潜力即变得极低，再加轮数不是主要安全考量。
*   **子域攻击**：通过将 $n$ 选为素数，避免除 $\mathbb{F}_2$ 外的子域。只要轮常量 $c_i \neq 1$，即可阻止攻击者将输入限制在小域内。

**渐进复杂度**：在目标应用中，MiMC的核心性能指标是域乘法次数。对于MiMC-n/n，生成一次加密输出需要 $r = O(n / \log_2 3)$ 次乘法。在SNARK设置中，每个轮函数 $x^3$ 可转化为一个二次约束（形如 $(X + \alpha)(X + \alpha + Y) = Y + Z$），因此约束数量与乘法次数成正比，同为 $O(n / \log_2 3)$。相较于需要大量异或操作的计算，MiMC的线性操作仅为每轮一次域加法，成本极低。

### 核心公式与流程

**[MiMC-n/n加密函数]**
$$E_k(x) = \left(F_{r-1} \circ F_{r-2} \circ \dots \circ F_0\right)(x) \oplus k$$
其中 $F_i(x) = (x \oplus k \oplus c_i)^3, c_0 = c_r = 0$
> 作用：定义了MiMC在SPN模式下的完整加密流程。每轮的核心操作是一个域乘法和两个域加法（实质上是异或）。

**[MiMC-2n/n Feistel轮函数]**
$$x_L || x_R \longleftarrow x_R \oplus (x_L \oplus k \oplus c_i)^3 || x_L$$
> 作用：定义了处理双倍块宽的Feistel变体的单轮状态更新。最后一轮不进行左右交换。

**[逆函数计算（用于解密）]**
$$F^{-1}(x) = x^s, \quad s = \frac{2^{n+1} - 1}{3}$$
> 作用：当n为奇数时，该指数s是3在模 $2^n - 1$ 下的逆，用于解密。其代数复杂性高于加密，具有安全性提升的附加效果。

**[SNARK中的约束合并]**
$$(X + \alpha)(X + \alpha + Y) = Y + Z$$
其中 $\alpha = k_i + c_i$
> 作用：将一轮MiMC的两个中间变量 $Y = U^2$ 和 $Z = U^3$ 的约束，与状态更新结合起来，形成一个单一的秩-1二次约束，从而最小化SNARK的约束数量。

### 实验结果

实验在Intel Core i7 2.10 GHz处理器、16 GB内存上进行，取2000次运行的平均值。所有实现（C++）使用NTL和gf2x库，编译器为gcc- O3。

核心实验是**SNARK设置中的哈希性能对比**。测试了处理单个消息块（512位）的时间：
*   MiMCHash-256（基于MiMC-1025/1025置换）：**7.8 ms**
*   SHA-256（作为对比基线）：**73 ms**
*   （类似SHA-3的）Keccak-[1600, 24]置换：**75.8 ms**
*   LowMC（块大小为1025位，两种参数化版本）：**90.3 ms**（R=16, m=196）和 **271.2 ms**（R=55, m=20）

结果表明，MiMC比SHA-256快约**9.4倍**。与LowMC相比，MiMC的速度优势可达**11.6倍**至**34.7倍**。这种性能优势并非仅仅因为乘法数量少，而是因为其几乎完全避免了昂贵的域上异或运算。相比之下，LowMC虽然乘法数（MULs）更少（3300 vs 1293），但极高的异或操作数（约2890万 vs 646）使其性能严重下降，证明了在SNARK的大域设置下，加法成本不能忽略。

### 局限性与开放问题

1.  **应用场景高度特定**：MiMC的卓越性能高度依赖在其目标场景（SNARKs、MPC等），其中域乘法的成本远高于加法和线性运算。在传统计算平台（如通用CPU）上，其极高的轮数（数百轮）会导致性能远低于AES等传统密码，限制了其普适性。
2.  **构造函数依赖**：MiMC的安全性论证强烈依赖于其简单的代数结构（插值阶数、GCD攻击）。对于更复杂的非代数攻击（如积分攻击、滑动攻击，或针对特定域大小的攻击），论文虽提供了基本论证，但可能仍存在未预见的攻击向量，尤其是当轮数选择刚好达到安全阈值时。
3.  **参数选择的权衡**：论文指出，出于技术原因（如为了FFT计算需要选择特定的域大小$n$和约束数量$N_c$），实际实现的轮数或许可以少于理论推导的轮数。这意味着存在一个理论安全与实现效率之间的精细平衡，为攻击者提供了利用参数调整引入的薄弱环节的可能性。

### 强关联论文

[ARS+15] Albrecht, M.R., Rechberger, C., Schneider, T., Tiessen, T., Zohner, M. Ciphers for MPC and FHE. **EUROCRYPT 2015** [Google Scholar](https://scholar.google.com/scholar?q=Ciphers+for+MPC+and+FHE)

[JK97] Jakobsen, T., Knudsen, L.R. The interpolation attack on block ciphers. **FSE 1997** [Google Scholar](https://scholar.google.com/scholar?q=The+interpolation+attack+on+block+ciphers)

[KN95] Knudsen, L.R., Nyberg, K. Provable security against a differential attack. **J. Crypt. 1995** [Google Scholar](https://scholar.google.com/scholar?q=Provable+security+against+a+differential+attack)

[PH78] Pohlig, S.C., Hellman, M.E. An improved algorithm for computing logarithms over GF(p) and its cryptographic significance. **IEEE Trans. Inf. Theory 1978** [Google Scholar](https://scholar.google.com/scholar?q=An+improved+algorithm+for+computing+logarithms+over+GF(p)+and+its+cryptographic+significance)

[NR97] Naor, M., Reingold, O. Number-theoretic constructions of efficient pseudo-random functions. **FOCS 1997** [Google Scholar](https://scholar.google.com/scholar?q=Number-theoretic+constructions+of+efficient+pseudo-random+functions)

[LMPR08] Lyubashevsky, V., Micciancio, D., Peikert, C., Rosen, A. SWIFFT: a modest proposal for FFT hashing. **FSE 2008** [Google Scholar](https://scholar.google.com/scholar?q=SWIFFT:+a+modest+proposal+for+FFT+hashing)

[BBL+15] Banerjee, A., Brenner, H., Leurent, G., Peikert, C., Rosen, A. SPRING: fast pseudorandom functions from rounded ring products. **FSE 2014** [Google Scholar](https://scholar.google.com/scholar?q=SPRING:+fast+pseudorandom+functions+from+rounded+ring+products)

[BSCG+13] Ben-Sasson, E., Chiesa, A., Genkin, D., Tromer, E., Virza, M. SNARKs for C: verifying program executions succinctly and in zero knowledge. **CRYPTO 2013** [Google Scholar](https://scholar.google.com/scholar?q=SNARKs+for+C:+verifying+program+executions+succinctly+and+in+zero+knowledge)

[CGP+12] Carlet, C., Goubin, L., Prouff, E., Quisquater, M., Rivain, M. Higher-order masking schemes for S-boxes. **FSE 2012** [Google Scholar](https://scholar.google.com/scholar?q=Higher-order+masking+schemes+for+S-boxes)


## 关键词

+ MiMC
+ 低乘法复杂度
+ 算术友好哈希函数
+ 零知识证明电路
+ SNARK优化