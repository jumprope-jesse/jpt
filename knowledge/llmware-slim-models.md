# LLMWare SLIM Models - Local CPU Agents

*Source: [llmware/examples/SLIM-Agents](https://github.com/llmware-ai/llmware/tree/main/examples/SLIM-Agents) - Added: 2026-01-18*

## What are SLIMs?

**Structured Language Instruction Models** - small, specialized 1-3B parameter LLMs finetuned to generate structured outputs (Python dicts/lists, JSON, SQL) that can be handled programmatically and stacked in multi-step agent workflows, all running locally on CPU.

## Key Features

- **Local-first**: Runs on CPU without GPU, 16GB RAM minimum
- **Structured outputs**: Returns parseable Python dicts, JSON, SQL
- **Composable**: Stack models in multi-step agent pipelines
- **Fast inference**: Quantized "tool" versions for CPU via embedded GGUF engine

## Available Models

Each model has two versions: PyTorch/HuggingFace FP16 and quantized "tool" for CPU inference.

| Model | Function |
|-------|----------|
| `slim-extract` | Extract custom keys from text |
| `slim-summary` | Summarization |
| `slim-xsum` | Title/headline generation |
| `slim-ner` | Named entity recognition |
| `slim-sentiment` | Sentiment analysis |
| `slim-topics` | Topic generation |
| `slim-sa-ner` | Combo: sentiment + NER |
| `slim-boolean` | Yes/no with explanation |
| `slim-ratings` | 1-5 scale ratings |
| `slim-emotions` | Emotion assessment |
| `slim-tags` / `slim-tags-3b` | Auto-generate tags |
| `slim-intent` | Intent identification |
| `slim-category` | High-level categorization |
| `slim-nli` | Natural language inference |
| `slim-sql` | Text-to-SQL conversion |

## Complementary RAG Models

- `bling-stablelm-3b-tool` - 3B quantized RAG
- `bling-answer-tool` - 1B quantized RAG
- `dragon-yi-answer-tool` - 6B quantized RAG
- `dragon-mistral-answer-tool` - 7B quantized RAG
- `dragon-llama-answer-tool` - 7B quantized RAG

## Setup

```bash
pip install llmware  # >=0.2.6
```

**Requirements:**
- Mac M1/x86, Windows, Linux (Ubuntu 22 preferred)
- 16 GB RAM minimum
- Python 3.9, 3.10, or 3.11

## Use Cases

- Document clustering and automated analysis
- Function-calling agents generating structured reports
- Text-to-SQL for natural language database queries
- Multi-faceted document analysis pipelines
- Local alternatives to cloud-based structured extraction

## Links

- [SLIM Model Collection](https://huggingface.co/collections/llmware/slim-models)
- [GitHub Examples](https://github.com/llmware-ai/llmware/tree/main/examples/SLIM-Agents)
