# JumpRope Aeries SIS Integration - Summary

**Date**: 2025-12-12 17:30
**Attendees**: Jenna Brown, Randall Catiller, Jesse Olsen, Alicia Gragnani, Jason Strong, Jenna Brown, Jesse Olsen, Charity Dodd, Chris Brown

---

### Integration Technical Questions

- 50+ questions compiled for Aeries development team
- Need answers before holiday break (by Dec 17, 5pm) to maintain project momentum
- Questions organized into categories: 1. Common workflows for Aeries customers
  2. Permission/enrollment mapping
  3. Student access for non-teaching staff
  4. Family contacts and privacy restrictions
  5. SAML authentication (separate discussion with Caleb scheduled Monday)
  6. Grade writeback and general API questions
- Async approach: Caleb and Win to review and provide answers - Randy to coordinate direct connection with Jesse/Jenna
  - Artifacts to live in team channel for visibility

### User Workflows and SSO Integration

- Confirmed: Teachers will still log into Aeries daily (attendance, student lookup)
- Development needed on Aeries side: - Link in sidebar or gradebook section to launch JumpRope via SSO
  - Configuration flag to identify JumpRope-enabled users
  - Seamless browser tab experience (same account, no separate password)
- Student/parent SSO less clear - existing SAML with ClassLink may be extensible
- Goal: Minimize friction, make JumpRope feel integrated with Aeries

### Staff Access and Permissions

- Use /staff endpoint (superset) rather than /teachers endpoint
- All staff members get JumpRope accounts for admin functions
- Two permission models for student access: 1. Teachers: Students from their assigned classes only
  2. Other staff: Either all students at school OR students from classes they’re assigned to
- Aeries has “can view all students” permission flag that can determine access level
- Counselor access: Typically assigned by last name ranges, but inconsistent across districts

### API Technical Details

- Rate limiting: Currently none (“we rate limit at the server side” = server crashes) - Should implement but not scope creep for this project
  - JumpRope makes ~6 API calls per customer daily (low impact)
- Staff vs Teachers endpoints: Staff is superset, more consistent
- Certificate provisioning process needs clarification
- Student photos: Nice-to-have feature, may skip if time-constrained

### Project Process and Timeline

- Using this integration to develop templates for future acquisitions
- 40-day development estimate accepted (starting mid-February)
- BRD format being refined - acceptance criteria included for AI test case generation
- Technical requirements will reference business requirements
- Project plan loaded with realistic dates targeting May 1 delivery

### Next Steps

- Randy: Connect Caleb/Win directly with Jesse/Jenna for question review
- Jesse: Convert question list to spreadsheet format (or Alicia will handle)
- Caleb meeting Monday for SAML discussion
- Team to review answers in channel for scope/experience feedback
- Continue development during holiday break when questions answered

Chat with meeting transcript: https://notes.granola.ai/t/c2bdba83-6d2b-4c6c-bee5-3ee281d93f20
