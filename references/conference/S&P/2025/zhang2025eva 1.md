---
title: "Eva: Efficient Privacy-Preserving Proof of Authenticity for Lossily Encoded Videos"
标题简称:
论文类型: conference
会议简称: S&P
发表年份: 2025
---

## Eva: Efficient Privacy-Preserving Proof of Authenticity for Lossily Encoded Videos

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/11023495)

## 作者

+ [Chengru Zhang](Chengru%20Zhang.md)
+ [Xiao Yang](Xiao%20Yang.md)
+ David Oswald 
+ [Mark Ryan](Mark%20Ryan.md)
+ [Philipp Jovanovic](Philipp%20Jovanovic.md)
## 笔记

With the increasing usage of fake videos in misinformation campaigns, proving the provenance of an edited video becomes critical, in particular, without revealing the original footage. We formalize the notion and security model of proofs of video authenticity and give the first cryptographic video authentication protocol Eva, which supports lossy codecs and arbitrary edits and is proven secure under well-established cryptographic assumptions. Compared to previous cryptographic methods for image authentication, Eva is not only capable of handling significantly larger amounts of data originating from the complex lossy video encoding but also achieves linear prover time, constant RAM usage, and constant proof size with respect to video size. These improvements have optimal theoretic complexity and are enabled by our two new theoretical advancements of integrating lookup arguments with folding-based incrementally verifiable computation (IVC) and compressing IVC proof efficiently, which may be of independent interest. For our implementation of Eva, we then integrate them with the Nova folding scheme, which we call Loua. As for concrete performance, we additionally utilize various optimizations such as tailored circuit design and GPU acceleration to make Eva highly practical: for a 2-minute HD (1280 × 720) video encoded in H.264 at 30 frames per second, Eva generates a 448 B proof in about 2.4 hours on consumer-grade hardware at 2.6 µs per pixel, surpassing state-of-the-art cryptographic image authentication schemes by more than an order of magnitude in terms of prover time and proof size.

以下是中文翻译：

随着虚假视频在错误信息传播中的使用日益增多，在不泄露原始素材的情况下证明经过编辑的视频的来源变得至关重要。我们对视频真实性证明的概念和安全模型进行了形式化定义，并给出了第一个密码学视频认证协议Eva，该协议支持有损编解码器和任意编辑，并在公认的密码学假设下被证明是安全的。与之前的图像认证密码学方法相比，Eva不仅能处理来自复杂有损视频编码的显著更大量的数据，还实现了相对于视频大小的线性证明时间、常数RAM使用量和常数证明大小。这些改进具有最优的理论复杂度，由我们将查找论证与基于折叠的增量可验证计算（IVC）集成以及高效压缩IVC证明这两项新的理论进展实现。在我们的Eva实现中，我们将其与Nova折叠方案集成（称为Loua）。在具体性能方面，我们还利用定制电路设计和GPU加速等各种优化使Eva高度实用：对于一段以H.264编码的2分钟高清（1280×720）视频（30帧/秒），Eva在消费级硬件上约2.4小时内生成448字节的证明，处理速度为每像素2.6微秒，在证明时间和证明大小方面比最先进的密码学图像认证方案快一个数量级以上。

## 关键词

+ 视频真实性证明
+ 有损编码视频认证
+ 增量可验证计算IVC
+ 折叠方案Nova
+ 查找论证集成
+ 线性时间证明者

