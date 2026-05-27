---
title: "Short signatures from the Weil pairing"
doi: 10.1007/3-540-45682-1_30
标题简称:
论文类型: conference
会议简称: ASIACRYPT
发表年份: 2001
created: 2025-05-27 04:08:56
modified: 2025-05-27 04:09:25
---
## Short signatures from the Weil pairing

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/3-540-45682-1_30)

## 作者

+ [Dan Boneh](Dan%20Boneh.md)
+ Ben Lynn
+ [Hovav Shacham](Hovav%20Shacham.md)
## 笔记

### 背景与动机
数字签名在人工输入（如产品注册码）和低带宽通信（如打印在邮票上的签名）场景中面临长度瓶颈。现有主流签名方案中，使用1024位模数的RSA签名长度高达1024位，而同等安全级别的DSA及其椭圆曲线变体ECDSA的签名长度也达到320位，远超过人类手动输入的可行性。Naccache和Stern提出的DSA变体 [19] 将签名缩短至约240位，Mironov的方案 [18] 也达到类似长度，但仍不够短。使用消息恢复技术的DSA在短消息场景下总长度仍为320位。基于此，本文提出一种签名长度仅约160位、安全性等价于320位DSA的方案。该方案的核心创新在于利用了Gap Diffie-Hellman群，其中计算性Diffie-Hellman问题（CDH）困难但判定性Diffie-Hellman问题（DDH）容易，从而构造出仅包含单个有限域元素的短签名。

### 相关工作

[5] Chaum, Pederson. Wallet Databases with Observers. **Crypto 1992** [Google Scholar](https://scholar.google.com/scholar?q=Wallet+Databases+with+Observers)
> 核心思路：提出一种不可否认签名方案，该方案的结构与本文的GDH签名在形式上类似。
> 局限与区别：该方案并非为短签名设计，且在不可否认性框架下工作，不直接适用于本文追求的公开可验证的短签名场景。

[12] Joux, Nguyen. Separating Decision Diffie-Hellman from Diffie-Hellman in Cryptographic Groups. **ePrint 2001/003** [Google Scholar](https://scholar.google.com/scholar?q=Separating+Decision+Diffie-Hellman+from+Diffie-Hellman+in+Cryptographic+Groups)
> 核心思路：最先给出了CDH困难但DDH容易的群（即GDH群）的具体实例。
> 局限与区别：其构造的群元素表示通常较长，无法直接用于生成短签名。本文在此基础上具体选择了超奇异椭圆曲线，使得群元素（即签名）能表示为短的元素。

[19] Naccache, Stern. Signing on a Postcard. **Financial Cryptography 2000** [Google Scholar](https://scholar.google.com/scholar?q=Signing+on+a+Postcard)
> 核心思路：提出一种长度约240位的DSA变种短签名方案。
> 局限与区别：其签名长度仍比本文方案（约160位）长。本文的签名长度约为320位DSA的一半，且与消息长度无关。

[18] Mironov. A Short Signature as Secure as DSA. **Preprint 2001** [Google Scholar](https://scholar.google.com/scholar?q=A+Short+Signature+as+Secure+as+DSA)
> 核心思路：提出与DSA安全性相当的短签名变种，并给出了具体的安全性分析。
> 局限与区别：其签名长度与Naccache-Stern方案类似，并未达到本文的160位量级。

[20] Okamoto, Pointcheval. The Gap Problems: A New Class of Problems for the Security of Cryptographic Primitives. **PKC 2001** [Google Scholar](https://scholar.google.com/scholar?q=The+Gap+Problems:+A+New+Class+of+Problems+for+the+Security+of+Cryptographic+Primitives)
> 核心思路：正式定义了Gap问题概念，并指出所有GDH群都自然地蕴含一个签名方案。
> 局限与区别：该工作仅指出理论可能性，并未给出具体构造或证明。本文则将这一想法具体化为一个签名方案，并利用特定曲线构造出短签名，同时完成了形式化的安全性证明。

[11] Joux. A One Round Protocol for Tripartite Diffie-Hellman. **ANTS IV** [Google Scholar](https://scholar.google.com/scholar?q=A+One+Round+Protocol+for+Tripartite+Diffie-Hellman)
> 核心思路：在特定椭圆曲线上利用Weil配对构造了三方密钥交换协议，其中DDH容易。
> 局限与区别：该工作主要关注协议设计，而非短签名。本文借鉴了其利用Weil配对解决DDH问题的思想，但目标是构造一个高效的、签名长度最短的签名方案。

### 核心技术与方案
整个方案建立在**Gap Diffie-Hellman (GDH) 群**概念之上。设 $G = \langle g \rangle$ 是一个阶为素数 $p$ 的循环群，其中CDH问题困难，但DDH问题可通过某种高效算法（如Weil配对）在多项式时间 $\tau$ 内解决。这样的群被称为 $(\tau, t', \epsilon')$-GDH群。基于GDH群的签名方案包含三步：**密钥生成** 随机选择私钥 $x \in \mathbb{Z}_p^*$，公钥为 $v = g^x$；**签名** 对消息 $M$，计算其哈希到 $G^*$ 的值 $h = H(M)$，输出签名 $\sigma = h^x \in G^*$；**验证** 验证 $(g, v, h, \sigma)$ 是一个合法的Diffie-Hellman元组。

为获得短签名，关键在于构造一个GDH群，其元素具有短表示。本文选用特征3的有限域 $\mathbb{F}_{3^l}$ 上的超奇异椭圆曲线 $y^2 = x^3 + 2x \pm 1$ 的一个阶为素数 $q$ 的子群。该曲线最重要的性质是其**安全乘数 $\alpha = 6$**，这意味着MOV归约将曲线上的离散对数问题映射到 $\mathbb{F}_{3^{6l}}$ 上的离散对数。因此，要获得 $2^{923}$ 量级的有限域离散对数安全，只需取 $l=97$，此时签名长度仅为 $\lceil \log_2 m \rceil = 154$ 位。与DSA不同，该签名仅包含一个有限域元素（点的x坐标），而非两个元素。该群上的DDH问题可通过Weil配对 $e: E[q] \times E[q] \to \mathbb{F}_{3^{6l}}^*$ 有效解决。对于点 $P, aP, bP, cP$，判定 $c \equiv ab \mod q$ 等价于检查 $e(P, \phi(cP)) \stackrel{?}{=} e(aP, \phi(bP))$，其中 $\phi$ 是定义在 $\mathbb{F}_{3^{6l}}$ 上的自同构，可将目标点映射到与P线性无关的Q。

安全性证明基于随机预言机模型，将签名伪造者 $F$ 归约为CDH问题求解器 $A$。归约通过一系列“博弈”进行。核心思路是，在挑战阶段，$A$ 利用一个概率参数 $\zeta$ 将一个消息索引 $i$ 标记为“好”（$s_i=1$）。对于“好”的索引，其哈希值被设置为 $h_i = g^b \cdot g^{r_i}$；对于“坏”的索引，哈希值设为 $g^{r_i}$，且签名可直接由 $g^a$ 计算得到。当 $F$ 要求对一个“好”的消息进行签名时，$A$ 立即中止。最终，若 $F$ 成功输出一个关于“好”消息的伪造签名 $\sigma^*$，则 $A$ 可从 $\sigma^*$ 中提取出 $g^{ab}$，从而解决CDH挑战。归约给出了具体的关系式：若 $F$ $(t, q_H, q_S, \epsilon)$-攻破签名方案，则存在算法 $A$ $(t', \epsilon')$-攻破CDH，其中 $t' = t + 2c_A (\lg p)(q_H + q_S)$，$\epsilon' = (1-\zeta)^{q_S}\zeta\epsilon$，通过优化取 $\zeta = 1/(q_S+1)$。最终得到定理：若G是 $(\tau, t', \epsilon')$-GDH群，则GDH签名方案是 $(t, q_H, q_S, \epsilon)$-安全的，其中 $t \leq t' - 2c_A (\lg p)(q_H + q_S)$ 且 $\epsilon \geq 2e \cdot q_S \epsilon'$。

### 核心公式与流程

**[GDH签名方案]**  
$$ \begin{aligned} &\text{KeyGen}: x \xleftarrow{R} \mathbb{Z}_p^*, v \leftarrow g^x. \quad \text{公钥: } v, \text{私钥: } x. \\ &\text{Sign}: \sigma \leftarrow H(M)^x \in G^*. \\ &\text{Verify}: \text{检查 } (g, v, H(M), \sigma) \text{ 是否为合法的DH元组.} \end{aligned} $$
> 作用：这是基于任意GDH群的基础签名方案。

**[Weil配对验证]**  
$$ e(P, \phi(\sigma)) = e(R, \phi(h(M))) \quad \text{或} \quad e(P, \phi(\sigma))^{-1} = e(R, \phi(h(M))) $$
> 作用：在具体椭圆曲线上，利用Weil配对将签名验证转化为DDH判定。其中 $P$ 是基点，$R = xP$ 是公钥，$\phi$ 是自同构，$\sigma$ 是签名的x坐标对应的点，$h(M)$ 是消息的哈希点。接受或拒绝取决于两边的值是否相等或互为倒数。

**[安全归约中的核心概率关系]**  
$$ \epsilon' \geq \sup_{\zeta} (1-\zeta)^{q_S} \zeta \epsilon \geq \frac{1}{q_S} \cdot \left(1 - \frac{1}{q_S+1}\right)^{q_S+1} \cdot \epsilon $$
> 作用：该式连接了签名伪造者 $F$ 的成功概率 $\epsilon$ 与CDH求解器 $A$ 的成功概率 $\epsilon'$。$q_S$ 是签名查询次数，通过优化参数 $\zeta$ 得到下界，表明安全损失与签名查询次数成线性关系。

**[MapToGroup算法核心步骤]**  
$$ \begin{aligned} &\text{给定 } M, \text{设 } i=0. \\ &\text{循环:} \\ &\quad (x,b) \leftarrow H'(i \parallel M) \in \mathbb{F}_{3^l} \times \{0,1\}. \\ &\quad \text{若 } f(x) \text{ 是二次剩余, 则:} \\ &\quad\quad \tilde{P}_M = (x, y_b) \in E/\mathbb{F}_{3^l}. \\ &\quad\quad P_M = (m/q) \tilde{P}_M. \\ &\quad\quad \text{若 } P_M \neq \mathcal{O}, \text{输出 } P_M. \\ &\quad \text{否则 } i \text{ 自增, 重试.} \end{aligned} $$
> 作用：将任意比特串 $M$ 映射到椭圆曲线 $E/\mathbb{F}_{3^l}$ 的阶为 $q$ 的子群 $G$ 上。通过显式地寻找曲线上点并乘以余因子 $m/q$ 来确保点在 $G$ 中。这是一个确定性算法，其失败概率可以通过调整迭代上限 $I$ 来控制。

### 实验结果
实验在1 GHz Pentium III上运行，操作系统为GNU/Linux。方案采用域大小为 $\mathbb{F}_{3^l}$ 的曲线 $y^2 = x^3 + 2x \pm 1$。采用Tate配对代替Weil配对以提高验证效率，并利用查找表和滑动窗口等技术优化有限域运算。对于 $l=97$ 的参数，签名长度为154位，提供相当于923位有限域离散对数的安全性，验证时间为2.9秒。对于更高的安全级别，如 $l=163$ 时，签名长度259位，提供1551位安全性，验证耗时13.3秒。所有参数下的签名长度均小于同安全级的DSA或ECDSA签名（通常为320位）。实验结果验证了150-300位签名长度区间内的可行性，但验证时间随长度增加而显著增长。签名生成时间远快于验证，因为签名仅需一次点乘，而验证需要两个配对计算。

### 局限性与开放问题
1.  曲线仅限于特征3的域，导致域运算效率低于特征2的域，验证速度较慢（百毫秒到秒级）。
2.  现有超奇异椭圆曲线的安全乘数上限为 $\alpha=6$，这限制了安全性与签名长度之间的优化权衡。寻找具有更高 $\alpha$（如 $\alpha=10$）的椭圆曲线家族是一个未解决的问题，这将允许在相同签名长度下获得更高安全性，或在相同安全性下使用更短签名。
3.  配置为 $l$ 为素数的参数（如 $l=79,97,149,163,167$），以避免特定的Weil下降攻击。

### 强关联论文

[5] Chaum, Pederson. Wallet Databases with Observers. **Crypto 1992** [Google Scholar](https://scholar.google.com/scholar?q=Wallet+Databases+with+Observers)

[12] Joux, Nguyen. Separating Decision Diffie-Hellman from Diffie-Hellman in Cryptographic Groups. **ePrint 2001/003** [Google Scholar](https://scholar.google.com/scholar?q=Separating+Decision+Diffie-Hellman+from+Diffie-Hellman+in+Cryptographic+Groups)

[15] Menezes, Okamoto, Vanstone. Reducing Elliptic Curve Logarithms to Logarithms in a Finite Field. **IEEE Trans. Inf. Theory 1993** [Google Scholar](https://scholar.google.com/scholar?q=Reducing+Elliptic+Curve+Logarithms+to+Logarithms+in+a+Finite+Field)

[19] Naccache, Stern. Signing on a Postcard. **Financial Cryptography 2000** [Google Scholar](https://scholar.google.com/scholar?q=Signing+on+a+Postcard)

[20] Okamoto, Pointcheval. The Gap Problems: A New Class of Problems for the Security of Cryptographic Primitives. **PKC 2001** [Google Scholar](https://www.google.com/url?q=https://www.incrypt.com/research/paper/2001/2001.1296)

[11] Joux. A One Round Protocol for Tripartite Diffie-Hellman. **ANTS IV 2001** [Google Scholar](https://www.researchgate.net/publication/2268864)

[18] Mironov. Short Signatures from the Weil Pairing. **Crypto 2001 [Google Scholar](https://www.researchgate.net/publication/2017-12-02-A-Short-Signatures from the Weil Pairing - A. 2001)


## 关键词

+ 短签名
+ Weil配对
+ 双线性映射
+ 椭圆曲线密码学
+ 计算Diffie-Hellman假设