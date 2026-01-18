# AWS SES Email Validation

Amazon SES now offers email validation to reduce bounce rates and protect sender reputation.

## Key Features

- **API Validation**: Validate individual email addresses via API calls
- **Auto-Validation**: Automatically validate all outbound emails without code changes
- **Configuration Levels**: Can be enabled at account level or configuration set level via AWS console

## Validation Insights

The API provides detailed validation data:
- Syntax checks
- DNS record verification
- Invalid address identification

## Benefits

- Maintain list hygiene
- Reduce bounces
- Improve delivery rates
- Protect sender reputation

## Availability

Available in all AWS Regions where Amazon SES operates.

## Documentation

- [Email Validation in Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/email-validation.html)
- [Amazon SES Console](https://console.aws.amazon.com/ses/)

## Relevance

Potentially useful for the JumpRope Communications/messaging product - email deliverability is critical for school communications. Auto-validation could streamline email hygiene without requiring development work.

---
*Source: AWS What's New announcement, December 2025*
