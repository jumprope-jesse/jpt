# FBI Cyber Threat Landscape (2024)

Summary of FBI Cyber Assistant Director Bryan Vorndran's remarks at the 2024 Boston Conference on Cyber Security (June 2024).

## FBI Cyber Strategy

1. **Investigate and attribute** - Punish cybercriminals, raise their cost to operate
2. **Gather and operationalize intelligence** - Support victim recovery, enable joint operations
3. **Partner broadly** - Domestic/global, public/private collaboration
4. **Victim engagement** - Rapid threat response and support

## Ransomware Business Model

Modern ransomware operates as organized crime with four key services:
- **Infrastructure** - Servers, hosting
- **Communications** - C2, affiliate coordination
- **Malware** - Sophisticated code developed by skilled coders
- **Currency** - Cryptocurrency laundering

**Affiliate model**: Less technical criminals deploy sophisticated malware, pay 20% cut to developers.

### Target Selection Criteria
1. Who is easily targetable? (poor net defense)
2. Who is likely to pay? (brand damage concerns)
3. Who will pay the most? (economic impact from downtime)

### Extortion Tactics
- **Double extortion**: Encryption + data theft
- **Triple extortion**: Encryption + data theft + harassment of victims/executives
- **Key insight**: Paying ransom only prevents release "right now" - assume data may be released later or used for re-extortion

## Major Operations (2024)

### Operation Endgame
- Targeted malware-as-a-service groups
- Took down 100+ servers, dismantled 4 global malware variants
- Multi-nation collaboration (Denmark, France, Germany, Netherlands)

### LockBit Disruption
- Most-deployed ransomware globally since 2022
- 1,800+ U.S. attacks, 2,400+ global, billions in damages
- Run by Dimitri Khoroshev (aliases: Putinkrab, Nerowolfe, LockBitsupp)
- FBI obtained 7,000+ decryption keys for victims
- LockBit was keeping victim data even after ransom paid

### Operation Dying Ember (Boston-led)
- Targeted Russian GRU botnet
- Remediated 1,000+ compromised home/small-business routers
- Same GRU unit behind NotPetya, Ukrainian grid attacks

### 911 S5 Botnet Takedown
- World's largest botnet/residential proxy service
- 19M IP addresses across 200 countries (600K in U.S.)
- Used for pandemic relief fraud, child exploitation, bomb threats
- $29M cryptocurrency seized

## Nation-State Threat Assessment

### China (characterized as "relentless")
- Largest cyber program in the world
- **Volt Typhoon**: Persistent access to U.S. critical infrastructure (telecom, energy, water)
- Uses "living off the land" techniques - exploits built-in tools to avoid detection
- Goals: IP theft, pre-positioning for future attacks ("prepping the battlefield")
- Targets aligned with China's 14th Five-Year Plan: AI/ML, biotech, clean energy, quantum, aerospace

### Russia
- Safe haven for ransomware criminals
- GRU conducts offensive cyber operations using criminal infrastructure
- "Blurs the line between criminal activity and state operations"

### Iran & North Korea
- Active nation-state actors mentioned but less detailed

## Security Recommendations

### Fundamentals (must be repeatable across entire org)
- Multi-factor authentication
- Password management
- Effective logging and log management
- Vulnerability and patch management
- Air-gapped, encrypted, current backups

### Planning Requirements
Four plans needed:
1. Business continuity
2. Crisis management
3. Disaster recovery
4. Incident response

**Exercise goals**:
1. Develop synergy among decision makers
2. Refine decision-making process

### Three Key Exercise Focus Areas

1. **Communications protocols** - Internal and external communication decision-making
2. **Pay/no-pay decision** - Pre-determine thresholds based on organizational impact
3. **Government sharing** - Decide what and when to share with USG

### Pre-Incident Relationships to Establish
- Outside counsel: retention threshold, information sharing guidance, report types
- Third-party IR firm: retention threshold, expected deliverables
- Insurance provider: counsel must know policy details before incident
- Industry peers: "Use 'peer' instead of 'competitor'" - if you're targeted, so are they

## Key Quotes

> "85-90% of the most powerful cyber-threat intelligence lies in the hands of those other than the United States government"

> "When companies are extorted and choose to pay to prevent the leak of data, you are paying to prevent the release of data right now—not in the future."

## FBI Director Wray's Munich Security Conference Remarks (February 2024)

### Russian Infrastructure Targeting
Following up on Operation Dying Ember, FBI Director Christopher Wray disclosed additional details at the Munich Security Conference about Russia's evolving cyber threat:

- **Critical infrastructure reconnaissance**: Russia conducting surveillance on U.S. energy sector and other critical systems
- **Quick pivot capability**: Once access is established, hackers can switch from information gathering to attack "quickly and without notice"
- **Global targeting**: Underwater cables, industrial control systems worldwide
- **Post-Ukraine invasion escalation**: Increased targeting of infrastructure since Russia's unprovoked invasion

### China Threat Scale
Wray characterized China's cyber program as "massive":
> "The cyberthreat posed by the Chinese government is massive. China's hacking program is larger than that of every other major nation combined."

This assessment aligns with the Volt Typhoon operation details from Operation Dying Ember.

### Botnet Disruption Details (February 2024)
The Russian intelligence operation disrupted in collaboration with international partners:
- **Scale**: 1,000+ home and small-business routers infected globally
- **Attribution**: Russian intelligence collaborating with cybercriminals
- **Targets**: Military and security organizations, private corporations in U.S. and allied countries
- **Technique**: Court-ordered operation to secretly copy and delete stolen data/malware from routers without affecting functionality
- **Purpose**: Intelligence gathering with capability to pivot to attacks

This operation represents the broader pattern of Russia using criminal infrastructure for state-sponsored operations, as noted in the threat assessment above.

## Resources
- FBI Internet Crime Complaint Center: ic3.gov
- Source: https://www.fbi.gov/news/speeches/fbi-cyber-assistant-director-bryan-vorndran-s-remarks-at-the-2024-boston-conference-on-cyber-security
- NYT Coverage (Feb 2024): https://www.nytimes.com/2024/02/15/us/politics/hacking-russian-intelligence-routers.html
