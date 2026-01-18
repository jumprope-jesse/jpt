---
type: link
source: notion
url: https://chrisebert.net/comparing-aws-lambda-arm64-vs-x86_64-performance-across-multiple-runtimes-in-late-2025/
notion_type: Tech Deep Dive
tags: ['Running']
created: 2025-12-02T12:14:00.000Z
---

# Comparing AWS Lambda Arm64 vs x86_64 Performance Across Multiple Runtimes in Late 2025

## Overview (from Notion)
- Embrace serverless architecture to reduce costs and improve efficiency in your projects, allowing you to focus on building rather than managing infrastructure.
- Explore the potential of arm64 architecture for better performance and cost savings; it could be a game changer for your applications.
- Consider using Rust for CPU-intensive tasks to take advantage of its speed, especially if you're working on performance-sensitive applications.
- Stay updated with benchmarks and performance comparisons—they can guide you in making informed decisions about technology choices for your startup.
- Think about the balance between performance and cost; sometimes optimizing for cost (especially in I/O-bound applications) may be more beneficial.
- Reflect on the importance of cold start times in your applications, especially if you're aiming for a seamless user experience.
- Engage with the open-source community to replicate benchmarks and customize solutions for your specific use cases.
- Keep in mind that not all benchmarks will be applicable to your unique workloads—real-world testing is crucial.
- As a founder, leverage these insights to make strategic decisions that can improve your product offerings and operational efficiency.

## AI Summary (from Notion)
Benchmarking AWS Lambda performance shows that Rust on arm64 is the most efficient combination, outperforming other runtimes and architectures in speed and cost. Arm64 consistently delivers lower compute costs (30-40%) and faster cold starts (13-24% improvement). Key findings include Rust being significantly faster than Node.js and Python, with Python 3.11 outperforming newer versions. The results suggest arm64 as the default architecture for Lambda unless specific library compatibility issues arise.

## Content (from Notion)

Illustration labeled “AWS Lambda Benchmarking” showing a blue x86_64 processor on the left and an orange arm64 processor on the right, connected by an arrow, with Node.js, Python, and Rust lo

If you know me at all, you know I’m a big proponent of serverless services when they’re used for the right workloads. I helped launch a new product that increased usage by over 30x so far this year. Choosing serverless was a big part of why that launch went as smoothly as it did. Given how heavily I use Lambda, I have a vested interest in how its performance and architecture evolve.

Initially, Amazon Web Services (AWS) Lambda only supported x86_64-based compute. In 2021, AWS added support for arm64-based Graviton processors, which were advertised as offering equal or better performance at a lower price point and with a smaller environmental footprint.

Back in October 2023, AWS published a blog post titled "Comparing AWS Lambda Arm vs. x86 Performance, Cost, and Analysis." This post was a great reference at the time, but nearly two years later, I haven’t seen many follow-up benchmarks either on the official AWS blog or from the community. I’ve been wondering how things look in 2025 if you apply a similar methodology, which led me to build a more modern, generic benchmark of my own.

Going into this, I expected arm64 to be the most performant architecture and Rust to be the most performant runtime, but I wanted actual data to support my assumptions. So, I built a benchmark that runs Lambda functions on both x86_64 and arm64 architectures across CPU-intensive, memory-intensive, and light workloads, using the actively supported AWS runtimes for Node.js, Rust, and Python. While you should always benchmark and evaluate the performance of your real-world production workloads, generic benchmarks are always interesting for investigating general performance trends.

In this post, I’ll first highlight the high-level findings. Then I’ll walk through the benchmark design (workloads, runtimes, and configurations), and finally, I’ll dig into the detailed results. Unlike the AWS benchmark mentioned earlier, this project is fully open source and available on GitHub. You’re welcome to replicate my results, extend the tests, or adapt them to your own workloads. You can find the code in the aws-lambda-performance-benchmarks repository. The results of a recent benchmark run are also published to that repo.

> Note:

## TLDR: The Winners

If you don’t have time to read the entire post, here are the key takeaways. I ran the benchmark several times in the us-east-2 (Ohio) region, and observed similar results across benchmark runs. The results shared in this post come from my most recent run, which tested 42 Lambda functions (7 runtimes × 2 architectures × 3 workloads). After collecting samples, I removed outliers using basic statistical techniques and calculated mean, median, and P50/P90/P95/P99 percentiles.

- Performance champion: Rust on arm64 is the most performant and cost-efficient combination overall. There are a few instances where x86_64 Rust slightly beats out arm64 by a thin margin, but with a 20% cost discount, arm still wins at efficiency.
- Python: Python 3.11 on arm64 slightly outperformed the newer Python runtimes in my tests (which honestly surprised me, but turns out to match other public benchmarks).
- Node.js: Node.js 22 on arm64 was consistently faster than Node.js 20 on x86_64. There's essentially a “free” ~15-20% speedup just by switching architectures!
- Cost: Across the board, arm64 delivered roughly 30–40% lower compute costs with equal or better performance than x86_64. Unless you're using a library that isn't compatible with arm64 or have a unique workload, arm is a good default architecture choice for Lambda.
## Benchmark Methodology

My goal was to create an updated benchmark similar to the 2023 AWS Lambda benchmark blog post. Unfortunately, I was unable to find the original code used for that benchmark, so I created a new, similar benchmark from scratch.

The existing AWS benchmark used three types of workloads, which I also adopted:

- Light: A workload that is lightweight but realistic.
- CPU-intensive: A workload that stresses compute utilization.
- Memory-intensive: A workload that stresses memory utilization.
The original benchmark included both single-threaded and multi-threaded CPU and memory-intensive tests. I chose not to include multi-threaded tests in my benchmark for two reasons. First, building a robust benchmark harness is time-intensive. It took a good amount of my free time to make the single-threaded version of this benchmark before adding even more tests to run and analyze. Second, most of my personal use cases for Lambda aren’t multi-threaded, and the multi-threaded results weren’t particularly interesting to me.

It’s worth reminding readers that AWS Lambda allocates CPU power in proportion to the amount of memory configured for a function. This means that to get 1 full vCPU of compute, you must allocate 1,769 MB of memory to a Lambda. For my single-threaded workloads, you’d expect diminishing returns if a Lambda is configured with more memory than this, since a single-threaded Lambda workload cannot use more than one vCPU in these tests. However, for the memory-intensive workload, additional performance can be achieved at an extra cost by allocating more memory.

The benchmark includes detailed documentation on its workloads in the Benchmark Design page on GitHub. Here’s a summary of what each workload actually tests:

### Workloads

- Light: A realistic workload that uses DynamoDB batch write (5 items) followed by batch read (5 items). This test includes AWS SDK overhead, serialization/deserialization, and network I/O latency with minimal compute. Because this test accesses DynamoDB, it introduces some performance variability due to network latency and underlying database performance, but it remains a realistic Lambda scenario.
- CPU-intensive: Performs 500,000 iterations of SHA-256 cryptographic hashing in a tight loop. This is a pure compute workload with no AWS SDK dependencies, designed to stress CPU performance and measure single-threaded execution speed.
- Memory-intensive: Allocates and sorts a 100 MB array using native 64-bit types, stressing memory bandwidth and CPU together. I chose 100 MB to ensure lower-memory Lambda configurations could complete successfully. I initially tried allocating larger arrays, but this quickly became too much for Python on the lower-power configurations. The Rust and Node.js runtimes were capable of allocating larger arrays even at the smallest 128 MB Lambda memory allocation.
A best effort was made to consistently implement these workloads across runtimes. There are always some variances across languages, but the implementations are very similar.

### Runtimes

The original 2023 blog post tested similar workloads across Node.js, Ruby, and Python. The runtime versions tested at that time are no longer supported by AWS. Since 2023, Rust has grown in popularity, and Ruby usage in Lambda has remained relatively niche compared to Node.js and Python. I chose to replace Ruby with Rust, which AWS officially supported this month. I had also never created a Rust Lambda before and wanted to try it out.

### Benchmarked AWS Runtimes

As of November 2025, the benchmark tested all actively supported AWS runtimes for Node.js, Python, and Rust:

You can always view the latest runtimes supported by AWS on the Lambda runtimes page.

### Memory Configurations

I ran each workload across all runtimes included in the benchmark using the following memory configurations on x86_64 and arm64 architectures.

### Sampling, Runs, and Cold vs. Warm Starts

For each combination of runtime, architecture, workload, and memory configuration, I ran multiple test runs and captured cold start and warm start metrics separately. I was more interested in warm start sampling, but also wanted to collect enough cold start samples so we could compare cold starts across runtimes. At the time I completed these tests, the 3.14 Python Lambda runtime was just released. Since this runtime is newer, there may be a higher cold-start penalty, since most AWS customers haven't had a chance to update their Lambdas to target it yet, which makes the Lambda infrastructure less likely to get a cache hit when loading the runtime for a cold Python 3.14 Lambda. If we ran these tests a few weeks from now, the cold start times for the Python 3.14 runtime could improve.

At a high level:

- Data collected: The Metrics Collection page provides complete details on how metrics are collected using CloudWatch log trailing, without adding any additional overhead to the tests. Init duration, duration, billed duration, and max memory used metrics for each Lambda invocation are collected and stored in DynamoDB. AWS provides helpful documentation on what these metrics mean on the Understanding the Lambda execution environment lifecycle page.
- Sample size: For each configuration, the benchmark performs 125 cold invocations and 500 warm invocations (625 total invocations per config) across 294 unique test configurations, resulting in 183,750 Lambda invocations per test run. I ran multiple benchmark runs in us-east-2 and saw results that were relatively similar across time of day.
- Cold start tests: Cold starts were triggered by toggling the Lambda's memory configuration, which invalidates all warm instances without requiring redeployment. For this benchmark, I collected 125 cold samples for each configuration. I borrowed this cold start testing technique from AJ Stuyvenberg's blog posts. AJ's approach dramatically speeds up testing by eliminating the need to wait for natural cold starts. The AWS Lambda Power Tuning Tool takes a similar approach when used to benchmark an individual Lambda.
- Warm start tests: For each configuration, 500 warm Lambda invocations were collected for this benchmark.
- Statistics: After collecting raw samples, statistical outliers (min and maxvalues) were removed. Then, from the cleaned data, the mean, median, standard deviation, and P50/P90/P95/P99 percentiles for each configuration were calculated.
## Results Overview

The primary comparisons in this post focus on warm invocations, since that's what most production traffic looks like. Here are some key findings from the data:

- arm64 wins on cost in every scenario
- Rust is dramatically faster than interpreted runtimes
- Python 3.11 is the fastest Python
- Node.js 22 beats Node.js 20
## CPU-Intensive Workload Results

The CPU-intensive workload (500,000 SHA-256 iterations) provides a clean view of raw compute performance without I/O overhead.

### Warm Start Performance

CPU-intensive warm start duration by memory configuration across all runtimes and architectures

Rust completes the same workload in a fraction of the time compared to interpreted runtimes:

Rust is 8x faster than Node.js and nearly twice as fast as Python for this compute-heavy workload.

One surprising finding: x86 Rust outperformed arm64 Rust by 10% at higher memory configurations. This was unexpected given arm64's general performance parity. For most runtimes, arm64 matches or exceeds x86 performance, but Rust on x86 appears to have an edge for pure compute at scale.

### Python Version Comparison

Python version comparison for CPU-intensive warm starts

Python 3.11 consistently outperformed newer versions across all memory configurations. It was 9-15% faster than Python 3.12, 3.13, and 3.14. This surprised me, but matched other Python benchmarks I found online. Python 3.11 had notable performance improvements over previous versions, and subsequent releases have had negligible single-threaded improvements.

### Node.js Version Comparison

Node.js 20 vs 22 comparison for CPU-intensive warm starts

Node.js 22 showed consistent improvements over Node.js 20, with execution times 8-11% faster across memory configurations. Combined with the benefits of the arm64 architecture, upgrading from Node.js 20 on x86 to Node.js 22 on arm64 delivers approximately 18% performance improvement at no additional cost.

### Rust Comparison

Rust performed consistently well regardless of the amount of memory allocated to it. It is a highly efficient runtime for CPU-intensive workloads.

P99 duration by runtime family for CPU-intensive warm starts

Rust vs Node.js 22 comparison for CPU-intensive warm starts

### Cost Analysis

Cost savings (%) when using arm64 vs x86 for CPU-intensive workloads

Arm64 delivered 7-38% cost savings for CPU-intensive workloads across all runtimes. Even when x86 is slightly faster, arm64's 20% lower price per GB-second wins on total cost.

## Memory-Intensive Workload Results

The memory-intensive workload allocates and sorts a 100MB array, stressing both memory bandwidth and CPU.

### Warm Start Performance

Memory-intensive warm start duration by memory configuration

This workload showed interesting patterns:

Arm64's advantage grows with memory allocation in these charts. At the maximum 10GB Lambda configuration, arm64 was 27-28% faster than x86 for Node.js workloads.

Rust again dominates, completing the memory-intensive workload 2.7x faster than Node.js and 13x faster than Python.

Python showed unexpectedly high variability in the memory-intensive workload. Python 3.12 and 3.13 on arm64 were actually slower than x86 at several memory configurations, which is not what we'd expect. I suspect this is related to Python's memory management and garbage collection behavior rather than the underlying architecture or an issue with my benchmark. Python 3.11 showed more consistent advantages on arm64.

Python version comparison for memory-intensive workloads

### Cost Analysis

Cost savings (%) when using arm64 vs x86 for memory-intensive workloads

Arm64 delivered significant cost savings for memory-intensive workloads, up to 42%, at higher memory configurations where arm64's performance advantage is most clear. Node.js and Rust showed the most consistent savings (23-42%), while Python's cost efficiency varied due to the performance anomalies noted above.

## Light Workload Results

The light workload (DynamoDB batch read/write) represents a realistic Lambda scenario in which I/O latency dominates execution time. I'll keep this section brief since the results tell a simple story.

Light workload warm start duration by memory configuration

For I/O-bound workloads, the runtime differences largely disappear. When network latency is the bottleneck, whether you're running Rust or Python matters far less. All runtimes completed the light workload in 15-80ms at 512MB and above. The main takeaway for light workloads: optimize for cost, not raw performance.

## Cold Start Analysis

Cold starts are often a critical concern for Lambda users, especially for latency-sensitive applications.

Here's a breakdown of the init duration by runtime we observed during these benchmarks:

Rust cold starts are 5-8x faster than interpreted runtimes. At 16ms on arm64, Rust initialization is nearly imperceptible. This makes Rust an excellent choice for latency-sensitive applications where cold starts matter.

Arm64 consistently showed 13-24% faster cold start initialization across all runtimes. This is a meaningful improvement that compounds with cold start frequency.

### Cost Efficiency Deep Dive

Cost vs performance scatter plot for CPU-intensive workloads

The cost analysis reveals why arm64 is such a great default:

- arm64 is 20% cheaper per GB-second than x86
- arm64 performance matches or exceeds x86 in most cases
The combined cost and performance efficiency of arm64 make it a strong default architecture for Lambda, unless a library you are using in a Lambda isn't compatible with arm. Even when x86 shows a slight performance edge (like Rust CPU-intensive at high memory), arm64's price advantage typically results in better cost efficiency.

### Performance Consistency (P99 Latency)

For production workloads, tail latency often matters more than averages. A function that's fast on average but spiky at P99 can still blow your latency budgets.

P99 latency scaling for CPU-intensive workloads

The P99 results largely mirror the mean duration patterns. Rust delivered the most consistent performance with P99/mean ratios close to 1.0. Python and Node.js showed slightly more variability (P99 was 5-15% higher than the mean in some configurations), but nothing that would change your runtime selection.

## Conclusions

The verdict is clear: arm64 should be your default targeted CPU architecture for Lambda. After multiple benchmark runs analyzing 183,750 Lambda invocations across 294 configurations, the data consistently points in one direction. Unless you have a specific library compatibility issue, arm64 wins.

### Why ARM64 Wins

The rare exceptions (like Rust being CPU-intensive at high memory usage) don't outweigh these consistent benefits.

### Runtime Selection Guide

You should never rely on generic benchmarks and instead, evaluate Lambdas for your specific workloads. However, if we were to use these generic benchmarks as a guide, this is what they would suggest:

### Writing Benchmarks Is Hard

This benchmark is relatively simple, with only three workloads to test. However, because each workload runs across multiple architectures and runtimes, even a ‘simple’ benchmark can become time-consuming to build, deploy, and collect results. I’m sure this benchmark isn’t perfect, but it still reveals some useful trends. Going through this process also gave me tremendous respect for the people who regularly build and contribute to benchmarking tools.

### Reproduce These Results

The complete benchmark code is available at aws-lambda-performance-benchmarks. Run your own tests, or adapt the workloads to match your production patterns. I'd love to hear how your real-world results compare. Switching to arm64 is the easiest performance win you can get.


