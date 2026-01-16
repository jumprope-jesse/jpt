# Product Integration - JR/Aeries - Requirement Review - Summary

**Date**: 2025-12-08 17:01
**Attendees**: Jenna Brown, Jesse Olsen, justin, Alicia Gragnani, Jenna Brown, Jesse Olsen, Justin Meyer

---

### Business Requirements Approval

- Requirements document received positive feedback from Aeries team
- Alicia confirmed they’re on right track, no major changes needed
- Document purposely kept non-technical per guidance
- Need more technical specificity in some areas (data import details, permissions structure)
- Technical requirements will be separate document for different audience

### Estimation & Project Sizing

- Jesse will provide developer day estimates rather than T-shirt sizes - Most requirements expected to be small-medium scope
  - Will double estimates as standard practice for optimistic developers
- Aeries uses sizing system: S/M/L/XL/1X/2X with corresponding day ranges
- Time tracking needed for future project velocity calculations
- Cost calculations will feed into pricing models for maintenance overhead

### Critical Aeries Development Dependencies

- Row 27: Grade passback integration - highest priority and complexity - Ellen already penciled into roadmap for Feb 17 delivery (pre-Aeries Con)
  - Fallback deadline: May 1 for live testing with Tahoe Truckee
  - Without this: manual CSV export/import (embarrassing but functional)
- API key setup automation needed - Currently requires complex 3-page manual process
  - Parent Square appears to have streamlined template - want same treatment
  - Chris Brown identified as key contact for integration patterns

### Single Sign-On Requirements

- Jumpro can handle SSO without Aeries development
- Better UX would include Aeries-to-Jumpro launch button (row 24)
- Need clarity on student/family login workflows and permissions
- Alicia advocates for seamless back-and-forth navigation between systems
- Critical for selling integrated package experience

### Technical Questions for Product Team

- Teacher daily workflow patterns - Do teachers log into Aeries daily or just use Jumpro gradebook?
  - How does attendance/gradebook split affect login needs?
- Student/staff permission structures in Aeries
- Contact strategy: - Ellen for roadmap coordination
  - Chris Brown for integration patterns and API setup
  - Possibly customer experience team for workflow insights
  - Consider asking Tahoe Truckee directly about teacher workflows

### Project Management Structure

- RAID log established for tracking risks, actions, issues, decisions
- Technical requirements will reference business requirement IDs
- One business requirement typically maps to multiple technical requirements
- Will use spreadsheet initially, then migrate to Jira for development tracking
- Integration with Aha planned for Ellen’s progress visibility

### Next Steps

- Jesse: Complete developer day estimates by end of week
- Jesse/Jenna: Begin technical requirements document
- Alicia: Coordinate with Ellen on development team assignment (likely Matt Hoffman)
- Team: Schedule meetings with Chris Brown and Ellen this week
- Alicia: Determine go-to-market plan ownership (Charity vs higher level)
- Target: Technical requirements and dev team assigned by next week

Chat with meeting transcript: https://notes.granola.ai/t/c668b3c4-205d-494a-84b0-09d8feea1b6c
