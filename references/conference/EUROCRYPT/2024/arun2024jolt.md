---
title: "Jolt: SNARKs for Virtual Machines via Lookups"
标题简称: Jolt
论文类型: conference
会议简称: EUROCRYPT
发表年份: 2024
modified: 2025-04-23 15:20:15
created: 2025-04-08 18:55:32
---

## Jolt: SNARKs for Virtual Machines via Lookups

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-58751-1_1)'
+ [code](https://github.com/a16z/jolt)

## 作者

+ [Arasu Arun](Arasu%20Arun.md)
+ [Srinath Setty](Srinath%20Setty.md)
+ [Justin Thaler](Justin%20Thaler.md)

## 笔记

Succinct Non-interactive Arguments of Knowledge (SNARKs) allow an untrusted prover to establish that it correctly ran some “witness-checking procedure” on a witness. A zkVM (short for zero-knowledge virtual machine) is a SNARK that allows the witness-checking procedure to be specified as a computer program written in the assembly language of a specific instruction set architecture (ISA).

A front-end converts computer programs into a lower-level representation such as an arithmetic circuit or generalization thereof. A SNARK for circuit-satisfiability can then be applied to the resulting circuit.

We describe a new front-end technique called Jolt that applies to a variety of ISAs. Jolt arguably realizes a vision called the lookup singularity, which seeks to produce circuits that only perform lookups into pre-determined lookup tables. The circuits output by Jolt primarily perform lookups into a gigantic lookup table, of size more than $2^{128}$, that depends only on the ISA. The validity of the lookups are proved via a new lookup argument described in a companion work called Lasso. Although size-$2^{128}$ tables are vastly too large to materialize in full, the tables arising in Jolt are structured, avoiding costs that grow linearly with the table size.

We describe performance and auditability benefits of Jolt compared to prior zkVMs, focusing on the popular RISC-V ISA as a concrete example. The dominant cost for the Jolt prover applied to this ISA (on 64-bit data types) is equivalent to cryptographically committing to under eleven 256-bit field elements per step of the RISC-V CPU. This compares favorably to prior zkVM provers, even those focused on far simpler VMs.

以下是中文翻译：

简洁非交互式知识证明（SNARKs）允许不可信的证明者证明其正确地运行了某个“见证检验程序”（witness-checking procedure）并对一个见证（witness）进行了验证。零知识虚拟机（zkVM）是一个SNARK，它允许将见证检验程序指定为用特定指令集架构（ISA）的汇编语言编写的计算机程序。

前端（front-end）将计算机程序转换为更低级的表示形式，如算术电路或其推广形式。然后，可以对生成的电路应用电路可满足性（circuit-satisfiability）相关的SNARK。

我们描述了一种新的前端技术，称为Jolt，它适用于多种ISA。Jolt可以说实现了一种称为查找奇点（lookup singularity）的愿景，该愿景旨在生成仅执行对预先确定的查找表（lookup tables）查找的电路。Jolt输出的电路主要执行对一个巨大的查找表的查找，该查找表的大小超过$2^{128}$，且仅依赖于ISA。查找的有效性通过一种新型的查找论证（lookup argument）来证明，该论证在一篇名为Lasso的相关工作中进行了描述。尽管大小为$2^{128}$的表在实际中无法完全实现，但Jolt中产生的表是结构化的，从而避免了与表大小线性增长的成本。

我们描述了Jolt相较于之前的zkVM在性能和可审计性方面的优势，重点以流行的RISC-V ISA作为具体示例。应用于该ISA（在64位数据类型下）的Jolt证明者的主要成本相当于在RISC-V CPU的每个步骤中对不到11个256位域元素进行密码学承诺。这与之前的zkVM证明者相比表现良好，即使是那些专注于更简单虚拟机的证明者。

## 关键词

+ 零知识虚拟机
+ 查找奇点
+ RISC-V指令集
+ Lasso查找论证
+ zkVM前端