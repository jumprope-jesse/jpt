# Product integration tech questions - Summary

**Date**: 2025-12-15 17:30

---

### Team introductions

- Jesse: Writes all code at JumpRope, based in NYC (snowy, 20°F)
- Jenna: JumpRope product owner starting Jan 1st, worked with Jesse 15 years
- Caleb Allen: Senior dev at Aries, 4 years tenure, lead of Strategic Team 2
- Wynn: Lead developer at Aries, 16 years experience
- Jenny Allen: Business analyst at Aries Strategic Team 1, 3+ years
- Sylvia: Tester at Aries, 12 years + 13 years prior school district experience

### Project overview and business requirements

- JumpRope acquired by Aries, selling as add-on for standards-based grading
- Target customers: Districts wanting JumpRope’s configurable standards-based reporting while keeping Aries for attendance/other functions
- Timeline: Need completion for spring/summer sales, customer onboarding over summer
- Integration approach: JumpRope doing majority of work using existing V5 API endpoints
- Scope limitations: Not integrating daily assignment-level data, only end-of-term grades

### SAML SSO implementation options

- IDP-initiated flow (Aries-initiated) - Low-hanging fruit, minimal development needed
  - Creates automatic navigation entry based on permissions
  - Security concerns: replay attacks, man-in-the-middle vulnerabilities
- SP-initiated flow (JumpRope-initiated) - Preferred security paradigm
  - Requires radio button selection (admin/teacher vs student/parent)
  - Potential UX improvement: craft redirect URL to skip radio button
- Admin SSO requires code changes (currently only Parents Square has admin access)
- Email verification concern: Aries admins can change emails without confirmation

### User provisioning and permissions mapping

- Staff vs Teachers distinction - Staff = actual people, Teachers = logical class assignments
  - Staff is superset of teachers, use staff endpoint for provisioning
  - Legacy scenarios may have teachers without staff accounts
- Permission flags available: is_teacher, is_administrator, is_counselor, is_parent, is_student - Reliability uncertain - may be optional customer configuration
  - Users can have multiple flags (e.g., administrator + teacher)
- JumpRope permissions simpler: admin access (see all students) vs teacher access (only assigned students)

### Student-teacher associations and access control

- Counselor relationships: student.counselor field gives counselors access to specific students - Could map to JumpRope’s advisor functionality
- TSA (Teacher Student Association) table exists but not exposed via current API - Automatically maintained, very dynamic
  - May need new API endpoint if granular access control required
- Current plan: Use class enrollments, manual teacher-student associations for edge cases

### Data integration specifics

- Student photos: Adding to existing student import
- Family contacts: New provisioning from Aries API
- Marking periods/terms: Import dates to reduce manual maintenance
- Grade writeback: Major development item requiring new Aries API endpoint - Push final course grades back to Aries for transcripts/permanent records
  - Not standards-level data, just overall academic + non-academic grades
- Teacher aid classes: Abundant in sandbox data, may need filtering logic

### Next steps

- Team will review technical questions document asynchronously by Thursday - Add responses/confirmations in “human answer” column
  - Include initials for attribution
- Follow-up meeting scheduled Thursday/Friday to review responses
- Jesse targeting development start in early January (~1 month of work)
- Shared customers available for early testing feedback

Chat with meeting transcript: https://notes.granola.ai/t/6235ba76-a863-435c-9707-094f994e7330
