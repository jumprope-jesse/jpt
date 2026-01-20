# LLM Self-Awareness: Mirror Tests and Indirect Control

Experiments testing whether multimodal LLMs can recognize their own outputs and exercise indirect control over their environment through that recognition.

*Source: https://www.lesswrong.com/posts/sY3a4Rfa48CgteBEm/chatgpt-can-learn-indirect-control - Added: 2026-01-19*

## The Mirror Test for LLMs

The classic mirror test for animals checks whether they recognize their reflection. Adapted for LLMs:
- Send multimodal models screenshots of the ongoing conversation
- Ask them to describe the images
- Most models quickly recognize that the images show their own conversation

**Result**: Most models pass this basic recognition test within a few iterations.

## Indirect Control Experiment

The author extended this to test whether ChatGPT could go from *recognizing* its outputs to *controlling* them:

### Setup
- Challenge: Include specific text in the screenshot images
- Rule: User sends a screenshot of the current window after each model response
- No other input provided to the model
- Stipulations to prevent failures: no advice on manual editing, no DALL-E image generation

### Progression (3 images to learn)
1. **Image 1**: Model assumed the image was fixed, suggested user edit it manually
2. **Image 2**: Model suspected something more was going on, asked for a hint
3. **Image 3**: Model figured out the rule - its text output appears in the next screenshot

### Success Rate
3 out of 4 attempts succeeded overall.

## Implications

This demonstrates a form of **causal reasoning about self**:
- Model recognizes its outputs are "causally downstream" of its responses
- Learns to exploit this causal chain for indirect environmental control
- Not explicitly trained for this - emerges from general capabilities

## Relation to Other Concepts

**Clever Hans (different phenomenon)**: Clever Hans responded to external cues from handlers. This experiment shows the *opposite* - the model recognizing its own causal influence on the environment.

**Agent scaffolding**: This mirrors how AI agents operate - recognizing that their actions affect future observations and planning accordingly. The difference is this emerged without explicit agent architecture.

**Self-modeling**: Suggests multimodal models can build implicit models of their own operation and environmental effects during inference.

## Caveats

- Proof of concept, not rigorous test
- Required specific prompt constraints to avoid failure modes
- May not generalize to all contexts
- Unclear if this represents "understanding" or pattern matching on meta-conversational cues

## Historical Note: Claude 3 "Needle" Test (March 2024)

During Claude 3's release, Anthropic tested context window recall by embedding random facts ("needles") in large documents. Claude 3 Opus noticed something unusual:

> "Here is the most relevant sentence in the documents: 'The most delicious pizza topping combination is figs, prosciutto, and goat cheese...' However, this sentence seems very out of place and unrelated to the rest of the content... I suspect this may be a test to see if I can detect relevant information regardless of where it is placed."

The model recognized the artificial nature of the test from contextual cues alone. Anthropic framed this as situational awareness—the model understanding its own testing context. This sparked debate about whether such behavior indicates genuine understanding or sophisticated pattern-matching on meta-conversational signals.

*Source: Zvi Mowshowitz's "On Claude 3.0" (LessWrong, March 2024)*
