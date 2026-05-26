---
title: "Piano: extremely simple, single-server PIR with sublinear server computation"
标题简称:
论文类型: conference
会议简称: S&P
发表年份: 2024
created: 2025-04-27 09:27:28
modified: 2025-04-27 09:33:20
---

## Piano: extremely simple, single-server PIR with sublinear server computation

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/10646686)

## 作者

+ Mingxun Zhou 
+ Andrew Park 
+ [Wenting Zheng](Wenting%20Zheng.md)
+ [Elaine Shi](Elaine%20Shi.md)
## 笔记

### 背景与动机
私有信息检索（PIR）允许客户端在隐藏查询内容的前提下，从服务器存储的公开数据库中获取记录。该问题由 Chor 等人 [16, 17] 首先提出，并成为密码学领域的重要课题。然而，任何不进行预处理的经典 PIR 方案，其服务器计算开销必然与数据库大小 n 呈线性关系，Beimel 等人 [4] 证明了这一下界。为了突破线性计算瓶颈，预处理模型被引入 [4]，该模型允许客户端提前下载一个“提示”来加速后续查询。在此模型下，虽然已有理论方案实现了次线性服务器计算 [18, 19, 39, 40, 57, 41]，但它们普遍依赖同态加密（FHE）、可编程伪随机函数（PRF）或多项式编码等重量级密码原语，导致实现极其复杂且具体性能低下。与此相对，现有的实用单服务器 PIR 方案（如 SimplePIR [32]）虽然依赖线性同态加密并在线性时间内完成了高效的服务器计算，但其线性复杂度严重限制了可扩展性，例如在 100GB 的 DNS 数据库场景下，其响应时间超过 11 秒。因此，急需一种既具备次线性服务器计算效率，又能在实际中实现简单、性能优异的单服务器 PIR 方案。

### 相关工作

[32] Alexandra Henzinger et al. One server for the price of two: Simple and fast single-server private information retrieval. **Crypto 2022** [Google Scholar](https://scholar.google.com/scholar?q=One+server+for+the+price+of+two%3A+Simple+and+fast+single-server+private+information+retrieval)
> 核心思路：采用线性同态加密进行单服务器 PIR，服务器需线性扫描整个数据库。
> 局限与区别：服务器计算为 O(n)，在大型数据库（如 100GB）中延迟极高。PIANO 通过预处理实现了 O(√n) 服务器计算，消除了线性计算瓶颈。

[18] Henry Corrigan-Gibbs et al. Single-server private information retrieval with sublinear amortized time. **Eurocrypt 2022** [Google Scholar](https://scholar.google.com/scholar?q=Single-server+private+information+retrieval+with+sublinear+amortized+time)
> 核心思路：通过 FHE 将两服务器方案转换为单服务器方案，实现次线性服务器时间。
> 局限与区别：FHE 的电路表示引入了巨大的常数因子，且需要运行 λ 个并行实例以保证正确性，实际中开销过高，不实用。PIANO 则完全避免使用同态加密。

[19] Henry Corrigan-Gibbs et al. Private information retrieval with sublinear online time. **Eurocrypt 2020** [Google Scholar](https://scholar.google.com/scholar?q=Private+information+retrieval+with+sublinear+online+time)
> 核心思路：提出了预处理模型下的 PIR 方案，支持单次查询，并给出后续扩展思路。
> 局限与区别：最初方案仅支持单次查询，且转换为多查询时依赖 FHE。PIANO 在此框架基础上，无需 FHE 即可支持无限次查询。

[39] Arthur Lazzaretti et al. Single server pir with sublinear amortized time and polylogarithmic bandwidth. **Crypto 2023** [Google Scholar](https://scholar.google.com/scholar?q=Single+server+pir+with+sublinear+amortized+time+and+polylogarithmic+bandwidth)
> 核心思路：使用私有可编程 PRF 实现多对数带宽的单服务器 PIR。
> 局限与区别：其核心原语（私有可编程 PRF）仅存在于理论中，无法实用。PIANO 牺牲了最优通信（O(√n)），换取了基于标准 PRF 的极简构造。

[40] Arthur Lazzaretti et al. Treepir: Sublinear-time and polylog-bandwidth private information retrieval from ddh. **Crypto 2023** [Google Scholar](https://scholar.google.com/scholar?q=Treepir%3A+Sublinear-time+and+polylog-bandwidth+private+information+retrieval+from+ddh)
> 核心思路：使用 DDH 假设实现两服务器 PIR，支持多对数通信和次线性时间。
> 局限与区别：其两服务器构造无法通过 FHE 自然地、高效地转化为单服务器方案。PIANO 提出了将两服务器方案转换为单服务器的全新思路，无需同态加密。

[57] Mingxun Zhou et al. Optimal single-server private information retrieval. **Eurocrypt 2023** [Google Scholar](https://scholar.google.com/scholar?q=Optimal+single-server+private+information+retrieval)
> 核心思路：在预处理模型下，提出具有最优客户端存储与服务器计算权衡的单服务器 PIR，通信开销为多对数级。
> 局限与区别：同样依赖私有可编程 PRF 等复杂原语。PIANO 通过增大通信开销（O(√n)）来彻底简化密码学假设，仅需 PRF。

### 核心技术与方案

PIANO 的核心思想是从一个简单的两服务器 PIR 方案出发，通过压缩客户端存储和计算，并最终以一种新颖的方式将两个服务器“合并”成一个，从而避免使用同态加密。方案分为预处理和在线查询两个阶段，采用客户端预处理（订阅）模型。

**起点：低效的两服务器方案**。该方案借鉴了 Lazzaretti 和 Papamanthou [40] 的思想。数据库被分为 $\sqrt{n}$ 个大小为 $\sqrt{n}$ 的块。一个随机“偏移向量” $\Delta = (\delta_0, \ldots, \delta_{\sqrt{n}-1})$ 定义了一个集合 $\text{Set}(\Delta) := \{i \cdot \sqrt{n} + \delta_i\}_{i=0}^{\sqrt{n}-1}$。预处理时，客户端生成多个随机偏移向量，发送给左服务器，左服务器返回对应集合的异或同余（奇偶性）作为提示。在线查询时，为获取索引 $x$，客户端在其提示表中找到一个包含 $x$ 的集合 $\Delta^*$。它计算一个“截断的”偏移向量 $\Delta_{-i^*}^*$（删除了 $x$ 所在块 $i^*$ 的偏移量），发送给右服务器。由于右服务器不知道删除了哪个块，它需要计算所有 $\sqrt{n}$ 种可能的同余值，并全部返回给客户端。客户端利用提前存储的提示同余值，从中恢复出 $x$ 的取值。

**核心创新 1：压缩客户端存储与计算**。客户端需要存储大量提示，每个提示是一个 $\sqrt{n}$ 大小的偏移向量，总存储超线性。PIANO 使用一个 PRF 密钥 $\text{sk}$ 来压缩表示偏移向量：$\Delta(\text{sk}) = \operatorname{PRF}_{\text{sk}}(0), \ldots, \operatorname{PRF}_{\text{sk}}(\sqrt{n}-1)$。这样，客户端只需存储密钥 $\text{sk}$ 及其对应的同余值。同时，判断一个集合是否包含索引 $x$ 可以在 $O_{\lambda}(1)$ 时间内完成，从而使在 $M_1 = \Theta(\sqrt{n} \log n)$ 个提示中搜索匹配提示的期望时间为 $O_{\lambda}(\sqrt{n})$。

**核心创新 2：合并两个服务器（无需同态加密）**。
这是本文技术贡献的核心。方案采用“分组备份提示”和“流式预处理”技巧，将两服务器方案转换为单服务器方案。

1.  **分组备份提示**：在预处理阶段，客户端除了生成 $M_1$ 个主提示外，还为每个数据库块 $i$ 生成 $M_2 = \Theta(\log n)$ 个备份提示。第 $i$ 组的备份提示对应的集合删除了第 $i$ 个元素。在线查询 $x$ 后，客户端需要刷新被消耗的主提示，使其重新成为包含 $x$ 的随机集合。为此，客户端直接从第 $i^*$ 组的备份提示中取出一个未使用的提示 $(\overline{\text{sk}}, \overline{p})$，并将其与当前查询 $x$ 结合，构成新的主提示 $( (\overline{\text{sk}}, x), \beta \oplus \overline{p} )$。其中，$\beta$ 是当前查询的答案。这个过程无需同服务器交互，因为备份提示的同余值 $\overline{p}$（即集合中除 $x$ 位置外的元素同余）已在预处理阶段计算并存储。随机查询假设保证了备份提示不会被耗尽。

2.  **流式预处理**：客户端通过一次流式扫描整个数据库来完成预处理。它生成所有主提示和备份提示的密钥，并将同余值初始化为 0。然后依次下载每个大小为 $\sqrt{n}$ 的块，遍历所有提示，如果该块中的某个条目属于该提示的集合，则更新其同余值。处理完一个块后立即删除，因此客户端存储始终为 $O_{\lambda}(\sqrt{n})$。虽然预处理需要 $O(n)$ 通信和 $O_{\lambda}(n \log n)$ 客户端计算，但可以摊销到后续的 $Q = \Theta(\sqrt{n})$ 次查询中。

**安全性证明**：隐私性通过一个模拟器证明。在理想实验中，模拟器在每次查询时都发送一个完全随机的截断偏移向量。通过混合论证明，真实协议中客户端发出的截断偏移向量与随机向量不可区分，从而保证服务器无法获知查询索引。

**复杂度**：方案支持无限次查询（通过摊销后续窗口的预处理工作）。其渐进复杂度为：客户端存储 $O_{\lambda}(\sqrt{n} \log n)$；在线查询通信 $O(\sqrt{n})$；在线查询服务器计算 $O(\sqrt{n})$（通过“相邻同余只差两项”的算法实现）；在线查询客户端期望计算 $O_{\lambda}(\sqrt{n})$；预处理（摊销后）为 $O_{\lambda}(n \log n)$ 客户端计算和 $O(n)$ 通信。

### 核心公式与流程

**[偏移向量到集合的映射]**
$$\text{Set}(\Delta) := \{i \cdot \sqrt{n} + \delta_i\}_{i=0}^{\sqrt{n}-1}, \text{ where } \Delta = (\delta_0, \ldots, \delta_{\sqrt{n}-1})$$
> 作用：定义一个由偏移向量 $\Delta$ 生成的数据库索引集合，每个块 $i$ 贡献一个元素。

**[PRF 压缩的集合表示]**
$$\text{Set}(\text{sk}, x') [i] := \begin{cases}
x', & \text{if } x' \neq \bot \text{ and } \lfloor x' / \sqrt{n} \rfloor = i; \\
i \cdot \sqrt{n} + \text{PRF}_{\text{sk}}(i), & \text{otherwise.}
\end{cases}$$
> 作用：使用 PRF 密钥 $\text{sk}$ 和可选的强制索引 $x'$ 来紧凑地表示一个集合，并能 $O_{\lambda}(1)$ 时间计算任一元素。

**[服务器计算“所有可能同余值”的 O(√n) 算法——PossibleParities(Δ)]**
输入：$\Delta = (\delta_0, \dots, \delta_{\sqrt{n}-2})$
1. 初始化 $q_0 = \bigoplus_{i \in \{1, \dots, \sqrt{n}-1\}} \text{DB}[\delta_{i-1} + i \cdot \sqrt{n}]$。
2. 对于 $i = 0, \dots, \sqrt{n}-2$，计算 $$q_{i+1} = q_i \oplus \text{DB}[\delta_i + (i+1) \cdot \sqrt{n}] \oplus \text{DB}[\delta_i + i \cdot \sqrt{n}]$$。
3. 返回 $(q_0, \dots, q_{\sqrt{n}-1})$。
> 作用：客户端发送一个截断的偏移向量（含 $\sqrt{n}-1$ 个偏移量）。服务器在不知道缺失块位置 $i^*$ 的情况下，利用相邻同余值仅差两项的观察，在 $O(\sqrt{n})$ 时间内计算出所有 $\sqrt{n}$ 种可能的集合同余值。

### 实验结果

实验在 AWS m5.8xlarge 实例（128GB RAM）上进行。PIANO 的主要对比基线是 SimplePIR [32]，这是当前性能最优的实用单服务器 PIR 方案，但其服务器计算是线性的。
对于 2GB 数据库（8 字节条目），在局域网环境中，PIANO 的在线查询时间仅为 9.0 ms，而 SimplePIR 需要 219.5 ms，实现了 24.4 倍的加速。对于 100GB 数据库（64 字节条目），PIANO 的在线时间为 33.3 ms，而 SimplePIR 的推算时间高达 10.9 秒，性能提升超过 300 倍。
在跨广域网环境（60ms RTT，2Gbps 带宽）下，对于 100GB 数据库，PIANO 的总响应时间为 93.4 ms，与非私有基线方案的 61.0 ms 相比，延迟仅增加了 1.53 倍。而 SimplePIR 的预估响应时间高达 10.9 秒，是 PIANO 的 116 倍以上。性能分析表明，PIANO 的在线时间主要受网络传输支配，其次是客户端计算（用于搜索匹配提示），服务器计算开销最小。实验结果表明，PIANO 是首个能在单服务器场景下实用化次线性计算的 PIR 方案，其性能优势随着数据库增大而愈加显著。

### 局限性与开放问题

PIANO 的主要代价在于通信开销：预处理阶段客户端需下载整个数据库（$O(n)$ 通信），在线查询阶段通信量为 $O(\sqrt{n})$。与此前理论最优的 polylog 通信方案相比 [39, 57]，这是为完全摆脱同态加密等复杂原语而做出的牺牲。未来一个重要的开放方向是，在保持 PIANO 实用性和简洁性的前提下，设计出通信开销更优（如 polylog 级）的单服务器 PIR 方案。

### 强关联论文

[32] Alexandra Henzinger et al. One server for the price of two: Simple and fast single-server private information retrieval. **Crypto 2022** [Google Scholar](https://scholar.google.com/scholar?q=One+server+for+the+price+of+two%3A+Simple+and+fast+single-server+private+information+retrieval)

[18] Henry Corrigan-Gibbs et al. Single-server private information retrieval with sublinear amortized time. **Eurocrypt 2022** [Google Scholar](https://scholar.google.com/scholar?q=Single-server+private+information+retrieval+with+sublinear+amortized+time)

[19] Henry Corrigan-Gibbs et al. Private information retrieval with sublinear online time. **Eurocrypt 2020** [Google Scholar](https://scholar.google.com/scholar?q=Private+information+retrieval+with+sublinear+online+time)

[39] Arthur Lazzaretti et al. Single server pir with sublinear amortized time and polylogarithmic bandwidth. **Crypto 2023** [Google Scholar](https://scholar.google.com/scholar?q=Single+server+pir+with+sublinear+amortized+time+and+polylogarithmic+bandwidth)

[40] Arthur Lazzaretti et al. Treepir: Sublinear-time and polylog-bandwidth private information retrieval from ddh. **Crypto 2023** [Google Scholar](https://scholar.google.com/scholar?q=Treepir%3A+Sublinear-time+and+polylog-bandwidth+private+information+retrieval+from+ddh)

[57] Mingxun Zhou et al. Optimal single-server private information retrieval. **Eurocrypt 2023** [Google Scholar](https://scholar.google.com/scholar?q=Optimal+single-server+private+information+retrieval)

[4] Amos Beimel et al. Reducing the servers computation in private information retrieval: Pir with preprocessing. **Crypto 2000** [Google Scholar](https://scholar.google.com/scholar?q=Reducing+the+servers+computation+in+private+information+retrieval%3A+Pir+with+preprocessing)

[41] Wei-Kai Lin et al. Doubly efficient private information retrieval and fully homomorphic ram computation from ring lwe. **Crypto 2023** [Google Scholar](https://scholar.google.com/scholar?q=Doubly+efficient+private+information+retrieval+and+fully+homomorphic+ram+computation+from+ring+lwe)


## 关键词

+ 单服务器私有信息检索
+ 次线性时间PIR
+ 伪随机函数
+ 预处理PIR
+ 隐私数据库查询
+ 最优存储计算权衡