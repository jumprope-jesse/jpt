# JumpRope & Aeries Round 2 - Summary

**Date**: 2025-12-18 18:59
**Attendees**: Jenna Brown, Nguyen Tran, Caleb Allen, Sylvia Nishimoto, Randall Catiller, Jesse Olsen, Alicia Gragnani, Jenna Brown, Jenni Allen, Jesse Olsen

---

### Integration Requirements Discussion

- BRD draft ready for ELT approval tomorrow (Justin presenting)
- Technical requirements starting phase with question review
- Focus on premium integration between JumpRope and Aries
- Scope management critical - avoiding feature creep

### Grade Submission Process Details

- GRD table initialization happens near end of term (admin process) - Creates empty records for each enrolled student per section
  - Recommended timing: day before teachers enter grades
  - Point-in-time enrollment snapshot
- JumpRope will only update existing GRD records, not insert new ones
- Validation required for grade codes - API should reject invalid grades to prevent system issues
  - GRC endpoint needed for valid grade mapping (minimal Aries work)
  - Alternative: error reporting via email if validation fails

### Authentication & Security Concerns

- Multi-district email address conflicts possible - Same email can exist across different Aries databases
  - Need error handling for staff working multiple districts
- Admin email modification security risk - Admins can change emails to potentially access other districts
  - Requires careful validation to prevent unauthorized access
- SSO implementation for managed identities - Password login disabled for Aries-managed accounts
  - Session extension complexity flagged as potential red flag

### Scheduling System Variations

- Four Aries scheduling types identified: 1. Flex - newest, supports daily schedule variations (Covid-era)
  2. Secondary - master schedule with courses/sections
  3. Elementary with Master - similar to secondary, daily attendance
  4. Elementary without Master - direct teacher-student mapping via CU field
- Current JumpRope integration only supports Flex
- TSA table option available but requires new Aries endpoint
- Elementary without Master usage appears minimal
- May defer non-Flex support until customer demand emerges

Chat with meeting transcript: https://notes.granola.ai/t/3ce51194-eae0-47a8-b38a-e3ddb1e89a20
