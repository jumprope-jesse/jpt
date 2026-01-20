# AWS QuickSight Embedding

## Overview

QuickSight embedding allows integrating AWS QuickSight dashboards and analytics directly into custom applications. Key for multi-tenant SaaS applications needing embedded BI.

## Key Considerations for Embedded QuickSight

### 1. Dynamic Filters (JS SDK)

- Use the QuickSight Embedding SDK to apply filters programmatically
- Can pass filter parameters at embed time for tenant isolation
- Reliability depends on proper SDK initialization and event handling

### 2. User-Saved Pivot/Dashboard Customizations

- **Bookmarks**: Allow users to save custom pivot layouts and filter states
- Consider whether to persist user preferences in QuickSight or application database
- Embedding API supports bookmark creation and retrieval

### 3. Data Export (CSV/XLSX)

- QuickSight supports native export to CSV and Excel
- Export availability can be controlled per dashboard/visual
- Consider data volume limits and security implications for exports

### 4. SPICE vs Direct Query

For large datasets (100M+ rows, millions added daily):

**SPICE (Super-fast, Parallel, In-memory Calculation Engine)**:
- In-memory caching for fast queries
- Scheduled refresh (hourly, daily, etc.)
- Better for dashboards with heavy usage
- Storage costs scale with data volume
- May not be ideal for rapidly changing data

**Direct Query**:
- Real-time queries against source (Redshift, etc.)
- Always current data
- Query performance depends on source database
- Better for near-real-time requirements
- Can leverage Redshift's query optimization

### 5. Row-Level Security (RLS) at Scale

- Essential for multi-tenant applications
- Can be implemented via:
  - **Dataset RLS rules**: Tag-based rules in QuickSight
  - **Database-level RLS**: Policies in Redshift itself
  - **Parameter-based filtering**: Pass tenant ID at embed time
- For scale, prefer database-level RLS or efficient tagging strategies
- Test performance with representative user counts

## Architecture Pattern: Multi-Tenant Embedded Analytics

```
Application (Java/Angular)
    │
    ├── Authentication → Generate QuickSight Embed URL
    │                    (with tenant context)
    │
    └── Embedded Dashboard
            │
            ├── JS SDK (dynamic filters, events)
            │
            └── QuickSight
                    │
                    ├── SPICE (cached) or Direct Query
                    │
                    └── Redshift (100M+ rows)
                            │
                            └── RLS policies (tenant isolation)
```

## Resources

- [QuickSight Embedding SDK](https://github.com/awslabs/amazon-quicksight-embedding-sdk)
- [Row-Level Security in QuickSight](https://docs.aws.amazon.com/quicksight/latest/user/restrict-access-to-a-data-set-using-row-level-security.html)
- [Reddit Discussion: Embedding Lessons](https://www.reddit.com/r/aws/comments/1lop69o/aws_quicksight_embedding_lessons_on_dynamic/)

## Analysis Authoring Experience (2023 Redesign)

In November 2023, QuickSight launched a redesigned analysis experience for dashboard authoring:

### 3-Pane Layout
- Organized workspace with clear navigation between data, visualization building, and object properties
- Vertically organized field wells with drag-and-drop
- Redesigned visual type selector
- Dedicated Properties pane for object-related settings

### Analysis Toolbar Improvements
- **Add visual**: Smoother process with clear differentiation between visuals and other objects (text, custom content)
- **Change visuals**: Context-aware UI that prevents accidental changes while enabling seamless modification
- **Quick search**: Integrated search (in Analysis menu) to locate features and workflows quickly
- Results refine with each keystroke

### Console Embedding
- New authoring experience available for embedded mode (console embedding) as of December 20, 2023
- Applies to both Standard and Enterprise editions

### Backward Compatibility
- Beta opt-out available until January 31, 2024 via "New Look" toggle
- Can switch back to previous experience temporarily

**Key benefit**: More intuitive, scalable, and efficient authoring workflows for creating dashboards and reports.

---
Source: Reddit r/aws discussion on QuickSight embedding patterns (2025-07)
Source: AWS Blog - QuickSight Analysis Experience Redesign (2023-11)
