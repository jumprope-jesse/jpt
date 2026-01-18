# AWS Lambda SnapStart

## Overview
AWS Lambda SnapStart provides sub-second cold start performance for Lambda functions. It works by taking a snapshot of the initialized execution environment and caching it, so subsequent invocations can restore from the snapshot instead of initializing from scratch.

## Key Benefits
- **Sub-second startup**: Dramatically reduces cold start latency
- **Better user experience**: Critical for customer-facing applications
- **Cost efficiency**: Faster starts mean less billable compute time during initialization

## Zappa Support
As of December 2025, Zappa has a PR (#1367) adding SnapStart support:
- PR: https://github.com/zappa/Zappa/pull/1367
- Adds `snap_start` configuration attribute
- Updates `create_lambda_function` and `update_lambda_configuration` methods
- New test coverage for SnapStart functionality

### Configuration
In `zappa_settings.json`:
```json
{
    "production": {
        "snap_start": true
    }
}
```

## Considerations
- SnapStart works best with Java and Python runtimes
- Some initialization code may need adjustment (e.g., establishing database connections)
- Not all Lambda configurations support SnapStart
- Consider testing thoroughly before production deployment

## References
- [AWS SnapStart Documentation](https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html)
- [Zappa PR #1367](https://github.com/zappa/Zappa/pull/1367)
