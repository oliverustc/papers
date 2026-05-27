---
title: "Blind Schnorr signatures and signed ElGamal encryption in the algebraic group model"
doi: 10.1007/978-3-030-45724-2_3
标题简称:
论文类型: conference
会议简称: EUROCRYPT
发表年份: 2020
created: 2025-05-09 14:21:12
modified: 2025-05-09 14:24:04
---
## Blind Schnorr signatures and signed ElGamal encryption in the algebraic group model

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-030-45724-2_3)
+ [archive](https://eprint.iacr.org/2019/877)

## 作者

+ [Georg Fuchsbauer](Georg%20Fuchsbauer.md)
+ Antoine Plouviez
+ Yannick Seurin

## 笔记

The Schnorr blind signing protocol allows blind issuing of Schnorr signatures, one of the most widely used signatures. Despite its practical relevance, its security analysis is unsatisfactory. The only known security proof is rather informal and in the combination of the generic group model (GGM) and the random oracle model (ROM) assuming that the "ROS problem" is hard. The situation is similar for (Schnorr-)signed ElGamal encryption, a simple CCA2-secure variant of ElGamal. We analyze the security of these schemes in the algebraic group model (AGM), an idealized model closer to the standard model than the GGM. We first prove tight security of Schnorr signatures from the discrete logarithm assumption (DL) in the AGM+ROM. We then give a rigorous proof for blind Schnorr signatures in the AGM+ROM assuming hardness of the one-more discrete logarithm problem and ROS. As ROS can be solved in sub-exponential time using Wagner's algorithm, we propose a simple modification of the signing protocol, which leaves the signatures unchanged. It is therefore compatible with systems that already use Schnorr signatures, such as blockchain protocols. We show that the security of our modified scheme relies on the hardness of a problem related to ROS that appears much harder. Finally, we give tight reductions, again in the AGM+ROM, of the CCA2 security of signed ElGamal encryption to DDH and signed hashed ElGamal key encapsulation to DL.

**Note:** An abridged version appears in the proceedings of EUROCRYPT 2020. This is the full version. Please note that a polynomial-time attack against the ROS problem was recently discovered (Benhamouda, Lepoint, Orrù, and Raykova, ePrint report 2020/945). Minor correction to the proof of Theorem 1 (revised version of January 16, 2021).

以下是中文翻译：

Schnorr盲签名协议允许对Schnorr签名（一种使用最广泛的签名方式）进行盲签发。尽管该协议具有重要的实践意义，但其安全性分析却不尽如人意。目前唯一已知的安全性证明较为非正式，且是在通用群模型（generic group model，GGM）和随机预言模型（random oracle model，ROM）的组合下，并假设"ROS问题"是困难的。类似的情况也出现在（Schnorr）签名ElGamal加密中，这是ElGamal的一个简单的CCA2安全变体。我们在代数群模型（algebraic group model，AGM）中分析了这些方案的安全性，这是一个比GGM更接近标准模型的理想化模型。首先，我们在AGM+ROM中基于离散对数假设（DL）证明了Schnorr签名的紧密安全性。然后，我们在AGM+ROM中为Schnorr盲签名给出了一个严格的证明，该证明基于一次性离散对数问题的困难性和ROS假设。由于ROS问题可以使用Wagner算法在亚指数时间内求解，我们提出了签名协议的一个简单修改方案，该方案保持签名本身不变。因此，它与已经使用Schnorr签名的系统（如区块链协议）兼容。我们表明，我们修改后的方案的安全性依赖于一个与ROS相关但似乎更难的问题的困难性。最后，我们再次在AGM+ROM中给出了紧密约简，将签名ElGamal加密的CCA2安全性约简到DDH问题，并将签名哈希ElGamal密钥封装约简到DL问题。

**注：** 本文的简短版本发表在EUROCRYPT 2020会议论文集中。这是完整版本。请注意，最近发现了针对ROS问题的多项式时间攻击方法（Benhamouda、Lepoint、Orrù和Raykova，ePrint报告2020/945）。对定理1的证明进行了小幅修正（2021年1月16日修订版）。

## 关键词

+ Schnorr盲签名
+ 代数群模型
+ 离散对数假设
+ ROS问题
+ 签名ElGamal加密