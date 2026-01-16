# Attendance notifications - Summary

**Date**: 2025-12-12 16:47

---

### Attendance Notifications Project Impact

- Customer expects simple email/SMS delivery without full data import - Likely assumes JumpRope can fire notifications to email without backend complexity
  - Reality: need family context, notification preferences, student data stored
  - Parent Square model: parents choose notification method (email/SMS/push)
- Technical requirements force complete data import - Need 10x current nightly import volume
  - All student/family data required for proper notification delivery
  - Talk.js involvement currently required but could be modified for notifications-only
- Infrastructure costs unknown for this scale - Most imported users won’t log in regularly
  - Need to test performance before committing
- Two key questions to ask customer: 1. What specific API content/format expected?
  2. Student count across their customer base?

### Roadmap and Integration Pivot

- Complete departure from current development timeline - Attendance notifications moved up from next year’s roadmap
  - May be different from “attendance intervention” mentioned previously
- Product integration project proceeding - 60-65 day estimate (conservative, likely faster given existing progress)
  - 50+ questions identified for Aries team
  - Dependencies on Aries systems documented
  - Confident in 99% of business requirements
- Global implementation potential attractive - Could position JumpRope as existing infrastructure for future customers
  - “You’re already using JumpRope for notifications, want to try the gradebook?”

### Team and Personal Updates

- Maris concerns - Multiple recent sick days coinciding with delayed offer letter
  - New role: renewals manager with variable compensation
  - Potential anxiety about sales function placement vs. relationship management
  - Jesse planning dinner invitation for support/check-in
- Abner opportunity - Aries hiring NYC-based account manager
  - $115-135k base plus commission, 50-75% NYC travel
  - Considering recommending him despite his Oregon move plans

Chat with meeting transcript: https://notes.granola.ai/t/2a7f0263-b76d-43bc-b941-95b663ca7370
