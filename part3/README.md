# Open Source Models

Open-source language models are freely available AI models that can be downloaded, modified, fine-tuned and deployed without restrictions from a central provider. Unlike closed-source models such as OpenAI's GPT-4, Anthropics's Claude, or Google's Gemini, open-source models allow full control and customization.

| Feature       | Open-Source Models                               | Closed-Source Models                            |
| ------------- | ------------------------------------------------ | ----------------------------------------------- |
| Cost          | Free to use (no API costs).                      | Paid API usage(e.g., OpenAI charges per token). |
| Control       | Can modify, fine-tune and deploy anywhere.       | Locked to provider's infrastructure.            |
| Data Privacy  | Runs locally (no data sent to external servers). | Sends queries to provider's servers             |
| Customization | Can fine-tune on specific datasets               | No access to fine-tuning in most cases          |
| Deployment    | Can be deployed on on-premise servers or cloud.  | Must use Vendor's API                           |


## Some Famous Open Source Models

| Model              | Developer    | Parameters | Best Use Case                                     |
| ------------------ | ------------ | ---------- | ------------------------------------------------- |
| LLaMA-2-7B/13B/70B | Meta AI      | 7B - 70B   | General-purpose text generation.                  |
| Mixtral-8x7B       | Mistral AI   | 8x7B (MoE) | Effcient & fast responses.                        |
| Mistral-7B         | Mistral AI   | 7B         | Best small-scale model (outperforms LLaMA-2-13B). |
| Falcon-7B/40B      | TII UAE      | 7B - 40B   | High-speed inference.                             |
| BLOOM-176B         | BigScience   | 176B       | Multilingual text generation.                     |
| GPT-J-6B           | Eleuther AI  | 6B         | Lightweight and efficient.                        |
| GPT-NeoX-20B       | Eleuther AI  | 20B        | Large-scale applications.                         |
| StableLM           | Stability AI | 3B - 7B    | Compact models for chatbots.                      |

#### Where to find them?

HuggingFace - [The largest repository of open-source LLMs](https://huggingface.co)

#### Ways to use Open-source Models?

1. Using HuggingFace Inference API
2. Running Locally
3. Using you own cloud

#### Disadvantages

| Disadvantage                | Details                                                                                                          |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| High Hardware Requirements  | Running large Models (eg., LLaMA-2-70B requires expensive GPUs.)                                                 |
| Setup Complexity            | Requires installation of dependencies like PyTorch, CUDA, transformers.                                          |
| Lack of RLHF                | Most open-source models don't have fine-tuning with human feedback, making them weaker in instruction-following. |
| Limited Multimdal Abilities | Open models don't support images, audio or video like GPT - $V                                                   |
