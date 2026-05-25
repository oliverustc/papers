---
title: 可验证查询-paper列表
modified: 2025-05-09 14:54:43
created: 2025-04-11 10:52:58
draft: true
---

就可验证范围查询而言，有多种技术路线：

其中包括：

## 累加器


[Matteo Campanelli](Matteo%20Campanelli.md), Dario Fiore, Semin Han, Jihye Kim, Dimitris Kolonelos, Hyunok Oh **Succinct zero-knowledge batch proofs for set accumulators** (**CCS 2022**) [web](https://dl.acm.org/doi/abs/10.1145/3548606.3560677) [scholar](https://scholar.google.com.hk/scholar?hl=zh-CN&as_sdt=0%2C5&q=Succinct%20zero-knowledge%20batch%20proofs%20for%20set%20accumulators&btnG=) [obsidian](campanelli2022succinct)


[Matteo Campanelli](Matteo%20Campanelli.md), Mathias Hall-Andersen, Simon Holmgaard Kamp **Curve trees: Practical and transparent Zero-Knowledge accumulators** (**USENIX Security 2023**) [web](https://www.usenix.org/conference/usenixsecurity23/presentation/campanelli) [scholar](https://scholar.google.com.hk/scholar?hl=zh-CN&as_sdt=0%2C5&q=Curve%20trees%3A%20Practical%20and%20transparent%20Zero-Knowledge%20accumulators&btnG=) [obsidian](campanelli2023curve)

[Jiajun Xin](Jiajun%20Xin.md), Arman Haghighi, Xiangan Tian, [Dimitrios Papadopoulos](Dimitrios%20Papadopoulos.md) **Notus: Dynamic Proofs of Liabilities from Zero-knowledge RSA Accumulators** (**USENIX Security 2024**) [web](https://www.usenix.org/conference/usenixsecurity24/presentation/xin) [scholar](https://scholar.google.com.hk/scholar?hl=zh-CN&as_sdt=0%2C5&q=Notus%3A%20Dynamic%20Proofs%20of%20Liabilities%20from%20Zero-knowledge%20RSA%20Accumulators&btnG=) [obsidian](xin2024notus)

[Zeyu Liu](Zeyu%20Liu.md), [Eran Tromer](Eran%20Tromer.md) **Oblivious message retrieval** (**CRYPTO 2022**) [web](https://link.springer.com/chapter/10.1007/978-3-031-15802-5_26) [scholar](https://scholar.google.com.hk/scholar?hl=zh-CN&as_sdt=0%2C5&q=Oblivious%20message%20retrieval&btnG=) [obsidian](liu2022oblivious)


累加器在零知识联邦学习中的应用：

Haodi Wang, Tangyu Jiang, Yu Guo, Fangda Guo, Rongfang Bie, Xiaohua Jia **Label Noise Correction for Federated Learning: A Secure, Efficient and Reliable Realization** (**ICDE 2024**) [web](https://ieeexplore.ieee.org/abstract/document/10597841) [scholar](https://scholar.google.com.hk/scholar?hl=zh-CN&as_sdt=0%2C5&q=Label%20Noise%20Correction%20for%20Federated%20Learning%3A%20A%20Secure%2C%20Efficient%20and%20Reliable%20Realization&btnG=) [obsidian](wang2024label)


累加器在 DID 中的应用：

Tianxiu Xie, Keke Gai, Jing Yu, Liehuang Zhu, Bin Xiao **SLVC-DIDA: Signature-less Verifiable Credential-based Issuer-hiding and Multi-party Authentication for Decentralized Identity** (**arxiv 2025**) [web](https://arxiv.org/abs/2501.11052) [scholar](https://scholar.google.com.hk/scholar?hl=zh-CN&as_sdt=0%2C5&q=SLVC-DIDA%3A%20Signature-less%20Verifiable%20Credential-based%20Issuer-hiding%20and%20Multi-party%20Authentication%20for%20Decentralized%20Identity&btnG=) [obsidian](xie2025slvc)


## 向量承诺


Sergey Gorbunov, Leonid Reyzin, Hoeteck Wee, [Zhenfei Zhang](Zhenfei%20Zhang.md) **Pointproofs: Aggregating Proofs for Multiple Vector Commitments** (**CCS 2020**) [web](https://dl.acm.org/doi/abs/10.1145/3372297.3417244) [scholar](https://scholar.google.com.hk/scholar?hl=zh-CN&as_sdt=0%2C5&q=Pointproofs%3A%20Aggregating%20Proofs%20for%20Multiple%20Vector%20Commitments&btnG=) [obsidian](gorbunov2020pointproofs)


Rui Gao, Zhiguo Wan, [Yuncong Hu](Yuncong%20Hu.md), Huaqun Wang **A Succinct Range Proof for Polynomial-based Vector Commitment** (**CCS 2024**) [web](https://dl.acm.org/doi/abs/10.1145/3658644.3670324) [scholar](https://scholar.google.com.hk/scholar?hl=zh-CN&as_sdt=0%2C5&q=A%20Succinct%20Range%20Proof%20for%20Polynomial-based%20Vector%20Commitment&btnG=) [obsidian](gao2024succinct)


[Vector commitments with proofs of smallness: Short range proofs and more (**PKC 2024**)](libert2024vector)

Benoit Libert **Vector commitments with proofs of smallness: Short range proofs and more** (**PKC 2024**) [web](https://link.springer.com/chapter/10.1007/978-3-031-57722-2_2) [scholar](https://scholar.google.com.hk/scholar?hl=zh-CN&as_sdt=0%2C5&q=Vector%20commitments%20with%20proofs%20of%20smallness%3A%20Short%20range%20proofs%20and%20more&btnG=) [obsidian](libert2024vector)


[Geoffroy Couteau](Geoffroy%20Couteau.md), Michael Klooß, Huang Lin, Michael Reichle **Efficient range proofs with transparent setup from bounded integer commitments** (**EUROCRYPT 2021**) [web](https://link.springer.com/chapter/10.1007/978-3-030-77883-5_9) [scholar](https://scholar.google.com.hk/scholar?hl=zh-CN&as_sdt=0%2C5&q=Efficient%20range%20proofs%20with%20transparent%20setup%20from%20bounded%20integer%20commitments&btnG=) [obsidian](couteau2021efficient)

Srinivasan, Shravan, Chepurnoy, Alexander, [Charalampos Papamanthou](Charalampos%20Papamanthou.md), Tomescu, Alin, [Yupeng Zhang](Yupeng%20Zhang.md) **Hyperproofs: Aggregating and Maintaining Proofs in Vector Commitments** (**USENIX Security 2022**) [web](https://www.usenix.org/conference/usenixsecurity22/presentation/srinivasan) [scholar](https://scholar.google.com.hk/scholar?hl=zh-CN&as_sdt=0%2C5&q=Hyperproofs%3A%20Aggregating%20and%20Maintaining%20Proofs%20in%20Vector%20Commitments&btnG=) [obsidian](srinivasan2022hyperproofs)

Weijie Wang, Annie Ulichney, [Charalampos Papamanthou](Charalampos%20Papamanthou.md) **BalanceProofs: Maintainable vector commitments with fast aggregation** (**USENIX Security 2023**) [web](https://www.usenix.org/conference/usenixsecurity23/presentation/wang-weijie) [scholar](https://scholar.google.com.hk/scholar?hl=zh-CN&as_sdt=0%2C5&q=BalanceProofs%3A%20Maintainable%20vector%20commitments%20with%20fast%20aggregation&btnG=) [obsidian](wang2023balanceproofs)

Zhongtang Luo, Yanxue Jia, Alejandra Victoria Ospina Gracia, Aniket Kate **Cauchyproofs: Batch-Updatable Vector Commitment with Easy Aggregation and Application to Stateless Blockchains** (**S&P 2025**) [scholar](https://scholar.google.com.hk/scholar?hl=zh-CN&as_sdt=0%2C5&q=Cauchyproofs%3A%20Batch-Updatable%20Vector%20Commitment%20with%20Easy%20Aggregation%20and%20Application%20to%20Stateless%20Blockchains&btnG=) [obsidian](luo2025cauchyproofs)


[Christodoulos Pappas](Christodoulos%20Pappas.md), [Dimitrios Papadopoulos](20-杂/blog-archive/survey/researchers/Dimitrios%20Papadopoulos.md), [Charalampos Papamanthou](20-杂/blog-archive/survey/researchers/Charalampos%20Papamanthou.md) **HydraProofs: Optimally Computing All Proofs in a Vector Commitment with applications to efficient zkSNARKs over data from multiple users** (**S&P 2025**) [web](https://www.computer.org/csdl/proceedings-article/sp/2025/223600d180/26hiVmh7o9q) [scholar](https://scholar.google.com.hk/scholar?hl=zh-CN&as_sdt=0%2C5&q=HydraProofs%3A%20Optimally%20Computing%20All%20Proofs%20in%20a%20Vector%20Commitment%20with%20applications%20to%20efficient%20zkSNARKs%20over%20data%20from%20multiple%20users&btnG=) [obsidian](pappas2025hydraproofs)



## 零知识证明

[Benedikt Bünz](Benedikt%20Bünz.md), [Jonathan Bootle](Jonathan%20Bootle.md), [Dan Boneh](Dan%20Boneh.md), Andrew Poelstra, Pieter Wuille, Greg Maxwell **Bulletproofs: Short proofs for confidential transactions and more** (**S&P 2018**) [web](https://ieeexplore.ieee.org/abstract/document/8418611) [scholar](https://scholar.google.com.hk/scholar?hl=zh-CN&as_sdt=0%2C5&q=Bulletproofs%3A%20Short%20proofs%20for%20confidential%20transactions%20and%20more&btnG=) [obsidian](bunz2018bulletproofs)

[Geoffroy Couteau](Geoffroy%20Couteau.md), Dahmun Goudarzi, Michael Klooß, Michael Reichle **Sharp: Short relaxed range proofs** (**CCS 2022**) [web](https://dl.acm.org/doi/abs/10.1145/3548606.3560628) [scholar](https://scholar.google.com.hk/scholar?hl=zh-CN&as_sdt=0%2C5&q=Sharp%3A%20Short%20relaxed%20range%20proofs&btnG=) [obsidian](couteau2022sharp)

Guofeng Tang, Shuai Han, Li Lin, Changzheng Wei, Ying Yan **Batch Range Proof: How to Make Threshold ECDSA More Efficient** (**CCS 2024**) [web](https://dl.acm.org/doi/abs/10.1145/3658644.3670287) [scholar](https://scholar.google.com.hk/scholar?hl=zh-CN&as_sdt=0%2C5&q=Batch%20Range%20Proof%3A%20How%20to%20Make%20Threshold%20ECDSA%20More%20Efficient&btnG=) [obsidian](tang2024batch)

Liam Eagen, Sanket Kanjalkar, Tim Ruffing, Jonas Nick **Bulletproofs++: Next generation confidential transactions via reciprocal set membership arguments** (**EUROCRYPT 2024**) [web](https://link.springer.com/chapter/10.1007/978-3-031-58740-5_9?fromPaywallRec=false) [scholar](https://scholar.google.com.hk/scholar?hl=zh-CN&as_sdt=0%2C5&q=Bulletproofs%2B%2B%3A%20Next%20generation%20confidential%20transactions%20via%20reciprocal%20set%20membership%20arguments&btnG=) [obsidian](eagen2024bulletproofs++)

Weihan Li, Zongyang Zhang, [Yanpei Guo](Yanpei%20Guo.md), Sherman SM Chow, Zhiguo Wan **Succinct Hash-Based Arbitrary-Range Proofs** (**TIFS 2024**) [web](https://ieeexplore.ieee.org/abstract/document/10752637) [scholar](https://scholar.google.com.hk/scholar?hl=zh-CN&as_sdt=0%2C5&q=Succinct%20Hash-Based%20Arbitrary-Range%20Proofs&btnG=) [obsidian](li2024succinct)


[SoK: Zero-knowledge range proofs (**archive 2024**)](christ2024sok)

[Zero-knowledge elementary databases with more expressive queries (**PKC 2019**)](libert2019zero)

[SwiftRange: a short and efficient zero-knowledge range argument for confidential transactions and more (**S&P 2024**)](wang2024swiftrange)

浮点数空间查询？：

[Zero-Knowledge Location Privacy via Accurate Floating-Point SNARKs (**S&P 2025**)](ernstberger2025zero)
