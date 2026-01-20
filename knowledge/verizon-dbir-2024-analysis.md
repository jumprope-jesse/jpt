# Verizon DBIR 2024 Analysis

Kelly Shortridge's analysis of the 2024 Verizon Data Breach Investigations Report, with pragmatic security economics insights.

Source: https://kellyshortridge.com/blog/posts/shortridge-makes-sense-of-verizon-dbir-2024/

## Key Finding: It's Still About Money

- **93% of breaches** are financially motivated
- Espionage only 7% (and concentrated in government/public administration)
- "Espionage" includes mundane things like sales reps taking contact lists to new employers
- Combined "employee whoopsies" + "organized crime" = 90% of threat actors

**Implication**: You're probably not important enough for nation-state targeting. Stop LARPing as counterintelligence.

## MOVEit vs Log4Shell: Why MOVEit Was Worse

MOVEit implicated in **1,567 breach notifications** - dwarfing Log4Shell's 0.4% of incidents.

Why MOVEit had more real-world impact:

1. **Scalable + easy monetization**: Designed to store sensitive data uniformly, trivial to ransom
2. **Log4Shell requires more work**: Get a shell... then what? Must tailor exploit, pivot, find value
3. **User software vs library**: IT tools harder to update than engineering libraries (automated tooling helps devs)
4. **Target industries**: Education and Healthcare - not known for effective software operationalization
5. **On-prem deployment**: SaaS can update on behalf of customers
6. **Internet-accessible + uniform deployment**: Easy to discover and automate attacks
7. **Compliance software doesn't have to be good**: Customers forced to buy it anyway

## The Phishing Reality

DBIR calls it "alarming" that users fall for phishing in <60 seconds. Shortridge's counter:

- Average email attention time: **9 seconds** (Litmus 2023)
- 30% of emails get <2 seconds attention
- At 100 emails/day, 1 malicious click = **0.008% fail rate**
- Even 100 malicious clicks = only 0.8%

**The math on scrutiny**:
- 1 minute per email × 26k emails/year = **217 hours/year**
- 5 minutes for real verification = **1,000+ hours/year** (45 days!)

**Solution**: Reduce email volume (10/day would make scrutiny reasonable), or stop blaming users for industry's UX failures.

## GenAI in Attacks: Not Happening

- <100 mentions on criminal forums over 2 years combined
- When mentioned, mostly for generating CSAM
- Attackers don't need it - "good enough" techniques already work

> "Attackers do not let 'good enough' be the enemy of perfect and care about results, not hype"

## Vulnerability Exploitation

- Exploitation up 180% but still only 10% of initial access
- **Credential stuffing in web apps** remains primary "way-in"
- Vulns predominantly exploited: web apps > desktop sharing > VPNs

### Better Approaches Than "Just Don't Write Vulns"

1. **Isolation** (spatial and temporal) - prevent chaining, limit access gained
2. **Modular architecture** - limits blast radius
3. **Learn from safety engineering** - things should work even with flaws (plane flies with cracked wing)
4. **Rust's approach**: Consider it a security bug when certain vuln classes are even possible to write

## Ransomware + Extortion (REx) Economics

- REx = ~62% of financially-motivated breach actions
- **Only 4% of REx complaints had actual loss** (down from 7%)
- Median loss: $46,000 (range: $3 to $1.14M for 95% of cases)
- Median ransom request: **1.34% of company revenue** (0.13% to 8.30% in 80% of cases)

### Bad Math for Budgeting

4% probability × 1.34% revenue = **~0.05% of revenue** to break even

For $100M revenue company:
- Break-even spend: ~$54,000
- EDR at that price: ~300 licenses (most orgs need 1k+ = $185k/year)

### Better Budget Conversations

Present options with ranges:
- 20% confidence interval: $5,200
- Median: $53,600
- 80% confidence interval: $332,000
- 95% tail risk: $999,600

Then list what mitigations each price point buys, starting with backups (useful for other purposes anyway).

## Quotable Insights

> "You are not a spider caught in a sexy spy web."

> "The real APTs – the ones motivated by geopolitical power – do not think about you at all."

> "We have utterly failed as an industry if our hope rests on humans not clicking things on the thing clicking machine."

> "Compliance software doesn't have to be good; compliance requirements force customers to buy it anyway."

## Related

- See also: [[fbi-cyber-threat-landscape-2024]] for FBI perspective on same threat landscape
- Kelly Shortridge's book: "Security Chaos Engineering: Sustaining Resilience in Software and Systems"
