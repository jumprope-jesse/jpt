# Product Meeting - Summary

**Date**: 2025-09-10 17:00
**Attendees**: Jenna Brown, Hayley Tanler, Justin Meyer, becky@jumpro.pe, Jesse Olsen, yamaris@jumpro.pe

---

### Team Meeting Format & Acquisition Context

- No cameras policy continues - judged for what we say, not how we look
- Aries acquisition context discussed - Jonathan and Brent (executives) want to join Weekly Wrap Friday
- Show up cameras off, be ourselves as gesture of their egalitarian approach

### IT Migration to Microsoft/Aries Systems

- Moving to Microsoft Teams by end of October - replaces Slack for chat and meetings
- Email migration from Google to Microsoft server - Jump rope email addresses likely stay same, just different hosting
  - Aries prefers not migrating old email data due to retention policies
  - Options: migrate last 6-12 months or clean slate approach
  - Team generally comfortable with clean slate/minimal migration
- Google SSO elimination requires comprehensive audit - Ward and Zendesk confirmed as only SSO-only systems
  - Others (Atlassian, ChatGPT) can use direct login via password reset
- Google Drive moving to SharePoint/OneDrive
- Work email access only through company devices, not personal phones
- VPN changes coming - current Nord setup will be replaced

### Customer Communication Strategy

- Public announcement timing: likely early October after Jennifer meeting
- Personal outreach before public announcement - Template being developed for key customer relationships
  - Geographic considerations for Aries partnership messaging
  - NYC customers less sensitive, others may need reassurance about continued service
  - Coordinate to avoid multiple team members contacting same customers
- Messaging focuses on Aries investment enabling better Jump rope service

### Technical Issues & Bug Fixes

- Jasper costs doubled in August - notified up chain of command
- Server upgraded to newer Jasper version (looks same, some minor config tweaks needed)
- Term dates bug: can create assessments without term dates set - Will fix to require term dates before assessment creation
  - Jenna handling cleanup of schools missing proper term dates
- Clever import supporting multiple schools - Mary Lyon splitting into elementary/high school sites
  - Using copy settings approach rather than code changes
  - User provisioning across schools needs development work (lower priority)

### Messaging System Opt-in Analysis

- Higher opt-in than opt-out rates - validates better user engagement
- 20% of users replying with thumbs-up emoji instead of “start” - Creates expensive failed message loops
  - System doesn’t recognize emoji responses
  - Will add auto-response for unrecognized replies: instructions to use “start/stop”
- Current accepted keywords: yes, start, subscribe, restart, unpause, plus Spanish versions
- Teachers can see SMS status in family contacts/outreach views using color codes

### VPN Access Requirements

- Current VPN-required systems: - Django admin
  - Zendesk Ninja buttons
  - Super password on non-JRSB sites
  - DevOps machine access
- Salesforce restricted to Justin and Jesse only
- Zendesk not VPN-gated (only Ninja links are)

### Customer Training & Support Notes

- Taft training Monday - Windows laptop screen size issues resolved with browser zoom
- Computer literacy gaps continue - basic zoom/browser functions not widely known
- Opt-in messaging requires FAQ updates with screenshots showing admin status views

### Action Items

- Jenna: Project manage IT migration, communicate with team on changes
- Jesse: Share SSO audit spreadsheet with Aries today, fix term dates assessment bug
- Yamaris: Draft customer announcement email for review, update messaging FAQ
- Hayley: Set up Mary Lyon as two separate schools using copy settings
- Justin: Coordinate with Jennifer on customer communication strategy and timing

Chat with meeting transcript: https://notes.granola.ai/d/23e295b6-ebbd-48d5-8e57-b8d48fbe47cf
