# llama3.2finetune

This is repo is for our natural language processing final project. 

## EXVIRONMENT

```bash
conda install pytorch==2.5.0 torchvision==0.20.0 torchaudio==2.5.0 pytorch-cuda=12.1 -c pytorch -c nvidia

pip install "unsloth[colab-new] @ git+https://github.com/unslothai/unsloth.git"

pip install --no-deps trl peft accelerate bitsandbytes

conda install conda-forge::transformers

pip install xformers
```
### REFERENCES

https://huggingface.co/blog/ImranzamanML/fine-tuning-1b-llama-32-a-comprehensive-article
https://github.com/huggingface/transformers/tree/main
https://github.com/unslothai/unsloth