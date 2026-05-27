---
title: Foundations of fully dynamic group signatures
doi: 10.1007/s00145-020-09357-w
标题简称: 
论文类型: journal
期刊简称: Journal of Cryptology
发表年份: 2020
created: 2025-05-12 08:59:30
modified: 2025-05-23 01:36:00
---
## Foundations of fully dynamic group signatures

## 发表信息

+ [原文链接](https://link.springer.com/article/10.1007/s00145-020-09357-w)

## 作者

+ [Jonathan Bootle](Jonathan%20Bootle.md)
+ Andrea Cerulli
+ Pyrros Chaidos
+ Essam Ghadafi
+ [Jens Groth](Jens%20Groth.md)

相同的作者和相同的标题在[ACNS 2016](https://link.springer.com/chapter/10.1007/978-3-319-39555-5_7)年发表过一次，2020年估计为最新版

## 笔记

### 背景与动机
群签名允许群组成员匿名代表群组签名，并由群管理员在必要时揭露签名者身份以追究责任。对于实际应用，群签名需支持完全动态的群组，即用户可随时加入和离开。然而，现有针对完全动态群签名的安全定义是非正式的、存在缺陷且相互不兼容 [48,53]。例如，这些定义常基于特定的撤销列表机制，缺乏通用性，并且在撤销发生后允许对先前时段的签名进行“伪造”，这隐含地使历史签名失效。本文旨在填补这一空白，提供一个形式化、严格且通用的安全模型。该模型不预设特定设计范式，能够囊括并比较不同构造的安全性，并针对恶意选择密钥的情况提供保护。此外，本文还指出，基于撤销列表的构造因策略定义导致新成员仅能达到较弱的可追踪性，而模型通过灵活的 IsActive 策略可自然捕获这种差异。

### 相关工作
[14] Bellare 等. Foundations of group signatures: Formal definitions, simplified requirements, and a construction based on general assumptions. **EUROCRYPT 2003** [Google Scholar](https://scholar.google.com/scholar?q=Foundations+of+group+signatures%3A+Formal+definitions%2C+simplified+requirements%2C+and+a+construction+based+on+general+assumptions)
> 核心思路：首次给出了静态群签名的形式化安全定义，包括完整匿名性和全可追踪性。
> 局限与区别：其模型假设群组在建立时固定，不支持用户加入或撤销，因此无法直接用于完全动态场景。

[19] Bellare 等. Foundations of group signatures: The case of dynamic groups. **CT-RSA 2005** [Google Scholar](https://scholar.google.com/scholar?q=Foundations+of+group+signatures%3A+The+case+of+dynamic+groups)
> 核心思路：将群管理员角色分为发行者与开启者，定义了部分动态群组（仅允许加入，不允许离开）的安全模型。
> 局限与区别：模型不支持用户撤销，且假设群管理员状态是分用户隔离的，而本文模型统一处理完全动态并允许并发加入。

[43] Kiayias 等. Secure scalable group signature with dynamic joins and separable authorities. **IJSN 2006** [Google Scholar](https://scholar.google.com/scholar?q=Secure+scalable+group+signature+with+dynamic+joins+and+separable+authorities)
> 核心思路：定义了单权威设置下的部分动态群签名模型，不要求正确开启的证明，信任群管理员。
> 局限与区别：该模型未提供开启证明，使得非陷害性定义依赖管理员的判断，而本文则提供了更强的、具备可验证证明的安全性定义。

[59] Sakai 等. On the security of dynamic group signatures: Preventing signature hijacking. **PKC 2012** [Google Scholar](https://scholar.google.com/scholar?q=On+the+security+of+dynamic+group+signatures%3A+Preventing+signature+hijacking)
> 核心思路：扩展了部分动态群组模型，引入了开启绑定与开启可靠性概念，防止签名被错误归属。
> 局限与区别：该工作聚焦于部分动态场景，而本文将这些概念推广到完全动态设置，并考虑了恶意管理员生成密钥的情况。

[48] Libert 等. Group signatures with almost-for-free revocation. **CRYPTO 2012** [Google Scholar](https://scholar.google.com/scholar?q=Group+signatures+with+almost-for-free+revocation)
> 核心思路：利用子集覆盖框架实现高效撤销的群签名。
> 局限与区别：其安全模型未考虑新成员签署先前时段签名的问题，导致其在该模型下只能达到较弱的可追踪性，本文通过修改策略或方案来弥补这一缺陷。

[53] Nakanishi 等. Revocable group signature schemes with constant costs for signing and verifying. **PKC 2009** [Google Scholar](https://scholar.google.com/scholar?q=Revocable+group+signature+schemes+with+constant+costs+for+signing+and+verifying)
> 核心思路：基于证书撤销列表，实现签名与验证时间与群组及撤销列表大小无关的常数级群签名。
> 局限与区别：其安全定义同样忽视签署时间与加入时间的顺序关系，与本文的强可追踪性定义存在差距。

[7] Bootle 等. Short accountable ring signatures based on DDH. **ESORICS 2015** [Google Scholar](https://scholar.google.com/scholar?q=Short+accountable+ring+signatures+based+on+DDH)
> 核心思路：提出可问责环签名，并给出将其转化为完全动态群签名的通用构造。
> 局限与区别：该工作并未给出完整的群管理细节（如加入协议），且其安全证明未考虑本模型中的恶意密钥生成与分离权威设置。本文补全了这些细节，并在更强模型下证明了安全性。

### 核心技术与方案
本文未提出新的群签名方案，而是建立了一个用于分析完全动态群签名的形式化安全框架。该框架的核心是定义一个名为 FDGS 的方案语法，包含 GSetup、GKGen、Join（用户-管理员交互协议）、UpdateGroup、Sign、Verify、Open、Judge 等算法以及一个 `Reg` 注册表。与现有模型的关键区别在于，本文显式引入了**时段**的概念：群的公共信息被分为永久的群公钥 gpk 和随时段 τ 变化的临时群信息 `info_τ`，用以反映群成员资格的动态变化。加入了 `IsActive` 策略：该策略是一个确定性算法，以用户标识 i、时段 τ 和管理员状态 `st_GM` 为输入，输出该用户是否被认为在该时段内活跃。这个抽象层使得模型能够统一涵盖不同的设计范式——例如累积器（记录活跃成员）和撤销列表（记录已撤销成员），因为两者的差异仅体现在 `IsActive` 的实现上。模型支持单权威设置（GM 同时管理群与开启签名）和双权威设置（GM 管理群，OA 开启签名），并分别给出了安全性定义。在双权威设置中，即使尝试恶意生成对方密钥，模型也提供了保护。

本文定义了四个核心安全性质：
1.  **正确性**：即使存在恶意用户，一个诚实用户在与诚实 GM 交互后仍能成功加入并在未被撤销前正常签名，且签名能被验证通过。
2.  **匿名性**：在诚实 OA（双权威）或诚实 GM（单权威）的前提下，敌手无法区分由两个不同诚实用户签署的签名。该定义涵盖了完整匿名性，即敌手甚至能看到所有用户的签名密钥和加入记录。
3.  **可追踪性**：任何能被验证通过的签名必然能被开启到一个活跃用户。若 GM（或 OA）的密钥泄露或被恶意运行，此性质依然成立。
4.  **非陷害性**：即使 GM、OA 和其他用户全部合谋，也无法将某个签名合理地归属到一个并未实际签署该签名的诚实用户。

此外，本文还单独定义了**开启绑定**和**开启可靠性**。前者保证一个签名无法被归属到两个不同的注册记录（即使所有方合谋）；后者保证一个诚实用户签名的签名不会被错误地归属到另一个用户（即使 OA 和 GM 合谋）。

模型通过限制注册表的操作（用户单次不可修改地写入，管理员可读取）和定义会话标识符，为实现上述性质提供了基础。其安全性证明思路通常是将对 FDGS 的攻击归约到其底层组件（如加密方案、签名方案）的安全性上。本文证明了，一个满足 DDH 假设下的可问责环签名方案 [7] 可以构造出一个满足本模型所有性质的完全动态群签名方案，并给出了正式的归约证明。对于基于撤销列表的方案 [48,49,53]，本文指出它们默认的 IsActive 策略允许用户签署加入前的签名，从而不能满足模型预设的强可追踪性，但可以通过修改策略（例如将未加入用户视为已撤销）或修改方案（将加入时段嵌入证书）来达到本模型的安全要求。这些分析验证了模型的设计无关性和表达力。

### 核心公式与流程

**[抽象注册表模型]**
```math
\text{Reg}: \text{数据结构，} \text{reg}_i \text{ 为第 } i \text{ 个会话的注册记录} \\
\text{ReadReg}(i): \text{返回 } \text{reg}_i \text{ 或 } \bot \\
\text{WriteReg}(i, M): \text{执行 } \text{reg}_i := M \text{，仅可调用一次。}
```
> 作用：抽象了群成员注册信息的存储与访问方式，通过限制单次写入确保用户对自身记录的控制权，是实现非陷害性的基础。

**[可追踪性安全游戏核心判定]**
```math
\text{Exp}_{\text{FDGS},\mathcal{A}}^{\text{Trace}}(\lambda) = 1 \iff \text{Verify}(\text{gpk}, \text{info}_\tau, m, \Sigma) = 1 \land \\
( \text{IsActive}(i, \tau, \text{st}_{\text{GM}}) = 0 \lor \text{Judge}(\text{gpk}, \text{info}_\tau, \text{reg}_i, m, \Sigma, \pi) = 0 )
```
> 作用：形式化定义了可追踪性的获胜条件，即敌手成功输出一个有效签名，但该签名要么开启到一个不活跃用户（逃避追踪），要么开启证明无效（错误归属）。

**[匿名性安全游戏的关键挑战]**
```math
\text{Chal}_b(\text{info}, m, i_0, i_1): \\
\text{若 } \{i_0, i_1\} \not\subseteq \mathcal{H} \text{，返回 } \bot \\
\Sigma_0 \leftarrow \text{Sign}(\text{gsk}_{i_0}, \text{info}, m) \\
\Sigma_1 \leftarrow \text{Sign}(\text{gsk}_{i_1}, \text{info}, m) \\
\text{返回 } \Sigma_b
```
> 作用：定义了匿名性的挑战过程。敌手选择两个诚实用户，方案随机选择其中一个签署消息，敌手无法区分签名来自哪个用户。

**[双权威匿名性游戏]**
```math
\text{Exp}_{\text{FDGS},\mathcal{A}}^{\text{Anon}-b}(\lambda): \\
\text{param} \leftarrow \text{GSetup}(1^\lambda) \\
((\text{mpk}; \text{st}_{\mathcal{A}}); (\text{opk}, \text{osk})) \leftarrow \langle \mathcal{A}(\text{param}); \text{GKGen}_{\text{OA}}(\text{param}) \rangle \\
\text{gpk} := (\text{param}, \text{mpk}, \text{opk}) \\
\text{返回 } b^* \leftarrow \mathcal{A}^{\text{SndToU}, \text{Open}, \text{Chal}_b, \text{ReadReg}}(\text{gpk}; \text{st}_{\mathcal{A}})
```
> 作用：展示了在双权威设置下，即使敌手可能恶意生成GM的密钥（`A`扮演GM），只要OA诚实，匿名性依然成立。敌手通过SndToU与诚实用户交互。

### 实验结果
本文是一项理论工作，主要提供安全模型和定义，并未提出具体的方案，因此没有包含任何实验或性能评估。文章的贡献在于形式化建模、安全性定义以及理论证明（如可追踪性定义对现有方案的适用性分析）。作者通过将现有静态和部分动态群签名模型 [14,19,43] 作为其模型的特例，并展示如何使用该模型分析 [7,48,49,53] 等具体方案，作为对其模型有效性的验证。具体来说，作者详细论证了Bootle等人的方案 [7] 满足其所有安全定义，而基于撤销列表的方案 [48,49,53] 仅在调整了 `IsActive` 策略或对方案本身进行简单修改后才能满足其预定义的强可追踪性要求，从而揭示了不同方案在安全模型中的细微差别。

### 局限性与开放问题
本文的模型虽然在通用性和严格性上迈出了重要一步，但并未指定 `IsActive` 算法的具体输入输出规则，只是给出了其应满足的必要条件。这意味着完全形式化一个方案的安全性仍需手动定义其 `IsActive` 策略，这可能成为完全形式化自动验证的一个障碍。此外，模型未明确处理诸如**背向不可链接性**等撤销场景下的常见性质，即已撤销用户的先前签名是否仍保持匿名。将定义扩展到处理这类性质以及背向匿名性，是模型的一个潜在扩展方向。最后，模型专注于标准的安全性概念，对于更高级的匿名性概念（如成员隐私 [12]）或应用（如匿名声誉系统 [32]）是开放性的，后续工作已在此方面进行了拓展。

### 强关联论文
[7] Bootle 等. Short accountable ring signatures based on DDH. **ESORICS 2015** [Google Scholar](https://scholar.google.com/scholar?q=Short+accountable+ring+signatures+based+on+DDH)

[14] Bellare 等. Foundations of group signatures: Formal definitions, simplified requirements, and a construction based on general assumptions. **EUROCRYPT 2003** [Google Scholar](https://scholar.google.com/scholar?q=Foundations+of+group+signatures%3A+Formal+definitions%2C+simplified+requirements%2C+and+a+construction+based+on+general+assumptions)

[19] Bellare 等. Foundations of group signatures: The case of dynamic groups. **CT-RSA 2005** [Google Scholar](https://scholar.google.com/scholar?q=Foundations+of+group+signatures%3A+The+case+of+dynamic+groups)

[43] Kiayias 等. Secure scalable group signature with dynamic joins and separable authorities. **IJSN 2006** [Google Scholar](https://scholar.google.com/scholar?q=Secure+scalable+group+signature+with+dynamic+joins+and+separable+authorities)

[48] Libert 等. Group signatures with almost-for-free revocation. **CRYPTO 2012** [Google Scholar](https://scholar.google.com/scholar?q=Group+signatures+with+almost-for-free+revocation)

[49] Libert 等. Scalable group signatures with revocation. **EUROCRYPT 2012** [Google Scholar](https://scholar.google.com/scholar?q=Scalable+group+signatures+with+revocation)

[53] Nakanishi 等. Revocable group signature schemes with constant costs for signing and verifying. **PKC 2009** [Google Scholar](https://scholar.google.com/scholar?q=Revocable+group+signature+schemes+with+constant+costs+for+signing+and+verifying)

[59] Sakai 等. On the security of dynamic group signatures: Preventing signature hijacking. **PKC 2012** [Google Scholar](https://scholar.google.com/scholar?q=On+the+security+of+dynamic+group+signatures%3A+Preventing+signature+hijacking)


## 关键词

+ 完全动态群签名安全模型
+ 群签名形式化安全定义
+ 动态成员管理与撤销
+ 匿名性与可追踪性平衡
+ 恶意密钥选择保护
+ 撤销列表可追踪性弱化