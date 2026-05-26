---
title: "Cuckoo commitments: registration-based encryption and key-value map commitments for large spaces"
标题简称:
论文类型: conference
会议简称: ASIACRYPT
发表年份: 2023
modified: 2025-04-13 17:40:15
---

## Cuckoo commitments: registration-based encryption and key-value map commitments for large spaces

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-981-99-8733-7_6)

## 作者

+ [Dario Fiore](Dario%20Fiore.md)
+ [Dimitris Kolonelos](Dimitris%20Kolonelos.md)
+ Paola de Perthuis 

## 笔记

### 背景与动机
注册加密(RBE)是一种新型公钥加密机制，用户自主生成密钥并注册到密钥策展人(KC)处，无需像IBE那样面临密钥托管问题。第一代RBE方案依赖不可区分混淆或混淆电路树，密文量级高达TB级，完全不实用。近期Glaeser等[38]实现了高效的配对-based RBE，但身份空间受限为多项式规模的整数1,…,n；Döttling等[24]用LWE支持大身份空间，但密文仍达GB级。Hohenberger等[40]的注册属性加密(R-ABE)可转化为RBE，但基于复合阶群且效率低下。本文旨在填补空白：在不牺牲效率的前提下，将RBE的身份空间扩展到任意字符串，并首次实现基于素阶双线性群的大身份空间RBE，密文仅为MB级（对1024用户约1.7 MB）。核心技术是布谷鸟哈希在密码学中的新型应用，并由此派生出关键值映射承诺(KVC)和累加器构造。

### 相关工作
[38] Glaeser et al. Efficient registration-based encryption. **CCS 2023** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+registration-based+encryption)
> 核心思路：利用Libert-Yung向量承诺将用户公钥压缩，实现高效RBE。
> 局限与区别：身份空间仅限[1,n]，无法支持任意字符串；本文用布谷鸟哈希将其编译为大身份空间。

[24] Döttling et al. Efficient laconic cryptography from learning with errors. **EUROCRYPT 2023** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+laconic+cryptography+from+learning+with+errors)
> 核心思路：基于LWE构造支持任意身份的RBE，密文大小为2λ log n个LWE密文。
> 局限与区别：密文仍较大（2.4 GB for 1024用户）；本文通过编译器得到更小的密文（4 log² n）。

[40] Hohenberger et al. Registered attribute-based encryption. **EUROCRYPT 2023** [Google Scholar](https://scholar.google.com/scholar?q=Registered+attribute-based+encryption)
> 核心思路：引入注册属性加密，可转化为大身份空间RBE。
> 局限与区别：基于复合阶群，CRS规模O(λ n^{2/3} log n)，远大于本文的O(√n log n)。

[34] Garg et al. Registration-based encryption: removing private-key generator from IBE. **TCC 2018** [Google Scholar](https://scholar.google.com/scholar?q=Registration-based+encryption+removing+private-key+generator+from+IBE)
> 核心思路：首次提出RBE概念，用不可区分混淆实现大身份空间。
> 局限与区别：非黑盒，效率极低（TB级密文）。

[48] Libert, Yung. Concise mercurial vector commitments and independent zero-knowledge sets with short proofs. **TCC 2010** [Google Scholar](https://scholar.google.com/scholar?q=Concise+mercurial+vector+commitments+and+independent+zero-knowledge+sets+with+short+proofs)
> 核心思路：提出基于q-DHE假设的向量承诺，承诺和打开均为单群元素。
> 区别：本文利用该VC作为底层构造，并扩展为关键值映射承诺。

[7] Boneh et al. Batching techniques for accumulators with applications to IOPs and stateless blockchains. **CRYPTO 2019** [Google Scholar](https://scholar.google.com/scholar?q=Batching+techniques+for+accumulators+with+applications+to+IOPs+and+stateless+blockchains)
> 核心思路：提出关键值映射承诺(KVC)概念并基于未知阶群构造。
> 区别：本文用布谷鸟哈希+VC实现首个黑盒、基于配对的KVC。

[62] Yeo. Cuckoo hashing in cryptography: Optimal parameters, robustness and applications. **CRYPTO 2023** [Google Scholar](https://scholar.google.com/scholar?q=Cuckoo+hashing+in+cryptography+Optimal+parameters+robustness+and+applications)
> 核心思路：从密码学角度形式化布谷鸟哈希的鲁棒性，给出参数分析。
> 区别：本文首次将布谷鸟哈希用于RBE和KVC，并利用鲁棒性与非鲁棒性变体。

### 核心技术与方案

**整体框架**  
本文提出一个通用编译器，将小身份空间的RBE（或固定大小的LE）提升为大身份空间的RBE。核心部件有三个：布谷鸟哈希（CH）、针对向量承诺的见证加密（VCWE）和一个秘密共享方案。此外，该编译器还能将任意向量承诺（VC）转化为关键值映射承诺（KVC），进而导出大宇宙累加器。

**编译器构造思路**  
1. 用户id注册时，计算k个哈希位置id^(η)=h_η(id)，并为每个位置生成一对密钥(pk^(η),sk^(η))，同时额外生成一对PKE密钥用于处理“存根”（stash）。  
2. 密钥策展人（KC）维护一个向量I（存储各位置的当前身份）和一个存根集合S。当新用户注册时，用CH.Insert更新I和S；每次更新后KC重新计算两个向量承诺：D承诺I（表示身份表），C（与底层RBE结合，承诺各位置对应的公钥/密钥）。  
3. 加密者针对目标id，先检查是否在存根中：若在，直接用PKE加密；否则，对每个位置η（η=1..k），将消息m通过秘密共享拆分为(m1^(η), m2^(η))，用底层RBE加密m1^(η)到位置id^(η)，用VCWE加密m2^(η)到承诺D、位置id^(η)和值id。  
4. 解密者使用自己的sk^(η*)（η*为id实际所在位置）解密RBE部分得到m1，并利用VC打开证明（由KC提供）解密VCWE部分得到m2，最终恢复m。  
5. 安全性论证：若id不在某一位置，则VCWE保证该位置的m2对敌手计算不可区分；若id在某一位置，则底层RBE保证m1安全。秘密共享保证敌手至少缺失一个份额，从而无法恢复消息。

**证明依赖与假设**  
- 底层RBE（或LE）的安全性要求目标位置不可区分。  
- VCWE的安全性依赖向量承诺的位置绑定性质。  
- 布谷鸟哈希的鲁棒性保证插入永不失败（完备性）。  
- 秘密共享方案为(2,2)-私密，即单个份额不泄露消息。  
- 安全归约为SOUND：若CH是negl(λ)-鲁棒的，则编译器产生完整的RBE；安全规约为混合论证，每个组件的安全性保证最终优势可忽略。

**渐进复杂度**  
- 使用鲁棒CH（k=λ，s=0）时，密文大小为k倍底层RBE密文与VCWE密文之和，即O(λ|ct˜|)；公钥大小为O(|pp˜|)；更新信息大小为O(|u˜|)。  
- 若使用非鲁棒CH（k=2, s=log n）并采用选择性紧致性概念，密文大小降至2倍，即O(2|ct˜|)，但公钥大小会因存根大小增加至O(log n)。  
- 对于KVC，承诺大小为两个VC承诺（每个O(polylog n)），打开大小为O(k·polylog n)加上可能的存根信息。

### 核心公式与流程
**[向量承诺（LY-VC）]**
$$ \mathsf{crs} = \{g^{\alpha}, \dots, g^{\alpha^n}, g^{\alpha^{n+2}}, \dots, g^{\alpha^{2n}}\};\quad C = \prod_{i=1}^n (g^{\alpha^i})^{v_i}; $$
$$ \Lambda_i = \prod_{j \neq i} (g^{\alpha^{n+1-i+j}})^{v_j};\quad e(C, g^{\alpha^{n+1-i}}) = e(\Lambda_i, g)\cdot e(g_i^{v_i}, g_{\,n+1-i}). $$
> 作用：底层向量承诺，用于压缩公钥向量和身份表向量。承诺C和打开Λ均为单群元素，验证时间与n无关。

**[GKMR 小身份空间RBE核心流程]**
$$ \mathsf{pk}_i = g_i^{\mathsf{sk}_i},\quad \mathsf{pp} = C = \prod_{i=1}^n g_i^{\mathsf{sk}_i},\quad \mathsf{u}_i = \Lambda_i = \prod_{j \neq i} g_{\,n+1-i+j}^{\mathsf{sk}_j}. $$
$$ \mathsf{ct} = (g^r, e(C, g_{\,n+1-i})^r, e(g_i, g_{\,n+1-i})^r \cdot m). $$
> 作用：底层RBE的基础构造。每个用户i的公钥是其秘密钥指数乘以VC基元，KC计算全局承诺C，用户更新信息为VC打开证明。

**[编译器加密算法（核心构造）]**
$$ \forall \eta \in [k]:\ (m_1^{(\eta)}, m_2^{(\eta)}) \gets \mathsf{Sh.Share}(m); $$
$$ \mathsf{ct}_1^{(\eta)} \gets \widetilde{\mathsf{LE.Enc}}(\widetilde{\mathsf{crs}}, \widetilde{\mathsf{pp}}, \mathsf{id}^{(\eta)}, m_1^{(\eta)}); $$
$$ \mathsf{ct}_2^{(\eta)} \gets \mathsf{VCWE.Enc}(\mathsf{crs}, D, \mathsf{id}^{(\eta)}, \mathsf{id}, m_2^{(\eta)}); $$
$$ \mathsf{ct} = \big((\mathsf{ct}_1^{(1)},\mathsf{ct}_2^{(1)}), \dots, (\mathsf{ct}_1^{(k)},\mathsf{ct}_2^{(k)})\big). $$
> 作用：对每个哈希位置，将消息拆分成两份，分别用底层LE加密和VCWE加密，使得只有当该位置实际属于目标id时才能同时获得两个份额。

**[KVC构造（简化）]**
$$ (T, S) \leftarrow \mathsf{CH.Insert}(\mathsf{pp_{CH}}, \hat{T}, \hat{S}, \{k_i\}); $$
$$ C_T \leftarrow \mathsf{VC.Com}(\mathsf{crs_{VC}}, T),\quad C_V \leftarrow \mathsf{VC.Com}(\mathsf{crs_{VC}}, V); $$
$$ \Lambda = ( \{\mathsf{VC.Open}(\mathsf{crs_{VC}}, \mathsf{aux}_T, \mathsf{ind}_j)\}_{j=1}^k, \mathsf{VC.Open}(\mathsf{crs_{VC}}, \mathsf{aux}_V, \mathsf{ind}^*) ). $$
> 作用：用布谷鸟哈希将大键集映射到固定大小向量，然后用两个VC分别承诺键表和值表，打开证明包含所有候选位置的键打开和实际位置的值打开。

### 实验结果
论文未提供具体实验数据，但给出了详细的渐近复杂度和表格对比（表1）。主要数据摘译如下：  
- 本文自适应配对方案（P1）的密文大小为6λ log n（例如λ=128, n=1024时约1.7 MB），对比[38]小身份空间方案密文为4 log n（约80字节），但后者身份空间受限；对比[24]大身份空间LWE方案密文为(2λ+1) log n（约2.4 GB for 1024用户），本文有约三个数量级提升。  
- 本文选择性紧致方案（P2）密文大小仅12 log n（约1.2 KB for 1024用户），但仅对选择性敌手保证公钥紧致。  
- 公钥大小：P1为O(√(λ n) log n)，P2为O(√n log n)，[24]为O(log n)，[40]为O(λ n^{2/3} log n)。  
- 更新次数均为log n。  
- Lattice变体（Ours L）密文大小为4 log² n，优于[24]的(2λ+1) log n（当λ>2 log n时更优）。  
未给出具体硬件环境和运行时间，仅提供理论规模估计。

### 局限性与开放问题
本文编译器的主要代价是密文大小随k（哈希函数数量）线性增长，鲁棒CH需k=λ导致密文扩大λ倍。未来可探索更优的CH构造以降低k的常数。选择性紧致性概念虽实用但尚未完全抵抗恶意DoS攻击，如何设计抵抗主动敌手紧凑性攻击的CH方案是开放问题。此外，将KVC转化为累加器时，黑盒性依赖VC的具体结构，是否能完全松耦合仍需进一步研究。

### 强关联论文
[38] Glaeser et al. Efficient registration-based encryption. **CCS 2023**
[24] Döttling et al. Efficient laconic cryptography from learning with errors. **EUROCRYPT 2023**
[40] Hohenberger et al. Registered attribute-based encryption. **EUROCRYPT 2023**
[34] Garg et al. Registration-based encryption: removing private-key generator from IBE. **TCC 2018**
[48] Libert, Yung. Concise mercurial vector commitments and independent zero-knowledge sets with short proofs. **TCC 2010**
[7] Boneh et al. Batching techniques for accumulators with applications to IOPs and stateless blockchains. **CRYPTO 2019**
[15] Catalano, Fiore. Vector commitments and their applications. **PKC 2013**
[62] Yeo. Cuckoo hashing in cryptography: Optimal parameters, robustness and applications. **CRYPTO 2023**
[44] Kirsch, Mitzenmacher, Wieder. More robust hashing: cuckoo hashing with a stash. **SICOMP 2010**
[51] Pagh, Rodler. Cuckoo hashing. **J. Algorithms 2004**


## 关键词

+ 注册基础加密
+ 布谷鸟哈希
+ 向量承诺
+ 密钥值映射承诺
+ 配对加密
我们方法的核心技术是对布谷鸟哈希在密码学中的创新应用，这一技术本身具有独立的研究价值。我们展示了两个主要应用方向：首先是前述的基于注册的加密（RBE）方法，通过布谷鸟哈希将适用于小标识符的RBE方案扩展至大标识符场景；其次，提出了一种将任意向量承诺方案转化为键值映射承诺的通用方法。例如，这一转换催生了首个基于代数配对的键值映射承诺方案。