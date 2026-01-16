# Review Q1 Product Goals - Summary

**Date**: 2025-12-16 17:01

---

### OE 2.0 Project Clarification

- Brent specified Q1 goals: steps 1-8 for most projects - Step 8 = rapid POC prototypes review/sign-off by stakeholders
  - Not step 9 (actual build/test/release)
- Confusion around prototyping vs UAT expectations - Stakeholders need to sign off on both POC and UAT phases
  - End of January = go/no-go decision for Aries Con
  - February 15th prototype sign-off may be too late
- Key results for OE 2.0: 1. Conduct stakeholder workshops by January 31st
  2. Agree on prototyping sign-off criteria by February 15th
  3. Achieve sign-off for Aries Con prototypes by March 15th
  4. Configure demo environment with infrastructure/plumbing

### Stakeholder Feedback Challenges

- Laura’s team rejected terminology and navigation hierarchy - Want “enrollment process” instead of “managed forms”
  - Requesting longer, enrollment-specific terms vs generic language
- Product team’s concern: building for broader use cases - System designed for re-enrollment, lottery, surveys beyond enrollment
  - Risk of narrow vision limiting future functionality
- Text changes require system-wide updates - Form references carry through multiple pages/documents
  - Conditional display suggested as solution for different contexts
- Market research shows similar terminology (SchoolMint example) - Need to balance innovation with stakeholder comfort

### API V6 Development

- Q1 scope: steps 1-4 only per Brent’s direction
- Key deliverables: - Published product roadmap
  - Draft VRD with ELT approval
  - Cross-divisional collaboration on go-to-market
  - JumpRope pricing/monetization review
- Vendor portal requirement identified as separate project - Cannot tie to API V6 development
  - AWS API Gateway vendor portal announced November (requires research)
  - Entirely separate requirement from API building

### JumpRope SBG Integration

- Timeline: Ready by March, stretch goal February 17th
- Technical requirements waiting on business requirements approval
- Critical dependency: writable endpoint for grade reporting - Need single class academic grade submission at term end
  - Must support resubmission and deletion
  - Fallback: SFTP export if endpoint development unfeasible
- Capacity concerns with Q1 resource availability
- Jesse handling requirements, Jenna as main Aries contact point

### Communications Project Status

- Strategic decisions still being made/deferred
- Justin holds business requirements
- Jesse recommends not investing time in current BRDs
- Parent Square contract complicates direction
- Goal marked as “bright red” vs API integration “green bleeding yellow”

### Action Items

- Ellen: Clarify step 8 expectations with Brent and ELT
- Ellen: Schedule capacity planning meeting with Jesse, Randy, James
- Jesse: Provide BRD links and add Aries requirement IDs
- Ellen: Add Jenna to tomorrow’s all-hands meeting
- Jason: Add team names in slide deck comments for presentation assignments

Chat with meeting transcript: https://notes.granola.ai/t/9316e580-034e-4822-a8e7-e239fc007c79
