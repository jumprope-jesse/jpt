# GL Interview : Backend Developer : Raju - Summary

**Date**: 2026-01-09 14:29
**Attendees**: raju.1@globallogic.com, Jesse Olsen, ankur.gupta4@globallogic.com, rashmi.khurana@globallogic.com, jesseo@aeries.com

---

### Raju’s Technical Background

- Python full stack developer with 9.5 years experience
- Specialized in Python, Django, Flask plus front-end work
- Cloud experience: AWS, Azure, GCP
- AI tools: GitHub Copilot, Cursor, Codeium
- Infrastructure: Docker, Kubernetes, DevOps automation
- API integrations: Stripe, PayPal, Google Drive
- GraphQL, React, Next.js, Node.js experience

### JumpRope Technical Architecture Discussion

- Python Django backend running in Docker containers on AWS Lambda - Serverless compute with MySQL Aurora RDS
  - Mono repo approach with same code across different Lambda configurations
  - GraphQL API built with Graphene (99% of traffic)
- Current tech stack: - Python 3, Django 5.2
  - UV instead of pip for package management
  - 40% unit test coverage (needs improvement)
- Production database considerations: - Single multitenant database for all customers
  - Staging environments point to same production database
  - Requires careful debugging practices with production access
  - Raju has similar experience from previous organization

### Working Practices & Collaboration

- Time zone alignment: 11-hour difference (Raju works until 10:30 PM IST) - Morning overlap possible for check-ins
  - Comfortable with asynchronous work via JIRA comments
  - No daily standups required, written updates preferred
- Code review approach: - Two-person team using AI tools for initial review
  - Focus on complex features requiring thoughtful review
  - Jesse wants thought partner for implementation decisions
- Security maintenance: - CVE monitoring through AWS Inspector/OpCenter
  - High-priority vulnerabilities must be resolved within 7 days
  - Raju experienced with package vulnerability management
  - Opportunity to automate OpCenter to JIRA integration

### Project Structure & Workflow

- Single application with 320 database tables
- Multiple Django apps governing different feature sets
- JIRA workflow: - Red: bugs from customers
  - Green: stories with design documents
  - Blue: engineering tasks/maintenance
  - Purple: small enhancements
- Release process: ~2-week cycles, branch-based development
- Development setup requires VPN + SSH tunnel to production database via bastion server

### Next Steps

- Budget approval pending from Jason (expected end of January)
- Ankur keeping Raju available for 3-4 weeks while approvals finalize
- Potential start date: February 1st with tentative approval
- Jesse to send feedback email to stakeholders (excluding Raju)
- Follow-up with Jason next week on budget timeline

Chat with meeting transcript: https://notes.granola.ai/t/d87bd4cb-f06d-4ca9-9e61-343e03020053
