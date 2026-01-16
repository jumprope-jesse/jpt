# Weekly Wrap - Summary

**Date**: 2025-12-05 20:36
**Attendees**: Sara Needleman, Hayley Tanler, Jesse Olsen, Jenna VanLooven, Stacey Gall, becky@jumpro.pe, Justin Meyer, yamaris@jumpro.pe

---

### ;’Benefits Package Discussion

- General sentiment: “kind of bad” - high out-of-pocket costs when using healthcare
- Previous Aetna plan better - $25-50 copays with most services covered
- Individual plans saving some money ($570/month for Jenna), but worse for families
- HSA approach: $1,500 contribution helps offset high deductibles
- Jesse opting out entirely - losing stipend creates significant pay cut
- Stacey got 40-hour offer letter (33% bump from 30 hours)

### Employment Status Updates

- Stacey received offer letter at 40 hours/week, hasn’t signed yet
- Jesse and others haven’t received new offer letters under updated titles/conditions
- General assumption: need offer letters post-transaction but no immediate concern
- Job security perspective: “they need me more than I need them”

### Kids & Personal Updates

- Joseph (Justin’s son) self-initiated potty training - Brought mini toilet from garage, sat down, took off diaper
  - Two-day struggle with bowel movements, finally succeeded
- Alex (Jesse’s son) discovered smuggling ornaments in sleep sack
- Tree decorating with felt ornaments for toddlers

### Product Development - Aha Integration

- Learning new Aha product roadmap tool
- Same functionality as Atlassian Compass
- Public ideas board capability (like UserVoice)
- No expectation to move off Jira currently
- Jason prefers Jira over Azure DevOps
- Ellen wants Aha integration for project visibility and release planning - Monthly release slots planned 6 months ahead
  - February release needs completion by January 26th
  - No flexibility for out-of-band releases

### Time Tracking & Metrics Discussion

- Aries using 7pace time tracking - employees hate it
- Support tickets require time entry per ticket
- Jesse’s approach: use standard units (30/60 minutes) rather than exact tracking
- Jason establishing baselines for capacity planning
- Resistance due to perverse incentives concerns

### System Transitions

- Fresh Desk migration planned - 6-month timeline
- Target: third week of July
- Fresh Desk created by former Zendesk employee - similar functionality
- Zendesk unchanged in 10 years except facelift

### Compensation & Bonus Structure

- Significant bonus reduction under new structure
- Previously 10%+ of salary on average
- New structure: company must hit goals for any bonus payout
- Prorated based on company performance
- Concern: goals will keep rising year-over-year to limit payouts
- EBITDA targets described as “insane” - $100M growth in 3 years

### Communications Product Requirements

- 95 business requirements identified, planning to cut to ~80
- Major areas needing discussion: 1. Permissions system - very granular, similar to Salesforce profiles
  2. Templates for reusable messages
  3. Recurring/scheduled messages (recurring pushed to Phase 2)
  4. Priority/emergency messaging
  5. Reporting capabilities
- Technical approach: leverage Django’s built-in permissions/groups system
- Message reactions considered P3 priority (likely to cut)
- Archive conversations feature removes from both sender/recipient inboxes

### UI & Architecture Decisions

- Building from scratch rather than extending TalkJS
- Message data structure needs complete redesign
- Templates include full message setup, not just content
- Letterhead/signature system: - Clean text message content separate from formatting
  - Header/footer added only for email delivery
  - Signatures don’t appear in threaded conversations
- Attachment handling: secure login-required links
- Student-centric recipient selection with parent inclusion toggles

### Meeting Structure & Leadership

- Too many meetings due to lack of clear decision-making authority
- Committee-style decisions instead of top-down direction
- Cross-functional work inefficiencies
- MSO meetings generally unproductive
- Becky’s new role: Director of Teaching and Learning Innovation

### Next Steps

- Jenna to refine communications requirements document
- Present to ELT in couple weeks after stakeholder reviews
- Get approval from Charity, Ellen, and Alicia
- Create UI mockups
- Show to Brent, Jonathan, and Andrea at next check-in (end of next week)
- Target approval by end of year (may slip to early January due to holidays)

Chat with meeting transcript: https://notes.granola.ai/t/41630157-0a75-46a2-8256-b38c89b0de1d
