# AI Safety & Policy Discourse

Tracking key arguments, positions, and developments in AI safety/alignment discussions.

---

## Sources

- **Zvi Mowshowitz** - Weekly AI newsletter on LessWrong (AI #NNN series)
  - Comprehensive weekly roundups of AI news, safety developments, and policy
  - URL pattern: https://www.lesswrong.com/posts/[id]/ai-NNN-[title]

---

## Key Themes (from AI #140, October 2025)

### The "Build vs. Don't Build" Debate

The discourse around whether to build superintelligence now without knowing how to do so safely:

- One camp: "How dare you say don't build superintelligence without knowing how to do it safely"
- Counter: We're being asked to accept "societal dynamics we do not know how to control"
- Zvi's framing: "Sometimes the best you can do is try to avoid things getting even worse even faster"

### AI Freedom of Speech (by Country)

From The Future of Free Speech report:

| Country | AI Speech Freedom | Notes |
|---------|------------------|-------|
| USA | Highest | Strong protections |
| EU | High | "Hate speech" style rules, but AI already self-censors |
| Brazil | Moderate | - |
| South Korea | Lower | - |
| India | Lower still | - |
| China | Much lower | Extensive pre-deployment testing, censorship verification |

Among models:
- Grok: 58-65% (highest)
- US labs (Anthropic, Google, OpenAI): 58-65%
- Mistral (France): 46%
- DeepSeek: 31.5%
- Qwen: 22%

**Key insight**: Even with "openness" as criteria, open models score lower on freedom than closed models.

### Comparative Advantage & AI Job Displacement

Recurring debate pattern:
- Critics: "But comparative advantage means everything will be fine!"
- Zvi's response: This is a common objection he's answered many times; historical comparative advantage arguments don't automatically apply to AI automation

### AI Model Censorship in Practice

Practical experience (as of late 2025):
- Claude (Sonnet 4.5/Opus 4): "Basically never censor things they shouldn't" - exception: bio-risk queries hitting filters accidentally
- GPT-5: Similar to Claude
- Gemini 2.5: "Totally does" over-censor

### Transaction Cost Reduction

AI/agents promise to radically reduce transaction costs in electronic markets, enabling:
- Richer, more efficient market designs
- Better matching at lower prices
- One estimate: 12-18% GDP boost over 15-25 years from this effect alone

---

## Alignment & Safety Notes

### WorldTest Benchmark Results

New "AutumnBench" suite testing AI understanding vs pattern-matching:

- 43 interactive worlds, 129 tasks
- Tests: predicting hidden world aspects, planning action sequences, detecting rule changes
- Finding: Humans reset 12% of time during exploration; models reset <2%
- Implication: Models don't explore/experiment strategically, rely heavily on pattern matching

### Sabotage Risks (Anthropic Research)

Anthropic publishing reports on sabotage risks - a new category of safety reporting to watch.

### Claude Introspection

Anthropic reports Claude can notice "thought injections" - relevant to prompt injection security.

---

## Companies & Strategy

### OpenAI Direction (late 2025)

- Launching browser and short-duration video social network
- Adding shopping integrations
- Adding erotica (with controversy)
- IPO discussions at $1T valuation

### Anthropic Direction (late 2025)

- Enterprise/business focus
- Financial services expansion (Claude for Excel beta, live data sources)
- 1 million TPUs from Google partnership
- Browser extension for Chrome

### Cursor 2.0

- Own coding model called "Composer"
- Claims 4x faster than comparable frontier models
- New multi-agent parallel interface
- "Plan mode" - plan with one model, execute with another

---

## Practical Notes

### AI-Generated Music (Suno v4-v5)

- Generic music now "indistinguishable from human music" in blind tests
- 50/50 identification rate general, 60/40 when same genre
- "Faster to create a Suno song than to listen to it"
- Quality bar: If you intend slop, you get slop; if you intend art, you get art

### Hospital Bill Negotiation

Claude reportedly helped cut hospital bill from $195k to $33k by identifying:
- Duplicative charges
- Improper coding
- Other violations

Barriers: (1) knowing you can do this, (2) getting itemized bill

---

## Meta-Commentary

Zvi's recurring frustrations:
- Having to repeatedly explain why "comparative advantage solves everything" is insufficient
- The need to explicitly state obvious things like "don't sell advanced chips to adversaries"
- People seeing one dumb AI output and concluding "AGI will never happen"
