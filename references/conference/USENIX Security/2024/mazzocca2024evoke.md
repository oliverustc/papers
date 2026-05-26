---
title: "EVOKE: Efficient Revocation of Verifiable Credentials in IoT Networks"
标题简称:
论文类型: conference
会议简称: USENIX Security
发表年份: 2024
---

## EVOKE: Efficient Revocation of Verifiable Credentials in IoT Networks

## 发表信息

+ [原文链接](https://www.usenix.org/conference/usenixsecurity24/presentation/mazzocca)

## 作者

+ Carlo Mazzocca 
+ Abbas Acar 
+ Selcuk Uluagac 
+ Rebecca Montanari 


## 笔记

### 背景与动机

IoT网络中设备间缺乏信任是阻碍数据协作的关键因素 [35]。传统方法依赖PKI和集中式CA，存在可扩展性差、单点故障、互操作性有限等问题。为促进去中心化，W3C提出了去中心化标识符（DID）和可验证凭证（VC）[54,55]，欧盟eIDAS法规亦将其视为关键技术 [38]。然而，VC的撤销机制在IoT场景下仍缺乏高效方案：IoT设备通常具有有限的计算、存储和网络能力，而现有撤销机制如OCSP [42]要求可靠连接且每请求约4 KB [31]，CRL [10]需要存储整个列表（百万证书达数MB），均不适合受限环境。W3C的Revocation List 2020草案 [53]虽然用比特串表示撤销，但百万VC仍需约125 KB。因此，需要一种存储开销恒定、支持批量撤销和离线更新的VC撤销方案。EVOKE正是针对此空白而设计。

### 相关工作

[27] Koisser等. V’CER: Efficient Certificate Validation in Constrained Networks. **USENIX Security 2022** [Google Scholar](https://scholar.google.com/scholar?q=V%27CER%3A+Efficient+Certificate+Validation+in+Constrained+Networks)
> 核心思路：使用稀疏Merkle树（SMT）验证PKI证书，存储开销约3KB/百万证书，支持离线更新。
> 局限与区别：EVOKE使用ECC累计器，存储仅1.5KB，且支持批量撤销（SMT证明大小O(log n)），而EVOKE的累计值大小恒定。

[53] W3C. Revocation List 2020. **W3C Recommendation** [Google Scholar](https://scholar.google.com/scholar?q=Revocation+List+2020)
> 核心思路：每个VC对应比特串中的一位，置1表示撤销。
> 局限与区别：比特串大小随VC数量线性增长（百万VC约125KB），不支持离线撤销和批量撤销时的恒定存储。

[45] Smith等. CRLite: A Scalable System for Pushing All TLS Revocations to All Browsers. **IEEE S&P 2017** [Google Scholar](https://scholar.google.com/scholar?q=CRLite%3A+A+Scalable+System+for+Pushing+All+TLS+Revocations+to+All+Browsers)
> 核心思路：用级联过滤器压缩CRL，减小存储至百KB级。
> 局限与区别：仍需要数百KB存储，不支持IoT设备间离线更新。

[22] Höglund等. Lightweight certificate revocation for low-power IoT with end-to-end security. **JISA 2023** [Google Scholar](https://scholar.google.com/scholar?q=Lightweight+certificate+revocation+for+low-power+IoT+with+end-to-end+security)
> 核心思路：TinyOCSP，将OCSP响应大小减少约70%。
> 局限与区别：仍依赖在线查询，不适合间歇性连接设备；存储开销未完全消除。

[30] Larisch等. CRLite: A Scalable System for Pushing All TLS Revocations to All Browsers. **IEEE S&P 2017** [Google Scholar](https://scholar.google.com/scholar?q=CRLite%3A+A+Scalable+System+for+Pushing+All+TLS+Revocations+to+All+Browsers)
> （同上，已提及）

[18] Fotiu等. Capabilities-based access control for IoT devices using Verifiable Credentials. **IEEE SPW 2022** [Google Scholar](https://scholar.google.com/scholar?q=Capabilities-based+access+control+for+IoT+devices+using+Verifiable+Credentials)
> 核心思路：基于W3C草案维护撤销列表，每个VC分配位置。
> 局限与区别：存储随VC数量线性增长，不支持批量撤销的恒定开销。

[6] Camenisch等. An Accumulator Based on Bilinear Maps and Efficient Revocation for Anonymous Credentials. **PKC 2009** [Google Scholar](https://scholar.google.com/scholar?q=An+Accumulator+Based+on+Bilinear+Maps+and+Efficient+Revocation+for+Anonymous+Credentials)
> 核心思路：使用双线性映射累计器实现匿名凭证撤销。
> 局限与区别：主要面向用户隐私场景，未专门针对IoT设备存储和离线更新优化。

[52] Vitto等. Dynamic universal accumulator with batch update over bilinear groups. **CT-RSA 2022** [Google Scholar](https://scholar.google.com/scholar?q=Dynamic+universal+accumulator+with+batch+update+over+bilinear+groups)
> 核心思路：提出支持批量更新的ECC累计器。
> 局限与区别：EVOKE直接采用该累计器作为底层原语，并针对IoT撤销场景设计协议。

### 核心技术与方案

EVOKE的整体框架包含三类实体：发行者 \( i_j \)、分布式账本（DAG）\( b \)、IoT设备 \( d_i \)（见图2）。其核心机制是利用正ECC累计器 [52] 将所有有效VC的哈希值聚合为固定长度的累计值 \( a_j \)，每个设备 \( d_i \) 存储对应的包含性证明（见证）\( w_i \)。验证时，设备将对方VC的哈希作为元素，通过 Verify 函数检查其是否在 \( a_j \) 中，从而实现常量时间验证。撤销时，发行者执行 UpdateAccumulator 删除被撤销VC的哈希，并重新计算见证，通过DAG分发。离线更新通过设备间交互实现：当设备 \( d_i \) 与 \( d_k \) 相遇时，比较累计值时间戳，较旧的一方从较新的一方或DAG获取最新累计值和见证（Algorithm 1）。

协议主要函数（见4.1节）：
- Setup(K): 生成椭圆曲线随机生成元。
- ComputeAccumulator(ainfo, V): 将有效VC集合V映射到曲线上计算出 \( a_j \)。
- RemoveFromAccumulator(ainfo, a_j^{t-1}, V): 删除V得到更新后的 \( a_j^t \)。
- ComputeWitness(a_j, vc_i): 为有效VC生成见证 \( w_i \)。
- Verify(a_j, vc_i, w_i, pk_i): 验证 \( vc_i \) 的哈希是否在 \( a_j \) 中，并检查签名。
- UpdateWitness(a_j^t, vc_i): 生成更新后的见证。

安全分析（第5节）基于Dolev-Yao模型，假设累计器抗碰撞。威胁包括发行者密钥泄露、设备被控、通信窃听。EVOKE通过以下方式缓解：发行者环境隔离；即使获取累计器参数也无法伪造签名；设备被控后发行者撤销其VC；通信中通过时间戳防止重放旧累计值；即使攻击者不转发更新，设备仍可通过其他诚实设备更新，且最多一小时内能覆盖96%设备（见6.4节）。

复杂度：存储方面，每个设备仅需1.5 KB（累计值+见证），与VC数量无关。验证计算时间为常数（椭圆曲线运算数次，实测<500ms on commodity devices）。发行者生成见证的计算量随设备数线性增长（图6），但百万见证约需80秒，且可通过并行优化。

### 核心公式与流程

**[累计值生成]**
$$a_j \leftarrow \mathsf{ComputeAccumulator}(\mathsf{a_{info}}, V)$$
> 作用：将有效VC集合V的哈希值累积到椭圆曲线点 \( a_j \) 上，输出固定长度（约32字节）的累计值。

**[见证生成]**
$$w_i \leftarrow \mathsf{ComputeWitness}(a_j, vc_i)$$
> 作用：为单个有效VC生成包含性证明，输出固定长度（约32字节）的椭圆曲线点。

**[验证操作]**
$$\{0,1\} \leftarrow \mathsf{Verify}(a_j, vc_i, w_i, pk_i)$$
> 作用：验证者使用设备公钥 \( pk_i \) 检查签名，并利用椭圆曲线双线性配对验证 \( w_i \) 是否为 \( a_j \) 中元素 \( vc_i \) 的证明。

**[撤销更新]**
$$a_j^t \leftarrow \mathsf{UpdateAccumulator}(\mathsf{a_{info}}, a_j^{t-1}, V)$$
> 作用：从当前累计值中移除被撤销VC的哈希，得到新的累计值。

**[离线更新算法 (Algorithm 1)]**
```python
for each d_i in D_j:
    d_i interacts with d_k (i != k)
    if a_j^i is older than a_j^k:
        a_j^i <- a_j^k
        if d_i has sufficient connectivity:
            w_i <- DirectRetrieval(b, d_i)
        else if d_k has sufficient connectivity:
            w_i <- IndirectRetrieval(b, d_k, d_i)
        else:
            disable trusted communications for d_i
```
> 作用：描述设备在发现累计值版本落后时，如何通过网络直接或间接从DAG获取最新见证，若无连接则暂时禁用信任通信。

### 实验结果

实验在三类场景下进行：1) 商品IoT设备（LG Smart TV、Amazon Echo Show、iPhone 12、Oculus Quest 2）上直接运行JavaScript/WASM代码，验证VC的时间在12.62 ms（iPhone）到499.70 ms（Echo Show）之间，存储需求恒定约1.5 KB。2) 混合网络（5个树莓派4代，WiFi局域网，分别模拟星型和网格拓扑），总延迟（验证+传输）在网格网络中为545.2 ms（EVOKE vs 基线97.4 ms，差异主要来自传输而非操作）；星型网络为1152.7 ms。结果表明EVOKE的操作仅贡献毫秒级开销。3) 大规模仿真（10K到1M设备，模拟一周），设置每日撤销率0.028%（约年10%）。当10%设备错过更新时，一小时内100%设备更新；30%错过时更新率达98%；50%错过时更新率达96%（图5）。网络开销：1M设备50%错过时约721.67 MB（一小时内）。发行者侧最耗时为见证生成（1M设备需80秒，图6）。对比其他方案（表6）：EVOKE存储1.5 KB远低于V’CER的3 KB、CRLite的112.5 KB、Revocation List 2020的125 KB；且同时支持批量撤销和离线撤销。

### 局限性与开放问题

EVOKE假设发行者具有足够计算能力且环境安全，但在实际部署中发行者自身的安全仍是独立问题。此外，当两个离线设备同时持有相同旧累计值时，它们可能无法检测到撤销；尽管论文指出该情况时间受限（一小时内更新），但在极端场景仍存在短暂风险。最后，EVOKE依赖DAG发布更新，DAG的性能（如确认延迟）可能影响更新传播速度，未来可探索更轻量的分布式存储方案。

### 强关联论文

[27] Koisser, D., Jauernig, P., Tsudik, G., Sadeghi, A.-R. V’CER: Efficient Certificate Validation in Constrained Networks. **USENIX Security 2022** [Google Scholar](https://scholar.google.com/scholar?q=V%27CER%3A+Efficient+Certificate+Validation+in+Constrained+Networks)

[52] Vitto, G., Biryukov, A. Dynamic universal accumulator with batch update over bilinear groups. **CT-RSA 2022** [Google Scholar](https://scholar.google.com/scholar?q=Dynamic+universal+accumulator+with+batch+update+over+bilinear+groups)

[53] W3C. Revocation List 2020. **W3C Recommendation** [Google Scholar](https://scholar.google.com/scholar?q=Revocation+List+2020)

[45] Smith, T., Dickinson, L., Seamons, K. Let’s Revoke: Scalable Global Certificate Revocation. **NDSS 2020** [Google Scholar](https://scholar.google.com/scholar?q=Let%27s+Revoke%3A+Scalable+Global+Certificate+Revocation)

[22] Höglund, J., Furuhed, M., Raza, S. Lightweight certificate revocation for low-power IoT with end-to-end security. **JISA 2023** [Google Scholar](https://scholar.google.com/scholar?q=Lightweight+certificate+revocation+for+low-power+IoT+with+end-to-end+security)

[10] Cooper, D., et al. Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile. **RFC 5280** 2008 [Google Scholar](https://scholar.google.com/scholar?q=Internet+X.509+Public+Key+Infrastructure+Certificate+and+CRL+Profile)

[30] Larisch, J., et al. CRLite: A Scalable System for Pushing All TLS Revocations to All Browsers. **IEEE S&P 2017** [Google Scholar](https://scholar.google.com/scholar?q=CRLite%3A+A+Scalable+System+for+Pushing+All+TLS+Revocations+to+All+Browsers)

[18] Fotiu, N., et al. Capabilities-based access control for IoT devices using Verifiable Credentials. **IEEE SPW 2022** [Google Scholar](https://scholar.google.com/scholar?q=Capabilities-based+access+control+for+IoT+devices+using+Verifiable+Credentials)

[6] Camenisch, J., et al. An Accumulator Based on Bilinear Maps and Efficient Revocation for Anonymous Credentials. **PKC 2009** [Google Scholar](https://scholar.google.com/scholar?q=An+Accumulator+Based+on+Bilinear+Maps+and+Efficient+Revocation+for+Anonymous+Credentials)

[42] Santesson, S., et al. X.509 Internet Public Key Infrastructure Online Certificate Status Protocol - OCSP. **RFC 6960** 2013 [Google Scholar](https://scholar.google.com/scholar?q=X.509+Internet+PKI+Online+Certificate+Status+Protocol+OCSP)


## 关键词

+ EVOKE物联网可验证凭证撤销
+ ECC累加器轻量级VC管理
+ 去中心化身份DID可验证凭证
+ 离线批量撤销机制
+ IoT设备低存储认证
+ eIDAS数字身份信任服务
