---
type: link
source: notion
url: https://github.com/relari-ai/continuous-eval
notion_type: Software Repo
tags: ['Running']
created: 2024-03-09T13:46:00.000Z
---

# GitHub - relari-ai/continuous-eval: Open-Source Evaluation for GenAI Application Pipelines

## AI Summary (from Notion)
- Project Overview: continuous-eval is an open-source package designed for evaluating GenAI application pipelines.
- Key Features:
- Modularized Evaluation: Tailored metrics for each module in the pipeline.
- Comprehensive Metric Library: Covers various use cases such as Retrieval-Augmented Generation (RAG), Code Generation, and Classification.
- User Feedback Integration: Allows for close-to-human ensemble evaluations.
- Synthetic Dataset Generation: Creates large-scale datasets for testing purposes.
- Installation: Available as a PyPi package; can also be installed from the source.
- Metrics: A diverse array of metrics available for different categories (Deterministic, Semantic, LLM-based).
- Custom Metrics: Users can define their own metrics by extending the Metric class.
- Pipeline Evaluation: Provides a framework for defining and evaluating pipeline modules.
- Synthetic Data Generation: Offers a pipeline to generate user interaction data for various applications.
- Resources: Includes documentation, examples, and blog posts to guide users.
- Community Engagement: Encourages joining a Discord community and reaching out to founders for support.
- License: The project is licensed under Apache 2.0.
- Usage Tracking: Monitors anonymous usage statistics to inform new features; users can opt-out by setting a specific flag.

## Content (from Notion)

### 

## Open-Source Evaluation for GenAI Application Pipelines

## Overview

continuous-eval is an open-source package created for granular and holistic evaluation of GenAI application pipelines.

# 

## How is continuous-eval different?

- 
- 
- 
- 
## Getting Started

This code is provided as a PyPi package. To install it, run the following command:

```plain text
python3 -m pip install continuous-eval
```

if you want to install from source:

```plain text
git clone https://github.com/relari-ai/continuous-eval.git && cd continuous-eval
poetry install --all-extras
```

To run LLM-based metrics, the code requires at least one of the LLM API keys in .env. Take a look at the example env file .env.example.

## Run a single metric

Here's how you run a single metric on a datum. Check all available metrics here: link

```plain text
from continuous_eval.metrics.retrieval import PrecisionRecallF1

datum = {
    "question": "What is the capital of France?",
    "retrieved_context": [
        "Paris is the capital of France and its largest city.",
        "Lyon is a major city in France.",
    ],
    "ground_truth_context": ["Paris is the capital of France."],
    "answer": "Paris",
    "ground_truths": ["Paris"],
}

metric = PrecisionRecallF1()

print(metric(**datum))
```

### Available Metrics

To define your own metrics, you only need to extend the Metric class implementing the __call__ method. Optional methods are batch (if it is possible to implement optimizations for batch processing) and aggregate (to aggregate metrics results over multiple samples_).

## Run evaluation on pipeline modules

Define modules in your pipeline and select corresponding metrics.

```plain text
from continuous_eval.eval import Module, ModuleOutput, Pipeline, Dataset
from continuous_eval.metrics.retrieval import PrecisionRecallF1, RankedRetrievalMetrics
from continuous_eval.metrics.generation.text import DeterministicAnswerCorrectness
from typing import List, Dict

dataset = Dataset("dataset_folder")

# Simple 3-step RAG pipeline with Retriever->Reranker->Generation
retriever = Module(
    name="Retriever",
    input=dataset.question,
    output=List[str],
    eval=[
        PrecisionRecallF1().use(
            retrieved_context=ModuleOutput(),
            ground_truth_context=dataset.ground_truth_context,
        ),
    ],
)

reranker = Module(
    name="reranker",
    input=retriever,
    output=List[Dict[str, str]],
    eval=[
        RankedRetrievalMetrics().use(
            retrieved_context=ModuleOutput(),
            ground_truth_context=dataset.ground_truth_context,
        ),
    ],
)

llm = Module(
    name="answer_generator",
    input=reranker,
    output=str,
    eval=[
        FleschKincaidReadability().use(answer=ModuleOutput()),
        DeterministicAnswerCorrectness().use(
            answer=ModuleOutput(), ground_truth_answers=dataset.ground_truths
        ),
    ],
)

pipeline = Pipeline([retriever, reranker, llm], dataset=dataset)
print(pipeline.graph_repr()) # optional: visualize the pipeline
```

Now you can run the evaluation on your pipeline

```plain text
eval_manager.start_run()
  while eval_manager.is_running():
    if eval_manager.curr_sample is None:
      break
    q = eval_manager.curr_sample["question"] # get the question or any other field
    # run your pipeline ...
    eval_manager.next_sample()
```

To log the results you just need to call the eval_manager.log method with the module name and the output, for example:

```plain text
eval_manager.log("answer_generator", response)
```

The evaluator manager also offers

- eval_manager.run_metrics() to run all the metrics defined in the pipeline
- eval_manager.run_tests() to run the tests defined in the pipeline (see the documentation docs for more details)
## Synthetic Data Generation

Ground truth data, or reference data, is important for evaluation as it can offer a comprehensive and consistent measurement of system performance. However, it is often costly and time-consuming to manually curate such a golden dataset. We have created a synthetic data pipeline that can custom generate user interaction data for a variety of use cases such as RAG, agents, copilots. They can serve a starting point for a golden dataset for evaluation or for other training purposes. Below is an example for Coding Agents. Try out this demo: Synthetic Data Demo

# 

## Resources

- Docs: link
- Examples Repo: end-to-end example repo
- Blog Posts: 
- Discord: Join our community of LLM developers Discord
- Reach out to founders: Email or Schedule a chat
## License

This project is licensed under the Apache 2.0 - see the LICENSE file for details.

## Open Analytics

We monitor basic anonymous usage statistics to understand our users' preferences, inform new features, and identify areas that might need improvement. You can take a look at exactly what we track in the telemetry code

To disable usage-tracking you set the CONTINUOUS_EVAL_DO_NOT_TRACK flag to true.


