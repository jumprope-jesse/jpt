# Aries grade reporting cycle integration planning with JumpRope

**Date**: 2026-01-08 19:10
**Participants**: title, created_at, creator, attendees, sharing_link_visibility, conferencing, url

## Notes

GRP stores marking period => M1 - M12

GRP has read endpoint, indicates current

LOC = School

[GRD.SH](http://GRD.SH) indicates which is initialized, but we should be able to use course number to determine which is the right row to write to.

We write to M1-M12, and maybe C1-C3

[LOC.tm](http://LOC.tm) = current mark that is initialized

COD table lists valid codes for C1-C3, has READ endpoint

GRD.UUN = username of person who submitted it (ADMIN)

[GRD.TG](http://GRD.TG) = status, but that will be CALCULATED BY AERIES

GRD.WH = work habits = different set of valid marks, where COD.FC='WH'

[GRD.CI](http://GRD.CI) = citizenship score, valid marks = COD.FC = 'CI'

for students, in GRD, the student identifier is the "student number" — student number will be DIFFERENT for a single student for each school they're enrolled in. PERM ID stays the same but it is not what is submitted

Schools should leave Require Comment? etc. in Portal options un-checked, to make those fields optional so it doesn't break

GRD.TG

GRD has fields that determine which rows are initialized, and we would want to 

Admin can post data any time

See "Multiple Mark Headings and Descriptions"
