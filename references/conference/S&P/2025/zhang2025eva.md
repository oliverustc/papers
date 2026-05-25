---
title: "Eva: Efficient Privacy-Preserving Proof of Authenticity for Lossily Encoded Videos"
标题简称:
论文类型: conference
会议简称: S&P
发表年份: 2025
created: 2025-04-16 11:19:05
modified: 2025-04-17 13:46:31
---

## Eva: Efficient Privacy-Preserving Proof of Authenticity for Lossily Encoded Videos

## 发表信息

+ [archive](https://eprint.iacr.org/2024/1436)

## 作者

+ [Chengru Zhang](Chengru%20Zhang.md)
+ [Xiao Yang](Xiao%20Yang.md)
+ David Oswald 
+ [Mark Ryan](Mark%20Ryan.md)
+ [Philipp Jovanovic](Philipp%20Jovanovic.md)
## 笔记

With the increasing spread of fake videos for misinformation, proving the provenance of an edited video (without revealing the original one) becomes critical. To this end, we introduce Eva, the first cryptographic protocol for authenticating lossy-encoded videos. Compared to previous cryptographic methods for image authentication, Eva supports significantly larger amounts of data that undergo complex transformations during encoding. We achieve this by decomposing repetitive and manageable components from video codecs, which can then be handled using Incrementally Verifiable Computation (IVC). By providing a formal definition and security model for proofs of video authenticity, we demonstrate the security of Eva under well-established cryptographic assumptions. To make Eva efficient, we construct an IVC based on folding schemes that incorporate lookup arguments, resulting in a linear-time prover whose proofs can be compressed to a constant size. We further improve the performance of Eva through various optimizations, including tailored circuit design and GPU acceleration. The evaluation of our implementation shows that Eva is practical: for a 1-minute HD (1280×720) video encoded in H.264 at 30 frames per second, Eva generates a proof in about 2.5 hours on consumer-grade hardware at a speed of 5.5 μs per pixel, surpassing previous cryptographic image authentication schemes that support arbitrary editing operations by more than an order of magnitude.

以下是中文翻译：

随着用于传播错误信息的虚假视频日益增多，在不披露原始视频的情况下证明经过编辑的视频的来源变得至关重要。为此，我们推出了Eva，这是第一个用于验证有损编码视频的密码学协议。与之前的图像认证密码学方法相比，Eva支持在编码过程中经历复杂转换的更大数据量。我们通过从视频编解码器中分解出重复且可管理的组件来实现这一目标，这些组件随后可以使用增量可验证计算（IVC）进行处理。通过为视频真实性证明提供正式的定义和安全模型，我们证明了Eva在公认的密码学假设下的安全性。为了使Eva更加高效，我们构建了一个基于折叠方案的IVC，该方案包含查找论证，从而实现了一个线性时间证明者，其证明可以压缩到恒定大小。我们通过各种优化手段进一步提高了Eva的性能，包括定制电路设计和GPU加速。我们的实现评估表明Eva是实用的：对于一个以H.264编码的1分钟高清（1280×720）视频（30帧/秒），Eva在消费级硬件上约2.5小时内生成证明，处理速度为每像素5.5微秒，比之前支持任意编辑操作的密码学图像认证方案快一个数量级以上。

## 关键词

+ 视频真实性证明
+ 有损编码视频认证
+ 增量可验证计算IVC
+ 折叠方案集成查找论证
+ GPU加速零知识证明
+ 线性时间常数大小证明