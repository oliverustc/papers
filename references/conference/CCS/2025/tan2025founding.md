---
title: Founding Zero-Knowledge Proofs of Training on Optimum Vicinity
doi: 10.1145/3719027.3744862
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2025
modified: 2025-04-11 10:12:47
---
## Founding Zero-Knowledge Proofs of Training on Optimum Vicinity

## 发表信息

+ [archive](https://eprint.iacr.org/2025/053)
+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3719027.3744862)

## 作者

+ Gefei Tan
+ Adrià Gascón
+ [Sarah Meiklejohn](Sarah%20Meiklejohn.md)
+ [Mariana Raykova](Mariana%20Raykova.md)
+ [Xiao Wang](Xiao%20Wang.md)
+ [Ning Luo](Ning%20Luo.md)

## 笔记

### 背景与动机
现有零知识证明训练协议通过证明训练过程的每一步正确执行来保证模型正确性，其证明规模与训练迭代次数呈线性关系，导致效率瓶颈。更重要的是，现有协议中训练随机性由证明方选择，这为拒绝采样攻击提供了可能：证明方可以使用不同随机种子本地训练多个模型，并选择一个能使其预测产生特定偏向的模型参与协议。由于零知识证明仅验证训练算法是否被正确执行，而算法输入中的随机种子已被恶意选择，因此该攻击无法被检测。实验表明，仅用1000个不同随机种子，攻击者就能使高达13.5%的高置信度预测被翻转。为从根本上解决这一问题，本文提出不关注训练过程本身的“最优邻近”概念，转而直接证明模型与训练数据所确定的数学最优解之间的距离足够小。该定义规避了随机性引入的攻击面，且证明规模与训练迭代次数完全无关。

### 相关工作

[APKP24] Abbaszadeh等. Zero-knowledge proofs of training for deep neural networks. **ACM CCS 2024** [Google Scholar](https://scholar.google.com/scholar?q=Zero-knowledge%20proofs%20of%20training%20for%20deep%20neural%20networks)
> 核心思路：提出了针对深度神经网络的零知识证明训练方案。
> 局限与区别：该方案针对非凸模型，无法直接应用最优邻近概念；本文与之不直接可比，因为目标模型类别不同。

[GGJ+23] Garg等. Experimenting with zero-knowledge proofs of training. **ACM CCS 2023** [Google Scholar](https://scholar.google.com/scholar?q=Experimenting%20with%20zero-knowledge%20proofs%20of%20training)
> 核心思路：构建了针对逻辑回归和支持向量机的零知识证明训练原型，是本文最重要的直接对比基线。
> 局限与区别：其证明规模随训练轮次线性增长，且易受拒绝采样攻击；本文通过直接证明最优邻近，在安全性和效率上均有本质改进。

### 核心技术与方案

**1. 最优邻近定义与理论保障**

定义ε-邻近：对于给定的训练数据D和损失函数L，若存在唯一的数学最优模型w*使得损失最小化，则称一个模型w是ε-邻近的，当且仅当‖w - w*‖₂ ≤ ε。该定义不依赖于训练算法、硬件平台或随机种子，因而天然免疫拒绝采样攻击。进一步，若预测函数f(w, x)关于w是K-利普希茨连续的，则对于任意数据点x，有|f(w, x) - f(w*, x)| ≤ K·ε，即邻近模型的预测误差可被严格界限。对于逻辑回归（sigmoid预测，0.25-利普希茨连续），该界限为0.25·‖x‖₂·ε。

**2. 通过强凸性导出可验证的上界**

由于数学最优解w*一般无法显式计算，无法直接计算ε_real = ‖w - w*‖₂。关键洞察是利用损失函数的强凸性导出上界。设损失函数L是m-强凸的且连续可微，则对于任意模型w，有：
‖w - w*‖₂ ≤ (1/m)·‖∇L(w)‖₂，
其中右端项仅依赖于计算w处的梯度，无需知道w*。此上界记为ε_SC。由于强凸性参数m通常无显式公式，且依赖未知的w*，本文进一步引入L2正则化：(λ/2)·‖w‖₂²。正则化项是λ-强凸的，而原始损失（如逻辑损失或合页损失）是凸的。根据引理2，二者之和是λ-强凸的，因此λ ≤ m。代入得：
ε_reg = (1/λ)·‖∇L_λ(w)‖₂ ≥ ε_SC ≥ ε_real，
即正则化参数λ可作为一个保守的且易于计算的下界。步骤中的两个不等式引入了强凸性间隙Δ_sc和正则化间隙Δ_rg，但它们仅放大上界（使证明更宽松），不会破坏可靠性。

**3. 有限精度下的可靠性保持**

为在零知识证明中实际计算ε_reg，需要将实数运算转化为有限精度定点数运算。直接使用定点数可能引入负数误差，导致ε_fp < ε_reg，破坏可靠性。为此本文采用定点区间算术：每个实数a维护一个区间[ a_lo, a_hi ]，保证a_lo ≤ a ≤ a_hi。加法、减法、乘法的区间运算规则被设计为总能维持该不变性。对于乘法，需分别使用向下取整和向上取整计算四个端点乘积的最小和最大值。最终使用区间的上端点作为ε_fp，确保ε_fp ≥ ε_reg。

**4. 适配区间算术的Sigmoid逼近**

直接计算Sigmoid函数在零知识证明中开销巨大，而现有的分段线性逼近（如[GGJ+23]所用）是单一近似函数，无法同时提供严格的下界和上界，因此不能直接用于区间算术。本文提出双函数逼近：分别构造两个分段线性函数σ_lo(z)和σ_hi(z)，满足对任意实数z，σ_lo(z) ≤ σ(z) ≤ σ_hi(z)。利用sigmoid在正半轴凹、负半轴凸的性质，在每个子区间内选择切线（提供上界或下界）或弦线（提供相反的界），在远端的饱和区域则直接使用渐近值加上一个小偏移ε_fp，以提高精度。这样，对任意输入区间[z_lo, z_hi]，输出区间[σ_lo(z_lo), σ_hi(z_hi)]严格包含真值，保证可靠性。逼近误差可通过增加子区间数来降低。

**5. 协议与安全性**

协议Π_VIC-ZK在混合模型中运行，证明方提交模型w和数据集D的承诺，双方协商一个公知的布尔电路C，该电路计算条件ε ≥ (1/λ)·‖∇L(w)‖₂并输出1当且仅当条件成立。将电路交由底层的零知识证明功能F_ZK实例化即可。安全性证明（定理5）采用标准模拟范式：对于恶意证明方，模拟器提取其输入的w和D，并在理想功能中检查电路是否成立，从而确保输出一致；对于恶意验证方，模拟器仅需发送ture/⊥即可完美模拟其视图。证明依赖于定理2中由强凸性保证的⊇SC ≥ ε_real这一不等式，因此任何通过电路检查的模型在理想功能中也必然通过检查，保证输出一致性。

### 核心公式与流程

**[ϵ-邻近的定义与理论界限]**
$$ \| \boldsymbol{w} - \boldsymbol{w}^* \|_2 \le \epsilon \quad \text{(ε-邻近)} $$
$$ \left| f(\boldsymbol{w}, \boldsymbol{x}) - f(\boldsymbol{w}^*, \boldsymbol{x}) \right| \le K \cdot \epsilon \quad \text{(预测误差界限)} $$
> 作用：定义最优邻近概念，并建立与预测性能的定量联系。

**[通过强凸性和正则化导出可验证上界]**
$$ \| \boldsymbol{w} - \boldsymbol{w}^* \|_2 \le \frac{1}{m} \| \nabla\mathcal{L}(\boldsymbol{w}) \|_2 \le \frac{1}{\lambda} \| \nabla\mathcal{L}(\boldsymbol{w}) \|_2 = \epsilon_{\text{reg}} $$
> 作用：将不可计算的真实距离转化为仅依赖梯度计算的保守上界，其中λ是已知的正则化参数。

**[定点区间算术的乘法定义]**
$$ [a,b] \cdot_{\text{fp}} [c,d] = [\min(S_{\text{lo}}), \max(S_{\text{hi}})] $$
其中 $S_{\text{lo}} = \{ a \cdot_{\text{lo}} c, a \cdot_{\text{lo}} d, b \cdot_{\text{lo}} c, b \cdot_{\text{lo}} d \}$ ，$S_{\text{hi}} = \{ a \cdot_{\text{hi}} c, a \cdot_{\text{hi}} d, b \cdot_{\text{hi}} c, b \cdot_{\text{hi}} d \}$，$\cdot_{\text{lo}}$ 和 $\cdot_{\text{hi}}$ 分别为向下和向上取整乘法。
> 作用：确保运算结果的上界始终不小于真值，从而维持可靠性。

**[协议Π_VIC-ZK的核心论证电路]**
$$ \mathcal{C}_{\mathcal{L},\epsilon,m}(\boldsymbol{w}, D) = 1 \iff \epsilon \ge \frac{1}{m} \| \nabla\mathcal{L}_D(\boldsymbol{w}) \|_2 $$
实际实现中 m 被 λ 替代。
> 作用：将最优邻近验证转化为一个布尔电路的满足性问题，从而可利用任意ZKP后端。

### 实验结果

实验在五个UCI/Kaggle数据集（Adult、Bank、Heart、Chess1、Chess2）上进行，使用逻辑回归和软间隔支持向量机。所有ZKP实验基于EMP-toolkit的布尔电路后端，运行于两台EC2 c7i.4xlarge实例。实验表明：1）拒绝采样攻击极其有效，仅用1000个随机种子即可翻转高达13.5%的高置信度预测；2）ε=0.01的ε-邻近模型在攻击模拟中未造成任何高置信度预测翻转，与理论预测一致；3）强凸性间隙和正则化间隙之和（Δ_sc + Δ_rg）的中位数小于0.01，意味着由理论推导引入的保守间隙很小；4）定点区间算术引入的过估计误差Δ_fp介于6.6×10⁻³与8.2×10⁻³之间，仍在可接受范围；5）端到端性能方面，本文方案在最复杂的Heart数据集上证明了ε_fp=0.0081，布尔电路大小对比基线[GGJ+23]减小了高达246×，算术电路大小减小了约5×，执行时间约快30×。对于软间隔支持向量机，布尔电路减小可达370×。关键优势是证明规模与训练轮次完全无关，因此随着训练轮次增加，加速比将进一步扩大。

### 局限性与开放问题
本文方法要求损失函数为强凸函数，目前主要适用于逻辑回归和软间隔支持向量机等模型，无法直接推广到深度神经网络等非凸训练场景。定点区间算术和分段线性sigmoid逼近会引入额外的过估计误差，虽然实验证明很小，但理论上可以通过增加子区间数进一步逼近，但这会增加证明中的分支判断开销。未来工作可探索如何将最优邻近概念扩展到更广泛的模型类别，以及如何与更高效的ZKP后端（如子线性证明协议）集成以降低通信开销。

### 强关联论文

[APKP24] Kasra Abbaszadeh, Christodoulos Pappas, Jonathan Katz, and Dimitrios Papadopoulos. Zero-knowledge proofs of training for deep neural networks. **ACM CCS 2024** [Google Scholar](https://scholar.google.com/scholar?q=Zero-knowledge%20proofs%20of%20training%20for%20deep%20neural%20networks)

[GGJ+23] Sanjam Garg, Aarushi Goel, Somesh Jha, Saeed Mahloujifar, Mohammad Mahmoody, Guru-Vamsi Policharla, and Mingyuan Wang. Experimenting with zero-knowledge proofs of training. **ACM CCS 2023** [Google Scholar](https://scholar.google.com/scholar?q=Experimenting%20with%20zero-knowledge%20proofs%20of%20training)

[STC+24] Ali Shahin Shamsabadi, Gefei Tan, Tudor Ioan Cebere, Aurélien Bellet, Hamed Haddadi, Nicolas Papernot, Xiao Wang, and Adrian Weller. Confidential-dpproof: Confidential proof of differentially private training. **ICLR 2024** [Google Scholar](https://scholar.google.com/scholar?q=Confidential-dpproof%3A%20Confidential%20proof%20of%20differentially%20private%20training)

[MR18] Payman Mohassel and Peter Rindal. ABY3: A mixed protocol framework for machine learning. **ACM CCS 2018** [Google Scholar](https://scholar.google.com/scholar?q=ABY3%3A%20A%20mixed%20protocol%20framework%20for%20machine%20learning)

[MZ17] Payman Mohassel and Yupeng Zhang. SecureML: A system for scalable privacy-preserving machine learning. **IEEE S&P 2017** [Google Scholar](https://scholar.google.com/scholar?q=SecureML%3A%20A%20system%20for%20scalable%20privacy-preserving%20machine%20learning)


## 关键词

+ 零知识证明训练
+ 最优邻域
+ 凸优化
+ 模型偏差控制
+ 电路复杂度优化