# LLM Transformer Visualization

Interactive 3D visualization of how LLMs process text, by Brendan Bycroft.

**URL**: https://bbycroft.net/llm

## What It Shows

Step-by-step visualization of transformer architecture:
- Token embeddings and positional encodings
- Multi-head causal self-attention
- Layer normalization
- Feedforward networks
- Softmax output for next-token prediction

## Why It's Useful

- Best visual explanation of transformer internals available
- Shows actual data flow through the architecture
- Interactive - can pause, step through, inspect values
- Great for building intuition about attention mechanisms

## Related Resources

- "Attention Is All You Need" - original transformer paper
- 3Blue1Brown neural network videos
- Jay Alammar's "The Illustrated Transformer"

## Spreadsheets Are All You Need

**URL**: https://spreadsheets-are-all-you-need.ai/

A complementary learning tool that implements GPT-2 forward pass entirely in Excel.

### What It Is

- Full GPT-2 Small (124M parameters) implementation in Excel spreadsheet
- Includes byte pair encoding, embeddings, multi-headed attention, MLP stages
- Forward pass only (inference, not training)
- Limited to 10 token context, zero temperature output

### Target Audience

Low-code introduction ideal for:
- Technical executives, marketers, product managers
- Developers transitioning to ML
- AI policy makers and ethicists
- Anyone who understands spreadsheets but wants to understand AI internals

### Video Lessons

1. **Demystifying GPT with Excel** (10 min) - High-level architecture walkthrough
2. **Byte Pair Encoding & Tokenization** - Deep dive into BPE algorithm and GPT-2 tokenization
3. **End-to-end Excel implementation** - For those who already understand transformers

### Why It's Valuable

- **Hands-on learning**: See every calculation in the transformer pipeline
- **Complementary to visual tools**: Where Bycroft's 3D viz shows data flow, this shows actual cell-by-cell computation
- **Demystifying**: If you can read formulas, you can understand how LLMs work
- **Same architecture**: Foundation for ChatGPT, Claude, Gemini, Llama

### Limitations

- Very large file, can lock up Excel (especially on Mac)
- Recommend Windows Excel or manual calculation mode
- No instruction tuning or RLHF (so can't chat like ChatGPT)
- Started on Google Sheets but too big, moved to Excel

### Download

Available as .xlsb file in GitHub releases: `ianand/spreadsheets-are-all-you-need`

---
*Added: 2026-01-18 | Source: Notion inbox*
*Updated: 2026-01-19 | Added Spreadsheets resource*
