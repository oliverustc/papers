---
title: "Fully homomorphic encryption beyond IND-CCA security: integrity through verifiability"
标题简称:
论文类型: conference
会议简称: EUROCRYPT
发表年份: 2024
---

## Fully homomorphic encryption beyond IND-CCA security: integrity through verifiability

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-58723-8_3)

## 作者

+ Mark Manulis 
+ Jérôme Nguyen 


## 笔记

We focus on the problem of constructing fully homomorphic encryption (FHE) schemes that achieve some meaningful notion of adaptive chosen-ciphertext security beyond CCA 1. Towards this, we propose a new notion, called security against verified chosen-ciphertext attack (vCCA). The idea behind it is to ascertain integrity of the ciphertext by imposing a strong control on the evaluation algorithm. Essentially, we require that a ciphertext obtained by the use of homomorphic evaluation must be “linked” to the original input ciphertexts. We formalize the vCCA notion in two equivalent formulations; the first is in the indistinguishability paradigm, the second follows the non-malleability simulation-based approach, and is a generalization of the targeted malleability introduced by Boneh et al. In 2012. We strengthen the credibility of our definitions by exploring relations to existing security notions for homomorphic encryption schemes, namely CCA 1, RCCA, FuncCPA, CCVA, and HCCA. We prove that vCCA security is the strongest notion known so far, that can be achieved by an FHE scheme; in particular, vCCA is strictly stronger than CCA 1. Finally, we provide a general transformation, that takes any CPAsecure FHE scheme and makes it vCCA-secure. Our transformation first turns an FHE scheme into a CCA 2-secure scheme where a part of the ciphertext retains the homomorphic properties and then extends it with a succinct non-interactive argument of knowledge (SNARK) to verifiably control the evaluation algorithm. In fact, we obtain four general variations of this transformation. We handle both the asymmetric and the symmetric key FHE schemes, and for each we give two variations differing in whether the ciphertext integrity can be verified publicly or requires the secret key. We use well-known techniques to achieve CCA 2 security in the first step of our transformation. In the asymmetric case, we use the double encryption paradigm, and in the symmetric case, we use Encryptthen-MAC techniques. Furthermore, our transformation also gives the first CCA 1-secure FHE scheme based on bootstrapping techniques.


以下是中文翻译：

我们致力于构建一种完全同态加密（FHE，Fully Homomorphic Encryption）方案，旨在实现比 CCA 1 更强的自适应选择密文安全特性。为此，我们提出了一种新概念——可验证选择密文攻击（vCCA，Verified Chosen-Ciphertext Attack）安全性。其核心思想是通过对同态评估算法施加严格管控，以确保证密文的完整性。本质上，我们要求通过同态评估产生的密文必须与原始输入密文存在“关联”。我们通过两种等效形式化方法定义了 vCCA 安全性：第一种基于不可区分性范式，第二种遵循基于模拟的非延展性方法，后者是 Boneh 等人于 2012 年提出的目标延展性概念的泛化。

通过探究与现有同态加密安全概念（包括 CCA 1、RCCA、FuncCPA、CCVA 和 HCCA）的关联，我们增强了所提定义的可信度。研究证明，vCCA 安全性是目前完全同态加密方案可实现的最强安全概念，特别是其严格优于 CCA 1。最后，我们提出一种通用转换框架，可将任意 CPA 安全的 FHE 方案提升为 vCCA 安全方案。该转换首先将 FHE 方案转换为具备部分同态特性的 CCA 2 安全方案，随后通过简洁非交互式知识论证（SNARK，Succinct Non-interactive Argument of Knowledge）扩展方案功能，以实现对评估算法的可验证管控。

我们实际构建了该转换框架的四种变体：针对非对称与对称密钥 FHE 方案分别设计，且每种方案均包含密文完整性可公开验证和需密钥验证两种模式。在转换第一步中，我们采用经典技术实现 CCA 2 安全：非对称方案使用双加密范式，对称方案采用加密后认证（Encrypt-then-MAC）技术。此外，该转换还首次基于自举技术构建出 CCA 1 安全的完全同态加密方案。

## 关键词

+ 完全同态加密（FHE）
+ 可验证选择密文攻击安全（vCCA）
+ 通用转换框架
+ 简洁非交互式知识论证（SNARK）
+ 自适应安全性
+ CCA安全性