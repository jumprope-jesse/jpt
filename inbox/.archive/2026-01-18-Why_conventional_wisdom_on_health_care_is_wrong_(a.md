---
type: link
source: notion
url: https://randomcriticalanalysis.com/why-conventional-wisdom-on-health-care-is-wrong-a-primer/
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-11-28T04:20:00.000Z
---

# Why conventional wisdom on health care is wrong (a primer) – Random Critical Analysis

## Content (from Notion)

This is a short condensed summary of key facts and relevant evidence I have discovered in my extensive research on healthcare. Conventional wisdom on healthcare is far from the mark, both in general and specifically as pertains to the United States. I have written several lengthy blog posts over several years in which I have reviewed the evidence in painstaking detail. Still, many people lack the time, interest, or attention span to fully absorb, and much of the information necessary to understand the big picture is spread across several pages. If you want to see further substantiation, please click through as I’m mostly focused on covering the highlights in relatively broad strokes.

Note (1): There are some new content and analysis on this page, but mostly I am aiming to summarize evidence I have already assembled and published on my blog.

Note (2): I have made extensive use of log-log plots in this post wherein the value displayed on the x-axis and the y-axis have been (natural) log-transformed. Although these types of transformations are bog-standard in economics, these are particularly useful here since I am trying to rapidly convey a bunch of statistical relationships and quantify their relative contributions. In case you’re not already aware, these slopes can be readily interpreted in percentage terms.

For example, the slope in the health expenditure-income plot below implies that a 1% increase in underlying value on the x-axis (income) predicts a 1.8% increase in value on the y-axis (health spending).

## Health spending is determined by income

Health spending is overwhelmingly determined by the average real income enjoyed by nations’ residents in the long run. The income elasticity of health expenditure is also extremely high at a national level — the health share rises rapidly with incomes. This can be plainly seen in OECD cross-sectional data.

We can also see this in a broader array of countries using a comprehensive measure of consumption, Actual Individual Consumption (AIC), which is a strong proxy for our income measure.

US health spending is well explained by these better, more comprehensive measures of income and consumption, i.e., the “household perspective,” since this better reflects the real purchasing power of a nations’ residents. This runs contrary to conventional wisdom because GDP has historically been used as a proxy for this concept. However, it is clear that:

1. It measures something different (results can be systematically different)
1. GDP is a much weaker predictor of health spending
1. It is also a much weaker predictor of virtually all other socially relevant metrics that we’d expect to be associated with prosperity (especially health measures)
GDP still has its place, and it still correlates with the household perspective. Still, the theoretical and empirical basis for using measures of the household perspective in applications like this is overwhelming. The OECD, World Bank (ICP), and other international data-gather organizations have been making measurement invariant statistics like these available for some time, so there’s not much reason to use GDP at this point.

## Income predicts changes in health expenditure

Comparable results are found in national time-series data. When real income changes, health spending responds in a manner that is consistent with cross-sectional results. Likely due to the large and growing role of third-party payment and an increasingly large, complex health system, the response in the same period has typically been negligible over the past several decades. It takes 3-4 years for payers and for providers to completely respond through reimbursement policy, premiums, services offered, and so on. Still, the strength of the long-run relationship is nonetheless readily apparent in the US time series.

Comparable results are obtained in OECD data with similar household income measures.

Amongst the high-income countries for which we have useful data, reverse causation is unlikely because changes in household income and consumption precede changes in health spending. It is very unlikely health spending somehow mechanically, artificially inflates observed household income levels or that the effects of health spending on health are so significant and transmitted so strongly to income levels amongst developed countries as to have substantial and consistent effects on this order.

## Causally-identified estimates are not per se incompatible with these national effects

Some economists do not like this sort of straight-forward analysis even though it’s supported by multiple lines of evidence and even though they lack a good working theory for what might confound these relationships. They want better causal identification. While it’d be nice to have additional evidence of this sort, high-quality studies that can directly address this argument are hard to come by because (1) these are national-level effects and (2) changes in income take several years to be reflected in changes in health spending due to well-known multi-year lags.

Expand for an explanation from CMS/HHS

Several economists have used instrumental variable estimates of the income shocks on health spending to argue the true causal effect is substantially below unity (income-elasticity less than one). Some of these estimates (e.g., oil shock) are credible insofar as they are likely to accurately measure the causal effects of income on health spending that play out at the regional level, especially in the short-run.1 However, this regional approach represents a substantially different unit of analysis. The effects of market income within any given region are likely to substantially leak out via taxes & transfers, employers, health insurers, hospital systems, and other intermediaries whose budgets and regulatory mechanisms are not neatly contained within any particular region. Furthermore, relative prices are also apt to screw up extrapolations from regional effects.

Expand for a fuller explanation of leakages and relative prices

Perhaps most importantly, these causally identified estimates are very much in the same ballpark as traditional OLS-style estimates of regional income effects. For example, while the central estimate derived from the famous oil shock study found local income effects of 0.72 (+/- SE of .21), the OLS estimates aren’t appreciably different.

source

Indeed, that credible causal (IV) estimates are indistinguishable from more conventional estimates (e.g., OLS) at comparable units of observation (regional) should give us more confidence that the income signal we detect with more straightforward techniques is not being severely confounded by lurking variables that we’re not controlling for. If there’s no evidence of significant confounding regionally, this might give us more confidence that the national estimates aren’t severely confounded either (particularly if obvious theorized confounds like age structure or disease burden, not to mention proxies for this like office visits, inpatient discharges, and bed-days, fail to correlate significantly with income levels nationally, which actually does robustly predict spending).

## The rising health share explained by rising quantities per capita (not prices!)

Well-measured, broadly representative health care prices have increased less quickly than GDP per capita and other broad income measures according to reliable domestic price measures, namely, the BEA’s PCE health care price index and CMS’s PHC price index.

source

This may come as a surprise to people familiar with charts like those popularized by Mark Perry of AEI.

These charts use BLS’s CPI health price indexes, which imply substantially more inflation. However, these indexes are not designed for this purpose, and they are not deemed to be reliable indicators of overall healthcare prices.2. Nominal incomes also nearly doubled in this period, so even if we take the CPI medical services component as a decent indicator of overall health prices3, the rising health share cannot be explained as primarily a price-driven phenomenon (particularly with newer, preferred CPI chain-price indexes).

If we want to assess the degree to which prices contribute to the rise in health spending relative to income, we should assess prices relative to income. Nominal rates of health inflation are difficult to interpret and compare without reference to income levels because much inflation is a monetary phenomenon and because some sectors are inherently more subject to productivity growth than others. Baumol’s effect implies we should expect real prices to rise unless productivity growth exceeds the rate of growth in prevailing wages in the sector (which correlates with rising overall income levels). However, none of this implies we should expect health prices to rise faster than income.  As Scott Alexander framed it:

> “The Baumol effect cannot make things genuinely less affordable for society, because society is more productive and can afford more stuff.”

That reliable health care prices have truly failed to keep pace with income growth suggests some combination of genuine productivity gains, slower than average compensation growth, or slower growth in operating surplus (profits) in healthcare.

source

## America spends much more because it consumes much more

While real prices for health care are higher in rich countries4, the price of healthcare does not rise as quickly as average incomes. We can see this by comparing relative prices in each country5 as it relates to their real income levels. Relative prices give us a reasonable sense of the opportunity cost to consume a comparable amount of healthcare spatially6, which we can then compare to real income levels7.

Comparable results are obtained with GDP as the reference.

This data shows us that the relative price of healthcare rises with real income levels. In lower-income countries, the same bundle of healthcare costs significantly less in real terms.8. However, real incomes are also much lower in lower-income countries. Relative to the resources available to the average resident of those countries, it’s not necessarily any cheaper. Indeed, the statistical evidence suggests health prices fall in relation to income as real incomes rise.9

As real incomes rise, the relative price of goods falls while the relative price of services increases. This is likely a consequence rich countries increasing productivity in goods substantially more rapidly than that of services10. Alternatively, high-income countries can use their higher real purchasing power to buy tradable goods from countries with lower real labor costs.

Because “services” tend to be driven by domestic labor costs and because their productivity growth typically is not as rapid, the real quantity of services consumed is somewhat less than adjustment for overall price levels (PPPs) for GDP or AIC would suggest. Nonetheless, the reliable price indexes make clear that rich countries consume much more healthcare in real terms, and the United States is no exception to the rule,

source

## The claim that US health care prices are inexplicably high was never well-evidenced!

Save perhaps for comparisons of pharmaceutical prices11, the prices typically proffered to compare the general price level of health care across countries are not up to the task. Such comparisons are non-trivial because countries rely on different schemes to provide care, to pay for care, and provide different types of care for roughly similar conditions.12 Substantial time and attention must be paid to these issues to obtain measurement invariant prices. Clearly, this is best done with the cooperation of national health authorities to ensure the types of prices are sufficiently representative and properly weighted.

The prices produced by the OECD’s recent health PPP benchmarks13 are probably the only methodologically credible price estimates. Their estimates (output) also appear to be quite credible. Unfortunately, their work has only rarely been cited to date. Instead, what we find are a large number of citations to prices published by an otherwise little known payer trade group, International Federation of Health Plans (IFHP), whose work on this topic14 has seemingly appeared whenever healthcare reform on the table politically. Surprisingly, their work has been accepted by many uncritically.15 Though their methods and data sources are insufficiently transparent, the details they do provide makes it quite apparent that their data cannot be relied upon.

Besides the critical identifiable methodological problems, their prices for surgical procedures, probably their most cited price category, are not credible. For example, while OECD hospital services price estimates (inpatient procedures) are strongly associated with income levels, with real prices rising at least as rapidly as real incomes, none of the “median” prices IFHP reports are even positively correlated with income levels.

That we are unable to detect the signal in IFHP’s data, which more robust price methodologies and theory tell us to expect, should be concerning. This goes doubly when the price-income slope is in the wrong direction for every single procedure.16 By contrast, when we look at price estimates for specific procedures in the associated working papers, we can easily see that prices for inpatient procedures are robustly correlated with income levels and that the prices rise roughly the same rate as income on average.

## The cost savings of Ambulatory Surgery Centers are real but do not prove as much as many believe.

Russ Roberts of EconTalk recently had the founder of the Surgery Center of Oklahoma on his show, wherein the guest touted the cost savings of his business. I am a fan of the show, and I support these sorts of developments, but since some people have taken this as proof that American hospitals are uniquely broken, I’d like to push back on this a little and put it in context.

Note: This is long, and it’s a bit of a tangent, so I’ve put it in a collapsible dialog to save those not interested from needing to scroll.

Expand for a long explanation

## Real health inputs (labor) increase rapidly with income levels

The density of health workers rises rapidly with incomes.

Health care also commands an increasingly large fraction of the workforce.

These Human Health Activities data are derived from SNA (National Accounts), as opposed to SHA (Health Accounts). These health activities are comprised entirely of hospitals and providers’ offices. It excludes things like pharmacies, insurance companies, drug and device manufacturers, and assorted middlemen.24. The vast majority of health expenditures flow to (through) these organizations and most of that which does go to meeting payroll within these same organizations:

> “It is not surprising that employment growth should be a bellwether for rising health care expenditures because salaries and wages account for an average 55% of operating expenses for hospitals, physician offices, and outpatient care, and nearly 70% of hospital expenses”

Even Ezekiel Emanuel has recently seen a little light on this issue:

> “Because health care is so labor-intensive, wages to workers are the real reason it costs so much. Wages explain why hospitals are so expensive: They are filled with workers.”

Ezekiel is not wrong on the fundamental domestic arithmetic: health spending and health employment are linked at the hip in the long run.

The health share of the workforce has increased about six-fold (!!!) since 1950.

We also find help health employment explains much between states (while prices explain very little).

source

The rapid increase in health employment argues quite strongly against several conventional narratives on the causes of high costs, and it lends further support to the notion that the rise is real (quantities per capita). Much the same goes for the United States relative to other high-income countries. Claims to the contrary, such as those from this highly influential famous paper, are at odds with the reliable price and quantity measures, and they are just plain wrong vis-a-vis inputs.

> “Because the US is still not devoting more real resources to medical care than the typical OECD country, we believe that the conclusion that “it’s the prices, stupid” remains valid.”

All of our extra health workers must be doing something and, if nothing else, they sure as hell demand to get paid. The rapid increase in health employment dramatically reduces the scope for high wage rates, profits, value-add, and economic rent to explain much. Every dollar paid out by physicians’ offices and hospitals for staff, and intermediate goods is a dollar not going in the pockets of physicians, hospital executives, and other assorted boogeymen.

## High overall wage rates and profit margins cannot explain much.

Many people have latched onto unreliable price estimates, along with a smattering of poorly characterized facts, to arrive at the notion that healthcare wages and profits are unusually high in the United States and that the cause of our increasing healthcare costs is somehow primarily attributable to increases in these figures. The implicit message is that the high-incomes earned by physicians, hospital executives, and other powerful actors drive spending and that we are going to be able to dramatically slash costs by reducing their income:

> “Because of America’s high prices, there is a $3.5 trillion industry invested in the status quo. Cutting prices, whether through global budgets or price-setting or other rules, means cutting income for health care providers.”

Undergirding this is the notion that we are likely to get something for nothing: that we can spend much less while still getting at least the same quantity and quality of healthcare Americans have come to expect. This just isn’t plausible.

If anyone actually bothers to check, it’s readily apparent that average compensation in healthcare in unexceptional and that it has not increased for decades.25

Average compensation may have increased decades ago, but this stopped around 1990. That increase can be attributed primarily to rising wages for nurses, who were initially poorly paid and whose training has increased relative to the population, along with increased nursing staffing ratios.26 similar changes likely played out in other countries for similar reasons.27

In any event, this average includes physicians, nurses, technicians, administrators, assistants, housekeepers, food services workers, and much, much more. The high and rising spending in this sector as a share in income clearly cannot be explained by high and rising compensation, but rather the high and rising density of these workers. Some of these occupational groups may earn relatively high-incomes (e.g., physicians), but then there must be many more earning relatively low-to-middling incomes.

Lest you believe the “profits” of providers’ offices and hospitals are what distinguish this sector, we can quickly dispense with this notion by comparing their profits to those other sectors.

Likewise, we can compare the net operating surplus (~=earnings) as a share of output (~=receipts) in human health activities (providers’ offices and hospitals) to that of other countries.

We can also compare their gross-value-added share.

This implies American health services compensation and profit share of receipts are actually somewhat below average.28 If US prices are (presumably) inexplicably high because providers were making out like bandits with exceptionally high margins, I’d expect to find some evidence of this in one or both indicators.

Similarly, null results are found when GVA is broken out on a per-worker basis (a proxy for real inputs).

Likewise, if we just focus on the labor compensation component.

You may also notice that the elasticity of GVA and CoE per health activities worker is substantially less than one, which implies that rising income per health services worker cannot arithmetically explain the observed health increase in health spending. That is, real incomes are rising faster than the rate at which we are increasing the real incomes of physicians’ offices and hospitals on a per head basis.29

Again, health spending is rising in the United States, as in other rich countries, because we are putting a lot more real resources into healthcare as real incomes rise, both as a share of the population and as a share of total employment. If we simply divide the oft-cited health spending statistic by total employment amongst hospitals and providers’ offices, it’s readily apparent their employment growth explains much.

This numerator (SHA current health expenditures) includes retail pharmaceuticals, medical devices, insurance/administration, and much more, whereas the denominator just reflects people that work directly in hospitals and providers’ offices. Real incomes are rising faster than real expenditures per employee in cross-section, ergo the denominator (health services workers) must be growing significantly more rapidly than overall health spending. This is a good indication the observed excess cost growth is unlikely to be explained by the combined increases in wage rates, profit margins, health insurance, drugs, devices, and the like over and above general economic growth. All of these extra workers in hospitals and providers’ offices demand to get paid at rates that approximately reflect the prevailing real wage in each country.

America is distinguished primarily by the sheer quantity of resources it puts into healthcare.30

## Physician take-home pay explains even less

Few would dispute the total earned income of physicians is high relative to the average worker, much of which follows from their relatively higher skills, education, training, and responsibilities.

Most importantly, for comparative purposes, their relative income has long been high in the United States and other developed countries. To appreciably explain the relative increase in health spending31, relative physician incomes must have grown tremendously, and they must be much higher than presumably “comparable” countries. The best available evidence suggests physician incomes have not increased appreciably in relative terms.32

source

There is not much sign of a trend here, and the increase is really quite modest (especially given likely compositional changes within and between specialties)33 These data are generally consistent with most other reasonably credible data sources.34

It’s also worth noting that there appears to be even less evidence of change when physicians are compared to the 90th percentile of all workers in the United States.

source

To the extent the modest apparent change is a product of broader macro-economic forces driving inequality higher, such as skills-based technological change or globalization, it indicates (1) the cause lies outside of health policy and (2) there are likely to be some offsetting effects vis-a-vis relatively cheaper wages elsewhere within healthcare.35

Physicians, particularly specialists, earn multiples of the average wage in most high-income countries.

source

These multiples are not too far away from multiples reported for the United States in 2003 for self-employed specialists (5.5x) and self-employed GPs (3.4x).36 This puts the estimated relative wage of American physicians within 20-30 percentage points of many high-income countries (less than some), and there are good reasons to believe the lower multiples reported for some countries are significant under-estimates37. Given that physicians account for roughly 5% of the health services employment in the United States and their total take-home pay perhaps eight-to-ten of percent of health spending, such differences simply cannot explain more than a tiny fraction of aggregate costs or relative prices.

When viewed from the perspective of the national income distribution, these differences appear to be even less impressive.

data source

When it comes to the viability of pay-setting practices, and the associated tradeoffs, relative wages of this sort are apt to be much more instructive than absolute comparisons.38

Regardless, differences in the national wage dispersion and returns to skill are likely to cut both ways: relatively higher wages for physicians are likely offset by relatively lower wages elsewhere within healthcare. There is no fundamental reason why relatively high wages for physicians mean price-to-income ratios must be higher than other countries as health prices are ultimately determined by much more than the cost of this one category of input.39

## The composition of the American health workforce is consistent with trends observed elsewhere.

While the density of physicians in America increased significantly over the past several decades, it’s likely much of this was due to technological changes within health care as opposed to independent income effects.40 When we look cross-sectionally, it’s quite evident that physician density is highly idiosyncratic. There is not an obvious statistically significant relationship between physician density and income levels or health spending.

Part of this may be due to differences in scope of practice laws and productivity. For example, it seems the United States has long had significantly more nurse practitioners in primary care roles. What is clear, however, is that the physician share of the health workforce tends to decline rapidly with income levels.

Put simply, non-physician occupational categories have clearly risen much, much more rapidly in the United States and other high-income countries. This hiring seems to be primarily through occupational categories such as nurses, personal care workers, physiotherapists, and others.41

Since hospital staffing (administration) has received much attention in America, it’s notable that the density of non-healthcare hospital staff rises sharply with income levels.42

People assume the growth in “administrators” is a uniquely American problem. Still, it’s very likely to be explained by inherent increases in complexity of healthcare, which is ultimately determined by income levels, and to a lesser degree, by definitional issues.43

## Commonly proffered utilization indicators do not show what people believe.

Even if one wants to summarily dismiss all of the other reliable evidence concerning the United States44, it makes no sense to use a handful of utilization measures (proxies for overall volume) of unknown validity to argue prices must be inexplicably high simply because these indicators are not as high as we would implicitly expect given what we are spending on healthcare. There must at least be a compelling relationship with health spending and a significant residual for the United States for this to count as meaningful evidence.

One should not just assume a 1:1 relationship exists for any and all indicators. If there is no apparent relationship, and if America is reasonably close to the trend (or lack thereof), there can be no meaningful residual to explain vis-a-vis implicit quantities. Even when there are unambiguous statistically significant relationships, the US residuals must be substantial and in the “wrong” direction (typically lower volumes) for this to rise to the level of compelling evidence. These data genuinely do not make their case.

To take a recent widely cited, representative example45:

> “Similar to previous work by Garber and Skinner, Reinhardt et al, and Anderson et al, that examined US health care spending relative to other OECD countries, we found that the United States spent significantly more on health care despite having similar levels of utilization“

source

The problem with this particular analysis is that observed US behavior in these utilization indicators are mostly very consistent with its spending levels. America’s position is directly proportional to the direction of the relationship and the strength of the relationship between the indicator and health spending.

The US is unexceptional in those indicators that are not robustly correlated with higher health spending.

Conversely, when we look at indicators where America skews high, these are precisely the sorts of things high-income, high-spending countries like the United States do relatively more of. Indeed, a fuller accounting of the procedures would likely push the United States somewhat higher still.46 Although there is some idiosyncratic variation, and the US is sometimes slightly below trend, the United States is not the outlier they need to make this argument47. There are no smoking guns to be had here.

FYI-Even though America’s rank in angioplasty (PCI) procedures is not notably low here, this picture would have looked quite a bit different just a few years before (new clinical evidence changed behavior)48

The results for the comparable data indicate the United States also performs at least as many cataract procedures as its health spending would predict.49

Cataract procedures

Cesarean section procedures

Of the procedures listed, only hysterectomy shows any signs of a potentially significant residual away from that which would be (weakly) predicted by health spending, but this is likely explained by evolving preferences and technological change (ambulatory procedures in particular)

Higher-income, higher-spending countries are, if anything, associated with shorter hospital stays and are clearly trending towards shorter stays in the long run!

Presumably, the United States inexplicably uses vastly more imaging technology than other developed countries, but mostly these track with income and spending levels.

In short, none of the selected “utilization” indicators published by Papanicolas et al. make a compelling case that the United States does appreciably less than that would be predicted by its level of expenditure.

Indeed, there is a decent case to be made that US utilization is, on balance, consistent with even more developed healthcare systems.50

If we look at some other oft-cited indicators, which Papanicolas et al. also cite, we find similarly weak relationships. For example, office visits just don’t correlate significantly.51

Likewise, hospital discharge rates (all causes) don’t obviously correlate with spending either.

This should not be entirely surprising for the United States, at least since hospital revenues and procedures have been shifting rapidly to outpatient settings for many years.

For many categories of procedures and treatments, due to the rise of minimally-invasive technology and other factors, inpatient admittance has ceased to be a reliable proxy for health system activity. This wasn’t always the case. For example, if we revisit the same indicators the paper above cited for 1996, we find results consistent with high-income elasticity52 whereas fourteen years later, there is barely any slope to be found, and the variance explained is trivial.

The problem with this whole enterprise is that the constant change in the technological frontier is likely to badly confound attempts to infer the volume of health system activity from observed utilization rates from lagging (obsolete) indicators of technological progress. Demand for specific technology is finite, relative prices fall, and real incomes rise. Consequently, observed utilization in lower-income countries rises while it stalls in rich countries. By the time these indicators are published by international authorities, and “recent” snapshots of them are cited, wealth (health spending) has often ceased to be a significant determinant of the variance.53

We can see this pattern unfolding with MRI exams in OECD panel data.

Extensive use of MRIs in healthcare is a relatively recent development, but it is still likely we won’t find much of an income or health spending signal here in a few more years.

## Better technological indicators are required to fully capture rising volumes through proxy measures

Technological change is fundamental because these innovations drive costs even when we have trouble identifying them in the available cross-sectional evidence. Yes, income is the ultimate (distal) cause of health spending, and itself explains almost everything, in the long run. Still, the primary proximate cause of excess spending growth is the adoption of technological change.54

I am hardly alone in emphasizing technological change. Most health economists have too. Even when these economists’ conceptual models explicitly treat income, insurance, relative medical price inflation, and more as independent variables for explaining the growth in real health spending, they attribute the majority of spending growth to technological change.55

source

Most of the indicators published by OECD and others reflect fairly old technological developments, but there are a handful of indicators here.

For example, we can compare surgical transplant rates.

Likewise, similar results out found for pacemakers.

Likewise for Implantable Cardioverter-Defibrillators (ICDs)

And a variety of fairly expensive medical equipment (imaging/diagnostics):

And insulin infusion pump therapy penetration amongst type I diabetics.

> “Although Western Europe has been well covered by reimbursement for many/several years, including close to or more than 10 years in some countries, it is noticeable that (1) the higher users are still behind the United States and (2) some significant heterogeneity remains about pump penetration among the various countries.”

source

For reference, pump therapy rates in the United States have clearly been substantially higher for longer.

Likewise for ADHD prescriptions (standard units)

There are certainly more data of this sort out there if one cares to look.

Please note that all of these indicators indicate quantity and that the observed income elasticity of demand is very high. As in, a 1% increase in real household income levels (or at least reasonable proxies for it) is often associated with a 1.5-3% increase in the adoption of relatively novel technology. If you further appreciate that these indicators tend to come with at least corresponding increases in labor to deliver this care56 and that these new workers tend to demand wages that approximate the prevailing national wage (Baumol’s effect), it shouldn’t be too difficult to understand how the adoption of this sort of health technology can drive aggregate cost growth.57

While it’s clear there are some idiosyncratic factors and that there is some role for particular reimbursement policies insofar as precisely what gets reimbursed, under what conditions, and how quickly58, it’s nonetheless true that income is the major determinant in the long run. Lower-income, lower-spending countries may occasionally show idiosyncratically high usage and high-income countries low usage, but they rarely do so consistently across categories. At moderately high levels of aggregation, idiosyncratic differences are apt to get averaged out to closely reflect health spending and (ultimately) income levels.

## Beware of false profits (intensity is distinct from price)

Several high profile researchers and advocates have advanced the notion that “prices” explain the increase in spending by estimating the average cost per health system encounter. Typically they call this something like “service price and intensity” in their research papers, but then take calling it “price” when communicating with the public.

Disaggregating the data in this fashion (amongst others) might be analytically useful in some circumstances, but it is not an indicator of price, and it’s very misleading to imply otherwise. It is particularly misleading when the reliable price indexes have failed to find a genuine price signal anywhere near this magnitude, and more detailed studies of similar nature clearly show that what they label “price and intensity” is explained by the intensity component.

When the data of this sort are disaggregated even further, it’s self-evident that (1) hospitals and ambulatory care providers are doing substantially more per encounter, and (2) it is poorly explained by factors like aging and rising disease burdens. The data also typically suggest people are not visiting the doctor that much more often. The data implies the rising health share of income has approximately nothing do with aging, disease burden, increasing propensity to seek care, or prices (over and above income growth). Instead, the data suggest that when people do seek care, much more is apt to be done on their behalf.

All of this is very consistent with the increasing adoption of technological improvements as income levels rise. People are more likely to get diagnosed and treated as average income increases in the long-run, ceteris paribus, and this doesn’t necessarily correlate meaningfully with the rate of encounters.59 To put this in more concrete terms, this primarily plays out through technological changes that allow for better diagnosis and better treatments. In the short run, when viewing granular time series, these changes might appear to be marked by discrete changes as genuine technological innovations in any single area are rarely perfectly continuous, and payer reimbursement policies can change behavior quite suddenly in response to pent up demand. However, when these technological changes aggregated, these stepping issues are bound to dissolve into fairly continuous changes in real expenditure that are converging on some equilibrium, one primarily determined by average income in the long run.

## Income predicts cross-sectional spending because it predicts intensity

That intensity rises sharply with income levels should be reasonably self-evident because (1) we know that income levels are exceptionally linked to health expenditures, both in cross-section and time-series, and (2) there’s no good reason to believe higher-income countries are systematically much older, sicker, or much more likely to seek care. If we actually check the data, we find richer, higher spending countries just are not more likely to visit the doctor, be admitted to hospital (inpatient), or even spend more bed-days in the hospital. Nor are they appreciably older, suffering from much higher rates of diabetes, etcetera, etcetera. We also know health prices are not rising faster than income in the US time series and in international cross-section. Still, health spending clearly rises sharply with real income levels.

If we approach the international data from the perspective of cost per encounter, as others have done for the US to argue “prices,” we can clearly see that “price and intensity” rises very rapidly with income. For example, we can compare the average cost per inpatient discharge with income levels.

Comparable results are obtained for the somewhat narrower curative care subset of inpatient activity (excludes rehabilitative care).

The results for cost per bed-day are comparable — factoring in length-of-stay doesn’t appreciably change these conclusions.

Given that we know for reasonably certain that the price of hospital services is not rising appreciably faster than income, it’s highly likely costs increase above unity (elasticity > 1) can be attributed to intensity rising with income. This is consistent with other lines of evidence on technological change and rising real inputs (worker density) in hospitals and health care writ large. Mostly, much more is being done per hospital inpatient encounter in wealthier countries.60

If we look at the best available data that also includes the United States, it also fits quite nicely on the trend.

Costs likely rise because hospitals in more prosperous countries can and do so much more vis-a-vis cutting edge medical technology (procedures, diagnostics, pharmaceuticals, etc.). Further, as hospital costs rise and as technology gets better, a substantial share of procedures get shifted to ambulatory settings, as in, hospital outpatient departments and alternative ambulatory surgery settings (e.g., ASCs), which moves the composition of hospital inpatient care to more complex cases that require invasive procedures and higher overhead.

Comparable results are obtained for average costs in ambulatory and comparable encounters outside inpatient settings.61

Though the apparent slope (elasticity) likely reflects an underlying truth vis-a-vis costs rising rapidly with technological change (intensity of care), it’s probably less interpretable than the inpatient estimates because the underlying data aren’t as good and numerator and denominator aren’t necessarily quite as well matched. In high-income countries, the cost of these encounters (the numerator) is likely to heavily entail ambulatory surgical procedures, therapies, advanced diagnostics, and much, much more62.

The high health expenditures observed in high-income countries simply can’t be explained based on the frequency of contact with the healthcare system (especially traditional office visits). The average costs per encounter are clearly rising much more rapidly than incomes even though the reliable price evidence does not suggest excess price growth of this nature.

## Rising productivity has consequences (“we ain’t gonna starve”)

The technological-led excess cost growth in health care means that other expenditure categories must fall as a proportion of consumption. A surprising number of people have taken this to mean that health care will eat our entire economy and that we will “starve.” These concerns are surely misplaced as these technological changes, and associated excess cost growth is very much linked to real income growth in the long run, and this growth is clearly not unchecked. The rate of excess cost growth and its relationship to income (ultimately productivity) growth matters

Because productivity is increasing and because excess cost growth eventually follows from this, it’s entirely possible to spend an ever-larger share of income on health without reducing our real consumption elsewhere. Indeed, the apparent rate of real income growth paints a considerably more pessimistic view of the fundamental necessities of life because prices also move relative to each other (which ultimately follows mostly from productivity). As the share of health, education, daycare, and other labor-intensive categories rise, the apparent rate of income growth seems to decline as these areas routinely show much less than average productivity growth, hence price indexes are increasingly weighted towards them. The flip side of this, however, is that the measured productivity growth and price-to-income ratios outside of these few labor-intensive categories are much, much more favorable than would be implied by the apparent average real income growth. Most prices have fallen exceptionally rapidly relative to average income levels within our lifetime.

With the same fraction of average income, we can buy much more of the basic necessities of life. This has consequences for how households choose to allocate their consumption expenditures. This can be clearly seen in the long-run in the share of consumption expenditures allocated to groceries.

The typical American household is much better fed today than in prior generations despite spending a much smaller share of their income on groceries and working fewer hours. I submit this is primarily a direct result of productivity. We can produce food so much more efficiently that we don’t need to prioritize it as we once did. The food productivity dividend, as it were, has been and is being spent on higher-order wants and needs like cutting edge healthcare, higher amenity education, and leisure activities.

Similar patterns have doubtless been playing out in other essential consumption categories.

source

Because the price-to-income ratios are falling so much more rapidly than the health-expenditure-to-income ratios are rising, potential consumption63 has clearly been trending steadily upwards across the vast majority of expenditure categories.

The actual quantities per capita have trended steadily upwards too, although the precise slopes vary some (partially determined by demand).64 So long as the relationship between these ratios don’t fundamentally change this trend can continue on without bending towards metaphorical “starvation.” Indeed, these trends indicate that the rising health share is robustly linked with a generally constant long-term of increasing in real consumption across essentially all other major consumption categories.

Comparable patterns are found with PPP benchmarks in international (OECD) cross-section vis-a-vis potential consumption per capita and health share of income. (You may also observe that the United States, the blue point, has much higher potential consumption after adjustment for purchasing power and that it’s generally very close to trend)

Comparable patterns for potential consumption are observed in virtually all of the more granular categories (save, perhaps, education). Reliable price indexes (PPPs) indeed indicate that rich countries can continue spending larger shares of their income on healthcare and still consume much more of virtually everything else in real terms. While the particular slopes may vary, the quantity per capita indexes are much compatible with this observation.

(likewise in more granular data)

Allocating larger shares of income to cutting edge healthcare clearly comes with tradeoffs, and it’s likely subject to rapidly diminishing returns. Still, there is no fundamental reason why the current trends are inherently unsustainable. Whether people believe this ever more technology-intensive, labor-heavy healthcare is genuinely valuable or feel they need to “show care” for other members of society, it shouldn’t be difficult to understand how real increases in average income can cause even more rapid increases health care spending.

The contribution of real national income and the associated differences in price levels between categories of consumption is likely significantly underestimated. Besides the role of other known factors within developed countries65, which likely diminish the role of individual and regional income are a determinant of spending, the very fact that income at sub-national units of observation are unlikely to correspond to systematic differences in relative prices on nearly the same order is likely to be a significant partial explanation.

## Diminishing returns to spending and worse lifestyle factors explain America’s mediocre health outcomes

America’s mediocre health outcomes can be explained by rapidly diminishing returns to spending and behavioral (lifestyle) risk factors, especially obesity, car accidents, homicide, and (most recently) drug overdose deaths. [Please read this post for the full explanation]

The diminishing returns are evident in cross-sectional analysis. Higher-income countries like Norway and Luxembourg spend twice as much as the likes of Spain and Italy and probably experience worse average outcomes.

Diminishing returns are also evident if we compare trends for countries within the OECD. Countries that were initially closer to the health frontier have seen much slower gains in life expectancy. Whereas life expectancy in Korea increased nearly 20 years, it increased by just 5 years in Sweden in this same period — these things clearly track robustly with the initial state of healthcare as indicated by initial health spending.

Likewise, the least developed parts of the world have converged rapidly on the most developed countries despite little-to-no convergence in income levels, health spending, and the like. Controlling for the change in health spending does not appreciably change these results. The supposedly radically divergent slope observed for the United States in widely circulated plots popularized by “Our World In Data” can be readily explained by distance from the frontier and the change in spending. America’s long-run rate of improvement in outcomes can be readily predicted based on patterns observed in other high-income countries — the US doesn’t even need to be included in the model to obtain such results.

This really just leaves the intercept to be explained. America has never compared favorably conditional on income or health spending — it’s long been about two years below expected life expectancy. As some less developed OECD countries have closed substantial ground in high-efficacy medicine and essential public health measures, they have been able to converge on the outcomes of higher-income countries and even surpass many since they are less encumbered by many of these same lifestyle factors. Cutting edge medicine, like recent advances in cancer therapy and heart procedures, simply don’t have sufficiently large effects on nation-wide indicators of health outcomes (e.g., life expectancy at birth).

America, meanwhile, has long suffered from much worse behavioral and lifestyle risk factors. Obesity, homicides, and car accidents have long separated the United States from most other high-income countries. Differences of this sort may be trivial in comparison to the much more significant issues faced by most developing countries, but amongst developed countries, they loom very large indeed. Obesity alone sharply distinguishes America from its high-income counterparts and probably explains about half the gap. Substantially larger fractions of our population are suffering from extreme forms of morbid obesity, where the effects on mortality risk have been found to be unusually large.

While it is true that BMI has increased in most countries, developed and otherwise, they’ve grown at least as quickly for the United States, which implies somewhat more significant effects on life expectancy gaps.

The effects of primarily idiosyncratic external causes of death, such as homicide, car accidents, and drug overdoses, are quite simple to calculate from the data. Research published by CDC affiliated researchers has shown that accounting for these directly (arithmetically) explain between 30 and 50% of the gap, depending on the gender and reference group countries. These estimates are also pretty close to those provided by IHME with somewhat different methods.

If we add the obesity (metabolic) risks together with the risks (causes) from homicide, car accidents, and drug abuse, there’s very little left to explain.

Comparable results are also obtained for individual US states. Those states that see reduced life expectancy are well explained by their much higher risk factors (which are unlikely to be significantly attributable to lack of health care provision).

The development of health care technology matters in the long-run, but not so much amongst developed countries since they’re all spending on high efficacy treatments and most of the marginal expenditures are going (increasingly) to cutting edge treatments that tend to have small effects on mortality. Some incremental spending in more cutting edge treatments for cancer, cardiovascular, metabolic, and other major categories of diseases may help the afflicted to some extent. Still, the fraction of people treated multiplied by plausible effect sizes implies this activity is not likely to visibly move the needle when we look at nation-wide measures like life expectancy at birth, especially not in comparison to some of the previously enumerated causes of mortality that (mostly) vary idiosyncratically between countries. Amongst developed countries, lifestyle is the 800-pound gorilla in the room.

## Notes

(see below)

- 
- 
- 

