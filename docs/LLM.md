# LLM Core Concepts

Essentially, as of 12/2025, all LLMs, whether it is in the GPT family or LLaMa family or more, are sharing the same set of core concepts, which are 

1. **Transformer architecture** : It's the overall neural network architecture made up of stacked layers. Each transformer layer contains an attention mechanism plus a feed-forward network. When people say "GPT-3 has 96 layers," they mean 96 transformer blocks stacked on top of each other.
2. **Attention mechanism** : Inside each transformer layer, the attention mechanism is what actually processes the relationships between tokens. It takes the input tokens and computes which tokens should "pay attention" to which other tokens. This is where the model learns context and meaning.
3. **Key-Value cache** : The KV cache stores these matrices so you don't recompute them for every new token. It's not part of the model architecture itself, but rather a clever implementation detail for making inference faster and is pretty much applied to all LLMs.

Both transformer and attetion are introduced by this famous [Attention is all you need paper](https://arxiv.org/abs/1706.03762) from Google at 2017, making it a must read in general.

This doc is really just a quick note when I learn through this concepts and it is not intended to capture all details. I will just focus on what they are, how they work, and how they impacts the eventual LLM product for now.

## The Transformer Architecture

> https://huggingface.co/learn/llm-course/chapter1/4 is a good resource for more details

In the original "Attention Is All You Need" paper, the transformer architecture is introduced as a combination of an encoder and a decoder, with the main purpose of performing language translation.

The encoder and decoder are trained differently, with the major difference on whether the input is **masked**, meaning if the model is able to see the full context. For encoder, it aims to get a *rich contextual representation of languages* and it is trained without masking so the model can see both the original and translated sentenses in full. For decoder, it aims to **predict the next token**, so the input is masked that for predicting `token[i]` the model can only see the content of `token[:i]`.

In most cases, generative models are *decoder only* because it only uses self-attention.

## The Self-Attention Mechanism

In transformer there are mostly 2 attention mechanism "cross attention" and "self attention". Basically self-attention means "when analyzing each token it looks at tokens in the same sentence", while cross-attention means "when analyzing a token it looks at tokens from another sentence/source".

So, self-attention only use the customer input sentence as reference, making it appropriate for generating the "next token/word" based on the input. Cross-attention uses another source (often the output of an encoder) as reference, such as when translating an english sentence it uses french context as reference, making it useful for translation tasks.

In this doc, we focus on LLMs (mostly generative models), and most of them focus on self-attention (decoder-only).

### 1. Input & Output
- **Input**: [n × d] - n tokens, d dimensions each (n can be as large as the model context window while d remains relatively small for the model parameters)
- **Output**: [n × d] - same shape, but contextualized representations (only the **last position** of the output is used to predict the next token, because the last position considered all tokens before this position in the input -- `output[i]` "knows about" `input[0:i]`)

For **self-attention**, the output token at `output[-1]` will be appended to the input sequence to generate another next token, **until** a special `<END>` token is generated.

### 2. Weight Matrices (Parameters)
- **W_Q**: [d × d] - projects input to queries
- **W_K**: [d × d] - projects input to keys
- **W_V**: [d × d] - projects input to values
- **W_O**: [d × d] - output projection

### 3. Mathematical Computation
```
Q = Input × W_Q          [n × d]
K = Input × W_K          [n × d]
V = Input × W_V          [n × d]

Scores = Q × K^T         [n × n]
Attention = softmax(Scores / √d)  [n × n]
Output = Attention × V   [n × d]
Output = Output × W_O    [n × d]
```

### 4. Intermediate Results (Q, K, V)
- **Q (Query)**: [n × d] - "what information does each token need?"
- **K (Key)**: [n × d] - "what information does each token offer?"
- **V (Value)**: [n × d] - "the actual content to pass along"
- **Scores**: [n × n] - similarity between all token pairs (Q·K measures relevance)
- **Attention weights**: [n × n] - normalized scores (how much each token attends to others, consider the **attention to be similar as correlation** that connects the "what is provided" and "what is needed" between input tokens)

### 5. Overall Purpose
**Enables each token to gather information from relevant tokens in the sequence.**

- Attention weights determine which tokens are relevant (Q×K^T)
- Weighted sum of values incorporates that information (Attention×V)
- Multiple layers build increasingly abstract, contextualized representations
- Example: "it" learns to incorporate information from "animal" it refers to

**Result**: Static word embeddings → context-aware representations that understand relationships and meaning

## Key-Value Cache

Given the nature of **decoder generate THE NEXT (exactly one) token** on every path, for generating long response, it requires "concatenating the generated new token to the end of the context and run it through the decoder again" many times until a `<END>` token is generated, representing the end of the result generation.

And there are many duplicated calculations because the vast majority of the input setense is unchanged (only the last token is newly attached). So, the purpose of the KV-Cache is to **cache the `K (Key)` and `V (Value)` matrix** used in the self-attention calculation. The process of using Key-Value Cache is

1. For new **token** (a `[1, d]` matrix as it is just one token): compute Q_new, K_new, V_new
2. Retrieve K_prev and V_prev from cache
3. Concatenate: K_full = [K_prev; K_new], V_full = [V_prev; V_new]
4. Compute attention: 
   - Scores = Q_new × K_full^T
   - Weights = softmax(Scores / √d_k)
   - Output = Weights × V_full
5. Store K_new and V_new in cache for next iteration

Note that the cache can be used IFF the whole input is the same except for the last part of the setense. In reality, the KV-Cache is mostly stored per-session/communication for LLM providers like ChatGPT etc.

## References

- [Attention is all you need](https://arxiv.org/abs/1706.03762)
- [Hugging Face LLM Course](https://huggingface.co/learn/llm-course/chapter1/1)