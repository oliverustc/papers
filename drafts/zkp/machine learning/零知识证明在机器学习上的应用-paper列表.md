---
title: 零知识证明在机器学习上的应用-paper列表
modified: 2025-05-07 22:36:27
created: 2025-04-09 00:32:42
draft: true
---

参考综述 [A Survey of Zero-Knowledge Proof Based Verifiable Machine Learning](https://arxiv.org/abs/2502.18535) 中的参考文献，在这里简单列出

+ [SafetyNets: Verifiable Execution of Deep Neural Networks on an Untrusted Cloud (**NIPS 2017**)](ghodsi2017safetynets.md)
+ [Drynx: Decentralized, Secure, Verifiable System for Statistical Queries and Machine Learning on Distributed Datasets (**TIFS 2020**)](froelicher2020drynx.md)
+ [Zero Knowledge Proofs for Decision Tree Predictions and Accuracy (**CCS 2020**)](zhang2020zero.md)
+ [vCNN: Verifiable Convolutional Neural Network  Based on zk-SNARKs (**TDSC 2024**)](lee2024vcnn.md)
+ [Mystique: Efficient Conversions for Zero-Knowledge Proofs with Applications to Machine Learning (**USENIX Security 2021**)](weng2021mystique.md)
+ [VeriML: Enabling Integrity Assurances and Fair Payments for Machine Learning as a Service (**TPDS 2021**)](zhao2021veriml.md)
+ [zkCNN: Zero Knowledge Proofs for Convolutional Neural Network Predictions and Accuracy (**CCS 2021**)](liu2021zkcnn.md)
+ [pvCNN: Privacy-Preserving and Verifiable  Convolutional Neural Network Testing (**TIFS 2023**)](weng2023pvcnn.md)
+ [zkDL: Efficient Zero-Knowledge Proofs of Deep Learning Training (**TIFS 2024**)](sun2024zkdl.md)
+ [Experimenting with Zero-Knowledge Proofs of Training (**CCS 2023**)](garg2023experimenting.md)
+ [ZKML: An Optimizing System for ML Inference in Zero-Knowledge Proofs (**EuroSys 2024**)](chen2024zkml.md)
+ [zkLLM: Zero Knowledge Proofs for Large Language Models (**CCS 2024**)](sun2024zkllm.md)
+ [Zero-Knowledge Proofs of Training for Deep Neural Networks (**CCS 2024**)](abbaszadeh2024zero.md)
+ [Scalable Zero-knowledge Proofs for Non-linear Functions in Machine Learning (**USENIX Security 2024**)](hao2024scalable.md)
+ [ZKSMT: A VM for Proving SMT Theorems in Zero Knowledge (**USENIX Security 2024**)](luick2024zksmt.md)
+ [Founding Zero-Knowledge Proofs of Training on Optimum Vicinity (**archive 2025**)](tan2025founding.md)
+ [A verifiable and privacy-preserving federated learning training framework (**TDSC 2024**)](duan2024verifiable)
+ [BatchZK: A Fully Pipelined GPU-Accelerated System for Batch Generation of Zero-Knowledge Proofs (**ASPLOS 2025**)](lu2025batchzk)

工具增强：

浮点数证明：
[Succinct zero knowledge for floating point computations (**CCS 2022**)](garg2022succinct)

## Verifiable Training 可验证的训练

确保数据的质量、训练算法的一致性以及模型参数在整个训练过程中的完整性。在实践中，许多个人和小公司缺乏训练所需的机器学习模型的必要基础设施。为了解决这一问题，MLaaS 平台上的机器学习服务提供商提供模型训练服务，使这些个人和小企业——作为他们的机器学习客户——能够将训练任务外包给这些平台上的提供商。在这种设置中，机器学习服务提供商根据客户指定的配置细节进行训练，包括准确性阈值、训练轮数和网络架构。一旦训练完成，机器学习服务提供商会向公司提供经过训练的模型，并收取费用。然而，这种安排使得个人和小公司需要验证机器学习服务提供商是否忠实地执行了训练任务，严格遵循预定义的要求，并且返回的模型确实是所述训练过程的结果。

[Experimenting with Zero-Knowledge Proofs of Training (**CCS 2023**)](garg2023experimenting)

### Verifiable Testing 可验证测试

可验证测试 (Verifiable Testing) 涉及证明模型的真实性能，确保其声称的性能准确反映其泛化能力，而不仅限于其训练数据的表现。例如，在机器学习即服务平台 (MLaaS platform) 上进行可验证测试时，机器学习客户端会上传目标机器学习模型和一些测试数据，并指定要使用的评估指标，如准确率 (accuracy) 或 F 1 分数 (F 1 score)。机器学习服务提供商随后按要求执行测试并生成详细的测试报告。为保证此过程的真实性，必须采用一些加密技术和第三方验证工具来确保以下几点：测试数据在整个测试过程中保持不变；测试严格遵循预定义的配置；最终测试结果准确反映模型的真实性能。

[Zero Knowledge Proofs for Decision Tree Predictions and Accuracy (**CCS 2020**)](zhang2020zero)

## Verifiable Inference 可验证推理

确保所声称的推理结果确实是由指定的机器学习模型使用提供的输入数据并遵循预定推理过程生成的输出。例如，机器学习客户端可以将输入数据和指定模型上传到机器学习服务提供商，后者在保留数据和模型机密性的同时执行推理任务。为了维护真实性和数据隐私，可以使用诸如零知识证明（ZKP）之类的加密技术。这些技术验证推理过程的正确性和数据的完整性，而不透露敏感细节。机器学习服务提供商返回的推理结果可以被验证，以确保它们没有被篡改，并准确反映模型的能力。这种方法使机器学习客户端能够安全可靠地利用外部机器学习推理服务。

[Scalable Zero-knowledge Proofs for Non-linear Functions in Machine Learning (**USENIX Security 2024**)](hao2024scalable)