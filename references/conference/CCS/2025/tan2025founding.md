---
title: Founding Zero-Knowledge Proofs of Training on Optimum Vicinity
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

Zero-knowledge proofs of training (zkPoT) allow a party to prove that a model is trained correctly on a committed dataset without revealing any additional information about the model or the dataset. Existing zkPoT protocols prove the entire training process in zero knowledge; i.e., they prove that the final model was obtained in an iterative fashion starting from the training data and a random seed (and potentially other parameters) and applying the correct algorithm at each iteration. This approach inherently requires the prover to perform work linear to the number of iterations.

In this paper, we take a different approach to proving the correctness of model training. Our approach is motivated by efficiency but also more urgently by the observation that the prover's ability to pick the random seed used for training introduces the potential for it to bias the model. In other words, if the input to the training algorithm is biased, the resulting model will be biased even if the prover correctly ran the training algorithm. Rather than prove the correctness of the training process, we thus directly prove the correctness of the training model using a notion we call _optimum vicinity_, which bounds the distance between the trained model and the mathematically optimal model for models that can be viewed as the solution to a convex optimization problem. We show both theoretically and experimentally that this ensures the trained model behaves similarly to the optimal model, and show this is not true for existing approaches. We also demonstrate significant performance improvements as compared to the existing zkPoT paradigm: the statement proven in ZK in our protocol has a size independent of the number of training iterations, and our Boolean (respectively arithmetic) circuit size is up to 246× (respectively 5×) smaller than that of a baseline zkPoT protocol that verifies the whole training process.

以下是中文翻译：

训练零知识证明（Zero-knowledge proofs of training, zkPoT）允许一方证明模型在承诺数据集上被正确训练，而不泄露关于模型或数据集的任何额外信息。现有的zkPoT协议以零知识方式证明整个训练过程；即，它们证明最终模型是通过迭代方式获得的，从训练数据和随机种子（以及可能的其他参数）开始，在每次迭代中应用正确的算法。这种方法本质上要求证明者执行与迭代次数成线性关系的工作量。

在本文中，我们采用了一种不同的方法来证明模型训练的正确性。我们的方法不仅出于效率考虑，更紧迫的是基于这样的观察：证明者选择用于训练的随机种子的能力引入了使模型产生偏差的潜在可能性。换句话说，如果训练算法的输入存在偏差，即使证明者正确运行了训练算法，得到的模型也会存在偏差。因此，我们不是证明训练过程的正确性，而是使用我们称为最优邻域（optimum vicinity）的概念直接证明训练模型的正确性，该概念限定了训练模型与数学最优模型之间的距离，适用于可以视为凸优化问题（convex optimization problem）解的模型。我们从理论和实验两方面证明，这确保了训练模型的行为与最优模型相似，并表明现有方法无法做到这一点。我们还展示了与现有zkPoT范式相比的显著性能改进：我们协议中以零知识方式证明的陈述大小与训练迭代次数无关，我们的布尔电路（Boolean circuit）（分别为算术电路arithmetic circuit）大小比验证整个训练过程的基准zkPoT协议小多达246倍（分别为5倍）。

## 关键词

+ 零知识证明训练
+ 最优邻域
+ 凸优化
+ 模型偏差控制
+ 电路复杂度优化