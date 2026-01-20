# Bootstrapped SaaS Lessons

Lessons from running self-funded SaaS businesses in competitive markets.

## Source
- [Four years of running a SaaS in a competitive market](https://maxrozen.com/on-four-years-running-saas-competitive-market) - Max Rozen (OnlineOrNot)

## Core Principles

### Time Management
- **Consistent daily effort** beats sporadic bursts - 2 hours/day, every workday
- The amount of time matters less than putting in effort consistently for years
- Adjust your schedule (wake earlier) rather than finding time

### Focus
- **No other side projects** - "the person who chases two rabbits catches neither"
- Building marketing/sales from $0 to $500 MRR is hard enough without splitting focus
- Once something works, double down instead of repeating the hardest part

### Product Development
- **Solve customer pain** - ask users what brought them to sign up, read every response
- **Be ruthlessly iterative** - if it can't ship in 2 hours, cut scope
- Ship early versions fast, build functionality once deployed (behind feature flags)

## Practical Lessons

### Onboarding & Conversion
- Free trials significantly outperform free tiers for conversion
- Default all users to free trial first - let them experience the full product
- Starting with "this is a paid service" beats "this is free, you might pay later"
- One founder doubled monthly growth rate by switching to trial-first

### Documentation
- **"Developers don't read documentation" is bullshit**
- Docs drive retention - users who find answers in docs stick around
- Build docs with same care as product (consider custom API docs for better UX)

### Mobile
- ~50% of B2B SaaS users start their journey on mobile
- Responsive mobile views are not optional - mobile users churn without them

### Analytics & Feedback
- Invasive product analytics (session recording, funnels) may not be worth it for solos
- Most products don't get enough volume for statistical significance
- Alternative: maintain an "inner-circle" of users for direct feedback/vibe checks
- **Always ask "How did you find out about us?"** - know which channels work

### Pricing
- Too high → churn from high expectations, or dead signups
- Too low → difficult customers who demand everything for $9
- Refund difficult customers, raise prices, move on
- **Never give away "unlimited" anything** - whales will exploit it
- Lifetime deals attract users expecting custom features for $100 one-time

### Technical Decisions
- Ship first, worry about scale later - embarrassment from incomplete UI beats building unused features
- Early users expect rough edges (especially with unpolished landing pages)
- Have an early-access program for opt-in beta users as product matures
- **Rate limit paid APIs** - protect yourself from unexpected bills

### Mistakes to Avoid
- Building features users suggest but won't use (ship smallest version, measure)
- Putting everything on one landing page - break features into separate pages
- Tunnel-visioning on MRR - changes take weeks/months to affect MRR
- Find other success metrics (images generated, form completions, etc.)

### Marketing Reality
- Competitors don't really matter - lack of awareness is the real competitor
- Increasing traffic is slow (months/years of consistent content)
- Changing what current traffic does is fast and entirely in your control

## Recommended Reading
1. The Mom Test - Rob Fitzpatrick
2. Deploy Empathy - Michele Hansen
3. Badass: Making Users Awesome - Kathy Sierra
4. The SaaS Playbook - Rob Walling

## Platform Work vs Problem-Solving
Less than half of programming time goes to the actual problem being solved. The rest is SaaS platform infrastructure:
- Authentication & user management
- Trials & onboarding
- Database jobs
- Team & invoice management
- Lifecycle emails

Outsource where comfortable (Stripe for payments), but expect to build much yourself.

## Lifestyle Business Advice (HN Thread)

From a founder running LibHunt & SaaSHub:

### Technical Independence
- **Learn software development** - dependency on engineers makes lifestyle businesses much harder
- Being able to build and iterate yourself is key to staying independent

### Framework Choice
- **Use Rails or Django** - battle-tested, stable, well-documented
- Avoid JS framework complexity for lifestyle businesses
- Phoenix/Elixir is excellent but requires more expertise - not worth it for getting started
- Simplicity and speed-to-ship beats technical sophistication

### Community
- **IndieHackers** - recommended for inspiration and shared experience
- Networking with others on same path provides support and practical insights
