# Amazon Q Developer IDE Customization

Amazon Q Developer can be customized with private code repositories to generate organization-specific code recommendations in IDE editors and chat.

## What It Does

- **Inline code completion**: Suggests code based on your organization's internal libraries, APIs, packages, classes, and methods
- **Chat customization** (preview): Ask questions about your organization's codebase in natural language
- Uses RAG (Retrieval Augmented Generation) to understand internal code patterns

## Example Use Cases

**Code Generation:**
- Developer writes `computePortfolioValue(customerId: String)`
- Q suggests implementation based on patterns from private repos

**Chat Queries:**
- "How do I connect to the database to retrieve customerId for a specific customer?"
- Q responds with relevant internal functions and connection methods

## Setup

### Data Sources
- Git repositories (GitHub, GitLab, BitBucket)
- Amazon S3 bucket

### Updating Customizations
1. Navigate to Amazon Q console > Customizations
2. Select customization > Actions > Create new version
3. Choose source code repository
4. Compare evaluation scores between versions before activating
5. Can revert to previous versions at any time

Administrators can schedule regular updates based on latest commits.

## Supported Languages

Currently supports customization for:
- Java
- JavaScript
- TypeScript
- Python

Other Q-supported languages (C#, Go, Rust, PHP, Ruby, Kotlin, C, C++, Shell, SQL, Scala) are not used for customization.

## Privacy & Security

- Code stays private to your organization
- Not used to train foundation model
- Inference endpoint is private per organization
- Per-customization access control for developers

## Monitoring

- Dashboard tracks: Daily active users, Lines of code generated, Security scans
- CloudWatch metrics: Block Accept Rate, Line Accept Rate (by language)
- Evaluate customization effectiveness over time

## Pricing

- Included in Amazon Q Developer Professional subscription (no extra charge)
- Up to 8 customizations per AWS account
- Up to 2 active customizations at a time

## IDE Support

- JetBrains
- Visual Studio Code
- Visual Studio (preview)

## References

- [AWS Blog: Customize Amazon Q Developer with your private code base (July 2024)](https://aws.amazon.com/blogs/aws/customize-amazon-q-developer-in-your-ide-with-your-private-code-base/)
- [Technical deep dive on RAG approach](https://aws.amazon.com/blogs/aws/) (linked from announcement)
