---
title: "Pairing-free blind signatures from standard assumptions in the rom"

标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 2024
modified: 2025-04-16 10:22:29
created: 2025-04-11 12:00:55
---

## Pairing-free blind signatures from standard assumptions in the rom

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-68376-3_7)

## 作者

+ Julia Kastner 
+ Ky Nguyen 
+ [Michael Reichle](Michael%20Reichle.md)
## 笔记

### 背景与动机
盲签名是隐私保护应用（如电子现金、匿名投票、匿名凭证）的核心原语，要求盲性（签名者无法从会话中获知消息）和单次额外不可伪造性（用户不能生成超过会话次数的签名）。现有实用盲签名方案要么依赖双线性对（如基于Boneh-Boyen签名的构造[64]），要么依赖格（如基于MLWE的构造[34]），但前者在主流密码库（如BoringSSL）中缺乏支持且性能瓶颈显著，后者尚未完成标准化。另一条路线是盲RSA[26]及其变体，其效率极高（签名768B，通信384B），但安全性依赖交互式假设（one-more RSA）和随机预言机模型，这类假设非标准且具适应性。本文试图填补的空白是：在不使用配对或格的前提下，基于标准非交互假设（强RSA假设和DDH假设）构造轮最优（两轮）盲签名方案，且安全性在随机预言机模型中可证。

### 相关工作

[23] Chairattana-Apirom et al. PI-cut-choo and friends: compact blind signatures via parallel instance cut-and-choose and more. **CRYPTO 2022** [Google Scholar](https://scholar.google.com/scholar?q=PI-cut-choo+and+friends)
> 核心思路：基于RSA的盲签名，通过并行实例切割-选择技术实现紧凑签名。
> 局限与区别：需要5轮交互且签名者维持状态，通信量线性增长于并发会话数；本文实现轮最优且无状态。

[24] Chairattana-Apirom et al. Pairing-free blind signatures from CDH assumptions. **ePrint 2023** [Google Scholar](https://scholar.google.com/scholar?q=Pairing-free+blind+signatures+from+CDH+assumptions)
> 核心思路：独立并发工作，基于CDH假设构造无配对盲签名。
> 局限与区别：其构造需4轮交互且满足较弱形式的一次额外不可伪造性，通信和签名大小（分别为26KB和10KB）均大于本文（10.98KB和4.28KB）。

[26] Chaum. Blind signatures for untraceable payments. **CRYPTO'82** [Google Scholar](https://scholar.google.com/scholar?q=Blind+signatures+for+untraceable+payments)
> 核心思路：提出首个盲签名方案（盲RSA），效率极佳。
> 局限与区别：安全性依赖one-more RSA这一交互式假设，而本文依赖非交互标准假设（sRSA和DDH）。

[38] Fischlin. The Cramer-Shoup strong-RSA signature scheme revisited. **PKC 2003** [Google Scholar](https://scholar.google.com/scholar?q=The+Cramer-Shoup+strong-RSA+signature+scheme+revisited)
> 核心思路：提出基于强RSA的Cramer-Shoup签名变体（本文记为$S_{\mathsf{fis}}$）。
> 局限与区别：原签名不含盲性且不利于零知识证明；本文通过替换XOR为加法掩码使其与Pedersen承诺兼容，并设计高效NIZK证明知识。

[39] Fischlin. Round-optimal composable blind signatures in the common reference string model. **CRYPTO 2006** [Google Scholar](https://scholar.google.com/scholar?q=Round-optimal+composable+blind+signatures+in+the+common+reference+string+model)
> 核心思路：提出通用框架，通过带all-but-one归约的签名方案构造轮最优盲签名。
> 局限与区别：原框架依赖配对实例化；本文采用其变体[64]并结合非配对签名。

[64] Katsumata et al. Practical round-optimal blind signatures in the ROM from standard assumptions. **Asiacrypt 2023** [Google Scholar](https://scholar.google.com/scholar?q=Practical+round-optimal+blind+signatures+in+the+ROM+from+standard+assumptions)
> 核心思路：改进Fischlin框架，用Boneh-Boyen签名和Pedersen承诺实例化，得基于配对的高效盲签名。
> 局限与区别：仍依赖双线性对；本文将其框架迁移至RSA+DDH环境，需解决承诺兼容性、子版本零知识、轮数优化等问题。

[32] Cramer, Shoup. Signature schemes based on the strong RSA assumption. **ACM CCS 99** [Google Scholar](https://scholar.google.com/scholar?q=Signature+schemes+based+on+the+strong+RSA+assumption)
> 核心思路：提出Cramer-Shoup签名，基于强RSA假设。
> 局限与区别：本文的签名变体$S_{\mathsf{fis}}$源自该方案，但调整算法以支持零知识证明。

[12] Bellare et al. The one-more-RSA-inversion problems and the security of Chaum’s blind signature scheme. **Journal of Cryptology 2003** [Google Scholar](https://scholar.google.com/scholar?q=The+one-more-RSA-inversion+problems+and+the+security+of+Chaum%27s+blind+signature+scheme)
> 核心思路：形式化one-more RSA假设并证明盲RSA的安全性。
> 局限与区别：本文依赖非交互的标准假设（sRSA和DDH）而非交互式假设。

[30] Couteau et al. Sharp: short relaxed range proofs. **ACM CCS 2022** [Google Scholar](https://scholar.google.com/scholar?q=Sharp:+short+relaxed+range+proofs)
> 核心思路：提出一种基于整数论的高效宽松范围证明，使用额外RSA模数提取整数。
> 局限与区别：本文利用该技术构造松弛范围证明以证明签名中$(e,a)$的范围，从而压缩NIZK证明大小。

[20] Bünz et al. Bulletproofs: short proofs for confidential transactions and more. **IEEE S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Bulletproofs:+short+proofs+for+confidential+transactions+and+more)
> 核心思路：基于内积论证的通用范围证明，适用于大范围。
> 局限与区别：对于本文所需的松弛范围（如$a\in[0,2^{384}]$），Bulletproofs证明生成需约1.6ms且证明大小约932B；本文提出的专用松弛范围证明更紧凑（仅额外784B模数），且无缝融入复杂Σ-协议。

### 核心技术与方案

**整体框架**：本文的盲签名构造遵循Katsumata等[64]提出的Fischlin变体框架。该框架要求底层签名方案具有“all-but-one”归约性质，且存在可加同态承诺方案与之兼容。具体而言，若签名算法$\mathsf{Sign}(\mathsf{sk},m)$可重写为$\widehat{\mathsf{Sig}}(\mathsf{sk},\mathsf{Com}(m;r)) - \mathsf{Com}(0;r)$（其中减法指同态运算），则可设计两轮盲签名：用户发送承诺$c=\mathsf{Com}(m;r)$，签名者返回$\hat\sigma=\widehat{\mathsf{Sig}}(\mathsf{sk},c)$，用户最终同态移除$\mathsf{Com}(0;r)$得正规签名。框架要求用户额外附上在线可提取的NIZK以证明$c$确实形成正确。由于原框架依赖配对实例化，本文将其核心思想迁移至RSA+DDH环境。

**底层签名变体**：本文采用Fischlin[38]提出的Cramer-Shoup签名变体（记为$S_{\mathsf{fis}}$），该方案验证方程为$y^e \equiv h \cdot h_1^a \cdot h_2^{a+\mathsf{H}(m)} \pmod{N}$，其中$a\in[0,2^{3\lambda}]$，$e$取自特定素数区间。为使方案与Pedersen承诺兼容，作者将原版中的XOR运算（$a\oplus m$）替换为加法掩码（$a+m$），从而允许承诺$c=h_2^m \cdot g^{r\cdot e}\pmod{N}$融入签名交互。签名者收到$c$后计算$y_r$满足$y_r^e \equiv h\cdot h_1^a \cdot h_2^a \cdot c \pmod{N}$，用户则通过$y \leftarrow y_r \cdot g^{-r}\pmod{N}$恢复合法签名$(e,a,y)$。

**轮数优化**：框架要求签名者先选择素数$e$，但用户需在发送承诺前知道$e$以计算$r\cdot e$。本文的解决方案是：用户首先对$(m,r)$进行整数承诺$c_Z$（使用ElGamal承诺），然后通过哈希函数$\mathsf{H}_\mathbb{P}(c_Z)$导出$e$，再计算$c=h_2^m\cdot g^{r\cdot e}\pmod{N}$。同时，签名者从伪随机函数$\mathsf{H}_{\mathsf{prf}}(c\|c_Z)$导出掩码$a$，确保对相同承诺对$(c,c_Z)$重用$a$以支持归约。用户还附加NIZK $\pi_{\mathsf{ped}}$证明$c$与$c_Z$的一致性，该NIZK具备部分在线可提取性，使归约能在签名前提取$(m,r)$。

**恶意盲性**：为抵抗恶意选择验证密钥的攻击，本文要求NIZK具有子版本零知识（即即使公钥中的crs被恶意生成，零知识仍成立）。具体地，crs被拆分为均匀部分urs（由随机预言机生成）和结构化部分srs（可检验成员资格），从而标准NIZK可在ROM下达到子版本安全。此外，针对Pedersen承诺在$\mathbb{Z}_N^*$中不隐藏的问题（若$\langle g\rangle \subsetneq \langle h_2\rangle$），签名者必须在验证密钥中附带NIZK $\pi_{\mathsf{gen}}$证明所有$\mathsf{QR}_N$元素生成相同子群。用户还需检查$c$和$y_r$均属于该子群，这依赖于引理2：对任意$e\gets S_e$，$\langle g^e\rangle=\langle g\rangle$以压倒性概率成立。

**一次额外不可伪造性**：证明采用与$S_{\mathsf{fis}}$类似的归约策略：归约者猜测敌手伪造的$(e,a)$格式（是否重用签名会话中的素数$e$，以及$a$是否等于$a_j$或$a_j+\overline{m}_j\neq a^*+\overline{m}^*$），然后以该猜测方式“穿刺”设置验证密钥，使得在不信任因数分解的情况下仍能签名所有会话，并在最后从敌手的NIZK $\pi_{\mathsf{fis}}$中提取签名并归约到sRSA。为防止提取过程受猜测影响，用户必须在输出签名前用完美绑定承诺$C_{\mathsf{RInt}}$固定$(e,a)$，确保提取出的值独立于猜测。

**高效NIZK实例化**：主要包括：(1) 松弛整数承诺$C_{\mathsf{RInt}}$，基于ElGamal承诺加松弛范围检验（保证$a$在$[-AT,AT]$内，$e-\overline{E}$在$[-ET,ET]$内），其NIZK $\Pi_{\mathsf{int}}$通过简单的Σ-协议编译Fiat-Shamir得到，额外添加$C_{\mathsf{RInt}}$的ElGamal打开及一个短整数承诺（基于额外RSA模数$\tilde{N}$）以提取整数。(2) 群元素承诺$\mathsf{C}_{\mathsf{Grp}}$，用于承诺未知阶群中的元素$y$，其通过$C_{\mathsf{RInt}}$承诺随机指数$s$并计算$\hat c = y\cdot \hat g^s$实现绑定，同样可通过Σ-协议证明打开。(3) 整体NIZK $\Pi_{\mathsf{fis}}$组合以上技术：用$C_{\mathsf{RInt}}$固定$(e,a)$，用$\mathsf{C}_{\mathsf{Grp}}$固定$y$，再通过承诺相等技术证明$y^e\equiv h\cdot h_1^a\cdot h_2^{a+\overline{m}}\pmod{N}$。

**复杂度**：签名大小4.28 KB，通信大小10.98 KB（包括用户发送的$(c,c_Z,\pi_{\mathsf{ped}})$和签名者返回的$(y,a)$以及最终签名$(\pi_{\mathsf{fis}},c_I)$）。计算量方面，签名者和用户均执行常数次模指数运算（约20-30次）和若干哈希计算。

### 核心公式与流程

**[原始签名验证方程]**
$$y^e \equiv h\cdot h_1^a\cdot h_2^{a+\mathsf{H}(m)} \pmod{N}$$
> 作用：定义$S_{\mathsf{fis}}$签名的正确性条件，其中$a\in[0,2^{3\lambda}]$，$e$为特定区间素数。

**[承诺格式]**
$$c = h_2^{\overline{m}} \cdot g^{r\cdot e} \pmod{N}$$
> 作用：用户发送的盲化承诺，其中$e=\mathsf{H}_\mathbb{P}(c_Z)$源自整数承诺$c_Z$对$(\overline{m},r)$的承诺。

**[预签名计算]**
$$y_r^e \equiv h\cdot h_1^a\cdot h_2^a\cdot c \pmod{N}$$
> 作用：签名者计算$y_r$，用户通过$y\leftarrow y_r\cdot g^{-r}$恢复完整签名。

**[最终盲签名输出]**
$$\sigma = (\pi_{\mathsf{fis}}, c_I), \quad c_I = C_{\mathsf{RInt}}.\mathsf{Commit}(\mathsf{pp}_I, (a, e-\overline{E}); r_I)$$
> 作用：用户通过NIZK $\pi_{\mathsf{fis}}$证明知道一个$S_{\mathsf{fis}}$签名$(e,a,y)$满足验证方程，且$(e,a)$完美绑定于$c_I$。

**[图1协议流程]** 见论文Fig. 1，综合展示了上述四轮交互（实际上因用户首轮同时发送$c$和$c_Z$可压缩为两轮）。

### 实验结果

**实验设置**：本文未提供实际实现评测，但基于参数分析给出具体数值（$\lambda=128$，RSA模数3072 bit，素数群阶$p\approx 2^{256}$）。主要性能数据来自表1。

**核心性能数值**：签名大小4.28 KB（含NIZK $\pi_{\mathsf{fis}}$和$c_I$），通信大小10.98 KB（含$(c,c_Z,\pi_{\mathsf{ped}})$和签名者返回的$(y,a)$以及最终签名）。相比之下，盲RSA[26]签名仅768 B且通信384 B，但基于交互式假设；[23]方案签名8.66 KB且通信8.08 KB，但需5轮交互且有状态；[64]的最佳配对实例化签名447 B且通信303 B（基于SXDH），但依赖配对；[34]格子方案签名100 KB且通信850 KB。

**与baseline对比**：本文签名大小约为[23]方案（8.66 KB）的一半，且具有轮最优、无状态优势；约为盲RSA的5.6倍，但避免了one-more RSA这一交互式假设。在计算效率上，本文使用标准RSA和群操作，预期与盲RSA相近（均需模指数），但额外需约10KB通信和多个NIZK验证。

**适用规模**：安全参数$\lambda=128$时，RSA模数3072 bit；消息空间为任意比特串（通过哈希映射到$[0,2^{2\lambda}-1]$）；支持多项式次并发签名会话（安全性证明在ROM下对有界多项式敌手成立）。

### 局限性与开放问题
本文的盲签名仍然依赖强RSA假设和DDH假设，且需要在经典群和RSA模数中同时工作，导致签名大小（4.28 KB）和通信（10.98 KB）远大于配对型方案（如[64]的447 B签名）或盲RSA（768 B签名）。此外，安全性证明在随机预言机模型中进行，且需要多个强原语（如在线可提取NIZK、子版本零知识），增加了参数选取的复杂性。开放问题包括：能否进一步压缩签名至1 KB级别？能否基于更弱的假设（如CDH而非DDH？）实现？以及如何构造标准模型下的无配对盲签名。

### 强关联论文

[26] Chaum. Blind signatures for untraceable payments. **CRYPTO'82** [Google Scholar](https://scholar.google.com/scholar?q=Blind+signatures+for+untraceable+payments)

[38] Fischlin. The Cramer-Shoup strong-RSA signature scheme revisited. **PKC 2003** [Google Scholar](https://scholar.google.com/scholar?q=The+Cramer-Shoup+strong-RSA+signature+scheme+revisited)

[39] Fischlin. Round-optimal composable blind signatures in the common reference string model. **CRYPTO 2006** [Google Scholar](https://scholar.google.com/scholar?q=Round-optimal+composable+blind+signatures+in+the+common+reference+string+model)

[64] Katsumata et al. Practical round-optimal blind signatures in the ROM from standard assumptions. **Asiacrypt 2023** [Google Scholar](https://scholar.google.com/scholar?q=Practical+round-optimal+blind+signatures+in+the+ROM+from+standard+assumptions)

[23] Chairattana-Apirom et al. PI-cut-choo and friends: compact blind signatures via parallel instance cut-and-choose and more. **CRYPTO 2022** [Google Scholar](https://scholar.google.com/scholar?q=PI-cut-choo+and+friends)

[24] Chairattana-Apirom et al. Pairing-free blind signatures from CDH assumptions. **ePrint 2023** [Google Scholar](https://scholar.google.com/scholar?q=Pairing-free+blind+signatures+from+CDH+assumptions)

[32] Cramer, Shoup. Signature schemes based on the strong RSA assumption. **ACM CCS 99** [Google Scholar](https://scholar.google.com/scholar?q=Signature+schemes+based+on+the+strong+RSA+assumption)

[12] Bellare et al. The one-more-RSA-inversion problems and the security of Chaum’s blind signature scheme. **Journal of Cryptology 2003** [Google Scholar](https://scholar.google.com/scholar?q=The+one-more-RSA-inversion+problems+and+the+security+of+Chaum%27s+blind+signature+scheme)

[30] Couteau et al. Sharp: short relaxed range proofs. **ACM CCS 2022** [Google Scholar](https://scholar.google.com/scholar?q=Sharp:+short+relaxed+range+proofs)

[20] Bünz et al. Bulletproofs: short proofs for confidential transactions and more. **IEEE S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Bulletproofs:+short+proofs+for+confidential+transactions+and+more)


## 关键词

+ 无配对盲签名标准假设ROM
+ 强RSA DDH最优轮次盲签名
+ NIZK友好签名Fischlin框架
+ 次要零知识大范围放松范围证明
+ 隐私支付电子投票匿名凭证