---
type: link
source: notion
url: https://www.npmjs.com/package/@joseairosa/recall
notion_type: Software Repo
tags: ['Running']
created: 2025-10-09T03:45:00.000Z
---

# @joseairosa/recall - npm

## Overview (from Notion)
- Enhanced Productivity: Utilize this tool to efficiently recall important coding practices and project specifics, saving time and preventing repetitive explanations.
- Family Engagement: Store memories related to family activities or personal projects, ensuring you can easily reference them in future conversations with your kids or spouse.
- Organizational Knowledge: Leverage collective team memories to maintain continuity in your startup, especially beneficial as your team grows or changes.
- Data Security Awareness: The emphasis on securing sensitive data resonates with the importance of protecting your family’s privacy and business information.
- Learning Curve: The need for proper Redis management reflects the learning journey of balancing work with personal life, highlighting the importance of continuous education.
- Community Building: This tool fosters collaboration among team members, which can parallel your role in nurturing a supportive environment at home or in your community.
- Future-Proofing: Consider how integrating such technology can keep you ahead in the tech landscape, ensuring your skills remain relevant in a competitive market.
- Work-Life Balance: The potential to streamline and automate memory storage could free up mental space, allowing you to focus more on family and personal interests.

## AI Summary (from Notion)
Recall enhances AI assistants by enabling them to remember important context and decisions across conversations, utilizing Redis for memory storage. Users must ensure Redis security, manage access, and comply with data regulations. The tool supports various memory types, allows for global and workspace-specific memory management, and offers features for memory retrieval, categorization, and analytics. Best practices include using secure Redis instances, enabling encryption, and regularly auditing stored memories.

## Content (from Notion)

Give Claude perfect recall with persistent memory that survives context limits and session restarts.

Your AI assistant can now remember important context, decisions, and patterns across all conversations—no more repeating yourself or losing critical information when the context window fills up.

IMPORTANT: READ BEFORE USE

Recall stores conversation memories in Redis, which may contain sensitive information including:

- Code snippets, API keys, credentials, and secrets discussed in conversations
- Business logic, architecture decisions, and proprietary information
- Personal data, team member names, and organizational details
- Any other context shared with Claude during conversations
You are responsible for:

1. Redis Security: Ensure your Redis instance is properly secured with authentication, TLS encryption, and network access controls
1. Data Ownership: Only use Redis servers that YOU control or have explicit permission to use
1. Access Control: Understand who has access to your Redis instance and stored memories
1. Sensitive Data: Never store memories on shared/public Redis instances if they contain sensitive information
1. Compliance: Ensure your use complies with your organization's data policies and relevant regulations (GDPR, CCPA, etc.)
Disclaimer of Liability:

THIS SOFTWARE IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND. THE AUTHOR (JOSÉ AIROSA) IS NOT LIABLE FOR:

- Data breaches, leaks, or unauthorized access to stored memories
- Loss of data or corrupted memories
- Compliance violations or regulatory issues
- Any damages arising from the use or misuse of this software
By using Recall, you acknowledge that you understand these risks and accept full responsibility for:

- Securing your Redis infrastructure
- Managing access to stored memories
- Protecting sensitive information
- Compliance with applicable laws and regulations
Best Practices:

- Use dedicated Redis instances with strong authentication
- Enable TLS/SSL encryption (rediss://) for remote connections
- Regularly audit stored memories for sensitive data
- Implement Redis access controls and firewall rules
- Use separate Redis databases for different security contexts
- Consider data retention policies and periodic cleanup
- Never share Redis credentials or connection strings publicly
See the Security Considerations section below for detailed guidance.

Recall is a brain extension for Claude that stores memories in Redis. It solves the context window problem by:

- 📝 Remembering directives, decisions, code patterns, and important information
- 🔍 Retrieving relevant context automatically when you need it
- 🔄 Persisting across sessions - memories survive restarts and context compaction
- 🗂️ Organizing by workspace - Project A memories don't pollute Project B
- Redis running locally (default: localhost:6379)
- Node.js 18 or higher
- Claude Code or Claude Desktop
Option 1: Local Redis (Recommended for getting started)

Option 2: Cloud Redis (No local install needed)

Use a free Redis cloud service:

- Upstash - Free tier with 10,000 commands/day
- Redis Cloud - Free 30MB database
- Railway - Free Redis with credit
Then use the provided connection URL in your config:

Option A: Using Claude CLI (Recommended)

Or use the MCP command directly in your Claude configuration (no installation needed):

Option B: Global installation

Option C: From source

Add to your Claude configuration file:

Claude Code (~/.config/Code/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json):

Claude Desktop (~/Library/Application Support/Claude/claude_desktop_config.json on macOS):

Restart Claude Code or Claude Desktop to load the MCP server.

Ask Claude:

```plain text
"Store a memory that I prefer using TypeScript for all new projects"

```

Then in a new conversation:

```plain text
"What do you know about my coding preferences?"

```

✨ It remembers!

If you use npx -y @joseairosa/recall in your config, you automatically get the latest version on every Claude restart. No action needed! 🎉

If using global installation:

If using from source:

After updating:

1. Restart Claude Code or Claude Desktop
1. Verify new version: Ask Claude "What Recall version are you using?"
1. Check CHANGELOG.md for new features and breaking changes
Upgrading to v1.3.0:

- No breaking changes, fully backward compatible
- To use global memories: Add WORKSPACE_MODE=hybrid to your config
- See Migration Guide below
Claude can automatically extract and store memories, or you can be explicit:

Natural language:

```plain text
"Remember that our API base URL is https://api.example.com/v2"

```

```plain text
"Store this as a directive: Always use functional components in React"

```

What Claude does: Uses the store_memory tool to save this information with appropriate context type and importance.

Store globally (v1.3+):

```plain text
"Remember globally: I prefer TypeScript strict mode for all projects"

```

```plain text
"Store this as a global preference: Always use ULIDs for database IDs"

```

What Claude does: Uses store_memory with is_global: true to make it accessible across all workspaces (requires WORKSPACE_MODE=hybrid or global).

Claude automatically retrieves relevant memories, but you can also ask:

```plain text
"What do you remember about our database schema?"

```

```plain text
"Recall any decisions we made about error handling"

```

What Claude does: Uses recall_relevant_context or search_memories to find related information.

Before context compaction, preserve important details:

```plain text
"Analyze our conversation and remember the important parts"

```

What Claude does: Uses analyze_and_remember to extract structured memories from the conversation.

Group related work:

```plain text
"Summarize this session and save it as 'Authentication Refactoring'"

```

What Claude does: Uses summarize_session to create a session snapshot with all relevant memories.

Promote workspace memory to global:

```plain text
"Convert this memory to global: mem_abc123"

```

What Claude does: Uses convert_to_global to move the memory from workspace-specific to globally accessible.

Convert back to workspace:

```plain text
"Convert this global memory to workspace-specific: mem_xyz789"

```

What Claude does: Uses convert_to_workspace to move the memory from global to current workspace.

Create relationships between memories:

```plain text
"Link these two memories: pattern mem_abc123 is an example of implementation mem_xyz789"

```

What Claude does: Uses link_memories to create an example_of relationship between the memories.

Find related memories:

```plain text
"Show me all memories related to mem_abc123"

```

What Claude does: Uses get_related_memories to traverse the relationship graph and find connected memories.

Remove a relationship:

```plain text
"Unlink relationship rel_123abc"

```

What Claude does: Uses unlink_memories to remove the relationship while keeping both memories intact.

View version history:

```plain text
"Show me the version history for memory mem_abc123"

```

What Claude does: Uses get_memory_history to retrieve all versions with timestamps and change reasons.

Rollback to previous version:

```plain text
"Rollback memory mem_abc123 to version ver_xyz789"

```

What Claude does: Uses rollback_memory to restore the memory to the specified version while preserving relationships.

Create a template:

```plain text
"Create a template for bug reports with fields: {{title}}, {{severity}}, {{steps}}"

```

What Claude does: Uses create_template to save a reusable template with placeholders.

Use a template:

```plain text
"Create a memory from bug template: title='Login fails', severity='high', steps='1. Click login 2. Error appears'"

```

What Claude does: Uses create_from_template to instantiate a memory with filled-in variables.

Assign category:

```plain text
"Categorize memory mem_abc123 as 'authentication'"

```

What Claude does: Uses set_memory_category to organize the memory.

List categories:

```plain text
"Show me all categories with memory counts"

```

What Claude does: Uses list_categories to display all categories and their sizes.

Get memories by category:

```plain text
"Show me all memories in the 'authentication' category"

```

What Claude does: Uses get_memories_by_category to retrieve all memories in that category.

Fuzzy search:

```plain text
"Search for 'authentification' with fuzzy matching"

```

What Claude does: Uses search_memories with fuzzy: true to find similar words despite typos.

Regex search:

```plain text
"Find memories matching the pattern 'API.*v[0-9]+'"

```

What Claude does: Uses search_memories with regex parameter for pattern-based search.

Category filtering:

```plain text
"Search for 'login' only in the 'authentication' category"

```

What Claude does: Uses search_memories with both query and category parameters.

Memories are categorized for better organization:

Claude has access to these memory tools:

- store_memory - Store a single memory
- store_batch_memories - Store multiple memories at once
- update_memory - Update existing memory (auto-creates version in v1.5+)
- delete_memory - Remove a memory
- search_memories - Search using semantic similarity (enhanced in v1.5+ with category/fuzzy/regex)
- organize_session - Create session groups
- recall_relevant_context - Proactively retrieve relevant memories
- analyze_and_remember - Extract and store memories from conversation
- summarize_session - Create session snapshot
- export_memories - Backup to JSON
- import_memories - Restore from JSON
- find_duplicates - Detect similar memories
- consolidate_memories - Merge multiple memories
- convert_to_global - Convert workspace memory to global
- convert_to_workspace - Convert global memory to workspace-specific
- link_memories - Create relationships between memories
- get_related_memories - Traverse relationship graph
- unlink_memories - Remove relationships
- get_memory_graph - Get full memory graph structure
- get_memory_history - View version history of a memory
- rollback_memory - Rollback to a previous version
- create_template - Create reusable memory template
- create_from_template - Instantiate memory from template
- list_templates - List available templates
- set_memory_category - Assign category to a memory
- list_categories - List all categories with counts
- get_memories_by_category - Retrieve memories by category
Browse memories directly using MCP resources:

- memory://recent - Recent memories (default 50)
- memory://by-type/{type} - Filter by context type
- memory://by-tag/{tag} - Filter by tag
- memory://important - High importance (≥8)
- memory://sessions - All sessions
- memory://session/{id} - Specific session
- memory://summary - Statistics overview
- memory://search?q=query - Semantic search
- memory://analytics - Usage analytics dashboard (v1.2+)
- memory://global/recent - Recent global memories (cross-workspace)
- memory://global/by-type/{type} - Global memories by context type
- memory://global/by-tag/{tag} - Global memories by tag
- memory://global/important - Important global memories
- memory://global/search?q=query - Search global memories
- memory://relationships - List all memory relationships
- memory://memory/{id}/related - Get related memories
- memory://graph/{id} - Get memory graph structure
Memories are automatically isolated by directory. Working in different projects? No problem:

```plain text
/Users/you/project-a/  → Workspace A memories
/Users/you/project-b/  → Workspace B memories

```

Memories from Project A never pollute Project B. Each workspace gets its own isolated memory space.

Want to:

- Share memories across machines? Use cloud Redis with the same REDIS_URL
- No local install? Use Upstash, Redis Cloud, or Railway (free tiers available)
- Team collaboration? Share Redis URL and workspace path with your team
See Configuration section for cloud Redis setup.

Recall enables teams to build collective knowledge that all Claude instances can access. Perfect for:

🏢 Organization-wide learning:

- Share coding standards, architecture decisions, and best practices across the entire team
- Build a living knowledge base that grows with every conversation
- New team members instantly access organizational context and conventions
👥 Team collaboration:

- Multiple developers using Claude can contribute to and benefit from shared memories
- Consistent answers to "how do we do X?" across all team members
- Preserve institutional knowledge even as team composition changes
🔄 Cross-project patterns:

- Share common patterns and solutions across different projects
- Build reusable memory templates for similar workflows
- Reduce repetitive explanations of organizational context
Setup for shared organizational memory:

1.  
1. 
1.  
Example workflow:

```plain text
Developer A: "Remember: Our API rate limit is 1000 requests/minute"
           [Stored in shared Redis]

Developer B: "What's our API rate limit?"
           [Claude retrieves from shared memory]
           "Your API rate limit is 1000 requests/minute"

```

Security considerations:

- Use Redis authentication and TLS (rediss://) for sensitive data
- Consider separate Redis databases for different teams/projects
- Implement access controls at the Redis level
- Audit memory contents periodically for sensitive information
See WORKSPACE_MODES.md for future plans on enhanced organizational memory features.

Cross-workspace memory sharing enables memories that work across all workspaces. Perfect for:

- Personal preferences and coding standards
- Team conventions and organizational knowledge
- Shared patterns and solutions
Workspace Modes:

- isolated (default) - Workspace-only memories, no cross-workspace access
- global - All memories shared globally, no workspace isolation
- hybrid - Both workspace-specific AND global memories (best of both worlds)
Configure workspace mode:

Create global memories:

```plain text
"Remember globally: I prefer TypeScript strict mode for all projects"

```

Claude stores with is_global: true, accessible across all workspaces.

Convert existing memories:

```plain text
"Convert this memory to global: [memory_id]"

```

Browse global memories:

- Use memory://global/recent resource
- Use memory://global/search?q=query for semantic search
- Global resources only work in global or hybrid modes
See WORKSPACE_MODES.md for detailed documentation.

Store memories that auto-expire:

```plain text
"Remember for the next hour: API is in maintenance mode"

```

Claude will add ttl_seconds: 3600 and Redis automatically removes it after 1 hour.

Use cases:

- Temporary debugging notes
- Session-specific context
- Time-sensitive reminders
Backup your memories:

```plain text
"Export all important memories to JSON"

```

Restore or migrate:

```plain text
"Import these memories: [paste JSON]"

```

Use cases:

- Regular backups
- Move memories between workspaces
- Share knowledge bases with team
- Archive old projects
Find similar memories:

```plain text
"Find duplicate memories with similarity above 90%"

```

Auto-merge duplicates:

```plain text
"Find and merge duplicate memories automatically"

```

Use cases:

- Clean up redundant memories
- Consolidate related information
- Optimize memory storage
See usage patterns:

```plain text
"Show me memory analytics"

```

Get insights on:

- Memory trends (24h, 7d, 30d)
- Most active types
- Top tags
- Importance distribution
- Daily activity breakdown
```plain text
You: "Remember: This project uses Prisma for database, tRPC for API, and Next.js for frontend"

Claude: [Stores 3 memories with type 'code_pattern']
         ✓ Stored: Prisma for database (importance: 8)
         ✓ Stored: tRPC for API (importance: 8)
         ✓ Stored: Next.js for frontend (importance: 8)

You (later): "What's our tech stack?"

Claude: [Retrieves memories]
        "Your project uses:
         - Prisma for database
         - tRPC for API
         - Next.js for frontend"

```

```plain text
You: "Store this error handling pattern we use:
     try { ... } catch (error) { logger.error(...); throw new AppError(...) }"

Claude: [Stores as 'code_pattern', importance: 9]
        ✓ Stored: Standard error handling pattern

You (in new file): "Add error handling here"

Claude: [Recalls pattern]
        "I'll use your standard error handling pattern with logger and AppError..."

```

```plain text
You: "We just finished refactoring auth. Summarize and save this session."

Claude: [Creates session with all relevant memories]
        ✓ Session created: "Auth Refactoring - 2025-01-15"
        ✓ 8 memories captured
        ✓ Summary: Refactored authentication to use JWT with refresh tokens

You (weeks later): "What did we change in the auth refactoring?"

Claude: [Retrieves session memories]
        "In the auth refactoring session, you:
         - Switched from sessions to JWT tokens
         - Added refresh token rotation
         - Implemented secure cookie storage
         - Updated middleware for new auth flow"

```

```plain text
# In project A (with WORKSPACE_MODE=hybrid)
You: "Remember globally: I prefer async/await over .then() in all projects"

Claude: [Stores with is_global: true]
        ✓ Stored globally: async/await preference (importance: 9)

# Switch to project B
You: "What are my coding preferences?"

Claude: [Retrieves global memories]
        "Your global coding preferences include:
         - Prefer async/await over .then() in all projects"

# Project-specific memory
You: "Remember for this project only: Use MongoDB with Mongoose"

Claude: [Stores with is_global: false]
        ✓ Stored: MongoDB with Mongoose (workspace-only, importance: 8)

# Back in project A
You: "What database are we using?"

Claude: [Only sees project A memories, not project B's MongoDB]
        "I don't see any database information stored for this workspace."

```

- REDIS_URL - Redis connection (default: redis://localhost:6379)
- ANTHROPIC_API_KEY - Claude API key for analysis and embeddings
- WORKSPACE_MODE (v1.3+) - Workspace memory mode (default: isolated) 
Local Redis (default):

Custom port:

Then set: REDIS_URL=redis://localhost:6380

Remote Redis:

Redis Cloud/AWS ElastiCache:

1. Storage: Memories stored in Redis with workspace isolation
1. Embeddings: Hybrid approach using Claude-extracted keywords + trigrams (128-dim vectors)
1. Search: Cosine similarity for semantic retrieval
1. Context: Auto-injected at conversation start via MCP prompts
1. Analysis: Claude Haiku analyzes conversations for memory extraction
Very affordable! Estimated ~$0.20/day for active development:

- Uses Claude Haiku (cheapest model) for analysis
- Hybrid embeddings reduce API calls
- Redis in-memory storage is fast and free
Recall stores all conversation context that Claude deems important, which may include:

- Credentials: API keys, passwords, tokens mentioned in conversations
- Code: Proprietary algorithms, business logic, security implementations
- Personal Information: Names, emails, organizational structures
- Business Secrets: Strategic decisions, financial data, competitive information
Critical Security Rules:

1. Never use public/shared Redis instances for sensitive projects
1. Never share Redis connection strings in public repositories or documentation
1. Always use authentication - Configure Redis with requirepass
1. Always use TLS for remote connections - Use rediss:// not redis://
1. Audit regularly - Review stored memories for inadvertently captured secrets
Local Redis (Development):

Production Redis (Cloud/Remote):

Additional Redis security:

- Bind to specific IPs: bind 127.0.0.1 ::1 (local only)
- Disable dangerous commands: rename-command FLUSHALL ""
- Use firewall rules to restrict access
- Enable Redis ACLs for fine-grained permissions (Redis 6+)
- Regular backups with encrypted storage
When deploying for team/organizational use:

Infrastructure Security:

- Deploy Redis in private VPC/network
- Use dedicated Redis instance (not shared with other services)
- Enable Redis encryption at rest
- Implement network segmentation and access controls
- Use VPN or private network access for remote connections
Access Management:

- Document who has Redis access
- Use separate Redis databases for different teams/security levels
- Implement audit logging for Redis access
- Regular access reviews and credential rotation
- Consider using Redis Enterprise with RBAC
Data Governance:

- Define data retention policies
- Implement automated cleanup of old/stale memories
- Create backup and disaster recovery procedures
- Document compliance requirements (GDPR, HIPAA, SOC2, etc.)
- Train users on what not to store in memories
Example: Multi-team isolation using Redis databases:

If you suspect a security breach:

1. Immediately rotate Redis credentials
1. Audit Redis access logs for unauthorized access
1. Review stored memories for exposed sensitive data
1. Flush compromised data using export_memories + selective deletion
1. Update all team members with new credentials
1. Review and strengthen security controls
GDPR (EU):

- Memories may contain personal data - ensure lawful basis for processing
- Implement data subject access rights (export/delete memories)
- Document data processing activities
- Ensure adequate security measures
CCPA (California):

- Disclose data collection and storage practices
- Provide mechanisms for data deletion
- Honor do-not-sell requests
HIPAA (Healthcare):

- Do not store PHI (Protected Health Information) in memories
- Use BAA-compliant Redis hosting if healthcare-related
- Implement encryption at rest and in transit
SOC2/ISO27001:

- Document security controls and procedures
- Implement access logging and monitoring
- Regular security assessments and audits
As a developer using Recall, you must:

✅ Do:

- Use secure, authenticated Redis instances
- Enable TLS for all remote connections
- Regularly audit stored memories
- Implement proper access controls
- Train your team on security best practices
- Have incident response procedures
- Comply with your organization's security policies
❌ Don't:

- Use public Redis instances for any sensitive data
- Store credentials or secrets in memories (use environment variables/secret managers instead)
- Share Redis connection strings publicly
- Ignore security warnings or skip authentication
- Store regulated data (PII, PHI, PCI) without proper controls
Solution 1: Start local Redis

Test connection:

Solution 2: Use cloud Redis (no install needed)

Sign up for free cloud Redis:

1.  
1.  
1.  
No local Redis installation required! ✨

Solution:

1. Check config file path is correct
1. Verify ANTHROPIC_API_KEY is set
1. Restart Claude completely (quit and reopen)
1. Check Claude's MCP logs for errors
Config file locations:

- Claude Code: ~/.config/Code/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json
- Claude Desktop (macOS): ~/Library/Application Support/Claude/claude_desktop_config.json
- Claude Desktop (Windows): %APPDATA%\Claude\claude_desktop_config.json
Solution: Check workspace isolation - you may be in a different directory.

Memories are scoped to the working directory where Claude was launched. To see your workspace:

```plain text
"What's my current memory workspace?"

```

Solution: Use smart context management:

```plain text
"Analyze our conversation and remember the important parts"

```

This extracts key information before context compaction.

Typical performance characteristics:

- Store Memory: ~200ms (includes embedding generation)
- Batch Store (10): ~500ms
- Get by ID: <1ms (Redis in-memory)
- Recent (50): ~10ms
- Semantic Search (1k memories): ~500ms
- Semantic Search (10k memories): ~2s
- v1.4.0 (Current) - Memory relationships, knowledge graphs, link related memories
- v1.3.0 - Global memories, cross-workspace sharing, workspace modes
- v1.2.0 - TTL support, Export/Import, Consolidation, Analytics
- v1.1.0 - Smart context management (recall, analyze, summarize)
- v1.0.0 - Initial release with core memory operations
See CHANGELOG.md for detailed changes

- Feature Documentation - Detailed v1.2 feature guide
- Context Management - Smart context guide (v1.1)
- Changelog - Complete version history
```plain text
/mem/
├── src/
│   ├── index.ts                 # Server entry point
│   ├── types.ts                 # TypeScript types & schemas
│   ├── redis/
│   │   ├── client.ts           # Redis connection
│   │   └── memory-store.ts     # Storage logic
│   ├── embeddings/
│   │   └── generator.ts        # Claude embeddings
│   ├── analysis/
│   │   └── conversation-analyzer.ts  # AI analysis
│   ├── tools/
│   │   ├── index.ts            # Core tools
│   │   ├── context-tools.ts    # Smart context tools
│   │   └── export-import-tools.ts    # Advanced tools
│   ├── resources/
│   │   ├── index.ts            # MCP resources
│   │   └── analytics.ts        # Analytics resource
│   └── prompts/
│       ├── index.ts            # MCP prompts
│       └── formatters.ts       # Context formatters
└── dist/                        # Built output

```

- Issues: Report bugs or request features on GitHub
- Questions: Open a discussion for help
- Documentation: Check the docs folder for detailed guides
MIT - See LICENSE file

Built with ❤️ by José Airosa for Claude users tired of repeating context

Powered by: TypeScript, Redis, Anthropic Claude, Model Context Protocol


