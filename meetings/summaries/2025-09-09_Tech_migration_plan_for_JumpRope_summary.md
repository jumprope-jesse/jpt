# Tech migration plan for JumpRope - Summary

**Date**: 2025-09-09 18:59
**Attendees**: Jesse Olsen, James Mallory, Jeremy Wiles

---

### Tech Migration Plan Overview

- JumpRope domain migration to Aeries Microsoft 365 tenant - Minimize disruption during busy season
  - Phase 1: Google Workspace → Microsoft 365 (Teams, email, Drive)
  - Phase 2: Q1 2026 tech stack migration to Aeries systems
- Unipoint LLC handling IT services migration - 25-year IT partner with Aeries
  - Will provide turnkey service desk via Teams
  - Jeremy Wiles (CEO) leading technical implementation

### Current JumpRope Tech Stack

- Email/collaboration: Google Workspace, Slack (minimal usage)
- Customer tools: Zendesk support, Olivio help center
- Business systems: Salesforce CRM/accounting, Atlassian (Jira active, Confluence dormant)
- Development: AWS infrastructure, various dev tools
- Authentication: Google SSO for multiple services including Zendesk
- Security: NordVPN + AWS VPN for sensitive access (Salesforce)
- File organization: Recently moved to Google Shared Drives (8 months ago)

### Implementation Approach

- Create dedicated JumpRope team in Microsoft Teams initially - Allows adjustment to new tools without disrupting workflows
  - Gradual integration with broader Aeries teams later
- Domain migration timeline: 2-3 weeks once plan finalized
- Email migration: Minimal/no historical data transfer preferred - Current policy forwards customer emails to Zendesk
  - 15 years of email history may be left behind
- Training materials: Aeries internal migration resources to be shared

### Next Steps

- Jesse: Compile complete SaaS application inventory with Google SSO dependencies
- Jesse: Create Google admin account for support@unipoint.com (initially user-level)
- Jeremy: Send IT takeover discovery document
- Jeremy: Build detailed migration plan for group review
- Schedule follow-up once plan complete for final approval

Chat with meeting transcript: https://notes.granola.ai/d/4b1d8468-8407-424f-9278-1f024aca8c1f
