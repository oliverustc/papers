---
title: "Nova: Recursive zero-knowledge arguments from folding schemes"

标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 2022
modified: 2025-04-23 15:25:24
created: 2025-04-13 17:44:41
---

## Nova: Recursive zero-knowledge arguments from folding schemes

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-15985-5_13)
+ [code](https://github.com/microsoft/Nova)

## 作者

+ Abhiram Kothapalli 
+ [Srinath Setty](Srinath%20Setty.md) 
+ Ioanna Tzialla 

## 笔记

这是一篇里程碑意义的paper，很多零知识证明相关的顶会paper都引用了它，目前还没有调研完，有时间继续调研：[scholar](https://scholar.google.com.hk/scholar?start=40&hl=zh-CN&as_sdt=2005&sciodt=0,5&cites=13185717178995702051&scipsc=)

We introduce a new approach to realize incrementally verifiable computation (IVC), in which the prover recursively proves the correct execution of incremental computations of the form $y=F^{(\mathscr{l})}(x)$, where _F_ is a (potentially non-deterministic) computation, _x_ is the input, _y_ is the output, and $\mathscr{l}>0$. Unlike prior approaches to realize IVC, our approach avoids succinct non-interactive arguments of knowledge (SNARKs) entirely and arguments of knowledge in general. Instead, we introduce and employ _folding schemes_, a weaker, simpler, and more efficiently-realizable primitive, which reduces the task of checking two instances in some relation to the task of checking a single instance. We construct a folding scheme for a characterization of NP and show that it implies an IVC scheme with improved efficiency characteristics: (1) the “recursion overhead” (i.e., the number of steps that the prover proves in addition to proving the execution of _F_) is a constant and it is dominated by two group scalar multiplications expressed as a circuit (this is the smallest recursion overhead in the literature), and (2) the prover’s work at each step is dominated by two multiexponentiations of size _O_(|_F_|), providing the fastest prover in the literature. The size of a proof is _O_(|_F_|) group elements, but we show that using a variant of an existing zkSNARK, the prover can prove the knowledge of a valid proof succinctly and in zero-knowledge with O(log⁡|F|) group elements. Finally, our approach neither requires a trusted setup nor FFTs, so it can be instantiated efficiently with any cycles of elliptic curves where DLOG is hard.

以下是中文翻译：

我们提出了一种新的方法来实现增量可验证计算（Incrementally Verifiable Computation，IVC），在该方法中，证明者递归地证明增量计算的正确执行，形式为 $y=F^{(\mathscr{l})}(x)$，其中 $F$ 是一种（可能是非确定性的）计算，$x$ 是输入，$y$ 是输出，且 $\mathscr{l}>0$。与之前实现 IVC 的方法不同，我们的方法完全避免了简洁非交互式知识论证（Succinct Non-interactive Arguments of Knowledge，SNARKs）以及一般的知识论证。相反，我们引入并采用了“折叠方案”（folding schemes），这是一种更弱、更简单且更高效可实现的原语，它将检查两个实例之间某种关系的任务简化为检查单个实例的任务。我们为 NP 的一种特征构造了一个折叠方案，并证明它暗示了一种具有改进效率特征的 IVC 方案：（1）“递归开销”（即，证明者在证明 $F$ 的执行之外所需证明的步骤数）是一个常数，并且由两个以电路形式表达的群标量乘法主导（这是文献中最小的递归开销），以及（2）证明者在每一步的工作量主要由两个大小为 $O(|F|)$ 的多重指数计算主导，从而提供了文献中最快的证明者。证明的大小为 $O(|F|)$ 个群元素，但我们展示了使用现有 zkSNARK 的一种变体，证明者可以以简洁且零知识的方式证明有效证明的知识，所需的群元素数量为 $O(\log |F|)$。最后，我们的方法既不需要可信的设置，也不需要快速傅里叶变换（FFTs），因此可以在任何离散对数问题（DLOG）困难的椭圆曲线周期上高效实现。

## 关键词

+ Nova折叠方案增量可验证计算
+ 常数递归开销最优证明者IVC
+ 无可信设置无FFT椭圆曲线IVC
+ NP折叠方案避免完整SNARK
+ 递归零知识论证折叠原语