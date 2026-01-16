# Aries grade reporting cycle integration planning with JumpRope - Summary

**Date**: 2026-01-08 19:10

---

### Grade Reporting Data Structure

- GRD table stores grades with M1-M12 fields for different marking periods - GRP table stores marking period definitions → maps to M1-M12
  - GRP has read endpoint that indicates current marking period
  - LOC table contains school information
  - LOC.tm field shows current mark that is initialized (https://loc.tm)
- Grade initialization creates records for all enrolled students - Inserts course, sheet number, and line number
  - Sheet/line number >0 indicates currently initialized course
  - Only update grades for initialized courses (sheet/line >0)

### API Implementation Requirements

- Update endpoint needed for GRD table with specific writable fields: - M1-M12: grade marks (validate against GRC table for valid values)
  - C1-C3: comment codes (validate against COD table where FC matches field)
  - WH: work habits (different valid marks where COD.FC=‘WH’)
  - CI: citizenship score (valid marks where COD.FC=‘CI’)
- Read-only fields calculated by Aeries: - GRD.TG: completion status (https://grd.tg)
  - GRD.UUN: username of submitter (auto-populated by system)
- Student identification uses school + student number (not perm ID) - Student number differs per school for same student
  - Perm ID stays constant but not used in GRD table

### Validation and Configuration

- Schools must uncheck “Require Comment” in Portal options - Makes comment fields optional to prevent API failures
  - Admin can post data anytime; teachers have date ranges
- COD table has read endpoint for valid comment codes - Structure: table name + field name lists all valid codes
  - Soft deletes filtered out in API responses
- JumpRope will handle marking period mapping - Fetch current periods via GRP endpoint
  - Present admin with choice or auto-determine M field
  - Support corrections/resubmissions to same period

### Development Estimate and Next Steps

- Aeries team estimates 4-5 days for GRD update endpoint + validation
- JumpRope starting development next week with Aeries sandbox
- Logging automatically captures all API updates
- Support will use JumpRope logs to identify who entered grades originally
- Work habits integration planned as fast follow after initial launch

Chat with meeting transcript: https://notes.granola.ai/t/365fa9b7-94a1-43ac-bdd0-c19877aa08f8
