---
title: "Zero Knowledge Proofs for Decision Tree Predictions and Accuracy"
doi: 10.1145/3372297.3417278
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2020

modified: 2025-05-07 22:34:11
created: 2025-04-07 16:21:14
---
## Zero Knowledge Proofs for Decision Tree Predictions and Accuracy

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3372297.3417278)

## 作者

+ [Jiaheng Zhang](Jiaheng%20Zhang.md)
+ [Zhiyong Fang](Zhiyong%20Fang.md)
+ [Yupeng Zhang](Yupeng%20Zhang.md)
+ [Dawn Song](Dawn%20Song.md)

## 笔记

### 背景与动机
机器学习在众多实际应用中日益突出，但其预测结果的完整性和声称的准确率缺乏安全保证。模型所有者希望在不泄露模型本身的前提下，向他人证明模型对特定样本的预测正确，或在公开数据集上达到了宣称的准确度。传统方案若直接公开模型则完全牺牲隐私；若采用黑盒测试则可能被逆向或窃取模型 [25]。通用零知识证明（ZKP）可将任意计算表示为算术电路并生成证明，但将其直接应用于决策树预测会导致证明生成时间极高，因为决策树的随机访问和条件分支在算术电路中开销巨大。本文首次系统研究零知识机器学习预测与准确性，并提出针对决策树的高效零知识协议，填补了该方向的研究空白。

### 相关工作

[4] *Human-guided burrito bots raise questions about the future of robo-delivery*. **The Hustle 2019** [Google Scholar](https://scholar.google.com/scholar?q=Human-guided+burrito+bots+raise+questions+about+the+future+of+robo-delivery)
> 核心思路：报道企业声称使用机器学习自动送餐但实际依赖远程人工的极端案例。
> 局限与区别：该案例凸显模型完整性问题的现实紧迫性，但未提供任何技术解决方案。

[9] Ben-Sasson et al. *SNARKs for C: Verifying program executions succinctly and in zero knowledge*. **CRYPTO 2013** [Google Scholar](https://scholar.google.com/scholar?q=SNARKs+for+C+Verifying+program+executions+succinctly+and+in+zero+knowledge)
> 核心思路：提出将C程序转化为RAM程序，再通过RAM-to-circuit归约生成算术电路，从而用SNARK验证程序执行。
> 局限与区别：通用RAM-to-circuit归约的开销极高（每条指令约4000个乘法门），导致证明生成慢。本文通过非黑盒方式直接构造适合决策树的小电路，避免了通用归约。

[10] Ben-Sasson et al. *Aurora: Transparent Succinct Arguments for R1CS*. **EUROCRYPT 2019** [Google Scholar](https://scholar.google.com/scholar?q=Aurora+Transparent+Succinct+Arguments+for+R1CS)
> 核心思路：提出基于IOP的透明零知识证明系统，支持任意算术电路，证明者时间O(|C| log|C|)，验证者时间O(|C|)，证明大小O(log²|C|)。
> 局限与区别：作为本文的ZKP后端，Aurora本身不针对决策树优化；本文构造的电路规模远小于通用电路，从而利用了Aurora的快速证明者优势。

[11] Ben-Sasson et al. *Succinct Non-Interactive Zero Knowledge for a von Neumann Architecture*. **USENIX Security 2014** [Google Scholar](https://scholar.google.com/scholar?q=Succinct+Non-Interactive+Zero+Knowledge+for+a+von+Neumann+Architecture)
> 核心思路：将RAM程序的逐条指令转换为小电路，实现von Neumann架构的SNARK。
> 局限与区别：适用于通用程序，但决策树预测的随机访问操作在RAM模型中仍产生较大开销。本文直接利用预测路径长度h和属性数d构建小电路O(d+h)，更高效。

[15] Bootle et al. *Arya: Nearly linear-time zero-knowledge proofs for correct program execution*. **ASIACRYPT 2018** [Google Scholar](https://scholar.google.com/scholar?q=Arya+Nearly+linear-time+zero-knowledge+proofs+for+correct+program+execution)
> 核心思路：提出使用特征多项式检验排列关系和多重集关系的技术，实现近线性时间的RAM程序零知识证明。
> 局限与区别：其排列检验方法（基于Schwartz-Zippel）被本文直接用于验证a和ā的排列关系，以及决策树节点多重集检验。

[18] Bünz et al. *Bulletproofs: Short Proofs for Confidential Transactions and More*. **S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Bulletproofs+Short+Proofs+for+Confidential+Transactions+and+More)
> 核心思路：基于离散对数的短证明系统，证明大小对数级。
> 局限与区别：本文使用Aurora优化证明者时间，若改用Bulletproofs可减小证明大小但牺牲证明者速度。

[26] Ghodsi et al. *Safetynets: Verifiable execution of deep neural networks on an untrusted cloud*. **NeurIPS 2017** [Google Scholar](https://scholar.google.com/scholar?q=Safetynets+Verifiable+execution+of+deep+neural+networks+on+an+untrusted+cloud)
> 核心思路：将神经网络验证委托给云服务器，假设验证者持有完整模型，通过承诺和概率检查保证计算正确。
> 局限与区别：不支持零知识（验证者需知模型），且仅保证一次预测的正确性而非模型准确性。本文支持零知识且可证明整体准确率。

[32] Merkle. *A Certified Digital Signature*. **CRYPTO 1989** [Google Scholar](https://scholar.google.com/scholar?q=A+Certified+Digital+Signature)
> 核心思路：提出Merkle哈希树，用于高效验证集合成员关系。
> 局限与区别：若直接用于决策树，每个预测路径需O(h log N)次哈希。本文的认证决策树（ADT）将哈希数降至O(h)，且哈希计算成为电路开销瓶颈。

[40] Wahby et al. *Doubly-efficient zkSNARKs without trusted setup*. **S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Doubly-efficient+zkSNARKs+without+trusted+setup)
> 核心思路：提出基于交互式证明的免信任设置ZK系统，证明者时间和验证者时间均为线性。
> 局限与区别：本文选用Aurora而非该系统，但方案与后端解耦，可替换。

[42] Zhang et al. *Transparent Polynomial Delegation and Its Applications to Zero Knowledge Proof*. **S&P 2020** [Google Scholar](https://scholar.google.com/scholar?q=Transparent+Polynomial+Delegation+and+Its+Applications+to+Zero+Knowledge+Proof)
> 核心思路：提出基于多项式委托的透明零知识证明，分析多种方案性能。
> 局限与区别：本文采用与[42]相同的基础域F_{p²}（p=2^61-1），因该域对Aurora友好。

### 核心技术与方案

**1. 零知识决策树预测（zkDT）**  
方案分为两个阶段：提交阶段和证明阶段。  
- **认证决策树（ADT）**：如图1所示，每个节点v存储属性索引v.att、阈值v.thr、左孩子指针v.left、右孩子指针v.right，以及子节点的哈希值。从叶子向根递归计算哈希，根哈希与随机数r的哈希作为承诺com_T。ADT满足完备性、可靠性（碰撞抗性）和隐藏性（r随机）。复杂度：提交O(N)哈希，证明/验证O(h)哈希。  
- **电路构造**（图2）：输入为公有的数据样本a、承诺com_T和预测结果y_a；私有的证人包括预测路径path_a（节点序列）、兄弟节点哈希、随机数r，以及a的排列ā（索引-值对）。电路包含三子电路：  
  (1) **决策树预测验证**：对路径上每个内部节点v_j，检查v_j.att == i_j，若a[i_j] < v_j.thr则v_{j+1} = v_j.left，否则v_{j+1} = v_j.right；最后检查y_a == v_h.class。该子电路大小为O(d+h)。  
  (2) **排列检验**：检验ā是a的排列。利用特征多项式：验证者选取随机点r'，电路计算乘积Π_{i=1}^d (r' - (a[i] + z·i)) == Π_{i=1}^d (r' - (ā[i] + z·i_j))，其中z由验证者选取，通过Schwartz-Zippel引理保证可靠性（错误概率≤2d/|F|）。该子电路大小为O(d)。  
  (3) **路径验证**：根据ADT算法，用path_a和兄弟哈希重新计算根哈希并与com_T比较。该子电路计算O(h)个哈希。  
  整体电路规模O(d+h)，证明者时间O(|C| log|C|)=O(d log d)，验证者时间O(d)，通信量O(log² d)。协议通过Fiat-Shamir转化为非交互式。

**2. 零知识决策树准确率（zkDTA）**  
目标是证明模型在含n个样本的数据集上的准确率。直接重复zkDT会导致O(nh)次哈希。两个关键优化将哈希数降至O(N)（N为节点总数）：  
- **多重集检验**：将所有预测路径中的节点组成的多重集Q与决策树节点集合S进行多重集关系检验。验证者选取随机数r，电路计算Π_{i=1}^m (r - q_i) == Π_{i=1}^N (r - s_i)^{f_i}，其中f_i为节点s_i在路径中出现的次数（二进制表示）。错误概率≤m/|F|。该检验使电路不依赖路径长度而仅依赖节点总数。  
- **决策树结构线性检查**（Algorithm 2）：提供所有N个节点（包括id、parent id、left child id、right child id、depth），通过线性扫描检查根节点唯一、父指针与孩子指针一致性、深度关系等。该检查O(N)门，确保节点集构成合法二叉树。实际实现中简化：仅检查id排序和左右孩子不重复（除非为空），因为路径节点本身已隐含父子关系。  
  整体电路（图4）包括：对每个样本a_i的排列检验（O(nd)）；决策树预测验证（O(nh)）；路径节点的多重集检验（O(N log n)）；承诺检验（重新计算全树哈希，O(N)）；准确率累加。总电路规模O(nd)（当N≪nd）。证明者时间O(nd log(nd))，验证者O(nd)，证明大小O(log²(nd))。

**3. 安全性**  
- **完备性**：诚实验证者接受诚实证明者的正确预测/准确率宣称。  
- **可靠性**：基于ADT的碰撞抗性和Aurora的知识可靠性。若证明者伪造预测或准确率，则要么ADT路径验证失败（碰撞概率可忽略），要么排列/多重集检验失败（Schwartz-Zippel错误概率可忽略），要么Aurora证明失败。  
- **零知识**：通过混合论证。模拟器S_1用ADT的隐藏性生成承诺（空树的哈希与其实树不可区分），S_2用Aurora的模拟器生成证明（仅需知道真实预测/准确率）。证明标准混合H_0（真实协议）→H_1（实际承诺+模拟证明）→H_2（模拟器）的不可区分性。

### 核心公式与流程

**[认证决策树（ADT）承诺计算]**
$$ \text{hash}(v) = \begin{cases} \text{hash}( \text{data}(v) , \text{hash}(v.\text{left}), \text{hash}(v.\text{right}) ) & v \text{ 是内部节点} \\ \text{hash}(v.\text{class}) & v \text{ 是叶子节点} \end{cases} $$
$$ \text{com}_{\mathcal{T}} = \text{hash}( \text{hash}(\text{root}), r ) $$
> 作用：将决策树压缩为短承诺，支持后续路径验证。

**[排列检验（zkDT）]**
$$ \prod_{i=1}^d \left( r' - ( \mathbf{a}[i] + z \cdot i ) \right) = \prod_{i=1}^d \left( r' - ( \bar{\mathbf{a}}[i] + z \cdot i_j ) \right) $$
> 作用：以高概率检验向量ā是a的排列，用于支持决策树中的随机属性访问。

**[多重集检验（zkDTA）]**
$$ \prod_{i=1}^{m} ( r - q_i ) = \prod_{i=1}^{N} ( r - s_i )^{f_i} $$
> 作用：检验预测路径节点集合（多重集）是决策树节点集合的子多重集，将哈希验证次数从O(nh)降至O(N)。

**[决策树结构线性检查（Algorithm 2 简化版）]**
对于 \(i=1,\dots,N\)，检查 \(T_i.\text{id} = i\)，且 \(T_i.\text{lid} \neq T_i.\text{rid}\) 除非两者均为0。
> 作用：以O(N)门确保提供的节点集形成合法二叉树，避免对不平衡树做2^h次哈希。

### 实验结果

实验在Amazon EC2 c5n.2xlarge（64GB RAM, 3GHz单核）上进行，使用Aurora后端，域为F_{p²}（p=2^61-1），哈希函数采用SWIFFT（约3000个乘法门/哈希）。数据集取自UCI：Breast-Cancer-Wisconsin（10属性，61节点，10层）、Spambase（57属性，441节点，26层）、Forest Covertype（54属性，1029节点，23层）。**zkDT**：预测路径长度6~48时，证明者时间0.754~7.024秒，验证者时间0.050~0.445秒，证明大小140~190KB。**zkDTA**：对最大模型（1029节点），测试5000样本时证明者时间250秒，证明大小287KB，验证者时间15.6秒。与基线对比：与基于TinyRAM的RAM方案相比，zkDT快100倍以上；与直接电路实现相比，当路径长度>12时zkDT显著更快（路径48时直接电路已不可行）。随机森林实验（含2~128棵树）证明者时间6.99~253.41秒。优化效果显著：若不做多重集检验和线性检查，对最大模型需约8000倍于当前性能。

### 局限性与开放问题
本文方案依赖Aurora透明ZKP后端和SWIFFT哈希，两者虽避免可信设置但证明者时间仍达分钟级（250秒），尚未满足实时性要求。方案目前仅支持决策树及其变种（回归树、多变量树、随机森林），未扩展至深度学习模型。实际部署中需考虑针对概率检验的攻击（如Schwartz-Zippel错误概率），建议在足够大的域上运行。未来工作可探索将方案与区块链结合构建公平交易平台，或优化哈希函数以进一步降低电路开销。

### 强关联论文

[9] Eli Ben-Sasson, Alessandro Chiesa, Daniel Genkin, Eran Tromer, Madars Virza. SNARKs for C: Verifying program executions succinctly and in zero knowledge. **CRYPTO 2013** [Google Scholar](https://scholar.google.com/scholar?q=SNARKs+for+C+Verifying+program+executions+succinctly+and+in+zero+knowledge)

[10] Eli Ben-Sasson, Alessandro Chiesa, Michael Riabzev, Nicholas Spooner, Madars Virza, Nicholas P. Ward. Aurora: Transparent Succinct Arguments for R1CS. **EUROCRYPT 2019** [Google Scholar](https://scholar.google.com/scholar?q=Aurora+Transparent+Succinct+Arguments+for+R1CS)

[11] Eli Ben-Sasson, Alessandro Chiesa, Eran Tromer, Madars Virza. Succinct Non-Interactive Zero Knowledge for a von Neumann Architecture. **USENIX Security 2014** [Google Scholar](https://scholar.google.com/scholar?q=Succinct+Non-Interactive+Zero+Knowledge+for+a+von+Neumann+Architecture)

[15] Jonathan Bootle, Andrea Cerulli, Jens Groth, Sune Jakobsen, Mary Maller. Arya: Nearly linear-time zero-knowledge proofs for correct program execution. **ASIACRYPT 2018** [Google Scholar](https://scholar.google.com/scholar?q=Arya+Nearly+linear-time+zero-knowledge+proofs+for+correct+program+execution)

[18] Benedikt Bünz, Jonathan Bootle, Dan Boneh, Andrew Poelstra, Pieter Wuille, Gregory Maxwell. Bulletproofs: Short Proofs for Confidential Transactions and More. **S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Bulletproofs+Short+Proofs+for+Confidential+Transactions+and+More)

[26] Zahra Ghodsi, Tianyu Gu, Siddharth Garg. Safetynets: Verifiable execution of deep neural networks on an untrusted cloud. **NeurIPS 2017** [Google Scholar](https://scholar.google.com/scholar?q=Safetynets+Verifiable+execution+of+deep+neural+networks+on+an+untrusted+cloud)

[32] Ralph C. Merkle. A Certified Digital Signature. **CRYPTO 1989** [Google Scholar](https://scholar.google.com/scholar?q=A+Certified+Digital+Signature)

[40] Riad S. Wahby, Ioanna Tzialla, Abhi Shelat, Justin Thaler, Michael Walfish. Doubly-efficient zkSNARKs without trusted setup. **S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Doubly-efficient+zkSNARKs+without+trusted+setup)

[42] Jiaheng Zhang, Tiancheng Xie, Yupeng Zhang, Dawn Song. Transparent Polynomial Delegation and Its Applications to Zero Knowledge Proof. **S&P 2020** [Google Scholar](https://scholar.google.com/scholar?q=Transparent+Polynomial+Delegation+and+Its+Applications+to+Zero+Knowledge+Proof)

[45] Yupeng Zhang, Daniel Genkin, Jonathan Katz, Dimitrios Papadopoulos, Charalampos Papamanthou. vRAM: Faster verifiable RAM with program-independent preprocessing. **S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=vRAM+Faster+verifiable+RAM+with+program-independent+preprocessing)


## 关键词

+ 零知识证明
+ 机器学习
+ 决策树
+ 隐私保护
+ 完整性验证
