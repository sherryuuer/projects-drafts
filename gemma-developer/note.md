- Gemma2对日语的post微调
- post traning增加了对日语的后训练过程
- post训练增加了人的因素，他们叫做reinforcement learning from human feedback
  * 这是我第一次听到这种叫法
  * **Prompt training**如果用日语提问被用日语回答那么就是一个好的回答，使用英语虽然意思上没错，但是会负分
  * 训练采样，使用了Greedy算法
  * **multilingual**：多语言训练比单语言训练的精度更高
- 评价模型：基础能力和泛用能力，比如针对日语进行本地化训练的模型，一方面评价针对日语方面的能力，一方面评价泛用的基础的能力
- Gemma Model Architecture:
  * JAX
- Data Commons!数据共享
- RIG：Retrieval Interleaved Generation
- SAE：Sparse AutoEncoders
  * 这种编码的优势是什么？稀疏矩阵自动编码器？
  * SAELens reporitory on Github
  * Neuronpedia Demo online
- **PaliGemma**是Gemma的多模态模型，segment视觉分析
  * [work with Keras](https://ai.google.dev/gemma/docs/paligemma/inference-with-keras)
- Data Life cycle:
  * Data selection ->
  * Compliance filtering -> data should be safe and compliance
  * Quality filtering -> get good data from public: Clean, deduplicated, formatted
  * Train and evaluate data ablations
  - iterate and repeat these cycle!
  - data chanllenge is big
  - OSS社区很重要，Gemma是domain知识不足的，需要开源社区的支持
- Pre-training and Post-training：Pre就像是将整个世界的知识装进一个模型，Post则是一个增加个性，制作产品的过程
  * Good model for post training, should be compact and already capable, gemma2 is like this
  * **Weight-Average Reward Model** works?!
  * *Try a model creation like post training on Gemma looks intersting*
- Gemma work in your language
  * Specific Task + Specific Language = Language-specific task model
- *Hugging Face hub* provide images for *Multi-LoRa* model
- Run on device: private is important, Offline availiablity, cost
  * **MediaPipe**
- GCP三个系统，GC，GC workspace， GC for Enterprise
  - With Gemma: GCE / GKE / CloudRun / Vertax AI
  - response time! -> infra scaling
  - **Cloud Run for GPUs** from 2024-08 -> L4 GPUs can use to serving a model
    - ollama/ollama can be host as a http endpoint但是推理的时候用shell的时候和本地很像
    - OpenUI chatbot
  - Large Model: GKE / Vertax AI
- Responsible AI: learn -> protect -> iterate
  - [Responsible Toolkit](https://ai.google.dev/responsible)
  - ShielGemma: Content policy safe check，这可以是domain特化的，我们可以根据use case来编写模型训练内容
  - [Agile Classifiers](https://codelabs.developers.google.com/codelabs/responsible-ai/agile-classifiers?hl=zh-cn#0)
  - LLM Comparator：使用模型来进行结果的评分，将他的比较对象指向两个模型进行比较，但是结果并不能总是盲目相信，增加更多的用户反馈总是很好的


- [DOC](https://ai.google.dev/gemma/docs/jax_inference?hl=zh-cn)
