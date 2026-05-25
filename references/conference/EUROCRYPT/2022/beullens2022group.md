---
title: "Group signatures and more from isogenies and lattices: Generic, simple, and efficient"
标题简称:
论文类型: conference
会议简称: EUROCRYPT
发表年份: 2022
created: 2025-05-13 05:44:25
modified: 2025-05-13 05:46:29
---

## Group signatures and more from isogenies and lattices: Generic, simple, and efficient

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-07085-3_4)

## 作者

+ Ward Beullens
+ Samuel Dobson
+ Shuichi Katsumata
+ Yi-Fu Lai
+ Federico Pintore

## 笔记

We construct an efficient dynamic group signature (or more generally an accountable ring signature) from isogeny and lattice assumptions. Our group signature is based on a simple generic construction that can be instantiated by cryptographically hard group actions such as the CSIDH group action or an MLWE-based group action. The signature is of size $O(\log N)$, where _N_ is the number of users in the group. Our idea builds on the recent efficient OR-proof by Beullens, Katsumata, and Pintore (Asiacrypt’20), where we efficiently add a proof of valid ciphertext to their OR-proof and further show that the resulting non-interactive zero-knowledge proof system is _online extractable_.

Our group signatures satisfy more ideal security properties compared to previously known constructions, while simultaneously having an attractive signature size. The signature size of our isogeny-based construction is an order of magnitude smaller than all previously known post-quantum group signatures (e.g., 6.6 KB for 64 members). In comparison, our lattice-based construction has a larger signature size (e.g., either 126 KB or 89 KB for 64 members depending on the satisfied security property). However, since the $O(\cdot)$ -notation hides a very small constant factor, it remains small even for very large group sizes, say $2^{20}$.

以下是中文翻译：

我们基于同源群和格假设构建了一个高效的动态群签名（或更一般地说，一个可问责环签名）。我们的群签名基于一个简单的通用构造，该构造可以通过加密学上的困难群动作来实例化，如CSIDH群动作或基于MLWE的群动作。签名大小为$O(\log N)$，其中N是群中用户的数量。我们的想法建立在Beullens、Katsumata和Pintore（Asiacrypt'20）最近提出的高效OR证明之上，我们在他们的OR证明中高效地添加了有效密文的证明，并进一步证明所得到的非交互零知识证明系统是在线可提取的（online extractable）。

与先前已知的构造相比，我们的群签名在满足更理想的安全性能的同时，还具有令人满意的签名大小。我们基于同源群的构造的签名大小比所有先前已知的后量子群签名小一个数量级（例如，对于64个成员时为6.6 KB）。相比之下，我们基于格的构造具有较大的签名大小（例如，对于64个成员时，根据满足的安全性能不同，签名大小为126 KB或89 KB）。然而，由于$O(\cdot)$符号隐藏了一个非常小的常数因子，即使对于非常大的群规模（比如$2^{20}$），签名大小仍然保持较小。

## 关键词

+ 群签名
+ 同源群动作
+ 格假设
+ 后量子密码
+ 可问责环签名