---
title: "Efficient zero-knowledge contingent payments in cryptocurrencies without scripts"
标题简称:
论文类型: conference
会议简称: ESORICS
发表年份: 2016
---

## Efficient zero-knowledge contingent payments in cryptocurrencies without scripts

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-319-45741-3_14)

## 作者

+ Wacław Banasik 
+ Stefan Dziembowski 
+ Daniel Malinowski 


## 笔记

### 背景与动机
比特币等加密货币支持“智能合约”，但实际应用受限，因为大多数矿工只接受标准交易，拒绝包含非平凡脚本的交易。比特币脚本语言不够灵活且存在交易可锻性漏洞，使得实现复杂合约困难。虽然以太坊支持图灵完备脚本，但存在安全性和激励问题。因此，一个重要的问题是：能否仅使用标准交易（即不需要非标准脚本）来构造非平凡的智能合约？本文对此给出肯定回答，构建了一个高效的零知识或有支付协议，适用于一类广泛的NP关系（特别是存在高效sigma协议的关系），例如出售RSA模数的分解。该协议无需通用安全多方计算或通用零知识方案，而是采用标准的cut-and-choose技术，结合时间锁承诺、Paillier同态加密和ECDSA签名，并保证在随机预言机模型下安全。

### 相关工作

[16] Bitcoin Wiki. *Zero Knowledge Contingent Payment*  
> 核心思路：描述了零知识或有支付的概念，允许买方通过脚本锁定资金，卖方提供见证后取得付款。  
> 局限与区别：该方案依赖非标准脚本，且易受交易可锻性攻击，同时使用通用零知识协议或仅适用于简单问题（如出售数独解）；本文使用更简单的cut-and-choose方法，并仅依赖标准交易。

[37] Rivest, R.L., Shamir, A., Wagner, D.A. *Time-lock puzzles and timed-release crypto*  
> 核心思路：提出时间锁承诺，允许承诺者通过计算困难问题在固定时间后强制打开承诺。  
> 局限与区别：本文将其用于强制买方在卖方不合作时取回资金，作为标准交易中无法直接实现“超时退款”的解决方案。

[35] Paillier, P. *Public-key cryptosystems based on composite degree residuosity classes*. **EUROCRYPT 1999**  
> 核心思路：提出具有加法同态性的公钥加密方案。  
> 局限与区别：本文利用同态性在分布式ECDSA签名生成中加密秘密份额，从而避免通用零知识证明。

[32] Nakamoto, S. *Bitcoin: A Peer-to-Peer Electronic Cash System*  
> 核心思路：比特币的基本协议。  
> 局限与区别：本文直接在比特币标准交易框架下工作，不对比特币核心协议提出修改。

[20] Damgard, I. *On Sigma-Protocols*  
> 核心思路：定义了Sigma协议，是一种高效的三轮零知识证明协议。  
> 局限与区别：本文对零知识证明的要求比Sigma协议更广（允许更多轮次，但提取器只依赖两个不同挑战），且要求抗恶意验证者；对于仅满足诚实验证者零知识的Sigma协议，可通过Fiat-Shamir变换转换为抗恶意验证者。

[8] Bellare, M., Goldreich, O. *On defining proofs of knowledge*. **CRYPTO 1992**  
> 核心思路：形式化了知识证明的定义。  
> 局限与区别：本文采用的知识提取性质基于两个不同挑战下的接受对话，属于较具体的提取机制。

[1] An, J.H., Dodis, Y., Rabin, T. *On the security of joint signature and encryption*. **EUROCRYPT 2002**  
> 核心思路：正式定义了强不可伪造签名（strong unforgeability）。  
> 局限与区别：本文假设ECDSA签名（经过“正s”限制后）满足强不可伪造性，这是协议安全的重要基础。

[39] Wuille, P. *Bitcoin Improvement Proposal 062: Dealing with malleability*  
> 核心思路：提议通过要求签名中s ≤ (p-1)/2来消除ECDSA签名的可锻性。  
> 局限与区别：本文直接采纳该规范，将ECDSA签名的强不可伪造性归约到该假设下。

[31] Maxwell, G. *The first successful Zero-Knowledge Contingent Payment*  
> 核心思路：实现了首个零知识或有支付（出售数独解）。  
> 局限与区别：该实现仍依赖非标准脚本；本文采用标准交易且支持更一般的NP关系。

[30] MacKenzie, P., Reiter, M.K. *Two-party generation of DSA signatures*. **Int. J. Inf. Secur. 2004**  
> 核心思路：提出了两方DSA签名生成协议，使用通用零知识证明。  
> 局限与区别：本文的分布式ECDSA生成协议（SharedKGen和KSignGen）避免了通用零知识，利用Paillier同态加密和cut-and-choose实现高效安全。

### 核心技术与方案
本文的整体框架分为三层子协议：两方ECDSA密钥生成协议（SharedKGen）、唯一签名生成协议（USG）和卖见证协议（SellWitnessf）。核心思想是让买方创建一个多签交易T1，将资金锁定到b个卖方公钥和b-1个买方公钥（共2b-1个密钥）。然后双方共同签名一个将资金转给卖方的交易T2。卖方获得对T2的b个有效签名（每个对应一个共享密钥），但T1未发布时她无法使用这些签名。卖方将每个签名的哈希值（通过随机预言机F）有承诺，同时将她的秘密份额通过时间锁承诺提交给买方。随后，卖方和买方执行一个基于cut-and-choose的零知识证明，证明她知道见证x（满足f(x)=true）。具体地，对于b个秘密中的每一个（索引i），双方运行2λ次SetupF，卖方对每个挑战（0和1）生成响应，并用秘密S^i,j作为对称密钥加密响应。买方随机选择λ个索引进行挑战验证，其余索引卖方打开两个加密的响应（但不打开秘密S）。若验证通过，买方发布T1。若卖方随后发布签名，买方可以从中恢复S^i,j，解密响应，并利用ExtractF从两个不同挑战的响应中提取见证x。若卖方不发布签名，买方在时间τ1后强制打开时间锁承诺，获取卖方的秘密份额，从而恢复完整的签署密钥，签署一个新交易将资金转回给自己。

安全性证明的思路：对于恶意卖方，她成功欺骗买方的概率（即不泄露x却能拿到钱）受限于两个cut-and-choose阶段的错误概率。USG阶段的错误概率为(b/a)^b；零知识证明阶段的错误概率在λ上可忽略。对于恶意买方，他必须在时间τ0之前获得一个有效签名或任何关于秘密S^i,j的信息；否则，时间锁承诺保证他无法在时间内强制打开。协议的安全性依赖以下假设：Paillier同态加密是语义安全的，随机预言机模型（用于承诺和F），时间锁承诺是(τ0, τ1)-安全的，ECDSA（经过正s限制后）是强不可伪造的。协议的计算复杂度：USG阶段的时间与a成正比，零知识阶段的时间与b·2λ成正比，通信量约为60 MB。对于推荐参数a=512, b=8, λ=1024，总计算时间约1分钟（单线程）。

### 核心公式与流程

**[USG协议中的KSignGen过程（图3）]**
$$
\begin{aligned}
&\text{双方计算} K = k_S \cdot k_B \cdot g,\ r = x(K) \bmod |\mathbb{G}|\\
&\text{卖方：}(pk_{AH},sk_{AH}) \leftarrow \text{AddHomGen}(1^\lambda),\ c_S = \text{AddHomEnc}_{pk_{AH}}(d_S)\\
&\text{买方：} c_0 = (k_B)^{-1} \cdot H(z) \bmod |\mathbb{G}|,\ c_1 = \text{AddHomEnc}_{pk_{AH}}(c_0),\\
&\quad t = (k_B^{-1})\cdot r \cdot d_B \bmod |\mathbb{G}|,\ c_2 = c_1 \otimes (c_S)^t\\
&\quad \text{取样} u \leftarrow \{1,\dots,|\mathbb{G}|^2\},\ c_B = c_2 \otimes \text{AddHomEnc}_{pk_{AH}}(u\cdot|\mathbb{G}|)\\
&\text{卖方：} s_0 = \text{AddHomDec}_{sk_{AH}}(c_B),\ s = (k_S)^{-1}\cdot s_0 \bmod |\mathbb{G}|\\
&\quad \sigma = (r,s),\ S = F(\sigma),\ \Gamma = \text{Commit}(S),\ \Phi = \text{TLCommit}(d_S)
\end{aligned}
$$
> 作用：在双方不暴露各自秘密份额的情况下，生成对消息z的ECDSA签名σ，并让卖方承诺其哈希值S，同时时限承诺其秘密份额d_S。

**[卖见证协议（图4）中提取见证的步骤（第5步）]**
$$
x' = \text{Extract}_{\mathcal{F}}(B_{\mathcal{F}}^{i,j}, c_1^{i,j}, r_1^{i,j}, c_2^{i,j}, r_2^{i,j})
$$
> 作用：当买方获得签名σ后，可计算S^{i,j}=F(σ)，解密得到两个不同挑战(c_1,r_1)和(c_2,r_2)，利用知识证明的提取函数得到见证x'。

**[作弊概率公式]**
$$
\epsilon = \left(\frac{b}{a}\right)^b
$$
> 作用：在USG阶段，恶意卖方成功破坏至少b个密钥（即未被发现的错误）的概率上界。对于a=512, b=8，ϵ = (8/512)^8 = 2^{-48}。

### 实验结果
实验实现使用C++（Crypto++库）和Java（bitcoinj库），通信通过Apache Thrift。运行在单机本地测试链上。参数：RSA模数素数约512比特，设置a=512, b=8, λ=1024，因此USG阶段需运行a=512次SharedKGen和KSignGen，零知识阶段需运行b·2λ=8×2048=16384次SetupF。总运行时间约1分钟（其中USG约33秒，第二步约28秒）。作弊概率为(b/a)^b=2^{-48}。通信量约60 MB，共12轮。论文还评估了不同参数下的性能：当b=1（单一签名）且λ=1024时，USG阶段时间与a线性增长（a=128时10秒，a=1024时70秒），作弊概率相应变化；当b=8时，使用多签交易最多允许b=8（因为Bitcoin标准多签最多支持15个公钥），安全性显著提升。第二步时间与b·λ成正比，对于b=8, λ=1024，时间约32秒。考虑到真实区块链延迟（两笔交易确认约2小时），论文建议设置τ0=5小时，τ1=50小时，时间锁承诺难度t=2^37（基于约2^19次平方/秒的估算）。

### 局限性与开放问题
协议依赖时间锁承诺，需要保守估计τ0和τ1，这引入了额外的等待时间（可能长达50小时），不适合高频或低延迟场景。通信量较大（约60 MB），对于带宽受限网络可能不实用。协议安全性依赖多个假设（随机预言机、Paillier语义安全、时间锁承诺、ECDSA强不可伪造性），任何假设被打破都会影响安全性。目前仅适用于存在高效sigma协议的NP关系，对于更复杂的关系可能需要更通用的零知识证明系统。另外，实验中仅实现了单线程版本，多线程优化可以显著减少运行时间。

### 强关联论文

[16] Bitcoin Wiki. *Zero Knowledge Contingent Payment* [Google Scholar](https://scholar.google.com/scholar?q=Zero+Knowledge+Contingent+Payment)

[37] Rivest, R.L., Shamir, A., Wagner, D.A. *Time-lock puzzles and timed-release crypto* [Google Scholar](https://scholar.google.com/scholar?q=Time-lock+puzzles+and+timed-release+crypto)

[35] Paillier, P. *Public-key cryptosystems based on composite degree residuosity classes*. **EUROCRYPT 1999** [Google Scholar](https://scholar.google.com/scholar?q=Public-key+cryptosystems+based+on+composite+degree+residuosity+classes)

[32] Nakamoto, S. *Bitcoin: A Peer-to-Peer Electronic Cash System* [Google Scholar](https://scholar.google.com/scholar?q=Bitcoin%3A+A+Peer-to-Peer+Electronic+Cash+System)

[20] Damgard, I. *On Sigma-Protocols* [Google Scholar](https://scholar.google.com/scholar?q=On+Sigma-Protocols)

[30] MacKenzie, P., Reiter, M.K. *Two-party generation of DSA signatures*. **Int. J. Inf. Secur. 2004** [Google Scholar](https://scholar.google.com/scholar?q=Two-party+generation+of+DSA+signatures)

[31] Maxwell, G. *The first successful Zero-Knowledge Contingent Payment* [Google Scholar](https://scholar.google.com/scholar?q=The+first+successful+Zero-Knowledge+Contingent+Payment)

[39] Wuille, P. *Bitcoin Improvement Proposal 062: Dealing with malleability* [Google Scholar](https://scholar.google.com/scholar?q=Bitcoin+Improvement+Proposal+062%3A+Dealing+with+malleability)

[8] Bellare, M., Goldreich, O. *On defining proofs of knowledge*. **CRYPTO 1992** [Google Scholar](https://scholar.google.com/scholar?q=On+defining+proofs+of+knowledge)

[1] An, J.H., Dodis, Y., Rabin, T. *On the security of joint signature and encryption*. **EUROCRYPT 2002** [Google Scholar](https://scholar.google.com/scholar?q=On+the+security+of+joint+signature+and+encryption)


## 关键词

+ 零知识条件支付
+ 无脚本智能合约
+ 比特币标准交易
+ NP关系与Sigma协议
+ 跨链交易