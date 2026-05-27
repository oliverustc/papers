---
title: "Monotone-policy aggregate signatures"
doi: 10.1007/978-3-031-58737-5_7
标题简称:
论文类型: conference
会议简称: EUROCRYPT
发表年份: 2024
created: 2025-04-28 11:29:47
modified: 2025-04-28 11:32:27
---
## Monotone-policy aggregate signatures

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-58737-5_7)

## 作者

+ Maya Farber Brodsky 
+ [Arka Rai Choudhuri](Arka%20Rai%20Choudhuri.md)
+ [Abhishek Jain](Abhishek%20Jain.md)
+ Omer Paneth 

## 笔记

### 背景与动机
许多去中心化应用（如拜占庭协议、加密钱包、DAO投票）需要一组参与者共同签署一条消息，使得验证者能够确认满足某种单调策略（如t-out-of-k门限）的签名集合存在。传统的门限签名支持门限策略且验证简洁，但需要交互式密钥设置和（通常）交互式签名协议，这在非交互式场景下不切实际。另一方面，聚合签名允许非交互地将多个签名合并为一个短证书，但只能证明所有参与者均签署了消息（即k-out-of-k策略），无法表达更丰富的签名策略如加权门限或层次门限。现有构造单调策略聚合签名的通用方法是将标准签名与适应性可靠的简洁非交互知识论证（SNARK）结合，但SNARK目前仅基于非标准假设或启发式方案，且知识提取能力受到强障碍的限制。本文填补的空白是：在标准多项式时间密码学假设下，首次构造出支持任意单调策略、签名大小和验证时间均为poly(log k, λ)的聚合签名方案，且无需交互式密钥设置。

### 相关工作

[9] Boneh et al. Aggregate and verifiably encrypted signatures from bilinear maps. **EUROCRYPT 2003** [Google Scholar](https://scholar.google.com/scholar?q=Aggregate+and+verifiably+encrypted+signatures+from+bilinear+maps)
> 核心思路：利用双线性映射实现非交互聚合签名，可聚合不同签名者的不同消息。
> 局限与区别：仅支持全聚合（k-out-of-k），不支持门限或其他单调策略；安全性依赖随机预言模型。

[11] Brakerski et al. SNARGs for monotone policy batch NP. **CRYPTO 2023** [Google Scholar](https://scholar.google.com/scholar?q=SNARGs+for+monotone+policy+batch+NP)
> 核心思路：构造单调策略下可提取的批参数（BARGs），支持多项式大小单调电路的策略。
> 局限与区别：其提取性质中必要子集$J$需非自适应地编程到CRS中，而本文的聚合签名安全性需要适应性选择的必要子集。

[19] Choudhuri et al. SNARGs for P from LWE. **FOCS 2022** [Google Scholar](https://scholar.google.com/scholar?q=SNARGs+for+P+from+LWE)
> 核心思路：基于LWE构造某处可提取的BARGs，支持k-out-of-k策略。
> 局限与区别：仅适用于合取策略，无法直接处理单调策略；本文在此基础上通过可组合vPIR将其扩展为适应性子集提取。

[25] Devadas et al. Rate-1 non-interactive arguments for batch-NP and applications. **FOCS 2022** [Google Scholar](https://scholar.google.com/scholar?q=Rate-1+non-interactive+arguments+for+batch-NP+and+applications)
> 核心思路：利用率-1 BARGs实现多跳聚合签名。
> 局限与区别：仅支持k-out-of-k策略；本文的方案可支持单调策略且单跳聚合，但多跳扩展留作未来工作。

[10] Boneh et al. Short signatures from the Weil pairing. **ASIACRYPT 2001** [Google Scholar](https://scholar.google.com/scholar?q=Short+signatures+from+the+Weil+pairing)
> 核心思路：BLS短签名，支持签名聚合和门限变体（需交互）。
> 局限与区别：门限实现需要交互式密钥生成和签名；本文实现非交互且在标准假设下。

[4] Ben-David et al. Verifiable private information retrieval. **TCC 2022** [Google Scholar](https://scholar.google.com/scholar?q=Verifiable+private+information+retrieval)
> 核心思路：构造可验证的私有信息检索协议（vPIR），用于只读一次、有界空间谓词。
> 局限与区别：原文仅处理非自适应选择的谓词；本文将其扩展到适应性设置，并利用其可组合性构造适应性子集提取BARGs。

[50] Waters and Wu. Batch arguments for NP and more from standard bilinear group assumptions. **CRYPTO 2022** [Google Scholar](https://scholar.google.com/scholar?q=Batch+arguments+for+NP+and+more+from+standard+bilinear+group+assumptions)
> 核心思路：基于双线性群上的DLIN假设构造某处可提取BARGs。
> 局限与区别：仅支持合取策略；本文通过vPIR技术将某处可提取BARGs提升为适应性子集提取BARGs。

[3] Bellare et al. Stronger security for non-interactive threshold signatures: BLS and FROST. **ePrint 2022** [Google Scholar](https://scholar.google.com/scholar?q=Stronger+security+for+non-interactive+threshold+signatures:+BLS+and+FROST)
> 核心思路：定义弱不可伪造性等安全性概念用于门限签名。
> 局限与区别：其弱不可伪造性定义与本文中弱不可伪造聚合签名中的定义对应；本文中弱不可伪造版本基于功能子集提取BARGs获得更广泛的政策支持。

### 核心技术与方案

**1. 整体框架：从BARGs到聚合签名的模板构造**
每个用户使用基础签名方案S生成自己的验证密钥${ \mathsf { v k } } _ { i }$。聚合验证密钥$\widehat { \mathsf { v k } }$通过碰撞抵抗哈希函数计算所有${ \mathsf { v k } } _ { i }$的哈希树根。聚合签名是一个BARG证明，证明存在一组有效签名，使得单调策略$f$的值为1。具体地，定义NP语言$\mathcal { L }$包含三元组$(\widehat { \mathsf { v k } } , m , i)$当且仅当存在一个验证密钥${ \mathsf { v k } } _ { i }$、一条从${ \mathsf { v k } } _ { i }$到$\widehat { \mathsf { v k } }$的认证路径以及一个在m下对${ \mathsf { v k } } _ { i }$有效的签名$\sigma _ { i }$。给定k个语句$(\widehat { \mathsf { v k } } , m , i)$，BARG证明$\widehat { \sigma }$证明$f(b_1,\ldots,b_k)=1$，其中$b_i$指示第i个语句是否为真。验证算法检查该BARG证明是否接受。签名大小和验证时间均为poly(log k, λ)（利用BARG对索引语言的高效验证性质）。

**2. 适应性子集提取BARGs（定理1的核心工具）**
定义：算法Setup输出CRS和陷门td，但CRS不针对任何特定子集编程。提取算法Extract(td, π)输出索引i和证据$w_i$。安全性要求：对于任何多项式大小的敌手$\mathcal { P } ^ { * }$，如果它输出一个接受证明π和一个必要子集$J \subseteq [k]$（即$f( \mathbb { 1 } _ { [k] \setminus J }) = 0$），那么以至少$\alpha / k - \mathsf {negl}$的概率，Extract输出一个索引$i \in J$且$M(z,i,w_i)=1$。这里$\alpha$是敌手输出接受证明且J必要的概率。这一性质对于合取策略是最优的（损失因子1/k）。

构造：基于可组合的可验证私有信息检索（vPIR）。给定一个读取一次、空间S的单调策略f，构造一个读取一次、空间S的谓词$P_f$，其输入为数据库$D=(w_1,\ldots,w_k)$，输出$f(b_1,\ldots,b_k)$，其中$b_i=1$当且仅当$w_i$是第i个语句的有效证据。CRS为vPIR查询（对随机索引j）。证明者为每个语句提供证据数据库，计算vPIR应答并发送。提取者解密应答得到$w_j$。为证明适应性子集提取，利用2-可组合vPIR：敌手不仅输出一个证明（即vPIR应答a），还输出一个额外应答$a'$，该应答通过vPIR从数据库$D'$计算，其中$D'$编码必要子集$J$的补集（即$b_i'=1$当且仅当$i \notin J$）。谓词$P_f'$检查$f(D')=0$（即J必要）。通过可组合vPIR的安全性，存在模拟器同时模拟两个数据库，保证提取的索引i属于J的概率至少为$\alpha/k - \mathsf{negl}$。

**3. 弱不可伪造聚合签名（定理3）**
对于任意多项式大小单调电路，构造功能子集提取BARGs。CRS编程了一个函数g。给定输入y（即所有验证密钥的向量），BARG验证者只使用y的哈希摘要。若$J=g(y)$是必要子集，则可从接受证明中提取$j \in J$的证据。利用该BARG和能生成“标记”验证密钥的签名方案（通过陷门识别标记密钥），构造弱不可伪造聚合签名：在安全性游戏中，诚实密钥被标记，函数g利用陷门输出所有标记密钥的索引集合J。由于敌手无法伪造标记密钥，J一定包含所有未被签名的诚实密钥。这直接与弱不可伪造性定义匹配。此构造避免了对适应性子集提取的需求，从而支持任意多项式大小单调电路（假设FHE和某处可提取BARGs）。

**4. 快速聚合器（定理2）**
对于门限策略，改进vPIR的编码方式：数据库仅包含t行（而非k行），每行存储一个证据及对应的索引j（递增顺序）。谓词检查t个索引的严格递增序列。这样证明者的运行时间从O(k)降为O(t)。适应性子集提取的论证类似，通过2-可组合vPIR保证提取的索引不在补集中，从而在$J^*$中。此技术可推广至其他策略。

### 核心公式与流程

**[聚合签名模板构造（Fig. 1）]**
$$
\begin{aligned}
&\mathsf{Setup}(1^\lambda): \text{生成哈希密钥 hk 和 BARG 的 }(\mathsf{crs}_{BARG},\mathsf{td}_{BARG}). \text{输出 } \mathsf{crs} = (\mathsf{hk},\mathsf{crs}_{BARG}).\\
&\mathsf{KeyAgg}(\mathsf{crs},\{\mathsf{vk}_i\}_{i\in[k]}): \text{计算 } \widehat{\mathsf{vk}} = \mathsf{Hash}_{HT}(\mathsf{hk},(\mathsf{vk}_1,\ldots,\mathsf{vk}_k)).\\
&\mathsf{SigAgg}(\mathsf{crs},f,\{\mathsf{vk}_i,\sigma_i\}_{i\in[k]},m):\\
&\quad \text{定义 } z = (\mathsf{hk},\widehat{\mathsf{vk}},m). \text{定义图灵机 } M(z,j,w_j) \text{ 验证认证路径和签名}.\\
&\quad \text{构造证据 } w = (w_1,\ldots,w_k). \text{输出 } \widehat{\sigma} = \mathcal{P}_{BARG}(\mathsf{crs}_{BARG}, f, M, z, 1^T, w).\\
&\mathsf{AggVerify}(\mathsf{crs},f,\widehat{\mathsf{vk}},m,\widehat{\sigma}): \text{解析 } \widehat{\sigma},\text{调用 } \mathcal{V}_{BARG}(\mathsf{crs}_{BARG}, x, \widehat{\sigma}),\text{其中 } x=(f,M,z,T).
\end{aligned}
$$
> 作用：该流程将任意单调策略聚合签名简化为BARG的证明。安全性依赖于BARG的适应性子集提取性质，从中可提取一个非平凡签名（或哈希碰撞）。

**[适应性子集提取安全性定义]**
$$
\Pr_{\mathsf{EXP}}\left[ i \in J \land M(z,i,w_i)=1 \right] \geq \frac{1}{\alpha(\lambda)} \cdot \Pr_{\mathsf{EXP}}\left[ \mathcal{V}(\mathsf{crs},x,\pi)=1 \land f(\mathbb{1}_{[k]\setminus J})=0 \right] - \mathsf{negl}(\lambda)
$$
> 作用：形式化BARG的适应性子集提取保证。敌手可先输出证明和必要子集J，提取器以损失因子α/k的概率（α定义为敌手输出接受证明且J必要的概率）提取到J中的有效证据。

### 实验结果
本文为理论密码学工作，未提供具体的实验评估。所有构造均在标准模型下给出，复杂度分析如下：对于读取一次、空间S的单调策略，CRS大小为poly(log k, λ)，聚合签名大小为poly(log k, S, λ)，验证时间为poly(log k, S, λ)。对于门限策略，聚合器运行时间为poly(t, λ)，其中t为门限值。对于弱不可伪造版本，支持任意多项式大小单调电路，CRS和签名大小仍为poly(log k, λ)。这些参数均以多项式形式随安全参数和参与者数量对数增长，理论高效性已通过渐近分析证明。

### 局限性与开放问题
本文构造的适应性子集提取BARGs仅适用于读取一次、有界空间的单调策略，对于任意多项式大小单调电路尚未实现（仅在弱不可伪造聚合签名中通过功能子集提取达成）。多跳聚合签名（即允许增量聚合）的扩展仅被提及为未来方向，未给出具体构造。此外，带权门限策略（权重为B比特）虽然支持，但聚合器运行时间与B的对数相关，对于极大权重可能效率下降。开放问题包括：能否在标准假设下实现完全自适应安全（非弱不可伪造）的任意单调策略聚合签名？能否将验证时间进一步降至与策略描述长度无关？

### 强关联论文

[11] Brakerski, Z., Brodsky, M.F., Kalai, Y.T., Lombardi, A., Paneth, O. SNARGs for monotone policy batch NP. **CRYPTO 2023**

[4] Ben-David, S., Kalai, Y.T., Paneth, O. Verifiable private information retrieval. **TCC 2022**

[19] Choudhuri, A.R., Jain, A., Jin, Z. SNARGs for P from LWE. **FOCS 2022**

[25] Devadas, L., Goyal, R., Kalai, Y., Vaikuntanathan, V. Rate-1 non-interactive arguments for batch-NP and applications. **FOCS 2022**

[50] Waters, B., Wu, D.J. Batch arguments for NP and more from standard bilinear group assumptions. **CRYPTO 2022**

[9] Boneh, D., Gentry, C., Lynn, B., Shacham, H. Aggregate and verifiably encrypted signatures from bilinear maps. **EUROCRYPT 2003**

[3] Bellare, M., Tessaro, S., Zhu, C. Stronger security for non-interactive threshold signatures: BLS and FROST. **ePrint 2022**

[10] Boneh, D., Lynn, B., Shacham, H. Short signatures from the Weil pairing. **ASIACRYPT 2001**

[34] Itakura, K., Nakamura, K. A public key cryptosystem suitable for digital multisignatures. **NEC Research and Development 1983**

[41] Micali, S. CS proofs (extended abstracts). **FOCS 1994**


## 关键词

+ 单调策略聚合签名
+ 非交互式批处理论证
+ 自适应安全性
+ 简洁签名
+ 门限签名策略
