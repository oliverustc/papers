---
title: "Sweep-uc: Swapping coins privately"
标题简称:
论文类型: conference
会议简称: S&P
发表年份: 2024
created: 2025-05-09 14:39:35
modified: 2025-05-09 14:41:26
---

## Sweep-uc: Swapping coins privately

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/10646880)
+ [archive](https://eprint.iacr.org/2022/1605)

## 作者

+ [Lucjan Hanzlik](Lucjan%20Hanzlik.md)
+ Julian Loss Sri
+ AravindaKrishnan Thyagarajan
+ Benedikt Wagner

## 笔记

Fair exchange (also referred to as atomic swap) is a fundamental operation in any cryptocurrency that allows users to atomically exchange coins. While a large body of work has been devoted to this problem, most solutions lack on-chain privacy. Thus, coins retain a public transaction history which is known to degrade the fungibility of a currency. This has led to a flourishing line of related research on fair exchange with privacy guarantees. Existing protocols either rely on heavy scripting (which also degrades fungibility and leads to high transaction fees), do not support atomic swaps across a wide range of currencies, or come with incomplete security proofs.To overcome these limitations, we introduce Sweep-UC 1, the first fair exchange protocol that simultaneously is efficient, minimizes scripting, and is compatible with a wide range of currencies (more than the state of the art). We build SweepUC from modular sub-protocols and give a rigorous security analysis in the UC framework. Many of our tools and security definitions can be used in standalone fashion and may serve as useful components for future constructions of fair exchange.

以下是中文翻译：

公平交换（Fair exchange，也称为原子交换）是任何加密货币中允许用户进行原子化代币交换的基本操作。尽管已有大量研究致力于解决这个问题，但大多数解决方案都缺乏链上隐私保护。因此，代币保留了公开的交易历史，这众所周知会降低货币的可替代性。这导致了一系列关于具有隐私保障的公平交换研究的蓬勃发展。现有的协议要么依赖于复杂的脚本编程（这也会降低可替代性并导致高额交易费用），要么不支持跨多种货币的原子交换，要么安全性证明不完整。

为了克服这些限制，我们提出了Sweep-UC 1，这是第一个同时具备高效性、最小化脚本使用，并且与广泛货币类型兼容（超过现有技术水平）的公平交换协议。我们通过模块化子协议构建SweepUC，并在UC框架（Universal Composability framework）下进行严格的安全性分析。我们的许多工具和安全性定义都可以独立使用，可能会成为未来构建公平交换系统的有用组件。

## 关键词

+ 公平交换原子交换
+ 隐私保护跨链交换
+ UC安全框架
+ 链上隐私
+ 可替代性加密货币
+ 模块化子协议设计