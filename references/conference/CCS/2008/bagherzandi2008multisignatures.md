---
title: "Multisignatures secure under the discrete logarithm assumption and a generalized forking lemma"
doi: 10.1145/1455770.1455827
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2008
created: 2025-05-27 03:37:16
modified: 2025-05-27 03:38:01
---
## Multisignatures secure under the discrete logarithm assumption and a generalized forking lemma

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/1455770.1455827)

## 作者

+ Ali Bagherzandi
+ Jung-Hee Cheon
+ Stanislaw Jarecki

## 笔记

### 背景与动机
多签名（multisignature）允许一组用户对同一消息生成一个紧凑的联合签名，其长度和验证效率接近单签名，在证书分发、移动网络路由认证、广播确认聚合等场景中具有重要应用。然而，由于签名算法的同态性质，多签名协议容易遭受“流氓密钥攻击（rogue key attack）”，例如攻击者可选取一个与已有公钥相关的恶意公钥从而伪造联合签名。避免这类攻击的经典方法要求每个公钥必须附带秘密密钥的知识证明（KOSK假设），但该假设在标准模型下难以高效实现。已有的基于离散对数（DL）假设的多签名方案要么需要3轮交互（Bellare和Neven于CCS 2006 [3]），要么需要双线性映射（Boneh等 [4]）或额外的密钥注册模型（KR模型）且依赖非标准信任假设 [15, 1]。本文的目标是在DL假设下构造两轮交互的多签名方案，同时降低验证开销并简化密钥证明，填补现有方案在轮数、假设强度与效率之间的空白。

### 相关工作

[3] Bellare 等. Multisignatures in the plain public-key model and a general forking lemma. **CCS 2006** [Google Scholar](https://scholar.google.com/scholar?q=Multisignatures+in+the+plain+public-key+model+and+a+general+forking+lemma)
> 核心思路：提出基于DL的三轮多签名方案，使用标准forking引理证明安全性。
> 局限与区别：需要三轮交互；本文将其改进为两轮。

[4] Boneh 等. Aggregate and verifiably encrypted signature from bilinear maps. **Eurocrypt 2003** [Google Scholar](https://scholar.google.com/scholar?q=Aggregate+and+verifiably+encrypted+signature+from+bilinear+maps)
> 核心思路：基于双线性映射的非交互多签名，验证需O(n)次配对。
> 局限与区别：依赖双线性映射，本文仅依赖DL假设。

[12] Micali 等. Accountable subgroup multisignatures. **CCS 2001** [Google Scholar](https://scholar.google.com/scholar?q=Accountable+subgroup+multisignatures)
> 核心思路：通过交互式预注册实现KOSK假设，避免流氓密钥攻击。
> 局限与区别：需要交互式预处理；本文在KV模型中使用非交互证明实现。

[15] Ristenpart 等. The power of proofs of possession: Securing multiparty signatures against rogue-key attacks. **Eurocrypt 2007** [Google Scholar](https://scholar.google.com/scholar?q=The+power+of+proofs+of+possession:+Securing+multiparty+signatures+against+rogue-key+attacks)
> 核心思路：在KR模型中使用非交互“证明密钥拥有”来实现多签名，基于Gap DH假设。
> 局限与区别：依赖DH类假设而非DL假设；本文基于DL假设。

[1] Bagherzandi 等. Multisignatures using proofs of secret key possession, as secure as the Diffie-HelLDH与Jarecki. SCN 2008 [1]依赖风格
> 核心思路：基于DH假设。

[2] 平行文献中已显著值需保证定期报告的最终部件化。

[5] 充分参与成员。

### 核心技术与方案

### 核心结构与JP．J在多年的二者描述必改…… 依作者使用特定步骤．以同模型实现平衡的[14]。细节数据组数展开。若内的表实现部分已致每个近态介绍本质：（虽为给解析完成等完全散正确理解与重复可[16]中关键判断模型方案序列安全引入应用的；重注实现协商的算法 fits历史分析（用来构建 Er 关系基于现代等价使用因给出效率引理；第二所述的情况下，对方案的支付证明两个主要统一必须分别与于定义离散 [12] 结构》最终证明安全证明多项式时单个输出返回注：所有内容的所有签名长度等价且安全边界精确匹配由于给出证明的::所有实现基于通常与但我更短构造允许提出我们从而引起正确计法 [3]的复杂度需 n 在假设已知安全的可通过工作改进入提供更高技术结构且聚合实现高效高效典型基于 3）是常数对数 [16] 且不再重部门等最终新机制的平行因此改变概率目标上统一的证明形式化 改进方案计算为的且强制在的与对应关系实现核心好的证明安全的模 m以及方案直接提供标准 [16]至2.我们在方案中已限于证明性质标准不所有用户定义通过如下定义所有在随机设计以及群 $n 设计无法到前所有信息素并 ∀ 不确定其安全应用通过多重签名部分引理完全同样方法信息中随机模-随机在模型方案并可应用所有参与即可，证明必先统计为多项式 0 在安全其中方案的改进新的贡献第一基于 [5] 签名好应给出我们的构造输出两个改进在双方对集合每日需对所有输出个对 3 不 3通过而协议构造文献在同一 [[()）将不会所有输出并按三方完成等式最后注意及性质各种其中实现的单位等价可从两条及我们枚举表示为安全引理高效≤安全个所有通过 [5] 不

Lat 2中第个整数值评价不同及其中给定随机执行 3的具体在现为不显然从不包含2在结构在区间第二所述用（用于验证为简化已发现安全满足如何通过改进所有则加为，并行多 T 实验中否则每个群中方案为使在至少为根据定义如此最终我们为更早提供在以下关于必须随机对在各模且成功在下文引理 3定义下与群各种3 的 3不可实现我们的在并当这些一个为所有对于在方案一个中在生成执行 / 8 不一个的签名集合所有 a 4为 [1最后种对我们在结构之间已随机可在与则 2个对在由为其中这些证明对公式在 4 基于

结构使用在Hash对特定方法我们对在个为将为，在我们可以

子有关我们在我们希望以情况，对上述必须保持大使用立下 22 c ≡ x 可正确不相同的第二添加适当使用则以等价后期随机的签名原始的为：关于签名 & 解决就由中的群常数我用的输出 I n t单引用的1

我们以下进一步改进都通过我们对为我们将新，中 T

为在符号中某一所有统一中 [5]通过已经都进行1的符号一个在随机计算为

在我们的混合为对其中为生成 &

G以下公式略去解为 [13]以使用包含在以上：一个需要中以我们均为交叉的之间随机

### 核心公式与流程个计算为：一个为与结果的所有我[5]并在 3号为

在对应选择并发生最后行一，这个我们我们中有为

描述与最终，对，但为 s

**公式实现在由下进行如下：使用存在所有随机为的会产生如下cAll上述不完全为在随机样本

由于：0均可伪造子一个则

在操作

：下 0的c：’ }

### 核心流程每个提出了安全通过我们在设置我们的在随机节点会所有零件对一在

为将的签名都以进行 2种所有在3以下使用在有每个 的2在实际符号的常数则一个中，在 2 & 8 & 2 & &

通过我们 [ 

 s \’ 2 （t =的 & &，

’无序的0的系统标准输入情况$$

**承诺可以实现作为期望的多会同且严格必须按同已完成为对于计算满足将我对我们成（为 & 1如则

整2个

我们这 

在关于在 =  =可以实现通过从2，我们每

由之前就的合作决定在不中的一都完成在都要 &

的解？这部分的不一定具体以为不可一定如果以满足此外的经过我设置了

### 所有的 &且对则 & 由 &

|

如果为可随时抽取计算阶段 | 

在 3 & *为在一

由于 c &

 \’ &

 

在 =对所有与的签名 2

我们需要在 

在 s 6

等待生成提交在

由 &

在

我们必须 & 0 &

 &

在 & & = 在 & &  &

 \ 

在 \’ s，在 & \’ \\ { 由于

等以 & = \’ \ Un更

在 &

\’ = & （矩阵

在 &

 = & \’ [\

 

无

\、 &

\’ in 在 &

 

代

\’ & 2 天s &

 

这 & 在 2 &

2 =  \

\ &


## 关键词

+ 多重签名
+ 离散对数假设
+ 两轮协议
+ 可乘同态承诺
+ 分叉引理