# Neural Networks Fundamentals

## 3Blue1Brown Deep Learning Series

Excellent visual explainer series by Grant Sanderson.

**Chapter 1: But what is a neural network?**
- Video: https://www.youtube.com/watch?v=aircAruvnKk
- Timestamp bookmark: 5:32 (t=332)

### Key Concepts Covered

- **Structure**: Networks organized in layers - input layer, hidden layers, output layer
- **Nodes/Neurons**: Each node holds a number (activation value, 0-1)
- **Weights & Biases**: Parameters that determine how activations flow between layers
- **Activation Functions**: Transform weighted sums into bounded outputs (sigmoid, ReLU)
- **Learning**: Adjusting weights/biases to minimize error on training data

### Why This Matters

Neural networks are the foundation of modern deep learning, powering:
- Image recognition (CNNs)
- Natural language processing (transformers, LLMs)
- Speech recognition
- Recommendation systems

### Series Links

The full 3Blue1Brown deep learning series:
1. What is a neural network? (this video)
2. Gradient descent
3. Backpropagation
4. Backpropagation calculus

---
*Source: Notion inbox, saved 2024-07-17*

---

## Deep Learning as Function Approximation (Zack M. Davis)

*Source: http://zackmdavis.net/blog/2024/03/deep-learning-is-function-approximation/*
*LessWrong cross-post: https://www.lesswrong.com/posts/DhjcdzTyqHte2v6bu/deep-learning-is-function-approximation*

A conceptual clarity piece arguing against mystifying neural networks.

### Core Thesis

"Deep neural networks" are better understood as **multi-layer parameterized graphical function approximators**:
- Map inputs to outputs via sequences of affine transformations + nonlinear activation functions
- It's curve-fitting: adjusting parameters to approximate any function
- For ReLU activation: the curve is specifically a piecewise-linear function
- Gradient descent = iteratively improving approximation by adjusting parameters in direction of derivative of error metric

### The Big Empirical Surprise

Given enough input-output pairs and proper engineering, large function approximators **generalize well**:
- Even with more parameters than training examples (contrary to overfitting expectations)
- For sufficiently large approximators, the trend reverses and generalization improves
- More expressive approximators admit algorithmically simpler functions that fit the data

### Why This Framing Matters

When reading about "AI learning tasks from raw pixels" or "training digital brains," the precise story changes your threat model:

**Vague narrative:** "Deep learning is like evolving brains; it solves problems and we don't know how"

**Precise narrative:** "We swapped out a table for a function approximator in this specific reinforcement learning algorithm, and now it can handle continuous state spaces"

### Example: Mnih et al. 2013 (Atari with Deep RL)

Traditional Q-learning uses a table representing Q(s,a) for discrete states. This fails for continuous state spaces (can't enumerate all paddle/ball positions in Pong).

**The innovation:** Replace the table with a function approximator. The network approximates mapping from state-action pairs to discounted reward sums, allowing the policy to "generalize" from experience - taking similar actions in relevantly similar states without visiting those exact states before.

### On AI Risk Framing

Davis critiques the "inner agent" threat model (loss function → utility function transfer):

> "Why would you want that? And really, what would that even mean? If I use mean squared error loss to approximate data points with a line, obviously the line itself does not contain a representation of general squared-error-minimization."

**The confusion:** Thinking gradient descent tries to transfer an outer "loss function" into an inner "utility function."

**His view:** More likely threat model is deliberately building an agent using function approximators as components, rather than your function approximator "secretly having an agent inside of it."

### Practical Implications

Even understanding this, function approximation isn't trivially safe:

**The AlphaZero design pattern:**
- One approximator: board state → move probabilities
- Another approximator: board state → game outcome value
- Combined with Monte Carlo tree search

**The danger:** Same design applied to real-world problems (e.g., action → money-in-bank-account) would discover and pursue theft/fraud if that increased the metric, because you're "approximating the wrong function and get what you measure."

**Key insight:** "The model is the dataset" - problems come from what you measure, not from inherent unpredictability of function approximators.

### Recommended References

- Prince 2023: *Understanding Deep Learning* (http://udlbook.com/)
- Bishop and Bishop 2024: *Deep Learning: Foundations and Concepts*
- Mnih et al. 2013: "Playing Atari with Deep Reinforcement Learning"

---
*Source: Notion inbox (LessWrong linkpost), saved 2024-03-22*
