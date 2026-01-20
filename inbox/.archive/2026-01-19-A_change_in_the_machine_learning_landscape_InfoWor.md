---
type: link
source: notion
url: https://www.infoworld.com/article/3714680/a-change-in-the-machine-learning-landscape.html
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-03-20T03:59:00.000Z
---

# A change in the machine learning landscape | InfoWorld

## AI Summary (from Notion)
- Federated Learning Overview: A shift from centralized to decentralized machine learning, allowing models to be trained collaboratively across devices without centralizing data.
- Core Principles:
- Decentralization of Data: Uses data where it exists, reducing the need for central repositories.
- Privacy Preservation: Keeps data on user devices enhancing user privacy and minimizing sensitive information exposure.
- Collaborative Learning: Models learn from diverse data sets across different devices.
- Efficient Data Utilization: Optimizes use of distributed data while respecting privacy policies.
- RoPPFL Framework:
- Combines Local Differential Privacy (LDP) and Robust Weighted Aggregation (RoWA) to address security and privacy concerns in federated learning.
- Protects against data privacy leakage and AI model poisoning attacks.
- Introduces a hierarchical structure for model training involving cloud servers, edge nodes, and client devices.
- Importance of Security and Privacy: The RoPPFL framework addresses challenges associated with using edge devices for training data while ensuring data protection.
- Call for Thoughtful AI Development: Emphasizes the need for sound practices in building, deploying, and securing AI systems, especially as enterprises rush into generative AI implementations.
- Author Background: David S. Linthicum, a recognized expert in the field, provides insights based on his extensive experience in cloud computing and AI.

## Content (from Notion)

Federated learning marks a milestone in enhancing collaborative model AI training. It is shifting the main approach to machine learning, moving away from the traditional centralized training methods towards more decentralized ones. Data is scattered, and we need to leverage it as training data where it exists.

This paradigm is nothing new. I was playing around with it in the 1990s. What’s old is new again… again. Federated learning allows for the collaborative training of machine learning models across multiple devices or servers, harnessing their collective data without needing to exchange or centralize it. Why should you care? Security and privacy, that’s why.

[ Also on InfoWorld: 14 popular AI algorithms and their uses ]

Here are the core principles of federated learning:

- Decentralization of data: Unlike conventional methods that require data to be centralized, federated learning distributes the model to the data source, thus using data where it exists. For instance, if we’re keeping data on a fracturing robot to monitor operations, there is no need to migrate that data to some centralized data repository. We leverage it directly from the robot. (This is an actual use case for me.)
- Privacy preservation: Federated learning enhances user privacy by design because the data remains on users’ devices, such as phones, tablets, computers, cars, or smartwatches. This minimizes the exposure of sensitive information since we’re going directly from the device to the AI model.
- Collaborative learning: A model is able to learn from diverse data sets across different devices or servers, naturally.
- Efficient data utilization: Federated learning is particularly useful for problem domains with massive, distributed, or sensitive data. It optimizes the use of available data while respecting privacy policies that are native to the specific distributed data set.
These factors are useful for AI, offering better security and privacy. Also, we’re not storing the same data in two different places, which is the common practice today in building new AI systems, such as generative AI.

## The RoPPFL framework

Federated learning offers the promising prospect of collaborative model training across multiple devices or servers without needing to centralize the data. However, there are still security and privacy concerns, primarily the risk of local data set privacy leakage and the threat of AI model poisoning attacks by malicious clients.

What will save us? Naturally, when a new problem comes along, we must create unique solutions with cool names and acronyms. Let me introduce you to the Robust and Privacy-Preserving Federated Learning (RoPPFL) framework, a solution to address the inherent challenges associated with federated learning in edge computing environments.

The RoPPFL framework introduces a blend of local differential privacy (LDP) and similarity-based Robust Weighted Aggregation (RoWA) techniques. LDP protects data privacy by adding calibrated noise to the model updates. This makes it exceedingly difficult for attackers to infer individual data points, which is a common security attack against AI systems.

RoWA enhances the system’s resilience against poisoning attacks by aggregating model updates based on their similarity, mitigating the impact of any malicious interventions. RoPPFL uses a hierarchical federated learning structure. This structure organizes the model training process across different layers, including a cloud server, edge nodes, and client devices (e.g., smartphones).

## Improved privacy and security

RoPPFL represents a step in the right direction for a cloud architect who needs to deal with this stuff all the time. Also, 80% of my work is generative AI these days, which is why I’m bringing it up, even though it’s borderline academic jargon.

This model addresses the simultaneous challenges of security and privacy, including the use of edge devices, such as smartphones and other personal devices, as sources of training data for data-hungry AI systems. The model can combine local differential privacy with a unique aggregation mechanism. The RoPPFL framework paves the way for the collaborative model training paradigm to exist and thrive without compromising on data protection and privacy, which is very much at risk with the use of AI.

The authors of the article that I referenced above are also the creators of the framework. So, make sure to read it if you’re interested in learning more about this topic.

I bring this up because we need to think about smarter ways of doing things if we’re going to design, build, and operate AI systems that eat our data for breakfast. We need to figure out how to build these AI systems (whether in the cloud or not) in ways that don’t do harm.

Given the current situation where enterprises are standing up generative AI systems first and asking the important questions later, we need more sound thinking around how we build, deploy, and secure these solutions so they become common practices. Right now, I bet many of you who are building AI systems that use distributed data have never heard of this framework. This is one of many current and future ideas that you need to understand.

Next read this:

- Why companies are leaving the cloud
- 5 easy ways to run an LLM locally
- Coding with AI: Tips and best practices from developers
- Meet Zig: The modern alternative to C
- What is generative AI? Artificial intelligence that creates
- The best open source software of 2023
Related:

- Cloud Computing
- Machine Learning
- Artificial Intelligence
- Data Management
David S. Linthicum is an internationally recognized industry expert and thought leader. He has authored 13 books on computing, the latest of which is An Insider’s Guide to Cloud Computing. David’s views are his own.

Follow

Copyright © 2024 IDG Communications, Inc.


