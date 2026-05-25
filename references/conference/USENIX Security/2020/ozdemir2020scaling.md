---
title: "Scaling verifiable computation using efficient set accumulators"
标题简称:
论文类型: conference
会议简称: USENIX Security
发表年份: 2020
modified: 2025-04-13 14:30:07
---

## Scaling verifiable computation using efficient set accumulators

## 发表信息

+ [原文链接](https://www.usenix.org/conference/usenixsecurity20/presentation/ozdemir)

## 作者

+ [Alex Ozdemir](Alex%20Ozdemir.md)
+ [Riad Wahby](Riad%20Wahby.md)
+ Barry Whitehat 
+ [Dan Boneh](Dan%20Boneh.md) 

## 笔记

Verifiable outsourcing systems offload a large computation to a remote server, but require that the remote server provide a succinct proof, called a SNARK, that proves that the server carried out the computation correctly. Real-world applications of this approach can be found in several blockchain systems that employ verifiable outsourcing to process a large number of transactions off-chain. This reduces the on-chain work to simply verifying a succinct proof that transaction processing was done correctly. In practice, verifiable outsourcing of state updates is done by updating the leaves of a Merkle tree, recomputing the resulting Merkle root, and proving using a SNARK that the state update was done correctly.

In this work, we use a combination of existing and novel techniques to implement an RSA accumulator inside of a SNARK, and use it as a replacement for a Merkle tree. We specifically optimize the accumulator for compatibility with SNARKs. Our experiments show that the resulting system can dramatically reduce costs compared to existing approaches that use Merkle trees for committing to the current state. These results apply broadly to any system that needs to offload batches of state updates to a remote untrusted server.

以下是中文翻译：

可验证外包系统将大规模计算任务卸载到远程服务器，但要求远程服务器提供一个简洁证明，称为 SNARK（Succinct Non-Interactive Argument of Knowledge，简洁非交互式知识论证），以证明服务器正确执行了计算。这种方法的实际应用可以在多个区块链系统中找到，这些系统采用可验证外包来处理大量链下交易。这将链上工作简化为仅验证一个简洁证明，该证明表明交易处理已正确完成。在实践中，状态更新的可验证外包是通过更新 Merkle 树（Merkle tree）的叶节点、重新计算生成的 Merkle 根，并使用 SNARK 证明状态更新已正确完成来实现的。

在这项工作中，我们结合现有技术和新颖技术，在 SNARK 内部实现了 RSA 累加器（RSA accumulator），并将其用作 Merkle 树的替代方案。我们专门针对与 SNARK 的兼容性对累加器进行了优化。我们的实验表明，与使用 Merkle 树提交当前状态的现有方法相比，所得到的系统可以显著降低成本。这些结果广泛适用于任何需要将批量状态更新卸载到远程不可信服务器的系统。

## 关键词

+ RSA累加器SNARK优化
+ 可验证外包计算
+ 状态更新批处理
+ Merkle树替代方案
+ 区块链链下计算
+ 集合成员性证明