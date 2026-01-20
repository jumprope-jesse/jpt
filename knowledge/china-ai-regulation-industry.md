# China's AI Industry & Regulatory Framework

*Source: LessWrong "A Brief Review of China's AI Industry and Regulations" (March 2024)*

Comprehensive overview of China's AI regulatory approach through three major pieces of legislation, plus context on industry development and comparative positioning vs. US/EU approaches.

---

## China's AI Industry Overview

### Market Size & Growth
- Forecasted 2024 market: **$38.89 billion** (37% the size of US market)
- 2017 AI development plan: become **global AI leader by 2030**
- Central concept: **"indigenous innovation" (自主创新)** - self-reliance in technology

### Research Output
- On par with US in share of top global publications and citations (CSET 2022)
- **78% of Chinese citizens** agree AI products have more benefits than drawbacks (highest of surveyed countries, vs 35% US)

### Notable LLMs
- **Wu Dao 2.0** (2021) - Beijing Academy of AI
  - Called "world's largest model" but uses mixture of experts (MoE) architecture
  - MoE = sparsely activated, different parameter groups for different inputs
  - More parameters than GPT-3 but NOT necessarily more powerful
  - Never publicly released or benchmarked properly

- **PanGu-Σ** (2023) - Huawei Technologies
  - Also MoE architecture
  - Computationally inexpensive relative to parameter count but can be outperformed by smaller dense models

### Copyright Differences
- **Beijing court ruling**: AI-generated content IS copyrightable in China
- Contrast: US and EU rule AI-generated content cannot be copyrighted
- Note: Some argue precedent is less binding in Chinese legal system; others expect huge impact

### US Export Controls Response (2022)
- Strict controls on computer chips necessary for advanced AI
- Includes materials and methods to manufacture chips
- See CSIS report or Deric Cheng's upcoming evaluation of AI chip registration policies

---

## The Three Major AI Regulations

### 1. Generative AI (2023)
**Interim Measures for the Management of Generative AI Services**

**Scope:**
- Only applies to **public-facing** GAI in mainland China
- Excludes internal/non-public business/research use

**Core Requirements:**

*Content & Values:*
- Must adhere to **core socialist values**
- Respect protected characteristics
- Adhere to IP & consent laws
- Must NOT:
  - Endanger national security or interests
  - Incite subversion or split the nation
  - Harm nation's image or reputation
  - Spread false information or disrupt economic/social order
  - Infringe others' lawful rights and interests

*Data & Training:*
- Training data must be legal, not discriminatory
- Manual labeling must use clear rules with quality assessments
- When editing biometric info, must prompt user to get consent
- Must watermark GAI output
- Must allow users to add conspicuous labels to output

*Provider Responsibilities:*
- GAI providers bear responsibility for violations
- Must provide easy complaint mechanisms
- Must cooperate with government oversight inspections
- Those with "public opinion properties" or "social mobilization capabilities" must file algorithms and conduct security assessments

*Government Role:*
- Will support industry innovation
- Conduct international exchange and participate in global AI regulation
- Penalties follow past legislation or warnings → corrections → service suspension

**Commentary:**
- **Jenny Shang (Pillsbury Law)**: Final version significantly lighter than early drafts
  - No mandatory pre-release reviews
  - No detailed filing requirements
  - No forced data security assessments for all providers

- **Matt Sheehan (Carnegie)**:
  > "By rolling out a series of more targeted AI regulations, Chinese regulators are steadily building up their bureaucratic know-how and regulatory capacity."

- **Matt O'Shaughnessy (Carnegie)**:
  > "Parts of the draft regulation would make real progress in shielding millions of people from potential harms of AI, if enforced in a uniform and meaningful way"

- **Qiheng Chen**: Gap in open-source guidance creates ambiguity, could hamper innovation

---

### 2. Deep Synthesis / Deepfakes (2022)
**Provisions on the Administration of Deep Synthesis Internet Information Services**

**Definition:**
"Deep synthesis technology" = any technology using generative synthetic algorithms (deep learning, VR) to produce:
- Text
- Images
- Audio (vocal and music)
- Video
- 3D construction and simulation

**Core Prohibitions:**
Deep synthesis must NOT be used to:
- Harm national security or interests
- Spread false information
- Recreate someone's image/voice without consent
- Produce, duplicate, publish, or spread illegal information

**Technical Requirements:**
- Must **watermark** all output
- Must allow users to add **conspicuous labels**
- Must ADD conspicuous labels when providing:
  - News editing/publishing
  - Services that edit biometric information
  - Services with public opinion properties or social mobilization capacity

**When Security Assessments Required:**
Tools that can:
- Generate/edit biometric info
- Generate/edit non-biometric info with public opinion/mobilization capacity
- Other tools that could create security risks

**Filing & Oversight:**
- Providers with public opinion properties or social mobilization capacity must:
  - File within 10 working days of service launch
  - Display filing number prominently
  - Conduct security assessments
- Internet/telecom/public security departments may conduct oversight inspections

**Penalties:**
- Violations → legal punishment
- Serious consequences → heavier penalties

**Commentary:**
- **Matt Sheehan (Carnegie)**:
  > "The deep synthesis regulation was years in the making, but in the end it suffered from particularly poor timing. It was finalized on November 25, 2022, just five days before the release of ChatGPT."

- **Paol Triolo (Albright Stonebridge)**:
  > "Chinese authorities are clearly eager to crack down on the ability of anti-regime elements to use deepfakes of senior leaders, including Xi Jinping, to spread anti-regime statements."

- **Kendra Schaefer (Trivium China)**:
  > "China is able to institute these rules because it already has systems in place to control the transmission of content in online spaces... How can Western democracies fight a war against disinformation... but without resorting to censorship?"

**Implementation:** Hard to find information on how laws have been applied since early 2023 effective date. At least one case where face-swapping app was court-ordered to compensate wronged individuals.

---

### 3. Algorithmic Recommendations (2021)
**Provisions on the Management of Algorithmic Recommendations in Internet Information Services**

**Definition:**
Algorithmic recommendation technology = using algorithms for:
- Generation and synthesis
- Individualized pushing
- Sequence refinement
- Search filtering
- Schedule decision-making

**Core Requirements:**

*General Obligations:*
Must NOT use ARS to:
- Spread false information
- Disrupt economic or social order
- Infringe others' lawful rights and interests
- Abuse market advantage or engage in monopolistic/unfair competition
- Engage in unreasonable differential treatment (price discrimination)

*User Rights:*
Must provide users with:
- Options to turn off algorithmic recommendations
- Convenient ways to select/delete tags used for recommendations
- Easy complaint registration

*Special Protections:*
- **Minors (under 18)**: When providing services, must establish special pages, channels, or functions that promote beneficial content and protect physical/mental health
- **Elderly**: Respect lawful rights
- **Workers**: Support those whose income depends on algorithmic systems (e.g., delivery workers subject to algorithmic scheduling or price discrimination)

*Governance Requirements:*
- Must uphold mainstream values
- Actively spread positive energy
- Must NOT establish clickbait titles/thumbnails using algorithms
- Must NOT create "filter bubbles" manipulating public opinion or circumventing information oversight
- Must set up classification systems that clearly mark source/accuracy/release time for news

**Registration & Oversight:**
- Categorized algorithm security management system based on:
  - Public opinion properties
  - Social mobilization capability
  - Content categories
  - Scale of users
  - Importance of data handled

- Providers with public opinion properties or social mobilization capabilities must:
  - **Register algorithm with government**
  - Submit self-assessment report
  - Submit security assessment
  - Maintain filing

- Cybersecurity department conducts algorithm security assessments
- Providers must preserve records and support government investigators

**Legal Liability:**
- Different violations → different legal consequences
- Criminal liability possible
- Fines up to **100,000 yuan ($14,000 USD)**

**Commentary:**
- **Matt Sheehan (Carnegie)**:
  > "The term 'algorithmic recommendation' first emerged during a 2017 CCP backlash against ByteDance's news and media apps, in which user feeds were dictated by algorithms. The party viewed this as threatening its ability to set the agenda of public discourse."

- **Lionel Lavenue et al. (Finnegan)**: On international law implications
  > "The regulations may allow Chinese litigants to refuse or delay discovery... Chinese defendants must 'know from the outset they risk serious consequences if and when they fail to obey a U.S. court's order to compel discovery'"

- **Steven Rolf**: Comparing to EU AI Act
  > "The major distinguishing feature of [the EU AI Act] is its emphasis on upholding fundamental individual rights... From the perspective of individuals, Europe's regulatory drive is preferable to China's – which places little emphasis on privacy or fundamental rights. But it does little to tackle issues beyond individual concerns."

  Key contrast: **China's 'social' model vs. Europe's 'individualist' model**
  - EU AI Act: Comprehensive horizontal regulation (covers all AI applications)
  - China: Vertical regulations (targets specific applications/manifestations)
  - China targets "societal-level harms" (e.g., tipping elections) more directly
  - EU focuses on individual rights (privacy, ethical decision-making)

---

## Key Concepts

### "Public Opinion Properties" & "Social Mobilization Capabilities"
These terms appear throughout all three regulations. They determine:
- Whether algorithm filing is required
- Whether security assessments are mandatory
- Level of government oversight
- Labeling requirements

Services with these properties face the strictest requirements.

### Algorithm Registry
- Reusable regulatory tool acting as "scaffolding" for successive regulations
- Providers must submit detailed information about algorithms
- Government maintains central registry
- Precedent for potential future AI regulations

---

## Regulatory Structure & Strategy

### Three Shared Structural Similarities (Matt Sheehan)

1. **Algorithms as point of entry** - Focus on algorithmic systems rather than general-purpose computing
2. **Building regulatory tools and bureaucratic know-how** - Iterative capacity building
3. **Vertical and iterative approach** - Laying groundwork for capstone AI law

**Vertical vs. Horizontal Regulation:**
- **Vertical**: Target specific application/manifestation (China's approach)
- **Horizontal**: Comprehensive umbrella law covering all applications (EU's AI Act approach)

### Three Primary Functions + One Auxiliary

**Primary:**
1. Shape technology to serve CCP's agenda for information control and political/social stability
2. Address social, ethical, and economic impacts on people (e.g., worker protections from algorithmic scheduling)
3. Create policy environment conducive to becoming global AI leader

**Auxiliary:**
- Build regulatory infrastructure and expertise for future comprehensive AI law

---

## Comparative Context

### vs. United States
- **US**: Export controls on chips to China (2022)
- **US**: Fair use likely applies to AI training (Anthropic case, 2025)
- **US**: AI-generated content NOT copyrightable
- **China**: AI-generated content IS copyrightable (Beijing court)
- **China**: More explicit content controls and political alignment requirements
- **Both**: Concerns about national security and competitiveness

### vs. European Union
- **EU AI Act**: Horizontal regulation (comprehensive)
- **China**: Vertical regulations (application-specific)
- **EU**: Focus on individual rights (privacy, non-discrimination)
- **China**: Focus on social/collective impacts (public opinion, social order)
- **EU**: Risk-based tiers for different AI applications
- **China**: Capability-based triggers (public opinion properties, social mobilization)

### Cultural & Legal Differences
- **Legal precedent**: Less binding in Chinese system (though Beijing copyright ruling may still have major impact)
- **Enforcement**: China has existing content control infrastructure to enforce these rules
- **Public trust**: 78% Chinese citizens positive on AI (vs 35% US)
- **Transparency**: Western democracies struggle to implement similar content controls without censorship concerns

---

## Strategic Implications

### "Indigenous Innovation" (自主创新)
- Long-standing emphasis on self-reliance in industry and technology
- Xi Jinping leadership concept
- Goal: reduce dependence on Western technology while becoming global leader

### US-China AI Competition
- **2017 AI development plan**: China aims to be global AI leader by 2030
- **US response**: 2022 chip export controls
- **Research output**: China on par with US in top publications/citations
- **Commercial deployment**: Different regulatory environments create different innovation patterns

### The "Race" Debate
- **US-China Commission**: Calls for explicit "race to AGI" (criticized for lack of evidence China is actually racing to AGI)
- **Chip controls**: Necessary for strategic positioning but must balance with allies/trade relationships
- **Market share vs. capabilities**: David Sacks "winning" = market share; others see strategic capability race

---

## Remaining Questions & Unknowns

1. **Enforcement**: How are these regulations applied in practice? Limited public information on enforcement actions since 2023.

2. **Wu Dao 2.0 capabilities**: Never publicly benchmarked - claims of superiority to GPT-3 unverified.

3. **Interplay between regulations**: How do the three regulations interact when a service involves multiple categories (generative AI + algorithmic recommendations)?

4. **Future comprehensive AI law**: China preparing to draft national AI law - these vertical regulations are building blocks.

5. **International influence**: Will China's approach influence other countries? Already seeing variations in Asian markets.

---

## Related Resources

- **Convergence Analysis**: Publishing deep dives on AI chip registration policies, EU/China/US legislation comparisons
- **State of AI Regulatory Landscape 2024**: Forthcoming comprehensive report
- **DigiChina**: Stanford University's resource on Chinese tech policy
- **CSET (Georgetown)**: Research on China-US AI comparison
- **Matt Sheehan's analysis**: "Making Sense of China's AI Regulations"

---

## Key Takeaways

1. **China has enacted substantive AI regulation** while US/EU still debating frameworks
2. **Vertical approach** targets specific applications (generative AI, deepfakes, recommendations) vs. EU's horizontal comprehensive approach
3. **Social/collective focus** vs. Western individual rights focus
4. **Existing content control infrastructure** enables enforcement Western democracies can't easily replicate
5. **Building regulatory capacity** iteratively toward comprehensive national AI law
6. **Strategic competition** with US focused on both capabilities and market position
7. **Copyright divergence** may create fundamentally different AI training ecosystems
8. **"Indigenous innovation"** drive toward self-reliance while becoming global leader

The Chinese approach represents a third way: neither the EU's comprehensive rights-based framework nor the US's mostly hands-off approach, but targeted interventions focused on social stability and strategic positioning.
