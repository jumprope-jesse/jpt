---
type: link
source: notion
url: https://www.astralcodexten.com/p/h5n1-much-more-than-you-wanted-to
notion_type: Tech Deep Dive
tags: ['Running']
created: 2025-01-01T18:58:00.000Z
---

# H5N1: Much More Than You Wanted To Know

## Content (from Notion)

What is the H5N1 bird flu? Will it cause the next big pandemic? If so, how bad would that pandemic be?

### Wait, What Even Is Flu?

Flu is a disease caused by a family of related influenza viruses. Pandemic flu is always caused by the influenza A virus. Influenza A has two surface antigen proteins, hemagglutinin (18 flavors) and neuraminidase (11 flavors). A particular flu strain is named after which flavors of these two proteins it has - for example, H3N2, or H5N1.

Influenza A evolved in birds, and stayed there for at least thousands of years. It crossed to humans later, maybe during historic times - different sources give suggest dates as early as 500 BC or as late as 1500 AD. It probably crossed over multiple times. Maybe it died out in humans after some crossovers, stuck around in birds, and crossed over from birds to humans again later.

During historic times, the flu has followed a pattern of big pandemics once every few decades, plus small seasonal epidemics each winter. The big pandemics happen when a new strain of flu crosses from animals into humans. Then the new strain sticks around, undergoes normal gradual mutation, and once a year immune response decays enough / mutations accumulate enough to cause another small seasonal epidemic (Why is this synced to the calendar year? See here for more).

The severity of any given flu epidemic depends both on the innate severity of the virus, and on how closely the human population’s circulating flu antibodies match the epidemic strain. People usually have good antibodies to the seasonal flu, because it’s only slightly different from last year’s seasonal flu. For the big new animal crossovers, the level of protection provided by existing antibodies is unpredictable. Older people may have antibodies left over from the last time that particular flu crossed over from animals to humans; younger people probably won’t. In some cases, people’s immune systems will be permanently synced to the first flu they encounter, with less protection against subsequent versions.

So for example, the Spanish Flu of 1918 was an H1N1 strain that killed about 2% of the world population. But the exact mortality pattern was surprising; people between 18 and 28 were especially likely to die, and people older than 88 especially likely to survive. Why? Because an H1N1 flu went pandemic in 1830; anyone who first encountered the flu around then had an immune system synced to H1N1. But an H3N8 flu went pandemic between 1890 and 1900; anyone who first encountered the flu then had an immune system synced to that strain and was unprepared for H1N1. See here for the details.

From “Genesis and pathogenesis of the 1918 pandemic H1N1 influenza A virus”, linked above. You may recognize the lead author - Michael Worobey has also been a leading voice on the zoonotic side of the COVID origins debate.

The recent history of the flu, as far as I can tell, is:

1918: An H1N1 flu (“Spanish flu”) jumped from birds to humans in America and killed 50 million people worldwide. This replaced all older strains, so most seasonal flus during this era were H1N1.

1957: An H2N2 flu (“Asian flu”) crossed from birds to humans in China, and killed about 2 million people worldwide. It replaced the H1N1 strain, so most seasonal flus during this era were H2N2.

1968: An H3N2 flu (“Hong Kong flu”) crossed from pigs (?) to humans in Hong Kong, and killed another 2 million people worldwide. It replaced the H2N2 strain, so most seasonal flus during this era were H3N2.

1977: An H1N1 flu (“Russian flu”) leaked from a biology lab (?) in Russia (it might have been a strain from the 1940s, which the Russians were trying to make a vaccine for). It didn’t kill that many people, but it stuck around, and from then on, seasonal flus could be either H3N2 or H1N1.

2009: An H1N1 flu (“Mexican flu” until the PC police stepped in; afterwards “swine flu”) took some horrible circuitous route between birds and pigs and back again, crossed over into humans in Mexico, and killed 200,000 people. It outcompeted older strains of H1N1, but couldn’t crowd out H3N2, so seasonal flus are still either H3N2 or H1N1.

…which brings us to the present, hopefully illuminating why “new flu strain crosses over from animals into humans” is such an “uh oh” moment.

Technically, all pandemic flus start as bird flus.

Influenza A evolved in birds. Sometimes it spreads to other animals, including pigs, cattle, and humans.

The most common way for a bird flu to spread to humans is to “reassort” (not exactly virus sex, but close enough, and the real version is less memorable) with a human flu virus (ie one that has already crossed over to humans). The resulting virus has all of the human flu virus’ human adaptations, but borrows enough new antigens from the bird virus to evade the immune system.

Pigs can be infected by both human and bird viruses, so they are a common place for this reassortment to take place. If reassortment is sort of like viral sex, pigs are sort of like Tinder. When a bird flu and human flu reassort in pigs, the resulting disease is called a swine flu. At least the 2009 flu pandemic was a swine flu, and a minority opinion thinks the 1918 pandemic was too. There aren’t major epidemiological differences between direct-from-bird flus and swine flus.

H5N1 was first noticed in birds - specifically, a flock of chickens in Scotland in 1959 - after which it disappeared for forty years. In 1996, it showed up in geese in China, then gradually increased its market share among birds worldwide. In 2022, it was found in minks; apparently it had learned to infect mammals. By early 2024, it was seen in cows. Now it’s in cow herds in 16 states, and one of them (California) has declared a state of emergency. And in October, H5N1 was found in pigs for the first time.

It’s not uncommon for humans to catch an animal disease. This doesn’t mean the disease has “crossed over” to humans. If the virus isn’t suited to human-to-human transmission, it simply dies off (either before or after killing its human host). Thus, chicken farmers have been reporting scattered H5N1 cases since 1997; now that the virus has spread to cattle, cow farmers have started reporting the same.

A Metaculus comment on this topic introduced me to the phrase “biocomputational surface”. Every viral replication that takes place in a human gives the virus one more chance to develop the set of mutations that makes it human-transmissible and start the next pandemic.

Or, more likely, every viral replication that takes place in a human who has both the H5N1 bird flu and a normal human flu - or in a pig which has both viruses - gives the virus one extra chance to reassort in a way that produces a bird-antigen-fortified human-adapted flu virus.

This doesn’t mean H5N1 will definitely become human-transmissible soon. Many viruses hang out on the borders of transmissibility for decades. Some, for unclear reasons, never cross over at all. But all of this is compatible with the virus becoming transmissible soon. So:

### What Is The Chance Of A Pandemic?

The prediction markets on this topic ask a question about “10,000 cases in the United States”. Does this necessarily mean “pandemic”? Might it be possible to get to 10,000 cases just from the scattered chicken and cow farmers, with no human-to-human transmission? Despite many chicken and cow infections this year, there have only been 60 - 70 recorded human cases. Unless there is a phase change in screening methods, it seems hard for this number to increase to 10,000 off farmers alone. I think it’s fair to treat this question as operationalizing “what is the chance of a pandemic”?

By this definition, Manifold estimates a 40% chance of an H5N1 pandemic in 2025. Metaculus estimates a 5% chance. You can see below whether that’s changed since I wrote this essay:

5% versus 40% is a big difference! Who do we trust?

I trust Metaculus. Metaculus has beaten Manifold in both of the two head-to-head comparisons that I know of (Jeremiah Johnson’s and mine). Manifold’s number swings by a factor of two from week to week; Metaculus has been steady.

But also, Metaculus hosts a CDC-sponsored respiratory disease forecasting tournament which has enriched them in epidemiological expertise. And if you look at the quality of comments on both sites, it’s pretty obvious where the people with more intellectual chops are hanging out. The Manifold comments are mostly single sentences, or occasionally just links to an article about new cases. The Metaculus comments look more like this one by dimaklenchin:

> Despite the panic propaganda, H5N1 is unlikely to be "just a single mutation away from switching host preference":

And Sergio:

> I'm currently at 20% on the question of reported human-to-human transmission of highly pathogenic avian influenza H5N1 globally before 2026. However, this question is only about the US, and is more general about all subtypes of H5. But H5N1 very strongly appears to be the most important subtype to consider in this time period. And, given the current situation in the US with H5N1 human cases derived from exposure to poultry or cattle (with cattle(mammals) being more worrisome), h2h transmission seems quite more likely to arise in North America than elsewhere before 2026.

That’s before 2026. What about longer-term?

Manifold gives a ~50% chance before 2030; Metaculus uses a more complicated method but it says about 25% chance before 2030.

H5N1 may cross to humans, but it could take a while.

Superforecaster Juan Cambeiro at The Institute For Progress estimated a 4% chance of a “worse than COVID” H5N1 pandemic in “the next year”, but their estimate was made in 2023. This seems high to me - Metaculus says 5% total for H5N1 pandemic, and most pandemic flus are not worse than COVID. IFP seem to be expecting a case fatality rate greater than 10%, which I find unlikely for the reasons mentioned above. I trust their estimate less than Metaculus’.

I conclude that the most plausible estimate for the chance of an H5N1 pandemic in the next year is 5%.

Interestingly, 5% is about the base rate for pandemic flus per year: five in the past century = one per twenty years = 5% chance per year. Isn’t it surprising that we’re still at the base rate when we can see a dangerous-looking flu virus spreading through the types of animals that have caused pandemic flus in the past?

Part of the answer is that we’re not - in addition to the 5% chance of H5N1, we have to add the chance of some other pandemic flu. This probably isn’t 5% on its own; scientists monitor flu strains closely, and they haven’t found any others which are giving off as many red flags as H5N1. Still, something could always come out of left field. Maybe we should add a 2.5% chance of some other strain, for a total of 7.5% chance of a flu pandemic (ie beyond normal seasonal flu) next year.

But still, isn’t it surprising that we’re so close to the base rate? One way to think about this: the base rate represents how concerned we should be if there was no epidemiological monitoring at all. In that case, we would estimate a probability distribution across different epidemiological landscapes, most of which contain some concerning-looking flu strains. Since we are doing the epidemiological monitoring, we can collapse that distribution into a single picture: one flu strain, H5N1, is in fact pretty concerning, and other strains mostly aren’t. This is enough to move our prior from 5% to 7.5%, but no more.

The forecasters I talked to raised one other point of uncertainty: does the flu work more like a dice roll, or like a bus? Dice rolls are uncorrelated with their predecessors; even if it’s been a hundred rolls since you last rolled a 6, your chance this time is still 1/6. But buses come at fixed intervals; if the buses are hourly, and you haven’t seen a bus in the past 59 minutes, then your chance of seeing a bus in the next minute is very high. It’s been 16 years since the last flu pandemic; these pandemics come (on average) every 20 years. I don’t think anyone has a good sense of how to think about this. But it was 40 years between the Spanish and Hong Kong flus, so the twenty year number is at best a rule of thumb.

The 5% number feels very low to me (and, apparently, to the average Manifold forecaster). Isn’t H5N1 spreading to cows and pigs and all sorts of other mammals? Isn’t it in the news all the time? I trust Metaculus a lot, but I agree that this is a surprising update, and I’m taking it on faith rather than feeling it in my bones.

### What Would The Fatality Rate Be For An H5N1 Pandemic?

There are four basic stories you could tell about likely H5N1 mortality.

First, maybe mortality would be 50%. The argument here is that official statistics report this mortality rate in the chicken farmers who have been infected with H5N1 so far. Several news sources and even some scientists have raised the specter of a pandemic version of H5N1 pandemic with this same death rate, which could kill a quarter to a third of the world population. THIS IS EXTREMELY FAKE. The official statistics only report fatality rate in the infections we know about. Bird flu is rare, there’s no mass testing, and we only learn that somebody had it if they’re in a hospital and the doctors are worried enough to test for rare conditions. Of Americans who got bird flu in the past year, 0 out of 61 have died. Probably this is mostly because America upped its detection game and is now finding milder cases; we also can’t rule out the virus mutating to become less virulent. Metaculus estimates the current true mortality rate as 1.25%.

…but leaves a wide 90% confidence interval, from 0.5% to 7%.

Second, maybe mortality would be somewhere around 1.25%. The argument here is that Metaculus uses this as its central estimate of US mortality. But Sentinel discusses some reasons to be skeptical of broad inferences from the US numbers:

> Scientists have been puzzled by the apparently low H5N1 case fatality rate in humans in the US. They offer a number of hypotheses:

Third, maybe mortality would be between 0.01% and 0.2%. The argument here is looking at normal (ie not 1918) flu pandemics of the past century. The least bad among these, the 2009 swine flu, had CFR of 0.01%. The worst, Hong Kong flu, was somewhere around 0.2%. If H5N1 is a normal pandemic flu - and right now there’s not much that differentiates it - it will probably be somewhere in that range.

Source: https://en.wikipedia.org/wiki/Spanish_flu#Comparison_with_other_pandemics

Fourth, maybe mortality will be 2-10%. This was the mortality rate of the 1918 Spanish Flu. It seems to be an outlier: as far as we know, no other flu in the past 500 years was nearly as bad (I’m using 500 years as a somewhat arbitrary cutoff since the 1510 flu is one of the better attested historical flus; before that they all sort of dissolve into general plagues) . If there have been ~25 major flu pandemics during that time, that gives us a base rate of only 4% for any given flu pandemic reaching that level of severity. But some people argue that H5N1 is unusually similar to the Spanish Flu, in that both diseases cause “cytokine storm” - a dangerous immune over-reaction which caused a majority of the deaths in 1918. On the other hand, this might be because H5N1 isn’t adapted to humans yet - less adapted viruses usually cause more immune reaction than better-adapted ones. It’s not clear whether this feature would stick around in a pandemic version of H5N1. At least improved medical technology (and lack of a World War screwing things up) probably mean that a virus which was just as severe as 1918 will cause fewer deaths than the 1918 virus did.

Much of this discussion hinges on whether we should expect flus to generally become less virulent when adapting to humans and going pandemic. There’s a hand-wavey evolutionary argument that they should: pathogens don’t “want” to kill (or incapacitate) their host before they can spread. But the biologists I talked to said people tend to overupdate on this, that evolution can do lots of weird things, and that the 1918 flu forgot to read the Evolutionary Virology textbook and actually mutated to get worse. There may be a slight tendency for things vaguely like this to happen, but we shouldn’t count on them.

After reading the arguments from each camp and talking them over with superforecasters, I think, regarding the infection fatality rate of a future H5N1 pandemic:

- 30% chance it’s about as bad as a normal seasonal flu
- 63% chance it’s between 2 - 10x as bad (eg the Hong Kong Flu of 1968)
- 6% chance it’s between 10 and 100x as bad (eg the Spanish Flu of 1918)
- <1% chance it’s more than 100x as bad (unprecedented)
If you multiply the 5% chance of an H5N1 pandemic per year by the 7% chance of severity ≥ Spanish Flu, you get an 0.35% of a Spanish Flu level pandemic this year - one in three hundred. That’s a little higher than base rates - the last pandemic as bad as Spanish flu was smallpox hitting the Indians circa 1500. If we don’t count that one (where would our conquistador equivalents come from?), then the last equally bad pandemic was the Black Death in the 1300s. So we seem to get that level of pandemic once every 500 - 1000 years; a 1/300 chance suggests a 2-3x elevated risk.

The Spanish Flu killed about 50 million people. A second Spanish flu could kill more people (because the population is higher), or fewer people (because medical care is better). If we assume those two cancel out, and that a second Spanish flu’s death toll would also be 50 million, then a 1/300 chance of 50 million deaths = 166,666 deaths. In some weird probabilistic expected utility way, about as many people will probably die of H5N1 next year as died in the past year of the Ukraine War. You will have to decide whether this is a reasonable way to allocate mental real estate to different catastrophes.

### Other Considerations

Even if H5N1 doesn’t go pandemic in humans for a while, it is already pandemic in many birds including chickens, getting there in cows, and possibly gearing up to get there in pigs. This will have economic repercussions for farmers and meat-eaters.

The CDC and various other epidemiological groups have raised the alarm about drinking raw milk while H5N1 is epidemic in cows. There is an obvious biological pathway by which the virus could get into raw milk and be dangerous, but I haven’t seen anyone quantify the risk level. Epidemiologists hate raw milk, think there is never any reason to drink it, and will announce that risks > benefits if the risk is greater than zero. I don’t know if the risk level is at a point where people who like raw milk should avoid it. Everyone says that pasteurized milk (all normal milk; your milk is pasteurized unless you get it from special hippie stores) is safe.

There are already H5N1 vaccines for both chickens and humans; pharma companies are working hard on cows. First World governments have been stockpiling human vaccines just in case, but have so far accumulated enough for only a few percent of the population. If H5N1 goes pandemic, it will probably be because it mutated or reassorted, and current vaccines may not work against the new pandemic strain.

Some people have suggestions for how to prepare for a possible pandemic, but none of them are very surprising: stockpile medications, stockpile vaccines, stockpile protective equipment. The only one that got so much as a “huh” out of me was Institute for Progress’ suggestion to buy out mink farms. Minks are even worse than pigs in their tendency to get infected with lots of different animal and human viruses; they are exceptionally likely to be a source of new zoonotic pandemics. Mink are farmed for their fur, but there aren’t as many New York City heiresses wearing mink coats as there used to be, and the entire US mink industry only makes $80 million/year. We probably lose more than $80 million/year in expectation from mink-related pandemics, so maybe we should just shut them down, the same way we tell the Chinese to shut down wet markets in bat-infested areas.

ACX grantee One Day Sooner is trying to help the FDA get more resources for Operation Warp Speed style pushes that could expedite approval of pandemic-related vaccines. ACX grantee Duncan Purvis is trying to improve existing influenza vaccines in ways that could make them more effective. ACX grantee Blueprint Biosecurity is working on pan-viral suppression techniques.

### Conclusions / Predictions

All discussed earlier in the piece, but putting them here for easy reference - see above for justifications and qualifications.

1. H5N1 is already pandemic in birds and cows and will likely continue to increase the price of meat and milk.
1. 5% chance that H5N1 starts a sustained pandemic in humans in the next year.
1. 50% chance that H5N1 starts a sustained pandemic in humans in the next twenty years, assuming no dramatic changes to the world (eg human extinction) during that time.
1. If H5N1 does start a sustained pandemic in the next few years, 30% chance it’s about as bad as a normal seasonal flu, 63% chance it’s between 2 - 10x as bad (eg Asian Flu), 6% chance it’s between 10 - 100x as bad (eg Spanish flu), and <1% chance it’s >100x as bad (unprecedented). The 1% chance is Outside View based on other people’s claims, and I don’t really understand how this could happen.
Thanks to Nuño Sempere and Sentinel for help and clarification. Sentinel is an organization that forecasts and responds to global catastrophes; you can find their updates, including on H5N1, here. As usual, any errors are mine alone.


