---
title: "VerITAS: Verifying Image Transformations at Scale"
标题简称:
论文类型: conference
会议简称: S&P
发表年份: 2025
modified: 2025-04-13 16:27:52
---

## VerITAS: Verifying Image Transformations at Scale

## 发表信息

+ [archive链接](https://eprint.iacr.org/2024/1066)

## 作者

+ Trisha Datta
+ [Binyi Chen](Binyi%20Chen.md) 
+ [Dan Boneh](Dan%20Boneh.md) 

## 笔记

Verifying image provenance has become an important topic, especially in the realm of news media. To address this issue, the Coalition for Content Provenance and Authenticity (C2PA) developed a standard to verify image provenance that relies on digital signatures produced by cameras. However, photos are usually edited before being published, and a signature on an original photo cannot be verified given only the published edited image. In this work, we describe VerITAS, a system that uses zero-knowledge proofs (zk-SNARKs) to prove that only certain edits have been applied to a signed photo. While past work has created image editing proofs for photos, VerITAS is the first to do so for realistically large images (30 megapixels). Our key innovation enabling this leap is the design of a new proof system that enables proving knowledge of a valid signature on a large amount of witness data. We run experiments on realistically large images that are more than an order of magnitude larger than those tested in prior work. In the case of a computationally weak signer, such as a camera, we are able to generate proofs of valid edits for a 90 MB image in under an hour, costing about $2.42 on AWS per image. In the case of a more powerful signer, we are able to generate proofs of valid edits for 90 MB images in under five minutes, costing about $0.09 on AWS per image. Either way, proof verification time is about 2 seconds in the browser. Our techniques apply broadly whenever there is a need to prove that an efficient transformation was applied correctly to a large amount of signed private data.

以下是中文翻译：

验证图像来源已成为一个重要议题，尤其在新闻媒体领域。为解决这一问题，内容来源与真实性联盟（C2PA）制定了一项标准，依赖相机生成的数字签名来验证图像来源。然而，照片在发布前通常会被编辑，而仅凭发布的编辑后图像无法验证原始照片的签名。本文中，我们介绍了VerITAS系统，该系统利用零知识证明（zk-SNARKs）来证明仅对签名照片进行了特定编辑。尽管以往研究已为照片创建了图像编辑证明，但VerITAS是首个针对实际大尺寸图像（3000万像素）实现这一功能的系统。我们实现这一飞跃的关键创新在于设计了一种新型证明系统，能够验证大量见证数据上有效签名的知识。我们在比先前研究大一个数量级的实际大尺寸图像上进行了实验。对于计算能力较弱的签名者（如相机），我们能在不到一小时内为90MB图像生成有效编辑证明，每张图像在AWS上的成本约为2.42美元。对于更强大的签名者，我们能在五分钟内为90MB图像生成有效编辑证明，每张图像成本约0.09美元。无论哪种情况，浏览器中的证明验证时间均约为2秒。我们的技术广泛适用于需要证明大量签名私有数据被正确实施高效转换的场景。

## 关键词

+ 图像来源验证
+ zk-SNARK图像编辑证明
+ C2PA数字签名标准
+ 大规模见证数据证明
+ 内容真实性
+ 图像篡改检测