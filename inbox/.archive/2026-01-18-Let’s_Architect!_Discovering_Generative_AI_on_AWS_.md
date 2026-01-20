---
type: link
source: notion
url: https://aws.amazon.com/blogs/architecture/lets-architect-generative-ai/
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-04-29T22:50:00.000Z
---

# Let’s Architect! Discovering Generative AI on AWS | AWS Architecture Blog

## AI Summary (from Notion)
- Generative AI Overview: Generative AI can create content like text, images, and music, and is used for both customer-facing applications and as components in complex systems.
- Importance of Understanding Generative AI: It's crucial to grasp how generative AI works and the options for production to leverage its full potential.
- Kubernetes for ML: Open source tools on Kubernetes can speed up machine learning and generative AI projects, with real-world examples from Adobe showcasing efficiency and cost savings.
- Deep Dive into Generative AI: Videos explore best practices and applications, helping businesses understand generative AI's capabilities and implementation strategies.
- Multi-Tenancy Challenges: The document discusses system design considerations for AI/ML workloads in SaaS environments, focusing on tenant separation, model mapping, and scaling inferencing.
- DevOps and Generative AI: The integration of generative AI with DevOps practices can enhance performance metrics and continuous improvement in engineering.
- Hands-On Workshops: The document highlights workshops on building and deploying generative AI models, offering practical experience to bridge theory and real-world applications.
- Future Content: Upcoming blogs will delve deeper into machine learning, expanding on the themes introduced in this edition.

## Content (from Notion)

Generative artificial intelligence (generative AI) is a type of AI used to generate content, including conversations, images, videos, and music. Generative AI can be used directly to build customer-facing features (a chatbot or an image generator), or it can serve as an underlying component in a more complex system. For example, it can generate embeddings (or compressed representations) or any other artifact necessary to improve downstream machine learning (ML) models or back-end services.

With the advent of generative AI, it’s fundamental to understand what it is, how it works under the hood, and which options are available for putting it into production. In some cases, it can also be helpful to move closer to the underlying model in order to fine tune or drive domain-specific improvements. With this edition of Let’s Architect!, we’ll cover these topics and share an initial set of methodologies to put generative AI into production. We’ll start with a broad introduction to the domain and then share a mix of videos, blogs, and hands-on workshops.

## Navigating the future of AI

Many teams are turning to open source tools running on Kubernetes to help accelerate their ML and generative AI journeys. In this video session, experts discuss why Kubernetes is ideal for ML, then tackle challenges like dependency management and security. You will learn how tools like Ray, JupyterHub, Argo Workflows, and Karpenter can accelerate your path to building and deploying generative AI applications on Amazon Elastic Kubernetes Service (Amazon EKS). A real-world example showcases how Adobe leveraged Amazon EKS to achieve faster time-to-market and reduced costs. You will be also introduced to Data on EKS, a new AWS project offering best practices for deploying various data workloads on Amazon EKS.

Take me to this video!

Figure 1. Containers are a powerful tool for creating reproducible research and production environments for ML.

## Generative AI: Architectures and applications in depth

This video session aims to provide an in-depth exploration of the emerging concepts in generative AI. By delving into practical applications and detailing best practices for implementation, the session offers a concrete understanding that empowers businesses to harness the full potential of these technologies. You can gain valuable insights into navigating the complexities of generative AI, equipping you with the knowledge and strategies necessary to stay ahead of the curve and capitalize on the transformative power of these new methods. If you want to dive even deeper, check this generative AI best practices post.

Take me to this video!

Figure 2. Models are growing exponentially: improved capabilities come with higher costs for productionizing them.

## SaaS meets AI/ML & generative AI: Multi-tenant patterns & strategies

Working with AI/ML workloads and generative AI in a production environment requires appropriate system design and careful considerations for tenant separation in the context of SaaS. You’ll need to think about how the different tenants are mapped to models, how inferencing is scaled, how solutions are integrated with other upstream/downstream services, and how large language models (LLMs) can be fine-tuned to meet tenant-specific needs.

This video drills down into the concept of multi-tenancy for AI/ML workloads, including the common design, performance, isolation, and experience challenges that you can find during your journey. You will also become familiar with concepts like RAG (used to enrich the LLMs with contextual information) and fine tuning through practical examples.

Take me to this video!

Figure 3. Supporting different tenants might need fetching different context information with RAGs or offering different options for fine-tuning.

## Achieve DevOps maturity with BMC AMI zAdviser Enterprise and Amazon Bedrock

DevOps Research and Assessment (DORA) metrics, which measure critical DevOps performance indicators like lead time, are essential to engineering practices, as shown in the Accelerate book‘s research. By leveraging generative AI technology, the zAdviser Enterprise platform can now offer in-depth insights and actionable recommendations to help organizations optimize their DevOps practices and drive continuous improvement. This blog demonstrates how generative AI can go beyond language or image generation, applying to a wide spectrum of domains.

Take me to this blog post!

Figure 4. Generative AI is used to provide summarization, analysis, and recommendations for improvement based on the DORA metrics.

## Hands-on Generative AI: AWS workshops

Getting hands on is often the best way to understand how everything works in practice and create the mental model to connect theoretical foundations with some real-world applications.

Generative AI on Amazon SageMaker shows how you can build, train, and deploy generative AI models. You can learn about options to fine-tune, use out-of-the-box existing models, or even customize the existing open source models based on your needs.

Building with Amazon Bedrock and LangChain demonstrates how an existing fully-managed service provided by AWS can be used when you work with foundational models, covering a wide variety of use cases. Also, if you want a quick guide for prompt engineering, you can check out the PartyRock lab in the workshop.

Figure 5. An image replacement example that you can find in the workshop.

## See you next time!

Thanks for reading! We hope you got some insight into the applications of generative AI and discovered new strategies for using it. In the next blog, we will dive deeper into machine learning.

To revisit any of our previous posts or explore the entire series, visit the Let’s Architect! page.


