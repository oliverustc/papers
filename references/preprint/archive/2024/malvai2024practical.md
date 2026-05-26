---
title: "Practical Proofs of Parsing for Context-free Grammars"
标题简称:
论文类型: preprint
预印本简称: archive
发表年份: 2024
created: 2025-04-16 10:35:39
modified: 2025-04-16 10:38:09
---

## Practical Proofs of Parsing for Context-free Grammars

## 发表信息

+ [原文链接](https://eprint.iacr.org/2024/562)

## 作者

+ Harjasleen Malvai 
+ Siam Hussain 
+ Gregory Neven 
+ [Andrew Miller](Andrew%20Miller.md) 

## 笔记

### 背景与动机
当前越来越多的数字信息以结构化格式（如 HTML、JSON、XML）存在，机器通过解析来提取信息。然而，在许多场景下，数据持有者（证明者）不想向验证者透露完整的文档内容，例如展示银行流水的一部分以证明偿债能力、或证明一封邮件的来源而不泄露收件人。零知识证明（ZKP）为此提供了理论工具，但现有方案存在瓶颈：有的依赖对字符串结构的先验假设，有的只能进行部分披露，更通用的方案通过将解析算法放入 ZK 虚拟机执行，其复杂度至少为解析本身的立方或二次方。本文旨在填补的空白是：首次实现一个在字符串长度上具有线性复杂度的、协议无关的零知识证明方案，用于证明上下文无关文法（CFG）解析的正确性，从而为 TLS 认证数据、身份凭证验证等应用提供高效的通用基础设施。

### 相关工作
[1] Angel 等. Reef: Fast Succinct Non-interactive Zero-Knowledge Regex Proofs. **CCS 2023** [Google Scholar](https://scholar.google.com/scholar?q=Reef+Fast+Succinct+Non-interactive+Zero-Knowledge+Regex+Proofs)
> 核心思路：利用递归证明系统实现正则表达式的解析证明。
> 局限与区别：仅适用于正则表达式（即有限自动机），其解析过程无需回溯。而 CFG 解析本质更复杂，且 Reef 与特定 ZK 系统和程序表示紧密耦合，本文的方案则与证明系统无关，且同样可结合递归技术。

[5] Angel 等. Reef: Fast Succinct Non-interactive Zero-Knowledge Regex Proofs. **CCS 2023** [Google Scholar](https://scholar.google.com/scholar?q=Reef+Fast+Succinct+Non-interactive+Zero-Knowledge+Regex+Proofs)
> 核心思路：同上。
> 局限与区别：同上，本文明确指出其方案作为主要对比基线，并强调自身可扩展性与系统无关性。

[4] zkjson. **GitHub repository** [Google Scholar](https://scholar.google.com/scholar?q=zkjson)
> 核心思路：在 ZK 电路内执行 JSON 解析。
> 局限与区别：其解析过程需在电路中执行所有可能分支，导致证明生成极慢。本文转而验证已生成的解析树，而非在电路中生成解析树。

[3] TLSNotary. **Web Project** [Google Scholar](https://scholar.google.com/scholar?q=TLSNotary)
> 核心思路：通过 TLS 预言机证明 TLS 会话中数据的真实性。
> 局限与区别：仅证明数据来源，不支持对结构化文档（JSON/XML）内容的细粒度选择性披露。本文提供了必要的解析证明层以填补这一空白。

[6] DECO: Liberating Web Data using Decentralized Oracles for TLS. **CCS 2020** [Google Scholar](https://scholar.google.com/scholar?q=DECO+Liberating+Web+Data+using+Decentralized+Oracles+for+TLS)
> 核心思路：利用 TLS 承诺与 ZKP 实现安全的数据来源证明。
> 局限与区别：依赖对字符串特定结构的先验假设（例如字段唯一键），其处理的对象并非严格意义上的 CFG。本文处理的是无此类假设的通用 CFG。

[7] Chainlink Labs. Deco Research Series #3: Parsing the Response. **Blog 2023** [Google Scholar](https://scholar.google.com/scholar?q=Deco+Research+Series+3+Parsing+the+Response)
> 核心思路：对 JSON 进行部分遮盖或揭露其骨架。
> 局限与区别：该方法会泄露字段的存在性信息。本文的 ZK 方案可以完全隐藏此类信息。

### 核心技术与方案
本文的核心思想是**将“证明一个字符串被正确解析”转化为“证明一个已生成的解析树是正确的”**。由于验证一个树比生成一个树在 ZK 电路中要高效得多，这是实现线性复杂度的关键。具体而言，解析树的所有节点和边数量与字符串长度 n 成线性正比（对于乔姆斯基范式下的 CFG，树节点总数为 3n – 1）。因此，证明者可以本地、快速地生成解析树，然后将该树作为秘密证人输入 ZKP 系统，用来证明其满足三个条件：叶子从左到右拼成原始字符串；每个节点都是文法的合法符号；每个非叶子节点和其子节点构成一条合法的产生式规则。这样，整个问题退化为一连串的集合成员证明问题。

**核心构造与数据表示**  
首先，将上下文无关文法转化为**乔姆斯基范式（CNF）**。在 CNF 中，每个产生式要么将一个非终结符替换为两个非终结符，要么替换为一个终结符。这保证了解析树的结构节点至多有两个子节点，从而简化了电路设计。  
为在 ZKP 系统中高效表示树，本文设计了一种扁平的、非递归的数据结构：定义 `Vertex`（包含标签和深度优先遍历索引 id）和 `Prod`（包含父节点、左子节点、可选的右子节点）。整个解析树 `Π` 用一个数组 `Prods` 表示，该数组按父节点索引排序，其长度为 2n – 1，等于树中非叶子节点数。

**验证算法**  
图 7 的核心算法 `check_parse_tree` 通过一个栈模拟深度优先遍历，依次验证每一个 `Prod` 是否合法。算法状态由 `expected`（期望的下一个父节点）和 `leaf_counter`（已处理的叶子数）维护。  
- **集合成员检查**：对每个 `Prod`，检查其构成的三元组是否属于文法产生式集合 P。  
- **字符串一致性检查**：每当遇到一个产生式仅有一个左子节点（即叶子节点）时，算法将其标签与字符串 s 的下一个字符 `s[leaf_counter]` 比较，并递增计数器。该过程需进行秘密索引访问。  
- **树结构一致性检查**：算法利用栈管理未使用的右子节点，确保每个节点（除根节点外）恰好一次作为父节点出现，且其子节点索引正确，从而隐式保证无环性。  
Claim 1 严格证明了该算法返回真时，`Prods` 必然代表字符串 s 在文法 G 下一个有效的解析树。

**其实例化**  
为适应不同证明系统的优化特性，本文给出了两种实例化：

1. **非交互式证明（算术电路）**  
   - **集合成员检查**：使用 Merkle 树作为累加器。每进行一次成员证明需 $O(\log(|P|))$ 个哈希操作，总复杂度为 $O(|s| \log(|P|))$。  
   - **字符串一致性检查**：使用一个类似栈的哈希链，计算所有叶子节点标签的哈希并与预计算哈希比对，复杂度降至 $O(|s|)$，避免昂贵的秘密索引。  
   - **栈实现**：利用哈希链模拟栈，每个 push/pop 操作复杂度为 $O(1)$。  
   - **整体复杂度**：$O(|s| \log(|P|))$。

2. **交互式证明（布尔电路）**  
   - 利用布尔电路中比较操作开销低的特点，采用**双重排序（Bitonic Sort）**。  
   - **集合成员批处理**：将产生式集合 P 与 Prods 数组合并后排序，通过统计唯一元素个数来批量验证成员关系。排序复杂度为 $O(b(|s|+|P|) \log^2(|s|+|P|))$，其中 b 为位宽。  
   - **字符串一致性检查**：利用叶子节点索引单调递增的性质，收集所有叶子标签后排序，并与字符串 s 比较，同样将问题转化为排序，复杂度为 $O(b|s| \log^2(|s|))$。  
   - **栈实现**：采用分层栈结构，每个 push/pop 的摊还成本为 $O(b \log(|s|))$。  
   - **整体复杂度**：$O(|s| \log^3(|s|))$。

**递归和并行化证明**  
为克服单次证明的 RAM 瓶颈以及加速证明生成，本文还设计了基于递增可验证计算（IVC）和证明携带数据（PCD）的递归方案。可以将算法中的循环分批证明，并将中间状态（如栈哈希、叶子计数器）通过公共输入在迭代间传递。利用 PCD 树（如二叉树），不同批次的证明可以并行生成，再由高层证明验证其连接，从而大幅降低复杂字符串的端到端墙上钟时间。

### 核心公式与流程
**[解析树节点个数公式]**
$$3|s| - 1$$
> 作用：对于一个长度为 |s| 的字符串，若其属于某个乔姆斯基范式下的 CFG，则其解析树的总节点数（顶点数）为 3|s| – 1。这保证了证明的证人数据量（生产式数组长度为 2|s| – 1）与字符串长度成线性关系，是本文所有方案线性复杂度的理论基础。

**[非交互式证明的渐进复杂度]**
$$O(|s| \log(|P|))$$
> 作用：本文的非交互式（算术电路）实现的总证明复杂度。主要受字符串长度 |s| 和产生式集合 |P| 的对数影响。其中集合成员检查的哈希操作和对栈的哈希操作均贡献了线性项。

**[交互式证明的渐进复杂度]**
$$O(b(|s| + |P|) \log^2(|s| + |P|)) \approx O(|s| \log^3(|s|))$$
> 作用：本文的交互式（布尔电路）实现的总证明复杂度。b 为位宽（用于标签和索引）。对于大 |s|，该式简化为 $O(|s| \log^3(|s|))$。瓶颈在于利用了排序操作以实现批量集合成员检查和字符串一致性检查。

**[parse tree 验证算法核心循环（伪代码流程）]**
```
for i in 0..2n-2:
    (parent, left, right) = Prods[i]
    assert(parent == expected)
    assert(left != None)
    assert(left.id == parent.id + 1)
    if right == None:
        assert((parent.label, left.label) ∈ P)   // 集合成员检查
        assert(s[leaf_counter] == left.label)     // 字符串一致性检查
        leaf_counter += 1
        if i < 2n-2:
            expected = stack.pop()
            assert(expected.id == left.id + 1)
    else:
        assert((parent.label, left.label, right.label) ∈ P)  // 集合成员检查
        expected = left
        stack.push(right)
```
> 作用：这是算法的核心，证明了正确解析树所需满足的三个条件。栈操作确保了深度优先遍历顺序；期望变量 `expected` 保证了每个“子节点”在后面的`Prod`中恰好一次被用作父节点，从而确保树的连接性和唯一性。所有断言均在 ZKP 电路中由本文设计的成员证明方案实例化实现。

### 实验结果
实验分为非交互式（基于 Noir 与 Barretenberg/PLONK 后端）和交互式（基于 Quicksilver）两类。  
- **非交互式设置**：在 AWS EC2 g3.8xlarge 实例 (32 CPU, 244GB RAM) 上，对于包含 1024 条产生式（与 JSON 文法规模相当）的字符串，证明一个 2^9 字节（1KB）的字符串解析，需 24.5 秒。证明生成时间主要取决于字符串长度。验证时间恒定，小于 0.14 毫秒，证明大小恒为 2.37KB，均与实例规模无关。  
- **交互式设置**：在 AWS c6gn.8xlarge 实例 (32 CPU, 64GB RAM, 50Gbps) 上，对于相同文法规模和 2^12 字节（8KB）字符串，证明需 16.8 秒；对于 2^16 字节（128KB）需 6.7 分钟；支持到 1GB 量级（2^19 字符）的证明在一个小时内完成。运行时间与门数变化趋势一致。  
- **递归并行化模拟**：基于实验测得的递归证明时间 ($t_{rec}$ 和 $t_{rec}'$)，推导了在 64 核机器上，对于 2^20 字符字符串，采用 arity-4 的 PCD 树进行并行证明，预测墙上钟时间约为 19 分钟。这表明递归技术不仅克服了 RAM 瓶颈，还显著加速了大型字符串的证明生成。

### 局限性与开放问题
尽管本文方案在理论上实现了线性复杂度，但在实际部署中仍面临挑战：非交互式证明的**RAM 消耗极高**（对于 2^9 字符串，超过 10GB），严重限制了可处理的字符串规模在不使用递归情况下的下限。交互式证明虽然计算更快，但**需要持续的在线通信**，不适合所有应用场景。此外，证明生成时间虽与字符串长度成线性关系，但系数仍相对较大（例如 1KB 需 24 秒），对于更大型或实时性要求高的应用，仍需进一步优化。最后，文中的方案仅适用于上下文无关文法，对于包含上下文依赖关系的特定格式（如某些编程语言语法）尚不适用。

### 强关联论文
[5] Sebastian Angel, Eleftherios Ioannidis, Elizabeth Margolin, Srinath Setty, and Jess Woods. Reef: Fast Succinct Non-interactive Zero-Knowledge Regex Proofs. **CCS 2023** [Google Scholar](https://scholar.google.com/scholar?q=Reef+Fast+Succinct+Non-interactive+Zero-Knowledge+Regex+Proofs)
[1] https://github.com/risc0/risc0/tree/main/examples/json. **GitHub repository 2024** [Google Scholar](https://scholar.google.com/scholar?q=https://github.com/risc0/risc0/tree/main/examples/json)
[4] https://github.com/chokermaxx/zkjson. **GitHub repository 2024** [Google Scholar](https://scholar.google.com/scholar?q=https://github.com/chokermaxx/zkjson)
[45] Fan Zhang, Deepak Maram, Harjasleen Malvai, Steven Goldfeder, and Ari Juels. DECO: Liberating Web Data using Decentralized Oracles for TLS. **CCS 2020** [Google Scholar](https://scholar.google.com/scholar?q=DECO+Liberating+Web+Data+using+Decentralized+Oracles+using+TLS+Liberating+Web+Data+Using++Oracles+Using


## 关键词

+ 上下文无关文法解析零知识证明
+ CFG字符串解析线性复杂度ZK
+ 网络API响应零知识验证
+ 非交互式交互式证明范式
+ ZK解析通用编程框架实现