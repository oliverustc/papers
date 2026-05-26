---
title: "Reef: Fast Succinct Non-InteractiveZero-Knowledge Regex Proofs"
标题简称:
论文类型: conference
会议简称: USENIX Security
发表年份: 2024
created: 2025-04-21 10:58:41
modified: 2025-04-23 15:46:35
---

## Reef: Fast Succinct Non-InteractiveZero-Knowledge Regex Proofs

## 发表信息

+ [原文链接](https://www.usenix.org/conference/usenixsecurity24/presentation/angel)
+ [code](https://github.com/eniac/Reef)

## 作者

+ Sebastian Angel 
+ Eleftherios Ioannidis 
+ Elizabeth Margolin 
+ [Srinath Setty](Srinath%20Setty.md) 
+ Jess Woods 

## 笔记

### 背景与动机
正则表达式被广泛用于文本模式匹配，但在许多场景下，文档持有者希望在不泄露文档内容的前提下，向验证者证明文档匹配或不匹配某个正则表达式。例如，用户可以向服务器证明密码满足强度策略，而无需暴露密码本身；记者可以证明经过涂改的邮件原始DKIM签名有效；网络管理员可以要求客户端证明DNS查询不包含恶意域名；用户可证明其基因组DNA序列包含特定变异。然而，将这些场景转化为高效的零知识证明面临核心挑战：如何在不读取整个文档的情况下，对“文档匹配正则表达式”这一计算进行安全、高效的算术化。现有工作（如基于DFA的ZK-Email [11]或基于Thompson NFA的Zombie [79]和ZK-Regex [56]）在算术化过程中需要遍历文档的全部字符，导致约束数量与文档长度成正比，且不支持前瞻等常见的PCRE语法。Reef旨在填补这一空白，它通过引入一种新型自动机（SAFA），利用NP检查器的思想，将“计算匹配”转变为“验证匹配”，从而在大规模文档和复杂正则表达式的场景下实现高效、公开可验证的零知识证明。

### 相关工作

[11] Zk email verify. **USENIX Security 2023** [Google Scholar](https://scholar.google.com/scholar?q=Zk+email+verify)
> 核心思路：将正则表达式编译为DFA，并算术化其转移函数，通过逐字符读取文档来证明匹配。
> 局限与区别：约束数量为$O(|D|\cdot |Q_{DFA}|\cdot |\Sigma|)$，无法处理带有前瞻的PCRE语法，且在大文档上内存和时间开销极高。

[79] Zhang et al. Zombie: Middleboxes that don’t snoop. **NSDI 2024** [Google Scholar](https://scholar.google.com/scholar?q=Zombie+Middleboxes+that+don%27t+snoop)
> 核心思路：使用Thompson NFA进行算术化，约束数量为$O(|D|\cdot |Q_{TNFA}|)$，并通过优化NFA的表示来提升效率。
> 局限与区别：不支持前瞻（lookaround）和否定字符类，其自动机的表示仍然与文档长度线性相关，且缺乏跳过无关字符的能力。

[56] Luo et al. Privacy-preserving regular expression matching using nondeterministic finite automata. **CCS 2023** [Google Scholar](https://scholar.google.com/scholar?q=Privacy-preserving+regular+expression+matching+using+nondeterministic+finite+automata)
> 核心思路：同样基于Thompson NFA进行算术化，约束数量为$O(|D|\cdot |Q_{TNFA}|)$。
> 局限与区别：不支持前瞻、否定字符类以及非匹配证明（non-match），其算术化方法无法利用文档中的“跳过”机会。

[64] Raymond et al. Efficient zero knowledge for regular language. **USENIX Security 2024** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+zero+knowledge+for+regular+language)
> 核心思路：基于Aho-Corasick DFA进行字符串匹配，约束数量为$O(|D|+|Q_{ADFA}|)$。
> 局限与区别：仅支持固定字符串集合的匹配，不支持如`ab*c`这样的无界重复、通配符范围或否定字符类，在包含通配符范围时会导致状态指数级爆炸。

[51] Kothapalli and Setty. HyperNova: recursive arguments for customizable constraint systems. **CRYPTO 2024** [Google Scholar](https://scholar.google.com/scholar?q=HyperNova+recursive+arguments+for+customizable+constraint+systems)
> 核心思路：提出了nlookup查找参数，用于在递归证明系统中高效地证明多个值属于一个公开或承诺的表格。
> 局限与区别：Reef在其基础上通过表投影和混合表技术进行深度定制，以支持文档的私有访问和跳过。

### 核心技术与方案

Reef的整体框架包含三个角色：承诺者（通常与证明者相同）、证明者和验证者。承诺者使用多项式承诺对文档进行承诺，证明者随后证明该承诺对应的文档匹配或不匹配某个公开的正则表达式。核心技术创新体现在以下两个层面。

**Skipping Alternating Finite Automata**。Reef引入了一种全新的自动机SAFA，其核心设计在于将传统自动机（DFA/NFA/AFA）的“计算”视角转变为“验证”视角。SAFA在交替有限自动机（AFA）的基础上增加了跳过（skip）的概念。跳过是一组非重叠的区间，例如$S=\{[2,6]\}$表示跳过2到6个字符。当SAFA处于一个具有跳过转移的状态时，证明者可以非确定性地将游标向前移动任意一个落在该区间内的步长，而不必读取和验证这些字符的具体内容。这一特性对于包含通配符（如`.{100}`）或Kleene星（`.*`）的正则表达式尤为关键，它使得证明者能够跳过大量无关的文档内容。SAFA中表示量词的$\forall$状态允许在并行分支中独立地移动游标，从而完美支持前瞻（lookahead）语法。理论上，SAFA与AFA在表达能力上等价，即语言类仍是正则语言，但SAFA在验证场景下能极大地压缩算术化的规模。

**递归证明与查找参数的整合**。Reef利用递归SNARK（如Nova [52]）将整个匹配过程分解为多个步骤的证明，每一步执行一个`match_step`函数。该函数通过nlookup [51]查找参数来访问两种表格：一个是公开的SAFA转移表，用于根据当前状态和游标移动量确定下一状态；另一个是私有的文档表，用于读取特定位置的字符。为了最小化开销，Reef将这两个表格合并为一个混合表，利用多项式承诺的线性同态性质，使验证者能够通过公开的转移表信息和关于文档承诺的证据来验证整体的查询。此外，Reef引入了表投影技术，当文档的某些区域是公开已知的时（如DNA的特定基因位点），证明者可以只在一个更小的投影表上运行sum-check协议，从而将昂贵的、与文档大小成线性关系的场运算限制在投影表的大小上，显著提升性能。整个系统最终提供了完备性、知识可靠性、零知识性和公开可验证性。

### 核心公式与流程

**[SAFA的跳过转移定义]**
$$S = \{[start, end]\} \quad \text{或} \quad S = \{[start, \infty)\}$$
> 作用：定义了SAFA中跳过操作的核心概念。一个跳过转移允许证明者将游标从当前位置向前移动任意一个属于集合$S$中某个整数区间内的步长，从而跳过对这一段文档内容的验证。

**[nlookup的核心验证等式]**
$$\sum_{i=1}^m \rho^i \cdot v_i = \sum_{i=1}^m \rho^i \cdot \sum_{j \in \{0,1\}^\ell} \widetilde{eq}(q_i, j) \cdot \widetilde{T}(j)$$
> 作用：这是nlookup查找参数的核心等式，用于证明一组值$\{v_i\}$都属于一个大小为$2^{\ell}$的公开表格$T$。等式的右侧通过sum-check协议进行验证，最终将多个查询归约为对多项式$\widetilde{T}$在单个点上的评估。

**[混合表的构建与验证]**
$$\widetilde{T}(q_r) = (1 - q_r[0]) \cdot \widetilde{S}(q_r[1..]) + q_r[0] \cdot \widetilde{\mathsf{D}}(q_r[1..]) = \nu_r$$
> 作用：该公式描述了Reef如何将公开的SAFA转移表（$S$）和私有的文档表（$\mathsf{D}$）合并成一个混合表$T$。验证者通过该等式将最终的评估声明分解为对公开表的自我计算（$\nu_s$）和对私有表（$\nu_d$）的零知识证明检查，并通过同态承诺和Schnorr等式证明来关联两者。

### 实验结果

实验在16核Intel Xeon Platinum 8253 CPU（2.20GHz）、764 GB RAM的服务器上进行，并对比了DFA、DFA+递归和SAFA+nlookup三种基线方法。核心应用包括邮件涂改、ODoH阻塞列表、密码强度证明和DNA变异证明。对于DNA染色体（约3230万字符）匹配的正则表达式证明，Reef在匹配情况下总耗时26.40秒，非匹配情况下为14.20秒，而SAFA+nlookup在不使用投影时分别需要17695.30秒和329.94秒，性能提升超过两个数量级。对于较小的应用（如密码强度证明，文档仅12个字符），Reef仅需约2.7秒即可生成证明，而DFA基线因不支持前瞻而无法运行。在内存使用方面，Reef通过递归和表投影技术将最大内存消耗控制在5.1 GB以内（DNA应用），而DFA和DFA+递归基线在大型邮件（1000字符）上消耗超过124 GB且无法完成。所有应用的证明大小均仅为几十KB，验证时间小于1秒，体现了其公开可验证和简洁性的优势。

### 局限性与开放问题
Reef在文档与正则表达式高度相似时，由于SAFA跳过机会减少，证明性能会下降，而Zombie [79]可能在相反场景（小文档或紧密匹配）下表现更优，两者存在互补空间。目前的系统仅支持正则表达式，尚不能处理上下文无关文法（如括号匹配），尽管其已有的栈结构为扩展奠定了基础。此外，Reef支持的“搜索替换”功能是一个有价值的未来研究方向，需要将修改后的结果与原始文档通过零知识证明关联起来。

### 强关联论文

[11] Zk email verify. **USENIX Security 2023** [Google Scholar](https://scholar.google.com/scholar?q=zk+email+verify)

[56] Luo et al. Privacy-preserving regular expression matching using nondeterministic finite automata. **CCS 2023** [Google Scholar](https://scholar.google.com/scholar?q=Privacy-preserving+regular+expression+matching+using+nondeterministic+finite+automata)

[64] Raymond et al. Efficient zero knowledge for regular language. **USENIX Security 2024** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+zero+knowledge+for+regular+language)

[79] Zhang et al. Zombie: Middleboxes that don’t snoop. **NSDI 2024** [Google Scholar](https://scholar.google.com/scholar?q=Zombie+Middleboxes+that+don%27t+snoop)

[52] Kothapalli et al. Nova: Recursive zero-knowledge arguments from folding schemes. **CRYPTO 2022** [Google Scholar](https://scholar.google.com/scholar?q=Nova+Recursive+zero-knowledge+arguments+from+folding+schemes)

[51] Kothapalli and Setty. HyperNova: recursive arguments for customizable constraint systems. **CRYPTO 2024** [Google Scholar](https://scholar.google.com/scholar?q=HyperNova+recursive+arguments+for+customizable+constraint+systems)

[76] Wahby et al. Doubly-efficient zkSNARKs without trusted setup. **S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Doubly-efficient+zkSNARKs+without+trusted+setup)

[66] Setty. Spartan: Efficient and general-purpose zkSNARKs without trusted setup. **CRYPTO 2020** [Google Scholar](https://scholar.google.com/scholar?q=Spartan+Efficient+and+general-purpose+zkSNARKs+without+trusted+setup)


## 关键词

+ Reef正则表达式零知识证明
+ SAFA跳过交替有限自动机
+ 文档匹配ZK证明系统
+ 密码强度匿名证明
+ DNS查询隐私保护ZK
+ 非交互式简洁正则证明
