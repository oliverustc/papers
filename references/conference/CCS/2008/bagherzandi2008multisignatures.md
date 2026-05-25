---
title: "Multisignatures secure under the discrete logarithm assumption and a generalized forking lemma"
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

Multisignatures allow n signers to produce a short joint signature on a single message. Multisignatures were achieved in the plain model with a non-interactive protocol in groups with bilinear maps, by Boneh et al, and by a three-round protocol under the Discrete Logarithm (DL) assumption, by Bellare and Neven, with multisignature verification cost of, respectively, O(n) pairings or exponentiations. In addition, multisignatures with O(1) verification were shown in so-called Key Verification (KV) model, where each public key is accompanied by a short proof of well-formedness, again either with a non-interactive protocol using bilinear maps, by Ristenpart and Yilek, or with a three-round protocol under the Diffie-Hellman assumption, by Bagherzandi and Jarecki.

We improve on these results in two ways: First, we show a two-round O(n)-verification multisignature secure under the DL assumption in the plain model, improving on the three-round protocol of Bellare-Neven. Second, we show a two-round O(1)-verification multisignature secure under the DL assumption in the KV model, improving on assumptions and/or communication rounds of the schemes of Ristenpart and Yilek and Bagherzandi and Jarecki. Exact security of both schemes matches (in ROM) that of Schnorr signatures. The reduced round complexity is due to a new multiplicatively homomorphic equivocable commitment scheme which can be of independent interest. Moreover, our KV model scheme is enabled by a generalized forking lemma, which shows that standard non-interactive zero-knowledge (NIZK) proofs of knowledge in ROM admit efficient simultaneous post-execution extraction of witnesses of all proof instances. As a consequence of this lemma, any DL-based multisignature secure in so-called Knowledge-of-Secret-Key model can be implemented in the KV model using standard ROM-based NIZK's of DL as proofs of key well-formedness.

以下是中文翻译：

多重签名允许 \( n \) 个签名者对单个消息生成一个简短的联合签名。Boneh 等人在具有双线性映射的群体中，通过非交互式协议实现了平面模型下的多重签名，而 Bellare 和 Neven 则在离散对数（DL）假设下通过三轮协议实现了多重签名，分别具有 \( O(n) \) 对应的配对或指数运算的验证成本。此外，在所谓的密钥验证（KV）模型中，展示了具有 \( O(1) \) 验证的多重签名，其中每个公钥都附带一个简短的良构性证明，这同样是通过 Ristenpart 和 Yilek 使用双线性映射的非交互式协议，或者通过 Bagherzandi 和 Jarecki 在迪菲-赫尔曼假设下的三轮协议实现的。

我们在这两方面对这些结果进行了改进：首先，我们展示了在平面模型下，基于 DL 假设的两轮 \( O(n) \) 验证多重签名，从而改进了 Bellare-Neven 的三轮协议。其次，我们展示了在 KV 模型下，基于 DL 假设的两轮 \( O(1) \) 验证多重签名，改进了 Ristenpart 和 Yilek 以及 Bagherzandi 和 Jarecki 的方案中的假设和/或通信轮数。这两个方案的确切安全性在随机预言机（ROM）模型中与 Schnorr 签名相匹配。减少的轮次复杂性得益于一种新的可乘同态可撤回承诺方案，这本身也可能具有独立的研究价值。此外，我们的 KV 模型方案得益于一个广义的分叉引理，该引理表明，ROM 中的标准非交互式零知识（NIZK）知识证明允许对所有证明实例的见证进行高效的同时后执行提取。根据该引理，任何基于 DL 的多重签名在所谓的秘密密钥知识模型中是安全的，可以使用基于 DL 的标准 ROM NIZK 作为密钥良构性的证明在 KV 模型中实现。

## 关键词

+ 多重签名
+ 离散对数假设
+ 两轮协议
+ 可乘同态承诺
+ 分叉引理