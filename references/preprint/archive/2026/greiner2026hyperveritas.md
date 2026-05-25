---
title: "HyperVerITAS: Verifying Image Transformations at Scale on Boolean Hypercubes"
标题简称:
论文类型: preprint
预印本简称: archive
发表年份: 2026
---

## HyperVerITAS: Verifying Image Transformations at Scale on Boolean Hypercubes

## 发表信息

+ [原文链接](https://eprint.iacr.org/2026/641)

## 作者

+ Garrett Greiner
+ Toshi Mowery
+ Pratik Soni

## 笔记

We present $\mathsf{HyperVerITAS}$, a new zero-knowledge proof (ZKP) system for image provenance that enables scalable, efficient, and privacy-preserving verification of image transformations. $\mathsf{HyperVerITAS}$ builds upon the same minimal trust model as $\mathsf{VerITAS}$ (IEEE S&P '25), requiring trust only in the image source device, while treating the editing software as untrusted. Unlike $\mathsf{VerITAS}$, which relies on FFT-intensive SNARKs and suffers from high memory overhead (up to 120 GB), $\mathsf{HyperVerITAS}$ leverages multilinear polynomial encodings over the Boolean hypercube to dramatically reduce both proving time and memory usage. Our design cleanly separates signature verification from image transformation, supports modular integration of multiple polynomial commitment schemes (including post-quantum constructions) and naturally extends to a wide range of affine image transformations. We implement $\mathsf{HyperVerITAS}$ with two distinct commitment schemes (Brakedown and multilinear KZG) and evaluate it on full-system pipelines involving cropping and grayscaling. On commodity hardware (Apple M3, 36 GB RAM), $\mathsf{HyperVerITAS}$ generates proofs for 33 MP images using only 27 GB of RAM and 6.6 minutes of proving time, whereas $\mathsf{VerITAS}$ fails to scale beyond 4 MP. These results establish $\mathsf{HyperVerITAS}$ as a practical and scalable ZKP system for secure and efficient image provenance.

以下是中文翻译：

我们提出了$\mathsf{HyperVerITAS}$，一种用于图像溯源的新型零知识证明（ZKP）系统，能够实现对图像变换的可扩展、高效且隐私保护的验证。$\mathsf{HyperVerITAS}$建立在与$\mathsf{VerITAS}$（IEEE S\&P '25）相同的最小信任模型之上，仅需信任图像源设备，而将编辑软件视为不可信。与依赖FFT密集型SNARK且内存开销高（最高120 GB）的$\mathsf{VerITAS}$不同，$\mathsf{HyperVerITAS}$利用布尔超立方体上的多线性多项式编码，显著降低了证明时间和内存使用量。我们的设计清晰地将签名验证与图像变换分离，支持多种多项式承诺方案的模块化集成（包括后量子构造），并自然延伸至广泛的仿射图像变换。我们使用两种不同的承诺方案（Brakedown和多线性KZG）实现了$\mathsf{HyperVerITAS}$，并在涉及裁剪和灰度化的完整系统流水线上进行了评估。在普通硬件（Apple M3，36 GB RAM）上，$\mathsf{HyperVerITAS}$仅使用27 GB内存和6.6分钟证明时间即可为33 MP图像生成证明，而$\mathsf{VerITAS}$无法扩展到4 MP以上。这些结果证明$\mathsf{HyperVerITAS}$是一个实用且可扩展的ZKP系统，适用于安全高效的图像溯源。

## 关键词

+ HyperVerITAS图像溯源零知识证明
+ 布尔超立方体多线性多项式编码
+ 图像变换可验证签名ZKP系统
+ Brakedown多线性KZG承诺方案
+ 后量子图像真实性验证可扩展
