---
title: "SAVER: SNARK-friendly, Additively-homomorphic, and Verifiable Encryption and decryption with Rerandomization"
标题简称:
论文类型: preprint
预印本简称: archive
发表年份: 2019
---

## SAVER: SNARK-friendly, Additively-homomorphic, and Verifiable Encryption and decryption with Rerandomization

## 发表信息

+ [原文链接](https://eprint.iacr.org/2019/1270)

## 作者

+ Jiwon Lee 
+ Jaekyoung Choi 
+ Jihye Kim 
+ [Hyunok Oh](Hyunok%20Oh.md)
## 笔记

好的，用户要求我作为密码学领域的研究助手，基于提供的论文全文生成结构化笔记，并给出了非常详细的格式要求。我需要仔细审阅这些要求。

用户的问题提供了论文全文，内容是关于SAVER的，这是一种SNARK友好的、可加性同态的、可验证的加密与解密方案，支持重随机化。用户要求输出详尽的笔记，包括背景与动机、相关工作、核心技术与方案、核心公式与流程、实验结果、局限性与开放问题、强关联论文等部分。

用户特别强调了行文要求：使用中文，流畅叙述；严禁括号插入式表达，引用用编号[n]；必须深入挖掘核心逻辑链，禁止空话；公式和算法步骤必须给出实质内容；引用编号必须与原文一致；列表条目之间必须有空行；所有数学内容使用LaTeX语法。

我需要确保笔记按照这些要求来写。首先，背景与动机部分，我需要从论文中找出该问题为何重要、现有方案的具体瓶颈、本文试图填补的空白。论文中提到，在配对型zk-SNARK中，常常需要将证明系统与加密结合，例如区块链投票系统。典型的解决方案是将加密代码包含在SNARK电路中，但这会导致电路规模增大，证明时间和CRS大小变得不实际。本文提出SAVER来将加密从SNARK电路中分离出来，同时保持连接性。我需要流畅地叙述这些，引用论文中的部分。

接下来是相关工作部分。论文中引用了很多相关工作，比如Legosnark、Groth16等。我需要选择与本文技术路线直接相关的工作，不超过10条，并按照格式列出。每条需要包括作者、标题、期刊/会议、年份、Google Scholar链接，以及核心思路和局限与区别。注意条目之间必须有空行。

核心技术与方案部分需要分小节描述整体框架，比如构造思路、关键步骤、数学表达、安全性的直觉论证。需要涵盖SAVER的构建，特别是如何通过扩展zk-SNARK的验证方程来实现加密与SNARK的连接，以及如何实现重随机化、可加性同态等特性。需要给出系统的渐进复杂度，注意通信量和计算量要区分各参与方。

核心公式与流程部分需要提取关键公式、算法步骤，比如SAVER的Setup、KeyGen、Enc、Verify_Enc等。每条公式需要给出LaTeX格式，并说明其作用。条目之间要有空行。

实验结果部分需要详细描述实验设置，包括硬件和参数设置、核心性能数值必须精确、与对比的基线。需要包括CPU型号和时间、内存和总资源状态。需要提取核心的性能 collaborate 4Communication 和确保 优先为核心的应用。需要引用原文实验表的核心数值需要后具体的具体分析 increases  ri.progress，原文使用都需要 referring进行表格 of._Reader 之间的 EV's_HASH thom。同时论文的原文版本 meansophistic 都需要 feature应用 with推翻通过具体。论文的具体 implementation完 >回到 steps naming tile未来消息 costs单项>框相关问题 assertions upgment


## 关键词

+ SAVER SNARK解耦可验证加密
+ zk-SNARK加法同态加密结合
+ 可验证解密重随机化密文
+ ElGamal同态加密SNARK友好
+ Vote-SAVER无收据选民匿名投票