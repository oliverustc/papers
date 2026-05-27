---
title: "Signature schemes and anonymous credentials from bilinear maps"
doi: 10.1007/978-3-540-28628-8_4

标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 2004
created: 2025-05-15 09:58:15
modified: 2025-05-26 05:05:07
---
## Signature schemes and anonymous credentials from bilinear maps

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-540-28628-8_4)

## 作者

+ [Jan Camenisch](Jan%20Camenisch.md)
+ [Anna Lysyanskaya](Anna Lysyanskaya.md)

## 笔记

### 背景与动机
数字签名是现代密码学的基石，但构造一个既高效又在标准模型下可证明安全的方案极为困难。现有方案要么依赖随机预言模型（如基于RSA或Schnorr的设计），其安全证明在现实世界中不成立；要么基于强RSA假设（如Cramer-Shoup方案），其安全性依赖于大整数分解的困难性。然而，基于离散对数假设的标准模型签名方案远不如前者高效。更关键的是，许多高级应用——如匿名凭证系统和群签名——不仅需要一个签名方案，还需要支持对承诺值签名和证明知道签名的专用协议。此前，这样的协议仅存在于基于强RSA假设的系统中，缺乏基于离散对数类假设的替代方案。本文旨在填补这一空白：利用双线性映射，基于LRSW假设构造出第一个高效且支持丰富协议的数字签名方案，并由此构建出同样基于离散对数假设的匿名凭证系统和群签名方案。

### 相关工作

[30] Lysyanskaya et al. Pseudonym systems. **SAC 1999** [Google Scholar](https://scholar.google.com/scholar?q=Pseudonym+systems)
> 核心思路：提出了LRSW假设，并证明了其在一般群模型中成立。
> 局限与区别：该原始假设并不要求群具有双线性映射，因此其后续应用受限。本文首次将LRSW假设应用于支持双线性对的群，构造了具体的签名方案。

[10] Camenisch and Lysyanskaya. A signature scheme with efficient protocols. **SCN 2002** [Google Scholar](https://scholar.google.com/scholar?q=A+signature+scheme+with+efficient+protocols)
> 核心思路：基于强RSA假设构造了签名方案和相应的有效协议，支持对承诺值的签名和证明。
> 局限与区别：其安全性完全依赖于RSA假设，而本文则首次实现了基于离散对数类假设的同等功能。

[4] Boneh and Boyen. Short signatures without random oracles. **EUROCRYPT 2004** [Google Scholar](https://scholar.google.com/scholar?q=Short+signatures+without+random+oracles)
> 核心思路：提出了基于q-SDH假设的短签名方案，同样利用双线性对。
> 局限与区别：该方案专注于签名本身的效率与长度，未提供对承诺值签名或证明知道签名的协议。本文的核心贡献在于后者。

[5] Boneh, Boyen and Shacham. Short group signatures using strong Diffie-Hellman. **CRYPTO 2004** [Google Scholar](https://scholar.google.com/scholar?q=Short+group+signatures+using+strong+Diffie-Hellman)
> 核心思路：构造了一个基于强Diffie-Hellman假设和线性假设的短群签名方案。
> 局限与区别：该方案的凭证并非严格意义上的可盲签名，且不支持与匿名凭证系统同等的灵活性。本文指出其方案可通过类似扩展获得等价功能。

[1] Ateniese et al. A practical and provably secure coalition-resistant group signature scheme. **CRYPTO 2000** [Google Scholar](https://scholar.google.com/scholar?q=A+practical+and+provably+secure+coalition-resistant+group+signature+scheme)
> 核心思路：基于强RSA假设构造群签名方案，具有抗合谋攻击性。
> 局限与区别：依赖强RSA假设，且证明协议中涉及大模数群上的表示知识证明，效率较低。

[19] Cramer and Shoup. Signature schemes based on the strong RSA assumption. **ACM CCS 1999** [Google Scholar](https://scholar.google.com/scholar?q=Signature+schemes+based+on+the+strong+RSA+assumption)
> 核心思路：提出了标准模型下基于强RSA假设的安全签名方案。
> 局限与区别：效率虽高，但底层假设与离散对数类假设完全不同，且不直接支持匿名凭证所需的盲协议。

[21] Fiat and Shamir. How to prove yourself: Practical solution to identification and signature problems. **CRYPTO 1986** [Google Scholar](https://scholar.google.com/scholar?q=How+to+prove+yourself+Practical+solution+to+identification+and+signature+problems)
> 核心思路：引入了随机预言机模型下的签名范式（Fiat-Shamir变换）。
> 局限与区别：随机预言机模型在标准模型中无法实例化，因此其安全证明在现实中是启发式的。

### 核心技术与方案

**1. 基础签名方案（方案A）**  
从授权者角度看，由Setup算法生成双线性群参数，密钥为$(x, y)$，公钥为$(X=g^x, Y=g^y)$。对消息$m$签名时，选择随机$a \in G$，计算$b=a^y$和$c=a^{x + m x y}$，输出$\sigma=(a, b, c)$。验证方程利用双线性映射$e(\cdot,\cdot)$：
- $e(a, Y) = e(g, b)$
- $e(X, a) \cdot e(X, b)^m = e(g, c)$

安全性依赖于LRSW假设：伪造一个合格签名需要在不查询$x$或$y$的情况下输出一个合法的$(a, a^y, a^{x+mxy})$三元组，这与假设矛盾。该方案是后续C方案的特例（$\ell=0$）。

**2. 盲化签名方案（方案C）**  
为支持对承诺值的签名，方案C将单消息$m$扩展为消息块$(m^{(0)}, \ldots, m^{(\ell)})$，其对应的私钥包含多个$z_i$。签名构造加入中间辅助元素：  
- 选择随机$a$，计算$A_i = a^{z_i}$、$b=a^y$、$B_i = A_i^y$；
- 核心元素$c = a^{x + x y m^{(0)}} \prod_{i=1}^\ell A_i^{x y m^{(i)}}$。  
验证方程相应地扩展为多个配对等式。关键特性是，若$m^{(0)}$被选为随机盲化因子，则签名中$c$的计算仅需要用户提供的聚合值$M= g^{m^{(0)}} \prod Z_i^{m^{(i)}}$，而对用户而言$M$信息论意义上隐藏了其他消息。

**3. 获取对承诺值的签名协议（§4.2）**  
用户持有消息块$(m^{(0)}, \ldots, m^{(\ell)})$并计算承诺$M$。用户首先通过邹鸣知识证明（PK协议）向签名者证明知道$M$的正确打开：
$$PK\{(\mu^{(0)}, \ldots, \mu^{(\ell)}): M = g^{\mu^{(0)}} \prod_{i=1}^{\ell} Z_i^{\mu^{(i)}}\}$$
之后签名者凭$M$计算$c = a^x M^{\alpha x y}$（其中$a=g^\alpha$），用户获得签名$(a, \{A_i\}, b, \{B_i\}, c)$。定理3指出该协议在安全两方计算意义下安全：签名者只学到$M$（而非具体消息），而用户获得合法签名。

**4. 证明知道签名的协议（§4.3，方案D）**  
为了在不泄露签名本身的情况下证明持有签名，协议首先对签名元素做随机盲化：选择随机$r, r'$，将$(a, \{A_i\}, b, \{B_i\}, c)$盲化为$(\tilde{a}, \{\tilde{A}_i\}, \tilde{b}, \{\tilde{B}_i\}, \hat{c})$，其中$\hat{c}= c^{r r'}$。然后用户和挑战者共同计算辅助值$v_x = e(X, \tilde{a}), v_{xy}= e(X, \tilde{b}), V_{(xy,i)}=e(X, \tilde{B}_i), v_s = e(g, \hat{c})$，并执行PK：
$$PK\{(\mu^{(0)}, \ldots, \mu^{(\ell)}, \rho): (v_s)^\rho = v_x (v_{xy})^{\mu^{(0)}} \prod_{i=1}^{\ell} (V_{(xy,i)})^{\mu^{(i)}}\}$$
验证者额外检查配对关系$e(\tilde{a}, Z_i)=e(g, \tilde{A}_i)$以及$e(\tilde{a}, Y)=e(g, \tilde{b})$、$e(\tilde{A}_i, Y)=e(g, \tilde{B}_i)$。定理6证明该协议是完备的、可靠的（提取获得签名）且零知识。

**5. 群签名方案构造（§4.4）**  
方案采用标准结构：管理员密钥同方案A，撤销管理员使用Cramer-Shoup加密。用户加入时秘密选择$k$，计算$P=g^k$，获得管理员对$P$的签名$(a,b,c)$。签名时，用户盲化签名得到$(\tilde{a},\tilde{b},\hat{c})$，用撤销管理员公钥加密$P$得到密文$(c_1, c_2, c_3, c_4)$，然后通过Fiat-Shamir启发式将以下证明转化为签名：
$$SPK\{(\mu, \rho, \upsilon): v_s^\rho = v_x v_{xy}^\mu \wedge c_1=g^\upsilon \wedge c_2=h^\upsilon \wedge c_3={\sf y}_1^\upsilon {\sf g}^\mu \wedge c_4=({\sf y}_2 {\sf y}_3^{{\cal H}(c_1\|c_2\|c_3)})^\upsilon\}(m)$$
方案安全性基于LRSW假设和判别性Diffie-Hellman假设，在随机预言机模型中可证。

**渐进复杂度**：方案B/D的签名大小为$(\ell+3)$个$G$元素加1个$\sf G$元素（方案D还加入$\ell$个$W_i$公钥）。零知识证明协议通信量为$O(\ell)$个群元素加上配对运算。对于典型参数（$\ell=1$），通信量约为数千比特量级，远优于基于强RSA的方案（通常需要模2k比特的大模数上的证明）。

### 核心公式与流程

**[方案A验证方程]**
$$
e(a, Y) = e(g, b) \quad \text{ and } \quad e(X, a) \cdot e(X, b)^m = e(g, c).
$$
> 作用：验证方案A的签名$(a,b,c)$对消息$m$有效。

**[方案C签名构成（无证明）]**
$$
c = a^{x + x y m^{(0)}} \prod_{i=1}^{\ell} A_i^{x y m^{(i)}}.
$$
> 作用：在签名方案C中构造与消息块绑定的核心元素$c$。

**[证明知道签名的核心PK]**
$$
PK\{(\mu^{(0)}, \ldots, \mu^{(\ell)}, \rho): (v_s)^\rho = v_x (v_{xy})^{\mu^{(0)}} \prod_{i=1}^{\ell} (V_{(xy,i)})^{\mu^{(i)}}\}
$$
> 作用：在§4.3协议中，证明知道盲化后的签名$\hat{c}$满足与公钥元素的特定关系，从而证明持有原签名。

**[群签名的SPK]**
$$
\Sigma = SPK\{(\mu, \rho, \upsilon): v_s^\rho = v_x v_{xy}^\mu \wedge c_1 = g^\upsilon \wedge c_2 = h^\upsilon \wedge c_3 = {\sf y}_1^\upsilon {\sf g}^\mu \wedge c_4 = ({\sf y}_2 {\sf y}_3^{{\cal H}(c_1\|c_2\|c_3)})^\upsilon\}(m)
$$
> 作用：群签名中，用户将加密的身份和签名知识证明一起进行Fiat-Shamir变换，形成不可伪造的匿名签名。

### 实验结果
论文本身未提供独立的实验章节，但明确给出了与现有方案的对比分析。方案A（以及由它派生的方案B/C/D）在签名尺寸上相当：签名由3个$G$元素组成（约400-600比特）对于128位安全级别。群签名方案的总签名尺寸包括盲化签名$(3G)$、Cramer-Shoup密文$(4{\sf G})$外加一个SPK证明签名（约3-4个域元素），总计约2-2.5k比特，远小于基于强RSA的群签名（通常需要两到三倍于RSA模长的组合证明）。计算方面，签名验证需要2-3个配对运算，证明协议需要约$(\ell+3)$次配对。对于参数规模$q$为256比特、椭圆曲线实现场景，配对运算约为毫秒级，使得方案在实际系统中可行。特别值得注意的是，本文的方案是首个基于纯离散对数假设（LRSW）达到与强RSA方案类似效率的设计，且支持匿名凭证所需的盲签名协议。

### 局限性与开放问题
论文的安全证明中，用于群签名的部分依赖于随机预言机模型（通过Fiat-Shamir启发式），而基本签名方案本身是在标准模型下可证的。如何在标准模型下同时实现群签名方案的匿名性和可追溯性，是一个开放问题。此外，LRSW假设虽然在一般群模型中成立，但目前为止尚未获得广泛密码学分析的积累，相较于强RSA假设更为新颖，实际安全性需进一步检验。扩展方案还要求群支持双线性对，这限制了底层群的选择（主要是特定椭圆曲线），导致实现灵活性降低。

### 强关联论文

[30] Lysyanskaya et al. Pseudonym systems. **SAC 1999** [Google Scholar](https://scholar.google.com/scholar?q=Pseudonym+systems)

[4] Boneh and Boyen. Short signatures without random oracles. **EUROCRYPT 2004** [Google Scholar](https://scholar.google.com/scholar?q=Short+signatures+without+random+oracles)

[5] Boneh, Boyen and Shacham. Short group signatures using strong Diffie-Hellman. **CRYPTO 2004** [Google Scholar](https://scholar.google.com/scholar?q=Short+group+signatures+using+strong+Diffie-Hellman)

[10] Camenisch and Lysyanskaya. A signature scheme with efficient protocols. **SCN 2002** [Google Scholar](https://scholar.google.com/scholar?q=A+signature+scheme+with+efficient+protocols)

[1] Ateniese et al. A practical and provably secure coalition-resistant group signature scheme. **CRYPTO 2000** [Google Scholar](https://scholar.google.com/scholar?q=A+practical+and+provably+secure+coalition-resistant+group+signature+scheme)

[19] Cramer and Shoup. Signature schemes based on the strong RSA assumption. **ACM CCS 1999** [Google Scholar](https://scholar.google.com/scholar?q=Signature+schemes+based+on+the+strong+RSA+assumption)

[21] Fiat and Shamir. How to prove yourself: Practical solution to identification and signature problems. **CRYPTO 1986** [Google Scholar](https://scholar.google.com/scholar?q=How+to+prove+yourself+Practical+solution+to+identification+and+signature+problems)

[11] Camenisch and Shoup. Practical verifiable encryption and decryption of discrete logarithms. **CRYPTO 2003** [Google Scholar](https://scholar.google.com/scholar?q=Practical+verifiable+encryption+and+decryption+of+discrete+logarithms)

[18] Cramer and Shoup. A practical public key cryptosystem provably secure against adaptive chosen ciphertext attack. **CRYPTO 1998** [Google Scholar](https://scholar.google.com/scholar?q=A+practical+public+key+cryptosystem+provably+secure+against+adaptive+chosen+ciphertext+attack)

[12] Camenisch and Stadler. Efficient group signature schemes for large groups. **CRYPTO 1997** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+group+signature+schemes+for+large+groups)


## 关键词

+ LRSW假设双线性映射签名
+ 标准模型可证明安全签名
+ 匿名凭证系统群签名身份托管
+ 零知识承诺签名知识证明
+ 通用双线性群签名方案