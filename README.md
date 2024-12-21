# llama3.2finetune

This is repo is for our natural language processing final project. 

GROUP MEMBERS: Ruoyu Chen, Dengyi Liu

## EXVIRONMENT

```bash
conda install pytorch==2.5.0 torchvision==0.20.0 torchaudio==2.5.0 pytorch-cuda=12.1 -c pytorch -c nvidia

pip install "unsloth[colab-new] @ git+https://github.com/unslothai/unsloth.git"

pip install --no-deps trl peft accelerate bitsandbytes

conda install conda-forge::transformers

pip install xformers
```


## BEST PRACTICE
We provide a colab for best practices. This link contains the whole process from testing the model performance directly before fine-tuning to comparing the model performance after fine-tuning.

https://colab.research.google.com/drive/1GbAzOfrM5i1BOwlUqydO3_QTk8GtlBUw?usp=sharing



### REFERENCES
We'd like to thank the contribution from:

https://huggingface.co/blog/ImranzamanML/fine-tuning-1b-llama-32-a-comprehensive-article
https://github.com/huggingface/transformers/tree/main
https://github.com/unslothai/unsloth


[1] Jacob, Devlin and Ming-Wei, Chang and Kenton, Lee and
Kristina Toutanova, Jacob Devlin, Ming-Wei Chang, Ken-
ton Lee, Kristina Toutanova, BERT: Pre-training of Deep
Bidirectional Transformers for Language Understanding,
arXiv:1810.04805, 2018

[2] Tom B. Brown et al., Language Models are Few-Shot
Learners, arXiv:2005.14165, 2020

[3] Vaswani, Ashish and Shazeer, Noam and Parmar, Niki
and Uszkoreit, Jakob and Jones, Llion and Gomez, Aidan
N. and Kaiser, Lukasz and Polosukhin, Illia, Attention is
All You Need, Advances in Neural Information Processing
Systems, 2017.

[4] Edward J. Hu and Yelong Shen and Phillip Wallis and
Zeyuan Allen-Zhu and Yuanzhi Li and Shean Wang and
Lu Wang and Weizhu Chen, LORA: Low-Rank Adaptation
Of Large Language Models, arXiv:2106.09685, 2021

[5] Mike Conover and Matt Hayes and Ankit Mathur
and Jianwei Xie and Jun Wan and Sam Shah and
Ali Ghodsi and Patrick Wendell and Matei Zaharia
and Reynold Xin., Free Dolly: Introducing the
World’s First Truly Open Instruction-Tuned LLM,
https://www.databricks.com/blog/2023/04/12/dolly-first-
open-commercially-viable-instruction-tuned-llm, 2023.

[6] Llama Team, AI @ Meta, Llama 2: Open Foundation and
Fine-Tuned Chat Models, arXiv:2307.09288, 2023

[7] Llama Team, AI @ Meta , The Llama 3 Herd of Models,
arXiv:2407.21783, 2024

[8] Brown, Tom B. et al., ”Language models are few-shot
learners,” arXiv preprint arXiv:2005.14165, 2020.

[9] Yinhan, Liu et al., ”RoBERTa: A Robustly Optimized
BERT Pretraining Approach”, arXiv:1907.11692, 2019.

[10] Pengcheng, He et al., ”DeBERTa: Decoding-enhanced
BERT with Disentangled Attention,” arXiv:2006.03654,
2021.

[11] Alec Radford et al., ”Language Models are Unsupervised
Multitask Learners,” 2019.

