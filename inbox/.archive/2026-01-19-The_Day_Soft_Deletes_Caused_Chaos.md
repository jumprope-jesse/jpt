---
type: link
source: notion
url: https://blog.bemi.io/soft-deleting-chaos/
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-03-13T03:13:00.000Z
---

# The Day Soft Deletes Caused Chaos

## AI Summary (from Notion)
- Topic: The chaos caused by soft deletes in software engineering.
- Key Lesson: Soft deletes should not be used in production-grade systems.
- Incident Overview: A pull request that removed soft deletion logic led to multiple sales of the same concert seats due to data being incorrectly restored.
- Soft Deletion Defined: Storing deleted data by setting a deleted flag instead of physically deleting it, which complicates data management.
- Critical Incident: A background worker mistakenly processed "deleted" records, resulting in double bookings for concert tickets.
- Consequences: Hundreds of refunds, canceled orders, and customer apologies were necessary due to the incident.
- Complexity Issues: Soft deletes complicate queries and can lead to unintentional data exposure.
- Data Integrity Risks: Managing soft deletes adds maintenance overhead and can lead to errors in data relationships.
- Recommended Alternatives: Archiving deleted data into history tables or creating an audit trail to maintain data integrity.
- Final Takeaway: Avoid soft deletes as they introduce significant risks and complexities; opt for archiving instead for safer data management.

## Content (from Notion)

The worst mistake I made in my software engineering career was merging a seemingly harmless pull request 5 years ago.

TLDR: Soft deletes should not be used in production-grade systems—a lesson I learned the hard way when a severe mishap enabled the sale of the same concert seats to unlimited buyers.

Soft deletion is the easiest way to store deleted data and means just setting a deleted flag instead of performing a DELETE operation directly.

Deleted user using soft deletion

You add a new column on a table, perform an update when deleting, and filter out deleted data when querying.

Querying with soft deletion

Although this approach is simple to set up, it can lead to dangerous consequences if it accidentally returns data not meant to be seen.

## Critical Incident

I was working at an events ticketing company and I created a pull request that was similar to this:

app/models/seat_claim.rb

migrations/19700101000000_migrate_deleted_seat_claims.rb

In the seating reservation experience, you could claim a seat for 5 minutes during the checkout flow before a background job would delete the claim and release the seat to be bookable again. I was migrating from soft deleting seat claim’s to a new collection explicitly meant for storing the deleted rows.

Seating Reservation UX

The incident was caused because of this line:

```plain text
- acts_as_paranoid

```

This removed the Paranoia library on the model that had abstracted away the soft deletion logic i.e. setting a deleted_at field to the current time when you delete a record. What wasn't top of mind for me was that it also automatically filtered out all soft-deleted records in the ORM.

Without the automatic exclusion of soft-deleted records and while the migration hadn't finished, the background worker began collecting claims that had already been "deleted" - inadvertently causing seats that were successfully paid for to be released and available for booking again!

I’ll never forget the sinking feeling and sense of dread when I realized what was happening.

This meant that the same seat at a Shawn Mendes concert was being sold multiple times over. Amplified by lots of seats, amplified by lots of events around the globe! Yeah it was bad.

Luckily there was a lot of observability in this area, so it was detected and remediated almost immediately. But the impact and fallout was still severe with hundreds of double bookings that had to refunded, orders cancelled, apology emails sent to affected customers, and a late night postmortem written.

## Don’t Soft Delete

The instinct to keep deleted data is understandable. Developers often want a safety net – a chance to recover from accidental deletions or to examine a deleted record for troubleshooting. Imagine a customer accidentally deleting a crucial invoice, or a social media user deleting a comment that broke the rules. Keeping deleted data for a grace period can be valuable. However, the soft deletes approach creates more problems than it solves.

### Complexity

Soft deletion infects everything and complicates queries. The application ORM layer usually automatically filters out "deleted" records, but this convenience can lead to oversight when constructing complex SQL queries manually. Like me, you might end up retrieving inaccurate results, potentially exposing sensitive data or making bad decisions based on incomplete information. Yes, creating a database View is safer, but it’s still extra complexity and an unneeded appendage.

Murphy's Law: anything that can go wrong will go wrong

Indexes, unique constraints, and foreign key relationships all also need to consider the "deleted" state, making them more intricate to create and maintain.

Creating a unique index on the email field for active users

Even with adding partial indexes, soft deletes can lead to significant bloat, adversely affecting table size and performance. In high-volume environments, this can become a bigger issue and require performance tuning or data partitioning to maintain efficiency.

### Data Integrity

Handling deletion in the application layer via soft deletes loses one of the benefits of the database, which tries to keep data valid for you.

Database foreign key violation error

Enforcing referential integrity on your own can be error prone and adds significant development and maintenance overhead.

## Alternatives to Soft Deletes

The best alternative to soft deletes is to just archive the deleted data into history tables. It's still simple to do and removes the long term liability and maintenance burden of soft deletes. This can be done by inserting the deleted record to a separate table before deleting.

Transaction to archive data before deleting

If you don't want to manually archive data all over your codebase, you can build an audit trail at the database layer.

For PostgreSQL, there are a few different strategies to implement this described in our Ultimate Guide to PostgreSQL Data Change Tracking. This can also be automated by services like bemi.io, which plugs into a database and provides immutable records of data changes automatically.

## The Bottom Line

Steer clear of soft deletes. They might look like the easy fix for managing deleted data, but trust me—they're a ticking time bomb. I learned this the hard way years ago, and it's a mistake you don't want to repeat. Opt for history or audit tables instead. It's cleaner, safer, and will save you a world of trouble down the line.


