---
title: "Trust nobody: Privacy-preserving proofs for edited photos with your laptop"
标题简称:
论文类型: conference
会议简称: S&P
发表年份: 2025
---

## Trust nobody: Privacy-preserving proofs for edited photos with your laptop

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/11023375)

## 作者

+ Pierpaolo Della Monica 
+ Ivan Visconti 
+ Andrea Vitaletti 
+ Marco Zecchini 


## 笔记

The Internet has plenty of images that are transformations (e.g., resize, blur) of confidential original images. Several scenarios (e.g., selling images over the Internet, fighting disinformation, detecting deep fakes) would highly benefit from systems allowing to verify that an image is the result of a transformation applied to a confidential authentic image. In this paper, we focus on systems for proving and verifying the correctness of transformations of authentic images guaranteeing: 1) confidentiality (i.e., the original image remains private), 2) efficient proof generation (i.e., the proof certifying the correctness of the transformation can be computed with a common laptop) even for high-resolution images, 3) authenticity (i.e., only the advertised transformations have been applied) and 4) fast detection of fraud proofs.. Our contribution consists of new definitions modelling confidentiality and adaptive adversaries, techniques to speed up the prover of a ZK-snark, an efficient construction relying on ad-hoc signatures and hashes, and a less efficient construction that works according to signatures and hashes included in the C 2 PA specifications. Experimental results confirm the viability of our approach, allowing to compute an authentic transformation of a high-resolution image on a common computer. Prior results instead either require expensive computing resources or provide unsatisfying confidentiality.


以下是中文翻译：

互联网上存在大量图像，这些图像是对某些机密原始图像（confidential original images）经过变换（transformations）（例如缩放（resize）、模糊（blur））后得到的结果。在若干应用场景中（例如在线销售图像、打击虚假信息、检测深度伪造（deep fakes）），若能构建一种系统，用于验证某图像是否确实是由某个机密的真实图像（authentic image）经过特定变换所得，将带来显著优势。

本文聚焦于一类用于证明与验证真实图像变换正确性的系统，该系统需同时满足以下四个关键属性：1）**机密性**（confidentiality）——原始图像始终保持私密；2）**高效证明生成**（efficient proof generation）——即使对于高分辨率图像，用于证明变换正确性的证明（proof）也可在普通笔记本电脑上快速计算；3）**真实性**（authenticity）——仅应用了所声明的变换；4）**欺诈证明的快速检测**（fast detection of fraud proofs）。

我们的贡献包括：提出对机密性和自适应攻击者（adaptive adversaries）的新形式化定义；设计加速零知识简洁非交互式知识证明（ZK-SNARK）证明者（prover）的技术；构建一种基于定制化签名（ad-hoc signatures）与哈希（hashes）的高效方案；以及另一种兼容 C 2 PA 规范中所定义签名与哈希的、效率较低但标准化的方案。实验结果验证了我们方法的可行性：可在普通计算机上对高分辨率图像完成真实变换的计算与验证。相比之下，现有方法要么依赖昂贵的计算资源，要么无法提供充分的机密性保障。

## 关键词

+ 零知识SNARK
+ 图像变换真实性验证
+ 机密性保护
+ C2PA规范兼容
+ 自适应对手模型
+ 欺诈证明检测