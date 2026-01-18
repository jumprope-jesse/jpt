# AWS Lambda ARM64 vs x86_64 Performance Benchmarks (Late 2025)

## Key Takeaways

**ARM64 should be your default Lambda architecture** unless you have specific library compatibility issues.

### Performance Summary
- **ARM64 wins on cost** in every scenario (20% cheaper per GB-second)
- **Rust on ARM64** is the most performant and cost-efficient combination overall
- ARM64 delivers 30-40% lower compute costs with equal or better performance than x86_64

### Cold Start Performance
- ARM64 consistently shows 13-24% faster cold start initialization across all runtimes
- Rust cold starts are 5-8x faster than interpreted runtimes (16ms on ARM64)
- Makes Rust excellent for latency-sensitive applications

### Runtime Recommendations

| Workload Type | Best Choice | Notes |
|---------------|-------------|-------|
| CPU-intensive | Rust on ARM64 | 8x faster than Node.js, ~2x faster than Python |
| Memory-intensive | Rust on ARM64 | 2.7x faster than Node.js, 13x faster than Python |
| I/O-bound (light) | Any runtime, ARM64 | Optimize for cost, not raw performance |
| General Python | Python 3.11 on ARM64 | Surprisingly faster than 3.12/3.13/3.14 |
| General Node.js | Node.js 22 on ARM64 | 8-11% faster than Node.js 20 |

### Surprising Findings
- **Python 3.11 outperforms newer Python versions** (9-15% faster than 3.12, 3.13, 3.14)
- **x86 Rust slightly outperforms ARM64 Rust** for pure compute at high memory configs (by ~10%) - but ARM64's price advantage still wins on total cost
- **Node.js 20 x86 to Node.js 22 ARM64** gives ~18% free performance improvement

### Cost Savings
- CPU-intensive workloads: 7-38% savings with ARM64
- Memory-intensive workloads: up to 42% savings at higher memory configurations
- Even when x86 is slightly faster, ARM64's 20% lower price typically results in better cost efficiency

## Benchmark Methodology
- 183,750 Lambda invocations across 294 configurations
- 7 runtimes x 2 architectures x 3 workloads (CPU, memory, light/I/O)
- 125 cold starts + 500 warm invocations per configuration
- Memory configs: 128MB to 10GB
- Region: us-east-2 (Ohio)

### Workloads Tested
1. **Light (I/O)**: DynamoDB batch write/read (5 items) - realistic Lambda scenario
2. **CPU-intensive**: 500,000 SHA-256 hash iterations
3. **Memory-intensive**: Allocate and sort 100MB array

## Resources
- Full benchmark code: [aws-lambda-performance-benchmarks](https://github.com/chrisebert/aws-lambda-performance-benchmarks)
- Source article: https://chrisebert.net/comparing-aws-lambda-arm64-vs-x86_64-performance-across-multiple-runtimes-in-late-2025/

## Related
- See also: `aws-lambda-snapstart.md` for cold start optimization via snapshots
