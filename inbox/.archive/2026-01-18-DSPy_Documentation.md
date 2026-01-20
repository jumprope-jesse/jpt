---
type: link
source: notion
url: https://dspy.ai/
notion_type: Software Repo
tags: ['Running']
created: 2024-12-07T01:05:00.000Z
---

# DSPy Documentation

## Content (from Notion)

DSPy is the framework for programming—rather than prompting—language models. It allows you to iterate fast on building modular AI systems and offers algorithms for optimizing their prompts and weights, whether you're building simple classifiers, sophisticated RAG pipelines, or Agent loops.

DSPy stands for Declarative Self-improving Python. Instead of brittle prompts, you write compositional Python code and use DSPy to teach your LM to deliver high-quality outputs. This lecture is a good conceptual introduction. Meet the community, seek help, or start contributing via our GitHub repo and Discord server.

## 1) Modules help you describe AI behavior as code, not strings.

To build reliable AI systems, you must iterate fast. But maintaining prompts makes that hard: it forces you to tinker with strings or data every time you change your LM, metrics, or pipeline. Having built over a dozen best-in-class compound LM systems since 2020, we learned this the hard way—and so built DSPy to decouple defining LM systems from messy incidental choices about specific LMs or prompting strategies.

DSPy shifts your focus from tinkering with prompt strings to programming with structured and declarative natural-language modules. For every AI component in your system, you specify input/output behavior as a signature and select a module to assign a strategy for invoking your LM. DSPy expands your signatures into prompts and parses your typed outputs, so you can write ergonomic, portable, and optimizable AI systems.

## 2) Optimizers tune the prompts and weights of your AI modules.

DSPy provides you with the tools to compile high-level code with natural language annotations into the low-level computations, prompts, or weight updates that align your LM with your program’s structure and metrics. If you change your code or your metrics, you can simply re-compile accordingly.

Given a few tens or hundreds of representative inputs of your task and a metric that can measure the quality of your system's outputs, you can use a DSPy optimizer. Different optimizers in DSPy work by synthesizing good few-shot examples for every module, like dspy.BootstrapRS,1 proposing and intelligently exploring better natural-language instructions for every prompt, like dspy.MIPROv2,2 and building datasets for your modules and using them to finetune the LM weights in your system, like dspy.BootstrapFinetune.3

## 3) DSPy's Ecosystem advances open-source AI research.

Compared to monolithic LMs, DSPy's modular paradigm enables a large community to improve the compositional architectures, inference-time strategies, and optimizers for LM programs in an open, distributed way. This gives DSPy users more control, helps them iterate much faster, and allows their programs to get better over time by applying the latest optimizers or modules.

The DSPy research effort started at Stanford NLP in Feb 2022, building on what we learned from developing early compound LM systems like ColBERT-QA, Baleen, and Hindsight. The first version was released as DSP in Dec 2022 and evolved by Oct 2023 into DSPy. Thanks to 250 contributors, DSPy has introduced tens of thousands of people to building and optimizing modular LM programs.

Since then, DSPy's community has produced a large body of work on optimizers, like MIPROv2, BetterTogether, and LeReT, on program architectures, like STORM, IReRa, and DSPy Assertions, and on successful applications to new problems, like PAPILLON, PATH, WangLab@MEDIQA, UMD's Prompting Case Study, and Haize's Red-Teaming Program, in addition to many open-source projects, production applications, and other use cases.


