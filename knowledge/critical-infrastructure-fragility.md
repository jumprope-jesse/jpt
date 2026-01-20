# Critical Infrastructure Fragility: A Pre-War Reality Check

Source: Bert Hubert presentation at Universiteit Leiden (2024)
https://berthub.eu/articles/posts/cyber-security-pre-war-reality-check/

## The Pre-War Framing

Donald Tusk (Polish PM): "A new era has begun. The pre-war era."

The presentation argues we should evaluate our infrastructure not just for peacetime resilience but for wartime/crisis scenarios where:
- Power may be out
- Cables to other continents may be cut
- Remote workers may be unreachable
- Cloud services may be unavailable

## Three Things That Matter in Crisis

1. **Robust infrastructure** - Does not fall by itself (Microsoft 365 falls over 1-2 days/year without being attacked)
2. **Limited, known dependencies** - Does your stuff need computers/people 5,000km away?
3. **Ability to improvise** - Can you truly own and understand your technology?

## The Sound-Powered Phone: A Model

The sound-powered phone has ~5 components, no electricity required, and works over 50km of cable. It survives ship fires, hammer strikes, and power outages.

Contrast with modern progression:
- Sound-powered phone → Dutch Emergency Network (20 bunkers, copper wire, fully redundant) → KPN VPN-based NCV → Microsoft Teams → WhatsApp (actual Dutch government emergency network)

Each step added complexity, dependencies, and fragility.

## Real Infrastructure Failures

### Botlek Bridge (Netherlands)
- Failed 250+ times total, 75 times/year initially
- Engineers lived on-site in a van trying to diagnose
- Root cause: a rotten ethernet cable/port
- **Diagnosis took 3+ years** because no one thought to check basic hardware
- "A sign you do not have control over your own infrastructure"

### Dutch Emergency Communications
- Old system: 20 bunkers with independent copper network, fully redundant
- New system: DSL modems using KPN VPN
- During a power outage, it didn't work. Because the power was out.

### Kyivstar (Ukraine, 2024)
- Major telecom, destructive Russian cyberattack
- **Back up in 2 days** because Ukrainians were battle-hardened and prepared
- Hubert's assessment: equivalent attack on Dutch telco → 6 months downtime

## The Outsourcing Problem

"5G equipment: we decided whether to use Chinese infrastructure. But Chinese were already running our infrastructure."

Current reality map:
- **Cloud**: US (Google, Microsoft, AWS)
- **Hardware maintenance**: Often India (even for "Ericsson/Nokia" equipment)
- **China & India**: Geopolitically aligned with Russia

"If they wanted to harm us, they just had to stop showing up for work."

Job vacancies at major telcos show no positions for anyone actually operating radio networks - it's all outsourced.

## Security Product Quality

Hubert scanned Dutch internet in a weekend, found 10,000 hackable systems.

Major security vendors have hundreds of vulnerabilities per month:
- "441 new security problems this month" is now normal
- Many are childishly simple (adding `/` to URL gives admin access, password reset sent to second email address without checking)

Even Hubert's own 1,600-line image sharing app (tinyimg) had 3 major vulnerabilities found by auditors. "Imagine 5 million lines."

## The Technical Expertise Drain

When organizations move to cloud:
1. Technical people leave (work gets boring)
2. You end up with no one who knows what's happening
3. Board decisions get made by non-technical people
4. "You could have a whole board full of people that studied history and art and French, and they sit there making cloud decisions"

The Dutch government has said they won't move "classified things and basic government registrations" to cloud. Everything else is on the table.

## Bright Spots

### Maeslantkering (Storm Surge Barrier)
- Sound-powered-phone philosophy: simple, passive, redundant
- Two engines push it closed, but it can close even if engines fail
- No sensors - completely passive operation
- "Shows it can be done"

### European Tech Capability
- All high-end chip-making equipment comes from a small area in Netherlands
- ASML, extreme UV optics
- "We're not completely helpless. We've just chosen to focus on handbags and EUV optics, not running our own vital infrastructure."

## Key Quotes

> "Non-technical people have made choices and have optimized for stuff being cheap. Or at least not hassle."

> "Can you imagine in a war situation that we have to beg the Donald Trump administration if they would please fix our cloud issues here?"

> "We are sitting ducks. And we're fine with that."

## Tags
infrastructure, cybersecurity, resilience, europe, critical-infrastructure, organizational-competence
